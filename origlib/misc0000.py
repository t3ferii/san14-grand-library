"""0000/*.bin small data files + the JBTP behaviour-tree container (bt.bin / bt_exce.bin).

Section container (ccscore_data, change_force_data, opcamera_data, param_s, experience_data(_exce)):
  u32 nsec, nsec x (u32 offset, u32 size), sections; each section = u32 count + count x stride bytes
  (stride = (size-4)/count, verified integer for every section; evidence MEAS).
effect_info.bin = 548 B = 137 x 4 raw records; se_info(_exce).bin = 215/220 B of zeros (MEAS) - sound-effect table not populated.
bt*.bin: 'JBTP' u32 ver=2 u32 4 u32 0 then 4 x (offset,size,hash) (contiguous, MEAS) ; each section holds one KTBT tree;
  node format: REA_Analysis/1022_REA_분석_전체합본.md section 6 (re-implemented and node counts re-verified: bt_exce 10312+246+348+111).
Evidence tags: MISC = reference_mod MISC_DATA_FILES.md 3 (experience), REA6 = REA doc section 6, MEAS = measured here.
"""
import struct
from functools import lru_cache
from .s14 import GAME, u32
from .spec import F, decode, unresolved_of

C = '확정'
# (file, section) -> spec.  Unlisted sections are fully unresolved.
SPECS = {
    ('experience_data', 0): dict(key='exp_levels', stride=10, fields=[F(0, 'u32', 'level', '', 'MISC', C), F(4, 'u32', 'need_exp', '', 'MISC', '추정'), F(8, 'u8', 'a', '', 'MISC', '추정'), F(9, 'u8', 'b', '', 'MISC', '추정')]),
    ('experience_data', 1): dict(key='exp_stats', stride=24, fields=[F(0, 'u32', 'value', '능력치 값', 'MISC', C), F(4, 'u32x5', 'exp', '그 값에 필요한 누적 경험치(통·무·지·정·매)', 'MISC', C)]),
}
SPECS[('experience_data_exce', 0)] = SPECS[('experience_data', 0)]
SPECS[('experience_data_exce', 1)] = SPECS[('experience_data', 1)]

SECTION_FILES = ('ccscore_data', 'change_force_data', 'opcamera_data', 'param_s', 'experience_data', 'experience_data_exce')


def read_sections(name):
    """[(offset, size, count, stride, records)] for a section-container file in 0000/."""
    r = (GAME / '0000' / (name + '.bin')).read_bytes()
    n = u32(r, 0)
    out = []
    for i in range(n):
        off, size = struct.unpack_from('<II', r, 4 + 8 * i)
        cnt = u32(r, off)
        stride = (size - 4) // cnt if cnt and (size - 4) % cnt == 0 else None
        recs = [r[off + 4 + k * stride: off + 4 + (k + 1) * stride] for k in range(cnt)] if stride else []
        out.append((off, size, cnt, stride, recs))
    return out


def section_table(name, sec):
    """Records of one section as dicts (named fields when a spec exists, else {'raw': bytes})."""
    off, size, cnt, stride, recs = read_sections(name)[sec]
    spec = SPECS.get((name, sec))
    out = []
    for i, r in enumerate(recs):
        d = decode(spec, r) if spec else {}
        d['_id'] = i
        d['_raw'] = r
        out.append(d)
    return out


def section_unresolved(name, sec):
    off, size, cnt, stride, recs = read_sections(name)[sec]
    spec = SPECS.get((name, sec), dict(stride=stride, fields=[]))
    return unresolved_of(spec, recs)


def effect_info():
    r = (GAME / '0000' / 'effect_info.bin').read_bytes()
    return [r[i:i + 4] for i in range(0, len(r), 4)]


# ------------------------------------------------------------------------------------------------------------------
class Node:
    __slots__ = ('index', 'flags', 'type', 'extra', 'parent', 'nchildren', 'params', 'name', 'arr')

    def __repr__(self):
        return 'Node(%d type=%08x parent=%d params=%s)' % (self.index, self.type, self.parent, self.params[:6])


def parse_tree(sec):
    """Parse the first KTBT tree inside one JBTP section -> (tree_hash, [Node])."""
    k = sec.find(b'KTBT')
    ver, thash, zero, n = struct.unpack_from('<4I', sec, k + 4)
    p = k + 20
    nodes = []
    for idx in range(n):
        nd = Node()
        nd.index = idx
        nd.flags, nd.type = struct.unpack_from('<II', sec, p)
        p += 8
        nd.extra = None
        if nd.flags & 4:
            nd.extra = struct.unpack_from('<I', sec, p)[0]
            p += 4
        nd.parent, nd.nchildren, pc = struct.unpack_from('<iII', sec, p)
        p += 12
        assert pc <= 128
        nd.params = list(struct.unpack_from('<%di' % pc, sec, p)) if pc else []
        p += 4 * pc
        nd.name = None
        if nd.flags & 2:
            ln = struct.unpack_from('<I', sec, p)[0]
            p += 4
            nd.name = sec[p:p + ln].decode('cp932', errors='replace')
            p += ln
        nd.arr = None
        if nd.flags & 8:
            m = struct.unpack_from('<I', sec, p)[0]
            p += 4
            nd.arr = list(struct.unpack_from('<%di' % m, sec, p))
            p += 4 * m
        nodes.append(nd)
    return thash, nodes


class BehaviorTrees:
    """bt_exce.bin (exce=True, the file the CE exe reads) or bt.bin."""

    def __init__(self, exce=True):
        self.path = GAME / '0000' / ('bt_exce.bin' if exce else 'bt.bin')
        self.raw = self.path.read_bytes()
        assert self.raw[:4] == b'JBTP'
        self.version, self.count = struct.unpack_from('<II', self.raw, 4)
        self.sections = [struct.unpack_from('<III', self.raw, 16 + 12 * i) for i in range(self.count)]   # offset,size,hash
        self._trees = {}

    def tree(self, i):
        if i not in self._trees:
            off, size, h = self.sections[i]
            self._trees[i] = parse_tree(self.raw[off:off + size])
        return self._trees[i]


@lru_cache(None)
def load_bt(exce=True):
    return BehaviorTrees(exce)
