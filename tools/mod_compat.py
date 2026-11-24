"""Compare external mod manifests without installing or executing a mod. stdlib only."""
from __future__ import annotations
import argparse
import json
from pathlib import Path, PurePosixPath
import re
import sys


def number(value):
    return int(value, 16) if isinstance(value, str) else int(value)


def validate(m):
    if m.get('schema') != 1 or not re.fullmatch('[a-z0-9][a-z0-9.-]*', m.get('id', '')):
        raise ValueError('schema=1 and a lowercase namespaced id required')
    if not isinstance(m.get('version'), str) or not m['version']:
        raise ValueError('version required')
    if not isinstance(m.get('game'), dict) or m['game'].get('exe') != 'SAN14CE_KO.exe':
        raise ValueError('game.exe must be SAN14CE_KO.exe')
    if not re.fullmatch('[0-9a-f]{64}', m['game'].get('unpacked_sha256', '')):
        raise ValueError('game.unpacked_sha256 required')
    for name in ('depends', 'conflicts', 'provides', 'uses', 'hooks', 'files', 'settings', 'ui', 'resources'):
        if not isinstance(m.get(name, []), list):
            raise ValueError(f'{name} must be an array')
    for name in ('depends', 'conflicts', 'provides', 'uses'):
        if not all(isinstance(s, str) and s for s in m.get(name, [])):
            raise ValueError(f'{name} entries must be nonempty strings')
    for f in m.get('files', []):
        if not isinstance(f, str) or not f: raise ValueError('file path must be a nonempty string')
        p = PurePosixPath(f.replace('\\', '/'))
        if p.is_absolute() or '..' in p.parts or ':' in f:
            raise ValueError(f'Unsafe installation path: {f}')
        if p.name.casefold() in ('san14ce_ko.exe',) or p.parts[0].casefold() in ('saves', 'save', 'backup'):
            raise ValueError('Original EXE/save/backup ownership forbidden')
    for hook in m.get('hooks', []):
        if not isinstance(hook, dict) or hook.get('kind') not in ('code', 'vtable', 'call'):
            raise ValueError('hook.kind must be code, vtable or call')
        if number(hook.get('rva', 0)) <= 0 or not isinstance(hook.get('length'), int) or not 1 <= hook['length'] <= 4096:
            raise ValueError('Positive hook RVA and length required')
        if not isinstance(hook.get('guard'), str) or not hook['guard'].strip():
            raise ValueError('Original bytes/value guard evidence required')
        if hook.get('on_mismatch') != 'disable_feature':
            raise ValueError('Hook mismatch must disable_feature')
    for s in m.get('settings', []):
        if not isinstance(s, dict) or any(not isinstance(s.get(k), str) or not s[k] for k in ('file', 'section', 'key')):
            raise ValueError('Each setting requires file, section and key')
    for name in ('ui', 'resources'):
        if not all(isinstance(s, str) and s for s in m.get(name, [])):
            raise ValueError(f'{name} entries must be globally namespaced strings')


def compare(manifests):
    issues = []
    ids = [m['id'] for m in manifests]
    def emit(level, a, b, kind, detail):
        issues.append({'level': level, 'mods': [a, b] if b else [a], 'kind': kind, 'detail': detail})
    for mid in sorted(set(ids)):
        if ids.count(mid) > 1: emit('error', mid, None, 'duplicate_id', 'Duplicate mod id')
    known = set(ids)
    graph = {m['id']: m.get('depends', []) for m in manifests}
    for m in manifests:
        for dep in m.get('depends', []):
            if dep not in known: emit('error', m['id'], dep, 'missing_dependency', dep)
        for other in m.get('conflicts', []):
            if other in known: emit('error', m['id'], other, 'declared_conflict', other)
        for api in m.get('uses', []):
            if not any(api in p.get('provides', []) for p in manifests):
                emit('error', m['id'], None, 'missing_api', api)
    done, active = set(), set()
    def visit(mid):
        if mid in active:
            emit('error', mid, None, 'dependency_cycle', mid); return
        if mid in done: return
        active.add(mid)
        for dep in graph.get(mid, []):
            if dep in graph: visit(dep)
        active.remove(mid); done.add(mid)
    for mid in ids: visit(mid)
    for i, a in enumerate(manifests):
        for b in manifests[i+1:]:
            aid, bid = a['id'], b['id']
            same_build = a['game']['unpacked_sha256'] == b['game']['unpacked_sha256']
            if not same_build: emit('error', aid, bid, 'different_game_build', 'RVA comparison unavailable across builds')
            for field, kind in (('files', 'file_collision'), ('ui', 'ui_collision'), ('resources', 'resource_collision'), ('provides', 'api_collision')):
                overlap = {s.replace('\\', '/').casefold() for s in a.get(field, [])} & {s.replace('\\', '/').casefold() for s in b.get(field, [])}
                for value in sorted(overlap): emit('error', aid, bid, kind, value)
            def settings(m):
                return {(s['file'].replace('\\', '/').casefold(), s['section'].casefold(), s['key'].casefold()) for s in m.get('settings', [])}
            for value in sorted(settings(a) & settings(b)): emit('error', aid, bid, 'setting_collision', '/'.join(value))
            if not same_build: continue
            for ah in a.get('hooks', []):
                for bh in b.get('hooks', []):
                    x, y = number(ah['rva']), number(bh['rva'])
                    xe, ye = x + ah['length'], y + bh['length']
                    if x < ye and y < xe:
                        emit('error', aid, bid, 'hook_overlap', f'{x:X}..{xe:X} / {y:X}..{ye:X}; chaining requires a separate reviewed agreement')
                    elif x//16 <= (ye-1)//16 and y//16 <= (xe-1)//16:
                        emit('warning', aid, bid, 'hook_16byte_block', f'{x:X} / {y:X}')
    return issues


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('manifests', nargs='+', type=Path); p.add_argument('--json', action='store_true')
    args = p.parse_args()
    try:
        manifests = [json.loads(x.read_text(encoding='utf-8-sig')) for x in args.manifests]
        for m in manifests: validate(m)
        issues = compare(manifests)
    except (ValueError, KeyError, OSError, TypeError) as e:
        print(f'Invalid manifest: {e}', file=sys.stderr); return 2
    if args.json: print(json.dumps(issues, ensure_ascii=False, indent=2))
    else:
        for x in issues: print(f'{x["level"]}: {" + ".join(x["mods"])} {x["kind"]}: {x["detail"]}')
        print(f'{len(issues)} declared conflicts/warnings. Undeclared or behavioral conflicts are not assessed.')
    return int(any(x['level'] == 'error' for x in issues))


if __name__ == '__main__':
    raise SystemExit(main())
