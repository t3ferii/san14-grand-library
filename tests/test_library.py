"""Synthetic regression tests: no copyrighted fixture or game binary."""
import contextlib
import copy
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import library as lib
import mod_compat as compat

HASH = 'a' * 64


def synthetic_export(folder, failures=False):
    folder.mkdir(parents=True, exist_ok=True)
    (folder / 'c').mkdir()
    tables = {
        'functions': 'rva\tend\tsize\tname\tshard\tline\tparameters\tsignature\tthunk\n00001000\t0000100F\t16\tfirst\tc/0000.c\t1\t0\tvoid first()\tfalse\n00002000\t0000200F\t16\tsecond\tc/0000.c\t3\t0\tvoid second()\tfalse\n',
        'calls': 'caller_func_rva\tcallsite_rva\tcallee_rva\tkind\n00001000\t00001002\t00002000\tdirect\n',
        'datarefs': 'from_rva\tfrom_func_rva\tto_rva\tref_type\n00001002\t00001000\t00003000\tREAD\n',
        'strings': 'rva\tencoding\ttext\tref_functions\n00003000\tunicode\tsynthetic\t00001000\n',
        'symbols': 'rva\tname\tkind\n00001000\tfirst\tFunction\n',
        'vtables': 'vftable_rva\tclass\tslot\ttarget_rva\tcode_refs\tfirst_ref_func\n00004000\tSynthetic\t0\t00001000\t1\t00002000\n',
        'imports': 'dll\tfunction\tiat_rva\nsynthetic.dll\tsynthetic\t00005000\n',
        'import_refs': 'from_rva\tfrom_func_rva\tdll\tfunction\n00001003\t00001000\tsynthetic.dll\tsynthetic\n',
        'failures': 'rva\treason\n' + ('00002000\tsynthetic timeout\n' if failures else ''),
    }
    for name, text in tables.items(): (folder / f'{name}.tsv').write_text(text, encoding='utf-8')
    (folder / 'c/0000.c').write_text('// ==== FUNC 00001000 first size=16 end=0000100F\nvoid first() {}\n// ==== FUNC 00002000 second size=16 end=0000200F\n' + ('// DECOMPILE_FAILED timeout\n' if failures else 'void second() {}\n'), encoding='utf-8')
    lib.write_json(folder / 'manifest.json', {'status': 'complete', 'sha256': HASH,
                   'counts': {k + '.tsv': len(v.splitlines())-1 for k, v in tables.items()}})


class CacheTests(unittest.TestCase):
    def test_concurrent_preparation_is_rejected_and_lock_released(self):
        with tempfile.TemporaryDirectory() as tmp:
            cache = Path(tmp)
            with lib.job_lock(cache):
                with self.assertRaisesRegex(RuntimeError, 'Another preparation'):
                    with lib.job_lock(cache): self.fail('Concurrent preparation must not proceed')
            with lib.job_lock(cache): pass

    @unittest.skipUnless(os.name == 'nt', 'Windows preparation pipeline')
    def test_preparation_pipeline_preserves_original_and_reuses_cache(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp); game = base / 'game'; game.mkdir()
            original = game / lib.EXE; original.write_bytes(b'synthetic packed fixture')
            packed, plain = lib.digest(original), __import__('hashlib').sha256(b'synthetic plain fixture').hexdigest()
            profile = {'packed_sha256': packed, 'unpacked_sha256': plain, 'steamless_args': [], 'smoke_rvas': ['1000']}
            fixture_root = base / 'repo'; (fixture_root / 'tools/ghidra_scripts').mkdir(parents=True)
            (fixture_root / 'tools/builds.json').write_text(json.dumps({'default':'test','builds':{'test':profile}}))
            (fixture_root / 'tools/dependencies.lock.json').write_text(json.dumps({x:{'version':'1','sha256':HASH,'url':'https://invalid.example'} for x in ('steamless','java','ghidra')}))
            staged = base / 'tool'; staged.mkdir()
            (staged / 'Steamless.CLI.exe').touch(); (staged / 'analyzeHeadless.bat').touch()
            (staged / 'bin').mkdir(); (staged / 'bin/java.exe').touch()
            cache = base / 'cache'; invocations = []
            def fake_run(command, logfile, env=None, cwd=None):
                invocations.append(list(map(str, command)))
                workspace = cache / 'builds' / plain[:16]
                if str(command[0]).endswith('Steamless.CLI.exe'):
                    (workspace / 'input/game.exe.unpacked.exe').write_bytes(b'synthetic plain fixture')
                elif 'San14AnalysisReport.java' in command:
                    (workspace / 'project/SAN14CE_KO.gpr').touch()
                    lib.write_json(workspace / 'analysis/analysis_report.json', {'sha256':plain, 'functions':2, 'analysis_timeout':False})
                else:
                    synthetic_export(workspace / 'export')
                    m = lib.read_json(workspace / 'export/manifest.json'); m['sha256'] = plain
                    lib.write_json(workspace / 'export/manifest.json', m)
                return ''
            # Steamless/.NET host is Windows; tools and all input files here are synthetic.
            with mock.patch.object(lib, 'ROOT', fixture_root), mock.patch.object(lib, 'install_tool', return_value=staged), mock.patch.object(lib, 'run', side_effect=fake_run):
                self.assertEqual(lib.main(['prepare','--game',str(game),'--cache-root',str(cache)]), 0)
                self.assertEqual(len(invocations), 3)
                self.assertEqual(original.read_bytes(), b'synthetic packed fixture')
                self.assertEqual(lib.main(['prepare','--game',str(game),'--cache-root',str(cache)]), 0)
                self.assertEqual(len(invocations), 3, 'Second preparation must not run tools')

    def test_index_queries_and_reuse(self):
        with tempfile.TemporaryDirectory() as tmp:
            export = Path(tmp) / 'export'; synthetic_export(export)
            lib.make_index(export)
            self.assertEqual(lib.verify(export, HASH, ['1000'])['functions'], 2)
            self.assertEqual(lib.verify(export, HASH, ['1002'])['functions'], 2, 'Interior RVA must resolve to its containing function')
            before = (export / 'index.sqlite').stat().st_mtime_ns
            lib.make_index(export)
            self.assertEqual((export / 'index.sqlite').stat().st_mtime_ns, before)
            with mock.patch.object(lib, 'select_export', return_value=export):
                for cmd, value, expected in [('func', '1002', 'void first()'), ('callers', '2000', '00001000'), ('callers', '2002', '00001000'), ('callees', '1000', '00002000'), ('callees', '1002', '00002000'), ('xref', '3000', 'READ'), ('str', 'synthetic', 'unicode'), ('vtable', '4000', 'Synthetic'), ('find', 'first', '00001000'), ('grep', 'second', '00002000')]:
                    output = io.StringIO()
                    with contextlib.redirect_stdout(output): self.assertEqual(lib.main([cmd, value]), 0)
                    self.assertIn(expected, output.getvalue())

    def test_stale_cache_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            export = Path(tmp) / 'export'; synthetic_export(export); lib.make_index(export)
            with (export / 'strings.tsv').open('a') as f: f.write('00006000\tascii\tchanged\t\n')
            with self.assertRaisesRegex(ValueError, 'stale'): lib.verify(export, HASH, ['1000'])

    def test_partial_and_wrong_build_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            export = Path(tmp); synthetic_export(export)
            with self.assertRaisesRegex(ValueError, 'different executable'): lib.validate_export(export, 'b'*64)
            m = lib.read_json(export / 'manifest.json'); m['status'] = 'partial'; lib.write_json(export / 'manifest.json', m)
            with self.assertRaisesRegex(ValueError, 'incomplete'): lib.validate_export(export, HASH)

    def test_failures_are_not_silent_success(self):
        with tempfile.TemporaryDirectory() as tmp:
            export = Path(tmp); synthetic_export(export, True); lib.make_index(export)
            result = lib.verify(export, HASH, ['1000'])
            self.assertEqual(result['status'], 'ready_with_decompile_failures')
            self.assertEqual(result['decompile_failures'], 1)
            with self.assertRaisesRegex(ValueError, 'failed decompilation'): lib.verify(export, HASH, ['2000'])

    def test_tsv_count_mismatch_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            export = Path(tmp); synthetic_export(export)
            m = lib.read_json(export / 'manifest.json'); m['counts']['calls.tsv'] = 99; lib.write_json(export / 'manifest.json', m)
            lib.make_index(export)
            with self.assertRaisesRegex(ValueError, 'count mismatch'): lib.verify(export, HASH, ['1000'])

    def test_zip_traversal_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            archive = Path(tmp) / 'bad.zip'
            with zipfile.ZipFile(archive, 'w') as z: z.writestr('../outside.txt', 'no')
            with self.assertRaisesRegex(ValueError, 'Unsafe'): lib.safe_extract(archive, Path(tmp) / 'safe')
            self.assertFalse((Path(tmp) / 'outside.txt').exists())

    def test_download_checksum_and_cached_archive(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'tool.zip'
            payload = b'synthetic download'
            expected = __import__('hashlib').sha256(payload).hexdigest()
            with mock.patch.object(lib.urllib.request, 'urlopen', return_value=io.BytesIO(payload)) as fetch:
                lib.download('https://invalid.example/tool.zip', target, expected)
                self.assertEqual(target.read_bytes(), payload)
                lib.download('https://invalid.example/tool.zip', target, expected)
                self.assertEqual(fetch.call_count, 1)

    def test_bad_download_is_never_promoted(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'tool.zip'
            with mock.patch.object(lib.urllib.request, 'urlopen', side_effect=lambda *a, **k: io.BytesIO(b'wrong fixture')):
                with self.assertRaisesRegex(ValueError, 'SHA256 mismatch'):
                    lib.download('https://invalid.example/tool.zip', target, HASH)
            self.assertFalse(target.exists())

    def test_tools_are_verified_before_reuse(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp); dest = base / 'tools/test-1'; dest.mkdir(parents=True)
            (dest / 'tool.txt').write_text('original')
            spec = {'version': '1', 'sha256': HASH, 'url': 'https://invalid.example/tool.zip'}
            lib.write_json(dest / '.verified.json', {'archive_sha256': HASH, 'files': lib.inventory(dest)})
            self.assertEqual(lib.install_tool('test', spec, base), dest)
            (dest / 'tool.txt').write_text('changed')
            with self.assertRaisesRegex(ValueError, 'Tool files changed'): lib.install_tool('test', spec, base)

    def test_original_and_checkout_cache_locations_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            game = Path(tmp) / 'game'
            with self.assertRaisesRegex(ValueError, 'outside'): lib.check_paths(game / 'cache', game)
            with self.assertRaisesRegex(ValueError, 'outside'): lib.check_paths(lib.ROOT / 'cache', game)

    def test_explicit_missing_game_does_not_guess(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ValueError, 'not found'): lib.discover_game(tmp)

    def test_address_normalization(self):
        self.assertEqual(lib.rva('0x140862030'), lib.rva('862030'))


def manifest(mid):
    return {'schema': 1, 'id': mid, 'version': '1.0', 'game': {'exe': 'SAN14CE_KO.exe', 'unpacked_sha256': HASH}}


def hook(address, length=5):
    return {'kind': 'code', 'rva': address, 'length': length, 'guard': 'synthetic fixture only', 'on_mismatch': 'disable_feature'}


class CompatTests(unittest.TestCase):
    def test_nonconflicting_independent_mods(self):
        a, b = manifest('a.mod'), manifest('b.mod')
        compat.validate(a); compat.validate(b)
        self.assertEqual(compat.compare([a,b]), [])

    def test_partial_hook_overlap_and_full_span_block(self):
        a, b = manifest('a.mod'), manifest('b.mod')
        a['hooks'] = [hook('100E', 5)]; b['hooks'] = [hook('1011', 5)]
        self.assertIn('hook_overlap', [x['kind'] for x in compat.compare([a,b])])
        b['hooks'] = [hook('1018', 5)]
        self.assertIn('hook_16byte_block', [x['kind'] for x in compat.compare([a,b])])

    def test_file_case_insensitive_and_key_scope(self):
        a,b = manifest('a.mod'), manifest('b.mod')
        a['files'] = ['Mods/A.dll']; b['files'] = ['mods\\a.DLL']
        a['settings'] = [{'file':'A.ini','section':'s','key':'k'}]
        b['settings'] = [{'file':'B.ini','section':'s','key':'k'}]
        kinds = [x['kind'] for x in compat.compare([a,b])]
        self.assertIn('file_collision', kinds); self.assertNotIn('setting_collision', kinds)

    def test_missing_dependency_cycles_and_api(self):
        a,b = manifest('a.mod'), manifest('b.mod')
        a['depends']=['b.mod','missing.mod']; b['depends']=['a.mod']; a['uses']=['missing.api/v1']
        kinds = [x['kind'] for x in compat.compare([a,b])]
        for kind in ('missing_dependency','dependency_cycle','missing_api'): self.assertIn(kind,kinds)

    def test_different_builds_not_compared_by_rva(self):
        a,b = manifest('a.mod'), manifest('b.mod')
        b['game']['unpacked_sha256'] = 'b'*64
        a['hooks'] = b['hooks'] = [hook('1000')]
        kinds = [x['kind'] for x in compat.compare([a,b])]
        self.assertIn('different_game_build', kinds); self.assertNotIn('hook_overlap', kinds)

    def test_missing_guards_and_unsafe_paths_rejected(self):
        m = manifest('a.mod'); m['hooks']=[hook('1000')]; del m['hooks'][0]['guard']
        with self.assertRaisesRegex(ValueError, 'guard'): compat.validate(m)
        for value in ('../elsewhere.dll', 'C:/absolute.dll', 'SAN14CE_KO.exe', 'Save/a.dat'):
            m = manifest('a.mod'); m['files']=[value]
            with self.assertRaises(ValueError): compat.validate(m)


if __name__ == '__main__':
    unittest.main()
