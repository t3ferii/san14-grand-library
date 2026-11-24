"""S14 container + chunk-chain walker.

File layout (evidence: reference_mod/Modding_DOCS/format/SCENARIO_PK_CE_COMPARE.md, LWC_FORMAT.md; re-verified by origlib tests):
  fixdata*/sceda*: plain header (480 B base game, 754 B PK/CE) then one LWC block ("LWC\\x1a");
  the body is a chain of tables.  Every table = <u32 id><u32 count> + count*stride bytes and the next
  header follows immediately.  The stride is not stored in the file; it is found by DFS ("the chain
  must hit a sane next header"), hinted by the stride tables that origlib.fixdata/scenario carry.
"""
import struct
import sys
from pathlib import Path
from . import lwc

def _find_game():
    # game folder = nearest ancestor holding 0010_KO (works from San14Sim/ and from .wt/<lane>/ worktrees); env SAN14_GAME overrides
    import os
    e = os.environ.get('SAN14_GAME')
    if e: return Path(e)
    for q in Path(__file__).resolve().parents:
        if (q / '0010_KO').is_dir(): return q
    return Path(__file__).resolve().parents[2]


GAME = _find_game()


def u8(b, p): return b[p]
def u16(b, p): return struct.unpack_from('<H', b, p)[0]
def i16(b, p): return struct.unpack_from('<h', b, p)[0]
def u32(b, p): return struct.unpack_from('<I', b, p)[0]
def i32(b, p): return struct.unpack_from('<i', b, p)[0]


def wstr(b, p=0, n=None):
    """UTF-16LE NUL-terminated string from b[p:p+n] (n in bytes)."""
    seg = b[p:p + n] if n is not None else b[p:]
    return seg.decode('utf-16le', errors='replace').split('\0')[0]


class Container:
    """header = plain bytes before the LWC block, body = decompressed payload."""

    def __init__(self, path):
        self.path = Path(path)
        self.raw = self.path.read_bytes()
        self.blob_off = lwc.find_blob(self.raw)
        self.header = self.raw[:self.blob_off]
        self.body = lwc.decompress(self.raw, self.blob_off)
        self.version = self.header[0x1CB] if len(self.header) > 0x1CB else None


class Chunk:
    __slots__ = ('id', 'count', 'stride', 'hdr', 'base', 'end')

    def __init__(self, id, count, stride, hdr):
        self.id, self.count, self.stride, self.hdr = id, count, stride, hdr
        self.base = hdr + 8
        self.end = self.base + count * stride

    def rec(self, body, i):
        return body[self.base + i * self.stride: self.base + (i + 1) * self.stride]

    def as_dict(self):
        return dict(id=self.id, count=self.count, stride=self.stride, hdr=self.hdr, base=self.base, end=self.end)


def walk_chain(body, start, hints=None, max_id_jump=60, max_count=100000):
    """DFS the table chain from `start`; returns the longest chain reached as list[Chunk].
    hints: {table_id: stride} that are tried first (speeds up and disambiguates)."""
    hints = hints or {}
    n = len(body)
    best = []
    sys.setrecursionlimit(5000)

    def rec(p, chain):
        nonlocal best
        if len(chain) > len(best):
            best = chain
        if p + 8 > n:
            return True
        i, c = struct.unpack_from('<II', body, p)
        order = []
        if i in hints:
            order.append(hints[i])
        order += [s for s in range(0, 3000) if s != hints.get(i)]
        for s in order:
            q = p + 8 + c * s
            if q > n:
                break
            ch = chain + [Chunk(i, c, s, p)]
            if q == n:
                if len(ch) > len(best):
                    best = ch
                return True
            if q + 8 > n:
                continue
            i2, c2 = struct.unpack_from('<II', body, q)
            if i < i2 <= i + max_id_jump and 1 <= c2 <= max_count:
                if rec(q, ch):
                    return True
        return False

    rec(start, [])
    return best
