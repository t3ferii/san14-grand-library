"""0010_KO/fixdataexce.s14 (CE, v102) and fixdata.s14 (base game, v51): the master definition tables.

Body = LWC payload: [u32 version=102][u32 12][12 x 20B region groups][chain of <u32 id><u32 count>+records ...].
Chain layout (walker verified, strides below found by DFS, see docs/orig/data_formats_game.md section 3):
the headers of ids 0..43 follow each other without gaps and end exactly at the end of the body.

Field specs: (offset, fmt, name, meaning, evidence, confidence)
  fmt: u8 u16 u32 i8 i16 i32 | wN = UTF-16LE string in N bytes | u8xN u16xN = arrays
  confidence: 확정 (editor oracle or code/dump verified), 추정 (value pattern only), 미해결 is never written here:
  anything not covered by a spec is reported by `unresolved()` with measured value distributions.
Evidence tags:  FRM = reference_mod/Modding_DOCS/format/FIXDATA_RECORD_MAP.md, FSIG = FIXDATA_SIGNATURE.md,
  MISC = MISC_DATA_FILES.md, WT = San14Sim/tools/worldmap_tables.py + gen_facility_tables.py (engine-verified rows),
  EXT = San14Sim/tools/extract/*.py, ORIG = checked in origlib tests against San14Sim/data/tables/*.json.
"""
import struct
from functools import lru_cache
from . import s14
from .s14 import GAME, Container, Chunk, walk_chain, u16, u32

# ---- stride hints per fixdata version (id -> stride); found by walk_chain, 0 = count-only marker -------------------
STRIDES_CE = {0: 32, 1: 53, 2: 40, 3: 2, 4: 0, 5: 3, 6: 65, 7: 0, 8: 51, 9: 53, 10: 0, 11: 152, 12: 94, 13: 22, 14: 127, 15: 166,
              16: 46, 17: 102, 18: 148, 19: 21, 20: 13, 21: 0, 22: 170, 23: 0, 24: 0, 25: 0, 26: 134, 27: 0, 28: 11, 29: 26, 30: 0,
              31: 0, 32: 14, 33: 0, 34: 0, 35: 138, 36: 29, 37: 77, 38: 80, 39: 4, 40: 34, 41: 37, 42: 35, 43: 0}

# --------------------------------------------------------------------------------------------------------------------
# Field specs.  Names are English identifiers; 'ko' = in-game table name.
# --------------------------------------------------------------------------------------------------------------------
from .spec import F, decode, fmt_size as _fmt_size, unresolved_of

C = '확정'
TABLES = {
    -1: dict(key='region_group', ko='지역구분', stride=20, fields=[
        F(0, 'w6', 'name', '지역구분 이름(하북·중원·서북·오월·형초·파촉+이민족5)', 'FRM', C),
        F(6, 'w6', 'reading', '발음(KO는 이름과 같음)', 'FRM', C)]),
    0: dict(key='state', ko='주(州)', stride=32, fields=[
        F(0, 'w10', 'name', '', 'FRM', C), F(0x0A, 'w14', 'reading', '', 'FRM', C), F(0x18, 'w6', 'abbr', '약칭', 'FRM', C),
        F(0x1E, 'u8', 'region_group', '지역구분 번호', 'FRM', C), F(0x1F, 'u8', 'geo', '지리 표(id35) 번호, 이민족 0', 'FRM', C)]),
    1: dict(key='city', ko='도시', stride=53, fields=[
        F(0, 'w8', 'name', '', 'FRM;ORIG', C), F(8, 'w8', 'reading', '', 'FRM', C), F(0x1C, 'u8x10', 'adjacent', '인접 거점(0=없음)', 'FRM', C),
        F(0x28, 'u32', 'max_gold', '', 'FRM', C), F(0x2C, 'u32', 'max_food', '', 'FRM', C), F(0x30, 'u32', 'max_troops', '', 'FRM', C),
        F(0x27, 'u8', 'id', '거점 번호(슬롯과 같음 0..51, MEAS)', 'MEAS', '추정'),
        F(0x34, 'u8', 'state', '주(州) 번호(52/52)', 'FRM', C)]),
    2: dict(key='gate', ko='관문', stride=40, fields=[
        F(0, 'w8', 'name', '', 'FRM', C), F(8, 'w8', 'reading', '', 'FRM', C), F(0x1C, 'u8x10', 'adjacent', '인접 거점', 'FRM', C)]),
    3: dict(key='slot_pair', ko='(미명명, 52x2B)', stride=2, fields=[]),
    4: dict(key='marker4', ko='(개수 표지 52)', stride=0, fields=[]),
    5: dict(key='cell_grid', ko='(칸 표 220x220, 3B)', stride=3, fields=[
        F(0, 'u8', 'a', '첫 바이트 (값 분포는 문서 참조)', '', '추정')]),
    6: dict(key='area', ko='지역', stride=65, fields=[
        F(0, 'w10', 'name', '', 'FRM;WT', C), F(0x0A, 'w10', 'reading', '', 'FRM', C), F(0x24, 'u8', 'base', '소속 거점', 'FRM;EXT', C),
        F(0x25, 'u16', 'center_cell', '중심 칸 번호(지도 칸)', 'FRM;EXT', C), F(0x27, 'u16', 'security_ref', '치안 기준(100)', 'FRM', C),
        F(0x29, 'u16', 'commerce_ref', '상업 기준(양평 290)', 'FRM', C), F(0x2B, 'u16', 'agri_ref', '농업 기준(양평 1190)', 'FRM', C),
        F(0x2D, 'u16', 'barracks_ref', '병영 기준(양평 600)', 'FRM', C), F(0x2F, 'u16x8', 'adjacent', '인접 지역', 'FRM;EXT', C),
        F(0x3F, 'u8', 'build_cap', '건설 상한(0~11)', 'FRM;WT area_fac_cap', '추정'), F(0x40, 'u8', 'adj_flags', '인접 제한 비트(0xFF가 대부분)', 'FRM', '추정')]),
    7: dict(key='marker7', ko='(개수 표지 3001)', stride=0, fields=[]),
    8: dict(key='terrain', ko='지형', stride=51, fields=[
        F(0, 'w8', 'name', '', 'EXT', C), F(8, 'w18', 'reading', '', 'FRM', C), F(0x1A, 'u16', 'move_cost', '이동 비용(EXE BE120 반환)', 'EXT terrain_table', C),
        F(0x1C, 'u8', 'flag', '', 'EXT', '추정')]),
    9: dict(key='facility', ko='시설', stride=53, fields=[
        F(0, 'w10', 'name', '', 'WT', C), F(0x0A, 'w10', 'reading', '', 'WT', C), F(0x1C, 'u8', 'cls', '분류(2군사,3방벽,4함정,1거점)', 'WT', C),
        F(0x1D, 'u16', 'hp', '내구', 'WT', C), F(0x1F, 'u16', 'cost', '건설 비용', 'WT', C), F(0x21, 'u16', 'f21', '', 'WT', '추정'),
        F(0x23, 'u8', 'need_effect', '필요 효과 id', 'WT', C), F(0x24, 'u8', 'interval', '발동 간격', 'WT', C),
        F(0x25, 'u8', 'eff1_kind', '', 'WT', C), F(0x26, 'u8', 'eff1_v', '', 'WT', C), F(0x27, 'u8', 'eff1_v2', '', 'WT', C),
        F(0x28, 'u8', 'eff2_kind', '', 'WT', C), F(0x29, 'u8', 'eff2_v', '', 'WT', C), F(0x2A, 'u8', 'eff2_v2', '', 'WT', C),
        F(0x2B, 'u8', 'min_dist', '대상 최소 거리(2AD8F0)', 'WT', C), F(0x2C, 'u8', 'range', '사거리', 'WT', C), F(0x2D, 'u8', 'f2d', '', 'WT', '추정'),
        F(0x2E, 'u32', 'terrain_mask', '설치 가능 지형 마스크', 'WT', C), F(0x32, 'u8', 'sub', '', 'WT', '추정'), F(0x33, 'u8', 'thr', '문턱값', 'WT', C),
        F(0x34, 'u8', 'f34', '', 'WT', '추정')]),
    10: dict(key='marker10', ko='(개수 표지 1851 = 무장 슬롯)', stride=0, fields=[]),
    11: dict(key='formation', ko='진형', stride=152, fields=[
        F(0, 'w6', 'name', '', 'FRM;ORIG', C), F(6, 'w14', 'reading', '', 'FRM', C), F(0x14, 'u8x8', 'usage', '용도(야전·유격·제압)', 'FRM', C),
        F(0x1C, 'w82', 'desc', '', 'FRM', C), F(0x6E, 'u8', 'water', '', 'EXT;ORIG', C), F(0x6F, 'u8', 'mobility', '', 'EXT;ORIG', C),
        F(0x73, 'u8', 'attack', '', 'EXT;ORIG', C), F(0x74, 'u8', 'siege', '', 'EXT;ORIG', C), F(0x75, 'u8', 'demolition', '', 'EXT;ORIG', C),
        F(0x76, 'u8', 'defense', '', 'EXT;ORIG', C), F(0x89, 'u16', 'cost', '', 'EXT;ORIG', C), F(0x95, 'u8', 'ranged', '', 'EXT;ORIG', C)]),
    12: dict(key='tactic', ko='전법', stride=94, fields=[
        F(0, 'w10', 'name', '', 'FRM;ORIG', C), F(0x0A, 'w38', 'reading', '', 'FRM', C), F(0x30, 'u8', 'family', '계통', 'FRM;ORIG', C),
        F(0x31, 'u16', 'wait', '대기시간(48/72/90)', 'FRM;ORIG', C), F(0x33, 'u8', 'flags', 'bit1 활성(콜라보 해금) bit0 lp42', 'FRM;ORIG', C),
        F(0x50, 'u8x8', 'effects', '효과1,2종류 / 범위 / 치1 / 치2', 'FRM;ORIG', C), F(0x58, 'u8', 'ability', '의존 능력 1무력 2지력', 'FRM;ORIG', C),
        F(0x59, 'u32', 'formation_mask', '사용 진형 마스크(비트 N=진형 N)', 'FRM;ORIG', C)]),
    13: dict(key='treasure', ko='명품', stride=22, fields=[
        F(0, 'w14', 'name', '', 'FRM;WT', C), F(0x0E, 'u8', 'kind', '종류(1도검…11명마)', 'FRM;WT', C), F(0x0F, 'u8', 'ability', '1통솔~5매력', 'FRM;WT', C),
        F(0x10, 'u8', 'value', '능력 가산', 'FRM;WT', C), F(0x11, 'u8', 'effect', '1퇴각확실 2수명연장', 'FRM;WT', C), F(0x13, 'u8', 'worth', '가치', 'FRM;WT', C),
        F(0x15, 'u8', 'cg', 'CG 번호', 'FRM', '추정')]),
    14: dict(key='nation', ko='국호', stride=127, fields=[
        F(0, 'w8', 'name', '', 'FRM', C), F(8, 'w14', 'reading', '', 'FRM', C), F(0x16, 'w102', 'desc', '', 'FRM', C)]),
    15: dict(key='rank', ko='관작', stride=166, fields=[
        F(0, 'w26', 'name', '', 'FRM;ORIG', C), F(0x1A, 'w26', 'reading', '', 'FRM', C), F(0x34, 'w102', 'desc', '', 'FRM', C),
        F(0x9A, 'u16', 'base_troops', '관작별 기준 병력', 'MISC 5', C)]),
    16: dict(key='office', ko='관직', stride=46, fields=[
        F(0, 'w10', 'name', '', 'FRM;ORIG', C), F(0x0A, 'w26', 'reading', '', 'FRM', C), F(0x24, 'u16', 'command', '지휘 병사', 'FRM;ORIG', C),
        F(0x26, 'u8', 'stipend', '봉록', 'FRM;ORIG', C), F(0x27, 'u8', 'rank', '관작', 'FRM;ORIG', C), F(0x28, 'u8x5', 'stats', '통무지정매 지정', 'FRM;ORIG', C),
        F(0x2D, 'u8', 'system', '체계', 'FRM;ORIG', C)]),
    17: dict(key='principle', ko='주의', stride=102, fields=[
        F(0, 'w8', 'name', '', 'FRM;ORIG', C), F(8, 'w8', 'reading', '', 'FRM', C), F(0x1C, 'w62', 'desc', '', 'FRM', C), F(0x5A, 'u8', 'lp67', '', 'FRM', '추정'),
        F(0x5B, 'u8x5', 'policy_slots', '전투·지원·모략·내정·인사', 'FRM;ORIG', C), F(0x60, 'u8x5', 'limits', '상한', 'FRM;ORIG', C), F(0x65, 'u8', 'lp72', '', 'FRM', '추정')]),
    18: dict(key='policy', ko='정책', stride=148, fields=[
        F(0, 'w12', 'name', '', 'FRM;ORIG', C), F(0x0C, 'w32', 'reading', '', 'FRM', C), F(0x2C, 'w92', 'desc', '', 'FRM', C),
        F(0x88, 'u8x8', 'effect_ids', '발동 효과(id26 정책효과 표)', 'FRM;ORIG', C), F(0x90, 'u8', 'category', '', 'EXT;ORIG', C),
        F(0x91, 'u8', 'composite', '', 'EXT;ORIG', C), F(0x92, 'u16', 'base_cost', '', 'EXT;ORIG', C)]),
    19: dict(key='tactic_book', ko='전법서', stride=21, fields=[
        F(0, 'w12', 'name', '', 'FRM', C), F(0x0E, 'u8', 'tactic', '전법 번호', 'FRM', C)]),
    20: dict(key='tab20', ko='(미명명, 13Bx400)', stride=13, fields=[]),
    21: dict(key='marker21', ko='(개수 표지 2001)', stride=0, fields=[]),
    22: dict(key='trait', ko='개성', stride=170, fields=[
        F(0, 'w12', 'name', '', 'FRM;ORIG', C), F(0x0C, 'w32', 'reading', '', 'FRM', C), F(0x2C, 'w102', 'desc', '', 'FRM', C),
        F(0x94, 'u8x2', 'conditions', '조건1·2', 'FRM;ORIG', C), F(0x98, 'u8', 'effect1', '', 'FRM;ORIG', C), F(0x99, 'i16', 'value1', '', 'FRM;ORIG', C),
        F(0x9B, 'u8', 'effect2', '', 'FRM;ORIG', C), F(0x9C, 'i16', 'value2', '', 'FRM;ORIG', C), F(0x9E, 'u8', 'color', '1청 2적 3금', 'FRM;ORIG', C),
        F(0x9F, 'u8', 'flags', 'bit0 적색발동 bit1 전투발동 bit3 곱연산 bit4 활성', 'FRM;ORIG', C), F(0xA0, 'i32x2', 'cond_values', '조건값1·2', 'FRM;ORIG', C),
        F(0xA9, 'u8', 'ce_extra', 'CE 추가 바이트(0~9)', 'FRM', '추정')]),
    26: dict(key='policy_effect', ko='정책효과', stride=134, fields=[
        F(0, 'w22', 'name', '', 'FRM;ORIG', C), F(0x72, 'u16x10', 'level_values', 'Lv1..10 값(101~104는 배치 다름)', 'FRM;ORIG', C)]),
    28: dict(key='tab28', ko='(미명명, 11Bx49)', stride=11, fields=[]),
    29: dict(key='tab29', ko='(미명명, 26Bx501)', stride=26, fields=[]),
    32: dict(key='tab32', ko='(미명명, 14Bx50)', stride=14, fields=[]),
    35: dict(key='geo', ko='지리', stride=138, fields=[
        F(0, 'w14', 'name', '', 'FRM', C), F(0x0E, 'w14', 'reading', '', 'FRM', C), F(0x1C, 'w104', 'desc', '', 'FRM', C),
        F(0x86, 'u8', 'effect1', '', 'FRM', C), F(0x87, 'u8', 'effect2', '', 'FRM', C)]),
    36: dict(key='trade_nation', ko='교역국', stride=29, fields=[
        F(0, 'w12', 'name', '', 'FRM', C), F(0x0C, 'w12', 'reading', '', 'FRM', C), F(0x18, 'u8', 'reward_lv1', '획득물 Lv1 명품(128~131)', 'FRM', C),
        F(0x19, 'u8', 'reward_lv2', '교역특전 번호', 'FRM', C), F(0x1A, 'u8', 'reward_lv3', '교역특전 번호', 'FRM', C),
        F(0x1B, 'u8', 'reward_lv4', '전법서(27~30)', 'FRM', C), F(0x1C, 'u8', 'port', '교역항구 거점(교지31·성도44·장안20·낙양18)', 'FRM', C)]),
    37: dict(key='trade_perk', ko='교역특전', stride=77, fields=[
        F(0, 'w38', 'name', '', 'FRM', C), F(0x26, 'w38', 'reading', '', 'FRM', C), F(0x4C, 'u8', 'u4c', '142~149 미확정', 'FRM', '추정')]),
    38: dict(key='scenic', ko='명승지', stride=80, fields=[
        F(0, 'w38', 'name', '', 'MISC 1.1', C), F(0x26, 'w38', 'reading', '', 'MISC 1.1', C), F(0x4C, 'u16', 'cell', '지도 칸 번호', 'MISC 1.1', C),
        F(0x4E, 'u8', 'kind', '1~8 종류/효과 번호로 보임', 'MISC 1.1', '추정'), F(0x4F, 'u8', 'u4f', '1~20', 'MISC 1.1', '추정')]),
    39: dict(key='merit_reward', ko='공적 보상', stride=4, fields=[
        F(0, 'u8', 'effect', '1지휘병사 2담당구역 3정책등급', 'MISC 4', C), F(1, 'u16', 'value', '', 'MISC 4', C), F(3, 'u8', 'grade', '', 'MISC 4', '추정')]),
    40: dict(key='tab40', ko='(미명명, 34Bx31)', stride=34, fields=[]),
    41: dict(key='tab41', ko='(미명명, 37Bx80)', stride=37, fields=[]),
    42: dict(key='tab42', ko='(미명명, 35Bx7)', stride=35, fields=[]),
}
for _k in list(TABLES):
    pass
BY_KEY = {t['key']: i for i, t in TABLES.items()}
BY_KO = {t['ko']: i for i, t in TABLES.items()}


class FixData:
    def __init__(self, exce=True):
        self.exce = exce
        self.path = GAME / '0010_KO' / ('fixdataexce.s14' if exce else 'fixdata.s14')
        self.c = Container(self.path)
        self.body = self.c.body
        ngroups = u32(self.body, 4)
        start = 8 + ngroups * 20
        hints = STRIDES_CE if exce else None
        self.chain = walk_chain(self.body, start, hints)
        self.chunks = {ch.id: ch for ch in self.chain}
        self.version = u32(self.body, 0)

    def raw_records(self, tid):
        ch = self.chunks[tid]
        return [ch.rec(self.body, i) for i in range(ch.count)]

    def table(self, key):
        """Records of one table as dicts (+ '_id' slot, '_raw' bytes)."""
        tid = key if isinstance(key, int) else BY_KEY.get(key, BY_KO.get(key))
        if tid is None:
            raise KeyError(key)
        spec = TABLES[tid]
        if tid == -1:
            recs = [self.body[8 + i * 20:8 + (i + 1) * 20] for i in range(u32(self.body, 4))]
        else:
            recs = self.raw_records(tid)
        out = []
        for i, r in enumerate(recs):
            d = decode(spec, r)
            d['_id'] = i
            d['_raw'] = r
            out.append(d)
        return out

    def keys(self):
        return [t['key'] for i, t in sorted(TABLES.items()) if i == -1 or i in self.chunks]

    def unresolved(self, tid):
        """Bytes of table `tid` not covered by a spec, with measured value distributions."""
        recs = ([self.body[8 + i * 20:8 + (i + 1) * 20] for i in range(u32(self.body, 4))] if tid == -1 else self.raw_records(tid))
        return unresolved_of(TABLES[tid], recs)


@lru_cache(None)
def _fix(exce):
    return FixData(exce)


def load_fixdata(lang='KO', exce=True):
    """{table key: [record dict]} for every table with a spec.  lang is fixed to KO."""
    f = _fix(exce)
    return {k: f.table(k) for k in f.keys()}
