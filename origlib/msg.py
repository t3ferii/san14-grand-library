"""0001_KO/msgdata(_exce).bin, msggame(_exce).bin -- 'zp1' zlib-chunk container + section/message tables.

Container (evidence: AI_TacticsMod/research/ui_atlas/read_messages.py, verified by origlib tests):
  'zp1\\0' u32 total_raw u32 chunk_size u32 nchunks  u32[nchunks] compressed sizes (incl. 4-byte prefix) ...
  chunks start at 0x800, each chunk = u32 (n-4) + zlib stream, next chunk 128-byte aligned.
msggame: u32 nsections, then nsections x (u32 offset, u32 size). Each section has a
  u32 count, section-relative u32 offsets, and text runs wrapped in 07 07 01 / 07 07 02.
msgdata: an outer section table with a single inner table. Its four sections are XL/0x13
  tables of null-terminated UTF-16LE strings. Original UI lookup 30F010 uses section 1.
The origlib ID for both is section*10000 + index.
Only the Korean tables (0001_KO) are in scope.
"""
import struct
import zlib
from functools import lru_cache
from .s14 import GAME

FILES = ('msgdata', 'msgdata_exce', 'msggame', 'msggame_exce')


def unpack_zp1(data):
    assert data[:4] == b'zp1\0'
    total, chunk, count = struct.unpack_from('<III', data, 4)
    sizes = struct.unpack_from('<' + 'I' * count, data, 16)
    p = 0x800
    out = bytearray()
    for n in sizes:
        size = struct.unpack_from('<I', data, p)[0]
        assert size == n - 4
        out += zlib.decompress(data[p + 4:p + n])
        p = (p + n + 0x7f) & ~0x7f
    assert len(out) == total
    return bytes(out)


def _text(raw):
    runs = []
    pos = 0
    while True:
        b = raw.find(b'\x07\x07\x01', pos)
        if b < 0:
            break
        e = raw.find(b'\x07\x07\x02', b + 3)
        if e < 0:
            break
        runs.append(raw[b + 3:e].decode('utf-16-le', errors='replace'))
        pos = e + 3
    return ''.join(runs)


def _sections(raw):
    count = struct.unpack_from('<I', raw)[0]
    return struct.iter_unpack('<II', raw[4:4 + count * 8])


def _xl_offsets(body):
    magic, version, _, count, stride, fields, base = struct.unpack_from('<2sHIHHII', body)
    if (magic, version, stride, fields) != (b'XL', 0x13, 4, 1) or body[0x14] != 0:
        raise ValueError('expected an XL table of strings')
    offsets = struct.unpack_from(f'<{count}I', body, base)
    return [base + offset for offset in offsets]


class MsgTable:
    def __init__(self, name):
        self.name = name
        self.raw = unpack_zp1((GAME / '0001_KO' / (name + '.bin')).read_bytes())
        self.is_data = name in ('msgdata', 'msgdata_exce')
        base = 0
        container = self.raw
        if self.is_data:
            (base, size), = _sections(container)
            container = container[base:base + size]
        self.sections = []
        for at, n in _sections(container):
            body = container[at:at + n]
            if self.is_data:
                offsets = _xl_offsets(body)
            else:
                count = struct.unpack_from('<I', body)[0] if n >= 4 else 0
                offsets = [offset for (offset,) in struct.iter_unpack('<I', body[4:4 + count * 4])]
            self.sections.append((base + at, n, body, offsets))

    def nsections(self):
        return len(self.sections)

    def count(self, sec):
        return len(self.sections[sec][3])

    def raw_msg(self, sec, idx):
        at, n, body, offs = self.sections[sec]
        if idx >= len(offs):
            return b''
        end = offs[idx + 1] if idx + 1 < len(offs) else n
        return body[offs[idx]:end]

    def get(self, sec, idx):
        raw = self.raw_msg(sec, idx)
        if self.is_data:
            return raw.decode('utf-16-le', errors='replace').partition('\0')[0]
        return _text(raw)

    def lookup(self, id):
        sec, idx = divmod(id, 10000)
        if self.is_data and sec >= self.nsections():
            # CE section 3 has 10,011 entries. Its tail still uses section 3.
            sec = self.nsections() - 1
            idx = id - sec * 10000
        return self.get(sec, idx)

    def items(self):
        for s in range(len(self.sections)):
            for i in range(self.count(s)):
                yield s * 10000 + i, self.get(s, i)


@lru_cache(None)
def table(name):
    return MsgTable(name)


def msg(id, name='msggame_exce', lang='KO'):
    """origlib.msg(id): id = section*10000 + index (the UI convention).  lang is fixed to KO."""
    return table(name).lookup(id)


def find(needle, names=FILES):
    """[(table, id, text)] where text contains needle."""
    r = []
    for n in names:
        for i, t in table(n).items():
            if needle in t:
                r.append((n, i, t))
    return r
