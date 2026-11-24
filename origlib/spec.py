"""Shared field-spec machinery: (offset, fmt, name, meaning, evidence, confidence).

fmt: u8 u16 u32 i8 i16 i32 | wN = UTF-16LE string in N bytes | <int>xN arrays (u8x10, u16x8 ...).
Anything not covered by a spec is reported by unresolved_of() with measured value distributions.
"""
import collections
import struct
from . import s14


def F(off, fmt, name, desc='', ev='', conf='추정'):
    return (off, fmt, name, desc, ev, conf)


_W = {'u8': 1, 'i8': 1, 'u16': 2, 'i16': 2, 'u32': 4, 'i32': 4}
_C = {'u8': 'B', 'i8': 'b', 'u16': 'H', 'i16': 'h', 'u32': 'I', 'i32': 'i'}


def fmt_size(fmt):
    if fmt.startswith('w'):
        return int(fmt[1:])
    base, _, n = fmt.partition('x')
    return _W[base] * (int(n) if n else 1)


def read_field(rec, off, fmt):
    if fmt.startswith('w'):
        return s14.wstr(rec, off, int(fmt[1:]))
    base, _, n = fmt.partition('x')
    cnt = int(n) if n else 1
    vals = struct.unpack_from('<' + _C[base] * cnt, rec, off)
    return list(vals) if n else vals[0]


def decode(spec, rec):
    return {name: read_field(rec, off, fmt) for off, fmt, name, *_ in spec['fields']}


def unresolved_of(spec, recs):
    """[(start, end, summary)] for bytes not covered by spec['fields'] (over all records)."""
    stride = spec['stride']
    covered = bytearray(stride)
    for off, fmt, *_ in spec['fields']:
        for k in range(off, min(stride, off + fmt_size(fmt))):
            covered[k] = 1
    res = []
    if not recs:
        return res
    k = 0
    while k < stride:
        if covered[k]:
            k += 1
            continue
        col = collections.Counter(r[k] for r in recs)
        if len(col) == 1:
            v = recs[0][k]
            j = k
            while j < stride and not covered[j] and len(set(r[j] for r in recs)) == 1 and recs[0][j] == v:
                j += 1
            res.append((k, j, '상수 0x%02x' % v))
            k = j
        else:
            vals = [r[k] for r in recs]
            res.append((k, k + 1, 'u8 distinct=%d min=%d max=%d top=%s' % (len(col), min(vals), max(vals), col.most_common(3))))
            k += 1
    return res
