"""LWC (Koei 삼국지14) 압축 해제 — San14EditorPKKO.exe 디코더 역어셈블 기반.

컨테이너:
    "LWC\x1a" | u32 raw_size | u32 comp_size | u8[256] 심볼표 | 비트스트림(comp_size)
    * comp_size 는 256바이트 심볼표를 포함하지 않는다.
    * comp_size == raw_size 이면 비압축 저장 (스트림을 그대로 복사).

심볼 코드 (MSB first):
    prefix = 1 이 (n-1) 개 + 0 한 개        -> n (= 선행 1비트 수 + 1)
    payload = n 비트
    value  = payload + 2**n - 2             -> n=1:0~1, n=2:2~5, n=3:6~13, ...
    (게임 내 tableA[byte]=선행1비트수+1, tableB[n]=2**n-2 로 구현되어 있음)

본문 디코드 루프:
    sym = decode()
    sym <  256 : 리터럴  -> symtab[sym] 출력
    sym >= 256 : 매치    -> dist = sym-256, len = decode()+3,
                            dist 만큼 뒤에서 len 바이트 바이트단위 복사(겹침 허용)
"""
import struct

MAGIC = b'LWC\x1a'

def _lead1(b):
    n = 0
    while n < 8 and (b >> (7 - n)) & 1:
        n += 1
    return n

_TABA = [_lead1(b) + 1 for b in range(256)]          # 게임 0x140042680
_TABB = [0] + [(1 << n) - 2 for n in range(1, 64)]   # 게임 0x140042580


class BitReader:
    __slots__ = ("d", "p", "cur", "avail")

    def __init__(self, data):
        self.d = data
        self.p = 0
        self.cur = 0      # 좌측 정렬된 현재 바이트의 남은 비트
        self.avail = 0

    def decode(self):
        d = self.d
        n = 0
        k = _TABA[self.cur & 0xFF]
        if k > self.avail:
            while True:
                n += self.avail
                b = d[self.p]; self.p += 1
                self.cur = b
                self.avail = 8
                k = _TABA[b]
                if k <= 8:
                    break
        n += k
        cur = (self.cur << k) & 0xFF          # prefix 비트 소비
        avail = self.avail - k

        if n <= avail:                         # payload 가 현재 바이트 안에서 해결
            val = (cur << n) >> 8
            self.cur = (cur << n) & 0xFF
            self.avail = avail - n
        else:                                  # 바이트 경계를 넘는 payload
            need = n - avail
            acc = (cur >> (8 - avail)) if avail else 0
            b = d[self.p]; self.p += 1
            if need > 8:
                whole = ((need - 9) >> 3) + 1
                need -= whole * 8
                for _ in range(whole):
                    acc = (acc << 8) | b
                    b = d[self.p]; self.p += 1
            val = ((b << need) >> 8) | (acc << need)
            self.cur = (b << need) & 0xFF
            self.avail = 8 - need
        return val + _TABB[n]


def find_blob(data, start=0):
    o = data.find(MAGIC, start)
    if o < 0:
        raise ValueError("LWC 블록 없음")
    return o


def decompress(data, off=None):
    """LWC 블록을 풀어 bytes 를 돌려준다. off 생략 시 매직을 찾는다."""
    if off is None:
        off = find_blob(data)
    if data[off:off+4] != MAGIC:
        raise ValueError("LWC 매직 불일치")
    raw, comp = struct.unpack_from('<II', data, off + 4)
    symtab = data[off+12:off+12+256]
    stream = data[off+268:off+268+comp]
    if len(stream) != comp:
        raise ValueError(f"스트림 잘림: {len(stream)} != {comp}")
    if comp == raw:                            # 비압축 저장
        return bytes(stream)
    br = BitReader(stream)
    out = bytearray()
    while len(out) < raw:
        sym = br.decode()
        if sym < 0x100:
            out.append(symtab[sym])
        else:
            dist = sym - 0x100
            if dist == 0 or dist > len(out):
                raise ValueError(f"매치 거리 오류 dist={dist} at out={len(out)}")
            ln = br.decode() + 3
            i = len(out) - dist
            for _ in range(ln):
                out.append(out[i]); i += 1
    return bytes(out)


def decompress_file(path):
    return decompress(open(path, 'rb').read())
