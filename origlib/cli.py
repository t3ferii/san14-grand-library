"""python -m origlib <command> ...   (run from the game root: python -X utf8 -m origlib ... with San14Sim on sys.path / cwd=San14Sim)"""
import sys
import json
from . import fixdata, scenario, event, mapbin, misc0000, dlc
from .msg import msg as _msg, find as _find, FILES as _FILES


def _clean(d):
    return {k: (v.hex() if isinstance(v, bytes) else v) for k, v in d.items() if k != '_raw'}


def main(argv=None):
    a = list(sys.argv[1:] if argv is None else argv)
    if not a:
        print(__doc__)
        print('commands: tables | table <key|ko name> [N] | unresolved <key> | scenarios | scenario <id> [block [N]] | msg <id> [table] | find <text> | '
              'events [file [index]] | map [cell] | misc [file] | bt | dlc | rdb <name> | layout [name] | bin0005 <n>')
        return 0
    c, rest = a[0], a[1:]
    fx = fixdata._fix(True)
    if c == 'tables':
        for tid, t in sorted(fixdata.TABLES.items()):
            ch = fx.chunks.get(tid)
            print('%3d %-14s %-22s stride=%-4d count=%s  fields=%d' % (tid, t['key'], t['ko'], t['stride'], ch.count if ch else (12 if tid == -1 else '?'), len(t['fields'])))
    elif c == 'table':
        rows = fx.table(rest[0])
        n = int(rest[1]) if len(rest) > 1 else len(rows)
        for r in rows[:n]:
            print(json.dumps(_clean(r), ensure_ascii=False))
    elif c == 'unresolved':
        tid = fixdata.BY_KEY.get(rest[0], fixdata.BY_KO.get(rest[0]))
        for s, e, d in fx.unresolved(tid):
            print('+0x%02x..+0x%02x  %s' % (s, e, d))
    elif c == 'scenarios':
        for i in scenario.scenario_ids():
            s = scenario.load_scenario(i)
            print(i, s.name, s.year, s.month, 'cat', s.category)
    elif c == 'scenario':
        s = scenario.load_scenario(int(rest[0]))
        if len(rest) == 1:
            print(json.dumps(dict(id=s.id, name=s.name, year=s.year, month=s.month, intro=s.intro, tables=[x.as_dict() for x in s.chain]), ensure_ascii=False, indent=1))
        else:
            rows = s.table(rest[1])
            n = int(rest[2]) if len(rest) > 2 else len(rows)
            for r in rows[:n]:
                print(json.dumps(_clean(r), ensure_ascii=False))
    elif c == 'msg':
        name = rest[1] if len(rest) > 1 else 'msggame_exce'
        print(_msg(int(rest[0]), name))
    elif c == 'find':
        for n, i, t in _find(rest[0], _FILES)[:200]:
            print(n, i, repr(t[:80]))
    elif c == 'events':
        if not rest:
            for f in event.event_files():
                e = event.events(f)
                print(f, e.n)
        else:
            e = event.events(rest[0])
            if len(rest) == 1:
                for k, v in sorted(event.opcode_stats(e).items()):
                    print(k, 'count', v[0], 'events', v[1])
            else:
                ev = e.event(int(rest[1]))
                print('id', ev.event_id, 'actors', ev.actors)
                for r in ev.conditions:
                    print(' cond', r[2:])
                for r in ev.actions:
                    print(' act ', r[2:])
                print(e.speech(ev))
    elif c == 'map':
        m = mapbin.load_map()
        print(m.cell(int(rest[0]))) if rest else print(mapbin.W, mapbin.H)
    elif c == 'misc':
        for n in misc0000.SECTION_FILES:
            print(n, [(s[2], s[3]) for s in misc0000.read_sections(n)])
    elif c == 'bt':
        b = misc0000.load_bt()
        print([len(b.tree(i)[1]) for i in range(b.count)])
    elif c == 'dlc':
        for x in dlc.dlc_scenarios():
            print(x)
    elif c == 'rdb':
        from . import rdb
        print(rdb.open(rest[0]))
    elif c == 'layout':
        from . import rdb
        if len(rest) > 1 or (rest and not rest[0].isascii()):
            print('사용법: layout [ASCII 논리 이름]', file=sys.stderr)
            return 2
        rows = rdb.read_layout_registry()
        if rest:
            key = rdb.layout_name_hash(rest[0])
            if key not in rows:
                print(f'등록된 레이아웃 이름 없음: {rest[0]} ({key:08X})', file=sys.stderr)
                return 1
            rows = {key: rows[key]}
        for key, row in rows.items():
            print(f'{key:08X}\t{row.wrapper:08X}\t{row.setting:08X}\t{row.layout:08X}')
    elif c == 'bin0005':
        from . import bin0005
        print(bin0005.open(rest[0]))
    else:
        print('unknown command', c)
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
