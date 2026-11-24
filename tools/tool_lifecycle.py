"""Track only artifacts created by preparation; never uninstall borrowed tools."""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil


def digest(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''): h.update(block)
    return h.hexdigest()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + '.tmp')
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    tmp.replace(path)


def marker(cache, relative):
    key = hashlib.sha256(relative.encode()).hexdigest()
    return Path(cache) / '.owned' / (key + '.json')


def safe_path(cache, record):
    cache = Path(cache).resolve()
    relative = record['relative']
    p = PurePosixPath(relative)
    if p.is_absolute() or '..' in p.parts or '\\' in relative or ':' in relative:
        raise ValueError('Unsafe ownership path')
    kind, name = record['kind'], record['name']
    if kind == 'tool' and name in ('java', 'ghidra', 'steamless'):
        version = record['version']
        if not re.fullmatch(r'[A-Za-z0-9.+_-]+', version) or relative != f'tools/{name}-{version}':
            raise ValueError('Unexpected owned tool path')
    elif kind == 'archive' and name in ('python', 'java', 'ghidra', 'steamless'):
        if relative != f'downloads/{name}.zip': raise ValueError('Unexpected archive path')
    elif kind == 'source_archive' and name == 'source':
        if not re.fullmatch(r'downloads/source-[0-9a-f]{32}\.zip', relative):
            raise ValueError('Unexpected source archive path')
    else:
        raise ValueError('Artifact is outside cleanup allowlist')
    if os.path.normcase(str(cache)) != os.path.normcase(record['cache_root']):
        raise ValueError('Ownership belongs to another cache root')
    path = cache / relative
    if path.resolve() != cache and cache not in path.resolve().parents:
        raise ValueError('Owned artifact escapes cache')
    for ancestor in (path, *path.parents):
        if ancestor == cache: break
        if is_link(ancestor): raise ValueError('Ownership path contains a reparse point')
    return path


def is_link(path):
    try:
        stat = path.lstat()
        return path.is_symlink() or bool(getattr(stat, 'st_file_attributes', 0) & 0x400)
    except FileNotFoundError:
        return False


def check_tree(path):
    if is_link(path): raise ValueError('Tool directory is a reparse point')
    for folder, dirs, files in os.walk(path, followlinks=False):
        for name in dirs + files:
            if is_link(Path(folder) / name): raise ValueError('Tool contains a reparse point')


def owned(cache, relative):
    m = marker(cache, relative)
    if not m.is_file() or is_link(m): return None
    data = json.loads(m.read_text(encoding='utf-8-sig'))
    safe_path(cache, data)
    if data.get('schema') != 1 or data['relative'] != relative: raise ValueError('Invalid ownership record')
    return data


def record_created(cache, relative, kind, name, version='', sha256=''):
    """Must be called before creating an absent artifact. Existing files are not adopted."""
    data = {'schema': 1, 'cache_root': str(Path(cache).resolve()), 'relative': relative,
            'kind': kind, 'name': name, 'version': version, 'sha256': sha256}
    path = safe_path(cache, data)
    previous = owned(cache, relative)
    if previous:
        if any(previous[k] != data[k] for k in ('kind', 'name', 'version', 'sha256')):
            raise ValueError('Ownership recipe changed; use a new cache root')
        return True
    if path.exists() or is_link(path): return False
    if is_link(Path(cache) / '.owned'): raise ValueError('Ownership directory is a reparse point')
    write_json(marker(cache, relative), data)
    return True


def finish_tool(cache, relative):
    data = owned(cache, relative)
    if data:
        path = safe_path(cache, data)
        data['proof_sha256'] = digest(path / '.verified.json')
        write_json(marker(cache, relative), data)


def inventory(path):
    check_tree(path)
    return {p.relative_to(path).as_posix(): digest(p) for p in sorted(path.rglob('*'))
            if p.is_file() and p != path / '.verified.json'}


def record_reused(cache, name, path):
    dest = Path(cache) / 'reused-tools.json'
    data = json.loads(dest.read_text(encoding='utf-8')) if dest.is_file() else {}
    data[name] = str(Path(path).resolve())
    write_json(dest, data)


def cleanup(cache):
    """Called only after cache verification. Modified/unproven artifacts are preserved."""
    cache = Path(cache).resolve()
    report = {'removed': [], 'preserved': [], 'errors': []}
    records = cache / '.owned'
    if is_link(records):
        report['errors'].append('Ownership directory is a reparse point')
        return report
    for m in sorted(records.glob('*.json')):
        label = m.name
        try:
            if is_link(m): raise ValueError('Ownership record is a symlink')
            data = json.loads(m.read_text(encoding='utf-8-sig'))
            label = data.get('relative', label)
            if data.get('schema') != 1 or marker(cache, label) != m:
                raise ValueError('Invalid ownership identity')
            path = safe_path(cache, data)
            if not path.exists():
                m.unlink(); continue
            if data['kind'] == 'tool':
                if not path.is_dir(): raise ValueError('Expected a tool directory')
                check_tree(path)
                proof = path / '.verified.json'
                if not data.get('proof_sha256') or not proof.is_file() or digest(proof) != data['proof_sha256']:
                    raise ValueError('Incomplete or modified installation; preserved')
                saved = json.loads(proof.read_text(encoding='utf-8'))
                if saved.get('files') != inventory(path) or saved.get('archive_sha256') != data['sha256']:
                    raise ValueError('Tool files changed; preserved')
                shutil.rmtree(path)
            else:
                if not path.is_file() or digest(path) != data['sha256']:
                    raise ValueError('Archive changed; preserved')
                path.unlink()
            m.unlink()
            report['removed'].append(label)
        except (ValueError, KeyError, TypeError, RuntimeError) as e:
            report['preserved'].append({'path': label, 'reason': str(e)})
        except OSError as e:
            report['errors'].append({'path': label, 'reason': str(e)})
    write_json(cache / 'cleanup-report.json', report)
    return report
