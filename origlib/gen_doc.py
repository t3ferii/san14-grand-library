"""Generate San14Sim/docs/orig/data_formats_game.md from the origlib specs + measured distributions.

  python -X utf8 -m origlib.gen_doc      (cwd = San14Sim)
The prose sections are in PROSE_* below; all tables (fields, unresolved bytes, strides, opcode stats) are measured from the files.
"""
import collections
import sys
from pathlib import Path
from . import fixdata, scenario, msg as _msgpkg, mapbin, misc0000, event, dlc, s14   # noqa
from .msg import table as msg_table, FILES as MSG_FILES
from .spec import fmt_size, unresolved_of

SIM = Path(__file__).resolve().parents[1]
OUT = SIM / 'docs' / 'orig' / 'data_formats_game.md'
G = s14.GAME
L = []
cnt = collections.Counter()


def w(*a):
    L.append(' '.join(str(x) for x in a))


def field_table(spec, recs=None, name_hdr=True):
    w('| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |')
    w('|---|---|---|---|---|---|')
    for off, fmt, name, desc, ev, conf in spec['fields']:
        w('| +0x%02X | %s(%dB) | %s | %s | %s | %s |' % (off, fmt, fmt_size(fmt), name, desc or '-', ev or '-', conf))
        cnt[conf] += 1
    if recs is not None:
        un = unresolved_of(spec, recs)
        if un:
            w('')
            w('미해결(스펙에 없는 바이트, 전 레코드 측정):')
            w('')
            for i, (s, e, d) in enumerate(un[:48]):
                w('- +0x%02X..+0x%02X : %s' % (s, e - 1, d))
                if d.startswith('상수'):
                    pass
                else:
                    cnt['미해결 바이트(가변)'] += 1
            if len(un) > 48:
                w('- ... (%d개 구간 더, `python -m origlib unresolved <key>`로 전체)' % (len(un) - 48))
    w('')


def main():
    fx = fixdata.FixData()
    w('# 삼국지14 원본 데이터 파일 형식 — 게임 데이터 해체 (0000 · 0001_KO · 0004 · 0010_KO · DLC)')
    w('')
    w('생성: `python -X utf8 -m origlib.gen_doc` (San14Sim 에서). 코드: `San14Sim/origlib/`, 시험: `San14Sim/tests/test_origlib.py`, 사용법: `San14Sim/origlib/README.md`.')
    w('이 문서의 표(필드·미해결 분포·stride·opcode 통계)는 파일에서 직접 측정해 만든 것이고, 해석 문장은 아래 근거 약어를 단다.')
    w('')
    w('범위: 한국어(KO)와 언어 무관 폴더만 (사용자 2026-11-07). 0001_EN/JP/SC/TC·0010_EN/JP/SC/TC·DLC 다른 언어 폴더는 다루지 않는다. 0002·0005 아카이브는 `data_formats_archives.md`(K4).')
    w('')
    w('확신도: **확정** = 편집기 오라클/교차 대조/이미 검증된 엔진 표/덤프 일치(근거 약어 표기), **추정** = 값 패턴만, **미해결** = 스펙에 없는 바이트(값 분포 실측 수록). 주의: 이 파일들의 필드 의미는 EXE 읽기 코드(ghidra_full)로 새로 확인한 것이 아니라 참고 모드 분석서(FRM 등)와 기존 엔진 표 + 이번 실측이다 — 코드 확인이 필요한 필드는 미해결/추정으로 남겼다.')
    w('')
    w('근거 약어: FRM=reference_mod/Modding_DOCS/format/FIXDATA_RECORD_MAP.md · FSIG=FIXDATA_SIGNATURE.md · MISC=MISC_DATA_FILES.md · SBM=SCENARIO_BODY_MAP.md · SGM=SAVE_GENERAL_MAP.md · SCF=SAVE_CITY_FACTION_MAP.md · REA6=REA_Analysis/1022_REA_분석_전체합본.md 6절 · WT=San14Sim/tools/worldmap_tables.py·gen_facility_tables.py(엔진 검증 표) · EXT=San14Sim/tools/extract/*.py · ORIG=origlib 시험이 기존 data/*.json과 대조 · MEAS=이번 실측.')
    w('')
    # ---------------------------------------------------------------- 1 inventory
    w('## 1. 파일 인벤토리 (무엇이 어디)')
    w('')
    w('| 위치 | 파일 | 형식 | 로더 | 절 |')
    w('|---|---|---|---|---|')
    inv = [
        ('0000/', 'Map.bin, MapExCe.bin', '4B 칸 수 + 48400x16B 칸', 'origlib.load_map(exce)', '7'),
        ('0000/', 'bt.bin, bt_exce.bin', 'JBTP 행동 트리 컨테이너 4트리', 'origlib.load_bt(exce)', '8.2'),
        ('0000/', 'ccscore_data, change_force_data, opcamera_data, param_s, experience_data(_exce)', '구간 컨테이너 (u32 n; n x(off,size); 구간=u32 개수+레코드)', 'misc0000.read_sections/section_table', '8.1'),
        ('0000/', 'effect_info.bin, se_info(_exce).bin', '4B 레코드 137개 / 0으로 찬 215·220B', 'misc0000.effect_info', '8.3'),
        ('0001_KO/', 'msgdata(_exce).bin, msggame(_exce).bin', "'zp1' zlib 청크 컨테이너 -> 구간 -> 문자열", 'origlib.msg(id, table) / origlib.find_text', '6'),
        ('0004/', 'Event001, EventPKCE001, CCEvent050-054, CCEventPKCE*, EventTutorial(PKCE)', '비압축 이벤트 스크립트 (조건/행동 44B 레코드)', 'origlib.events(file)', '9'),
        ('0004/', 'EventSample{Ko,En,Jp,Sc,Tc}.s14', '편집기용 샘플 목록(UTF-16 제목·설명+이진)', '(미해체: Ko만 범위, 목록 용도)', '9.5'),
        ('0010_KO/', 'fixdata.s14 / fixdataexce.s14', 'S14 헤더 + LWC, 표 연쇄 (base 51 / CE 102)', 'origlib.load_fixdata(exce)', '2-3'),
        ('0010_KO/', 'sceda01-08,55-57,71 (base) / scedaexce 50개(번호 1-9,12-18,21-28,30-31,34-35,55-63,71-73,100-104,150-154) (CE)', 'S14 헤더 + LWC, 표 연쇄', 'origlib.load_scenario(id)', '4'),
        ('DLC/0010_KO/', 'sceda09-29, scedaex09-29,150-154, scedaexce10-11,32-33', 'XOR 포장 후 S14', 'origlib.dlc.load_dlc_scenario(file)', '10'),
        ('DLC/', 'DLCInfo*.s14 (45), 0011/gd_*.s14', '암호화(미해독)', '목록만', '10'),
        ('DLC/', '0003/*.wmv, 0005/*.bin', '동영상 / 아카이브(K4)', '-', '10'),
    ]
    for r in inv:
        w('| ' + ' | '.join(r) + ' |')
    w('')
    # ---------------------------------------------------------------- 2 container
    w('## 2. 공통 컨테이너')
    w('')
    w('### 2.1 S14 헤더 + LWC (fixdata·sceda·scedaexce)')
    w('')
    w('- 평문 헤더: base 480B(ver 51), PK 754B(ver 92), CE 754B(ver 102). +0x04 `SN14SCEXVER0001`, +0x14 소개문(UTF-16LE), +0x1A6 이름, +0x1C8 u16 시작 년, +0x1CA u8 분류(1 일반/2 튜토리얼/4 신군주), +0x1CB u8 계층 버전, +0x1CD u8 시작 월, +0x1CE u8 시나리오 번호 (SBM; 50개 CE 시나리오로 MEAS 확정).')
    w('- 헤더 +0x1CF u32 = fixdata 본문 서명 `pow(sum(body)&0xFFFF, 5, 0x3FDE03A3)` (FSIG; 시험이 재확인). 시나리오는 0. 검사 코드는 EXE RVA 0x32A290 로더(옛 빌드 기준 RVA, FSIG).')
    w('- 이어서 `LWC\\x1a` 블록 1개: `u32 raw_size, u32 comp_size, u8[256] 심볼표, 비트스트림` (`origlib/lwc.py`, 기존 tools/extract/lwc.py 복사·통합. 디코더 해석은 LWC_FORMAT.md/EXE 0x140001EDD 근거).')
    w('')
    w('### 2.2 표 연쇄 (chunk chain)')
    w('')
    w('본문은 `<u32 표ID><u32 레코드수>` + 레코드수 x stride 바이트가 끝까지 틈 없이 이어진 연쇄다 (SBM 1(3)절). **stride 는 파일에 없다**: `s14.walk_chain` 이 DFS 로 "다음 헤더가 sane 한 id/개수로 나타나고 연쇄가 파일 끝에 정확히 닿는" stride 를 찾는다 (fixdataexce: 44개 표 전부, 0.1초; 시나리오 50개 CE 전부 연쇄 완주 — 시험). stride 0 인 표는 개수만 선언된 표지(데이터 없음)다.')
    w('')
    w('fixdataexce 연쇄 (ID, 레코드수, stride, 본문 base — 측정):')
    w('')
    w('| ID | 키 | 이름 | 개수 | stride | base | 스펙 필드 수 |')
    w('|---|---|---|---|---|---|---|')
    w('| -1 | region_group | 지역구분 | 12 | 20 | 0x08 | 2 |')
    for ch in fx.chain:
        t = fixdata.TABLES.get(ch.id, dict(key='?', ko='?', fields=[]))
        w('| %d | %s | %s | %d | %d | 0x%X | %d |' % (ch.id, t['key'], t['ko'], ch.count, ch.stride, ch.base, len(t['fields'])))
    w('')
    # ---------------------------------------------------------------- 3 fixdata
    w('## 3. fixdata 표 (0010_KO/fixdataexce.s14, CE v102)')
    w('')
    w('API: `origlib.load_fixdata()` -> `{키: [레코드 dict]}` (각 dict 에 `_id`, `_raw`). `fixdata.FixData().table(키|한글이름)`, `.unresolved(id)`.')
    w('이름 문자열은 레코드 안(UTF-16LE)에 있다 (msg 파일에는 없음: 이름·발음·설명이 fixdata 안에 인라인 — 시험으로 확인).')
    w('')
    for tid, spec in sorted(fixdata.TABLES.items()):
        ch = fx.chunks.get(tid)
        recs = None
        if tid == -1:
            recs = [fx.body[8 + i * 20:8 + (i + 1) * 20] for i in range(12)]
            n = 12
        elif ch:
            recs = fx.raw_records(tid)
            n = ch.count
        else:
            continue
        w('### 3.%s 표 %d `%s` — %s (%dB x %s)' % (tid if tid >= 0 else 'a', tid, spec['key'], spec['ko'], spec['stride'], n))
        w('')
        if spec['stride'] == 0:
            w('개수 표지 (데이터 없음).')
            w('')
            continue
        field_table(spec, recs)
    w('### 3.z fixdata 정정·충돌 메모')
    w('')
    w('- **정정(해결, L1)**: 기존 `data/tables/terrain.json` 은 51행이었지만 지형 표(ID 8)는 **31행**이다(헤더 `(8,31)`). 뒤 20행은 시설 표 앞부분 바이트였다. `tools/extract/terrain_table.py` 가 origlib 로 31행을 다시 만들고 엔진은 31행을 요구한다. 지도 칸의 지형 ID 는 1..24 뿐이라 영향 없음 (확정, 헤더).')
    w('- **정정**: 시설 표(ID 9)의 레코드 수는 31(ids 0..30)이며 이름 필드는 레코드 +0x00(10B)에 있다 (`gen_facility_tables.py` 의 FAC_NAMES 수동 표는 이 이름과 일치).')
    w('- 도시 레코드 +0x27 u8 은 슬롯 번호(0..51)와 같다 (MEAS) — FRM 에 없던 필드.')
    w('')
    # ---------------------------------------------------------------- 4 scenario
    w('## 4. 시나리오 (0010_KO/scedaexce*.s14, CE)')
    w('')
    w('API: `origlib.load_scenario(id)` -> `Scenario`(name/year/month/category/chain, `.table(키)`, `.bases()`, `.generals()`), `origlib.load_scenario(id, "general")` -> 레코드 리스트. `origlib.scenario_ids()` = 50개(1-9,12-18,21-28,30-31,34-35,55-63,71-73,100-104,150-154; 헤더 번호).')
    w('')
    w('본문: `u32 ver, u32 N(=1852), u16 무장번호표 x N`, 이어서 0xE9A 부터 표 연쇄. 표 ID 는 fixdata 와 같은 번호 공간(1 도시, 2 관문, 3 세력, 4 군단, 6 지역, 10 무장, 13 명품, 22 개성 사본). 슬롯과 무장번호는 1~1000 에서만 같다 (SBM 2.3: 1001-1100=2001-2100, 1101-1300=4001-4200, 1301-1400=5001-5100, 이후 0).')
    w('')
    s3 = scenario.load_scenario(3)
    w('시나리오 03 (군웅할거) 의 연쇄 (모든 CE 시나리오 동일 — 시험):')
    w('')
    w('| ID | 키 | 개수 | stride | base | 스펙 필드 수 |')
    w('|---|---|---|---|---|---|')
    for ch in s3.chain:
        t = scenario.TABLES.get(ch.id)
        w('| %d | %s | %d | %d | 0x%X | %d |' % (ch.id, t['key'] if t else '(미스펙)', ch.count, ch.stride, ch.base, len(t['fields']) if t else 0))
    w('')
    w('150~154 번은 ID 104 표가 없다(연쇄 45개). 측정: 아래 목록.')
    w('')
    w('| 번호 | 파일 | 이름 | 년.월 | 분류 |')
    w('|---|---|---|---|---|')
    for i in scenario.scenario_ids():
        s = scenario.load_scenario(i)
        w('| %d | %s | %s | %d.%d | %d |' % (i, s.path.name, s.name, s.year, s.month, s.category))
    w('')
    for tid, spec in sorted(scenario.TABLES.items()):
        ch = s3.chunks[tid]
        recs = s3.raw_records(tid)
        w('### 4.%d 표 %d `%s` — %s (%dB x %d)' % (tid, tid, spec['key'], spec['ko'], spec['stride'], ch.count))
        w('')
        if spec.get('skew'):
            w('레코드는 청크 base%+d 에서 시작 (이유: SBM 은 지역 1 을 0x57FC 라 적었고 측정으로 343/343 일치).' % spec['skew'])
            w('')
        field_table(spec, recs)
    for tid in sorted(s3.chunks):
        if tid not in scenario.TABLES:
            ch = s3.chunks[tid]
            if ch.stride:
                w('### 4.%d 표 %d (미스펙, %dB x %d)' % (tid, tid, ch.stride, ch.count))
                w('')
                un = unresolved_of(dict(stride=ch.stride, fields=[]), s3.raw_records(tid))
                for s, e, d in un[:30]:
                    w('- +0x%02X..+0x%02X : %s' % (s, e - 1, d))
                if len(un) > 30:
                    w('- ... (%d개 구간 더)' % (len(un) - 30))
                w('')
            else:
                w('- 표 %d: 개수 %d 표지 (stride 0)' % (tid, ch.count))
    w('')
    w('### 4.z 시나리오 정정·충돌 메모')
    w('')
    w('- **정정(해결, L1)**: 세력 레코드 우호도 배열은 `+0x02` 부터 **52칸**(`+0x35` 까지, 인덱스 = 세력 슬롯, 자기 칸 100)이다. 덤프 1940601 의 세력 행(`+0x14` 부터 51칸 = 런타임 `+0x13+슬롯`)과 51 x 51 = 2601 칸이 모두 일치한다. 옛 `extract.py` 는 `+0x13` 에서 읽어 17칸 밀려 있었다. 시나리오 파일의 세력 슬롯 번호와 도시·무장의 `force` 번호(= 런타임 번호 13,14,15,16..)는 다르다(슬롯 21 = 런타임 16 등): 엔진 행렬은 지배자 무장의 `force` 로 슬롯을 변환한다(`extract.py`).')
    w('- **정정(해결, L1)**: 관문 레코드 +3/+7/+11 = (금, 군량, 병사) 이다. 덤프 1940601 관문 52..61 의 병사 3000/0/3000/0/0/2000/3000/2000/1000/2000 이 `+0x0B` 와 일치하고 금·군량은 둘 다 0 이다. 중립 관문의 덤프 내구는 최대의 절반(4000/8000, 2500/5000)이다(시나리오 내구는 최대값).')
    w('- **정정**: 지역 레코드 시작이 청크 base-2 (SBM 의 0x57FC) — 지역 표 한 곳만 청크 base 와 어긋남.')
    w('- **정정(해결, L1)**: 도시 규모는 도시 레코드 +0x14 = 런타임 +0xB8 이다(덤프 1940601 51/51 일치). 시나리오 03·57·8 은 내구 2000/3000/4000 과 1:1 이나 마제(31)는 수춘·강릉이 규모 2·내구 2000 이라 내구로 유도하면 틀린다. 영웅집결(8, 251년)은 전 도시 규모 1. 규모는 플레이 중 도시별로 1→2→3 으로 올라간다(덤프: 1→2 가 196~208년, 2→3 이 202~217년, 도시마다 다른 달; 조건은 rules_domestic 5절 27B4B0 규칙으로 확정). `bases[].size` 가 이 값을 담는다.')
    w('- **해결(L1)**: 기존 `data/scenarios/*.json` 은 11-04 생성, 게임 파일은 11-05 15:21 갱신이라 무장 743 의 개성 순서 한 건이 달랐다(집합은 같음). `tools/extract/extract.py` 를 origlib 호출로 바꿔 4개 시나리오를 다시 만들었다(시험 `tests/test_l1_data.py` 가 JSON = 재생성 결과를 지킨다). 개성은 9칸 중 앞 8칸만 JSON 에 둔다(엔진은 앞 5칸 사용).')
    w('- 표 7(3001x6B)은 칸 슬롯 표로 보임: `u16 칸 번호, u8 시설(0/1 도시 51/2 관문 10), u8 세력, u16 내구` — 도시 51 + 관문 10 이 표 1·2 의 내구와 일치(추정).')
    w('- 표 31 은 오프닝 내레이션 8줄 (213B: u8 종류, u32 a, u32 b, 204B 문장 UTF-16LE). 시험 `Scn` 에 문장 확인 없음, CLI 로 `scenario 2 narration` 확인.')
    w('')
    # ---------------------------------------------------------------- 5 msg
    w('## 6. 문자열 상세')
    w('')
    w("컨테이너 `zp1`: `u32 magic 'zp1\\0', u32 total_raw, u32 chunk_size, u32 nchunks, u32 sizes[nchunks]`, 0x800 부터 청크마다 `u32 (n-4) + zlib` (128B 정렬). 근거: `AI_TacticsMod/research/ui_atlas/read_messages.py`(검증) + origlib 재구현.")
    w('')
    for name in MSG_FILES:
        t = msg_table(name)
        if name.startswith('msggame'):
            w('### 6.%s (%d 바이트, 구간 %d)' % (name, len(t.raw), t.nsections()))
            w('')
            w('구간 구조: `u32 nsec, nsec x (u32 offset, u32 size)`, 구간 = `u32 count, u32 오프셋[count], 본문`. 메시지 id = 구간 x 10000 + 번호 (UI 관례; EXE 조회 코드 확인은 아님 -> 추정). 본문 텍스트는 `07 07 01 <UTF-16LE> 07 07 02` 구간들, 그 밖의 바이트는 색·줄 제어 코드(`^02`=이름색 등은 UTF-16 텍스트 안).')
            w('')
            w('| 구간 | 개수 | 예시 |')
            w('|---|---|---|')
            for s in range(t.nsections()):
                ex = ''
                for i in range(min(t.count(s), 300)):
                    x = t.get(s, i)
                    if len(x) > 4:
                        ex = x.replace('\n', ' ')[:30]
                        break
                w('| %d | %d | %s |' % (s, t.count(s), ex))
            w('')
        else:
            w('### 6.%s (%d 바이트)' % (name, len(t.raw)))
            w('')
            w("바깥 구간 표의 유일한 항목 안에 구간 표와 XL 블록 4개가 있다. XL 블록은 `+0x00 'XL', +0x02 u16 버전 0x13, +0x08 u16 행 수, +0x0A u16 행 간격 4, +0x0C u32 열 수 1, +0x10 u32 표 시작(이 설치본은 0x18), +0x14 열 종류 0`이다. 각 행의 u32 오프셋을 표 시작에 더하면 해당 NUL 종결 UTF-16LE 문자열의 위치가 된다(`3E5E00/3E5F00`).")
            w('')
            w('블록별 행 수는 %s이다.' % '/'.join(str(t.count(i)) for i in range(t.nsections())))
            w('')
            w("로더 `30C0B0`은 한국어 `msgdata_exce.bin`을 초기화한다. `30F010`은 블록 1의 0..2999를 UI 이름으로 읽는다. 따라서 원작 버튼 키 `0x5FA`는 `origlib.msg(10000 + 0x5FA, 'msgdata_exce')`에서 「관문정보」다. origlib에서는 구간×10000+번호로 조회한다. CE 블록 3의 마지막 11개(10000..10010번)는 origlib ID 40000..40010이다.")
            w('')
    w('')
    # ---------------------------------------------------------------- map
    w('## 7. 지도 (0000/Map.bin, MapExCe.bin)')
    w('')
    w('```')
    w(mapbin.__doc__.strip())
    w('```')
    m = mapbin.load_map()
    w('')
    w('측정: MapExCe 와 Map 은 지형(+4)·지역(+6) 칸이 일부 다르다(CE 가 편집). 지형 종류 24(Map 23), 지역 번호 0..343. 칸 번호 <-> (x,y) = (i%220, i//220) (헥스 배치 방식은 지도 문서 worldmap_spec 참조).')
    cc = collections.Counter(m.terrain(i) for i in range(mapbin.N))
    w('')
    w('지형 id 분포(MapExCe): ' + ', '.join('%d:%d' % kv for kv in sorted(cc.items())))
    w('')
    # ---------------------------------------------------------------- misc
    w('## 8. 0000 폴더의 나머지')
    w('')
    w('### 8.1 구간 컨테이너 파일')
    w('')
    for n in misc0000.SECTION_FILES:
        w('- `%s.bin`: ' % n + ', '.join('구간 %d: %d개 x %sB' % (k, s[2], s[3]) for k, s in enumerate(misc0000.read_sections(n))))
    w('')
    for n in misc0000.SECTION_FILES:
        secs = misc0000.read_sections(n)
        for k, s in enumerate(secs):
            spec = misc0000.SPECS.get((n, k))
            if n == 'experience_data' and k > 1:
                continue
            w('#### %s 구간 %d (%d x %sB)' % (n, k, s[2], s[3]))
            w('')
            if spec:
                field_table(spec, s[4])
            else:
                for st, e, d in misc0000.section_unresolved(n, k)[:24]:
                    w('- +0x%02X..+0x%02X : %s' % (st, e - 1, d))
                w('')
    w('경험치 구간(MISC 3): 구간 0 = 레벨 표 11행, 구간 1 = 능력치값 1..100 별 누적 경험치(통무지정 같은 값, 매력 다름), exce 의 구간 2(7x15B)·3(16x6B)은 미해독.')
    w('')
    w('### 8.2 행동 트리 (bt.bin / bt_exce.bin)')
    w('')
    w(misc0000.__doc__.split('bt*.bin:')[1].split('Evidence')[0].strip() if 'bt*.bin:' in misc0000.__doc__ else '')
    b = misc0000.load_bt(True)
    b0 = misc0000.load_bt(False)
    w('')
    w('측정: bt_exce.bin 구간(offset,size,hash) = ' + str(b.sections) + ', 노드 수 = %s; bt.bin 노드 수 = %s.' % ([len(b.tree(i)[1]) for i in range(4)], [len(b0.tree(i)[1]) for i in range(4)]))
    w('REA 합본 6절(10-22 시점)의 노드 수는 10312/246/348/111 이었고 현재 bt_exce.bin(11-05 15:21 갱신)은 구간 순서 246/10790/348/111 이다(주 트리 +478 노드, 갱신). 조건 번호표·노드 의미는 K2 문서(원작 AI) 담당.')
    w('')
    w('### 8.3 effect_info / se_info')
    w('')
    w('effect_info.bin 548B = 4B x 137 (바이트 4개 레코드, 의미 미해결: 값 분포) ; se_info.bin(215B)·se_info_exce.bin(220B) 는 전부 0 (미사용, MEAS).')
    ei = misc0000.effect_info()
    for j in range(4):
        col = collections.Counter(r[j] for r in ei)
        w('- effect_info 바이트 %d: distinct=%d %s' % (j, len(col), col.most_common(5)))
    w('')
    # ---------------------------------------------------------------- events
    w('## 9. 이벤트 스크립트 (0004)')
    w('')
    w('```')
    w(event.__doc__.strip())
    w('```')
    w('')
    w('| 파일 | 이벤트 수 | 조건 레코드 | 행동 레코드 | 텍스트 표 |')
    w('|---|---|---|---|---|')
    for f in event.event_files():
        e = event.events(f)
        nc = sum(len(x.conditions) for x in e.events())
        na = sum(len(x.actions) for x in e.events())
        w('| %s | %d | %d | %d | %s |' % (f, e.n, nc, na, e.text_table()))
    w('')
    w('### 9.4 opcode 통계 (Event001 + EventPKCE001 합산; (종류, 코드) -> 레코드 수, 쓰는 이벤트 수, 인수1..8 의 (distinct,min,max))')
    w('')
    w('현재판 실행·설명 함수와 RTTI 클래스는 [이벤트 코드 색인](event_opcodes.json)에 454개 전수 매핑했다. [날짜 6.1절](rules_time.md)에서 스크립트 대조 및 실행 호출을 확인할 수 있다. 아래 표는 두 파일의 인수 분포이며 각 명령 인수의 뜻은 실행 함수에서 확인한다.')
    w('')
    agg = collections.defaultdict(lambda: [0, 0, None])
    for f in ('Event001.s14', 'EventPKCE001.s14'):
        for k, (c, ne, cols) in event.opcode_stats(event.events(f)).items():
            a = agg[k]
            a[0] += c
            a[1] += ne
            if a[2] is None:
                a[2] = [list(x) for x in cols]
            else:
                for j, x in enumerate(cols):
                    a[2][j] = [max(a[2][j][0], x[0]), min(a[2][j][1], x[1]), max(a[2][j][2], x[2])]
    w('| 종류 | 코드 | 레코드 | 이벤트 | 인수1 | 인수2 | 인수3 | 인수4 | 인수5 | 인수6 | 인수7 | 인수8 |')
    w('|---|---|---|---|---|---|---|---|---|---|---|---|')
    for (kind, code), (c, ne, cols) in sorted(agg.items()):
        w('| %s | %d | %d | %d | ' % (kind, code, c, ne) + ' | '.join('%d/%d/%d' % tuple(x) for x in cols) + ' |')
        cnt['opcode(%s)' % kind] += 1
    w('')
    w('### 9.5 EventSample*.s14')
    w('')
    w('`u32 1` 로 시작하는 편집기 샘플 이벤트 목록(제목 `샘플이벤트（…）` + 설명 UTF-16LE + 이진). 게임 이벤트 스크립트가 아니다. 구조 미해결, 언어별 5개 중 Ko만 범위.')
    w('')
    # ---------------------------------------------------------------- dlc
    w('## 10. DLC')
    w('')
    w(dlc.__doc__.strip())
    w('')
    w('| 파일 | 계층 | 번호 | 초기 state | 이름 |')
    w('|---|---|---|---|---|')
    for f, tier, num, st in dlc.dlc_scenarios():
        c = dlc.load_dlc_scenario(f)
        w('| %s | %s | %d | %s | %s |' % (f, tier, num, st, s14.wstr(c.header, 0x1A6, 0x22)))
    w('')
    w('DLCInfo*.s14 (%d개): ' % len(dlc.dlc_info_files()) + ', '.join(dlc.dlc_info_files()[:8]) + ' ... 크기 7~1100B, 엔트로피 높음. 0011/gd_*.s14 %d개 x 846B. 같은 XOR 스트림(초기 state = 번호/번호²/0/1)으로는 풀리지 않았다 -> 미해결.' % len(dlc.dlc_gd_files()))
    w('')
    # ---------------------------------------------------------------- summary
    w('## 11. 요약 수치')
    w('')
    w('- 스펙 필드: 확정 %d, 추정 %d (위 표들의 합)' % (cnt['확정'], cnt['추정']))
    w('- 미해결 가변 바이트 구간(스펙 밖, 표당 최대 48줄 표시): %d' % cnt['미해결 바이트(가변)'])
    w('- Event001/PKCE001의 통계에 등장한 코드: 조건 %d종, 행동 %d종. 실행·설명 주소는 [이벤트 코드 색인](event_opcodes.json).' % (cnt['opcode(cond)'], cnt['opcode(act)']))
    OUT.write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('wrote', OUT, len(L), 'lines', dict(cnt))


if __name__ == '__main__':
    main()
