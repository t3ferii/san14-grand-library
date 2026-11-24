"""Ownership/cleanup regressions using synthetic files, never installed user tools."""
import contextlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import library as lib
import tool_lifecycle as life
from test_library import synthetic_export


def owned_tool(cache, name='ghidra'):
    rel = f'tools/{name}-1'
    life.record_created(cache, rel, 'tool', name, '1', 'a'*64)
    path = cache / rel; path.mkdir(parents=True)
    (path / 'synthetic.txt').write_text('tool fixture')
    lib.write_json(path / '.verified.json', {'archive_sha256':'a'*64, 'files':life.inventory(path)})
    life.finish_tool(cache, rel)
    return path


def owned_archive(cache, name='python'):
    rel = f'downloads/{name}.zip'
    payload = b'fixture zip'; sha = __import__('hashlib').sha256(payload).hexdigest()
    life.record_created(cache, rel, 'archive', name, sha256=sha)
    path = cache / rel; path.parent.mkdir(exist_ok=True); path.write_bytes(payload)
    return path


class CleanupTests(unittest.TestCase):
    @unittest.skipUnless(os.name == 'nt', 'Windows preparation pipeline')
    def test_failed_preparation_keeps_tools_then_success_removes_them(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp); game = base/'game'; game.mkdir(); original = game/lib.EXE
            original.write_bytes(b'packed fixture'); plain_bytes = b'plain fixture'
            packed = lib.digest(original); plain = __import__('hashlib').sha256(plain_bytes).hexdigest()
            repo = base/'repo'; (repo/'tools/ghidra_scripts').mkdir(parents=True)
            build = {'packed_sha256':packed,'unpacked_sha256':plain,'steamless_args':[],'smoke_rvas':['1000']}
            lib.write_json(repo/'tools/builds.json',{'default':'test','builds':{'test':build}})
            lib.write_json(repo/'tools/dependencies.lock.json',{n:{'version':'1','url':'https://invalid.example','sha256':'a'*64} for n in ('steamless','java','ghidra')})
            cache = base/'cache'
            def install(name, spec, destination):
                path = destination/f'tools/{name}-1'
                if not path.exists():
                    life.record_created(destination,f'tools/{name}-1','tool',name,'1','a'*64)
                    path.mkdir(parents=True)
                    entry = {'steamless':'Steamless.CLI.exe','java':'bin/java.exe','ghidra':'support/analyzeHeadless.bat'}[name]
                    (path/entry).parent.mkdir(parents=True,exist_ok=True); (path/entry).touch()
                    lib.write_json(path/'.verified.json',{'archive_sha256':'a'*64,'files':life.inventory(path)})
                    life.finish_tool(destination,f'tools/{name}-1')
                return path
            fail = [True]
            def run(command, logfile, env=None,cwd=None):
                workspace = cache/'builds'/plain[:16]
                if str(command[0]).endswith('Steamless.CLI.exe'):
                    (workspace/'input/game.exe.unpacked.exe').write_bytes(plain_bytes)
                elif 'San14AnalysisReport.java' in command:
                    if fail[0]: raise RuntimeError('synthetic interrupted analysis')
                    (workspace/'project/SAN14CE_KO.gpr').touch()
                    lib.write_json(workspace/'analysis/analysis_report.json',{'sha256':plain,'functions':2,'analysis_timeout':False})
                else:
                    synthetic_export(workspace/'export')
                    manifest=lib.read_json(workspace/'export/manifest.json'); manifest['sha256']=plain
                    lib.write_json(workspace/'export/manifest.json',manifest)
                return ''
            args=['prepare','--game',str(game),'--cache-root',str(cache)]
            with mock.patch.object(lib,'ROOT',repo), mock.patch.object(lib,'install_tool',side_effect=install), mock.patch.object(lib,'run',side_effect=run):
                with mock.patch.object(lib,'cleanup_tools',wraps=lib.cleanup_tools) as cleanup:
                    with contextlib.redirect_stderr(io.StringIO()): self.assertEqual(lib.main(args),1)
                    cleanup.assert_not_called()
                self.assertTrue(all((cache/f'tools/{n}-1').exists() for n in ('steamless','java','ghidra')))
                fail[0]=False
                self.assertEqual(lib.main(args),0)
                self.assertFalse(any((cache/f'tools/{n}-1').exists() for n in ('steamless','java','ghidra')))
                proof=lib.read_json(cache/'builds'/plain[:16]/'ready.json')
                self.assertEqual(len(proof['tool_cleanup']['removed']),3)
                self.assertEqual(original.read_bytes(),b'packed fixture')
                # Borrowing fingerprints must not trigger a new expensive analysis.
                lock=lib.read_json(repo/'tools/dependencies.lock.json')
                lock['steamless']['runtime_files']={'synthetic.exe':'b'*64}
                lib.write_json(repo/'tools/dependencies.lock.json',lock)
                with mock.patch.object(lib,'install_tool') as install_again, mock.patch.object(lib,'run') as run_again:
                    self.assertEqual(lib.main(args),0)
                    install_again.assert_not_called(); run_again.assert_not_called()

    def test_owned_build_tools_removed_but_query_runtime_and_cache_kept(self):
        with tempfile.TemporaryDirectory() as tmp:
            cache = Path(tmp)
            tools = [owned_tool(cache, n) for n in ('java','ghidra','steamless')]
            archives = [owned_archive(cache, n) for n in ('python','java','ghidra','steamless')]
            runtime = cache / 'tools/python-3.12.10/python.exe'; runtime.parent.mkdir(); runtime.write_bytes(b'query runtime fixture')
            data = cache / 'builds/cache.txt'; data.parent.mkdir(); data.write_text('cached facts')
            report = life.cleanup(cache)
            self.assertEqual(len(report['removed']), 7)
            self.assertFalse(report['errors']); self.assertFalse(report['preserved'])
            self.assertTrue(all(not p.exists() for p in tools + archives))
            self.assertTrue(runtime.is_file()); self.assertEqual(data.read_text(), 'cached facts')
            self.assertEqual(life.cleanup(cache)['removed'], [], 'Cleanup must be idempotent')

    def test_preexisting_files_are_not_adopted(self):
        with tempfile.TemporaryDirectory() as tmp:
            cache = Path(tmp)
            external = cache / 'tools/ghidra-1'; external.mkdir(parents=True); (external/'user.txt').write_text('original')
            archive = cache/'downloads/java.zip'; archive.parent.mkdir(); archive.write_bytes(b'preexisting')
            self.assertFalse(life.record_created(cache, 'tools/ghidra-1', 'tool', 'ghidra', '1', 'a'*64))
            self.assertFalse(life.record_created(cache, 'downloads/java.zip', 'archive', 'java', sha256='a'*64))
            life.cleanup(cache)
            self.assertEqual((external/'user.txt').read_text(), 'original'); self.assertEqual(archive.read_bytes(), b'preexisting')

    def test_modified_or_extended_tools_and_archives_are_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            cache = Path(tmp); path = owned_tool(cache); archive = owned_archive(cache)
            extra = path / 'nested/.verified.json'; extra.parent.mkdir(); extra.write_text('user added file')
            archive.write_bytes(b'user changed archive')
            report = life.cleanup(cache)
            self.assertEqual(len(report['preserved']), 2); self.assertEqual(report['removed'], [])
            self.assertTrue(extra.exists()); self.assertTrue(archive.exists())

    def test_tampered_proof_is_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            cache = Path(tmp); path = owned_tool(cache)
            (path/'.verified.json').write_text('{}')
            self.assertEqual(len(life.cleanup(cache)['preserved']), 1)
            self.assertTrue(path.exists())

    def test_incomplete_tool_is_kept_for_recovery(self):
        with tempfile.TemporaryDirectory() as tmp:
            cache = Path(tmp)
            life.record_created(cache, 'tools/java-1', 'tool', 'java', '1', 'a'*64)
            path = cache / 'tools/java-1'; path.mkdir(parents=True); (path/'partial').write_text('interrupted')
            self.assertEqual(len(life.cleanup(cache)['preserved']), 1)
            self.assertTrue((path/'partial').exists())

    def test_malicious_record_cannot_delete_outside_cache_or_python(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); cache = root/'cache'; cache.mkdir(); outside = root/'user.txt'; outside.write_text('keep')
            for rel, kind, name in [('../user.txt','archive','java'), ('tools/python-1','tool','python')]:
                record = dict(schema=1, cache_root=str(cache.resolve()), relative=rel,kind=kind,name=name,version='1',sha256='a'*64)
                lib.write_json(life.marker(cache,rel), record)
            report = life.cleanup(cache)
            self.assertEqual(len(report['preserved']), 2); self.assertEqual(outside.read_text(), 'keep')

    def test_foreign_cache_ownership_is_not_trusted(self):
        with tempfile.TemporaryDirectory() as tmp:
            cache = Path(tmp); path = owned_tool(cache)
            marker = life.marker(cache, 'tools/ghidra-1'); data = json.loads(marker.read_text()); data['cache_root'] += '-other'
            lib.write_json(marker, data)
            self.assertEqual(len(life.cleanup(cache)['preserved']), 1); self.assertTrue(path.exists())

    def test_reparse_tool_is_not_removed(self):
        with tempfile.TemporaryDirectory() as tmp:
            cache = Path(tmp); path = owned_tool(cache)
            original = life.is_link
            with mock.patch.object(life, 'is_link', side_effect=lambda p: Path(p)==path or original(p)):
                self.assertEqual(len(life.cleanup(cache)['preserved']), 1)
            self.assertTrue(path.exists())

    def test_new_download_install_and_cleanup(self):
        with tempfile.TemporaryDirectory() as tmp:
            cache = Path(tmp); content = io.BytesIO()
            with zipfile.ZipFile(content, 'w') as z:z.writestr('bin/java.exe', 'synthetic fixture')
            payload = content.getvalue()
            spec = {'version':'1','url':'https://invalid.example/tool.zip','sha256':__import__('hashlib').sha256(payload).hexdigest()}
            with mock.patch.object(lib, 'discover_tool', return_value=None), mock.patch.object(lib.urllib.request, 'urlopen', return_value=io.BytesIO(payload)):
                path = lib.install_tool('java', spec, cache)
            self.assertTrue(path.exists()); self.assertTrue((cache/'downloads/java.zip').exists())
            report = life.cleanup(cache)
            self.assertEqual(len(report['removed']), 2); self.assertFalse(path.exists())

    def test_borrowed_tool_is_untouched(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); external = root/'installed-java'; external.mkdir(); (external/'user.txt').write_text('keep')
            cache = root/'cache'; cache.mkdir()
            with mock.patch.object(lib, 'discover_tool', return_value=external), mock.patch.object(lib,'download') as download:
                self.assertEqual(lib.install_tool('java', {'version':'1'}, cache), external)
                download.assert_not_called()
            self.assertEqual(life.cleanup(cache)['removed'], [])
            self.assertEqual((external/'user.txt').read_text(), 'keep')

    def test_detects_only_matching_existing_java_and_ghidra(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); (root/'bin').mkdir(); (root/'bin/java.exe').touch()
            (root/'release').write_text('JAVA_RUNTIME_VERSION="21.0.13.1+2-LTS"\n')
            (root/'support').mkdir(); (root/'support/analyzeHeadless.bat').touch()
            (root/'Ghidra').mkdir(); (root/'Ghidra/application.properties').write_text('application.version=12.1.4\n')
            with mock.patch.dict(os.environ, {'SAN14_JAVA_HOME':str(root),'SAN14_GHIDRA_HOME':str(root)}, clear=True), mock.patch.object(lib.shutil, 'which', return_value=None):
                self.assertEqual(lib.discover_tool('java', {'version':'21.0.13.1+2'}), root.resolve())
                self.assertIsNone(lib.discover_tool('java', {'version':'21.0.12+7'}))
                self.assertEqual(lib.discover_tool('ghidra', {'version':'12.1.4'}), root.resolve())

    def test_source_archive_with_ownership_removed(self):
        with tempfile.TemporaryDirectory() as tmp:
            cache = Path(tmp); rel = 'downloads/source-'+'b'*32+'.zip'
            payload = b'synthetic source archive'; sha = __import__('hashlib').sha256(payload).hexdigest()
            life.record_created(cache, rel, 'source_archive', 'source', sha256=sha)
            path = cache/rel; path.parent.mkdir(); path.write_bytes(payload)
            self.assertEqual(life.cleanup(cache)['removed'], [rel]); self.assertFalse(path.exists())

    @unittest.skipUnless(os.name=='nt', 'Windows PowerShell runtime resolver')
    def test_powershell_uses_existing_python_without_installing(self):
        with tempfile.TemporaryDirectory() as tmp:
            cache = Path(tmp)/'cache'
            command = ". '"+str(ROOT/'tools/python_runtime.ps1')+"'; Resolve-San14Python -CacheRoot '"+str(cache)+"' -RepoRoot '"+str(ROOT)+"'"
            result = subprocess.run(['powershell','-NoProfile','-ExecutionPolicy','Bypass','-Command',command], env=dict(os.environ,SAN14_PYTHON=sys.executable), capture_output=True,text=True,timeout=30)
            self.assertEqual(result.returncode,0,result.stderr)
            self.assertEqual(Path(result.stdout.strip()).resolve(),Path(sys.executable).resolve())
            self.assertFalse(cache.exists())

    @unittest.skipUnless(os.name=='nt', 'Windows PowerShell ownership writer')
    def test_powershell_archive_records_are_cleaned_by_python(self):
        with tempfile.TemporaryDirectory() as tmp:
            cache=Path(tmp)/'cache'; cache.mkdir()
            payload=b'archive fixture'; sha=__import__('hashlib').sha256(payload).hexdigest()
            source='downloads/source-'+'c'*32+'.zip'; (cache/source).parent.mkdir(); (cache/source).write_bytes(payload)
            command=". '"+str(ROOT/'tools/python_runtime.ps1')+"'; "
            command+="Register-San14Archive -CacheRoot '"+str(cache)+"' -Relative 'downloads/python.zip' -Kind archive -Name python -Sha256 '"+sha+"'; "
            command+="Register-San14Archive -CacheRoot '"+str(cache)+"' -Relative '"+source+"' -Kind source_archive -Name source -Sha256 '"+sha+"' -CreatedByCaller"
            result=subprocess.run(['powershell','-NoProfile','-ExecutionPolicy','Bypass','-Command',command],capture_output=True,text=True,timeout=30)
            self.assertEqual(result.returncode,0,result.stderr)
            (cache/'downloads/python.zip').write_bytes(payload)
            report=life.cleanup(cache)
            self.assertEqual(set(report['removed']),{'downloads/python.zip',source})
            self.assertFalse(report['preserved']); self.assertFalse(report['errors'])


if __name__=='__main__':unittest.main()
