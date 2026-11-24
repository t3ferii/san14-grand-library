"""Deterministic local preparation and bounded queries. Python stdlib only, Windows x64.

No game process is started or attached to. Original files are only read.
"""
from __future__ import annotations

import argparse
import contextlib
import csv
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sqlite3
import struct
import subprocess
import sys
import time
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CACHE = Path(os.environ.get('LOCALAPPDATA', str(Path.home()))) / 'San14GrandLibrary'
EXE = 'SAN14CE_KO.exe'
TABLES = ('functions', 'calls', 'datarefs', 'strings', 'symbols', 'vtables', 'imports', 'import_refs', 'failures')
MAX_CELL = 16 * 1024 * 1024
csv.field_size_limit(MAX_CELL)


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def write_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + '.tmp')
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    tmp.replace(path)


def digest(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def require_hash(path, expected):
    if digest(path) != expected:
        raise ValueError(f'SHA256 mismatch: {path}')


def log(message):
    print(time.strftime('%H:%M:%S'), message, flush=True)


def cache_root(value=None):
    return Path(value or os.environ.get('SAN14_LIBRARY_CACHE') or DEFAULT_CACHE).resolve()


def discover_game(explicit=None):
    """Only Steam registry/libraryfolders/appmanifest locations; never a disk-wide scan."""
    if explicit or os.environ.get('SAN14_GAME'):
        path = Path(explicit or os.environ['SAN14_GAME']).expanduser().resolve()
        if not (path / EXE).is_file():
            raise ValueError(f'{EXE} not found in {path}')
        return path
    steam_roots = []
    if os.name == 'nt':
        import winreg
        for hive, key, field in (
            (winreg.HKEY_CURRENT_USER, r'Software\Valve\Steam', 'SteamPath'),
            (winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\WOW6432Node\Valve\Steam', 'InstallPath'),
        ):
            try:
                with winreg.OpenKey(hive, key) as k:
                    steam_roots.append(Path(winreg.QueryValueEx(k, field)[0]))
            except OSError:
                pass
    steam_roots.append(Path(os.environ.get('ProgramFiles(x86)', r'C:\Program Files (x86)')) / 'Steam')
    libraries = set(steam_roots)
    for base in steam_roots:
        folders = base / 'steamapps/libraryfolders.vdf'
        if folders.is_file():
            text = folders.read_text(encoding='utf-8-sig')
            libraries.update(Path(p.replace('\\\\', '\\')) for p in re.findall(r'"path"\s*"([^"]+)"', text))
    found = set()
    for base in libraries:
        manifest = base / 'steamapps/appmanifest_872410.acf'
        if not manifest.is_file():
            continue
        match = re.search(r'"installdir"\s*"([^"]+)"', manifest.read_text(encoding='utf-8-sig'))
        if match:
            path = (base / 'steamapps/common' / match[1]).resolve()
            if (path / EXE).is_file():
                found.add(path)
    if len(found) != 1:
        raise ValueError(f'Expected one CE KO installation, found {len(found)}. Use -GamePath / --game.')
    return found.pop()


def installed_build(game):
    p = game.parent.parent / 'appmanifest_872410.acf'
    if not p.is_file():
        return None
    m = re.search(r'"buildid"\s*"(\d+)"', p.read_text(encoding='utf-8-sig'))
    return m[1] if m else None


def check_paths(cache, game):
    """The private workspace must be outside the install and the published checkout."""
    for protected in (game, ROOT):
        if cache == protected or protected in cache.parents:
            raise ValueError(f'Cache must be outside {protected}')
    if os.name == 'nt' and any(c in str(cache) for c in '()!%&^'):
        raise ValueError('Ghidra batch path cannot contain ()!%&^. Select another --cache-root.')


@contextlib.contextmanager
def job_lock(cache):
    cache.mkdir(parents=True, exist_ok=True)
    # OS releases this lock if the job is interrupted. The persistent file is harmless.
    with (cache / 'prepare.lock').open('a+b') as f:
        f.seek(0)
        if os.name == 'nt':
            import msvcrt
            if f.read(1) == b'':
                f.write(b'0'); f.flush()
            f.seek(0)
            try:
                msvcrt.locking(f.fileno(), msvcrt.LK_NBLCK, 1)
            except OSError as e:
                raise RuntimeError('Another preparation job is using this cache.') from e
        else:
            import fcntl
            fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
        try:
            yield
        finally:
            if os.name == 'nt':
                f.seek(0); msvcrt.locking(f.fileno(), msvcrt.LK_UNLCK, 1)


def safe_extract(archive, dest):
    dest = Path(dest).resolve()
    with zipfile.ZipFile(archive) as z:
        for member in z.infolist():
            target = (dest / member.filename).resolve()
            if target != dest and dest not in target.parents:
                raise ValueError(f'Unsafe ZIP member: {member.filename}')
            if (member.external_attr >> 16) & 0o170000 == 0o120000:
                raise ValueError('ZIP symlinks are not accepted')
        z.extractall(dest)


def download(url, path, expected):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.is_file() and digest(path) == expected:
        log(f'[cached] archive {path.name}')
        return
    tmp = path.with_suffix(path.suffix + '.part')
    log(f'Downloading {path.name}')
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'San14GrandLibrary/1'}), timeout=60) as response, tmp.open('wb') as out:
                shutil.copyfileobj(response, out, 1024 * 1024)
            require_hash(tmp, expected)
            tmp.replace(path)
            return
        except (OSError, ValueError):
            if attempt == 2:
                raise
            log('Download failed; retrying from the beginning.')


def inventory(directory):
    return {p.relative_to(directory).as_posix(): digest(p) for p in sorted(directory.rglob('*')) if p.is_file() and p.name != '.verified.json'}


def install_tool(name, spec, cache):
    dest = cache / 'tools' / f"{name}-{spec['version']}"
    proof = dest / '.verified.json'
    if proof.is_file():
        saved = read_json(proof)
        if saved.get('archive_sha256') == spec['sha256'] and saved.get('files') == inventory(dest):
            log(f'[cached] verified {name} {spec["version"]}')
            return dest
        raise ValueError(f'Tool files changed: {dest}. Select a new cache root or inspect this tool directory.')
    archive = cache / 'downloads' / f'{name}.zip'
    download(spec['url'], archive, spec['sha256'])
    safe_extract(archive, dest)
    write_json(proof, {'archive_sha256': spec['sha256'], 'files': inventory(dest)})
    return dest


def find_one(directory, suffix):
    found = list(directory.rglob(suffix))
    if len(found) != 1:
        raise ValueError(f'Expected exactly one {suffix} in {directory}, got {len(found)}')
    return found[0]


def run(command, logfile, env=None, cwd=None):
    log(f'Running {Path(command[0]).name}; log: {logfile}')
    # No shell string interpolation. Never run the game EXE; only the three tool entrypoints.
    with logfile.open('w', encoding='utf-8') as f:
        p = subprocess.Popen([str(x) for x in command], stdout=f, stderr=subprocess.STDOUT, env=env, cwd=cwd)
        while True:
            try:
                code = p.wait(timeout=30)
                break
            except subprocess.TimeoutExpired:
                log(f'Still working (PID {p.pid}); detailed progress is in {logfile.name}')
            except KeyboardInterrupt:
                # Kill only our tool process and its descendants, never a game process by name.
                if os.name == 'nt':
                    subprocess.run(['taskkill', '/PID', str(p.pid), '/T', '/F'], capture_output=True)
                else:
                    p.terminate()
                p.wait()
                raise
    if code:
        raise RuntimeError(f'Tool exited {code}; see {logfile}')
    text = logfile.read_text(encoding='utf-8', errors='replace')
    if re.search(r'SCRIPT ERROR|Error running script|ERROR REPORT:|Exception in thread', text):
        raise RuntimeError(f'Tool reported errors; see {logfile}')
    return text


def export_files(export):
    return sorted([export / 'manifest.json', *export.glob('*.tsv'), *export.glob('c/*.c')])


def source_signature(export):
    return hashlib.sha256(json.dumps([(p.relative_to(export).as_posix(), p.stat().st_size, p.stat().st_mtime_ns) for p in export_files(export)]).encode()).hexdigest()


def validate_export(export, expected):
    m = read_json(export / 'manifest.json')
    if m.get('status') != 'complete' or m.get('sha256') != expected:
        raise ValueError(f'Export is incomplete or for a different executable: {export}')
    for table in TABLES:
        if not (export / f'{table}.tsv').is_file():
            raise ValueError(f'Missing export table: {table}')
    if not list(export.glob('c/*.c')):
        raise ValueError('No decompiled shards')
    return m


def make_index(export):
    """Index TSV metadata and shard positions, not a second copy of all function bodies."""
    sig = source_signature(export)
    dest = export / 'index.sqlite'
    if dest.is_file():
        with contextlib.closing(sqlite3.connect(dest)) as c:
            try:
                if c.execute("select value from meta where key='signature'").fetchone() == (sig,):
                    log('[cached] search index'); return
            except sqlite3.Error:
                pass
    tmp = export / 'index.sqlite.tmp'
    if tmp.exists():
        tmp.unlink()
    with contextlib.closing(sqlite3.connect(tmp)) as con:
        con.execute('pragma journal_mode=OFF')
        con.execute('create table meta(key text primary key, value text)')
        con.execute('insert into meta values(?,?)', ('signature', sig))
        for table in TABLES:
            with (export / f'{table}.tsv').open(encoding='utf-8', newline='') as f:
                rows = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
                cols = next(rows)
                if not all(re.fullmatch(r'[a-z_]+', x) for x in cols):
                    raise ValueError(f'Invalid TSV header: {table}')
                con.execute(f'create table "{table}" ({",".join(chr(34)+x+chr(34)+" text" for x in cols)})')
                con.executemany(f'insert into "{table}" values({",".join("?" for _ in cols)})', rows)
        con.execute('create index function_rva on functions(rva)')
        con.execute('create index caller on calls(caller_func_rva)')
        con.execute('create index callee on calls(callee_rva)')
        con.execute('create index data_target on datarefs(to_rva)')
        con.execute('create table bodies(rva text primary key, shard text, offset integer, length integer)')
        for shard in sorted(export.glob('c/*.c')):
            with shard.open('rb') as f:
                previous = None
                while True:
                    offset = f.tell(); line = f.readline()
                    if line.startswith(b'// ==== FUNC ') or not line:
                        if previous:
                            con.execute('insert into bodies values(?,?,?,?)', (*previous, offset - previous[2]))
                        if not line:
                            break
                        previous = (line.split()[3].decode(), shard.relative_to(export).as_posix(), offset)
        con.commit()
    tmp.replace(dest)
    log('Search index ready')


def verify(export, expected, samples):
    m = validate_export(export, expected)
    if not (export / 'index.sqlite').is_file():
        raise ValueError('Index missing')
    with contextlib.closing(sqlite3.connect(export / 'index.sqlite')) as con:
        if con.execute('pragma quick_check').fetchone()[0] != 'ok':
            raise ValueError('SQLite integrity failure')
        if con.execute("select value from meta where key='signature'").fetchone() != (source_signature(export),):
            raise ValueError('Index is stale')
        for table in TABLES:
            count = con.execute(f'select count(*) from "{table}"').fetchone()[0]
            declared = m.get('counts', {}).get(table + '.tsv')
            if declared is not None and count != declared:
                raise ValueError(f'{table} count mismatch: {count} != {declared}')
        n = con.execute('select count(*) from functions').fetchone()[0]
        if n == 0 or con.execute('select count(*) from bodies').fetchone()[0] != n:
            raise ValueError('Function body index is incomplete')
        for address in samples:
            rva = f'{int(address, 16):08X}'
            function = con.execute('select rva from functions where rva<=? and "end">=? order by rva desc limit 1', (rva, rva)).fetchone()
            row = con.execute('select shard,offset,length from bodies where rva=?', function).fetchone() if function else None
            if not row:
                raise ValueError(f'Sample function missing: {rva}')
            with (export / row[0]).open('rb') as f:
                f.seek(row[1]); body = f.read(row[2])
            if not body.startswith(b'// ==== FUNC ' + function[0].encode() + b' ') or b'DECOMPILE_FAILED' in body:
                raise ValueError(f'Sample function failed decompilation: {rva}')
        failures = con.execute('select count(*) from failures').fetchone()[0]
    return {'functions': n, 'decompile_failures': failures, 'sample_rvas': samples,
            'status': 'ready_with_decompile_failures' if failures else 'ready'}


def prepare(args):
    if os.name != 'nt':
        raise ValueError('Preparation currently supports Windows x64 only.')
    cache = cache_root(args.cache_root)
    game = discover_game(args.game)
    check_paths(cache, game)
    builds = read_json(ROOT / 'tools/builds.json')
    packed_hash = digest(game / EXE)
    candidates = [(bid, b) for bid, b in builds['builds'].items() if b['packed_sha256'] == packed_hash]
    if not candidates:
        raise ValueError(f'Unsupported CE KO EXE SHA256 {packed_hash}; no analysis started. Report build {installed_build(game)} and this hash in an issue.')
    bid, build = candidates[0]
    if installed_build(game) not in (None, bid):
        raise ValueError('Steam manifest build differs from EXE profile; finish Steam update first.')
    log(f'Found CE KO build {bid}; original SHA256 verified')
    if args.doctor:
        print(json.dumps({'game': str(game), 'build': bid, 'packed_sha256': packed_hash,
                          'cache': str(cache), 'free_gib': round(shutil.disk_usage(cache.anchor).free / 2**30, 1)}, indent=2))
        return
    expected = build['unpacked_sha256']
    workspace = cache / 'builds' / expected[:16]
    export = workspace / 'export'
    lock = read_json(ROOT / 'tools/dependencies.lock.json')
    scripts = ROOT / 'tools/ghidra_scripts'
    recipe = hashlib.sha256((json.dumps(lock, sort_keys=True) + json.dumps(build, sort_keys=True) +
                            digest(Path(__file__)) + ''.join(digest(x) for x in sorted(scripts.glob('*.java')))).encode()).hexdigest()
    with job_lock(cache):
        workspace.mkdir(parents=True, exist_ok=True)
        proof = workspace / 'ready.json'
        if args.verify_only or (proof.is_file() and read_json(proof).get('recipe') == recipe):
            require_hash(workspace / 'input/game.exe.unpacked.exe', expected)
            result = verify(export, expected, build['smoke_rvas'])
            print(json.dumps(result, indent=2)); log('[cached] ready; no download or analysis needed')
            return
        if shutil.disk_usage(cache).free < 8 * 2**30:
            raise ValueError('At least 8 GiB free disk space required for tools, analysis and cache.')
        # Check for host .NET 4.x before downloading larger packages (Steamless requirement).
        import winreg
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full') as k:
                if winreg.QueryValueEx(k, 'Release')[0] < 461808:
                    raise OSError('old .NET')
        except OSError as e:
            raise ValueError('.NET Framework 4.7.2+ required. Windows 10/11 normally include it; complete Windows Update first.') from e
        steamless = install_tool('steamless', lock['steamless'], cache)
        inp = workspace / 'input'; inp.mkdir(exist_ok=True)
        original = inp / 'game.exe'
        if not original.exists():
            shutil.copyfile(game / EXE, original)
        require_hash(original, packed_hash)
        plain = inp / 'game.exe.unpacked.exe'
        if not plain.exists():
            run([find_one(steamless, 'Steamless.CLI.exe'), *build['steamless_args'], original], workspace / 'unpack.log', cwd=steamless)
        require_hash(plain, expected)
        require_hash(game / EXE, packed_hash)
        log('Unpacked working copy matches the library reference SHA256 exactly')
        if args.reuse_export:
            source = Path(args.reuse_export).resolve()
            validate_export(source, expected)
            if (export / 'manifest.json').is_file() and read_json(export / 'manifest.json').get('sha256') != expected:
                raise ValueError('Existing export is for another executable; select a new cache root.')
            export.mkdir(exist_ok=True)
            # Copy the completion manifest last; retry safely after an interrupted copy.
            items = export_files(source)
            items.sort(key=lambda x: x.name == 'manifest.json')
            for item in items:
                dest = export / item.relative_to(source)
                dest.parent.mkdir(parents=True, exist_ok=True)
                if item != dest and (not dest.is_file() or digest(dest) != digest(item)):
                    shutil.copy2(item, dest)
        else:
            java = install_tool('java', lock['java'], cache)
            ghidra = install_tool('ghidra', lock['ghidra'], cache)
            java_exe = find_one(java, 'java.exe')
            launcher = find_one(ghidra, 'analyzeHeadless.bat')
            env = dict(os.environ, JAVA_HOME=str(java_exe.parent.parent), GHIDRA_HEADLESS_MAXMEM='4G')
            # Batch launchers cannot reliably receive shell metacharacters. Only staged, controlled paths enter this call.
            script_hash = hashlib.sha256(''.join(digest(x) for x in sorted(scripts.glob('*.java'))).encode()).hexdigest()[:16]
            staged = cache / 'scripts' / script_hash
            staged.mkdir(parents=True, exist_ok=True)
            for source in scripts.glob('*.java'):
                target = staged / source.name
                if not target.exists(): shutil.copy2(source, target)
                require_hash(target, digest(source))
            project = workspace / 'project'; project.mkdir(exist_ok=True)
            common = [launcher, project, 'SAN14CE_KO', '-max-cpu', str(min(4, os.cpu_count() or 1)), '-scriptPath', staged]
            certified = workspace / 'analysis/analysis_report.json'
            if not certified.is_file():
                mode = ['-process', plain.name] if (project / 'SAN14CE_KO.gpr').exists() else ['-import', plain]
                run([*common, *mode, '-postScript', 'San14AnalysisReport.java', workspace / 'analysis', expected], workspace / 'analysis.log', env)
            report = read_json(certified)
            if report.get('sha256') != expected or report.get('functions', 0) == 0 or report.get('analysis_timeout') is not False:
                raise ValueError('Analysis completion report failed validation')
            # Resume completed shards; restart an interrupted shard. This read does not rerun auto-analysis.
            run([*common, '-process', plain.name, '-noanalysis', '-readOnly', '-postScript',
                 'San14FullExport.java', export, expected], workspace / 'export.log', env)
        make_index(export)
        result = verify(export, expected, build['smoke_rvas'])
        write_json(proof, {**result, 'recipe': recipe, 'build': bid, 'packed_sha256': packed_hash,
                           'sha256': expected, 'created_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                           'reused_export': bool(args.reuse_export), 'tools': lock})
        require_hash(game / EXE, packed_hash)
        print(json.dumps(result, indent=2))
        log(f'Ready. Private cache: {export}')


def rva(value):
    n = int(value, 16)
    return n - 0x140000000 if n >= 0x140000000 else n


def select_export(cache, build=None):
    builds = read_json(ROOT / 'tools/builds.json')
    profile = builds['builds'][build or builds['default']]
    path = cache / 'builds' / profile['unpacked_sha256'][:16] / 'export'
    validate_export(path, profile['unpacked_sha256'])
    return path


def pe_bytes(path, address, length):
    if not 1 <= length <= 256:
        raise ValueError('Byte length must be between 1 and 256')
    with Path(path).open('rb') as f:
        if f.read(2) != b'MZ': raise ValueError('Not a PE')
        f.seek(60); pe = struct.unpack('<I', f.read(4))[0]
        f.seek(pe)
        if f.read(4) != b'PE\0\0': raise ValueError('Bad PE signature')
        f.seek(pe + 6); count = struct.unpack('<H', f.read(2))[0]
        f.seek(pe + 20); opt = struct.unpack('<H', f.read(2))[0]
        for i in range(count):
            f.seek(pe + 24 + opt + 40 * i + 8)
            vs, va, raw_size, raw_off = struct.unpack('<4I', f.read(16))
            if va <= address and address + length <= va + raw_size:
                f.seek(raw_off + address - va)
                return f.read(length).hex(' ')
    raise ValueError('RVA is outside file-backed PE sections')


def query(args):
    export = select_export(cache_root(args.cache_root), args.build)
    if args.command == 'status':
        print(json.dumps(read_json(export.parent / 'ready.json'), ensure_ascii=False, indent=2)); return
    uri = (export / 'index.sqlite').as_uri() + '?mode=ro'
    with contextlib.closing(sqlite3.connect(uri, uri=True)) as con:
        if con.execute("select value from meta where key='signature'").fetchone() != (source_signature(export),):
            raise ValueError('Index is stale. Run prepare.ps1 again.')
        if args.command == 'func':
            n = rva(args.value)
            row = con.execute('select rva from functions where rva<=? and "end">=? order by rva desc limit 1', (f'{n:08X}', f'{n:08X}')).fetchone()
            if not row: raise ValueError('Function not found')
            record = con.execute('select shard,offset,length from bodies where rva=?', row).fetchone()
            with (export / record[0]).open('rb') as f:
                f.seek(record[1]); lines = f.read(record[2]).decode('utf-8').splitlines()
            print('\n'.join(lines[:args.limit]))
            if len(lines) > args.limit: print(f'... {len(lines)-args.limit} more lines; increase --limit')
            return
        if args.command == 'bytes':
            expected = read_json(export / 'manifest.json')['sha256']
            plain = export.parent / 'input/game.exe.unpacked.exe'
            require_hash(plain, expected)
            print(pe_bytes(plain, rva(args.value), args.length)); return
        table, field = {'callers': ('calls', 'callee_rva'), 'callees': ('calls', 'caller_func_rva'),
                        'xref': ('datarefs', 'to_rva'), 'str': ('strings', 'text'),
                        'vtable': ('vtables', 'vftable_rva'), 'find': ('functions', 'name')}[args.command] if args.command != 'grep' else (None, None)
        if args.command == 'grep':
            # Literal, bounded scan; never dump the whole cache into an AI context.
            needle = args.value.casefold(); count = 0
            for p in sorted(export.glob('c/*.c')):
                with p.open(encoding='utf-8') as f:
                    function = ''
                    for line_no, line in enumerate(f, 1):
                        if line.startswith('// ==== FUNC '): function = line.split()[3]
                        if needle in line.casefold():
                            print(f'{function} {p.name}:{line_no}: {line.rstrip()}'); count += 1
                            if count >= args.limit: return
            return
        text_search = args.command in ('str', 'find')
        value = args.value if text_search else f'{rva(args.value):08X}'
        if args.command in ('callers', 'callees'):
            function = con.execute('select rva from functions where rva<=? and "end">=? order by rva desc limit 1', (value, value)).fetchone()
            if function and function[0] != value:
                print(f'# {value} belongs to function {function[0]}')
                value = function[0]
        sql = f'select * from "{table}" where "{field}" {"like" if text_search else "="} ? limit ?'
        cursor = con.execute(sql, (f'%{value}%' if text_search else value, args.limit))
        print('\t'.join(x[0] for x in cursor.description))
        for row in cursor: print('\t'.join(str(x) for x in row))


def data_query(args):
    os.environ['SAN14_GAME'] = str(discover_game(args.game))
    sys.path.insert(0, str(ROOT))
    from origlib.cli import main as orig_main
    values = list(args.arguments)
    if (len(values) == 2 and values[0] == 'table') or (len(values) == 3 and values[0] == 'scenario'):
        values.append('20')
        print('Showing first 20 rows by default; supply an explicit row count for more.', file=sys.stderr)
    return orig_main(values)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    p = commands.add_parser('prepare')
    p.add_argument('--game'); p.add_argument('--doctor', action='store_true'); p.add_argument('--verify-only', action='store_true')
    p.add_argument('--reuse-export', help='Advanced: verified local export of the exact same SHA256; never a download')
    d = commands.add_parser('data')
    d.add_argument('--game'); d.add_argument('--cache-root')
    d.add_argument('arguments', nargs=argparse.REMAINDER)
    compat = commands.add_parser('compat')
    compat.add_argument('--cache-root')
    compat.add_argument('arguments', nargs=argparse.REMAINDER)
    for name in ('status', 'func', 'callers', 'callees', 'xref', 'str', 'vtable', 'find', 'grep', 'bytes'):
        q = commands.add_parser(name)
        if name != 'status': q.add_argument('value')
        q.add_argument('--limit', type=int, default=120)
        if name == 'bytes': q.add_argument('--length', type=int, default=32)
        q.add_argument('--build')
    for sub in [p, *[x for k, x in commands.choices.items() if k not in ('prepare', 'data', 'compat')]]:
        sub.add_argument('--cache-root')
    args = parser.parse_args(argv)
    if hasattr(args, 'limit') and not 1 <= args.limit <= 10000: parser.error('--limit must be 1..10000')
    try:
        if args.command == 'data': return data_query(args)
        if args.command == 'compat':
            sys.path.insert(0, str(ROOT / 'tools'))
            import mod_compat
            sys.argv = ['mod_compat.py', *args.arguments]
            return mod_compat.main()
        prepare(args) if args.command == 'prepare' else query(args)
        return 0
    except (OSError, ValueError, RuntimeError, KeyError, sqlite3.Error, zipfile.BadZipFile) as e:
        print(f'ERROR: {e}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
