"""0004/Event*.s14, CCEvent*.s14, EventPKCE001.s14, EventTutorial(PKCE).s14: event scripts (uncompressed, little endian).

File layout (19 installed scripts measured). The current-build opcode dispatch is indexed in docs/orig/event_opcodes.json.
Argument layouts are per opcode. Speech opcode 95 is confirmed by text lookup:
  0x00 u32 version=3, u32 5, u32 9, u32 4, u32 14, u32 0 x3, u32 1 (@0x20), u32 0 x3, u32 N events (@0x30), u32 0 x3
  0x40 u32 offsets[1 + 2N + 2]:  [0] = offset of table A, [1..N] = offset of each event's condition list,
       [N+1..2N] = offset of each event's action list, then two trailing u32 (0, and the file end - 4 / 100)
  table A: N x 68 bytes: u32 event_id, 0, 0, u32 999, 0, 0, 1, 1, then u32 actors[5] (general ids, 1000 = placeholder), rest 0
  condition list (variable): k x 44-byte records of 11 x i32 = [event_index, 0, cond_code, a1..a8]; the first record of every event
       is the placeholder [idx,0,0,1,2,3,4,-1,-2,-3,-4] (44 B lists with only the placeholder = event without extra condition)
  action list  (variable): k x 44-byte records of 11 x i32 = [event_index, 0, op_code, a1..a8]
  op 95 = speech line: a1 = speaker general id, a2 = message id (section*10000 + index in msggame / msggame_exce), a4 = listener
  text table: files with 'PKCE' in the name use 0001_KO/msggame_exce.bin, the others use msggame.bin
EventSample{Ko,..}.s14: separate editor-sample catalog (u32 1 + UTF-16 titles/descriptions + binary), not event scripts (language files other than Ko ignored).
"""
import struct
from functools import lru_cache
from .s14 import GAME

N_REC = 44


class Event:
    def __init__(self, f, idx, a, conds, acts):
        self.file, self.index, self.a, self.conditions, self.actions = f, idx, a, conds, acts

    @property
    def event_id(self):
        return self.a[0]

    @property
    def actors(self):
        return self.a[8:13]


class EventFile:
    def __init__(self, name):
        self.name = name
        self.path = GAME / '0004' / name
        self.raw = self.path.read_bytes()
        r = self.raw
        self.header = struct.unpack_from('<16I', r)
        self.version = self.header[0]
        n = self.n = self.header[12]
        offs = struct.unpack_from('<%dI' % (1 + 2 * n + 2), r, 0x40)
        self.a_off = offs[0]
        self.cond_off = list(offs[1:1 + n])
        self.act_off = list(offs[1 + n:1 + 2 * n])
        self.tail = offs[-2:]
        self.table_a = [list(struct.unpack_from('<17i', r, self.a_off + 68 * i)) for i in range(n)]
        self._ends_c = self.cond_off[1:] + [self.act_off[0]]
        self._ends_a = self.act_off[1:] + [len(r) - 8]

    def _recs(self, b, e):
        return [list(struct.unpack_from('<11i', self.raw, p)) for p in range(b, e, N_REC)]

    def event(self, i):
        return Event(self.name, i, self.table_a[i], self._recs(self.cond_off[i], self._ends_c[i]), self._recs(self.act_off[i], self._ends_a[i]))

    def events(self):
        return [self.event(i) for i in range(self.n)]

    def text_table(self):
        return 'msggame_exce' if 'PKCE' in self.name else 'msggame'

    def speech(self, ev):
        """[(speaker, text, listener)] of the speech opcodes (95) of an Event."""
        from .msg import table
        out = []
        for r in ev.actions:
            if r[2] == 95:
                out.append((r[3], table(self.text_table()).get(r[4] // 10000, r[4] % 10000), r[6]))
        return out


def event_files():
    return sorted(p.name for p in (GAME / '0004').glob('*.s14') if not p.name.startswith('EventSample'))


@lru_cache(None)
def events(file):
    """origlib.events('EventTutorial.s14') -> EventFile (use .events() / .event(i))."""
    if not file.endswith('.s14'):
        file += '.s14'
    return EventFile(file)


def opcode_stats(f):
    """{('cond'|'act', code): (count, events, [per-arg (distinct, min, max)])} for one EventFile."""
    import collections
    st = {}
    for kind in ('conditions', 'actions'):
        for ev in f.events():
            for r in getattr(ev, kind):
                k = ('cond' if kind == 'conditions' else 'act', r[2])
                st.setdefault(k, []).append((ev.index, r))
    out = {}
    for k, rows in st.items():
        cols = []
        for j in range(3, 11):
            vals = [r[j] for _, r in rows]
            cols.append((len(set(vals)), min(vals), max(vals)))
        out[k] = (len(rows), len(set(i for i, _ in rows)), cols)
    return out
