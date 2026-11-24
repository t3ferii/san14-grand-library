"""San14 원작 0005/00N.bin 읽기 (읽기 전용, 표준 라이브러리만).

형식(확정, 전수 확인: 000=300개, 001=45개, 002=300개, 모두 끝까지 정확히 맞음)
  파일 = u32 개수 N, 이어서 N × (u32 오프셋, u32 크기) 표(오프셋은 파일 처음 기준, 표 끝=첫 항목 시작),
         그 뒤 항목 본문이 빈틈 없이 이어짐 (오프셋[i]+크기[i] == 오프셋[i+1], 마지막은 파일 끝).
  항목 = "zp1\\0" 압축 묶음:
         +4 u32 압축 해제 전체 크기, +8 u32 조각 크기(0x40000), +12 u32 조각 수 K, +16 K×u32 조각 저장 크기(앞 4바이트 길이 포함),
         조각들은 0x800에서 시작, 0x80 정렬. 조각 = u32(저장크기-4) + zlib 스트림.
         (같은 zp1 형식을 0001_KO/msg*.bin 메시지 표도 쓴다: AI_TacticsMod/research/ui_atlas/read_messages.py)
  해제 결과 = GT1G0600 텍스처 한 장(BC3, fmt 0x5b). 파일마다 2048x1024,
  512x512, 1024x1024 순서로 세 구간이며 구간별 000/002는 100개, 001은 15개다.
  현재 EXE의 등록과 로딩식에 따르면 6000~6214의 같은 얼굴은 세 구간의 같은 순번이다.
  DLC/0005/003.bin에는 같은 형식으로 6215~6244에 대응하는 30명분이 있다.
API
  a = open(0)             # 0,1,2 또는 '000'
  a.entries               # [(오프셋, 크기)]
  a.read(i)               # 해제된 G1T 바이트
  a.head(i)               # {w,h,fmt,count,ver,...} (첫 조각만 해제)
  portrait_location(id, kind) # (파일 번호, 항목 인덱스), kind는 9/10/11
  portrait_identity(n, i)  # (얼굴 번호, 종류), location의 역변환
  export_catalog(outdir)  # bin0005.jsonl
"""
from __future__ import annotations

import builtins
import json
import mmap
import struct
import zlib
from pathlib import Path

try:
    from .s14 import GAME as ROOT
except ImportError:
    ROOT = Path(__file__).resolve().parents[2]
DIR0005 = ROOT / '0005'
PORTRAIT_RANGES = ((6000, 100), (6100, 15), (6115, 100), (6215, 30))


def portrait_location(face_id: int, kind: int) -> tuple[int, int]:
    """등록된 얼굴 번호와 종류를 묶음 번호·0 기반 항목 인덱스로 변환한다.

    6215~6244의 003.bin은 설치본의 DLC/0005에만 있을 수 있다.
    실제 게임의 DLC 사용 가능 여부는 이 함수에서 판정하지 않는다.
    """
    if kind not in (9, 10, 11):
        raise ValueError('얼굴 종류는 9, 10, 11 중 하나여야 한다')
    for number, (start, count) in enumerate(PORTRAIT_RANGES):
        if start <= face_id < start + count:
            return number, (kind - 9) * count + face_id - start
    raise ValueError('0005에 등록된 얼굴 번호가 아니다')


def portrait_identity(number: int, index: int) -> tuple[int, int]:
    """묶음 번호와 0 기반 항목 인덱스를 (얼굴 번호, 종류 9/10/11)로 변환한다."""
    if not isinstance(number, int) or not 0 <= number < len(PORTRAIT_RANGES):
        raise ValueError('등록된 초상화 묶음 번호가 아니다')
    start, count = PORTRAIT_RANGES[number]
    if not isinstance(index, int) or not 0 <= index < count * 3:
        raise ValueError('초상화 항목 인덱스가 범위를 벗어났다')
    group, offset = divmod(index, count)
    return start + offset, 9 + group


def unpack_zp1(d, first_chunk_only: bool = False) -> bytes:
    # 원작 30AB30과 같은 규칙: 마지막이 아닌 조각은 크기 칸이 조각 크기 이상이면 압축 없이 그 크기만큼 복사하고,
    # 마지막 조각은 머리 +3 바이트의 비트 2가 켜져 있으면 복사한다(나머지는 u32 길이 + zlib).
    if bytes(d[:3]) != b'zp1' or d[3] & ~2:
        raise ValueError('zp1 아님')
    total, chunk, count = struct.unpack_from('<III', d, 4)
    sizes = struct.unpack_from('<%dI' % count, d, 16)
    p = 0x800
    out = bytearray()
    for i, n in enumerate(sizes):
        last = i == count - 1
        piece = (total % chunk or chunk) if last else chunk
        if (last and d[3] & 2) or (not last and n >= piece):
            out += bytes(d[p:p + piece])
            p = (p + n + 0x7f) & ~0x7f
            if first_chunk_only:
                return bytes(out)
            continue
        sz = struct.unpack_from('<I', d, p)[0]
        if sz != n - 4:
            raise ValueError('zp1 조각 길이 불일치')
        out += zlib.decompress(bytes(d[p + 4:p + n]))
        p = (p + n + 0x7f) & ~0x7f
        if first_chunk_only:
            return bytes(out)
    if len(out) != total:
        raise ValueError(f'zp1 해제 크기 불일치 {len(out)} != {total}')
    return bytes(out)


class Bin0005:
    def __init__(self, n, root: Path | None = None):
        n = int(n) if not isinstance(n, int) else n
        self.n = n
        self.path = (Path(root) if root else DIR0005) / f'{n:03d}.bin'
        self._f = builtins.open(self.path, 'rb')
        self._m = mmap.mmap(self._f.fileno(), 0, access=mmap.ACCESS_READ)
        cnt = struct.unpack_from('<I', self._m, 0)[0]
        self.entries = [struct.unpack_from('<II', self._m, 4 + 8 * i) for i in range(cnt)]
        ok = self.entries[0][0] == 4 + 8 * cnt and self.entries[-1][0] + self.entries[-1][1] == len(self._m) and all(
            self.entries[i][0] + self.entries[i][1] == self.entries[i + 1][0] for i in range(cnt - 1))
        if not ok:
            raise ValueError(f'{self.path}: 표가 연속 구조가 아님')

    def close(self):
        self._m.close()
        self._f.close()

    def __enter__(self):
        return self

    def __exit__(self, *a):
        self.close()

    def raw(self, i):
        o, s = self.entries[i]
        return self._m[o:o + s]

    def read(self, i) -> bytes:
        return unpack_zp1(self.raw(i))

    def head(self, i) -> dict:
        b = unpack_zp1(self.raw(i), True)
        fs, to, cnt = struct.unpack_from('<III', b, 8)
        offs = struct.unpack_from('<%dI' % cnt, b, to)
        h = to + offs[0]
        return {'ver': b[:8].decode('latin1'), 'count': cnt, 'fmt': b[h + 1], 'w': 1 << (b[h + 2] & 15),
                'h': 1 << (b[h + 2] >> 4), 'mip': b[h] >> 4}


def open(n, root: Path | None = None) -> Bin0005:  # noqa: A001
    return Bin0005(n, root)


def export_catalog(outdir, root: Path | None = None, log=print) -> dict:
    """0005/*.bin 전체 목록(순번, 오프셋, 저장 크기, 해제 크기, 조각 수, G1T 형식·가로·세로)을 bin0005.jsonl로."""
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    counts = {}
    with builtins.open(outdir / 'bin0005.jsonl', 'w', encoding='utf-8') as out:
        for n in (0, 1, 2):
            with Bin0005(n, root) as a:
                for i, (o, s) in enumerate(a.entries):
                    raw = a.raw(i)
                    total, chunk, k = struct.unpack_from('<III', raw, 4)
                    face_id, kind = portrait_identity(n, i)
                    rec = {'file': f'0005/{n:03d}.bin', 'idx': i, 'face_id': face_id, 'portrait_kind': kind,
                           'offset': o, 'size': s, 'raw_size': total,
                           'chunk': chunk, 'chunks': k, 'category': 'graphics', 'lang': 'neutral', **a.head(i)}
                    out.write(json.dumps(rec, ensure_ascii=False) + '\n')
                counts[n] = len(a.entries)
                log(n, counts[n])
    return counts
