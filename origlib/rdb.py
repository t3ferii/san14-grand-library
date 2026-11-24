"""San14 원작 0002 *.rdb (+ .rdb.bin<뱅크>) 컨테이너 읽기 (읽기 전용, 표준 라이브러리만).

형식 요약(상세: San14Sim/docs/orig/data_formats_archives.md)
  <name>.rdb           = 색인. "_DRK0000" 헤더(0x20바이트) + IDRK0000 항목 N개(4바이트 정렬).
  <name>.rdb.bin[뱅크] = 본문 묶음. 항목마다 "IDRK0000" 머리 + 16KB 단위 zlib 조각들 + 길이0 조각.
  항목 위치 문자열(색인 항목 꼬리): "<오프셋hex>@<크기hex>[#<뱅크hex>[&<하위hex>]"
       뱅크 b → 파일 <name>.rdb.bin{b 10진, 0이면 생략}, 하위 s가 있으면 뒤에 "_{s}".
API
  a = open('ScreenLayout')      # 또는 'ScreenLayout.rdb'
  a.entries                     # [Entry...]
  a.read(ktid)                  # 압축 해제된 본문 bytes (Entry도 가능)
  a.raw(entry)                  # IDRK 원시 바이트(머리+조각)
  list_archives(), open_data_file(path), open_bin0005(...)는 bin0005.py 참조
"""
from __future__ import annotations

import builtins
import mmap
import os
import re
import struct
import zlib
from dataclasses import dataclass, field
from pathlib import Path

try:
    from .s14 import GAME as ROOT
except ImportError:
    ROOT = Path(__file__).resolve().parents[2]
DIR0002 = ROOT / '0002'
RDB_NAMES = ['system', 'KIDSSystemResource', 'ScreenLayout', 'FieldEditor4',
             'CharacterEditor', 'MaterialEditor', 'RRPreview']

_LOC = re.compile(r'([0-9a-f]+)@([0-9a-f]+)(?:#([0-9a-f]+))?(?:&([0-9a-f]+))?$')


@dataclass
class Entry:
    index: int               # 색인 안 순번
    ktid: int                # 0x24 u32 (이름/경로 해시로 추정, 해시 함수 미해결)
    typeinfo: int            # 0x28 u32 (자료 종류 해시)
    kind16: int              # 0x2e u16 (0x12=위치 문자열 있음, 0x11/0x01=위치 없음 참조 항목)
    aux: int                 # 0x20 u32
    dsize: int               # 0x18 u64 (압축 해제 크기, 위치 없는 항목은 별도 의미)
    index_offset: int
    index_size: int
    head_extra: bytes        # 0x2c 이후 위치 문자열 앞까지(형식 매개 해시 열)
    locator: str             # 위치 문자열(없으면 '')
    offset: int | None = None
    entry_size: int | None = None
    bank: int | None = None
    sub: int | None = None
    bank_file: str | None = None

    @property
    def has_body(self) -> bool:
        return self.offset is not None


def bank_filename(name: str, bank: int, sub: int | None) -> str:
    s = f'{name}.rdb.bin' + (str(bank) if bank else '')
    if sub is not None:
        s += f'_{sub}'
    return s


def parse_index(path: Path, name: str | None = None):
    """색인 파일을 스트리밍 없이(색인은 최대 1.6MB) 읽어 (헤더dict, [Entry])."""
    path = Path(path)
    name = name or path.name[:-len('.rdb')]
    d = path.read_bytes()
    if d[:8] != b'_DRK0000':
        raise ValueError(f'{path}: _DRK0000 아님')
    hs, h12, count, hhash = struct.unpack_from('<IIII', d, 8)
    out = []
    p = hs
    i = 0
    while p < len(d):
        if d[p:p + 8] != b'IDRK0000':
            raise ValueError(f'{path}: 오프셋 {p:#x}에 IDRK0000 없음')
        size = struct.unpack_from('<I', d, p + 8)[0]
        ln, dsz = struct.unpack_from('<QQ', d, p + 0x10)
        aux, ktid, typ = struct.unpack_from('<III', d, p + 0x20)
        kind16 = struct.unpack_from('<H', d, p + 0x2e)[0]
        e = d[p:p + size]
        headlen = size - ln
        loc = e[headlen:].rstrip(b'\0').decode('ascii') if ln else ''
        ent = Entry(i, ktid, typ, kind16, aux, dsz, p, size, bytes(e[0x30:headlen]), loc)
        m = _LOC.match(loc) if loc else None
        if m:
            ent.offset = int(m[1], 16)
            ent.entry_size = int(m[2], 16)
            ent.bank = int(m[3], 16) if m[3] else 0
            ent.sub = int(m[4], 16) if m[4] else None
            ent.bank_file = bank_filename(name, ent.bank, ent.sub)
        elif loc:
            raise ValueError(f'{path}: 알 수 없는 위치 문자열 {loc!r}')
        out.append(ent)
        p += (size + 3) & ~3
        i += 1
    if p != len(d) or i != count:
        raise ValueError(f'{path}: 항목 수/끝 불일치 {i}/{count} {p}/{len(d)}')
    return {'header_size': hs, 'field12': h12, 'count': count, 'hash': hhash}, out


def decompress_entry(raw, first_chunk_only: bool = False) -> bytes:
    """IDRK 원시 바이트 → 본문. 머리 0x30에 CRC32(압축부), 0x08 전체, 0x10 압축부, 0x18 원 크기."""
    if raw[:8] != b'IDRK0000':
        raise ValueError('IDRK0000 아님')
    total, csz, dsz = struct.unpack_from('<QQQ', raw, 8)
    q = len(raw) - csz
    out = bytearray()
    while q < len(raw):
        n = struct.unpack_from('<I', raw, q)[0]
        q += 4
        if not n:
            break
        out += zlib.decompressobj().decompress(raw[q:q + n])
        q += n
        if first_chunk_only:
            return bytes(out)
    if len(out) != dsz:
        raise ValueError(f'해제 크기 불일치 {len(out)} != {dsz}')
    return bytes(out)


class Archive:
    def __init__(self, name: str, root: Path | None = None):
        if name.endswith('.rdb'):
            name = name[:-4]
        self.name = name
        self.dir = Path(root) if root else DIR0002
        self.path = self.dir / (name + '.rdb')
        self.header, self.entries = parse_index(self.path, name)
        self.by_ktid: dict[int, list[Entry]] = {}
        for e in self.entries:
            self.by_ktid.setdefault(e.ktid, []).append(e)
        self._maps: dict[str, tuple] = {}

    # --- 뱅크 파일 mmap ---
    def _bank(self, fname: str):
        m = self._maps.get(fname)
        if m is None:
            f = builtins.open(self.dir / fname, 'rb')
            mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            m = (f, mm)
            self._maps[fname] = m
        return m[1]

    def close(self):
        for f, mm in self._maps.values():
            mm.close()
            f.close()
        self._maps.clear()

    def __enter__(self):
        return self

    def __exit__(self, *a):
        self.close()

    def _entry(self, key, which: int = 0) -> Entry:
        if isinstance(key, Entry):
            return key
        lst = self.by_ktid[key]
        return lst[which]

    def raw(self, key, which: int = 0) -> bytes:
        e = self._entry(key, which)
        if not e.has_body:
            raise KeyError('본문 위치 없는 항목')
        mm = self._bank(e.bank_file)
        return mm[e.offset:e.offset + e.entry_size]

    def read(self, key, which: int = 0, first_chunk_only: bool = False) -> bytes:
        return decompress_entry(self.raw(key, which), first_chunk_only)

    def head(self, key, n: int = 16, which: int = 0) -> bytes:
        """본문 앞 n바이트(첫 조각만 해제)."""
        return self.read(key, which, True)[:n]

    def bank_files(self):
        return sorted({e.bank_file for e in self.entries if e.bank_file})


def open(name: str, root: Path | None = None) -> Archive:  # noqa: A001 (API 이름 요구)
    return Archive(name, root)


def list_archives(root: Path | None = None):
    d = Path(root) if root else DIR0002
    return [n for n in RDB_NAMES if (d / (n + '.rdb')).exists()]


# ======================================================================
# 형식 식별·해독 도우미 (분류표는 docs/orig/data_formats_archives.md 3절)
# ======================================================================
import json  # noqa: E402

# typeinfo → (이름, 분류, 확신도, 설명)
TYPE_TABLE = {
    0xafbec60c: ('G1T_texture', 'graphics', '확정', 'GT1G0600 텍스처(BC3 0x5b 등). 픽셀 해독은 범위 밖'),
    0xf20de437: ('sprite_table', 'ui', '확정', '스프라이트 표: u32 개수 + 104바이트 레코드(이름64 + 쪽u32 + uv8f + u32)'),
    0x5599aa51: ('LCSK_layout', 'ui', '확정', 'LCSK 화면 레이아웃 (AI_TacticsMod/research/ui_atlas/build_layouts.py가 부품까지 해독)'),
    0xf13845ef: ('ui_param_array', 'ui', '추정', 'ScreenLayout 8개. u32 개수 + 0x0f + 0 채움 + 값들(532B). 용도 미해독'),
    0x20a6a0bb: ('KIDS_DOK', 'engine_data', '확정(구조)/추정(속성)', '_DOK0000 객체 DB: IDOK0000 객체 열(크기·객체ID·클래스해시·속성). 스크립트·엔진 설정 객체, 게임 규칙 아님'),
    0xbf6b52c7: ('external_stub', 'ref', '확정(구조)/미해결(대상)', '위치 문자열 없는 항목(kind16=0x11). dsize=외부 자원 크기, 대상 미확인. rdb마다 마지막 1개는 rdb 자체(ktid=헤더 해시)'),
    0x7bcd279f: ('S2G_resource', 'shader', '추정', '_S2G3000 system.rdb 22589개(약 30KB). 셰이더/효과 묶음으로 추정'),
    0x563bdef1: ('M1G_model', 'model', '확정(형식)', '_M1G73xx 3D 모델'),
    0xbe144b78: ('text_texture_index', 'graphics', '확정', 'UTF-8 BOM 텍스트 "texture index,filename" 목록'),
    0xbd05b27: ('text_shader_list', 'shader', '확정', 'UTF-8 텍스트 "; Sha..." 셰이더 목록'),
    0xb1630f51: ('RGK_resource', 'shader', '추정', '_RGK0000 (INGK 조각). 렌더 그래프/키 자원 추정'),
    0x1fdcaa40: ('TGK_resource', 'shader', '추정', '_TGK0000 (INGK 조각)'),
    0x56d8deda: ('CE1Resource_text', 'shader', '확정', 'ShaderID/CE1Resource 텍스트 표'),
    0xd7f47fb1: ('raw_buffer', 'model', '추정', '정점/인덱스/_DVS1000/_MHK0100 등 원시 버퍼'),
    0x8e39aa37: ('model_aux_a', 'model', '추정', '모델별 32~96B 보조 배열'),
    0x1ab40ae8: ('model_aux_b', 'model', '추정', '모델별 u32 개수 + 배열'),
    0xb340861a: ('model_aux_c', 'model', '추정', '모델별 u32 개수 2개 + 배열'),
    0x56efe45c: ('model_aux_d', 'model', '추정', '모델별 32B 보조'),
    0x5c3e543c: ('SWGQ_param', 'model', '추정', 'SWGQ 매개(396B)'),
    0xed410290: ('GSTK_material', 'model', '확정(형식)', 'GSTK 재질'),
    0x54738c76: ('OC1G_occlusion', 'model', '추정', 'OC1G 형식'),
    0x82945a44: ('field_param', 'model', '미해결', 'FieldEditor4 2개(43700B)'),
    0x6fa91671: ('A1G_A2G_anim', 'model', '확정(형식)', '_A1G/_A2G 애니메이션'),
    0xb097d41f: ('XF1G_skeleton', 'model', '추정', 'XF1G 형식'),
    0xbbd39f2d: ('ASRS_sound', 'audio', '확정(형식)', 'ASRS/KTSR 소리 묶음(제외, 목록만)'),
    0x786dcd84: ('N1G_resource', 'model', '추정', '_N1G0000'),
    0x4d0102ac: ('ME1G_resource', 'model', '추정', 'ME1G1000'),
    0xb0a14534: ('CGRS_resource', 'model', '추정', 'CGRS'),
    0xd34474d: ('external_data_file', 'audio', '확정', '0002/data/<ktid>.file 참조 스텁. 파일 내용 TSRS/KTSR(소리)'),
    0xa027e46b: ('external_data_file_empty', 'ref', '확정', '0002/data/<ktid>.file 참조 스텁(내용 0바이트)'),
}

# 본문 앞 4바이트 → 형식 이름
MAGICS = {b'GT1G': 'G1T', b'LCSK': 'LCSK', b'_DOK': 'DOK', b'_M1G': 'M1G', b'_S2G': 'S2G', b'_RGK': 'RGK',
          b'_TGK': 'TGK', b'_A1G': 'A1G', b'_A2G': 'A2G', b'_N1G': 'N1G', b'ME1G': 'ME1G', b'XF1G': 'XF1G',
          b'OC1G': 'OC1G', b'GSTK': 'GSTK', b'SWGQ': 'SWGQ', b'ASRS': 'ASRS', b'KTSR': 'KTSR', b'CGRS': 'CGRS',
          b'_DVS': 'DVS', b'_MHK': 'MHK', b'TSRS': 'TSRS'}

_LANG_RE = re.compile(r'^(kr|en|jp|ch|cn|tw)_|_(kr|en|jp|ch|cn|tw)$')
KO_TOKENS = {'kr'}


def lang_tokens(names) -> set:
    t = set()
    for n in names:
        m = _LANG_RE.search(n)
        if m:
            t.add(m[1] or m[2])
    return t


def lang_class(tokens) -> str:
    """'neutral'(언어 표지 없음) / 'ko' / 'mixed'(ko+타언어) / 'foreign'(타언어만) — 한국어(KO)만 해독 정책용."""
    if not tokens:
        return 'neutral'
    if tokens <= KO_TOKENS:
        return 'ko'
    if tokens & KO_TOKENS:
        return 'mixed'
    return 'foreign'


def parse_sprite_table(b: bytes):
    """f20de437 본문 → [{name,page,uv[8],flag}]."""
    c = struct.unpack_from('<I', b)[0]
    if 4 + 104 * c != len(b):
        raise ValueError('스프라이트 표 크기 불일치')
    out = []
    for i in range(c):
        o = 4 + 104 * i
        name = b[o:o + 64].split(b'\0')[0].decode('latin1')
        vals = struct.unpack_from('<I8fI', b, o + 64)
        out.append({'name': name, 'page': vals[0], 'uv': [round(x, 6) for x in vals[1:9]], 'flag': vals[9]})
    return out


def parse_g1t_head(b: bytes):
    """GT1G0600 첫 텍스처 (w,h,fmt,mip, 개수)."""
    fs, to, cnt = struct.unpack_from('<III', b, 8)
    offs = struct.unpack_from('<%dI' % cnt, b, to)
    h = to + offs[0]
    return {'ver': b[:8].decode('latin1'), 'count': cnt, 'fmt': b[h + 1], 'w': 1 << (b[h + 2] & 15),
            'h': 1 << (b[h + 2] >> 4), 'mip': b[h] >> 4}


def parse_dok(b: bytes):
    """_DOK0000 → (헤더, [(offset,size,objid,classhash)]). 속성 해독은 미완(속성=12바이트 3열 추정)."""
    if b[:8] != b'_DOK0000':
        raise ValueError('_DOK0000 아님')
    hs, ver, n, hh, total = struct.unpack_from('<IIIII', b, 8)
    objs = []
    p = hs
    while p < len(b):
        if b[p:p + 8] != b'IDOK0000':
            break   # 객체 없는 작은 DOK(28~140바이트)는 머리 뒤에 다른 꼬리가 있다
        size, oid, cls = struct.unpack_from('<III', b, p + 8)
        objs.append((p, size, oid, cls))
        p += (size + 3) & ~3   # 객체는 4바이트 정렬
    return {'header_size': hs, 'version': ver, 'count': n, 'hash': hh, 'total': total, 'trailer': len(b) - p}, objs


@dataclass(frozen=True)
class LayoutResource:
    wrapper: int
    setting: int
    layout: int


def layout_name_hash(name: str) -> int:
    """Hash an ASCII layout name as the original loader does."""
    key = 0
    power = 1
    for byte in name.encode('ascii'):
        power = (power * 31) & 0xffffffff
        key = (key + byte * power) & 0xffffffff
    return key


def read_layout_registry(root: Path | None = None) -> dict[int, LayoutResource]:
    """Read common setting and resolve its layout rows against the installed RDBs."""
    with open('KIDSSystemResource', root) as archive:
        common = archive.read(0x6d011726)
        resources = archive.read(0x208be13a)
    _, objects = parse_dok(common)
    settings = next(
        (obj for obj in objects if obj[2:] == (0x61ad16cf, 0xdac911d7)), None
    )
    if settings is None:
        raise ValueError('common setting 객체 없음')

    offset, size, _, _ = settings
    fields = struct.unpack_from('<I', common, offset + 20)[0]
    cursor = offset + 24 + 12 * fields
    columns = {}
    column_keys = (0x10fa95c2, 0xb45b5e75, 0x1bf404e7)
    for i in range(fields):
        kind, count, key = struct.unpack_from('<III', common, offset + 24 + 12 * i)
        if kind not in (1, 5):
            raise ValueError(f'common setting 속성 형식 {kind}')
        end = cursor + count * (4 if kind == 5 else 1)
        if end > offset + size:
            raise ValueError('common setting 속성이 객체 경계를 넘음')
        if key in column_keys:
            if kind != 5 or key in columns:
                raise ValueError(f'잘못된 레이아웃 속성 {key:08x}')
            columns[key] = struct.unpack_from(f'<{count}I', common, cursor)
        cursor = end
    if cursor != offset + size or set(columns) != set(column_keys):
        raise ValueError('common setting 레이아웃 표가 불완전함')

    _, objects = parse_dok(resources)
    wrappers, references = {}, {}
    for offset, size, object_id, kind in objects:
        if kind == 0x63336873:
            output, property_key = wrappers, 0x15be61ad
        elif kind == 0xa1a84f2c:
            output, property_key = references, 0x91ce400e
        else:
            continue
        count, value_type, value_count, key = struct.unpack_from('<4I', resources, offset + 20)
        if (value_type, value_count, key) != (5, 1, property_key) or 28 + 12 * count > size:
            raise ValueError(f'잘못된 레이아웃 참조 객체 {object_id:08x}')
        output[object_id] = struct.unpack_from('<I', resources, offset + 24 + 12 * count)[0]

    with open('ScreenLayout', root) as archive:
        layouts = {entry.ktid for entry in archive.entries if entry.has_body and entry.typeinfo == 0x5599aa51}
    rows = {}
    for key, wrapper, setting in zip(*(columns[key] for key in column_keys), strict=True):
        layout = wrappers.get(wrapper)
        if key in rows or references.get(setting) != wrapper or layout not in layouts:
            raise ValueError(f'레이아웃 등록표 불일치 {key:08x}')
        rows[key] = LayoutResource(wrapper, setting, layout)
    return rows


def parse_lcsk_head(b: bytes):
    """LCSK 머리: 버전, 전체 크기(+8), 노드 수(섹션 1 +0x12 u16), 섹션 목록. 부품 해독은 ui_atlas/build_layouts.py."""
    secs = []
    nodes = None
    p = 0x4c
    while p + 8 <= len(b):
        k, sz = struct.unpack_from('<II', b, p)
        if sz < 8 or p + sz > len(b):
            break
        secs.append((k, sz))
        if k == 1 and sz >= 0x14 and nodes is None:
            nodes = struct.unpack_from('<H', b, p + 0x12)[0]
        p += sz
    names = re.findall(rb'[A-Za-z][A-Za-z0-9_]{3,}', b[-max(64, len(b) // 2):])
    return {'ver': b[:8].decode('latin1'), 'size': struct.unpack_from('<I', b, 8)[0],
            'nodes': nodes,
            'sections': secs}, [n.decode('latin1') for n in names]


_FULL_READ = (0x20a6a0bb, 0xf20de437, 0x5599aa51, 0xf13845ef, 0xbe144b78, 0xbd05b27, 0x56d8deda)


def classify(a: 'Archive', e: Entry):
    """항목 하나의 요약 dict (jsonl 한 줄). 본문은 필요한 만큼만 읽는다."""
    t = TYPE_TABLE.get(e.typeinfo, ('unknown', 'unknown', '미해결', ''))
    rec = {'archive': a.name, 'idx': e.index, 'ktid': f'{e.ktid:08x}', 'type': f'{e.typeinfo:08x}',
           'type_name': t[0], 'category': t[1], 'dsize': e.dsize, 'kind16': e.kind16}
    if not e.has_body:
        rec['stub'] = True
        rec['data_file'] = (f'0002/data/0x{e.ktid:08x}.file' if e.typeinfo in (0xd34474d, 0xa027e46b) else None)
        rec['lang'] = 'neutral'
        return rec
    rec.update(locator=e.locator, bank_file=e.bank_file, offset=e.offset, entry_size=e.entry_size)
    full = e.typeinfo in _FULL_READ and e.dsize <= 64 * 1024 * 1024
    body = a.read(e) if full else a.read(e, first_chunk_only=True)
    magic = body[:4]
    rec['magic'] = MAGICS.get(magic, 'text' if body[:3] in (b'\xef\xbb\xbf', b';\r\n') else magic.hex())
    lang = 'neutral'
    try:
        if e.typeinfo == 0xafbec60c:
            rec['info'] = parse_g1t_head(body)
        elif e.typeinfo == 0xf20de437:
            sp = parse_sprite_table(body)
            rec['info'] = {'sprites': len(sp), 'first': sp[0]['name'] if sp else None}
            tok = lang_tokens(s['name'] for s in sp)
            lang = lang_class(tok)
            rec['lang_tokens'] = sorted(tok)
        elif e.typeinfo == 0x5599aa51:
            head, names = parse_lcsk_head(body)
            rec['info'] = {'ver': head['ver'], 'nodes': head['nodes'], 'sections': len(head['sections'])}
            tok = lang_tokens(names)
            lang = lang_class(tok)
            rec['lang_tokens'] = sorted(tok)
        elif e.typeinfo == 0x20a6a0bb:
            head, objs = parse_dok(body)
            rec['info'] = {'objects': len(objs), 'declared': head['count'], 'ok': len(objs) == head['count']}
        elif body[:4] == b'_M1G':
            rec['info'] = {'ver': body[:8].decode('latin1')}
        elif body[:4] in (b'ASRS', b'KTSR'):
            rec['info'] = {'ver': body[:8].hex()}
    except Exception as ex:  # 형식 해독 실패는 기록만
        rec['info_error'] = str(ex)[:80]
    rec['lang'] = lang
    return rec


def export_catalog(outdir, names=None, sprites_ko=True, log=print):
    """모든 rdb 항목 목록을 outdir/<rdb>.jsonl로, KO·중립 스프라이트 표 내용을 sprites_ko.jsonl로 쓴다.
    원본 내용 사본은 만들지 않는다(요약만). 반환: {rdb: 항목수}."""
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    counts = {}
    spr = builtins.open(outdir / 'sprites_ko.jsonl', 'w', encoding='utf-8') if sprites_ko else None
    for n in names or RDB_NAMES:
        with Archive(n) as a, builtins.open(outdir / f'{n}.jsonl', 'w', encoding='utf-8') as f:
            for e in a.entries:
                r = classify(a, e)
                f.write(json.dumps(r, ensure_ascii=False) + '\n')
                if spr and e.typeinfo == 0xf20de437 and r.get('lang') in ('neutral', 'ko', 'mixed'):
                    sp = parse_sprite_table(a.read(e))
                    spr.write(json.dumps({'archive': n, 'ktid': r['ktid'], 'lang': r['lang'], 'sprites': sp},
                                         ensure_ascii=False) + '\n')
            counts[n] = len(a.entries)
        log(n, counts[n])
    if spr:
        spr.close()
    return counts


# ----------------------------------------------------------------------
# 0002/data/0x<ktid>.file : 단일 IDRK 항목 파일(외부 자원). 압축 조각 없이 원시 저장(압축부 == 원 크기).
#   머리 0x38바이트 + 원시 본문. 본문은 TSRS/KTSR(소리 묶음) → 제외 대상, 목록만.
# ----------------------------------------------------------------------
def open_data_file(path_or_ktid, root: Path | None = None) -> dict:
    """data/*.file 한 개의 머리 정보를 읽는다(본문은 읽지 않음). 본문은 read_data_file()."""
    d = Path(root) if root else DIR0002
    p = Path(path_or_ktid) if not isinstance(path_or_ktid, int) else d / 'data' / f'0x{path_or_ktid:08x}.file'
    with builtins.open(p, 'rb') as f:
        h = f.read(0x40)
    if h[:8] != b'IDRK0000':
        raise ValueError(f'{p}: IDRK0000 아님')
    total, csz, dsz = struct.unpack_from('<QQQ', h, 8)
    aux, ktid, typ = struct.unpack_from('<III', h, 0x20)
    crc = struct.unpack_from('<I', h, 0x30)[0]
    return {'path': str(p), 'total': total, 'csize': csz, 'dsize': dsz, 'ktid': ktid, 'type': typ, 'crc32': crc,
            'raw_stored': csz == dsz, 'head_size': total - csz, 'magic': h[0x38:0x40].decode('latin1') if total > 0x38 else ''}


def read_data_file(path_or_ktid, offset: int = 0, size: int | None = None, root: Path | None = None) -> bytes:
    """data/*.file 본문(헤더 뒤) 일부를 읽는다. 대용량(최대 185MB)이므로 범위 지정 권장."""
    info = open_data_file(path_or_ktid, root)
    if not info['raw_stored']:
        raise NotImplementedError('압축 조각형 data 파일은 없음(전수 확인 12개 모두 원시 저장)')
    n = info['dsize'] - offset if size is None else size
    with builtins.open(info['path'], 'rb') as f:
        f.seek(info['head_size'] + offset)
        return f.read(n)


def export_data_files(outdir, root: Path | None = None):
    """0002/data/*.file 목록 jsonl (소리: 목록만)."""
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    d = Path(root) if root else DIR0002
    refs = {}
    with Archive('RRPreview', d) as a:
        for e in a.entries:
            if not e.has_body and e.typeinfo in (0xd34474d, 0xa027e46b):
                refs[e.ktid] = e
    n = 0
    with builtins.open(outdir / 'data_files.jsonl', 'w', encoding='utf-8') as out:
        for p in sorted((d / 'data').glob('*.file')):
            info = open_data_file(p)
            info['path'] = str(p.relative_to(d.parent)).replace('\\', '/')
            info['type_name'] = TYPE_TABLE.get(info['type'], ('unknown',))[0]
            info['category'] = 'audio' if info['dsize'] else 'ref'
            info['referenced_by'] = f'RRPreview.rdb idx {refs[info["ktid"]].index}' if info['ktid'] in refs else None
            info['lang'] = 'neutral'
            out.write(json.dumps(info, ensure_ascii=False) + '\n')
            n += 1
    return n
