# 삼국지14 원본 데이터 파일 형식 — 게임 데이터 해체 (0000 · 0001_KO · 0004 · 0010_KO · DLC)

생성: `python -X utf8 -m origlib.gen_doc` (San14Library 에서). 코드: `San14Library/origlib/`, 시험: `San14Library/tests/test_origlib.py`, 사용법: `San14Library/origlib/README.md`.
이 문서의 표(필드·미해결 분포·stride·opcode 통계)는 파일에서 직접 측정해 만든 것이고, 해석 문장은 아래 근거 약어를 단다.

범위: 한국어(KO)와 언어 무관 폴더만 (사용자 2026-11-07). 0001_EN/JP/SC/TC·0010_EN/JP/SC/TC·DLC 다른 언어 폴더는 다루지 않는다. 0002·0005 아카이브는 `data_formats_archives.md`(K4).

확신도: **확정** = 편집기 오라클/교차 대조/이미 검증된 표/덤프 일치(근거 약어 표기), **추정** = 값 패턴만, **미해결** = 스펙에 없는 바이트(값 분포 실측 수록). 주의: 이 파일들의 필드 의미는 EXE 읽기 코드(ghidra_full)로 새로 확인한 것이 아니라 참고 모드 분석서(FRM 등)와 기존 표 + 이번 실측이다 — 코드 확인이 필요한 필드는 미해결/추정으로 남겼다.

근거 약어: FRM=reference_mod/Modding_DOCS/format/FIXDATA_RECORD_MAP.md · FSIG=FIXDATA_SIGNATURE.md · MISC=MISC_DATA_FILES.md · SBM=SCENARIO_BODY_MAP.md · SGM=SAVE_GENERAL_MAP.md · SCF=SAVE_CITY_FACTION_MAP.md · REA6=REA_Analysis/1022_REA_분석_전체합본.md 6절 · WT=San14Library/archive/tools/worldmap_tables.py·gen_facility_tables.py(검증 표) · EXT=San14Library/archive/tools/extract/*.py · ORIG=origlib 시험이 기존 data/*.json과 대조 · MEAS=이번 실측.

## 1. 파일 인벤토리 (무엇이 어디)

| 위치 | 파일 | 형식 | 로더 | 절 |
|---|---|---|---|---|
| 0000/ | Map.bin, MapExCe.bin | 4B 칸 수 + 48400x16B 칸 | origlib.load_map(exce) | 7 |
| 0000/ | bt.bin, bt_exce.bin | JBTP 행동 트리 컨테이너 4트리 | origlib.load_bt(exce) | 8.2 |
| 0000/ | ccscore_data, change_force_data, opcamera_data, param_s, experience_data(_exce) | 구간 컨테이너 (u32 n; n x(off,size); 구간=u32 개수+레코드) | misc0000.read_sections/section_table | 8.1 |
| 0000/ | effect_info.bin, se_info(_exce).bin | 4B 레코드 137개 / 0으로 찬 215·220B | misc0000.effect_info | 8.3 |
| 0001_KO/ | msgdata(_exce).bin, msggame(_exce).bin | 'zp1' zlib 청크 컨테이너 -> 구간 -> 문자열 | origlib.msg(id, table) / origlib.find_text | 6 |
| 0004/ | Event001, EventPKCE001, CCEvent050-054, CCEventPKCE*, EventTutorial(PKCE) | 비압축 이벤트 스크립트 (조건/행동 44B 레코드) | origlib.events(file) | 9 |
| 0004/ | EventSample{Ko,En,Jp,Sc,Tc}.s14 | 편집기용 샘플 목록(UTF-16 제목·설명+이진) | (미해체: Ko만 범위, 목록 용도) | 9.5 |
| 0010_KO/ | fixdata.s14 / fixdataexce.s14 | S14 헤더 + LWC, 표 연쇄 (base 51 / CE 102) | origlib.load_fixdata(exce) | 2-3 |
| 0010_KO/ | sceda01-08,55-57,71 (base) / scedaexce 50개(번호 1-9,12-18,21-28,30-31,34-35,55-63,71-73,100-104,150-154) (CE) | S14 헤더 + LWC, 표 연쇄 | origlib.load_scenario(id) | 4 |
| DLC/0010_KO/ | sceda09-29, scedaex09-29,150-154, scedaexce10-11,32-33 | XOR 포장 후 S14 | origlib.dlc.load_dlc_scenario(file) | 10 |
| DLC/ | DLCInfo*.s14 (45), 0011/gd_*.s14 | 암호화(미해독) | 목록만 | 10 |
| DLC/ | 0003/*.wmv, 0005/*.bin | 동영상 / 아카이브(K4) | - | 10 |

## 2. 공통 컨테이너

### 2.1 S14 헤더 + LWC (fixdata·sceda·scedaexce)

- 평문 헤더: base 480B(ver 51), PK 754B(ver 92), CE 754B(ver 102). +0x04 `SN14SCEXVER0001`, +0x14 소개문(UTF-16LE), +0x1A6 이름, +0x1C8 u16 시작 년, +0x1CA u8 분류(1 일반/2 튜토리얼/4 신군주), +0x1CB u8 계층 버전, +0x1CD u8 시작 월, +0x1CE u8 시나리오 번호 (SBM; 50개 CE 시나리오로 MEAS 확정).
- 헤더 +0x1CF u32 = fixdata 본문 서명 `pow(sum(body)&0xFFFF, 5, 0x3FDE03A3)` (FSIG; 시험이 재확인). 시나리오는 0. 검사 코드는 EXE RVA 0x32A290 로더(옛 빌드 기준 RVA, FSIG).
- 이어서 `LWC\x1a` 블록 1개: `u32 raw_size, u32 comp_size, u8[256] 심볼표, 비트스트림` (`origlib/lwc.py`, 기존 tools/extract/lwc.py 복사·통합. 디코더 해석은 LWC_FORMAT.md/EXE 0x140001EDD 근거).

### 2.2 표 연쇄 (chunk chain)

본문은 `<u32 표ID><u32 레코드수>` + 레코드수 x stride 바이트가 끝까지 틈 없이 이어진 연쇄다 (SBM 1(3)절). **stride 는 파일에 없다**: `s14.walk_chain` 이 DFS 로 "다음 헤더가 sane 한 id/개수로 나타나고 연쇄가 파일 끝에 정확히 닿는" stride 를 찾는다 (fixdataexce: 44개 표 전부, 0.1초; 시나리오 50개 CE 전부 연쇄 완주 — 시험). stride 0 인 표는 개수만 선언된 표지(데이터 없음)다.

fixdataexce 연쇄 (ID, 레코드수, stride, 본문 base — 측정):

| ID | 키 | 이름 | 개수 | stride | base | 스펙 필드 수 |
|---|---|---|---|---|---|---|
| -1 | region_group | 지역구분 | 12 | 20 | 0x08 | 2 |
| 0 | state | 주(州) | 23 | 32 | 0x100 | 5 |
| 1 | city | 도시 | 52 | 53 | 0x3E8 | 8 |
| 2 | gate | 관문 | 11 | 40 | 0xEB4 | 3 |
| 3 | slot_pair | (미명명, 52x2B) | 52 | 2 | 0x1074 | 0 |
| 4 | marker4 | (개수 표지 52) | 52 | 0 | 0x10E4 | 0 |
| 5 | cell_grid | (칸 표 220x220, 3B) | 48400 | 3 | 0x10EC | 1 |
| 6 | area | 지역 | 501 | 65 | 0x24824 | 11 |
| 7 | marker7 | (개수 표지 3001) | 3001 | 0 | 0x2C761 | 0 |
| 8 | terrain | 지형 | 31 | 51 | 0x2C769 | 4 |
| 9 | facility | 시설 | 31 | 53 | 0x2CD9E | 21 |
| 10 | marker10 | (개수 표지 1851 = 무장 슬롯) | 1851 | 0 | 0x2D411 | 0 |
| 11 | formation | 진형 | 21 | 152 | 0x2D419 | 12 |
| 12 | tactic | 전법 | 201 | 94 | 0x2E099 | 8 |
| 13 | treasure | 명품 | 202 | 22 | 0x32A6F | 7 |
| 14 | nation | 국호 | 101 | 127 | 0x33BD3 | 3 |
| 15 | rank | 관작 | 13 | 166 | 0x36DF6 | 4 |
| 16 | office | 관직 | 256 | 46 | 0x3766C | 7 |
| 17 | principle | 주의 | 11 | 102 | 0x3A474 | 7 |
| 18 | policy | 정책 | 121 | 148 | 0x3A8DE | 7 |
| 19 | tactic_book | 전법서 | 31 | 21 | 0x3EEDA | 2 |
| 20 | tab20 | (미명명, 13Bx400) | 400 | 13 | 0x3F16D | 0 |
| 21 | marker21 | (개수 표지 2001) | 2001 | 0 | 0x405C5 | 0 |
| 22 | trait | 개성 | 356 | 170 | 0x405CD | 12 |
| 23 | ? | ? | 501 | 0 | 0x4F23D | 0 |
| 24 | ? | ? | 31 | 0 | 0x4F245 | 0 |
| 25 | ? | ? | 501 | 0 | 0x4F24D | 0 |
| 26 | policy_effect | 정책효과 | 101 | 134 | 0x4F255 | 2 |
| 27 | ? | ? | 501 | 0 | 0x5273B | 0 |
| 28 | tab28 | (미명명, 11Bx49) | 49 | 11 | 0x52743 | 0 |
| 29 | tab29 | (미명명, 26Bx501) | 501 | 26 | 0x52966 | 0 |
| 30 | ? | ? | 51 | 0 | 0x55C50 | 0 |
| 31 | ? | ? | 8 | 0 | 0x55C58 | 0 |
| 32 | tab32 | (미명명, 14Bx50) | 50 | 14 | 0x55C60 | 0 |
| 33 | ? | ? | 201 | 0 | 0x55F24 | 0 |
| 34 | ? | ? | 31 | 0 | 0x55F2C | 0 |
| 35 | geo | 지리 | 18 | 138 | 0x55F34 | 5 |
| 36 | trade_nation | 교역국 | 5 | 29 | 0x568F0 | 7 |
| 37 | trade_perk | 교역특전 | 9 | 77 | 0x56989 | 3 |
| 38 | scenic | 명승지 | 101 | 80 | 0x56C46 | 5 |
| 39 | merit_reward | 공적 보상 | 7 | 4 | 0x58BDE | 3 |
| 40 | tab40 | (미명명, 34Bx31) | 31 | 34 | 0x58C02 | 0 |
| 41 | tab41 | (미명명, 37Bx80) | 80 | 37 | 0x59028 | 0 |
| 42 | tab42 | (미명명, 35Bx7) | 7 | 35 | 0x59BC0 | 0 |
| 43 | ? | ? | 100 | 0 | 0x59CBD | 0 |

## 3. fixdata 표 (0010_KO/fixdataexce.s14, CE v102)

API: `origlib.load_fixdata()` -> `{키: [레코드 dict]}` (각 dict 에 `_id`, `_raw`). `fixdata.FixData().table(키|한글이름)`, `.unresolved(id)`.
이름 문자열은 레코드 안(UTF-16LE)에 있다 (msg 파일에는 없음: 이름·발음·설명이 fixdata 안에 인라인 — 시험으로 확인).

### 3.a 표 -1 `region_group` — 지역구분 (20B x 12)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | w6(6B) | name | 지역구분 이름(하북·중원·서북·오월·형초·파촉+이민족5) | FRM | 확정 |
| +0x06 | w6(6B) | reading | 발음(KO는 이름과 같음) | FRM | 확정 |

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x0C..+0x13 : 상수 0x00

### 3.0 표 0 `state` — 주(州) (32B x 23)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | w10(10B) | name | - | FRM | 확정 |
| +0x0A | w14(14B) | reading | - | FRM | 확정 |
| +0x18 | w6(6B) | abbr | 약칭 | FRM | 확정 |
| +0x1E | u8(1B) | region_group | 지역구분 번호 | FRM | 확정 |
| +0x1F | u8(1B) | geo | 지리 표(id35) 번호, 이민족 0 | FRM | 확정 |

### 3.1 표 1 `city` — 도시 (53B x 52)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | w8(8B) | name | - | FRM;ORIG | 확정 |
| +0x08 | w8(8B) | reading | - | FRM | 확정 |
| +0x1C | u8x10(10B) | adjacent | 인접 거점(0=없음) | FRM | 확정 |
| +0x28 | u32(4B) | max_gold | - | FRM | 확정 |
| +0x2C | u32(4B) | max_food | - | FRM | 확정 |
| +0x30 | u32(4B) | max_troops | - | FRM | 확정 |
| +0x27 | u8(1B) | id | 거점 번호(슬롯과 같음 0..51, MEAS) | MEAS | 추정 |
| +0x34 | u8(1B) | state | 주(州) 번호(52/52) | FRM | 확정 |

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x10..+0x1B : 상수 0x00
- +0x26..+0x26 : 상수 0x00

### 3.2 표 2 `gate` — 관문 (40B x 11)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | w8(8B) | name | - | FRM | 확정 |
| +0x08 | w8(8B) | reading | - | FRM | 확정 |
| +0x1C | u8x10(10B) | adjacent | 인접 거점 | FRM | 확정 |

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x10..+0x1B : 상수 0x00
- +0x26..+0x26 : 상수 0x00
- +0x27..+0x27 : u8 distinct=11 min=0 max=10 top=[(0, 1), (1, 1), (2, 1)]

### 3.3 표 3 `slot_pair` — (미명명, 52x2B) (2B x 52)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x00..+0x00 : u8 distinct=48 min=0 max=239 top=[(0, 3), (182, 2), (85, 2)]
- +0x01..+0x01 : u8 distinct=5 min=0 max=16 top=[(0, 14), (2, 13), (3, 13)]

### 3.4 표 4 `marker4` — (개수 표지 52) (0B x 52)

개수 표지 (데이터 없음).

### 3.5 표 5 `cell_grid` — (칸 표 220x220, 3B) (3B x 48400)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | u8(1B) | a | 첫 바이트 (값 분포는 문서 참조) | - | 추정 |

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x01..+0x01 : u8 distinct=256 min=0 max=255 top=[(0, 12583), (84, 635), (53, 503)]
- +0x02..+0x02 : u8 distinct=2 min=0 max=1 top=[(0, 37669), (1, 10731)]

### 3.6 표 6 `area` — 지역 (65B x 501)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | w10(10B) | name | - | FRM;WT | 확정 |
| +0x0A | w10(10B) | reading | - | FRM | 확정 |
| +0x24 | u8(1B) | base | 소속 거점 | FRM;EXT | 확정 |
| +0x25 | u16(2B) | center_cell | 중심 칸 번호(지도 칸) | FRM;EXT | 확정 |
| +0x27 | u16(2B) | security_ref | 치안 기준(100) | FRM | 확정 |
| +0x29 | u16(2B) | commerce_ref | 상업 기준(양평 290) | FRM | 확정 |
| +0x2B | u16(2B) | agri_ref | 농업 기준(양평 1190) | FRM | 확정 |
| +0x2D | u16(2B) | barracks_ref | 병영 기준(양평 600) | FRM | 확정 |
| +0x2F | u16x8(16B) | adjacent | 인접 지역 | FRM;EXT | 확정 |
| +0x3F | u8(1B) | build_cap | 건설 상한(0~11) | FRM;WT area_fac_cap | 추정 |
| +0x40 | u8(1B) | adj_flags | 인접 제한 비트(0xFF가 대부분) | FRM | 추정 |

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x14..+0x23 : 상수 0x00

### 3.7 표 7 `marker7` — (개수 표지 3001) (0B x 3001)

개수 표지 (데이터 없음).

### 3.8 표 8 `terrain` — 지형 (51B x 31)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | w8(8B) | name | - | EXT | 확정 |
| +0x08 | w18(18B) | reading | - | FRM | 확정 |
| +0x1A | u16(2B) | move_cost | 이동 비용(EXE BE120 반환) | EXT terrain_table | 확정 |
| +0x1C | u8(1B) | flag | - | EXT | 추정 |

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x1D..+0x1E : 상수 0x00
- +0x1F..+0x1F : u8 distinct=2 min=0 max=100 top=[(100, 28), (0, 3)]
- +0x20..+0x20 : 상수 0x00
- +0x21..+0x21 : u8 distinct=2 min=0 max=100 top=[(100, 28), (0, 3)]
- +0x22..+0x22 : 상수 0x00
- +0x23..+0x23 : u8 distinct=2 min=0 max=100 top=[(100, 28), (0, 3)]
- +0x24..+0x24 : 상수 0x00
- +0x25..+0x25 : u8 distinct=2 min=0 max=100 top=[(100, 28), (0, 3)]
- +0x26..+0x26 : 상수 0x00
- +0x27..+0x27 : u8 distinct=2 min=0 max=100 top=[(100, 28), (0, 3)]
- +0x28..+0x28 : 상수 0x00
- +0x29..+0x29 : u8 distinct=2 min=0 max=100 top=[(100, 28), (0, 3)]
- +0x2A..+0x2A : 상수 0x00
- +0x2B..+0x2B : u8 distinct=2 min=0 max=100 top=[(100, 28), (0, 3)]
- +0x2C..+0x2C : 상수 0x00
- +0x2D..+0x2D : u8 distinct=2 min=0 max=100 top=[(0, 18), (100, 13)]
- +0x2E..+0x2E : 상수 0x00
- +0x2F..+0x2F : u8 distinct=3 min=0 max=2 top=[(0, 23), (1, 6), (2, 2)]
- +0x30..+0x30 : u8 distinct=4 min=0 max=3 top=[(0, 17), (1, 8), (3, 4)]
- +0x31..+0x31 : u8 distinct=11 min=0 max=10 top=[(0, 9), (2, 6), (1, 3)]
- +0x32..+0x32 : 상수 0x00

### 3.9 표 9 `facility` — 시설 (53B x 31)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | w10(10B) | name | - | WT | 확정 |
| +0x0A | w10(10B) | reading | - | WT | 확정 |
| +0x1C | u8(1B) | cls | 분류(2군사,3방벽,4함정,1거점) | WT | 확정 |
| +0x1D | u16(2B) | hp | 내구 | WT | 확정 |
| +0x1F | u16(2B) | cost | 건설 비용 | WT | 확정 |
| +0x21 | u16(2B) | f21 | - | WT | 추정 |
| +0x23 | u8(1B) | need_effect | 필요 효과 id | WT | 확정 |
| +0x24 | u8(1B) | interval | 발동 간격 | WT | 확정 |
| +0x25 | u8(1B) | eff1_kind | - | WT | 확정 |
| +0x26 | u8(1B) | eff1_v | - | WT | 확정 |
| +0x27 | u8(1B) | eff1_v2 | - | WT | 확정 |
| +0x28 | u8(1B) | eff2_kind | - | WT | 확정 |
| +0x29 | u8(1B) | eff2_v | - | WT | 확정 |
| +0x2A | u8(1B) | eff2_v2 | - | WT | 확정 |
| +0x2B | u8(1B) | min_dist | 대상 최소 거리(2AD8F0) | WT | 확정 |
| +0x2C | u8(1B) | range | 사거리 | WT | 확정 |
| +0x2D | u8(1B) | f2d | - | WT | 추정 |
| +0x2E | u32(4B) | terrain_mask | 설치 가능 지형 마스크 | WT | 확정 |
| +0x32 | u8(1B) | sub | - | WT | 추정 |
| +0x33 | u8(1B) | thr | 문턱값 | WT | 확정 |
| +0x34 | u8(1B) | f34 | - | WT | 추정 |

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x14..+0x1B : 상수 0x00

### 3.10 표 10 `marker10` — (개수 표지 1851 = 무장 슬롯) (0B x 1851)

개수 표지 (데이터 없음).

### 3.11 표 11 `formation` — 진형 (152B x 21)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | w6(6B) | name | - | FRM;ORIG | 확정 |
| +0x06 | w14(14B) | reading | - | FRM | 확정 |
| +0x14 | u8x8(8B) | usage | 용도(야전·유격·제압) | FRM | 확정 |
| +0x1C | w82(82B) | desc | - | FRM | 확정 |
| +0x6E | u8(1B) | water | - | EXT;ORIG | 확정 |
| +0x6F | u8(1B) | mobility | - | EXT;ORIG | 확정 |
| +0x73 | u8(1B) | attack | - | EXT;ORIG | 확정 |
| +0x74 | u8(1B) | siege | - | EXT;ORIG | 확정 |
| +0x75 | u8(1B) | demolition | - | EXT;ORIG | 확정 |
| +0x76 | u8(1B) | defense | - | EXT;ORIG | 확정 |
| +0x89 | u16(2B) | cost | - | EXT;ORIG | 확정 |
| +0x95 | u8(1B) | ranged | - | EXT;ORIG | 확정 |

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x70..+0x70 : u8 distinct=7 min=0 max=120 top=[(0, 8), (120, 5), (80, 2)]
- +0x71..+0x71 : u8 distinct=8 min=0 max=200 top=[(0, 10), (200, 3), (150, 2)]
- +0x72..+0x72 : 상수 0x00
- +0x77..+0x78 : 상수 0x00
- +0x79..+0x79 : u8 distinct=2 min=0 max=100 top=[(100, 20), (0, 1)]
- +0x7A..+0x7A : 상수 0x00
- +0x7B..+0x7B : u8 distinct=2 min=0 max=100 top=[(100, 20), (0, 1)]
- +0x7C..+0x7C : 상수 0x00
- +0x7D..+0x7D : u8 distinct=2 min=0 max=100 top=[(100, 20), (0, 1)]
- +0x7E..+0x7E : 상수 0x00
- +0x7F..+0x7F : u8 distinct=2 min=0 max=100 top=[(100, 20), (0, 1)]
- +0x80..+0x80 : 상수 0x00
- +0x81..+0x81 : u8 distinct=2 min=0 max=100 top=[(100, 20), (0, 1)]
- +0x82..+0x82 : 상수 0x00
- +0x83..+0x83 : u8 distinct=2 min=0 max=100 top=[(100, 20), (0, 1)]
- +0x84..+0x84 : 상수 0x00
- +0x85..+0x85 : u8 distinct=2 min=0 max=100 top=[(100, 20), (0, 1)]
- +0x86..+0x86 : 상수 0x00
- +0x87..+0x87 : u8 distinct=2 min=0 max=100 top=[(100, 20), (0, 1)]
- +0x88..+0x88 : 상수 0x00
- +0x8B..+0x94 : 상수 0x00
- +0x96..+0x96 : 상수 0x00
- +0x97..+0x97 : u8 distinct=2 min=0 max=1 top=[(0, 14), (1, 7)]

### 3.12 표 12 `tactic` — 전법 (94B x 201)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | w10(10B) | name | - | FRM;ORIG | 확정 |
| +0x0A | w38(38B) | reading | - | FRM | 확정 |
| +0x30 | u8(1B) | family | 계통 | FRM;ORIG | 확정 |
| +0x31 | u16(2B) | wait | 대기시간(48/72/90) | FRM;ORIG | 확정 |
| +0x33 | u8(1B) | flags | bit1 활성(콜라보 해금) bit0 lp42 | FRM;ORIG | 확정 |
| +0x50 | u8x8(8B) | effects | 효과1,2종류 / 범위 / 치1 / 치2 | FRM;ORIG | 확정 |
| +0x58 | u8(1B) | ability | 의존 능력 1무력 2지력 | FRM;ORIG | 확정 |
| +0x59 | u32(4B) | formation_mask | 사용 진형 마스크(비트 N=진형 N) | FRM;ORIG | 확정 |

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x34..+0x35 : 상수 0x00
- +0x36..+0x36 : u8 distinct=2 min=0 max=100 top=[(100, 200), (0, 1)]
- +0x37..+0x37 : 상수 0x00
- +0x38..+0x38 : u8 distinct=2 min=0 max=100 top=[(100, 200), (0, 1)]
- +0x39..+0x39 : 상수 0x00
- +0x3A..+0x3A : u8 distinct=2 min=0 max=100 top=[(100, 200), (0, 1)]
- +0x3B..+0x3B : 상수 0x00
- +0x3C..+0x3C : u8 distinct=2 min=0 max=100 top=[(100, 200), (0, 1)]
- +0x3D..+0x3D : 상수 0x00
- +0x3E..+0x3E : u8 distinct=2 min=0 max=100 top=[(100, 200), (0, 1)]
- +0x3F..+0x3F : 상수 0x00
- +0x40..+0x40 : u8 distinct=2 min=0 max=100 top=[(100, 200), (0, 1)]
- +0x41..+0x41 : 상수 0x00
- +0x42..+0x42 : u8 distinct=2 min=0 max=100 top=[(100, 200), (0, 1)]
- +0x43..+0x43 : 상수 0x00
- +0x44..+0x44 : u8 distinct=2 min=0 max=100 top=[(100, 200), (0, 1)]
- +0x45..+0x4F : 상수 0x00
- +0x5D..+0x5D : u8 distinct=4 min=0 max=3 top=[(0, 178), (3, 10), (1, 8)]

### 3.13 표 13 `treasure` — 명품 (22B x 202)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | w14(14B) | name | - | FRM;WT | 확정 |
| +0x0E | u8(1B) | kind | 종류(1도검…11명마) | FRM;WT | 확정 |
| +0x0F | u8(1B) | ability | 1통솔~5매력 | FRM;WT | 확정 |
| +0x10 | u8(1B) | value | 능력 가산 | FRM;WT | 확정 |
| +0x11 | u8(1B) | effect | 1퇴각확실 2수명연장 | FRM;WT | 확정 |
| +0x13 | u8(1B) | worth | 가치 | FRM;WT | 확정 |
| +0x15 | u8(1B) | cg | CG 번호 | FRM | 추정 |

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x12..+0x12 : u8 distinct=2 min=0 max=10 top=[(0, 196), (10, 6)]
- +0x14..+0x14 : 상수 0x00

### 3.14 표 14 `nation` — 국호 (127B x 101)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | w8(8B) | name | - | FRM | 확정 |
| +0x08 | w14(14B) | reading | - | FRM | 확정 |
| +0x16 | w102(102B) | desc | - | FRM | 확정 |

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x7C..+0x7C : u8 distinct=35 min=0 max=51 top=[(0, 54), (6, 4), (14, 4)]
- +0x7D..+0x7D : u8 distinct=27 min=0 max=43 top=[(0, 64), (18, 4), (15, 2)]
- +0x7E..+0x7E : u8 distinct=2 min=0 max=1 top=[(0, 63), (1, 38)]

### 3.15 표 15 `rank` — 관작 (166B x 13)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | w26(26B) | name | - | FRM;ORIG | 확정 |
| +0x1A | w26(26B) | reading | - | FRM | 확정 |
| +0x34 | w102(102B) | desc | - | FRM | 확정 |
| +0x9A | u16(2B) | base_troops | 관작별 기준 병력 | MISC 5 | 확정 |

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x9C..+0x9C : u8 distinct=10 min=0 max=9 top=[(1, 4), (0, 1), (2, 1)]
- +0x9D..+0x9D : u8 distinct=6 min=0 max=5 top=[(5, 4), (1, 3), (0, 2)]
- +0x9E..+0x9E : u8 distinct=6 min=0 max=5 top=[(5, 4), (1, 3), (0, 2)]
- +0x9F..+0x9F : u8 distinct=6 min=0 max=5 top=[(5, 4), (1, 3), (0, 2)]
- +0xA0..+0xA0 : u8 distinct=6 min=0 max=5 top=[(5, 4), (1, 3), (0, 2)]
- +0xA1..+0xA1 : 상수 0x00
- +0xA2..+0xA2 : u8 distinct=4 min=0 max=15 top=[(15, 6), (0, 4), (7, 2)]
- +0xA3..+0xA3 : u8 distinct=6 min=0 max=5 top=[(5, 4), (0, 3), (4, 2)]
- +0xA4..+0xA4 : u8 distinct=8 min=0 max=40 top=[(40, 6), (0, 1), (30, 1)]
- +0xA5..+0xA5 : u8 distinct=9 min=0 max=36 top=[(36, 4), (33, 2), (0, 1)]

### 3.16 표 16 `office` — 관직 (46B x 256)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | w10(10B) | name | - | FRM;ORIG | 확정 |
| +0x0A | w26(26B) | reading | - | FRM | 확정 |
| +0x24 | u16(2B) | command | 지휘 병사 | FRM;ORIG | 확정 |
| +0x26 | u8(1B) | stipend | 봉록 | FRM;ORIG | 확정 |
| +0x27 | u8(1B) | rank | 관작 | FRM;ORIG | 확정 |
| +0x28 | u8x5(5B) | stats | 통무지정매 지정 | FRM;ORIG | 확정 |
| +0x2D | u8(1B) | system | 체계 | FRM;ORIG | 확정 |

### 3.17 표 17 `principle` — 주의 (102B x 11)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | w8(8B) | name | - | FRM;ORIG | 확정 |
| +0x08 | w8(8B) | reading | - | FRM | 확정 |
| +0x1C | w62(62B) | desc | - | FRM | 확정 |
| +0x5A | u8(1B) | lp67 | - | FRM | 추정 |
| +0x5B | u8x5(5B) | policy_slots | 전투·지원·모략·내정·인사 | FRM;ORIG | 확정 |
| +0x60 | u8x5(5B) | limits | 상한 | FRM;ORIG | 확정 |
| +0x65 | u8(1B) | lp72 | - | FRM | 추정 |

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x10..+0x1B : 상수 0x00

### 3.18 표 18 `policy` — 정책 (148B x 121)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | w12(12B) | name | - | FRM;ORIG | 확정 |
| +0x0C | w32(32B) | reading | - | FRM | 확정 |
| +0x2C | w92(92B) | desc | - | FRM | 확정 |
| +0x88 | u8x8(8B) | effect_ids | 발동 효과(id26 정책효과 표) | FRM;ORIG | 확정 |
| +0x90 | u8(1B) | category | - | EXT;ORIG | 확정 |
| +0x91 | u8(1B) | composite | - | EXT;ORIG | 확정 |
| +0x92 | u16(2B) | base_cost | - | EXT;ORIG | 확정 |

### 3.19 표 19 `tactic_book` — 전법서 (21B x 31)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | w12(12B) | name | - | FRM | 확정 |
| +0x0E | u8(1B) | tactic | 전법 번호 | FRM | 확정 |

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x0C..+0x0D : 상수 0x00
- +0x0F..+0x0F : u8 distinct=12 min=0 max=141 top=[(124, 6), (127, 5), (125, 3)]
- +0x10..+0x10 : u8 distinct=2 min=0 max=5 top=[(5, 30), (0, 1)]
- +0x11..+0x11 : u8 distinct=2 min=0 max=5 top=[(5, 30), (0, 1)]
- +0x12..+0x12 : u8 distinct=2 min=0 max=5 top=[(5, 30), (0, 1)]
- +0x13..+0x13 : u8 distinct=2 min=0 max=5 top=[(5, 30), (0, 1)]
- +0x14..+0x14 : u8 distinct=2 min=0 max=5 top=[(5, 30), (0, 1)]

### 3.20 표 20 `tab20` — (미명명, 13Bx400) (13B x 400)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x00..+0x00 : u8 distinct=103 min=0 max=253 top=[(4, 13), (21, 13), (0, 12)]
- +0x01..+0x01 : u8 distinct=32 min=172 max=215 top=[(199, 36), (197, 34), (198, 34)]
- +0x02..+0x03 : 상수 0x00
- +0x04..+0x04 : u8 distinct=103 min=0 max=253 top=[(4, 13), (21, 13), (0, 12)]
- +0x05..+0x05 : u8 distinct=32 min=172 max=215 top=[(199, 36), (197, 34), (198, 34)]
- +0x06..+0x0B : 상수 0x00
- +0x0C..+0x0C : u8 distinct=15 min=1 max=31 top=[(10, 88), (1, 80), (14, 46)]

### 3.21 표 21 `marker21` — (개수 표지 2001) (0B x 2001)

개수 표지 (데이터 없음).

### 3.22 표 22 `trait` — 개성 (170B x 356)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | w12(12B) | name | - | FRM;ORIG | 확정 |
| +0x0C | w32(32B) | reading | - | FRM | 확정 |
| +0x2C | w102(102B) | desc | - | FRM | 확정 |
| +0x94 | u8x2(2B) | conditions | 조건1·2 | FRM;ORIG | 확정 |
| +0x98 | u8(1B) | effect1 | - | FRM;ORIG | 확정 |
| +0x99 | i16(2B) | value1 | - | FRM;ORIG | 확정 |
| +0x9B | u8(1B) | effect2 | - | FRM;ORIG | 확정 |
| +0x9C | i16(2B) | value2 | - | FRM;ORIG | 확정 |
| +0x9E | u8(1B) | color | 1청 2적 3금 | FRM;ORIG | 확정 |
| +0x9F | u8(1B) | flags | bit0 적색발동 bit1 전투발동 bit3 곱연산 bit4 활성 | FRM;ORIG | 확정 |
| +0xA0 | i32x2(8B) | cond_values | 조건값1·2 | FRM;ORIG | 확정 |
| +0xA9 | u8(1B) | ce_extra | CE 추가 바이트(0~9) | FRM | 추정 |

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x92..+0x92 : u8 distinct=3 min=0 max=147 top=[(0, 354), (95, 1), (147, 1)]
- +0x93..+0x93 : u8 distinct=2 min=0 max=2 top=[(0, 355), (2, 1)]
- +0x96..+0x96 : u8 distinct=3 min=0 max=255 top=[(0, 291), (255, 64), (12, 1)]
- +0x97..+0x97 : u8 distinct=2 min=0 max=255 top=[(0, 292), (255, 64)]
- +0xA8..+0xA8 : 상수 0x00

### 3.26 표 26 `policy_effect` — 정책효과 (134B x 101)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | w22(22B) | name | - | FRM;ORIG | 확정 |
| +0x72 | u16x10(20B) | level_values | Lv1..10 값(101~104는 배치 다름) | FRM;ORIG | 확정 |

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x16..+0x16 : u8 distinct=22 min=9 max=252 top=[(21, 69), (128, 4), (76, 3)]
- +0x17..+0x17 : u8 distinct=18 min=0 max=215 top=[(200, 70), (189, 5), (0, 3)]
- +0x18..+0x18 : u8 distinct=22 min=0 max=244 top=[(69, 68), (0, 5), (220, 4)]
- +0x19..+0x19 : u8 distinct=17 min=0 max=214 top=[(204, 68), (179, 5), (194, 4)]
- +0x1A..+0x1A : u8 distinct=12 min=0 max=244 top=[(168, 69), (196, 7), (12, 5)]
- +0x1B..+0x1B : u8 distinct=12 min=0 max=255 top=[(214, 69), (201, 7), (255, 5)]
- +0x1C..+0x1C : u8 distinct=13 min=0 max=252 top=[(252, 69), (32, 11), (21, 8)]
- +0x1D..+0x1D : u8 distinct=12 min=0 max=255 top=[(172, 69), (0, 12), (214, 8)]
- +0x1E..+0x1E : u8 distinct=13 min=0 max=252 top=[(32, 77), (0, 5), (48, 5)]
- +0x1F..+0x1F : u8 distinct=16 min=0 max=213 top=[(0, 78), (173, 4), (181, 3)]
- +0x20..+0x20 : u8 distinct=16 min=0 max=217 top=[(36, 69), (168, 7), (208, 4)]
- +0x21..+0x21 : u8 distinct=12 min=0 max=255 top=[(193, 71), (214, 7), (197, 4)]
- +0x22..+0x22 : u8 distinct=15 min=0 max=252 top=[(133, 68), (32, 10), (252, 8)]
- +0x23..+0x23 : u8 distinct=13 min=0 max=255 top=[(186, 69), (0, 12), (172, 8)]
- +0x24..+0x24 : u8 distinct=19 min=0 max=245 top=[(133, 68), (193, 7), (32, 4)]
- +0x25..+0x25 : u8 distinct=12 min=0 max=255 top=[(199, 72), (192, 8), (0, 6)]
- +0x26..+0x26 : u8 distinct=20 min=0 max=244 top=[(200, 68), (185, 7), (92, 4)]
- +0x27..+0x27 : u8 distinct=14 min=0 max=214 top=[(178, 69), (194, 8), (0, 4)]
- +0x28..+0x28 : u8 distinct=19 min=0 max=252 top=[(228, 68), (0, 9), (32, 4)]
- +0x29..+0x29 : u8 distinct=12 min=0 max=214 top=[(178, 69), (0, 13), (172, 4)]
- +0x2A..+0x2A : u8 distinct=15 min=0 max=221 top=[(0, 80), (32, 5), (41, 3)]
- +0x2B..+0x2B : u8 distinct=12 min=0 max=255 top=[(0, 84), (188, 4), (213, 3)]
- +0x2C..+0x2C : u8 distinct=15 min=0 max=201 top=[(0, 80), (193, 3), (40, 3)]
- +0x2D..+0x2D : u8 distinct=13 min=0 max=214 top=[(0, 85), (192, 4), (214, 2)]
- +0x2E..+0x2E : u8 distinct=13 min=0 max=252 top=[(0, 82), (185, 3), (193, 3)]
- +0x2F..+0x2F : u8 distinct=8 min=0 max=201 top=[(0, 86), (172, 3), (194, 3)]
- +0x30..+0x30 : u8 distinct=11 min=0 max=237 top=[(0, 86), (58, 3), (185, 3)]
- +0x31..+0x31 : u8 distinct=10 min=0 max=255 top=[(0, 89), (194, 3), (192, 2)]
- +0x32..+0x32 : u8 distinct=12 min=0 max=221 top=[(0, 86), (201, 4), (185, 2)]
- +0x33..+0x33 : u8 distinct=12 min=0 max=255 top=[(0, 85), (183, 4), (194, 2)]
- +0x34..+0x34 : u8 distinct=9 min=0 max=196 top=[(0, 89), (32, 5), (189, 1)]
- +0x35..+0x35 : u8 distinct=8 min=0 max=213 top=[(0, 93), (193, 2), (188, 1)]
- +0x36..+0x36 : u8 distinct=9 min=0 max=201 top=[(0, 89), (12, 3), (157, 3)]
- +0x37..+0x37 : u8 distinct=9 min=0 max=255 top=[(0, 89), (255, 3), (201, 3)]
- +0x38..+0x38 : u8 distinct=8 min=0 max=185 top=[(0, 93), (28, 2), (52, 1)]
- +0x39..+0x39 : u8 distinct=5 min=0 max=255 top=[(0, 94), (172, 4), (188, 1)]
- +0x3A..+0x3A : u8 distinct=7 min=0 max=133 top=[(0, 94), (58, 2), (48, 1)]
- +0x3B..+0x3B : u8 distinct=5 min=0 max=213 top=[(0, 97), (188, 1), (213, 1)]
- +0x3C..+0x3C : u8 distinct=8 min=0 max=153 top=[(0, 94), (112, 1), (58, 1)]
- +0x3D..+0x3D : u8 distinct=6 min=0 max=213 top=[(0, 96), (173, 1), (213, 1)]
- +0x3E..+0x3E : u8 distinct=7 min=0 max=157 top=[(0, 95), (69, 1), (4, 1)]
- +0x3F..+0x3F : u8 distinct=6 min=0 max=255 top=[(0, 96), (197, 1), (178, 1)]
- +0x40..+0x40 : u8 distinct=5 min=0 max=192 top=[(0, 97), (32, 1), (58, 1)]
- +0x41..+0x41 : u8 distinct=6 min=0 max=255 top=[(0, 96), (179, 1), (193, 1)]
- +0x42..+0x42 : u8 distinct=6 min=0 max=237 top=[(0, 96), (12, 1), (41, 1)]
- +0x43..+0x43 : u8 distinct=4 min=0 max=255 top=[(0, 98), (255, 1), (214, 1)]
- +0x44..+0x44 : u8 distinct=4 min=0 max=55 top=[(0, 97), (32, 2), (55, 1)]
- +0x45..+0x45 : u8 distinct=2 min=0 max=193 top=[(0, 100), (193, 1)]
- ... (22개 구간 더, `python -m origlib unresolved <key>`로 전체)

### 3.28 표 28 `tab28` — (미명명, 11Bx49) (11B x 49)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x00..+0x00 : u8 distinct=2 min=0 max=1 top=[(1, 30), (0, 19)]
- +0x01..+0x01 : u8 distinct=49 min=0 max=48 top=[(0, 1), (1, 1), (3, 1)]
- +0x02..+0x04 : 상수 0x00
- +0x05..+0x05 : u8 distinct=49 min=0 max=48 top=[(0, 1), (1, 1), (3, 1)]
- +0x06..+0x08 : 상수 0x00
- +0x09..+0x09 : u8 distinct=32 min=0 max=217 top=[(1, 17), (2, 2), (0, 1)]
- +0x0A..+0x0A : 상수 0x00

### 3.29 표 29 `tab29` — (미명명, 26Bx501) (26B x 501)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x00..+0x00 : u8 distinct=9 min=0 max=8 top=[(0, 357), (3, 44), (4, 22)]
- +0x01..+0x01 : u8 distinct=5 min=0 max=5 top=[(0, 358), (1, 125), (3, 6)]
- +0x02..+0x02 : u8 distinct=141 min=0 max=145 top=[(100, 357), (2, 2), (75, 2)]
- +0x03..+0x05 : 상수 0x00
- +0x06..+0x06 : u8 distinct=141 min=0 max=145 top=[(100, 357), (2, 2), (75, 2)]
- +0x07..+0x09 : 상수 0x00
- +0x0A..+0x0A : u8 distinct=141 min=0 max=145 top=[(100, 357), (2, 2), (75, 2)]
- +0x0B..+0x0D : 상수 0x00
- +0x0E..+0x0E : u8 distinct=141 min=0 max=145 top=[(100, 357), (2, 2), (75, 2)]
- +0x0F..+0x11 : 상수 0x00
- +0x12..+0x12 : u8 distinct=135 min=0 max=230 top=[(100, 357), (24, 3), (108, 3)]
- +0x13..+0x13 : 상수 0x00
- +0x14..+0x14 : u8 distinct=134 min=0 max=230 top=[(0, 357), (24, 3), (108, 3)]
- +0x15..+0x15 : 상수 0x00
- +0x16..+0x16 : u8 distinct=134 min=0 max=230 top=[(0, 357), (24, 3), (108, 3)]
- +0x17..+0x17 : 상수 0x00
- +0x18..+0x18 : u8 distinct=45 min=0 max=44 top=[(0, 358), (6, 9), (3, 9)]
- +0x19..+0x19 : 상수 0x00

### 3.32 표 32 `tab32` — (미명명, 14Bx50) (14B x 50)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x00..+0x00 : u8 distinct=32 min=0 max=234 top=[(0, 9), (89, 3), (179, 3)]
- +0x01..+0x01 : u8 distinct=30 min=0 max=181 top=[(0, 9), (50, 3), (111, 3)]
- +0x02..+0x02 : u8 distinct=28 min=0 max=250 top=[(0, 9), (233, 4), (153, 4)]
- +0x03..+0x03 : u8 distinct=29 min=0 max=183 top=[(0, 9), (58, 4), (118, 3)]
- +0x04..+0x04 : u8 distinct=40 min=0 max=249 top=[(0, 9), (249, 2), (217, 2)]
- +0x05..+0x05 : u8 distinct=32 min=0 max=187 top=[(0, 9), (54, 3), (113, 3)]
- +0x06..+0x06 : u8 distinct=23 min=0 max=254 top=[(0, 27), (37, 2), (12, 1)]
- +0x07..+0x07 : u8 distinct=23 min=0 max=186 top=[(0, 26), (121, 2), (134, 2)]
- +0x08..+0x08 : u8 distinct=3 min=0 max=203 top=[(0, 48), (203, 1), (105, 1)]
- +0x09..+0x09 : u8 distinct=3 min=0 max=185 top=[(0, 48), (165, 1), (185, 1)]
- +0x0A..+0x0A : u8 distinct=3 min=0 max=90 top=[(0, 48), (90, 1), (15, 1)]
- +0x0B..+0x0B : u8 distinct=3 min=0 max=187 top=[(0, 48), (168, 1), (187, 1)]
- +0x0C..+0x0D : 상수 0x00

### 3.35 표 35 `geo` — 지리 (138B x 18)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | w14(14B) | name | - | FRM | 확정 |
| +0x0E | w14(14B) | reading | - | FRM | 확정 |
| +0x1C | w104(104B) | desc | - | FRM | 확정 |
| +0x86 | u8(1B) | effect1 | - | FRM | 확정 |
| +0x87 | u8(1B) | effect2 | - | FRM | 확정 |

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x84..+0x84 : u8 distinct=11 min=0 max=10 top=[(2, 5), (1, 4), (0, 1)]
- +0x85..+0x85 : u8 distinct=4 min=0 max=3 top=[(2, 11), (3, 4), (1, 2)]
- +0x88..+0x88 : u8 distinct=13 min=0 max=150 top=[(20, 3), (0, 2), (50, 2)]
- +0x89..+0x89 : u8 distinct=4 min=0 max=30 top=[(0, 15), (30, 1), (20, 1)]

### 3.36 표 36 `trade_nation` — 교역국 (29B x 5)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | w12(12B) | name | - | FRM | 확정 |
| +0x0C | w12(12B) | reading | - | FRM | 확정 |
| +0x18 | u8(1B) | reward_lv1 | 획득물 Lv1 명품(128~131) | FRM | 확정 |
| +0x19 | u8(1B) | reward_lv2 | 교역특전 번호 | FRM | 확정 |
| +0x1A | u8(1B) | reward_lv3 | 교역특전 번호 | FRM | 확정 |
| +0x1B | u8(1B) | reward_lv4 | 전법서(27~30) | FRM | 확정 |
| +0x1C | u8(1B) | port | 교역항구 거점(교지31·성도44·장안20·낙양18) | FRM | 확정 |

### 3.37 표 37 `trade_perk` — 교역특전 (77B x 9)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | w38(38B) | name | - | FRM | 확정 |
| +0x26 | w38(38B) | reading | - | FRM | 확정 |
| +0x4C | u8(1B) | u4c | 142~149 미확정 | FRM | 추정 |

### 3.38 표 38 `scenic` — 명승지 (80B x 101)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | w38(38B) | name | - | MISC 1.1 | 확정 |
| +0x26 | w38(38B) | reading | - | MISC 1.1 | 확정 |
| +0x4C | u16(2B) | cell | 지도 칸 번호 | MISC 1.1 | 확정 |
| +0x4E | u8(1B) | kind | 1~8 종류/효과 번호로 보임 | MISC 1.1 | 추정 |
| +0x4F | u8(1B) | u4f | 1~20 | MISC 1.1 | 추정 |

### 3.39 표 39 `merit_reward` — 공적 보상 (4B x 7)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | u8(1B) | effect | 1지휘병사 2담당구역 3정책등급 | MISC 4 | 확정 |
| +0x01 | u16(2B) | value | - | MISC 4 | 확정 |
| +0x03 | u8(1B) | grade | - | MISC 4 | 추정 |

### 3.40 표 40 `tab40` — (미명명, 34Bx31) (34B x 31)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x00..+0x00 : u8 distinct=30 min=0 max=255 top=[(186, 2), (0, 1), (124, 1)]
- +0x01..+0x01 : u8 distinct=4 min=0 max=3 top=[(0, 11), (2, 8), (1, 7)]
- +0x02..+0x02 : u8 distinct=8 min=0 max=184 top=[(9, 8), (184, 7), (41, 6)]
- +0x03..+0x03 : u8 distinct=3 min=0 max=3 top=[(2, 18), (3, 9), (0, 4)]
- +0x04..+0x04 : u8 distinct=10 min=0 max=189 top=[(9, 9), (184, 6), (41, 6)]
- +0x05..+0x05 : u8 distinct=4 min=0 max=3 top=[(2, 19), (3, 7), (0, 4)]
- +0x06..+0x06 : u8 distinct=28 min=0 max=255 top=[(184, 2), (41, 2), (35, 2)]
- +0x07..+0x07 : u8 distinct=4 min=0 max=3 top=[(0, 11), (2, 7), (3, 7)]
- +0x08..+0x08 : u8 distinct=7 min=0 max=191 top=[(0, 8), (9, 7), (184, 6)]
- +0x09..+0x09 : u8 distinct=4 min=0 max=3 top=[(2, 15), (0, 8), (3, 7)]
- +0x0A..+0x0D : 상수 0x00
- +0x0E..+0x0E : u8 distinct=31 min=0 max=82 top=[(0, 1), (1, 1), (4, 1)]
- +0x0F..+0x11 : 상수 0x00
- +0x12..+0x12 : u8 distinct=31 min=0 max=83 top=[(0, 1), (2, 1), (5, 1)]
- +0x13..+0x15 : 상수 0x00
- +0x16..+0x16 : u8 distinct=24 min=0 max=75 top=[(0, 8), (3, 1), (8, 1)]
- +0x17..+0x21 : 상수 0x00

### 3.41 표 41 `tab41` — (미명명, 37Bx80) (37B x 80)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x00..+0x00 : u8 distinct=35 min=0 max=245 top=[(192, 8), (21, 8), (52, 7)]
- +0x01..+0x01 : u8 distinct=22 min=172 max=214 top=[(200, 10), (201, 8), (185, 8)]
- +0x02..+0x02 : u8 distinct=36 min=0 max=252 top=[(37, 18), (148, 6), (88, 6)]
- +0x03..+0x03 : u8 distinct=22 min=172 max=214 top=[(184, 18), (200, 10), (193, 8)]
- +0x04..+0x04 : u8 distinct=27 min=0 max=252 top=[(21, 37), (196, 6), (252, 6)]
- +0x05..+0x05 : u8 distinct=18 min=0 max=214 top=[(172, 44), (200, 7), (194, 5)]
- +0x06..+0x06 : u8 distinct=26 min=0 max=252 top=[(84, 37), (4, 6), (88, 6)]
- +0x07..+0x07 : u8 distinct=17 min=0 max=214 top=[(214, 38), (199, 8), (200, 7)]
- +0x08..+0x08 : u8 distinct=6 min=0 max=183 top=[(0, 36), (183, 30), (28, 6)]
- +0x09..+0x09 : u8 distinct=5 min=0 max=200 top=[(0, 65), (172, 8), (188, 5)]
- +0x0A..+0x0A : u8 distinct=11 min=0 max=149 top=[(0, 36), (41, 6), (85, 5)]
- +0x0B..+0x0B : u8 distinct=9 min=0 max=214 top=[(0, 36), (198, 10), (188, 7)]
- +0x0C..+0x0C : u8 distinct=7 min=0 max=196 top=[(0, 44), (196, 15), (112, 5)]
- +0x0D..+0x0D : u8 distinct=6 min=0 max=214 top=[(0, 44), (179, 15), (172, 6)]
- +0x0E..+0x0E : u8 distinct=2 min=0 max=84 top=[(0, 79), (84, 1)]
- +0x0F..+0x0F : u8 distinct=2 min=0 max=214 top=[(0, 79), (214, 1)]
- +0x10..+0x15 : 상수 0x00
- +0x16..+0x16 : u8 distinct=8 min=0 max=7 top=[(1, 30), (3, 9), (4, 9)]
- +0x17..+0x17 : u8 distinct=7 min=0 max=6 top=[(1, 13), (2, 13), (3, 13)]
- +0x18..+0x18 : u8 distinct=8 min=0 max=11 top=[(7, 18), (2, 12), (5, 12)]
- +0x19..+0x19 : u8 distinct=7 min=0 max=6 top=[(0, 44), (3, 6), (4, 6)]
- +0x1A..+0x1A : u8 distinct=5 min=0 max=4 top=[(0, 44), (3, 18), (1, 6)]
- +0x1B..+0x1B : u8 distinct=20 min=0 max=208 top=[(1, 38), (20, 8), (15, 5)]
- +0x1C..+0x1C : u8 distinct=3 min=0 max=39 top=[(0, 78), (7, 1), (39, 1)]
- +0x1D..+0x1D : u8 distinct=2 min=0 max=1 top=[(0, 68), (1, 12)]
- +0x1E..+0x1E : u8 distinct=80 min=0 max=79 top=[(0, 1), (1, 1), (6, 1)]
- +0x1F..+0x1F : u8 distinct=54 min=0 max=54 top=[(1, 6), (12, 3), (8, 3)]
- +0x20..+0x20 : u8 distinct=50 min=0 max=55 top=[(26, 3), (27, 3), (15, 3)]
- +0x21..+0x21 : u8 distinct=56 min=0 max=79 top=[(0, 7), (50, 3), (34, 3)]
- +0x22..+0x22 : u8 distinct=32 min=0 max=78 top=[(0, 31), (55, 4), (48, 3)]
- +0x23..+0x23 : u8 distinct=26 min=0 max=79 top=[(0, 49), (65, 2), (63, 2)]
- +0x24..+0x24 : u8 distinct=26 min=0 max=79 top=[(0, 55), (7, 1), (50, 1)]

### 3.42 표 42 `tab42` — (미명명, 35Bx7) (35B x 7)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x00..+0x00 : u8 distinct=6 min=0 max=120 top=[(17, 2), (13, 1), (109, 1)]
- +0x01..+0x01 : u8 distinct=6 min=172 max=255 top=[(201, 2), (255, 1), (213, 1)]
- +0x02..+0x02 : u8 distinct=6 min=0 max=196 top=[(40, 2), (0, 1), (165, 1)]
- +0x03..+0x03 : u8 distinct=6 min=0 max=201 top=[(184, 2), (0, 1), (199, 1)]
- +0x04..+0x0D : 상수 0x00
- +0x0E..+0x0E : u8 distinct=6 min=0 max=120 top=[(17, 2), (13, 1), (109, 1)]
- +0x0F..+0x0F : u8 distinct=6 min=172 max=255 top=[(201, 2), (255, 1), (213, 1)]
- +0x10..+0x10 : u8 distinct=6 min=0 max=196 top=[(40, 2), (0, 1), (165, 1)]
- +0x11..+0x11 : u8 distinct=6 min=0 max=201 top=[(184, 2), (0, 1), (199, 1)]
- +0x12..+0x1B : 상수 0x00
- +0x1C..+0x1C : u8 distinct=6 min=0 max=224 top=[(0, 2), (24, 1), (220, 1)]
- +0x1D..+0x1D : u8 distinct=6 min=0 max=252 top=[(0, 2), (252, 1), (5, 1)]
- +0x1E..+0x1E : u8 distinct=2 min=0 max=1 top=[(1, 4), (0, 3)]
- +0x1F..+0x1F : u8 distinct=2 min=0 max=1 top=[(0, 4), (1, 3)]
- +0x20..+0x22 : 상수 0x00

### 3.z fixdata 정정·충돌 메모

- **정정(해결, L1)**: 기존 `data/tables/terrain.json` 은 51행이었지만 지형 표(ID 8)는 **31행**이다(헤더 `(8,31)`). 뒤 20행은 시설 표 앞부분 바이트였다. `tools/extract/terrain_table.py` 가 origlib 로 31행을 다시 만들었다. 지도 칸의 지형 ID 는 1..24 뿐이라 영향 없음 (확정, 헤더).
- **정정**: 시설 표(ID 9)의 레코드 수는 31(ids 0..30)이며 이름 필드는 레코드 +0x00(10B)에 있다 (`gen_facility_tables.py` 의 FAC_NAMES 수동 표는 이 이름과 일치).
- 도시 레코드 +0x27 u8 은 슬롯 번호(0..51)와 같다 (MEAS) — FRM 에 없던 필드.

## 4. 시나리오 (0010_KO/scedaexce*.s14, CE)

API: `origlib.load_scenario(id)` -> `Scenario`(name/year/month/category/chain, `.table(키)`, `.bases()`, `.generals()`), `origlib.load_scenario(id, "general")` -> 레코드 리스트. `origlib.scenario_ids()` = 50개(1-9,12-18,21-28,30-31,34-35,55-63,71-73,100-104,150-154; 헤더 번호).

본문: `u32 ver, u32 N(=1852), u16 무장번호표 x N`, 이어서 0xE9A 부터 표 연쇄. 표 ID 는 fixdata 와 같은 번호 공간(1 도시, 2 관문, 3 세력, 4 군단, 6 지역, 10 무장, 13 명품, 22 개성 사본). 슬롯과 무장번호는 1~1000 에서만 같다 (SBM 2.3: 1001-1100=2001-2100, 1101-1300=4001-4200, 1301-1400=5001-5100, 이후 0).

시나리오 03 (군웅할거) 의 연쇄 (모든 CE 시나리오 동일 — 시험):

| ID | 키 | 개수 | stride | base | 스펙 필드 수 |
|---|---|---|---|---|---|
| 1 | city | 52 | 23 | 0xEA2 | 10 |
| 2 | gate | 11 | 20 | 0x1356 | 8 |
| 3 | force | 52 | 329 | 0x143A | 6 |
| 4 | corps | 52 | 4 | 0x5716 | 3 |
| 5 | (미스펙) | 48400 | 0 | 0x57EE | 0 |
| 6 | region | 501 | 8 | 0x57F6 | 6 |
| 7 | slot_cells | 3001 | 6 | 0x67A6 | 4 |
| 8 | (미스펙) | 31 | 0 | 0xAE04 | 0 |
| 9 | (미스펙) | 31 | 0 | 0xAE0C | 0 |
| 10 | general | 1851 | 316 | 0xAE14 | 42 |
| 11 | (미스펙) | 21 | 0 | 0x99AF0 | 0 |
| 12 | (미스펙) | 201 | 0 | 0x99AF8 | 0 |
| 13 | treasure | 202 | 65 | 0x99B00 | 8 |
| 14 | (미스펙) | 101 | 0 | 0x9CE52 | 0 |
| 15 | (미스펙) | 13 | 0 | 0x9CE5A | 0 |
| 16 | (미스펙) | 256 | 0 | 0x9CE62 | 0 |
| 17 | (미스펙) | 11 | 0 | 0x9CE6A | 0 |
| 18 | (미스펙) | 121 | 0 | 0x9CE72 | 0 |
| 19 | tab19 | 31 | 15 | 0x9CE7A | 0 |
| 20 | (미스펙) | 400 | 0 | 0x9D053 | 0 |
| 21 | (미스펙) | 2001 | 0 | 0x9D05B | 0 |
| 22 | trait_copy | 356 | 60 | 0x9D063 | 8 |
| 23 | (미스펙) | 501 | 0 | 0xA23DB | 0 |
| 24 | (미스펙) | 31 | 0 | 0xA23E3 | 0 |
| 25 | (미스펙) | 501 | 0 | 0xA23EB | 0 |
| 26 | (미스펙) | 101 | 0 | 0xA23F3 | 0 |
| 27 | (미스펙) | 501 | 0 | 0xA23FB | 0 |
| 28 | (미스펙) | 49 | 0 | 0xA2403 | 0 |
| 29 | (미스펙) | 501 | 0 | 0xA240B | 0 |
| 30 | (미스펙) | 51 | 0 | 0xA2413 | 0 |
| 31 | narration | 8 | 213 | 0xA241B | 4 |
| 32 | (미스펙) | 50 | 0 | 0xA2ACB | 0 |
| 33 | (미스펙) | 201 | 0 | 0xA2AD3 | 0 |
| 34 | (미스펙) | 31 | 0 | 0xA2ADB | 0 |
| 35 | (미스펙) | 18 | 0 | 0xA2AE3 | 0 |
| 36 | trade_state | 5 | 5 | 0xA2AEB | 0 |
| 37 | (미스펙) | 9 | 0 | 0xA2B0C | 0 |
| 38 | scenic_state | 101 | 1 | 0xA2B14 | 1 |
| 39 | (미스펙) | 7 | 0 | 0xA2B81 | 0 |
| 40 | (미스펙) | 31 | 0 | 0xA2B89 | 0 |
| 41 | (미스펙) | 80 | 0 | 0xA2B91 | 0 |
| 42 | (미스펙) | 7 | 0 | 0xA2B99 | 0 |
| 43 | tab43 | 1 | 269 | 0xA2BA1 | 0 |
| 100 | tab100 | 1 | 1741 | 0xA2CB6 | 0 |
| 101 | (미스펙) | 102 | 0 | 0xA338B | 0 |
| 104 | (미스펙) | 105 | 0 | 0xA3393 | 0 |

150~154 번은 ID 104 표가 없다(연쇄 45개). 측정: 아래 목록.

| 번호 | 파일 | 이름 | 년.월 | 분류 |
|---|---|---|---|---|
| 1 | scedaexce01.s14 | 황건의 난 | 184.2 | 1 |
| 2 | scedaexce02.s14 | 반동탁 연합 | 190.1 | 1 |
| 3 | scedaexce03.s14 | 군웅할거 | 194.6 | 1 |
| 4 | scedaexce04.s14 | 관도대전 | 200.1 | 1 |
| 5 | scedaexce05.s14 | 삼고초려 | 207.9 | 1 |
| 6 | scedaexce06.s14 | 한중쟁탈전 | 217.7 | 1 |
| 7 | scedaexce07.s14 | 출사표 | 227.2 | 1 |
| 8 | scedaexce08.s14 | 영웅집결 | 251.1 | 1 |
| 9 | scedaexce09.s14 | 동관 전투 | 211.7 | 1 |
| 12 | scedaexce12.s14 | 여포토벌전 | 198.3 | 1 |
| 13 | scedaexce13.s14 | 하북쟁란 | 202.6 | 1 |
| 14 | scedaexce14.s14 | 합비 전투 | 215.8 | 1 |
| 15 | scedaexce15.s14 | 정시정변 | 249.1 | 1 |
| 16 | scedaexce16.s14 | 성씨패란 | 251.1 | 1 |
| 17 | scedaexce17.s14 | 황천당립 | 188.8 | 1 |
| 18 | scedaexce18.s14 | 하북영웅 공손찬 | 199.7 | 1 |
| 21 | scedaexce21.s14 | 이원의 전망 | 191.10 | 1 |
| 22 | scedaexce22.s14 | 적벽대전 | 208.10 | 1 |
| 23 | scedaexce23.s14 | 관우포위망 | 219.7 | 1 |
| 24 | scedaexce24.s14 | 요동정벌 | 238.1 | 1 |
| 25 | scedaexce25.s14 | 영웅난무 | 251.1 | 1 |
| 26 | scedaexce26.s14 | 흔들리는 한조 | 188.6 | 1 |
| 27 | scedaexce27.s14 | 조조의 대두 | 196.6 | 1 |
| 28 | scedaexce28.s14 | 남만정벌 | 225.7 | 1 |
| 30 | scedaexce30.s14 | 한조의 향방 | 191.4 | 1 |
| 31 | scedaexce31.s14 | 마제와 삼영웅 | 194.4 | 1 |
| 34 | scedaexce34.s14 | 촉제 동정 | 221.5 | 1 |
| 35 | scedaexce35.s14 | 십이패란 | 251.1 | 1 |
| 55 | scedaexce55.s14 | 조가 분열 | 209.3 | 1 |
| 56 | scedaexce56.s14 | 한의 충신 | 199.11 | 1 |
| 57 | scedaexce57.s14 | 지재천리 | 209.6 | 1 |
| 58 | scedaexce58.s14 | 화북패자 원소 | 201.5 | 1 |
| 59 | scedaexce59.s14 | 추풍이 지나고 | 235.1 | 1 |
| 60 | scedaexce60.s14 | 천하이분계 | 210.11 | 1 |
| 61 | scedaexce61.s14 | 황제 여포 | 197.7 | 1 |
| 62 | scedaexce62.s14 | 금마초 비상 | 212.6 | 1 |
| 63 | scedaexce63.s14 | 영걸집결 | 251.1 | 1 |
| 71 | scedaexce71.s14 | 튜토리얼① | 190.1 | 2 |
| 72 | scedaexce72.s14 | 튜토리얼① | 191.9 | 2 |
| 73 | scedaexce73.s14 | 튜토리얼① | 196.8 | 2 |
| 100 | scedaexce100.s14 | 반동탁 연합 | 190.1 | 4 |
| 101 | scedaexce101.s14 | 관도대전 | 199.12 | 4 |
| 102 | scedaexce102.s14 | 적벽대전 | 208.9 | 4 |
| 103 | scedaexce103.s14 | 형주쟁탈전 | 218.10 | 4 |
| 104 | scedaexce104.s14 | 오장원 전투 | 233.10 | 4 |
| 150 | scedaexce150.s14 | 유비 입촉 | 211.6 | 4 |
| 151 | scedaexce151.s14 | 맹장석권 | 251.1 | 4 |
| 152 | scedaexce152.s14 | 하북평정전 | 204.8 | 4 |
| 153 | scedaexce153.s14 | 오평정전 | 279.11 | 4 |
| 154 | scedaexce154.s14 | 연주쟁탈전 | 194.4 | 4 |

### 4.1 표 1 `city` — 도시 (23B x 52)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | u16(2B) | governor | 태수 무장번호 | SBM;SCF | 확정 |
| +0x02 | u8(1B) | force | 세력(런타임 번호) | SBM;SCF | 확정 |
| +0x03 | u32(4B) | gold | - | SCF;EXT | 확정 |
| +0x07 | u32(4B) | food | - | SCF;EXT | 확정 |
| +0x0B | u32(4B) | troops | - | SCF;EXT | 확정 |
| +0x0F | u8(1B) | morale | - | SCF | 확정 |
| +0x10 | u16(2B) | durability | 내구 상한 | SCF;EXT | 확정 |
| +0x12 | u8(1B) | tactic | 거점 전법 | SCF | 확정 |
| +0x14 | u8(1B) | size | 규모 1/2/3 = 런타임 도시 +0xB8 (덤프 1940601 51/51 일치; 시나리오 03 은 내구 2000/3000/4000 과 1:1 이나 마제 시나리오는 수춘·강릉이 규모 2 / 내구 2000). 플레이 중 개발도로 자람(rules_domestic 5절 27B4B0 규칙) | MEAS;DUMP | 확정 |
| +0x15 | u8(1B) | price | 시세(전 도시 50, 추정) | MEAS | 추정 |

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x13..+0x13 : 상수 0x00
- +0x16..+0x16 : 상수 0x00

### 4.2 표 2 `gate` — 관문 (20B x 11)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | u16(2B) | governor | - | SBM | 확정 |
| +0x02 | u8(1B) | force | - | SBM | 확정 |
| +0x03 | u32(4B) | gold | 전부 0 (덤프 일치) | MEAS;DUMP | 확정 |
| +0x07 | u32(4B) | food | 전부 0 (덤프 일치) | MEAS;DUMP | 확정 |
| +0x0B | u32(4B) | troops | 1000~12000 병사 (덤프 1940601 관문 52..61 병사·금 0·군량 0 와 일치, L1) | MEAS;DUMP | 확정 |
| +0x0F | u8(1B) | morale | - | SCF | 확정 |
| +0x10 | u16(2B) | durability | 5000/6000/8000 | SCF | 확정 |
| +0x12 | u8(1B) | tactic | - | SCF | 확정 |

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x13..+0x13 : 상수 0x00

### 4.3 표 3 `force` — 세력 (329B x 52)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | u16(2B) | ruler | 군주 무장번호 | SBM;SCF | 확정 |
| +0x02 | u8x52(52B) | friendship | 세력간 우호도, 인덱스 = 세력 슬롯 0..51(자기 칸 = 100, 2601/2601 칸이 덤프 1940601 과 일치, L1) | SCF;MEAS;DUMP | 확정 |
| +0x36 | u8(1B) | title | 작위(4~9) | SCF | 추정 |
| +0x38 | u8(1B) | color | 세력색 | SCF;EXT | 확정 |
| +0x3B | u16(2B) | advisor | 군사 무장번호 | SCF;EXT | 확정 |
| +0x104 | u8x60(60B) | tactic_books | 전법서 보유(60B, 추정) | SBM 6 | 추정 |

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x37..+0x37 : 상수 0x00
- +0x39..+0x3A : 상수 0x00
- +0x3D..+0xCE : 상수 0x00
- +0xCF..+0xCF : u8 distinct=2 min=0 max=12 top=[(0, 51), (12, 1)]
- +0xD0..+0xD0 : u8 distinct=3 min=0 max=24 top=[(0, 49), (24, 2), (12, 1)]
- +0xD1..+0xD1 : u8 distinct=2 min=0 max=12 top=[(0, 51), (12, 1)]
- +0xD2..+0xD2 : u8 distinct=2 min=0 max=12 top=[(0, 51), (12, 1)]
- +0xD3..+0xD3 : u8 distinct=2 min=0 max=12 top=[(0, 51), (12, 1)]
- +0xD4..+0xD4 : 상수 0x00
- +0xD5..+0xD5 : u8 distinct=2 min=0 max=24 top=[(0, 51), (24, 1)]
- +0xD6..+0xD6 : 상수 0x00
- +0xD7..+0xD7 : u8 distinct=2 min=0 max=24 top=[(0, 51), (24, 1)]
- +0xD8..+0xDD : 상수 0x00
- +0xDE..+0xDE : u8 distinct=3 min=0 max=24 top=[(0, 50), (24, 1), (12, 1)]
- +0xDF..+0xDF : u8 distinct=2 min=0 max=12 top=[(0, 50), (12, 2)]
- +0xE0..+0xE2 : 상수 0x00
- +0xE3..+0xE3 : u8 distinct=2 min=0 max=24 top=[(0, 51), (24, 1)]
- +0xE4..+0xE4 : 상수 0x00
- +0xE5..+0xE5 : u8 distinct=2 min=0 max=12 top=[(0, 50), (12, 2)]
- +0xE6..+0xE6 : u8 distinct=2 min=0 max=12 top=[(0, 50), (12, 2)]
- +0xE7..+0xE7 : u8 distinct=2 min=0 max=12 top=[(0, 50), (12, 2)]
- +0xE8..+0x103 : 상수 0x00
- +0x140..+0x140 : u8 distinct=2 min=0 max=11 top=[(11, 51), (0, 1)]
- +0x141..+0x145 : 상수 0x00
- +0x146..+0x146 : u8 distinct=2 min=0 max=8 top=[(0, 45), (8, 7)]
- +0x147..+0x147 : u8 distinct=19 min=0 max=221 top=[(0, 32), (206, 2), (202, 2)]
- +0x148..+0x148 : u8 distinct=3 min=0 max=2 top=[(0, 44), (2, 4), (1, 4)]

### 4.4 표 4 `corps` — 군단 (4B x 52)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | u8(1B) | force | 0=빈 슬롯 | SBM | 확정 |
| +0x01 | u8(1B) | ordinal | 세력 안 순번 | SBM | 확정 |
| +0x02 | u16(2B) | governor | 도독 무장번호 | SBM | 확정 |

### 4.6 표 6 `region` — 지역 (8B x 501)

레코드는 청크 base-2 에서 시작 (이유: SBM 은 지역 1 을 0x57FC 라 적었고 측정으로 343/343 일치).

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | u16(2B) | u0 | 항상 0 (레코드는 청크 base-2에서 시작: SCENARIO_BODY_MAP의 지역1 = 0x57FC와 일치, MEAS 343/343) | SBM;MEAS | 추정 |
| +0x02 | u16(2B) | population | - | SBM;EXT | 확정 |
| +0x04 | u8(1B) | security | - | SBM;EXT | 확정 |
| +0x05 | u8(1B) | initial_force | 초기 영유 세력(마스터 ID) | SCF;EXT | 확정 |
| +0x06 | u8(1B) | flags | bit7 탐색 후보 지역, bit6 북방 변경 속성 | SCF;MISC 1.3 | 확정 |
| +0x07 | u8(1B) | u7 | 0 또는 30의 배수 | SCF | 추정 |

### 4.7 표 7 `slot_cells` — (칸 슬롯 3001x6B) (6B x 3001)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | u16(2B) | cell | 지도 칸 번호(슬롯0=0xFFFF) | MEAS | 추정 |
| +0x02 | u8(1B) | facility | 0 없음 / 1 도시(51) / 2 관문(10) | MEAS | 추정 |
| +0x03 | u8(1B) | owner | 세력 | MEAS | 추정 |
| +0x04 | u16(2B) | durability | 도시 2000/3000 (도시 표 내구와 일치) | MEAS | 추정 |

### 4.10 표 10 `general` — 무장 (316B x 1851)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | w14(14B) | family_name | 성 | SGM | 확정 |
| +0x0E | w14(14B) | given_name | 명 | SGM | 확정 |
| +0x1C | w6(6B) | courtesy | 자 | SGM | 확정 |
| +0x22 | w14(14B) | name | 표시명 | SGM;EXT | 확정 |
| +0x94 | u16(2B) | face | 모습 | SGM | 확정 |
| +0x96 | u16(2B) | id | 무장번호(슬롯 1~1000 = 번호) | SGM;EXT | 확정 |
| +0x98 | u16(2B) | spouse | - | SGM;EXT | 확정 |
| +0x9A | u16(2B) | sworn | 의형(그룹 대표) | SGM;EXT | 확정 |
| +0x9C | u8(1B) | force | - | SGM;EXT | 확정 |
| +0x9D | u8(1B) | base | 소속 도시 | SGM;EXT | 확정 |
| +0x9F | u8(1B) | location | 소재 통합 ID(0~51 도시/52~61 관문/62~ 부대) | SGM;EXT | 확정 |
| +0xA1 | u8(1B) | status | 신분 1군주 3태수 4일반 7재야 | SGM;EXT | 확정 |
| +0xA2 | u8(1B) | office | 관직 | SGM;EXT | 확정 |
| +0xA3 | u8(1B) | loyalty | 충성 | SGM;EXT | 확정 |
| +0xA6 | u8x5(5B) | stats | 통솔·무력·지력·정치·매력 | SGM;EXT | 확정 |
| +0xAB | u8x5(5B) | growth_room | = 100 - 능력 | SGM | 확정 |
| +0xB0 | u16x9(18B) | traits | 개성 번호 9칸(0=없음) | SGM;EXT | 확정 |
| +0xC2 | u32(4B) | formation_mask | 진형 비트필드 | SGM;EXT | 확정 |
| +0xC6 | u8x10(10B) | tactics | 전법 10칸 | SGM;EXT | 확정 |
| +0xD0 | u8(1B) | policy | - | SGM;EXT | 확정 |
| +0xD1 | u8(1B) | voice1 | 억양1 | SGM | 추정 |
| +0xD2 | u8(1B) | voice2 | 전용 음성 | SGM | 확정 |
| +0xD3 | u8(1B) | voice3 | - | SGM | 추정 |
| +0xD5 | u8(1B) | join_year | 임관 연도 | SGM;EXT | 확정 |
| +0xD8 | u8(1B) | gender | 0남 1여 | SGM;EXT | 확정 |
| +0xD9 | u16(2B) | appear | 등장 연도 | SGM;EXT | 확정 |
| +0xDB | u16(2B) | birth | - | SGM;EXT | 확정 |
| +0xDD | u16(2B) | death | - | SGM;EXT | 확정 |
| +0xDF | u8(1B) | death_kind | 사인(추정) | SGM | 추정 |
| +0xE0 | u16(2B) | clan | 가문 창시자 | SGM;EXT | 확정 |
| +0xE2 | u16(2B) | father | 10000+n = 가공 부친 | SGM;EXT | 확정 |
| +0xE4 | u16(2B) | mother | - | SGM;EXT | 확정 |
| +0xE6 | u8(1B) | generation | 세대 | SGM | 확정 |
| +0xE7 | u8(1B) | affinity | 상성 0~149 | SGM | 확정 |
| +0xE8 | u16x8(16B) | likes | 친애 무장 | SGM;EXT | 확정 |
| +0xF8 | u16x8(16B) | dislikes | 혐오 무장 | SGM | 확정 |
| +0x108 | u16x5(10B) | stat_caps | 능력 상한 | SGM | 확정 |
| +0x112 | u8(1B) | principle | 주의 | SGM;EXT | 확정 |
| +0x114 | i16x12(24B) | aptitude | 적성/성장 경향(-20..20) | SGM | 추정 |
| +0x12C | u8(1B) | policy_level | 정책 Lv | SGM;EXT | 확정 |
| +0x133 | u8(1B) | merit_rank | 공적 등급 0~5 | SGM;EXT | 확정 |
| +0x134 | u16(2B) | merit | 공적(100단위) | SGM;EXT | 확정 |

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x30..+0x93 : 상수 0x00
- +0x9E..+0x9E : 상수 0x00
- +0xA0..+0xA0 : 상수 0x00
- +0xA4..+0xA5 : 상수 0x00
- +0xD4..+0xD4 : 상수 0x00
- +0xD6..+0xD7 : 상수 0x00
- +0x113..+0x113 : 상수 0x00
- +0x12D..+0x131 : 상수 0x00
- +0x132..+0x132 : u8 distinct=2 min=0 max=32 top=[(0, 1751), (32, 100)]
- +0x136..+0x13B : 상수 0x00

### 4.13 표 13 `treasure` — 명품 (65B x 202)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | u16(2B) | owner | 보유 무장(0=무소속) | SCF;EXT | 확정 |
| +0x04 | u8(1B) | flag4 | 대개 1, 옥새 0 | SCF | 추정 |
| +0x05 | u8(1B) | flag5 | - | SCF | 추정 |
| +0x06 | w14(14B) | name | - | SCF;EXT | 확정 |
| +0x14 | w14(14B) | reading | - | SCF | 확정 |
| +0x3A | u8(1B) | kind | 종류(fixdata 명품 +0x0E와 같은 번호) | SCF;EXT | 확정 |
| +0x3B | u8x5(5B) | attrs | 속성 5칸(+0x3F는 능력값/가치 추정) | SCF | 추정 |
| +0x40 | u8(1B) | unique_no | 고유번호(전부 다름) | SCF | 확정 |

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x02..+0x02 : u8 distinct=64 min=0 max=247 top=[(0, 120), (130, 3), (157, 3)]
- +0x03..+0x03 : u8 distinct=2 min=0 max=1 top=[(0, 191), (1, 11)]
- +0x22..+0x39 : 상수 0x00

### 4.19 표 19 `tab19` — (미명명, 15Bx31) (15B x 31)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x00..+0x00 : u8 distinct=27 min=0 max=222 top=[(0, 5), (166, 1), (157, 1)]
- +0x01..+0x01 : u8 distinct=2 min=0 max=1 top=[(0, 26), (1, 5)]
- +0x02..+0x02 : u8 distinct=24 min=0 max=255 top=[(0, 7), (44, 2), (42, 1)]
- +0x03..+0x03 : u8 distinct=2 min=0 max=1 top=[(0, 22), (1, 9)]
- +0x04..+0x04 : u8 distinct=22 min=0 max=230 top=[(0, 10), (207, 1), (71, 1)]
- +0x05..+0x05 : u8 distinct=2 min=0 max=1 top=[(0, 29), (1, 2)]
- +0x06..+0x06 : u8 distinct=18 min=0 max=254 top=[(0, 13), (16, 2), (254, 1)]
- +0x07..+0x07 : u8 distinct=2 min=0 max=1 top=[(0, 30), (1, 1)]
- +0x08..+0x08 : u8 distinct=18 min=0 max=250 top=[(0, 14), (153, 1), (250, 1)]
- +0x09..+0x09 : u8 distinct=2 min=0 max=1 top=[(0, 29), (1, 2)]
- +0x0A..+0x0A : u8 distinct=2 min=0 max=1 top=[(1, 30), (0, 1)]
- +0x0B..+0x0B : u8 distinct=2 min=0 max=1 top=[(1, 30), (0, 1)]
- +0x0C..+0x0C : u8 distinct=2 min=0 max=1 top=[(1, 30), (0, 1)]
- +0x0D..+0x0D : u8 distinct=2 min=0 max=1 top=[(1, 30), (0, 1)]
- +0x0E..+0x0E : u8 distinct=2 min=0 max=1 top=[(1, 30), (0, 1)]

### 4.22 표 22 `trait_copy` — 개성 사본 (60B x 356)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | w12(12B) | name | - | FRM | 확정 |
| +0x0C | w32(32B) | reading | - | FRM | 확정 |
| +0x2C | u8x2(2B) | conditions | - | FRM | 확정 |
| +0x2E | i32x2(8B) | cond_values | - | FRM | 확정 |
| +0x36 | u8(1B) | effect1 | - | FRM | 확정 |
| +0x37 | i16(2B) | value1 | - | FRM | 확정 |
| +0x39 | u8(1B) | effect2 | - | FRM | 확정 |
| +0x3A | i16(2B) | value2 | - | FRM | 확정 |

### 4.31 표 31 `narration` — 오프닝 내레이션 (213B x 8)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | u8(1B) | kind | 1/2 | MEAS | 추정 |
| +0x01 | u32(4B) | a | 표시 타이밍으로 보이는 값(1950, 12800…) | MEAS | 추정 |
| +0x05 | u32(4B) | b | - | MEAS | 추정 |
| +0x09 | w204(204B) | text | 한 줄 문장(UTF-16LE) | SBM 3;MEAS | 확정 |

### 4.36 표 36 `trade_state` — (미명명, 5Bx5 = 교역국 상태) (5B x 5)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x00..+0x04 : 상수 0x00

### 4.38 표 38 `scenic_state` — 명승지 상태 (1B x 101)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | u8(1B) | state | 0/2/3 (명승지 101칸) | MEAS | 추정 |

### 4.43 표 43 `tab43` — (미명명, 269Bx1) (269B x 1)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x00..+0x03 : 상수 0x00
- +0x04..+0x04 : 상수 0x01
- +0x05..+0x0A : 상수 0x00
- +0x0B..+0x0B : 상수 0x01
- +0x0C..+0x12 : 상수 0x00
- +0x13..+0x13 : 상수 0x01
- +0x14..+0x17 : 상수 0x00
- +0x18..+0x18 : 상수 0x01
- +0x19..+0x38 : 상수 0x00
- +0x39..+0x39 : 상수 0x01
- +0x3A..+0x48 : 상수 0x00
- +0x49..+0x49 : 상수 0x01
- +0x4A..+0x58 : 상수 0x00
- +0x59..+0x59 : 상수 0x01
- +0x5A..+0x60 : 상수 0x00
- +0x61..+0x61 : 상수 0x01
- +0x62..+0x70 : 상수 0x00
- +0x71..+0x71 : 상수 0x01
- +0x72..+0x74 : 상수 0x00
- +0x75..+0x75 : 상수 0x01
- +0x76..+0x8C : 상수 0x00
- +0x8D..+0x8D : 상수 0x01
- +0x8E..+0x90 : 상수 0x00
- +0x91..+0x91 : 상수 0x01
- +0x92..+0x94 : 상수 0x00
- +0x95..+0x95 : 상수 0x01
- +0x96..+0xA4 : 상수 0x00
- +0xA5..+0xA5 : 상수 0x01
- +0xA6..+0xAC : 상수 0x00
- +0xAD..+0xAD : 상수 0x01
- +0xAE..+0xB0 : 상수 0x00
- +0xB1..+0xB1 : 상수 0x01
- +0xB2..+0xB8 : 상수 0x00
- +0xB9..+0xB9 : 상수 0x01
- +0xBA..+0xC0 : 상수 0x00
- +0xC1..+0xC1 : 상수 0x64
- +0xC2..+0xC4 : 상수 0x00
- +0xC5..+0xC5 : 상수 0x64
- +0xC6..+0xD4 : 상수 0x00
- +0xD5..+0xD5 : 상수 0x64
- +0xD6..+0xD8 : 상수 0x00
- +0xD9..+0xD9 : 상수 0x64
- +0xDA..+0xE0 : 상수 0x00
- +0xE1..+0xE1 : 상수 0x64
- +0xE2..+0xE4 : 상수 0x00
- +0xE5..+0xE5 : 상수 0x64
- +0xE6..+0xE8 : 상수 0x00
- +0xE9..+0xE9 : 상수 0x64
- ... (11개 구간 더, `python -m origlib unresolved <key>`로 전체)

### 4.100 표 100 `tab100` — (미명명, 1741Bx1) (1741B x 1)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|

미해결(스펙에 없는 바이트, 전 레코드 측정):

- +0x00..+0x00 : 상수 0x64
- +0x01..+0x07 : 상수 0x00
- +0x08..+0x08 : 상수 0x64
- +0x09..+0x0B : 상수 0x00
- +0x0C..+0x0C : 상수 0x64
- +0x0D..+0x0F : 상수 0x00
- +0x10..+0x10 : 상수 0x64
- +0x11..+0x1B : 상수 0x00
- +0x1C..+0x1C : 상수 0x64
- +0x1D..+0x1F : 상수 0x00
- +0x20..+0x20 : 상수 0x64
- +0x21..+0x23 : 상수 0x00
- +0x24..+0x24 : 상수 0x64
- +0x25..+0x27 : 상수 0x00
- +0x28..+0x28 : 상수 0x64
- +0x29..+0x2F : 상수 0x00
- +0x30..+0x30 : 상수 0x64
- +0x31..+0x37 : 상수 0x00
- +0x38..+0x38 : 상수 0x96
- +0x39..+0x3B : 상수 0x00
- +0x3C..+0x3C : 상수 0x64
- +0x3D..+0x43 : 상수 0x00
- +0x44..+0x44 : 상수 0x64
- +0x45..+0x47 : 상수 0x00
- +0x48..+0x48 : 상수 0x64
- +0x49..+0x4B : 상수 0x00
- +0x4C..+0x4C : 상수 0x64
- +0x4D..+0x4F : 상수 0x00
- +0x50..+0x50 : 상수 0x64
- +0x51..+0x53 : 상수 0x00
- +0x54..+0x54 : 상수 0x64
- +0x55..+0x57 : 상수 0x00
- +0x58..+0x58 : 상수 0x64
- +0x59..+0x5B : 상수 0x00
- +0x5C..+0x5C : 상수 0x64
- +0x5D..+0x5F : 상수 0x00
- +0x60..+0x60 : 상수 0x96
- +0x61..+0x63 : 상수 0x00
- +0x64..+0x64 : 상수 0x96
- +0x65..+0x67 : 상수 0x00
- +0x68..+0x68 : 상수 0x96
- +0x69..+0x6B : 상수 0x00
- +0x6C..+0x6C : 상수 0x64
- +0x6D..+0x6F : 상수 0x00
- +0x70..+0x70 : 상수 0x64
- +0x71..+0x73 : 상수 0x00
- +0x74..+0x74 : 상수 0x64
- +0x75..+0x7B : 상수 0x00
- ... (508개 구간 더, `python -m origlib unresolved <key>`로 전체)

- 표 5: 개수 48400 표지 (stride 0)
- 표 8: 개수 31 표지 (stride 0)
- 표 9: 개수 31 표지 (stride 0)
- 표 11: 개수 21 표지 (stride 0)
- 표 12: 개수 201 표지 (stride 0)
- 표 14: 개수 101 표지 (stride 0)
- 표 15: 개수 13 표지 (stride 0)
- 표 16: 개수 256 표지 (stride 0)
- 표 17: 개수 11 표지 (stride 0)
- 표 18: 개수 121 표지 (stride 0)
- 표 20: 개수 400 표지 (stride 0)
- 표 21: 개수 2001 표지 (stride 0)
- 표 23: 개수 501 표지 (stride 0)
- 표 24: 개수 31 표지 (stride 0)
- 표 25: 개수 501 표지 (stride 0)
- 표 26: 개수 101 표지 (stride 0)
- 표 27: 개수 501 표지 (stride 0)
- 표 28: 개수 49 표지 (stride 0)
- 표 29: 개수 501 표지 (stride 0)
- 표 30: 개수 51 표지 (stride 0)
- 표 32: 개수 50 표지 (stride 0)
- 표 33: 개수 201 표지 (stride 0)
- 표 34: 개수 31 표지 (stride 0)
- 표 35: 개수 18 표지 (stride 0)
- 표 37: 개수 9 표지 (stride 0)
- 표 39: 개수 7 표지 (stride 0)
- 표 40: 개수 31 표지 (stride 0)
- 표 41: 개수 80 표지 (stride 0)
- 표 42: 개수 7 표지 (stride 0)
- 표 101: 개수 102 표지 (stride 0)
- 표 104: 개수 105 표지 (stride 0)

### 4.z 시나리오 정정·충돌 메모

- **정정(해결, L1)**: 세력 레코드 우호도 배열은 `+0x02` 부터 **52칸**(`+0x35` 까지, 인덱스 = 세력 슬롯, 자기 칸 100)이다. 덤프 1940601 의 세력 행(`+0x14` 부터 51칸 = 런타임 `+0x13+슬롯`)과 51 x 51 = 2601 칸이 모두 일치한다. 옛 `extract.py` 는 `+0x13` 에서 읽어 17칸 밀려 있었다. 시나리오 파일의 세력 슬롯 번호와 도시·무장의 `force` 번호(= 런타임 번호 13,14,15,16..)는 다르다(슬롯 21 = 런타임 16 등): 변환은 지배자 무장의 `force` 로 슬롯을 찾는다(`extract.py`).
- **정정(해결, L1)**: 관문 레코드 +3/+7/+11 = (금, 군량, 병사) 이다. 덤프 1940601 관문 52..61 의 병사 3000/0/3000/0/0/2000/3000/2000/1000/2000 이 `+0x0B` 와 일치하고 금·군량은 둘 다 0 이다. 중립 관문의 덤프 내구는 최대의 절반(4000/8000, 2500/5000)이다(시나리오 내구는 최대값).
- **정정**: 지역 레코드 시작이 청크 base-2 (SBM 의 0x57FC) — 지역 표 한 곳만 청크 base 와 어긋남.
- **정정(해결, L1)**: 도시 규모는 도시 레코드 +0x14 = 런타임 +0xB8 이다(덤프 1940601 51/51 일치). 시나리오 03·57·8 은 내구 2000/3000/4000 과 1:1 이나 마제(31)는 수춘·강릉이 규모 2·내구 2000 이라 내구로 유도하면 틀린다. 영웅집결(8, 251년)은 전 도시 규모 1. 규모는 플레이 중 도시별로 1→2→3 으로 올라간다(덤프: 1→2 가 196~208년, 2→3 이 202~217년, 도시마다 다른 달; 조건은 rules_domestic 5절 27B4B0 규칙으로 확정). `bases[].size` 가 이 값을 담는다.
- **해결(L1)**: 기존 `data/scenarios/*.json` 은 11-04 생성, 게임 파일은 11-05 15:21 갱신이라 무장 743 의 개성 순서 한 건이 달랐다(집합은 같음). `tools/extract/extract.py` 를 origlib 호출로 바꿔 4개 시나리오를 다시 만들었다(시험 `tests/test_l1_data.py` 가 JSON = 재생성 결과를 지킨다). 개성은 9칸 중 앞 8칸만 JSON 에 둔다.
- 표 7(3001x6B)은 칸 슬롯 표로 보임: `u16 칸 번호, u8 시설(0/1 도시 51/2 관문 10), u8 세력, u16 내구` — 도시 51 + 관문 10 이 표 1·2 의 내구와 일치(추정).
- 표 31 은 오프닝 내레이션 8줄 (213B: u8 종류, u32 a, u32 b, 204B 문장 UTF-16LE). 시험 `Scn` 에 문장 확인 없음, CLI 로 `scenario 2 narration` 확인.

## 6. 문자열 상세

컨테이너 `zp1`: `u32 magic 'zp1\0', u32 total_raw, u32 chunk_size, u32 nchunks, u32 sizes[nchunks]`, 0x800 부터 청크마다 `u32 (n-4) + zlib` (128B 정렬). 근거: `AI_TacticsMod/research/ui_atlas/read_messages.py`(검증) + origlib 재구현.

### 6.msgdata (892408 바이트)

바깥 구간 표의 유일한 항목 안에 구간 표와 XL 블록 4개가 있다. XL 블록은 `+0x00 'XL', +0x02 u16 버전 0x13, +0x08 u16 행 수, +0x0A u16 행 간격 4, +0x0C u32 열 수 1, +0x10 u32 표 시작(이 설치본은 0x18), +0x14 열 종류 0`이다. 각 행의 u32 오프셋을 표 시작에 더하면 해당 NUL 종결 UTF-16LE 문자열의 위치가 된다(`3E5E00/3E5F00`).

블록별 행 수는 5414/3000/500/8000이다.

로더 `30C0B0`은 한국어 `msgdata_exce.bin`을 초기화한다. `30F010`은 블록 1의 0..2999를 UI 이름으로 읽는다. 따라서 원작 버튼 키 `0x5FA`는 `origlib.msg(10000 + 0x5FA, 'msgdata_exce')`에서 「관문정보」다. origlib에서는 구간×10000+번호로 조회한다. CE 블록 3의 마지막 11개(10000..10010번)는 origlib ID 40000..40010이다.

### 6.msgdata_exce (1025860 바이트)

바깥 구간 표의 유일한 항목 안에 구간 표와 XL 블록 4개가 있다. XL 블록은 `+0x00 'XL', +0x02 u16 버전 0x13, +0x08 u16 행 수, +0x0A u16 행 간격 4, +0x0C u32 열 수 1, +0x10 u32 표 시작(이 설치본은 0x18), +0x14 열 종류 0`이다. 각 행의 u32 오프셋을 표 시작에 더하면 해당 NUL 종결 UTF-16LE 문자열의 위치가 된다(`3E5E00/3E5F00`).

블록별 행 수는 6153/3000/500/10011이다.

로더 `30C0B0`은 한국어 `msgdata_exce.bin`을 초기화한다. `30F010`은 블록 1의 0..2999를 UI 이름으로 읽는다. 따라서 원작 버튼 키 `0x5FA`는 `origlib.msg(10000 + 0x5FA, 'msgdata_exce')`에서 「관문정보」다. origlib에서는 구간×10000+번호로 조회한다. CE 블록 3의 마지막 11개(10000..10010번)는 origlib ID 40000..40010이다.

### 6.msggame (2153128 바이트, 구간 10)

구간 구조: `u32 nsec, nsec x (u32 offset, u32 size)`, 구간 = `u32 count, u32 오프셋[count], 본문`. 메시지 id = 구간 x 10000 + 번호 (UI 관례; EXE 조회 코드 확인은 아님 -> 추정). 본문 텍스트는 `07 07 01 <UTF-16LE> 07 07 02` 구간들, 그 밖의 바이트는 색·줄 제어 코드(`^02`=이름색 등은 UTF-16 텍스트 안).

| 구간 | 개수 | 예시 |
|---|---|---|
| 0 | 1590 | , 선양을 받고 국호  제정 |
| 1 | 3210 | 메뉴를 선택해주십시오. |
| 2 | 3973 | 의 상업을 끌어올리고 싶은데 의 자금을 주시지 않겠수？ |
| 3 | 4872 | 무장봉기한 ^05황건적^00이 각지의 관군을 차례로 격 |
| 4 | 1813 | 국력 향상의 기본 |
| 5 | 1544 | , 화계 성공 후  |
| 6 | 1 |  |
| 7 | 828 | 전기제패 모드에서는 실행불가 |
| 8 | 1 |  |
| 9 | 1 |  |

### 6.msggame_exce (2746104 바이트, 구간 10)

구간 구조: `u32 nsec, nsec x (u32 offset, u32 size)`, 구간 = `u32 count, u32 오프셋[count], 본문`. 메시지 id = 구간 x 10000 + 번호 (UI 관례; EXE 조회 코드 확인은 아님 -> 추정). 본문 텍스트는 `07 07 01 <UTF-16LE> 07 07 02` 구간들, 그 밖의 바이트는 색·줄 제어 코드(`^02`=이름색 등은 UTF-16 텍스트 안).

| 구간 | 개수 | 예시 |
|---|---|---|
| 0 | 1631 | , 선양을 받고 국호  제정 |
| 1 | 3579 | 메뉴를 선택해주십시오. |
| 2 | 4453 | 의 상업을 끌어올리고 싶은데 의 자금을 주시지 않겠수？ |
| 3 | 7655 | 무장봉기한 ^05황건적^00이 각지의 관군을 차례로 격 |
| 4 | 2785 | 국력 향상의 기본 |
| 5 | 1591 | , 화계 성공 후  |
| 6 | 1 |  |
| 7 | 828 | 전기제패 모드에서는 실행불가 |
| 8 | 1 |  |
| 9 | 1 |  |


## 7. 지도 (0000/Map.bin, MapExCe.bin)

```
0000/Map.bin (base) and 0000/MapExCe.bin (CE): the 220 x 220 map cell table.

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
```

측정: MapExCe 와 Map 은 지형(+4)·지역(+6) 칸이 일부 다르다(CE 가 편집). 지형 종류 24(Map 23), 지역 번호 0..343. 칸 번호 <-> (x,y) = (i%220, i//220) (헥스 배치 방식은 지도 문서 worldmap_spec 참조).

지형 id 분포(MapExCe): 1:4847, 2:1756, 3:3770, 4:2151, 5:2383, 6:767, 7:383, 8:3851, 9:4076, 10:4871, 11:494, 12:33, 13:755, 14:4679, 15:242, 16:357, 17:42, 18:40, 19:4188, 20:311, 21:102, 22:583, 23:7309, 24:410

## 8. 0000 폴더의 나머지

### 8.1 구간 컨테이너 파일

- `ccscore_data.bin`: 구간 0: 100개 x 120B, 구간 1: 100개 x 48B
- `change_force_data.bin`: 구간 0: 196개 x 12B
- `opcamera_data.bin`: 구간 0: 52개 x 20B
- `param_s.bin`: 구간 0: 1개 x 1612B
- `experience_data.bin`: 구간 0: 11개 x 10B, 구간 1: 101개 x 24B
- `experience_data_exce.bin`: 구간 0: 11개 x 10B, 구간 1: 101개 x 24B, 구간 2: 7개 x 15B, 구간 3: 16개 x 6B

#### ccscore_data 구간 0 (100 x 120B)

- +0x00..+0x00 : u8 distinct=6 min=0 max=200 top=[(0, 91), (150, 4), (50, 2)]
- +0x01..+0x01 : u8 distinct=2 min=0 max=1 top=[(0, 99), (1, 1)]
- +0x02..+0x03 : 상수 0x00
- +0x04..+0x04 : u8 distinct=5 min=0 max=250 top=[(0, 91), (100, 4), (250, 2)]
- +0x05..+0x07 : 상수 0x00
- +0x08..+0x08 : u8 distinct=5 min=0 max=250 top=[(0, 91), (100, 3), (200, 2)]
- +0x09..+0x0B : 상수 0x00
- +0x0C..+0x0C : u8 distinct=6 min=0 max=200 top=[(0, 91), (50, 3), (150, 2)]
- +0x0D..+0x0D : u8 distinct=2 min=0 max=1 top=[(0, 99), (1, 1)]
- +0x0E..+0x0F : 상수 0x00
- +0x10..+0x10 : u8 distinct=6 min=0 max=250 top=[(0, 92), (100, 3), (50, 2)]
- +0x11..+0x13 : 상수 0x00
- +0x14..+0x14 : u8 distinct=5 min=0 max=250 top=[(0, 93), (250, 2), (150, 2)]
- +0x15..+0x17 : 상수 0x00
- +0x18..+0x18 : u8 distinct=4 min=0 max=150 top=[(0, 94), (100, 3), (150, 2)]
- +0x19..+0x19 : u8 distinct=2 min=0 max=1 top=[(0, 99), (1, 1)]
- +0x1A..+0x1B : 상수 0x00
- +0x1C..+0x1C : u8 distinct=4 min=0 max=200 top=[(0, 97), (100, 1), (50, 1)]
- +0x1D..+0x1F : 상수 0x00
- +0x20..+0x20 : u8 distinct=2 min=0 max=150 top=[(0, 99), (150, 1)]
- +0x21..+0x23 : 상수 0x00
- +0x24..+0x24 : u8 distinct=2 min=0 max=150 top=[(0, 99), (150, 1)]
- +0x25..+0x27 : 상수 0x00
- +0x28..+0x28 : u8 distinct=6 min=0 max=200 top=[(0, 91), (100, 2), (50, 2)]

#### ccscore_data 구간 1 (100 x 48B)

- +0x00..+0x00 : u8 distinct=2 min=0 max=16 top=[(0, 90), (16, 10)]
- +0x01..+0x01 : u8 distinct=2 min=0 max=39 top=[(0, 90), (39, 10)]
- +0x02..+0x03 : 상수 0x00
- +0x04..+0x04 : u8 distinct=2 min=0 max=64 top=[(0, 90), (64, 10)]
- +0x05..+0x05 : u8 distinct=2 min=0 max=31 top=[(0, 90), (31, 10)]
- +0x06..+0x07 : 상수 0x00
- +0x08..+0x08 : u8 distinct=2 min=0 max=112 top=[(0, 90), (112, 10)]
- +0x09..+0x09 : u8 distinct=2 min=0 max=23 top=[(0, 90), (23, 10)]
- +0x0A..+0x0B : 상수 0x00
- +0x0C..+0x0C : u8 distinct=2 min=0 max=148 top=[(0, 90), (148, 10)]
- +0x0D..+0x0D : u8 distinct=2 min=0 max=17 top=[(0, 90), (17, 10)]
- +0x0E..+0x0F : 상수 0x00
- +0x10..+0x10 : u8 distinct=2 min=0 max=16 top=[(0, 90), (16, 10)]
- +0x11..+0x11 : u8 distinct=2 min=0 max=39 top=[(0, 90), (39, 10)]
- +0x12..+0x13 : 상수 0x00
- +0x14..+0x14 : u8 distinct=2 min=0 max=64 top=[(0, 90), (64, 10)]
- +0x15..+0x15 : u8 distinct=2 min=0 max=31 top=[(0, 90), (31, 10)]
- +0x16..+0x17 : 상수 0x00
- +0x18..+0x18 : u8 distinct=2 min=0 max=112 top=[(0, 90), (112, 10)]
- +0x19..+0x19 : u8 distinct=2 min=0 max=23 top=[(0, 90), (23, 10)]
- +0x1A..+0x1B : 상수 0x00
- +0x1C..+0x1C : u8 distinct=2 min=0 max=148 top=[(0, 90), (148, 10)]
- +0x1D..+0x1D : u8 distinct=2 min=0 max=17 top=[(0, 90), (17, 10)]
- +0x1E..+0x1F : 상수 0x00

#### change_force_data 구간 0 (196 x 12B)

- +0x00..+0x00 : u8 distinct=40 min=7 max=254 top=[(244, 149), (253, 3), (35, 2)]
- +0x01..+0x01 : u8 distinct=2 min=0 max=1 top=[(1, 154), (0, 42)]
- +0x02..+0x03 : 상수 0x00
- +0x04..+0x04 : u8 distinct=26 min=0 max=40 top=[(0, 149), (6, 6), (35, 4)]
- +0x05..+0x07 : 상수 0x00
- +0x08..+0x08 : u8 distinct=22 min=0 max=37 top=[(0, 149), (25, 4), (35, 4)]
- +0x09..+0x0B : 상수 0x00

#### opcamera_data 구간 0 (52 x 20B)

- +0x00..+0x00 : u8 distinct=52 min=0 max=51 top=[(0, 1), (1, 1), (2, 1)]
- +0x01..+0x03 : 상수 0x00
- +0x04..+0x04 : u8 distinct=38 min=0 max=224 top=[(0, 7), (32, 3), (93, 2)]
- +0x05..+0x05 : u8 distinct=39 min=0 max=247 top=[(0, 6), (71, 3), (206, 2)]
- +0x06..+0x06 : u8 distinct=3 min=0 max=2 top=[(2, 20), (1, 20), (0, 12)]
- +0x07..+0x07 : 상수 0x00
- +0x08..+0x08 : u8 distinct=37 min=0 max=248 top=[(0, 8), (172, 2), (24, 2)]
- +0x09..+0x09 : u8 distinct=40 min=0 max=253 top=[(0, 6), (125, 2), (191, 2)]
- +0x0A..+0x0A : u8 distinct=3 min=0 max=2 top=[(1, 20), (0, 16), (2, 16)]
- +0x0B..+0x0B : 상수 0x00
- +0x0C..+0x0C : u8 distinct=44 min=0 max=255 top=[(0, 7), (163, 2), (173, 2)]
- +0x0D..+0x0D : u8 distinct=42 min=0 max=240 top=[(0, 6), (175, 2), (40, 2)]
- +0x0E..+0x0E : u8 distinct=3 min=0 max=2 top=[(1, 23), (2, 18), (0, 11)]
- +0x0F..+0x0F : 상수 0x00
- +0x10..+0x10 : u8 distinct=43 min=0 max=255 top=[(0, 6), (162, 2), (65, 2)]
- +0x11..+0x11 : u8 distinct=44 min=0 max=250 top=[(0, 6), (77, 2), (33, 2)]
- +0x12..+0x12 : u8 distinct=3 min=0 max=2 top=[(1, 22), (0, 18), (2, 12)]
- +0x13..+0x13 : 상수 0x00

#### param_s 구간 0 (1 x 1612B)

- +0x00..+0x00 : 상수 0x04
- +0x01..+0x02 : 상수 0x00
- +0x03..+0x03 : 상수 0x40
- +0x04..+0x04 : 상수 0x03
- +0x05..+0x06 : 상수 0x00
- +0x07..+0x07 : 상수 0x40
- +0x08..+0x0A : 상수 0x00
- +0x0B..+0x0B : 상수 0x20
- +0x0C..+0x0F : 상수 0x00
- +0x10..+0x10 : 상수 0x01
- +0x11..+0x12 : 상수 0x00
- +0x13..+0x13 : 상수 0x40
- +0x14..+0x14 : 상수 0x64
- +0x15..+0x1A : 상수 0x00
- +0x1B..+0x1B : 상수 0x20
- +0x1C..+0x1C : 상수 0x01
- +0x1D..+0x1F : 상수 0x00
- +0x20..+0x20 : 상수 0x64
- +0x21..+0x23 : 상수 0x00
- +0x24..+0x24 : 상수 0x14
- +0x25..+0x26 : 상수 0x00
- +0x27..+0x27 : 상수 0x40
- +0x28..+0x28 : 상수 0x02
- +0x29..+0x2B : 상수 0x00

#### experience_data 구간 0 (11 x 10B)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | u32(4B) | level | - | MISC | 확정 |
| +0x04 | u32(4B) | need_exp | - | MISC | 추정 |
| +0x08 | u8(1B) | a | - | MISC | 추정 |
| +0x09 | u8(1B) | b | - | MISC | 추정 |

#### experience_data 구간 1 (101 x 24B)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | u32(4B) | value | 능력치 값 | MISC | 확정 |
| +0x04 | u32x5(20B) | exp | 그 값에 필요한 누적 경험치(통·무·지·정·매) | MISC | 확정 |

#### experience_data_exce 구간 0 (11 x 10B)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | u32(4B) | level | - | MISC | 확정 |
| +0x04 | u32(4B) | need_exp | - | MISC | 추정 |
| +0x08 | u8(1B) | a | - | MISC | 추정 |
| +0x09 | u8(1B) | b | - | MISC | 추정 |

#### experience_data_exce 구간 1 (101 x 24B)

| 오프셋 | 폭 | 필드 | 뜻 | 근거 | 확신도 |
|---|---|---|---|---|---|
| +0x00 | u32(4B) | value | 능력치 값 | MISC | 확정 |
| +0x04 | u32x5(20B) | exp | 그 값에 필요한 누적 경험치(통·무·지·정·매) | MISC | 확정 |

#### experience_data_exce 구간 2 (7 x 15B)

- +0x00..+0x00 : u8 distinct=7 min=0 max=6 top=[(0, 1), (1, 1), (2, 1)]
- +0x01..+0x03 : 상수 0x00
- +0x04..+0x04 : u8 distinct=6 min=0 max=240 top=[(0, 2), (60, 1), (90, 1)]
- +0x05..+0x05 : u8 distinct=6 min=0 max=148 top=[(0, 2), (8, 1), (140, 1)]
- +0x06..+0x06 : u8 distinct=6 min=0 max=21 top=[(0, 2), (7, 1), (10, 1)]
- +0x07..+0x07 : u8 distinct=4 min=0 max=5 top=[(0, 2), (3, 2), (5, 2)]
- +0x08..+0x08 : u8 distinct=6 min=0 max=160 top=[(0, 2), (40, 1), (60, 1)]
- +0x09..+0x09 : u8 distinct=6 min=0 max=184 top=[(0, 2), (176, 1), (8, 1)]
- +0x0A..+0x0A : u8 distinct=6 min=0 max=14 top=[(0, 2), (4, 1), (7, 1)]
- +0x0B..+0x0B : u8 distinct=4 min=0 max=4 top=[(0, 2), (2, 2), (4, 2)]
- +0x0C..+0x0C : u8 distinct=6 min=0 max=192 top=[(0, 2), (96, 1), (16, 1)]
- +0x0D..+0x0D : u8 distinct=6 min=0 max=28 top=[(0, 2), (9, 1), (14, 1)]
- +0x0E..+0x0E : u8 distinct=4 min=0 max=6 top=[(0, 2), (4, 2), (6, 2)]

#### experience_data_exce 구간 3 (16 x 6B)

- +0x00..+0x00 : u8 distinct=16 min=0 max=15 top=[(0, 1), (1, 1), (2, 1)]
- +0x01..+0x03 : 상수 0x00
- +0x04..+0x04 : u8 distinct=5 min=0 max=50 top=[(0, 6), (10, 3), (30, 3)]
- +0x05..+0x05 : u8 distinct=5 min=0 max=20 top=[(0, 6), (5, 3), (10, 3)]

경험치 구간(MISC 3): 구간 0 = 레벨 표 11행, 구간 1 = 능력치값 1..100 별 누적 경험치(통무지정 같은 값, 매력 다름), exce 의 구간 2(7x15B)·3(16x6B)은 미해독.

### 8.2 행동 트리 (bt.bin / bt_exce.bin)

'JBTP' u32 ver=2 u32 4 u32 0 then 4 x (offset,size,hash) (contiguous, MEAS) ; each section holds one KTBT tree;
  node format: REA_Analysis/1022_REA_분석_전체합본.md section 6 (re-implemented and node counts re-verified: bt_exce 10312+246+348+111).

측정: bt_exce.bin 구간(offset,size,hash) = [(64, 10378, 2093567770), (10442, 443346, 1918962887), (453788, 15076, 2623249025), (468864, 4604, 4218001847)], 노드 수 = [246, 10790, 348, 111]; bt.bin 노드 수 = [211, 6781, 348, 55].
REA 합본 6절(10-22 시점)의 노드 수는 10312/246/348/111 이었고 현재 bt_exce.bin(11-05 15:21 갱신)은 구간 순서 246/10790/348/111 이다(주 트리 +478 노드, 갱신). 조건 번호표·노드 의미는 K2 문서(원작 AI) 담당.

### 8.3 effect_info / se_info

effect_info.bin 548B = 4B x 137 (바이트 4개 레코드, 의미 미해결: 값 분포) ; se_info.bin(215B)·se_info_exce.bin(220B) 는 전부 0 (미사용, MEAS).
- effect_info 바이트 0: distinct=4 [(1, 60), (2, 31), (6, 27), (5, 19)]
- effect_info 바이트 1: distinct=5 [(6, 52), (3, 50), (4, 28), (2, 6), (1, 1)]
- effect_info 바이트 2: distinct=1 [(1, 137)]
- effect_info 바이트 3: distinct=2 [(0, 135), (1, 2)]

## 9. 이벤트 스크립트 (0004)

```
0004/Event*.s14, CCEvent*.s14, EventPKCE001.s14, EventTutorial(PKCE).s14: event scripts (uncompressed, little endian).

File layout (19 installed scripts measured). The current-build opcode dispatch is indexed in docs/orig/event_opcodes.json.
Argument layouts are per opcode. Speech opcode 95 is confirmed by text lookup:
  0x00 u32 version=3, u32 5, u32 9, u32 4, u32 14, u32 0 x3, u32 1 (@0x20), u32 0 x3, u32 N events (@0x30), u32 0 x3
  0x40 u32 offsets[1 + 2N + 2]:  [0] = offset of table A, [1..N] = offset of each event's condition list,
       [N+1..2N] = offset of each event's action list, then two trailing u32 (0, and the file end - 4 / 100)
  table A: N x 68 bytes: u32 event_id, 0, 0, u32 999, 0, 0, 1, 1, then u32 actors[5] (general ids, 1000 = placeholder), rest 0
  condition list (variable): k x 44-byte records of 11 x i32 = [event_index, 0, cond_code, a1..a8]; the first record of every event
       is the placeholder [idx,0,0,1,2,3,4,-1,-2,-3,-4] (44 B lists with only the placeholder = event without extra condition)
  action list  (variable): k x 44-byte records of 11 x i32 = [event_index, 0, op_code, a1..a8]
  op 95 = speech line: a1 = speaker general id, a2 = message id (section*10000 + index in msggame / msggame_exce), a4 = listener
  text table: files with 'PKCE' in the name use 0001_KO/msggame_exce.bin, the others use msggame.bin
EventSample{Ko,..}.s14: separate editor-sample catalog (u32 1 + UTF-16 titles/descriptions + binary), not event scripts (language files other than Ko ignored).
```

| 파일 | 이벤트 수 | 조건 레코드 | 행동 레코드 | 텍스트 표 |
|---|---|---|---|---|
| CCEvent050.s14 | 956 | 1147 | 1625 | msggame |
| CCEvent051.s14 | 956 | 1020 | 1386 | msggame |
| CCEvent052.s14 | 956 | 1150 | 1578 | msggame |
| CCEvent053.s14 | 956 | 1208 | 1612 | msggame |
| CCEvent054.s14 | 956 | 1103 | 1859 | msggame |
| CCEventPKCE000.s14 | 956 | 1080 | 1568 | msggame_exce |
| CCEventPKCE001.s14 | 956 | 1098 | 1671 | msggame_exce |
| CCEventPKCE002.s14 | 956 | 1176 | 1618 | msggame_exce |
| CCEventPKCE003.s14 | 956 | 1140 | 1532 | msggame_exce |
| CCEventPKCE004.s14 | 956 | 1030 | 1243 | msggame_exce |
| CCEventPKCE050.s14 | 956 | 1147 | 1625 | msggame_exce |
| CCEventPKCE051.s14 | 956 | 1020 | 1386 | msggame_exce |
| CCEventPKCE052.s14 | 956 | 1150 | 1578 | msggame_exce |
| CCEventPKCE053.s14 | 956 | 1208 | 1612 | msggame_exce |
| CCEventPKCE054.s14 | 956 | 1103 | 1859 | msggame_exce |
| Event001.s14 | 962 | 3219 | 27972 | msggame |
| EventPKCE001.s14 | 962 | 5713 | 57839 | msggame_exce |
| EventTutorial.s14 | 78 | 78 | 517 | msggame |
| EventTutorialPKCE.s14 | 155 | 155 | 1078 | msggame_exce |

### 9.4 opcode 통계 (Event001 + EventPKCE001 합산; (종류, 코드) -> 레코드 수, 쓰는 이벤트 수, 인수1..8 의 (distinct,min,max))

현재판 실행·설명 함수와 RTTI 클래스는 [이벤트 코드 색인](event_opcodes.json)에 454개 전수 매핑했다. [날짜 6.1절](rules_time.md)에서 스크립트 대조 및 실행 호출을 확인할 수 있다. 아래 표는 두 파일의 인수 분포이며 각 명령 인수의 뜻은 실행 함수에서 확인한다.

| 종류 | 코드 | 레코드 | 이벤트 | 인수1 | 인수2 | 인수3 | 인수4 | 인수5 | 인수6 | 인수7 | 인수8 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| act | 0 | 1078 | 1053 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 1 | 3399 | 736 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 2 | 3399 | 736 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 3 | 1655 | 662 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 4 | 3399 | 736 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 5 | 115 | 38 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 6 | 115 | 38 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 7 | 292 | 51 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 8 | 292 | 51 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 9 | 44 | 20 | 16/23/551 | 2/0/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 13 | 5 | 5 | 2/2/4 | 3/187/212 | 3/6/12 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 16 | 6 | 4 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 17 | 2 | 2 | 1/2/2 | 1/5003/5003 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 18 | 24 | 7 | 2/1/2 | 2/-1/132 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 20 | 22 | 14 | 9/-5/724 | 2/2/4 | 5/1/45 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 22 | 1 | 1 | 1/266/266 | 1/2/2 | 1/1/1 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 24 | 22 | 8 | 5/-1/925 | 4/1/5 | 8/1/8 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 25 | 32 | 27 | 12/-5/987 | 2/0/1 | 15/-5/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 26 | 58 | 38 | 11/-5/987 | 19/-10/4101 | 4/3/6 | 6/1/6 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 27 | 1 | 1 | 1/266/266 | 1/1/1 | 1/932/932 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 28 | 4 | 2 | 1/-1/-1 | 2/2/4 | 2/1/2 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 30 | 32 | 8 | 2/-5/945 | 2/1/3 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 31 | 240 | 28 | 1/-1/-1 | 6/1/6 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 33 | 26 | 4 | 3/3/770 | 2/521/769 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 34 | 40 | 35 | 3/521/952 | 2/1/2 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 35 | 2 | 2 | 1/553/553 | 1/379/379 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 36 | 31 | 9 | 2/1/2 | 5/-5/521 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 38 | 3 | 1 | 1/35/35 | 1/4/4 | 1/1/1 | 3/1/3 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 43 | 60 | 8 | 1/-1/-1 | 5/1/5 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 46 | 2 | 2 | 1/521/553 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 47 | 4 | 2 | 1/-5/-5 | 1/2/2 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 49 | 598 | 52 | 26/-4/61 | 2/1/2 | 30/-10/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 50 | 273 | 63 | 42/-3/46 | 2/1/2 | 28/-5/963 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 56 | 1369 | 222 | 276/-17/1000 | 2/1/2 | 46/-10/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 57 | 20 | 13 | 11/147/953 | 2/1/2 | 10/6/45 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 59 | 267 | 58 | 127/1/996 | 8/1/9 | 7/0/9 | 4/0/4 | 4/0/6 | 3/0/8 | 1/0/0 | 1/0/0 |
| act | 60 | 1 | 1 | 1/596/596 | 1/0/0 | 1/266/266 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 61 | 6 | 6 | 3/379/793 | 1/5/5 | 2/100/150 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 62 | 26 | 8 | 14/193/953 | 1/0/0 | 7/32/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 64 | 1104 | 184 | 237/1/1000 | 7/0/953 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 66 | 2 | 2 | 1/952/952 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 68 | 4 | 3 | 2/1/69 | 2/440/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 69 | 22 | 12 | 5/249/792 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 70 | 20 | 2 | 1/169/169 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 71 | 25 | 2 | 15/72/856 | 2/344/440 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 74 | 2 | 2 | 1/34/34 | 1/1/1 | 1/8/8 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 75 | 24 | 10 | 4/-14/997 | 4/1/5 | 2/4/5 | 8/42/92 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 76 | 34 | 15 | 3/2/6 | 3/0/2 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 80 | 42 | 17 | 4/2/5 | 3/1/3 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 81 | 79 | 10 | 18/80/973 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 82 | 938 | 658 | 54/-4/51 | 1/-1/-1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 83 | 136 | 136 | 23/-10/987 | 1/-1/-1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 84 | 32 | 30 | 14/80/5003 | 1/-1/-1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 85 | 2293 | 864 | 39/0/47 | 2/0/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 86 | 15 | 15 | 6/1/6 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 87 | 2220 | 644 | 63/0/78 | 2/0/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 88 | 88 | 36 | 6/0/7 | 2/0/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 89 | 12 | 6 | 4/0/124 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 91 | 1690 | 854 | 18/0/23 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 92 | 1968 | 689 | 77/0/94 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 93 | 45 | 33 | 10/-5/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 94 | 2240 | 777 | 1/1/1 | 1146/30001/37649 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 95 | 39 | 20 | 13/-14/5032 | 20/30030/37600 | 2/0/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 96 | 11439 | 864 | 275/-17/5035 | 5889/30003/37653 | 2/0/1 | 1/0/0 | 2/0/952 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 97 | 438 | 178 | 26/-17/5072 | 195/30331/37449 | 2/0/1 | 30/34586/34618 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 98 | 992 | 270 | 33/-5/4181 | 29/-5/4181 | 4/0/952 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 99 | 1178 | 390 | 50/-4/46 | 13/-3/38 | 4/0/37 | 2/0/36 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 100 | 61 | 31 | 18/12/322 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 101 | 11972 | 875 | 279/-17/5072 | 214/-15/5071 | 189/-14/5011 | 131/-14/5004 | 71/-14/5003 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 102 | 52 | 24 | 18/1/149 | 2/0/88 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 103 | 246 | 105 | 20/15/20000 | 2/0/50000 | 2/0/30000 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 104 | 323 | 185 | 2/0/1 | 6/0/7 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 106 | 4203 | 859 | 202/-17/5071 | 171/-16/5071 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 107 | 1575 | 312 | 87/-15/5072 | 153/-17/5035 | 86/-16/5071 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 108 | 2 | 2 | 1/1/1 | 1/5014/5014 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 109 | 224 | 85 | 8/0/12 | 5/0/5 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 110 | 2187 | 693 | 4/-1/800 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 111 | 789 | 559 | 3/-1/600 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 112 | 4 | 4 | 2/5002/5003 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 113 | 5 | 5 | 3/16/20 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 114 | 6 | 6 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 115 | 39 | 20 | 16/-14/987 | 6/-3/46 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 116 | 17 | 17 | 12/-10/963 | 8/0/932 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 117 | 39 | 26 | 24/-10/987 | 8/35/952 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 118 | 18 | 16 | 9/35/953 | 12/-13/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 119 | 6 | 6 | 4/553/987 | 4/92/997 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 120 | 76 | 57 | 12/-5/963 | 8/1/8 | 5/0/5 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 121 | 64 | 64 | 5/-1/952 | 2/1000/2000 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 122 | 196 | 136 | 24/-5/987 | 14/-50/100 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 123 | 159 | 96 | 21/-5/987 | 33/-10/4101 | 10/0/100 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 124 | 16 | 11 | 5/-5/952 | 5/-4/952 | 4/-30/50 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 125 | 30 | 20 | 9/-5/987 | 14/-5/987 | 6/3/24 | 2/0/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 126 | 24 | 22 | 11/-5/987 | 11/32/952 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 127 | 12 | 8 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 128 | 12 | 8 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 129 | 12 | 8 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 130 | 12 | 8 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 131 | 12 | 8 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 132 | 43 | 19 | 22/-14/963 | 2/1/2 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 133 | 28 | 24 | 13/-9/987 | 15/-4/36 | 6/0/35 | 4/0/37 | 2/0/14 | 2/0/22 | 1/0/0 | 1/0/0 |
| act | 134 | 30 | 20 | 10/-9/987 | 8/-9/33 | 4/0/35 | 4/0/36 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 135 | 3 | 3 | 2/-5/521 | 2/53/114 | 2/518/751 | 2/-2/0 | 1/0/0 | 1/0/0 | 1/0/0 | 2/1/4 |
| act | 137 | 2 | 2 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 138 | 2 | 2 | 1/-30/-30 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 141 | 2 | 2 | 1/12/12 | 1/5/5 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 142 | 49 | 45 | 8/-9/45 | 6/2000/20000 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 143 | 66 | 50 | 22/-9/45 | 6/10000/50000 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 144 | 106 | 65 | 25/-9/45 | 8/2000/30000 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 145 | 7 | 7 | 4/2/18 | 3/0/2000 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 146 | 9 | 7 | 3/10/18 | 3/9/20 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 147 | 9 | 7 | 3/10/18 | 3/9/20 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 148 | 11 | 7 | 4/10/53 | 3/9/20 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 149 | 448 | 63 | 30/-4/61 | 14/0/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 150 | 5 | 5 | 2/10/18 | 2/9/20 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 151 | 2 | 2 | 1/18/18 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 152 | 278 | 278 | 46/1/46 | 4/1/4 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 153 | 217 | 89 | 128/16/4200 | 18/-10/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 154 | 150 | 55 | 28/-4/52 | 75/-14/1000 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 155 | 379 | 55 | 21/-4/61 | 22/-9/46 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 156 | 72 | 33 | 41/16/952 | 15/-8/963 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 159 | 16 | 2 | 2/412/988 | 4/1/5 | 1/1/1 | 7/42/92 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 160 | 173 | 85 | 89/5/997 | 10/90/255 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 162 | 168 | 90 | 140/3/992 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 163 | 25 | 9 | 17/29/996 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 164 | 14 | 12 | 6/379/953 | 7/249/792 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 165 | 2 | 2 | 1/459/459 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 166 | 35 | 32 | 23/34/987 | 20/-13/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 167 | 2 | 2 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 168 | 2 | 2 | 1/-1/-1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 169 | 2 | 2 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 170 | 2 | 2 | 1/-14/-14 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 171 | 32 | 11 | 19/120/952 | 3/360/1080 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 172 | 923 | 197 | 207/-15/5072 | 5/1/5 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 173 | 8 | 5 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 174 | 10 | 6 | 5/-5/952 | 4/0/952 | 4/0/724 | 3/0/280 | 3/0/947 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 175 | 8 | 2 | 4/25/35 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 177 | 6 | 6 | 2/521/952 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 178 | 30 | 18 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 179 | 2 | 2 | 1/-4/-4 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 180 | 12 | 10 | 2/-5/952 | 1/6/6 | 2/49/69 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 181 | 16 | 14 | 3/-5/952 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 182 | 8 | 8 | 1/2/2 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 183 | 6 | 4 | 2/0/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 184 | 4 | 4 | 2/32/521 | 2/0/10 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 185 | 22 | 20 | 3/-5/952 | 4/-50/20 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 186 | 2 | 2 | 1/736/736 | 1/35/35 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 187 | 2 | 2 | 1/521/521 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 188 | 834 | 107 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 189 | 397 | 44 | 14/12/319 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 190 | 136 | 93 | 31/-10/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 191 | 2 | 2 | 1/828/828 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 192 | 81 | 43 | 22/-9/45 | 3/0/23 | 2/0/24 | 2/0/20 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 193 | 4 | 2 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 194 | 28 | 25 | 3/1/3 | 4/5/100 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 195 | 4 | 2 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 196 | 2 | 2 | 1/2/2 | 1/100/100 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 197 | 4 | 2 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 198 | 2 | 2 | 1/2/2 | 1/100/100 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 199 | 4 | 2 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 200 | 2 | 2 | 1/2/2 | 1/100/100 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 201 | 2 | 2 | 1/952/952 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 202 | 88 | 65 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 203 | 521 | 109 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 204 | 144 | 75 | 38/-4/46 | 15/0/46 | 7/0/38 | 6/0/39 | 4/0/37 | 2/0/38 | 2/0/39 | 1/0/0 |
| act | 205 | 85 | 55 | 26/-10/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 206 | 70 | 36 | 22/-8/953 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 207 | 76 | 33 | 20/-4/44 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 208 | 26 | 23 | 9/-1/952 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 209 | 15 | 7 | 1/2/2 | 2/5000/10000 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 210 | 42 | 37 | 3/1/3 | 7/10/100 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 211 | 3 | 3 | 1/2/2 | 2/10/20 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 212 | 54 | 41 | 12/-10/987 | 12/-14/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 213 | 38 | 24 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 214 | 81 | 45 | 3/1/3 | 2/0/2 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 215 | 1133 | 326 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 216 | 578 | 131 | 154/3/5017 | 96/0/5018 | 71/0/968 | 60/0/973 | 48/0/977 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 217 | 461 | 309 | 40/-10/987 | 2/0/223 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 218 | 132 | 65 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 219 | 14 | 8 | 4/35/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 220 | 31 | 25 | 8/-8/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 221 | 24 | 20 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 222 | 2 | 2 | 1/-5/-5 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 223 | 216 | 92 | 53/-14/987 | 25/-14/986 | 16/-17/902 | 10/-14/989 | 8/0/952 | 5/-17/952 | 1/0/0 | 1/0/0 |
| act | 224 | 55 | 18 | 26/-4/61 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 225 | 251 | 97 | 42/-10/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 226 | 427 | 204 | 6/1/8 | 6/0/8 | 3/0/4 | 3/0/5 | 2/0/8 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 227 | 116 | 46 | 26/-9/57 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 229 | 4 | 4 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 230 | 51 | 24 | 5/1/5 | 5/-20/20 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 231 | 194 | 99 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 232 | 130 | 87 | 15/-30/100 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 233 | 103 | 58 | 6/95/150 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 234 | 121 | 56 | 27/-14/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 235 | 349 | 97 | 37/-9/46 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 236 | 137 | 52 | 15/-8/953 | 5/0/36 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 237 | 42 | 37 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 238 | 176 | 72 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 239 | 163 | 138 | 4/1/4 | 3/0/3 | 3/0/3 | 1/0/0 | 1/0/0 | 1/0/0 | 5/2/6 | 1/0/0 |
| act | 240 | 48 | 23 | 3/1/3 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 241 | 390 | 365 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 245 | 93 | 49 | 46/-14/963 | 3/0/433 | 2/0/656 | 2/0/185 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 247 | 276 | 276 | 3/2/4 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 248 | 276 | 276 | 3/34784/34801 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 249 | 314 | 130 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 251 | 5 | 5 | 2/880/987 | 3/-10/893 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 252 | 78 | 65 | 38/-10/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 254 | 4 | 4 | 2/5006/5008 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 256 | 21 | 21 | 7/-10/952 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 258 | 85 | 83 | 1/13/13 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 259 | 21 | 19 | 11/32/664 | 2/1/2 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 260 | 3 | 1 | 1/1/1 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 261 | 21 | 18 | 13/32/952 | 3/2/6 | 3/0/2 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 262 | 2 | 2 | 1/769/769 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 263 | 96 | 32 | 26/-9/61 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 264 | 2 | 2 | 1/12/12 | 1/2/2 | 1/35/35 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 265 | 3 | 2 | 2/521/952 | 2/3/5 | 3/34/526 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 267 | 343 | 34 | 11/7/61 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 268 | 5 | 3 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 269 | 5 | 3 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 270 | 43 | 34 | 10/-5/987 | 11/0/988 | 7/0/739 | 6/0/855 | 2/0/96 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 271 | 11 | 11 | 5/32/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 272 | 10 | 10 | 4/32/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 273 | 13 | 13 | 5/-1/14 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 274 | 9 | 9 | 5/2/41 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 275 | 9 | 9 | 5/2/14 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 276 | 4 | 4 | 2/2/9 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 277 | 64 | 23 | 14/-3/46 | 22/1000/30000 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 278 | 64 | 23 | 14/-3/46 | 23/2000/150000 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 279 | 73 | 24 | 18/-4/55 | 20/3000/50000 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 280 | 26 | 14 | 7/-3/36 | 2/3/5 | 14/1000/30000 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 281 | 26 | 14 | 7/-3/36 | 2/3/5 | 15/2000/150000 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 282 | 35 | 15 | 11/-4/55 | 2/3/5 | 16/3000/50000 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 283 | 9 | 5 | 3/2/14 | 3/3/5 | 3/1/2000 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 284 | 10 | 10 | 5/32/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 285 | 293 | 44 | 30/-4/61 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 286 | 6 | 3 | 6/7/35 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 287 | 51 | 21 | 23/-10/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 288 | 188 | 92 | 21/500/5500 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 289 | 20 | 20 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 290 | 38 | 7 | 17/-4/52 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 291 | 5 | 3 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 292 | 2 | 2 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 293 | 22 | 15 | 4/-3/10 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 294 | 75 | 64 | 37/-10/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 295 | 304 | 49 | 33/-4/61 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 296 | 4 | 2 | 1/58/58 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 297 | 4 | 2 | 2/687/887 | 1/0/0 | 1/32/32 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 298 | 94 | 28 | 29/32/953 | 2/0/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 299 | 559 | 95 | 40/-10/987 | 17/-10/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 301 | 2 | 2 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 302 | 4 | 2 | 1/35/35 | 1/3/3 | 2/20/30 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 303 | 3 | 3 | 2/35/521 | 2/0/40 | 2/40/120 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 304 | 2 | 2 | 1/35/35 | 1/40/40 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 305 | 33 | 26 | 2/2/3 | 6/10/80 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 306 | 41 | 34 | 2/2/3 | 7/10/100 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 307 | 14 | 12 | 2/2/3 | 5/10/70 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 308 | 9 | 9 | 5/-3/44 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 309 | 9 | 9 | 5/-3/44 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 310 | 9 | 9 | 5/-3/44 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 312 | 60 | 42 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 313 | 15 | 8 | 6/3/17 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 314 | 21 | 3 | 5/1/7 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 315 | 79 | 74 | 48/35/4196 | 19/0/4197 | 13/0/4198 | 12/0/4199 | 11/0/4200 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 316 | 146 | 76 | 32/-10/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 318 | 2 | 2 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 319 | 16 | 4 | 5/102/974 | 5/102/974 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 320 | 2 | 2 | 1/379/379 | 1/997/997 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 321 | 83 | 50 | 30/-3/46 | 5/0/34 | 5/-9/34 | 3/0/28 | 2/0/36 | 2/0/37 | 1/0/0 | 1/0/0 |
| act | 322 | 17 | 11 | 6/-3/47 | 4/0/48 | 4/0/49 | 4/0/50 | 3/0/51 | 2/0/51 | 1/0/0 | 1/0/0 |
| act | 323 | 17 | 15 | 7/-5/952 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 324 | 141 | 69 | 25/0/94 | 12/300/4500 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 325 | 25 | 19 | 4/30/80 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 326 | 1346 | 152 | 33/50/4500 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 327 | 2 | 2 | 1/0/0 | 1/0/0 | 1/379/379 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 328 | 204 | 81 | 25/29/94 | 22/500/7000 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 329 | 228 | 86 | 29/29/94 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 330 | 3 | 3 | 2/521/952 | 2/16/459 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 332 | 4 | 2 | 1/5023/5023 | 2/32732/32733 | 1/0/0 | 1/34598/34598 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 336 | 2 | 2 | 1/4101/4101 | 1/0/0 | 1/-1/-1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 346 | 100 | 6 | 10/52/61 | 1/2/2 | 3/700/900 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 347 | 43 | 13 | 2/0/1 | 27/-3/44 | 2/0/11 | 2/0/25 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 348 | 13 | 4 | 13/1/39 | 4/0/26 | 3/0/25 | 2/0/11 | 2/0/25 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 349 | 7 | 7 | 3/-5/952 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 350 | 1 | 1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 351 | 10 | 8 | 4/-4/938 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 352 | 6 | 4 | 3/32/553 | 4/501/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 356 | 1 | 1 | 1/16/16 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 359 | 27 | 16 | 25/-14/963 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 360 | 61 | 29 | 17/-5/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 364 | 8 | 8 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 365 | 10 | 10 | 2/-9/4 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 366 | 5 | 5 | 5/4101/4181 | 1/3/3 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 368 | 1 | 1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 369 | 5 | 5 | 5/1/17 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 370 | 17 | 10 | 8/1/17 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 372 | 30 | 2 | 3/5/34 | 3/7/35 | 3/6/32 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 373 | 30 | 2 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 374 | 54 | 2 | 1/1/1 | 2/0/1 | 2/132/736 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 375 | 21 | 8 | 5/-5/893 | 15/1/44 | 7/0/42 | 7/0/43 | 3/0/40 | 2/0/41 | 2/0/1 | 1/0/0 |
| act | 376 | 9 | 6 | 3/1/123 | 4/42/736 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 377 | 4 | 4 | 2/1/12 | 3/147/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 378 | 10 | 2 | 1/-5/-5 | 1/1/1 | 1/35/35 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 379 | 30 | 2 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 380 | 2 | 2 | 1/123/123 | 1/130/130 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 381 | 92 | 21 | 14/-5/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 382 | 4 | 4 | 1/-4/-4 | 2/521/736 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 383 | 32 | 24 | 2/80/100 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 384 | 8 | 2 | 4/32/953 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 418 | 1 | 1 | 1/161/161 | 1/658/658 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 420 | 1 | 1 | 1/658/658 | 1/161/161 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 422 | 3 | 1 | 3/41/50 | 1/2/2 | 1/-1/-1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 424 | 1 | 1 | 1/2/2 | 1/-1/-1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 425 | 311 | 107 | 100/1/100 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 426 | 19 | 19 | 19/132/151 | 5/-4/526 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 427 | 20 | 20 | 20/1/20 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 428 | 214 | 103 | 110/1/997 | 14/100/2500 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 430 | 81 | 78 | 13/15/300 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 432 | 51 | 17 | 17/1/17 | 2/1/2 | 1/4/4 | 2/2/3 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 433 | 18 | 6 | 6/1/6 | 2/1/2 | 1/4/4 | 2/2/3 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 434 | 12 | 6 | 6/1/6 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 435 | 6 | 6 | 6/1/6 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 437 | 1 | 1 | 1/1/1 | 1/52/52 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 438 | 3 | 3 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 439 | 3 | 3 | 3/-10/20 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 440 | 3 | 1 | 1/4/4 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 441 | 16 | 5 | 14/1/39 | 2/1/3 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 443 | 1 | 1 | 1/1000/1000 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 445 | 1 | 1 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 446 | 11 | 4 | 8/-14/963 | 5/-3/41 | 5/0/24 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 447 | 1 | 1 | 1/139/139 | 1/-8/-8 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 448 | 1 | 1 | 1/123/123 | 1/551/551 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 449 | 2 | 2 | 2/798/877 | 1/2/2 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 450 | 1 | 1 | 1/952/952 | 1/2/2 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 451 | 3 | 1 | 3/41/50 | 1/4/4 | 1/4/4 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| act | 453 | 100 | 100 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 0 | 1070 | 1070 | 1/1/1 | 2/1/2 | 2/1/3 | 2/1/4 | 2/-1/1 | 2/-2/1 | 2/-3/1 | 2/-4/1 |
| cond | 5 | 221 | 151 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 6 | 221 | 151 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 7 | 105 | 62 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 8 | 105 | 62 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 9 | 125 | 108 | 71/3/519 | 2/0/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 10 | 228 | 191 | 134/2/526 | 2/4/6 | 12/1/72 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 12 | 10 | 10 | 5/1/5 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 13 | 10 | 9 | 1/4/4 | 7/184/235 | 3/1/10 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 14 | 152 | 146 | 2/4/6 | 37/189/264 | 12/1/12 | 5/1/21 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 15 | 427 | 427 | 2/2/4 | 9/0/360 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 16 | 58 | 58 | 2/0/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 17 | 24 | 24 | 1/2/2 | 3/5001/5003 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 18 | 88 | 86 | 2/1/2 | 11/-5/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 19 | 7 | 7 | 1/2/2 | 2/18/20 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 20 | 222 | 174 | 33/-5/987 | 5/2/6 | 15/1/35 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 21 | 28 | 28 | 1/-1/-1 | 1/4/4 | 5/1/5 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 22 | 58 | 44 | 8/-5/945 | 2/2/4 | 6/0/7 | 5/1/6 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 23 | 2 | 2 | 1/-1/-1 | 1/6/6 | 1/50000/50000 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 24 | 119 | 95 | 10/-5/952 | 5/1/6 | 9/1/9 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 25 | 201 | 139 | 26/-5/987 | 2/0/1 | 37/-5/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 26 | 195 | 154 | 26/-5/4101 | 40/-5/4181 | 4/1/6 | 6/1/6 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 27 | 41 | 35 | 11/-5/987 | 1/1/1 | 17/-1/4121 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 28 | 2 | 2 | 1/-1/-1 | 1/4/4 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 29 | 2 | 2 | 1/-1/-1 | 1/4/4 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 30 | 59 | 53 | 7/-5/952 | 4/1/6 | 2/0/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 32 | 11 | 11 | 5/1/6 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 33 | 4 | 2 | 2/29/459 | 1/-5/-5 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 34 | 60 | 48 | 3/521/952 | 3/1/3 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 35 | 11 | 11 | 3/-5/952 | 2/379/440 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 36 | 92 | 76 | 2/1/2 | 40/-5/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 37 | 2 | 2 | 1/521/521 | 1/4/4 | 1/952/952 | 1/2/2 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 38 | 113 | 69 | 15/-5/987 | 3/2/4 | 6/0/5 | 17/1/17 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 39 | 4 | 4 | 2/-1/987 | 1/4/4 | 2/10/50 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 40 | 23 | 23 | 1/4/4 | 2/3/4 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 41 | 2 | 2 | 1/1/1 | 1/4/4 | 1/2/2 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 42 | 2 | 2 | 1/952/952 | 1/4/4 | 1/90/90 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 46 | 4 | 4 | 1/-1/553 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 47 | 2 | 2 | 1/-5/-5 | 1/2/2 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 48 | 9 | 9 | 1/2/2 | 1/736/736 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 49 | 72 | 33 | 15/2/58 | 2/1/2 | 13/-5/953 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 50 | 1020 | 516 | 46/1/46 | 2/1/2 | 47/-5/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 52 | 280 | 280 | 47/-1/46 | 2/2/4 | 2/90/100 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 55 | 276 | 276 | 46/1/46 | 1/2/2 | 3/1/3 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 56 | 582 | 251 | 146/5/1000 | 2/1/2 | 33/-5/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 57 | 31 | 18 | 11/-4/5003 | 2/1/2 | 17/6/39 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 58 | 2 | 2 | 1/179/179 | 1/2/2 | 1/260/260 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 59 | 72 | 61 | 39/5/1000 | 6/1/7 | 5/0/8 | 3/0/4 | 3/0/5 | 2/0/8 | 1/0/0 | 1/0/0 |
| cond | 60 | 112 | 28 | 27/-4/997 | 1/0/0 | 24/-4/997 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 61 | 30 | 30 | 14/5/997 | 2/4/6 | 2/90/95 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 62 | 180 | 105 | 48/-8/997 | 1/0/0 | 34/-8/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 64 | 355 | 299 | 65/-8/987 | 94/0/997 | 72/-8/997 | 44/-7/1000 | 18/0/952 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 65 | 4 | 4 | 2/5006/5008 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 66 | 34 | 20 | 14/249/952 | 2/0/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 67 | 34 | 30 | 14/5/997 | 2/1/2 | 6/-4/952 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 68 | 6 | 6 | 3/1/124 | 3/-4/736 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 69 | 36 | 34 | 16/95/997 | 5/0/980 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 73 | 4 | 4 | 1/-4/-4 | 2/4/6 | 2/10/11 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 74 | 2 | 2 | 1/736/736 | 1/2/2 | 1/18/18 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 75 | 8 | 8 | 2/440/988 | 1/3/3 | 2/4/6 | 1/70/70 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 78 | 4 | 4 | 2/29/444 | 1/2/2 | 2/459/576 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 79 | 2 | 2 | 1/828/828 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 216 | 6 | 6 | 3/371/893 | 3/97/754 | 3/638/958 | 3/208/973 | 3/0/968 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 225 | 2 | 2 | 1/736/736 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 229 | 4 | 4 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 231 | 6 | 6 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 243 | 8 | 8 | 3/179/526 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 244 | 24 | 24 | 12/95/953 | 7/0/997 | 4/0/988 | 2/0/147 | 2/0/656 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 246 | 276 | 276 | 46/1/46 | 3/6/12 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 255 | 30 | 30 | 1/-1/-1 | 1/4/4 | 8/20/700 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 257 | 6 | 6 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 264 | 14 | 12 | 9/12/319 | 1/2/2 | 9/-5/952 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 265 | 64 | 53 | 9/-5/952 | 4/3/6 | 21/-5/987 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 280 | 5 | 5 | 1/-1/-1 | 1/4/4 | 1/80000/80000 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 282 | 7 | 7 | 6/4/51 | 2/4/5 | 2/50000/100000 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 298 | 518 | 257 | 50/29/987 | 2/0/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 300 | 21 | 21 | 7/34/987 | 2/0/1 | 9/32/4101 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 317 | 2 | 2 | 1/35/35 | 1/4/4 | 1/3/3 | 1/7/7 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 335 | 25 | 25 | 5/1/17 | 2/0/1 | 1/-1/-1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 336 | 31 | 31 | 5/4101/4181 | 2/0/1 | 1/-1/-1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 347 | 37 | 17 | 1/1/1 | 30/1/46 | 2/0/17 | 2/0/13 | 2/0/11 | 2/0/25 | 1/0/0 | 1/0/0 |
| cond | 353 | 17 | 17 | 10/1/57 | 2/0/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 355 | 10 | 8 | 6/32/987 | 1/1/1 | 5/3/16 | 4/0/17 | 2/0/7 | 2/0/5 | 1/0/0 | 1/0/0 |
| cond | 361 | 2 | 2 | 1/4/4 | 1/4/4 | 1/100/100 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 362 | 8 | 8 | 4/1/17 | 1/4/4 | 1/100/100 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 363 | 8 | 8 | 4/1/17 | 1/5/5 | 1/50000/50000 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 367 | 5 | 5 | 5/4101/4181 | 1/3/3 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 369 | 5 | 5 | 5/1/17 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 371 | 5 | 5 | 5/1/17 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 372 | 2 | 2 | 1/15/15 | 1/14/14 | 1/16/16 | 1/17/17 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 373 | 2 | 2 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 374 | 2 | 2 | 1/1/1 | 1/1/1 | 1/736/736 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 378 | 5 | 5 | 1/-1/-1 | 1/0/0 | 1/-5/-5 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 379 | 2 | 2 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 417 | 3 | 3 | 2/-5/557 | 1/1/1 | 2/20/25 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 422 | 312 | 131 | 100/1/100 | 1/2/2 | 1/-1/-1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 423 | 100 | 100 | 100/1/100 | 1/6/6 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 431 | 72 | 6 | 1/-1/-1 | 72/2/73 | 1/1/1 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 436 | 1 | 1 | 1/123/123 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 437 | 2 | 1 | 1/1/1 | 1/52/52 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 444 | 9 | 2 | 9/1/39 | 3/1/3 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 451 | 8 | 6 | 8/13/80 | 1/4/4 | 2/2/4 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |
| cond | 452 | 1 | 1 | 1/4101/4101 | 1/0/0 | 1/521/521 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 | 1/0/0 |

### 9.5 EventSample*.s14

`u32 1` 로 시작하는 편집기 샘플 이벤트 목록(제목 `샘플이벤트（…）` + 설명 UTF-16LE + 이진). 게임 이벤트 스크립트가 아니다. 구조 미해결, 언어별 5개 중 Ko만 범위.

## 10. DLC

DLC/ folder (language-independent parts and 0010_KO only).

DLC/0010_KO/sceda*.s14, scedaex*.s14, scedaexce10/11/32/33.s14 are wrapped in an XOR stream over the WHOLE file (reference_mod MISC_DATA_FILES.md 2):
    state = (state * 0x6C078965 + 0x3039) mod 2^32   (rolled BEFORE each byte)
    out   = in ^ ((state >> 16) & 0xFF) ^ ((state >> 24) & 0xFF)
    initial state = DLC id + scenario number (transform is its own inverse)
The initial states below were recovered by brute force search over 0..6e7 (known plaintext: tier version u32 + 'SN14SCEXVER0001', MEAS);
the base-game files (sceda) share the state of the scedaex file with the same number (same keystream, verified by LWC magic after decoding).
DLC/DLCInfo*.s14와 DLC/0011/gd_*.s14는 본문을 해독하지 않고 목록만 작성했다. 이후 현재 EXE의 DLCInfo 읽기 경로에서 바이트별 XOR 스트림을 확인했지만 초기 상태는 파일 번호만이 아니라 다른 정수에도 의존하며, 읽기 전에 Steam 인터페이스 결과를 검사한다. 상세는 [아카이브 1.4절](data_formats_archives.md)이다. gd 파일에 같은 처리가 쓰이는지는 미확인이다.
DLC/0003/*.wmv (movies) and DLC/0005/*.bin (archives, K4 scope) are not parsed here.

| 파일 | 계층 | 번호 | 초기 state | 이름 |
|---|---|---|---|---|
| sceda09.s14 | base(51) | 9 | 1198845 | 동관 전투 |
| sceda10.s14 | base(51) | 10 | 1198840 | 이릉 전투 |
| sceda11.s14 | base(51) | 11 | 1198842 | 추풍오장원 |
| sceda12.s14 | base(51) | 12 | 1198851 | 여포토벌전 |
| sceda13.s14 | base(51) | 13 | 1198856 | 하북쟁란 |
| sceda14.s14 | base(51) | 14 | 1198858 | 합비 전투 |
| sceda15.s14 | base(51) | 15 | 1198847 | 정시정변 |
| sceda16.s14 | base(51) | 16 | 1198862 | 성씨패란 |
| sceda17.s14 | base(51) | 17 | 1198864 | 황천당립 |
| sceda18.s14 | base(51) | 18 | 1198866 | 하북영웅 공손찬 |
| sceda19.s14 | base(51) | 19 | 1258173 | 영원한 꿈 속에서 |
| sceda26.s14 | base(51) | 26 | 1431509 | 흔들리는 한조 |
| sceda27.s14 | base(51) | 27 | 1431514 | 조조의 대두 |
| sceda28.s14 | base(51) | 28 | 1431521 | 남만정벌 |
| sceda29.s14 | base(51) | 29 | 1431509 | 촉한의 멸망 |
| scedaex09.s14 | PK(92) | 9 | 1198845 | 빠른 오호십육국 |
| scedaex10.s14 | PK(92) | 10 | 1198840 | 이릉 전투 |
| scedaex11.s14 | PK(92) | 11 | 1198842 | 추풍오장원 |
| scedaex12.s14 | PK(92) | 12 | 1198851 | 여포토벌전+ |
| scedaex13.s14 | PK(92) | 13 | 1198856 | 하북쟁란+ |
| scedaex14.s14 | PK(92) | 14 | 1198858 | 동천당립 |
| scedaex15.s14 | PK(92) | 15 | 1198847 | 정시정변 |
| scedaex150.s14 | PK(92) | 150 | 1431635 | 유비 입촉 |
| scedaex151.s14 | PK(92) | 151 | 1431639 | 맹장석권 |
| scedaex152.s14 | PK(92) | 152 | 1431642 | 하북평정전 |
| scedaex153.s14 | PK(92) | 153 | 1431647 | 오평정전 |
| scedaex154.s14 | PK(92) | 154 | 1431651 | 연주쟁탈전 |
| scedaex16.s14 | PK(92) | 16 | 1198862 | 17주 쟁탈전 |
| scedaex17.s14 | PK(92) | 17 | 1198864 | 황천당립 |
| scedaex18.s14 | PK(92) | 18 | 1198866 | 중원황제 원술 |
| scedaex19.s14 | PK(92) | 19 | 1258173 | 영원한 꿈속에서 |
| scedaex26.s14 | PK(92) | 26 | 1431509 | 흔들리는 한조 |
| scedaex27.s14 | PK(92) | 27 | 1431514 | 조조의 대두 |
| scedaex28.s14 | PK(92) | 28 | 1431521 | 남만정벌 |
| scedaex29.s14 | PK(92) | 29 | 1431509 | 촉한의 멸망 |
| scedaexce10.s14 | CE(102) | 10 | 1198840 | 이릉 전투 |
| scedaexce11.s14 | CE(102) | 11 | 1198842 | 추풍오장원 |
| scedaexce32.s14 | CE(102) | 32 | 4598982 | 조조의 오산 |
| scedaexce33.s14 | CE(102) | 33 | 4598993 | 패기웅심 |

DLCInfo*.s14 (35개): DLCInfo08.s14, DLCInfo09.s14, DLCInfo10.s14, DLCInfo11.s14, DLCInfo13.s14, DLCInfo14.s14, DLCInfo15.s14, DLCInfo17.s14 ... 크기 7~1100B, 엔트로피 높음. 0011/gd_*.s14 45개 x 846B. 이전에 시험한 초기 state = 번호/번호²/0/1로는 풀리지 않았다. 현재 EXE에서 DLCInfo 경로의 XOR과 초기 상태 계산·Steam 검사 순서는 확인했으나 파일 본문과 gd 경로는 미해독이다([아카이브 1.4절](data_formats_archives.md)).

## 11. 요약 수치

- 스펙 필드: 확정 218, 추정 43 (위 표들의 합)
- 미해결 가변 바이트 구간(스펙 밖, 표당 최대 48줄 표시): 233
- Event001/PKCE001의 통계에 등장한 코드: 조건 103종, 행동 335종. 실행·설명 주소는 [이벤트 코드 색인](event_opcodes.json).
