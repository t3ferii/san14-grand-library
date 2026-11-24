"""0000/Map.bin (base) and 0000/MapExCe.bin (CE): the 220 x 220 map cell table.

File: u32 count (48400 = 0xBD10) + 48400 cells x 16 bytes, row-major (cell = y*220 + x).
Cell (evidence MEAS = measured by origlib tests; MISC 1.2 = reference_mod MISC_DATA_FILES.md; NATIVE = AI_TacticsMod/docs/NATIVE_FUNCTIONS.md):
  +0 u32  cell index (== position, 48400/48400, MEAS)
  +4 u8   terrain id (fixdata terrain table id 8, 24 distinct values; NATIVE 'Tile+0x10')
  +5 u8   always 0
  +6 u16  area (지역) number 0..343 (0 = sea/none; 'cell -> area' oracle: every area's center cell has that area, test_origlib)
  +8 u8   0/1/2   (22 cells non-zero)                                   -> 미해결
  +9 u8   0..6    (6 on 34169 cells)                                    -> 미해결
  +10..+13 u8 flags (0/1: 591/395/187/195 cells)                        -> 미해결
  +14 u8  0..15 (16 values)                                             -> 미해결
  +15 u8  0/1 (38 cells)                                                -> 미해결
"""
import struct
from functools import lru_cache
from .s14 import GAME

W = H = 220
N = W * H


class MapBin:
    def __init__(self, exce=True):
        self.path = GAME / '0000' / ('MapExCe.bin' if exce else 'Map.bin')
        self.raw = self.path.read_bytes()
        assert struct.unpack_from('<I', self.raw)[0] == N and len(self.raw) == 4 + 16 * N

    def cell(self, i):
        r = self.raw[4 + i * 16:20 + i * 16]
        return dict(index=struct.unpack_from('<I', r)[0], terrain=r[4], area=struct.unpack_from('<H', r, 6)[0],
                    u8=r[8], u9=r[9], flags=list(r[10:14]), u14=r[14], u15=r[15], _raw=r)

    def terrain(self, i):
        return self.raw[4 + i * 16 + 4]

    def area(self, i):
        return struct.unpack_from('<H', self.raw, 4 + i * 16 + 6)[0]

    @staticmethod
    def xy(i):
        return i % W, i // W

    @staticmethod
    def index(x, y):
        return y * W + x

    def at(self, x, y):
        return self.cell(y * W + x)

    def terrain_grid(self):
        return [self.raw[4 + i * 16 + 4] for i in range(N)]


@lru_cache(None)
def load_map(exce=True):
    return MapBin(exce)
