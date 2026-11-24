"""0010_KO/sceda*.s14 (base game, v51) and scedaexce*.s14 (CE, v102) scenarios.

Plain header (754 B CE / 480 B base): +0x04 'SN14SCEXVER0001', +0x14 intro text (UTF-16LE), +0x1A6 name, +0x1C8 u16 year,
+0x1CA u8 category (1 normal, 2 tutorial, 4 new-ruler), +0x1CB u8 tier version (51/92/102), +0x1CD u8 month, +0x1CE u8 scenario number.
Body = LWC payload: [u32 ver][u32 N=1852][u16 general ids x N] then the table chain starting at body 0xE9A (CE).
Same chain convention as fixdata (<u32 id><u32 count> + count*stride).  Table ids match fixdata ids
(1 city, 2 gate, 3 force, 4 corps, 6 region, 10 general, 13 treasure, 22 trait copy, 19/31/36/38/43 scenario state).
Evidence tags: SBM = reference_mod/Modding_DOCS/format/SCENARIO_BODY_MAP.md, SGM = SAVE_GENERAL_MAP.md (scenario = save offset - 0x18),
SCF = SAVE_CITY_FACTION_MAP.md, FRM = FIXDATA_RECORD_MAP.md, EXT = San14Sim/tools/extract/extract.py, MEAS = measured here (origlib tests).
"""
import struct
from functools import lru_cache
from . import s14
from .s14 import GAME, Container, walk_chain, u16, u32
from .spec import F, decode, unresolved_of

C = '확정'
STRIDES_CE = {1: 23, 2: 20, 3: 329, 4: 4, 5: 0, 6: 8, 7: 6, 8: 0, 9: 0, 10: 316, 11: 0, 12: 0, 13: 65, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 15,
              20: 0, 21: 0, 22: 60, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0, 30: 0, 31: 213, 32: 0, 33: 0, 34: 0, 35: 0, 36: 5, 37: 0,
              38: 1, 39: 0, 40: 0, 41: 0, 42: 0, 43: 269, 100: 1741, 101: 0, 104: 0}

TABLES = {
    1: dict(key='city', ko='도시', stride=23, fields=[
        F(0, 'u16', 'governor', '태수 무장번호', 'SBM;SCF', C), F(2, 'u8', 'force', '세력(런타임 번호)', 'SBM;SCF', C),
        F(3, 'u32', 'gold', '', 'SCF;EXT', C), F(7, 'u32', 'food', '', 'SCF;EXT', C), F(11, 'u32', 'troops', '', 'SCF;EXT', C),
        F(15, 'u8', 'morale', '', 'SCF', C), F(16, 'u16', 'durability', '내구 상한', 'SCF;EXT', C), F(18, 'u8', 'tactic', '거점 전법', 'SCF', C),
        F(20, 'u8', 'size', '규모 1/2/3 = 런타임 도시 +0xB8 (덤프 1940601 51/51 일치; 시나리오 03 은 내구 2000/3000/4000 과 1:1 이나 마제 시나리오는 수춘·강릉이 규모 2 / 내구 2000). 플레이 중 개발도로 자람(rules_domestic 5절 27B4B0 규칙)', 'MEAS;DUMP', C), F(21, 'u8', 'price', '시세(전 도시 50, 추정)', 'MEAS', '추정')]),
    2: dict(key='gate', ko='관문', stride=20, fields=[
        F(0, 'u16', 'governor', '', 'SBM', C), F(2, 'u8', 'force', '', 'SBM', C), F(3, 'u32', 'gold', '전부 0 (덤프 일치)', 'MEAS;DUMP', C),
        F(7, 'u32', 'food', '전부 0 (덤프 일치)', 'MEAS;DUMP', C), F(11, 'u32', 'troops', '1000~12000 병사 (덤프 1940601 관문 52..61 병사·금 0·군량 0 와 일치, L1)', 'MEAS;DUMP', C),
        F(15, 'u8', 'morale', '', 'SCF', C), F(16, 'u16', 'durability', '5000/6000/8000', 'SCF', C), F(18, 'u8', 'tactic', '', 'SCF', C)]),
    3: dict(key='force', ko='세력', stride=329, fields=[
        F(0, 'u16', 'ruler', '군주 무장번호', 'SBM;SCF', C), F(2, 'u8x52', 'friendship', '세력간 우호도, 인덱스 = 세력 슬롯 0..51(자기 칸 = 100, 2601/2601 칸이 덤프 1940601 과 일치, L1)', 'SCF;MEAS;DUMP', C),
        F(0x36, 'u8', 'title', '작위(4~9)', 'SCF', '추정'), F(0x38, 'u8', 'color', '세력색', 'SCF;EXT', C), F(0x3B, 'u16', 'advisor', '군사 무장번호', 'SCF;EXT', C),
        F(0x104, 'u8x60', 'tactic_books', '전법서 보유(60B, 추정)', 'SBM 6', '추정')]),
    4: dict(key='corps', ko='군단', stride=4, fields=[
        F(0, 'u8', 'force', '0=빈 슬롯', 'SBM', C), F(1, 'u8', 'ordinal', '세력 안 순번', 'SBM', C), F(2, 'u16', 'governor', '도독 무장번호', 'SBM', C)]),
    6: dict(key='region', ko='지역', stride=8, skew=-2, fields=[
        F(0, 'u16', 'u0', '항상 0 (레코드는 청크 base-2에서 시작: SCENARIO_BODY_MAP의 지역1 = 0x57FC와 일치, MEAS 343/343)', 'SBM;MEAS', '추정'),
        F(2, 'u16', 'population', '', 'SBM;EXT', C), F(4, 'u8', 'security', '', 'SBM;EXT', C), F(5, 'u8', 'initial_force', '초기 영유 세력(마스터 ID)', 'SCF;EXT', C),
        F(6, 'u8', 'flags', 'bit7 탐색 후보 지역, bit6 북방 변경 속성', 'SCF;MISC 1.3', C), F(7, 'u8', 'u7', '0 또는 30의 배수', 'SCF', '추정')]),
    7: dict(key='slot_cells', ko='(칸 슬롯 3001x6B)', stride=6, fields=[
        F(0, 'u16', 'cell', '지도 칸 번호(슬롯0=0xFFFF)', 'MEAS', '추정'), F(2, 'u8', 'facility', '0 없음 / 1 도시(51) / 2 관문(10)', 'MEAS', '추정'),
        F(3, 'u8', 'owner', '세력', 'MEAS', '추정'), F(4, 'u16', 'durability', '도시 2000/3000 (도시 표 내구와 일치)', 'MEAS', '추정')]),
    10: dict(key='general', ko='무장', stride=316, fields=[
        F(0x00, 'w14', 'family_name', '성', 'SGM', C), F(0x0E, 'w14', 'given_name', '명', 'SGM', C), F(0x1C, 'w6', 'courtesy', '자', 'SGM', C),
        F(0x22, 'w14', 'name', '표시명', 'SGM;EXT', C), F(0x94, 'u16', 'face', '모습', 'SGM', C), F(0x96, 'u16', 'id', '무장번호(슬롯 1~1000 = 번호)', 'SGM;EXT', C),
        F(0x98, 'u16', 'spouse', '', 'SGM;EXT', C), F(0x9A, 'u16', 'sworn', '의형(그룹 대표)', 'SGM;EXT', C), F(0x9C, 'u8', 'force', '', 'SGM;EXT', C),
        F(0x9D, 'u8', 'base', '소속 도시', 'SGM;EXT', C), F(0x9F, 'u8', 'location', '소재 통합 ID(0~51 도시/52~61 관문/62~ 부대)', 'SGM;EXT', C),
        F(0xA1, 'u8', 'status', '신분 1군주 3태수 4일반 7재야', 'SGM;EXT', C), F(0xA2, 'u8', 'office', '관직', 'SGM;EXT', C), F(0xA3, 'u8', 'loyalty', '충성', 'SGM;EXT', C),
        F(0xA6, 'u8x5', 'stats', '통솔·무력·지력·정치·매력', 'SGM;EXT', C), F(0xAB, 'u8x5', 'growth_room', '= 100 - 능력', 'SGM', C),
        F(0xB0, 'u16x9', 'traits', '개성 번호 9칸(0=없음)', 'SGM;EXT', C), F(0xC2, 'u32', 'formation_mask', '진형 비트필드', 'SGM;EXT', C),
        F(0xC6, 'u8x10', 'tactics', '전법 10칸', 'SGM;EXT', C), F(0xD0, 'u8', 'policy', '', 'SGM;EXT', C), F(0xD1, 'u8', 'voice1', '억양1', 'SGM', '추정'),
        F(0xD2, 'u8', 'voice2', '전용 음성', 'SGM', C), F(0xD3, 'u8', 'voice3', '', 'SGM', '추정'), F(0xD5, 'u8', 'join_year', '임관 연도', 'SGM;EXT', C),
        F(0xD8, 'u8', 'gender', '0남 1여', 'SGM;EXT', C), F(0xD9, 'u16', 'appear', '등장 연도', 'SGM;EXT', C), F(0xDB, 'u16', 'birth', '', 'SGM;EXT', C),
        F(0xDD, 'u16', 'death', '', 'SGM;EXT', C), F(0xDF, 'u8', 'death_kind', '사인(추정)', 'SGM', '추정'), F(0xE0, 'u16', 'clan', '가문 창시자', 'SGM;EXT', C),
        F(0xE2, 'u16', 'father', '10000+n = 가공 부친', 'SGM;EXT', C), F(0xE4, 'u16', 'mother', '', 'SGM;EXT', C), F(0xE6, 'u8', 'generation', '세대', 'SGM', C),
        F(0xE7, 'u8', 'affinity', '상성 0~149', 'SGM', C), F(0xE8, 'u16x8', 'likes', '친애 무장', 'SGM;EXT', C), F(0xF8, 'u16x8', 'dislikes', '혐오 무장', 'SGM', C),
        F(0x108, 'u16x5', 'stat_caps', '능력 상한', 'SGM', C), F(0x112, 'u8', 'principle', '주의', 'SGM;EXT', C), F(0x114, 'i16x12', 'aptitude', '적성/성장 경향(-20..20)', 'SGM', '추정'),
        F(0x12C, 'u8', 'policy_level', '정책 Lv', 'SGM;EXT', C), F(0x133, 'u8', 'merit_rank', '공적 등급 0~5', 'SGM;EXT', C), F(0x134, 'u16', 'merit', '공적(100단위)', 'SGM;EXT', C)]),
    13: dict(key='treasure', ko='명품', stride=65, fields=[
        F(0, 'u16', 'owner', '보유 무장(0=무소속)', 'SCF;EXT', C), F(4, 'u8', 'flag4', '대개 1, 옥새 0', 'SCF', '추정'), F(5, 'u8', 'flag5', '', 'SCF', '추정'),
        F(6, 'w14', 'name', '', 'SCF;EXT', C), F(0x14, 'w14', 'reading', '', 'SCF', C), F(0x3A, 'u8', 'kind', '종류(fixdata 명품 +0x0E와 같은 번호)', 'SCF;EXT', C),
        F(0x3B, 'u8x5', 'attrs', '속성 5칸(+0x3F는 능력값/가치 추정)', 'SCF', '추정'), F(0x40, 'u8', 'unique_no', '고유번호(전부 다름)', 'SCF', C)]),
    19: dict(key='tab19', ko='(미명명, 15Bx31)', stride=15, fields=[]),
    22: dict(key='trait_copy', ko='개성 사본', stride=60, fields=[
        F(0, 'w12', 'name', '', 'FRM', C), F(0x0C, 'w32', 'reading', '', 'FRM', C), F(0x2C, 'u8x2', 'conditions', '', 'FRM', C),
        F(0x2E, 'i32x2', 'cond_values', '', 'FRM', C), F(0x36, 'u8', 'effect1', '', 'FRM', C), F(0x37, 'i16', 'value1', '', 'FRM', C),
        F(0x39, 'u8', 'effect2', '', 'FRM', C), F(0x3A, 'i16', 'value2', '', 'FRM', C)]),
    31: dict(key='narration', ko='오프닝 내레이션', stride=213, fields=[
        F(0, 'u8', 'kind', '1/2', 'MEAS', '추정'), F(1, 'u32', 'a', '표시 타이밍으로 보이는 값(1950, 12800…)', 'MEAS', '추정'),
        F(5, 'u32', 'b', '', 'MEAS', '추정'), F(9, 'w204', 'text', '한 줄 문장(UTF-16LE)', 'SBM 3;MEAS', C)]),
    36: dict(key='trade_state', ko='(미명명, 5Bx5 = 교역국 상태)', stride=5, fields=[]),
    38: dict(key='scenic_state', ko='명승지 상태', stride=1, fields=[F(0, 'u8', 'state', '0/2/3 (명승지 101칸)', 'MEAS', '추정')]),
    43: dict(key='tab43', ko='(미명명, 269Bx1)', stride=269, fields=[]),
    100: dict(key='tab100', ko='(미명명, 1741Bx1)', stride=1741, fields=[]),
}
BY_KEY = {t['key']: i for i, t in TABLES.items()}
BY_KO = {t['ko']: i for i, t in TABLES.items()}


def scenario_ids(exce=True):
    pat = 'scedaexce' if exce else 'sceda'
    out = []
    for p in sorted((GAME / '0010_KO').glob(pat + '*.s14')):
        tail = p.stem[len(pat):]
        if tail.isdigit() and (exce or not p.stem.startswith('scedaex')):
            out.append(int(tail))
    return sorted(out)


class Scenario:
    def __init__(self, id, exce=True):
        self.id = id
        self.exce = exce
        name = ('scedaexce%02d.s14' if exce else 'sceda%02d.s14') % id
        self.path = GAME / '0010_KO' / name
        self.c = Container(self.path)
        h = self.c.header
        self.body = self.c.body
        self.year = u16(h, 0x1C8)
        self.month = h[0x1CD]
        self.category = h[0x1CA]
        self.number = h[0x1CE]
        self.name = s14.wstr(h, 0x1A6, 0x22)
        self.intro = s14.wstr(h, 0x14, 0x192)
        n = u32(self.body, 4)
        start = 0xe9a if exce else self.body.find(struct.pack('<II', 1, 52), 8 + 2 * n)
        self.chain = walk_chain(self.body, start, STRIDES_CE if exce else None)
        self.chunks = {c.id: c for c in self.chain}
        # general id list head: u16 x N (last 0)
        self.general_ids = [u16(self.body, 8 + 2 * i) for i in range(n)]

    def raw_records(self, tid):
        """Raw records; a spec may carry 'skew' (record i starts at chunk.base + skew + i*stride, see region)."""
        ch = self.chunks[tid]
        sk = TABLES.get(tid, {}).get('skew', 0)
        return [self.body[ch.base + sk + i * ch.stride: ch.base + sk + (i + 1) * ch.stride] for i in range(ch.count)]

    def table(self, key):
        tid = key if isinstance(key, int) else BY_KEY.get(key, BY_KO.get(key))
        spec = TABLES[tid]
        out = []
        for i, r in enumerate(self.raw_records(tid)):
            d = decode(spec, r)
            d['_slot'] = i
            d['_raw'] = r
            out.append(d)
        return out

    def keys(self):
        return [t['key'] for i, t in sorted(TABLES.items()) if i in self.chunks]

    def unresolved(self, tid):
        return unresolved_of(TABLES[tid], self.raw_records(tid))

    def info(self):
        return dict(id=self.id, file=self.path.name, name=self.name, year=self.year, month=self.month, category=self.category, tier=self.c.version,
                    tables=[c.as_dict() for c in self.chain])

    # ---- convenience views (CE) ------------------------------------------------------------------------------------
    def bases(self):
        """Cities (base 0..51) and gates (52..61) as dicts with 'base' id."""
        out = []
        for i, r in enumerate(self.table('city')):
            r['base'] = i
            out.append(r)
        for i, r in enumerate(self.table('gate')):
            if i == 0:
                continue
            r['base'] = 51 + i
            out.append(r)
        return out

    def generals(self):
        """Non-empty general slots; slot != id beyond slot 1000 (see data_formats_game.md)."""
        out = []
        for r in self.table('general'):
            if r['id']:
                out.append(r)
        return out


@lru_cache(None)
def _scn(id, exce):
    return Scenario(id, exce)


def load_scenario(id, block=None, exce=True):
    """origlib.load_scenario(id) -> Scenario; origlib.load_scenario(id, 'city') -> list of record dicts."""
    s = _scn(id, exce)
    return s if block is None else s.table(block)
