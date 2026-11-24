# 원작 구조체·필드 오프셋 통합 (STRUCT)

> **이 문서에서 찾는 법**: 1 개요 · 2 구조체 지도(world 표) · 3 구조체별 절 · 4 fixdata 표 등록부 · 5 엔진 대응 · 6 충돌 · 7 정정 기록 · 8 미해결 · 9 출처와 낡음 확인.
> **새 확정 사실은 이 문서의 해당 절에 추가한다.** 기계가 읽는 사본은 `structs.json`(구조체→오프셋→필드·폭·뜻·근거·확신도·엔진 필드).

작성 2026-11-07 (M1, 2단계 통합). 기준 빌드 `1a4a447d14e68c40…`(Steam buildid 25953386, TimeDateStamp 0x6AD06F53). 옛 `1fbe6be7…`(0x6A983C25).

## 1. 개요

- **오프셋은 두 빌드에서 같다.** world 구조체 필드 오프셋 22종(`+0x871E8` game, `+0xDD38/DED8/DF30/E0D0/E270/6CAF0/6DA98/73A50/7E838/158` 표, 날짜 `+0x34/+0x36/+0x37` 등)은 두 빌드 C 추출본 전체 스캔에서 사용 횟수와 값이 일치(build_remap.md §1). 객체 크기(stride)는 생성자 상수 개수와 사람 슬롯 나눗셈 상수로 간접 확인했다. 변경 없음이 직접 확인된 필드: army `+0x12/+0x16/+0x1A/+0x2A/+0x37/+0x38/+0x3A/+0x140`, troops `+0x14/+0x16/+0x18`, 표 `0x7E838/0x73860/0x73958`, `0x85F20`(BUILD_25953386_COMBAT.md §1).
- **세 가지 오프셋 좌표를 섞지 말 것**: ① *런타임 객체 오프셋*(이 문서의 기본), ② *fixdata 레코드 오프셋*(파일 본문 안; 진형은 객체 = 레코드 + 0x10, 지형은 +0x10(+0x1C까지)/+0x11), ③ *에디터 AST 선언*(`reference_mod/Editor_Source/san14ce/memschema.py`; 기준점이 객체 시작이 아닌 표가 있음). 압축해제 본문 오프셋·압축 파일 오프셋·PE 파일오프셋·RVA도 서로 다르다(data_model.md).
- **확신도**: *확정* = 코드/덤프 근거, *추정*, *충돌*(문서끼리 어긋남, 6절), *미해결*. 필드마다 출처 문서와 절을 단다. 약어: W=worldmap_spec.md, WB=worldmap_spec_b.md, CA=command_audit.md, DM=REA_Analysis/data_model.md(옛 에디터 선언), DMs=dump_measurements.md, L1~L4=lane_L1~L4.md, DF=difficulty.md.
- 구조체 24개. 2026-11-07 L3b: 충돌 18건 중 7건 해소(S2·S6·S7·S8·S9·S11·S12), 신규 2건(S17·S18); 미해결 U 12건 중 U2·U12 해소, U8 시도 기록 갱신. 2·3차 묶음 절은 본문으로 옮기고 삭제했다. 필드 수 통계는 structs.json 재생성 전까지 옛 값(298개)이다.
- 엔진(San14Sim/engine)은 구조체 대신 **병렬 배열**을 쓴다(`core/sim.h`의 `Game::Data`: `gold[NB]`, `person_*[]`, `hex_owner[48400]` …)와 `struct Unit`/`Facility`. 엔진 필드 열은 이 이름들이다. 엔진 RVA 주석은 새 빌드 값이다(sim.h 머리말).

## 2. 구조체 지도 (세계 루트에서 각 객체 표)

| 오프셋 | 이름 | 뜻 | 엔진 | 출처 | 확신도 |
|---|---|---|---|---|---|
| `+0xDD38` | city_table | 도시 객체 표(stride 0x168, 객체 앵커 +0x34). 도시 id 0~0x33 | Data::gold/food/troops[NB] 등 병렬 배열 | DM 주소 기준점 | 확정 |
| `+0xDC80` | state_table | 주(州) 객체 표 23칸(8B 포인터; fixdata 표 `state`와 같은 번호). 도시 `+0xCE`(byte) 가 번호, `935F0`이 조회(범위 밖은 0번). 주 `+0x30`(byte) = state.geo(0..17) = 지방 이점 번호(`92AE0`) | 조건 139 | L3 5차(`A5B10`·`935F0`·`2C9120`) | 확정 |
| `+0x85990` | geo_advantage_table | 지방 이점 객체 표 18칸(주 `+0x30` 색인, 0 = 없음). 객체 `+0x95`(byte) = 기준 도시 수 cap(+0xA0..A8 목록이 5원소면 vcall +0x48 로 계산), 번호 `22F440`(조건 140) | 조건 139·140; 정보 CVariableGetAdvantageInfo | L3 5차(`93480`·`2C9120`) | 확정(위치·기준값)/추정(이점 효과 내용) |
| `+0xDED8` | gate_table | 관문 객체 표(stride 0xC0). 관문 id 0x34~0x3D | Data[NB=62] 중 관문 슬롯 | DM | 확정 |
| `+0xDF30` | force_table | 세력 객체 표(stride 0x268) | Data::ruler/alive/... [NF=52] | DM | 확정 |
| `+0xE0D0` | corps_table | 군단 객체 표(stride 0x30, 앵커 +0x10) | Data::corps_*[NF] | DM | 확정 |
| `+0xE270` | hex_table | 칸(HEX) 포인터 표 220x220. 칸 번호=(객체-표[0])>>5 (`22F830`) | Data::hex_owner[48400], Map::tile | W §0.2; DM | 확정 |
| `+0x6CAF0` | area_table | 지역 객체 표(stride 0x98, 앵커 +0x52). 지역 1..343, 덤프 area 표는 501칸 | Map::region_* / Data::region_*[NR=344] | DM; W §1.1 | 확정 |
| `+0x6DA98` | building_table | 지도 건축물(시설) 표(stride 0x20). 덤프 3,063개 | Game::Facility (fac_*) | DM; WB §6.1 | 확정 |
| `+0x73860` | terrain_objects | 지형 객체 표(객체 0x48 B; 덤프 정의표에서는 0x80B로도 기재) | Map::terrain_cost/flag/attr42/drain/fire | W §0.4; CA §15; WB §6.2 | 확정 |
| `+0x73958` | facility_defs | 시설 정의 표(런타임 104B). `27A8D0`의 3번째 인자 | engine/rules/facility_tables.h FAC_DEF | W §3.1; WB §6.2 | 확정 |
| `+0x73A50` | person_table | 무장 객체 표(stride 0x1F0, 앵커 +0xEC). 물리 길이 1851, 참고 스캔 상한 3000 | Data::person_*[] | DM | 확정 |
| `+0x774D0` | tactic_table | 전법 표(201칸) — 무장 +0x130[10]이 이 표의 id를 가진다 | Map::tactic_* | CA #23 | 추정(주소만 인용됨) |
| `+0x77428` | formation_table | 진형 객체 표(stride 0xC8). 길 찾기가 부대 [+0x1B]/[+0x1C]로 인덱스 | Map::formation_*[21] | DM; W §4.5 | 확정 |
| `+0x77B18` | treasure_table | 명품 객체 표(stride 0x80) | engine/rules/treasure_tables.h | DM | 확정 |
| `+0x78490` | rank_post_table | 관직 순위 표 — 엔진 미추출 항목(approx_inventory S8/D3) | 미반영(office_rank 근사) | approx_inventory.md S8 | 추정 |
| `+0x784F8` | post_table | 관직 객체 표(stride 0x58) | Map::office_stats/office_rank | DM | 확정 |
| `+0x78D50` | policy_table | 정책 객체 표(stride 0xA8) | Map::policy_* | DM | 확정 |
| `+0x79118` | tactic_book_table | 전법서 31칸(21B 레코드). 세력 +0x120[idx]가 재고 | Data::force_book[NF*31] | CA #23 | 확정 |
| `+0x7DD18` | trait_objects | 개성 객체 표(232B). 한 무장은 개성 9칸(traits9 이전 5칸) | Map::trait_*; Game::trait_effect* | WB §5.2 | 확정 |
| `+0x7E838` | army_table | 부대 객체 표(stride 0x200) | Data::units (Unit) | DM; BUILD_25953386_COMBAT §1 | 확정 |
| `+0x7F8D8` | troops_by_id | 군세 id 조회 표 | - | DM(추가 관측) | 확정 |
| `+0x80880` | policy_effect_index | 세력 정책 효과 index 표(`41E570`/`22DFD0`이 사용) | Data::policy_effect[NF*101] | WB §5.3; formation_mapping.md | 확정 |
| `+0x85A90` | scenery_table | 명승(Scenery) 표 101칸(간격 0x78). 객체 `+0x5C` = 칸, `+0x5F` bit0, `+0x64`/`+0x66`/`+0x68`/`+0x6C` = 투자·발전 필드(`8B190` case 44 조건: +0x64==1, +0x6C 1..5, +0x66==0, +0x68<1). 이전 "숨은 물건 목록" 해석은 정정 | 명승·숨은 물건 APPROX 배치 | L3b 2차(`8FFA0`, `2826B0`) | 확정(표 종류)/추정(필드 이름) |
| `+0x85DF0` | rank_reward_table | fixdata 표 ID 39 `공적 보상`(7 x 4B) | Game::rank_bonus (능력 영향 없음으로 정정) | CA §15 항목 5 | 확정 |
| `+0x85F20` | doctrine_table | 주의(신념) 표 (+0x44 항). BUILD_..._COMBAT는 '기술 0x85F20' | Data::force_ideology_exp | BUILD_25953386_COMBAT §1; DMs | 확정(주소)/의미 추정 |
| `+0x871E8` | game_state | 게임 진행 단일 객체(GAME) 포인터. 플레이어 세력 `2337B0`(새 235150)이 여기를 읽음 | Game::d (year/month/day/player_forces) | DM; DF §1 | 확정 |
| `+0x158` | person_gameid_lookup | 무장 게임ID 조회표(+0x73A50 슬롯표와 구분) | Game::pindex | DM | 확정 |
| `+0x872C0` | mod_expansion | 모드 확장 표 — 원래 배열 범위로 일반화 금지 | - | DM | 확정(주의) |

## 3. 구조체별 절

### 3.1 HEX — 칸(HEX) 런타임 객체

- RTTI `CHexData` · 표: +0xE270[48400] · 크기: 32 · 앵커: +0
- 출처: W §0.2 (0장 확정, 덤프 48,400/48,400 일치)
- 지도 220x220(id=y*220+x, 유효 0..48399, 무효값 48400=0xBD10). 이웃 규칙은 열 오프셋 평탑(W §0.3). 칸 번호=(객체-표[0])>>5.

| 오프셋 | 폭 | 이름 | 뜻 | 엔진 필드 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `+0x00` | vptr | vtable | vtable |  | W §0.2 | 확정 |
| `+0x10` | u8 | terrain_id | 지형 id (<0x1F, 지형 객체 표 인덱스) | Map::tile / Map::terrain | W §0.2 | 확정 |
| `+0x12` | u16 | area_id | 지역 번호(0=지역 없음=통행불가 지형 19~23) | Map::tile(region) | W §0.2 | 확정 |
| `+0x14` | u8 | owner | 소유 세력: 0 무주, 1..51, 0x33 중립, 0x2E~0x32 이민족. 쓰기 입구 `186E60` | Data::hex_owner | W §0.2, §1.2 | 확정 |
| `+0x16` | u16 | fire | 화염값(0..720). `2A3CF0` 이 칸마다 매 틱 `DAT_141A4C070` 만큼 줄이고(0이 아니면), `43E660`·`2A3510`·`2E5DA0`(점화 `2E8160`)이 읽는다. 1권의 "경로 예약 표지, 덤프 항상 0"은 화염이 없던 덤프의 값(해소) | Data::hex_fire | L3b(`2A3CF0` 코드); CA §15; rules_combat_effects.md | 확정 |
| `+0x19` | u8 | supply_cut_pct | 보급 소비 감면 %(시설 효과 18이 범위 칸에 씀, 겹치면 큰 값, 상한 100). `300970`이 매 갱신 지우고 다시 씀 | engine/rules/facility_game.h | W §0.2, §2.5 | 확정(코드+덤프 30건) |
| `+0x1A` | u16 | facility_id | 시설·거점 건물 id(0 없음). 도시·관문은 7칸(중심+6)에 같은 id(<=61), 시설(id>=62)은 정확히 1칸 | Game::fac_at / Map::foot | W §0.2 | 확정 |
| `+0x1E` | u16 | base_mark | 거점 표식(약 100칸만 0이 아님) |  | W §0.2 | 추정 |
| `+0x2C` | bit1 | terrain_layer | 지형층 비트(함정 효과 판정에서 같은 지형층 비교, `hex+0x2C` bit1) |  | L3 함정 | 추정 |

### 3.2 HEX_FILE — 지도 파일 칸 (MapExCe.bin)

- RTTI `-` · 표: 파일 `0000/MapExCe.bin` (data/map_cells.bin 동일 바이트) · 크기: 16 · 앵커: 머리 4B(u32=48400)+칸x16B
- 출처: W §0.1~0.2
- 774,404바이트. 엔진 init.cpp는 칸 +4(지형)을 읽고 extract.py는 +6(지역)만 map.json.tiles로 뽑는다.

| 오프셋 | 폭 | 이름 | 뜻 | 엔진 필드 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `+0` | u16 | cell_id | 칸 번호(0..48399) |  | W §0.2 | 확정 |
| `+4` | u8 | terrain_id | 지형 id(1~24), 런타임 hex+0x10과 100% 일치 | Map::terrain | W §0.2 | 확정 |
| `+6` | u16 | area_id | 지역 번호, 런타임 hex+0x12와 100% 일치 | Map::tile | W §0.2 | 확정 |
| `+8` | u8(0/1/2) | unk8 | 시나리오 시작 소유·표식 후보(22칸만 0이 아님) |  | W §0.2 | 미해결 |
| `+9` | u8(0..6) | unk9 | 시각 속성 후보 |  | W §0.2 | 미해결 |
| `+10..13` | u8 x4 | flags | 플래그 4개 |  | W §0.2 | 미해결 |
| `+14` | u8 | unk14 | 지형 변형·그림 후보 |  | W §0.2 | 미해결 |
| `+15` | u8 | unk15 | 38칸만 0이 아님 |  | W §0.2 | 미해결 |

### 3.3 TERRAIN — 지형 객체

- RTTI `CTerrainData` · 표: +0x73860[31] · 크기: 0x48 (런타임) · 앵커: fixdata 표 8 레코드 51B(포장)
- 출처: W §0.4; CA §15 '지형 객체 레이아웃 정정'
- 런타임 오프셋 = fixdata 레코드 오프셋 + 0x10 (+0x1C까지), 이후(u16 배열 짝수 정렬 뒤)는 + 0x11. `BF1B0`(옛 `BE120`)이 비용을 반환.

| 오프셋 | 폭 | 이름 | 뜻 | 엔진 필드 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `레코드 +0x1A / 런타임 +0x2A` | u16 | move_cost | 이동 비용(평지 225, 가도 150, 모래 300, 습지 375, 밀림 525, 독늪 750, 고산 600, 마을·도시·관문·항 150, 여울 375, 강 450, 대하 300) | Map::terrain_cost | W §0.4,§4.1 | 확정 |
| `레코드 +0x1C / 런타임 +0x2C` | u8 | flags | 플래그(5 육상, 1 육상 일부, 2 수상(비트1), 0 통행 불가) | Map::terrain_flag | W §0.4; CA §15 | 확정(수상 비트)/추정(나머지) |
| `레코드 +0x1F,+0x21..+0x2D` | u16 x8 | formation_family_pct | 진형 계열별 지형 보정 %(8번째=수군). 대하14·격류24는 앞 7개 0·마지막 100 |  | W §0.4 | 확정(값)/추정(용도) |
| `레코드 +0x2F / 런타임 +0x40` | u8 | drain_base | 정기 사기 감소 기본값(거침 등급 0/1/2). `2B2330`(옛 `2B0070`)이 읽음. 평지·가도 1, 모래·습지·고산·산길 3, 숲·밀림 2, 독늪·강·여울·대하 0, 마을·도시·관문·항 1 | Map::terrain_drain | CA §15 (정정본); W §0.4 | 확정(덤프) |
| `레코드 +0x30 / 런타임 +0x41` | u8 | fire_class | 화염 계열(0 불가, 1 평지, 2 숲·밀림·산, 3 모래·습지·고산·산길) | Map::terrain_fire | CA §15 | 확정(덤프) |
| `레코드 +0x31 / 런타임 +0x42` | u8 | category | 지형 분류(1 평지, 2 산, 3 숲, 4 대하, 5 습지·여울·강). 개성 조건 14~19, 정책 효과 0x30 항(분류 2·4)이 읽음 | Map::terrain_attr42 | CA §15 | 확정(조건 함수와 이름 일치) |

### 3.4 FACILITY_DEF — 시설 정의

- RTTI `-` · 표: +0x73958[31] (런타임 104B) · 크기: 53 B (fixdata 표 9, 본문 0x2CD9E x31; 직렬화 `23C6F0`) · 앵커: 파일 오프셋
- 출처: W §3.1 (확정)
- id 1 도시, 2 관문, 3 진, 4 요새, 5 망루, 6 투석대, 7 군악대, 8 석병팔진, 9 토성, 10 석벽, 11 불함정, 12 맹화함정, 13 화선, 14 구덩이, 15 망대, 16 철쇄, 17 낙석, 18~30 건물(미사용). 표 원문은 San14Sim/docs/fidelity/worldmap/facility_table.json.

| 오프셋 | 폭 | 이름 | 뜻 | 엔진 필드 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `+0x1C` | u8 | class | 1 거점, 2 군사시설, 3 방벽, 4 함정 | engine/rules/facility_tables.h FacDef | W §3.1 | 확정 |
| `+0x1D` | u16 | durability | 내구 최대(진 400, 요새 600, 망루 300, 투석대 400, 군악대 300, 석병팔진 300, 토성 500, 석벽 800, 함정 15~30, 화선 20, 철쇄 350, 망대 200, 낙석 20) |  | W §3.1 | 확정(관측 최대 일치) |
| `+0x1F` | u16 | cost_gold | 비용(금). 착공 때 부대 출발 거점 금에서 차감(`2AD6C0`) |  | W §3.1; worldmap_s4s6.md | 확정(s4s6에서 코드 확인) |
| `+0x21` | u16 (런타임 def+0x32) | required_list_no | 건설 담당 목록 번호(석병팔진 49). `27A8D0`이 목록 검사 |  | W §3.2 항 9 | 확정(위치)/미해결(의미) |
| `+0x23` | u8 | need_effect_id | 필요 정책 효과 id(13 지원시설해방, 19 화계전법강화, 24 산천시설해방, 0 없음) |  | W §3.2 항 8 | 확정 |
| `+0x24` | u8 | spacing | 간격값(`27DAF0`): 도시·관문 3, 군사시설 2, 방벽·함정 0 |  | W §3.1 | 확정 |
| `+0x2B` | u8 | min_range | 효과 최소 거리(투석대 2, 나머지 1) |  | L3 `180870` | 확정 |
| `+0x2C` | u8 | range | 효과 범위(진 2, 요새 2, 망루 2, 투석대 3, 군악대 2, 석병팔진 1, 불함정 1, 맹화 2, 화선 1, 구덩이 2, 망대 2, 낙석 2) |  | W §3.1 | 확정 |
| `+0x2E` | u32 | terrain_mask | 건설 허용 지형 비트마스크(0xE 평지·가도·모래, 0x300 저산·중산, 0x4000 대하, 0x10000 도시, 0x20000 관문). `43720`이 판정 |  | W §3.1 | 확정 |
| `+0x32` | u8 | trap_subkind | 함정 하위 종류(1/2). 의미 미상 |  | W §3.1 | 미해결 |
| `+0x33` | u8 | need_threshold | 필요 효과 합 임계(요새 7, 투석대 10, 군악대 4, 석벽 2, 화선 5, 맹화 10, 망대 10, 철쇄 2, 낙석 5) |  | W §3.1 | 확정 |

### 3.5 BUILDING — 지도 건축물(시설 인스턴스)

- RTTI `CObjectData` · 표: +0x6DA98 (stride 0x20) · 크기: 32 · 앵커: +0
- 출처: W §3.2; DM 건축물 표
- 덤프 3,063개. 도시·관문·시설 모두 이 표. 시설 내구는 `1F42B0(건물,값)`(새 `1F5680`)이 설정(증감이 아니라 새 값).

| 오프셋 | 폭 | 이름 | 뜻 | 엔진 필드 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `+0x10` | u16 | tile | 위치(칸 번호) | Facility.tile | W §3.2; DM | 확정 |
| `+0x12` | u8 | type | 종류(시설 정의 id) | Facility.type | W §3.2 | 확정 |
| `+0x13` | u8 | owner | 세력(마스터 세력 ID) | Facility.force | W §3.2 | 확정 |
| `+0x14` | u16 | durability | 현재 내구(`1F42B0`이 씀) | Facility.hp | W §3.2; pre6_tactics §4 | 확정 |
| `+0x16` | u8 bit0 | complete | 완성 표지(내구가 최대에 도달하는 날 켜짐) | complete = hp >= FAC_DEF[type].hp | W §3.2 | 확정 |
| `+0x5F (정의/인스턴스)` | bit0 | blocking_done | 완성된 막는 시설 표지(건설 가능 판정 1항) |  | W §3.2 항1 | 확정(코드) |

### 3.6 AREA — 지역(AREA / REGION)

- RTTI `CAreaData` · 표: +0x6CAF0 · 크기: 152 · 앵커: +0x52 (에디터 기준점)
- 출처: DM 지역 표; W §1.1; DMs 수입식; L2
- 지역 소유 = 지역 중심 칸 `+0x3A`의 소유 세력(`22E260`/`22CC00` 계열). 지역 343개(0=무). 에디터 표의 '미확정' 구간 일부가 후속 조사로 확정됨.

| 오프셋 | 폭 | 이름 | 뜻 | 엔진 필드 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `+0x34` | u8 | city_circle | 도시권(에디터) |  | DM | 추정 |
| `+0x35` | u8 | home_base | 소속거점 |  | DM | 추정 |
| `+0x36` | u16 | officer | 지역 담당관 무장 | Data::region_officer | DM; command_audit #4 | 확정 |
| `+0x38` | bit 0x10 | facility_flag | 시설 플래그(연 4~5개 지역; 군량 수입 추가 150%) |  | DMs 수입식 | 확정(코드)/엔진 미반영 |
| `+0x3A` | u16 | center_tile | 중심칸 — 지역 소유 판정 기준 | Map::center | DM; W §1.1 | 확정 |
| `+0x3C` | u16 | commerce_progress | 상업 개발 진행값(단계1~5 조회) | Data::region_commerce | 능력치.md; L2 | 확정 |
| `+0x3E` | u16 | agriculture_progress | 농업 개발 진행값 | Data::region_agriculture | 능력치.md | 확정 |
| `+0x40` | u16 | barracks_progress | 병영 개발 진행값(징병 풀) | Data::region_barracks | 능력치.md; L4 case 0x13 | 확정 |
| `+0x42` | u16 | security_base | 치안 기준값 |  | DM | 추정 |
| `+0x44` | u16 | commerce_base | 상업 기준값(금 수입식 입력) | Map::commerce_base | DM; DMs 수입식 | 확정 |
| `+0x46` | u16 | agriculture_base | 농업 기준값(군량 수입식 입력) | Map::agriculture_base | DM; DMs | 확정 |
| `+0x48` | u16 | barracks_base | 병영 기준값(징병식 입력) | Map::barracks_base | DM; RULES.md 징병 | 확정 |
| `+0x4A` | u16 | gold_income | 지역 금 수입 저장칸(`2BBCB0` 호출자가 저장) | (파생) | DMs 4차 | 확정 |
| `+0x4C` | u16 | food_income | 지역 군량 수입 저장칸 | (파생) | DMs 4차 | 확정 |
| `+0x4E` | u16 | recruit_count | 모병 수 |  | DMs 4차 | 추정 |
| `+0x52` | u16 | population | 인구 | Data::population | DM | 확정 |
| `+0x54` | u8 | security | 치안(수입식 하한 50). `175DE0`(공격 후 효과)가 쓴다 | Data::security | DM; DMs; L2 2차 | 확정 |
| `+0x56` | u16[8] | adjacent_areas | 인접 지역 8칸 |  | DM; DF 인접효과 | 확정 |
| `+0x66` | u8 | adjacency_mask | 인접 효과 집계 마스크(통행금지 마스크 아님) | (미모형) | DM; DF 항 2B07C0 | 확정(집계 사용)/추정(비트 의미) |
| `+0x68` | u16 | owned_tiles | 지역 소유 세력이 가진 칸 수(중심 소유자와 같은 소유 칸). 343개 중 337 일치, 6개는 이민족·중립 지역 0 | Data::area_owned | W §1.1 | 확정 |
| `+0x6D` | u8 | reserved_6d | 지역 점령 확정 때 초기화(`1FD930`) |  | W §1.2 | 추정 |
| `+0x6E` | u8 | facility_cap | 지역 시설(클래스 2·3·4) 수 상한(0~27) | area_fac_cap.json | W §3.2 항5 | 확정 |
| `+0x72` | u8 | dev_direction | 개발 방향 | Data::region_direction | L2; sim.h | 확정 |
| `+0x76` | u16 | total_tiles | 지역 총 칸 수(343/343 일치) | Map::tile_count | W §1.1 | 확정 |

### 3.7 CITY — 도시(거점) 객체

- RTTI `CCityData` · 표: +0xDD38 · 크기: 360 · 앵커: +0x34
- 출처: DM 도시 표; pre6_occupation §0; L2 S1
- 관문(GATE)은 같은 표 형식의 변형(stride 0xC0). 덤프의 거점 블록과 같은 필드.

| 오프셋 | 폭 | 이름 | 뜻 | 엔진 필드 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `+0x2E` | u16 | governor | 태수 | Data::governor | DM | 확정 |
| `+0x30` | u8 | corps_slot | 군단 객체 슬롯(마스터 세력 ID 아님) | Data::base_corps | DM | 확정 |
| `+0x34` | u32 | gold | 금 | Data::gold | DM | 확정 |
| `+0x38` | u32 | food | 군량 | Data::food | DM | 확정 |
| `+0x3C` | u32 | troops | 병사(수비병) | Data::troops | DM | 확정 |
| `+0x40` | u32 | wounded_pool | 부상병 풀(거점) — 덤프 파서의 wounded_base | Data::wounded_base | pre6_occupation §용어; dump_measurements.md:69 | 확정(덤프) |
| `+0x44` | u8 | morale | 사기. `2BDCD0` 이 byte 로 읽는다(도시도 u8; 에디터의 u16 은 폭 선언 차이로 해소) | Data::morale | DM; L3b(`2BDCD0` 코드) | 확정 |
| `+0x46` | u16 | durability_cap | 내구 상한 | Data::maxhp | DM | 확정 |
| `+0x4E` | u16 | base_no | 거점번호 |  | DM | 확정 |
| `+0x50` | u16 | officer_alloc_50 | 부상병이 아니다. 부상병 풀은 `+0x40`(`2BDCD0`: 풀을 병력 `+0x3C` 로 전환·사기 `+0x44` 혼합). 에디터의 '부상병' 선언은 오류로 해소 | | DM; dump_measurements.md:69; L3b | 확정 |
| `+0x58` | u8[10] | adjacent_bases | 인접거점 슬롯(u16[10] 아님) |  | DM 정정; city_attack_routes | 확정 |
| `+0xB8` | u8 | size | 규모 1..4(시나리오 이벤트 `3AB400`/`3B3B60`로 성장). 병력·금·군량 상한 기준(`269760`) | base_size() | L2 S1 | 확정 |
| `+0xCA` | u16 | recruit_officer | 모병담당 | Data::recruitment_officer | DM | 확정 |
| `+0xCC` | u16 | training_officer | 훈련담당 | Data::training_officer | DM | 확정 |
| `+0xCE` | bytes | tribe_type | 이민족 부족 유형 |  | CA #f 도적 | 추정 |
| `+0xCF` | u8 | recruit_turns | 모병 순수(1일 0, 11일 1, 21일 2) | Data::recruitment_turns | RULES.md 징병 | 확정 |

### 3.8 GATE — 관문 객체

- RTTI `CGateData` · 표: +0xDED8 · 크기: 192 · 앵커: +0x0
- 출처: DM 관문 표
- 도시와 유사. 관문 id 0x34~0x3D, 거점번호 +0x10.

| 오프셋 | 폭 | 이름 | 뜻 | 엔진 필드 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `+0x10` | u8 | base_no | 거점번호 |  | DM | 확정 |
| `+0x12` | utf16[16] | name | 이름 |  | DM | 확정 |
| `+0x2E` | u16 | governor | 태수 |  | DM | 확정 |
| `+0x30` | u8 | corps_slot | 군단 객체 슬롯 |  | DM | 확정 |
| `+0x3C` | u32 | troops | 병사 |  | DM | 확정 |
| `+0x44` | u8 | morale | 사기 |  | DM | 확정 |
| `+0x46` | u16 | durability_cap | 내구상한 |  | DM | 확정 |
| `+0x50` | u16 | officer_alloc_50 | 도시와 같음: 부상병 아님(관문도 부상병 풀은 `+0x40`) |  | DM; L3b | 확정 |

### 3.9 FORCE — 세력 객체

- RTTI `CForceData` · 표: +0xDF30 · 크기: 616 · 앵커: +0x0
- 출처: DM 세력 표; difficulty.md; command_audit; worldmap_spec §2
- 세력 id 1..51(0x33 중립, 0x2E~0x32 이민족). 동맹 바이트는 `+0xEA+상대`(코드) / 에디터 `+0xEB`.

| 오프셋 | 폭 | 이름 | 뜻 | 엔진 필드 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `+0x10` | u16 | ruler | 군주 | Data::ruler | DM | 확정 |
| `+0x12` | bit8 | flag_divination | 세력 플래그(비트8: 점술 개성 분기) |  | L1 개성 67 | 추정 |
| `+0x14` | u8[51] | friendship | 우호도 0..200(변경 함수 `2719C0`→`25A080` 한 곳) | Data::friendship[NF*NF] | DM; CA #13~14 | 확정 |
| `+0x47` | u8 | rank_title | 작위(계급 표 +0xAD+idx로 직위 항) |  | DMs; DM | 확정 |
| `+0x48` | u8 | kingdom_name | 국호 |  | DM | 확정 |
| `+0x49` | u8 | color | 세력색 | Data::color | DM | 확정 |
| `+0x4A` | s8 | force_purpose | 세력 행동방침(-128..127; 판단표 노드 CForceSetPurposeNode `56A40` 이 쓴다. 세력 판단표 N146~N154 가 0~3 을 정함, 군단 판단표 N673~N680 이 0/1/2/3 으로 군단 방침 기준값 62/15/5/목록길이를 고름. 조건 25) |  | L3b(`56A40`·`AED60` 코드) | 확정 |
| `+0x4B` | s8 | force_aux | 세력정보 항목 1 이 읽는 부호 있는 바이트(`232F50`). 군단 판단표 N667 이 읽음. 쓰는 곳·의미 미확인 |  | L3b(`8CAE0` case 1) | 확정(위치)/미해결(의미) |
| `+0x4C` | u32? | rerequest_date | 공격 요청 60일 재요청 제한 날짜(사람 플레이어만, `235150`) | (시뮬 해당 없음) | CA #15 | 확정 |
| `+0x52` | u16 | advisor | 군사 | Data::advisor | DM; sim.h | 확정 |
| `+0x54` | 5 x 0x1E B rows | government_rows | 시정 5줄(시정 대기·활성) | Data::government_officers/wait | sim.h; DMs H | 확정 |
| `+0xEA` | u8[51] | alliance_bytes | 동맹·정전·속국 관계 바이트: 하위 7비트=개월(0이면 비동맹). `+0xEA+상대` | Data::alliance_until | W §2.1; CA 시간 경과 | 확정(코드) |
| `+0xEB` | u8[51] | alliance_editor | 에디터가 적은 동맹 위치 = 같은 배열의 세력 번호 1 원소(배열 기준 `+0xEA`, 원소 = `+0xEA + 상대 세력 번호`, 번호 0 은 미사용). 조건 16(AA930)이 `+0xEA + 번호` 를 읽는다. 어긋남 해소 |  | DM; L3b(조건 16 코드) | 확정 |
| `+0x120` | u16[31] | tactic_book_stock | 전법서 재고(idx 1..30; 에디터는 +0x122 u16[30]) | Data::force_book | CA #23; DM | 확정(+0x120 idx1=+0x122) |
| `+0x15E` | u8 | water_ship_tier | 세력 기본 수상 진형/수군 단계. `2C8AB0`(격류 통과)이 12·13·17·18만 허용하고 14는 거부. **덤프 상관(2026-11-08)**: 대부분 세력은 11(주가)이고, 세력 8이 1960111에 11→12가 되자 이후 부대 수상 진형 `+0x1C`가 11(주가)에서 12(몽충)로 바뀌고, 세력 1·3·8·23·35는 13(누선)까지 오른다 |  | W §1.2; 덤프 | 추정(강한 상관) |
| `+0x15F` | u8 | atkreq_from | 공격 요청 보낸 세력(요청받은 세력 쪽에 기록) | Data::atkreq_from | sim.h S11 | 확정 |
| `+0x160` | u8 | atkreq_base | 공격 요청 대상 거점 | Data::atkreq_base | sim.h | 확정 |
| `+0x164` | u32 | ideology_exp | 사상경험치(에디터) | Data::force_ideology_exp | DM | 추정 |
| `+0x184` | u16[5] | tribe_intimacy | 이민족 5부족 친밀(0..1000) | Data::tribe_fav | CA #b 교역; sim.h S16 | 확정 |
| `+0x18E` | u8[5] | tribe_state | 이민족 5부족 상태 | Data::tribe_state | sim.h | 확정 |
| `+0x17A` | u8[5] | target_forces | 공략 대상 세력 5칸(세력 번호, 0 이면 없음). 판단표 노드 CSetTargetForceListNode(`58C90`)가 쓰고 CClearTargetForceListNode(`52950`)가 비운다. 세력정보 항목 6 = 첫 칸, 항목 27 = 목록 | | L3b(`58C90` 코드) | 확정 |
| `+0x17F` | u8[5] | friend_forces | 친선 대상 세력 5칸. CSetFriendForceListNode(`58B90`)가 쓰고 `52910` 이 비운다. 세력정보 항목 7 = 첫 칸 | | L3b(`58B90` 코드) | 확정 |
| `+0x218`/`+0x228`/`+0x238` | list ptr | foothold_lists | 세력이 보관하는 거점 목록 3종(세력정보 항목 19/21/33). 이름 추정 | | L3b(`8CAE0`) | 확정(위치)/추정(이름) |
| `+0x193` | bits | force_flags | 비트1: 진형 5 기동 +2, 비트2: 진형 5 +5, 비트3: 수상 기동 항 등 | Data::force_flags | DMs 175~; DF | 확정(비트 사용)/추정(의미) |
| `+0x194` | holder | subject_of | 속국 관계 보유(이민족 복속) | Data::subject_of | W §2.1; sim.h | 확정 |
| `+0x1BE` | s16 | force_pexp | (±1000) `2255F0` 호출 22곳, 단계표 `1413A9DDC` — 의미 미정 | Data::force_pexp | CA 15절 | 미해결 |
| `+0x1CB` | u8[10] | policy_got | "획득한 항목" 비트열(비트 = 효과 id-1). 일반 세력은 다수 비트, 이민족은 비트 0만(L2 4차 덤프). 쓰는 곳 `2EF700` 하나, 읽는 곳 `22DB30`(비정책 효과 값 = `world+0x85F20[id]+0x44`) |  | L1 2·3차; L3b | 확정 |
| `+0x1D5` | u8[10] | policy_mask | 효과 마스크(`+0x1CB` 와 짝) |  | L1 2차 | 확정 |
| `+0x1DF` | u8[10] | policy_unlock | 해금 비트열(`2EF700` 이 씀) |  | L1 3차 | 확정 |
| `+0x1C5` | u8 x6 | doctrine_gain | 주의 경험 슬롯 6칸(+0x1C5+종류-1, 상한 99, `1DF490`이 가산) |  | CA 15절; L1 4차 | 확정 |

### 3.10 CORPS — 군단(District)

- RTTI `CDistrictData` · 표: +0xE0D0 · 크기: 48 · 앵커: +0x10
- 출처: DM 군단 표; RULES.md S9; L4
- 세력 id는 +0x10. 명령서 +0x14는 군단 객체에 있다(DESIGN.md:75).

| 오프셋 | 폭 | 이름 | 뜻 | 엔진 필드 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `+0x10` | u8 | force | 세력 | Data::corps_force | DM | 확정 |
| `+0x11` | u8 | order | 순서 |  | DM | 확정 |
| `+0x12` | u16 | leader | 군단장 | Data::corps_governor | DM | 확정 |
| `+0x14` | u8 | order_count | 명령서(1장 소비해 출진 등) | Data::corps_orders | DM; DESIGN.md:75 | 확정 |
| `+0x15` | s8 | action_setting | 군단 행동방침 0/1/2: 판단표 노드 CDistrictSetPurposeNode(`36D00`)가 쓴다(군단 판단표 N705~N720). UI 설정 아님. 규칙 효과 없음 | Data::corps_action_setting | CA #25; L3b | 확정 |
| `+0x17` | u8 | delegation | 위임방침: 1 전체위임, 2 세력공략, 3 거점공략, 4 내정, 5 지원(msggame_exce 41241 순서; 1·5 는 조건 160 코드 확인, 2~4 순서 추정). 조건 110 의 n = 값 - 1 | Data::corps_delegation | CA #25; L3b | 확정(1·5)/추정(2~4) |
| `+0x1B` | u8 | permissions | 권한 설정(실행허가행동 일부; 조건 108 이 bit2~6 = 항목 0~4). 군단 초기화 `2F02E0` 이 0xFF | Data::corps_permissions | CA #25; L3b | 확정 |
| `+0x1C` | u32 bits | permissions2 | 권한 비트 하위 31비트(조건 108 의 항목 5~). `2F02E0` 이 31비트를 모두 1 로 | | L3b(`2F02E0`) | 확정 |
| `+0x20/+0x21/+0x22` | u8 x3 | priority_levels | 물자 확보 수준 3종(0 보통, 1 많이, 2 적게; 군단설정 항목 0 = +0x20 금(필요 금 6/8/4), 항목 1 = +0x22 (병사로 추정), 항목 2 = +0x21 군량(군량 인수 6/8/4)). 초기화 `2F02E0` 이 0. 화면 "중시항목"/물자에 대응 | | L3b(조건 111, rulebase N11~N24) | 확정(위치·값)/추정(항목 이름) |
| `+0x18` | u8 | goal | 위임 목표 번호(위임방침 5 지원이면 목표 군단 번호). 에디터 "목표" | | DM; L3b(조건 160 `A4960`) | 확정 |
| `+0x19` | u8 | goal_kind | 위임 목표 종류(8 = 군단) | | L3b(조건 160) | 확정(값 8)/추정(다른 종류) |
| `+0x16` | s8 | corps_aux | 군단정보 항목 1 이 읽는 부호 있는 바이트(`2327F0`). 쓰는 곳·의미 미확인 | | L3b(`88780` case 1) | 확정(위치)/미해결(의미) |

### 3.11 ARMY — 부대(Unit)

- RTTI `CArmyUnitData` · 표: +0x7E838[501] · 크기: 512 · 앵커: +0x0
- 출처: DM; W §0~4; dump_measurements; lane_L4; command_audit; approx_inventory
- 덤프 종류 `+0x10`: 1 전투 부대(진형 1~10·14), 2 수송(진형 19). 엔진 Unit.kind==1이 수송(`g1_replay.doc_from_turn`이 2→1). 목록 `+0xF0`(소멸 부대 정리), `+0x70`(부대 목록).

| 오프셋 | 폭 | 이름 | 뜻 | 엔진 필드 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `+0x10` | u8 | kind | 1 전투 / 2 수송(11도 유효 부대) | Unit.kind (2→1) | W 용어; L4 | 확정 |
| `+0x12` | u16 | commander | 대장(무장 id) | Unit.officer | DM | 확정 |
| `+0x14` | u16 | move_accum | 이동 누산기(상한 1000). `2DB9A0`이 `269150`(새 26AB00) 점수를 더함 | Unit.mp | W §4.2; DMs | 확정 |
| `+0x16` | u16 | troops | 병사 | Unit.troops | DM | 확정 |
| `+0x18` | u16 | wounded | 부상병 | Unit.wounded | DM | 확정 |
| `+0x1A` | u8 | morale | 사기(0이면 즉시 격파 `25A880`) | Unit.morale | DM; L4 U8 | 확정 |
| `+0x1B` | u8 | land_formation | 육상 진형(+0x1C 수상 진형과 둘 다 보유) | Unit.formation | DM; W §4.5 | 확정 |
| `+0x1C` | u8 | water_formation | 수상 진형(11 주가, 12 몽충, 13 누선, 17·18·20 수송 수선) | Unit.wform | W §4.5 | 확정 |
| `+0x1D` | u8[3] | tactics | 보유 전법 |  | DM | 확정 |
| `+0x20..+0x22` | bytes | state_bytes | 전법 관련 상태 바이트 3종. **쓰기 지점 확정(2026-11-08)**: `173DD0`(AI 전법 선택)·`174F40`(전법 실행)이 대상 부대마다 `부대 + 0x20 + i`(i=0..2)에 값을 쓴다(디컴파일 표기는 `lVar9 + 0x20 + lVar11`). 값은 `clamp(...)`: **i=0** = `clamp(진형 보정 − 세력 보정 + 참가 부대 전법 객체 +0x42(wait 추정) 평균, 0, 100)`(2026-11-17 정정: 평균 피해 아님). 출진 `2D4C80` 초기값은 40 + 진형 보정 − 세력 보정 / 150 / 200이고 진형 보정은 진형 1 → +8, 진형 2/14 → −8, 그 밖 0(`141A4C004/00C/014`, 판정 `22CB80`), 세력 보정은 대상 세력 `+0x193 & 0x40`이면 4(`141A4BC6C`). **i=1/2**는 상한 상수 `141A4B0D4`=150·`141A4B0E0`=200. 읽기: `170150` 5번째 검사 `+0x20==0`, `17E810` 동일, `16E820`은 `+0x21≠0 → 1.0`, `+0x22≠0 → 1.4`, 둘 다 0 → 1.8. **덤프 확인**: 2090211 턴 30부대 중 23부대가 `+0x21=150`·`+0x22=200`, `+0x20`은 0(26부대)·8·18·34. 다음 턴(2090221)에는 `+0x20`만 전부 0으로 돌아오고 `+0x21`/`+0x22`는 같은 23부대가 150/200을 유지한다 → `+0x20`이 먼저 낮아진 표본이다. `3045F0 → 225710`이 낮춘다: `+0x20`은 병참 연결 때 하루 −4, `+0x21/+0x22`는 지휘무장만(rules_combat_effects.md E1 "전법 게이지 일생"·전법 게이지 감쇠) |  | L3 C4; `173DD0`·`174F40`; 덤프 2턴 | 확정(쓰기·값·지속) |
| `+0x23` | u8 | st_confusion | 혼란 게이지(0..120, 단절 시 일 -4) | Unit.st_conf | W §2.2; DM | 확정 |
| `+0x24` | u8 | st_halt | 저지(에디터 '정지') 게이지 | Unit.st_halt | W §2.2 | 확정 |
| `+0x25` | u8 | st_taunt | 도발 게이지(대상 필드 별도) | Unit.st_taunt | CA 3·15 | 확정 |
| `+0x26` | bits | flags | bit1 병참 연결(1=연결), bit2 자주퇴각, bit3 추격 옵션 | Unit.supply | W §2.1; L4 | 확정 |
| `+0x2A` | u16 | tile | 위치(칸 번호 y*220+x) | Unit.tile | W §0.1 | 확정 |
| `+0x2C..+0x34` | u16[5] | relay_tiles | 경유지 칸 5개(2F05A0이 채움). 군세 +0x18 목록과 다른 자료 | Unit.relay[5] | DM; sim.h | 확정 |
| `+0x36` | u8 | facing | 방향 1..6(2A9910 번호), 몸 모양 칠하기 `18A190` | Unit.facing | sim.h S1 | 확정 |
| `+0x37` | u8 | act | 행동(8 건설, 9 이동 후 건설, 10 지역 점령형, 0xB/0xC 퇴각 등) | Unit.act | W §3.2; L4 | 확정 |
| `+0x38` | u8 | target_kind | 목표 종류(5 도시, 6 관문, 9 칸, 0xB 지역, 0x1B 부대) | Unit.pkind | L4 | 확정 |
| `+0x3A` | u16 | target | 목표 id(<501이면 부대) | Unit.pid | L4 | 확정 |
| `+0x3C/+0x3E` | u8+u16 | post_target | 사후 목표(L4) / 도발 시전자(종류·id)(L2 2·3차 덤프 대조). 부대정보 항목 9/10 이 `+0x3C` byte, `+0x3E` u16 으로 읽는다. 두 해석이 같은 칸이며 충돌 S17 로 기록 |  | L4; L2 2·3차; L3b | 확정(위치)/충돌(의미) |
| `+0x40` | u8 | option | 접근 시 반응 옵션 0·1·2. 2일 때만 `273AC0`이 3칸 안 적을 모아 교전(`2B76B0`→`2903E0`). 컴퓨터 출진 기본값은 1(`43A50`). 1·2는 전법 피해식 `177B30`의 정책 0x20/0x21 보정 선택에도 쓰임 |  | L4; ai/roles.md 6-4 (디컴파일 2026-11-12) | 확정 |
| `+0x41` | u8 | post_order | 사후 명령(1 퇴각 `2EC570`, 2 주둔) |  | L4 | 확정(판단 영역) |
| `+0x42` | u16 | build_tile | 건설 칸 |  | W §3.2 | 확정 |
| `+0x46` | u8 | build_kind | 건설 시설 종류 | Unit.build | W §3.2 | 확정 |
| `+0x48` | u16 | next_tile | 다음 칸(막히면 0xBD10). 출진 때는 `1EDC30`이 성 → 목적 칸 경로의 성 밖 첫 칸을 쓴다(출진 명령 `[24]`도 같은 칸) |  | W §4.1; DM; ai/roles.md 6-3 | 확정 |
| `+0x152` | u16 | origin_tile | 출진 때 `+0x2A`와 함께 출발 성 칸으로 초기화(`2D4C80`). 이후 용도 미확인 |  | ai/roles.md 6-3 (디컴파일 2026-11-12) | 확정(쓰기)/미확인(용도) |
| `+0x4A+i` | s8[5] | ability_level | 전법 능력 변경 단계 -10..10 (i=0 이동, 1..4 공격·공성·방어·파성) | Unit.lv[5] | CA §12 | 확정 |
| `+0x4B..+0x4E` | s8 | temp_modifiers | 공군/공성/방어 입력 일시보정 후보(+0x4B 공군 2B21A0, +0x4C 공성 2B2440, +0x4D 방어 2A9E50) |  | DM 추가 관측 | 확정(읽기)/추정(의미) |
| `+0x50+i` | u8[5] | ability_duration | 능력 변경 남은 기간 0..240(0xF0) | Unit.ld[5] | CA §12 | 확정 |
| `+0x54` | u8 | (오표기 정정) | difficulty.md·RULES.md는 '소속 부대 +0x54 최저치'로 적었으나 command_audit §4는 같은 입력을 '지역 치안 +0x54(지역 +0x52 인구·+0x54 치안)의 최저값'으로 정정. 부대 +0x54의 독립 의미는 확인되지 않음 |  | DF 항 44; CA §4 | 충돌(정정본: 지역 치안) |
| `+0x58` | u16 | troops_id | 소속 군세 ID(에디터의 출발도시 u8 주장은 폐기) |  | DM 정정 | 확정 |
| `+0x64` | 36 slots | trait_slots | 부대 개성 슬롯 36칸(무장 개성과 합산해 127칸) |  | L1 `26BBE0` | 확정 |
| `+0x13C` | index | retreat_index | 퇴각 재지정 색인(표 0x84BC8) |  | L4 A5 | 추정 |
| `+0x140..0x142` | bytes | pending_cmd | 보류 명령(`2E3BC0`이 행동·목표로 확정) |  | L4 case 4 | 확정 |
| `+0x1F0` | u32 | ai_flags | 개별 AI 플래그, bit3=병참 단절 후보 |  | DM 추가 관측 | 추정 |
| `+0x1F4` | i32 | cut_target | 병참 절단 대상 부대 번호 후보 |  | DM | 추정 |
| `+0x1F8` | u16 | goal_tile_cache | 경로 재구성 `303EA0` 이 경로 끝 칸(없으면 0xBD10)을 쓰고 읽는 목적칸 캐시. 에디터의 "목적칸"과 같은 용도(해소) |  | DM; approx_inventory A2; L3b(`303EA0` 코드) | 확정 |

### 3.12 TROOPS — 군세(Troops)

- RTTI `CTroopsData` · 표: +0x7F8D8 (id 조회표) · 크기: - · 앵커: +0x0
- 출처: DM 추가 관측 (siege_logistics/분석근거.md)
- 행동트리 컨텍스트와 방식을 가진 군세 객체.

| 오프셋 | 폭 | 이름 | 뜻 | 엔진 필드 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `+0x14` | u16 | mode | 군세 행동 방식(5 건설 군세, 8/9/10/11/22 편성 방식) |  | DM; worldmap_spec §3.2 | 확정 |
| `+0x16` | u16 | target_id | 군세 목표 ID(방식에 따라 거점/토지) |  | DM | 확정 |
| `+0x18` | u16[10] | area_list | 동적 지역처리 목록: 중심 HEX(고정 도시쌍 경유 표 아님) |  | DM | 확정 |
| `+0x30` | u64 ptr | bt_context | 행동트리 실행 컨텍스트 후보 |  | DM | 추정 |

### 3.13 PERSON — 무장(Person)

- RTTI `CPersonData` · 표: +0x73A50 · 크기: 496 · 앵커: +0xEC
- 출처: DM 무장 표(memschema 선언), command_audit, lane_L1/L2, sim.h
- 에디터 레코드 stride 496, 앵커 +0xEC(능력 5개 u8). 파일 저장 스키마(402B)와 메모리 객체(0x1F0)는 다른 배치.

| 오프셋 | 폭 | 이름 | 뜻 | 엔진 필드 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `+0x10` | u16 | game_id | 게임ID | Data::person_id | DM | 확정 |
| `+0x12` | utf16[14] | surname | 성(+0x20 명, +0x2E 자, +0x34 이름[24]) | person_name | DM | 확정 |
| `+0xA6` | u16 | portrait | 모습 |  | DM | 확정 |
| `+0xA8` | u16 | join_year | 임관 |  | DM | 확정 |
| `+0xA9` | u8 | gender | 성별(0 남 1 여; 개성 조건 21/22) | person_gender | sim.h S18 | 확정 |
| `+0xAA` | u16 | appear | 등장 연도(덤프 1,400명 대조: 시나리오 +0xD9 와 같은 값) | person_appear | DM; L1 3차 | 확정 |
| `+0xAC` | u16 | birth | 생년 | person_birth | DM | 확정 |
| `+0xAE` | u16 | death | 졸년 | person_death | DM | 확정 |
| `+0xB0` | u8 | death_kind | 사인 구분(0 / 1). 1이면 졸년 + 10~13년 사망, 질병 발병 임계 +10(`26B920`). 기존 표는 u16 death_cause 로 선언했으나 런타임 값은 0/1뿐이고 시나리오 `+0xDF` 와 1,400/1,400 일치 |  | L1 3차(덤프 + `26B920`) | 확정 |
| `+0xB2` | u16 | clan | 씨족 | person_clan | sim.h R7 | 확정 |
| `+0xB4` | u16 | father | 부 | person_father | sim.h | 확정 |
| `+0xB6` | u16 | mother | 모 | person_mother | sim.h | 확정 |
| `+0xBA` | u16 | spouse | 배우자 | person_spouse | sim.h | 확정 |
| `+0xBC` | u16 | sworn | 의형제 그룹 | person_sworn | sim.h | 확정 |
| `+0xBE` | u8 | affinity | 상성(0~149). 무장정보 항목 4 가 byte 로 읽는다. `2A8010` 상성 격차(원형 거리 최대 75), `2A8C90` 등급 경계 11/30/47 | | DM; L3b; L2 3차 | 확정 |
| `+0xC0` | u16[8] | favorites | 친애(애호 목록) | person_fav | DM | 확정 |
| `+0xD0` | u16[8] | hate | 혐오 | person_hate | DM | 확정 |
| `+0xE0` | u8 | corps_slot | 군단 객체 슬롯(마스터 세력 ID 아님) | person_force | DM | 확정 |
| `+0xE2` | u16 | home_base | 소속 거점/등장도시. 병참 연결 판정의 출발 거점(`2AB620`) | Unit.source | W §2.1; DM | 확정 |
| `+0xE4` | u16 | location | 현재 위치 | person_location | DM | 확정 |
| `+0xE6` | u8 | status | 신분(1 군주, 4/2/3/6 등) | person_status | CA 충성; DMs | 확정 |
| `+0xE7` | u8 | post | 관직(관직 표 인덱스) | person_office | DM; DMs | 확정 |
| `+0xE8` | u8 | loyalty | 충성 | person_loyalty | DM; CA | 확정 |
| `+0xEC..+0xF0` | u8 x5 | abilities | 통솔·무력·지력·정치·매력(실효값은 `231770`/옛 22FCE0 경유) | person_leadership/strength/intelligence/politics/charm | DM; 능력치.md | 확정 |
| `+0xF2` | u8[5] | growth_room | 성장여유 |  | DM | 확정 |
| `+0xF8` | u16[5] | ability_cap | 능력상한 |  | DM | 확정 |
| `+0x104` | u32[5] | exp | 경험누계 |  | DM | 확정 |
| `+0x118` | u16[9] (traits9 이전 5) | traits | 개성 | person_traits | DM; WB §5.2 | 확정 |
| `+0x12C` | u32 | formation_mask | 진형 | person_formation_mask | DM | 확정 |
| `+0x130` | u8[10] | tactics | 전법 id 바이트(표 +0x774D0) | person_tactics | DM; CA #23 | 확정 |
| `+0x14C` | u8 | principle | 주의(신념) | person_principle | DM | 확정 |
| `+0x14D` | u8 | policy | 정책 | person_policy | DM | 확정 |
| `+0x15E` | u16 bits | flags | 시나리오 속성 플래그: 비트 5(0x20) 위임 중 전법 사용 불가(`170216`에서 검사, 사유 `0xC964`), 비트 13 충성 255 고정(`1FEF60`), 비트 14 연계 불참(조건 159), 0x8000 acted(포상 실행 `1ED620`·`1ED8F0` 이 set), 0x4000 이탈 등급(`335C20` set), 0x6000, 비트 0 = 무장정보 항목 12. **L3 5차 추가 비트**: 비트 10(0x400) = 건강 틱 면제(발병 `26B920`·빈사 사망 `26B500`·`345D00`·`3566E0` 이 `&0x400==0` 을 요구; `2E46F0` 이 비트 13 이 켜진 무장(ID 3001~3150 밖)에 set, `229820` 이 ID 5101~5200 에 0x600 을 set), 비트 9(0x200) = 가공·특수 무장 표식(`229820` 이 ID 5101~5200 에 비트 9·10 동시 set; `2FAFD0` 등용 가능 판정·`2FA7C0` 이 읽음, 등용·인발 대상 제외 계열 추정), 비트 7(0x80) = 신규 합류·생성 직후 표식(`29FB50` 무장 생성/편입·`273100` 임관 처리가 set; 목록 정렬 `3BAC00`·`3C0A90`·`3DFDD0` UI 가 읽음, 추정), 비트 4(0x10) = 이번 등용 실패 표식(`2FC080` 이 `279DE0`==0 일 때 set; UI `66B850`·`672450` 이 읽음, 추정), 비트 3(0x8) = 건강 계열(`26B3F0`·`27E480`·`2CB210` 이 발병·행동 계산에서 읽음, 의미 추정), 비트 11(0x800)(`20B640` 이 set, `36BF30` 이 읽음, 의미 미확인) | person_pflag | L3 C3; CA 15절; DMs; L2 2차 | 확정(일부 비트)/추정 |
| `+0x161` | u8 | injury_grade | 건강·부상 등급 0~3 -> 능력 계수 100/80/50/20 %. 질병 틱 `27E480` 이 1/2 를 쓰고 읽으며 월 경계에서만 바뀐다 |  | DMs; L2 C12; L1 3차 | 확정(코드)/엔진 일부 |
| `+0x162` | u16 | prev_lord | 옛 군주(무장 id). 등용 평가 `279DE0` 이 `+0x162 == 등용하는 군주 id` 이면 등용 불가로 처리하므로 "옛 군주"(L1 2차)가 맞다. 에디터의 "사관금지" 명칭은 해소 | | DM; L1 2차; L3b 3차(`279DE0`) | 확정 |
| `+0x164` | u16 | ban_period | 금지기간(월 1일에만 -1) |  | DM; DMs | 확정 |
| `+0x166` | u16 | join_year_lord | 현재 군주 임관 연도 | person_rel_year | sim.h S11 | 확정 |
| `+0x168` | u8 | captive_months | 포로 보유 개월(포획 0, 월 1일마다 +1, 1 초과부터 탈출 판정 `2A1530`/`2694A0`) |  | L1 2차(덤프 추적 + `2694A0`) | 확정 |
| `+0x16A..+0x180` | s16[12] | aptitude | 적성·내면 값 12칸(-20..20; 시나리오 무장 표 +0x114 `aptitude i16x12` 와 같은 값). 판단표 무장정보 항목 13~20·31·32·34·35 가 읽는다(순서: +0x16A=13, +0x16C=14, +0x16E=15, +0x170=16 ... +0x178=20, +0x17A=31, +0x17C=32, +0x17E=34, +0x180=35). **이름 대응(L3b 3차)**: 정책 선택 비교자 `6B5980` 이 정책 분류 3/4/5/6 에 칸 {max(0, 9)} / 10 / 2 / 11 을 쓴다(분류 3 = 군사 정책 -> 칸 0 호전·칸 9 야망, 4 = 책략 정책 -> 칸 10 책략, 5 = 내정 정책 -> 칸 2 내정, 6 = 정령철저·태학 계열 -> 칸 11). 칸 1 의리, 칸 8 한조(`2FA7C0` 이탈 판정), 칸 7 외교(포로 처분 생존 확률 칸 7+80), 칸 3·4·5 물자(금·군량·병사 = 지역 개발 가중 상업·농업·병영), 칸 6(+0x176)은 **건설이 아님**(L3 5차: +0x176 읽는 코드는 `AD4E0`(군주 칸6+칸2 > 29 이면 이탈 임계 +1)·`2FA7C0`(대상 칸6+칸2 < 11 이면 50% 분기)·`2FAFD0`(칸 6 단독 비교)·판단표 등용 평가 수식뿐이고 건설·개발 경로는 읽지 않는다) -> 이름은 "등용·충성 계열 성향" 후보(낮음). 칸 3~5 만 개발성향(판단표 항목 16~18). 이름은 추정(칸 0·1·7·8·9·3~5 높음/중간, 2·10·11 중간, 6 낮음). `+0x16C/+0x17C` 는 충성 하락 몫(-20/-10/0/+10) 판정에도 쓰이는 공감값 2종 | person_rel16/17 | sim.h S11; DM; L3b | 확정(위치)/추정(이름) |
| `+0x182` | u16 | policy_level | 정책 Lv | person_policy_level | DM | 확정 |
| `+0x184` | bits | trait_flags | 개성 비트 마스크(`26C070`이 사용) |  | L1 | 추정 |
| `+0x1C6/+0x1C7/+0x1C8` | u8 x3 | poach_mark | 인발 표식(시전 세력, 30, 60). `1FEF60`(계략 0x18)이 쓴다. **2026-11-08 보강**: `+0x1C7`은 **남은 일수**로 날짜 상태기계 case 2 `458520`이 매일 `141A4BDE0`(=1)씩 빼고, 0이 되면 `+0x1C6`을 0으로 지운 뒤 msggame_exce `0x34C5`/`0x34C6`("…비어가 해소되어 출진가능")를 띄운다. 즉 이 표식의 게임 용어는 **비어(유언비어)**이며 효과는 출진 불가다(기간 상수 `141A4B6E4`=30) |  | L2 2차; `458520`·메시지 표 | 확정(타이머) |
| `+0x1E8` | u32 | duty_limit | 담당 직무 한도(무장정보 항목 37). 현재 직무 수(`2ABF60(무장,2)`) + 1 <= 한도이면 직무 추가 가능(`43800`, 항목 38). 조건 32 와 같은 묶음 | | L3b(`8F810` case 36~38; `43800`) | 확정(위치)/추정(의미) |
| `+0x1BC` | u8 | rank | 공적 등급(위계 0..6) | person_rank | DM; sim.h S16 | 확정 |
| `+0x1BE` | s16/u16 | merit | 공적(-1000..12000). 에디터 u16 vs 헤더 i16: 부호 미검증 | person_merit | DM 정정·충돌; sim.h | 확정(범위)/미해결(부호) |
| `+0x1C0` | s16 | pending_score | 대기 점수(AddMerit `16A4E0`이 더함, /10 환산) | person_pend | CA 15절 | 확정 |
| `+0x1C2/+0x1C3` | u8 x2 | rank_bonus | 위계 배분(지휘병사 500/500/1000; 담당 지역 +1/+1) | person_bonus | CA 15절 | 확정 |
| `+0x1EC/+0x1ED` | ... | ability_cap_fields | 능력 상한 필드(+0x1ED 매력, +0x1EC 그 외; 가상 getter +0x48로 평가) |  | 능력치.md | 확정 |
| `+0xF1` | u8 | duel_hp | 단기접전 체력(0..100) |  | L2 4차 | 확정 |

### 3.14 FORMATION — 진형

- RTTI `CFormationData` · 표: +0x77428[21] · 크기: 200 · 앵커: +0x0 (fixdata 레코드 = 객체 -0x10, 152B, 본문 0x2D419+id*152)
- 출처: formation_mapping.md; W §4.5; DMs 175~; formation.json
- 진형 id 1~21. 길 찾기가 부대 +0x1B/+0x1C로 인덱스. 객체 오프셋 = fixdata 레코드 오프셋 + 0x10.

| 오프셋 | 폭 | 이름 | 뜻 | 엔진 필드 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `+0x7E (레코드 +0x6E)` | u8 | water | 1 육상, 2 수상 진형 | Map::formation_* | W §4.5; DM | 확정 |
| `+0x7F (레코드 +0x6F)` | u8 | mobility | 기동(어린 14, 학익 20, 봉시 26 ...; 수상 주가 10, 몽충 20, 누선 30) | Map::formation_mobility | DMs 176 | 확정 |
| `+0x80/+0x81 (레코드 +0x70/+0x71)` | u8 x2 | footprint_thresholds | 점령폭 3/5 병력 임계(x100). `2AF740` | Map::formation_n0/n1 | sim.h S1 | 확정 |
| `+0x83 (레코드 +0x73)` | u8 | attack_unit | 공군(대부대 공격). getter `2B2720`(새 2B4AA0), 동적 1..45 | Map::formation_attack | formation_mapping.md | 확정 |
| `+0x84 (레코드 +0x74)` | u8 | attack_siege | 공성. getter `2B2690`(새 2B4A10), 1..70 | Map::formation_siege | formation_mapping.md | 확정 |
| `+0x85 (레코드 +0x75)` | u8 | attack_demolish | 파성. getter `2B27B0`(새 2B4B30), 1..60 | Map::formation_demolition | formation_mapping.md; DMs 80 | 확정(getter)/추정(옛 REA 후보) |
| `+0x86 (레코드 +0x76)` | u8 | defense | 방어. getter `2A9DC0`(새 2AC010), 1..40 | Map::formation_defense | formation_mapping.md | 확정 |
| `+0x9A` | u16 | cost | 비용 | Map::formation_cost | DM | 확정 |
| `+0xA6` | u8 | ranged | 원거리(누선만 1) | Map::formation_ranged | DM; W §4.5 | 확정 |

### 3.15 TACTIC — 전법(fixdata 표 12)

- RTTI `CTacticsData` · 표: +0x774D0 (201칸) · 크기: 94 B · 앵커: 본문 0x2E099 (0010_KO/fixdataexce.s14)
- 출처: WB §5.1; appendix_tactics.md
- id 1..200(201칸, 0 무효). 이름 있는 것 196. `tools/extract/fidelity_tables.py`가 data/tables/tactic.json으로 추출.

| 오프셋 | 폭 | 이름 | 뜻 | 엔진 필드 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `(이름)` | utf16 | name | 이름 |  | WB §5.1 | 확정 |
| `family` | u8 | family | 분류 1~8 | Map::tactic_family | WB §5.1 | 확정 |
| `+0x31` | u8 | wait | 대기(72→131종, 48→24, 90→23, 0→22). 전투는 런타임 전법 객체 `+0x42`(u16)로 읽어 발동 뒤 게이지 재충전값으로 쓴다(`174F40`, 하루 −4; rules_combat_effects.md E1) | Map::tactic_wait | WB §5.1 | 확정(값)/추정(런타임 위치·단위) |
| `flags` | u8 | flags | 플래그 |  | WB §5.1 | 추정 |
| `effects[8]` | u8/s16 | effects | [0..1] 효과 종류 2칸, [2..3] 범위, [4..5] 치1(위력, `16E5E0`=+0x66+칸), [6..7] 치2(`16E670`=+0x68+칸) | Map::tactic_effect[201*8] | WB §5.1; CA §12 | 확정 |
| `+0x58` | u8 | ability | 기준 능력(분류1=무력1, 그 외 지력2) | Map::tactic_ability | WB §5.1; 능력치.md | 확정 |
| `+0x59` | u8(bits) | formation_mask | 사용 가능 진형 비트(기본 0x7E = 진형 1~6) | Map::tactic_formation_mask | WB §5.1 | 확정 |

### 3.16 TRAIT — 개성(fixdata 표 22)

- RTTI `CPersonalityData` · 표: +0x7DD18[356] (런타임 232B) · 크기: 170 B (파일) · 앵커: 본문 0x405CD + id*170
- 출처: WB §5.2; lane_L1; appendix_traits.md
- 개성 id 1~355, 효과 있는 것 206. 효과 이름 132종은 reference_mod trait_effects.json.

| 오프셋 | 폭 | 이름 | 뜻 | 엔진 필드 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `런타임 +0xA4/+0xA5` | u8 x2 | conditions | 조건 2칸 | Map::trait_conditions | WB §5.2 | 확정 |
| `런타임 +0xA8/+0xAC` | u32 x2 | condition_values | 조건값 2칸 | Map::trait_condval | WB §5.2 | 확정 |
| `런타임 +0xB4` | s16 | lpb0 | -1 자기 부대 포함 / 0 제외 / 12 (조건 없음 판정 `+0xB4==-1`) |  | WB §5.2; CA §12b | 확정 |
| `런타임 +0xB6/+0xB8` | s16 x2 | effect1 | 효과1(id, 값) | Map::trait_effect_ids/values | WB §5.2 | 확정 |
| `런타임 +0xBA/+0xBC` | s16 x2 | effect2 | 효과2(id, 값) |  | WB §5.2 | 확정 |
| `런타임 +0xBF` | u8 bits | flags | bit1 전투 발동, bit4 활성. '곱연산' 비트는 게임이 읽지 않음 | Map::trait_flags | WB §5.2 | 확정 |
| `파일 +98/+9B, +99/+9C` | ... | effect_ids_values | 효과 id(+98/+9B), signed 효과치(+99/+9C) (옛 REA 설치 레코드 판독) |  | formation_mapping.md | 확정(옛 REA) |

### 3.17 POLICY — 정책(fixdata 표 18)

- RTTI `CPolicyData` · 표: +0x78D50 · 크기: 168 · 앵커: 본문 0x3A8DE (121행 x 148B)
- 출처: WB §5.3; appendix_policy_effects.md
- 정책 121종. 방책(계략·전략 정책)은 같은 표에서 `category`로 구분.

| 오프셋 | 폭 | 이름 | 뜻 | 엔진 필드 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `(파일) 이름` | utf16 | name | 이름 |  | WB §5.3 | 확정 |
| `category` | u8 | category | 분류 | Map::policy_category | WB §5.3 | 확정 |
| `base_cost` | u16 | base_cost | 기본 비용 | Map::policy_base_cost | WB §5.3 | 확정 |
| `효과 id 8칸` | u8 x8 | effect_ids | 발동 효과(런타임 +0x98 u8[8]) | Map::policy_effect_ids | WB §5.3; DM | 확정 |

### 3.18 POLICY_EFFECT — 정책 효과(fixdata 표 26)

- RTTI `-` · 표: 표 +0x80880 index · 크기: 134 B · 앵커: 본문 0x4F255 (101행)
- 출처: WB §5.3; appendix_policy_effects.md
- 레벨 1~10 값(대부분 [1,3,5,7,10,14,18,22,25,30]; 진형강화 [2,4,...,20]; 수군진형 [3,5,7,10,15,20,25,30,40,50]; 수송 [2,4,9,14,...,44]). 세력 효과 = 활성 군사·시정 무장 정책 레벨 합(`41E570`/`26C340`, `22DFD0` 레벨→값).

| 오프셋 | 폭 | 이름 | 뜻 | 엔진 필드 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `레벨값[10]` | ... | level_values | 레벨 1~10 값 | Map::policy_values[101*10] | WB §5.3 | 확정 |
| `(effect id)` | - | ids | 엔진이 읽는 id: 1~9 진형 강화, 10 사기상한, 12 수송, 23 외교조건, 28 모병, 38 담당관비, 0x27 내구상한/동맹, 0x2D·0x2E 점령 병력·금, 0x30 지형 항(새 빌드), 0x34·0x35 수입, 0x46 인접효과 가산, 0x47 사기상한 | Game::policy_effect | WB §5.3 | 확정 |

### 3.19 TREASURE — 명품(fixdata)

- RTTI `CGemData` · 표: +0x77B18 (런타임 0x80) · 크기: 22 B x202 (유효 1~151) · 앵커: 본문 0x32A6F
- 출처: WB §5.4; appendix_treasures.md
- 152~201은 '아이템' 예비. 수여·몰수 불가는 옥새·동작(+5).

| 오프셋 | 폭 | 이름 | 뜻 | 엔진 필드 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `파일 +0x0E` | u8 | kind | 종류 |  | WB §5.4 | 확정 |
| `파일 +0x0F` | u8 | ability | 능력(1 통솔..5 매력) |  | WB §5.4 | 확정 |
| `파일 +0x10` | u8 | value | 능력값(1~10) |  | WB §5.4 | 확정 |
| `파일 +0x11` | u8 | special | 특수효과(1 퇴각확실: 명마 10, 2 수명연장: 의서3+마누 법전) |  | WB §5.4 | 확정 |
| `파일 +0x13` | u8 | price | 가치 |  | WB §5.4 | 확정 |
| `파일 +0x15` | u8 | picture | 그림 |  | WB §5.4 | 확정 |
| `런타임 +0x44` | u8 | kind | 명품 종류(12 옥새, 13 동작, 그 밖 기타). 탐색 `281480`이 이 값으로 목록을 나눈다 |  | 2026-11-08 | 확정 |
| `런타임 +0x48` | u8 | effect_value | 효과값 |  | DM | 확정 |
| `런타임 +0x49` | u8 | value | 가치 |  | DM | 확정 |
| `런타임 +0x4A` | u16 | owner_person | 보유무장 |  | DM | 확정 |
| `런타임 +0x4C` | u16 | location | 소재 |  | DM | 확정 |
| `런타임 +0x50` | u8 | state | 상태 |  | DM | 추정 |
| `런타임 +0x51` | u8 | cg | CG |  | DM | 확정 |

### 3.20 POST — 관직(Post)

- RTTI `CPostData` · 표: +0x784F8 · 크기: 88 · 앵커: +0x0
- 출처: DM; DMs 190
- 관직별 통무지정매 보정은 레코드 +0x28~2C(office.json stats).

| 오프셋 | 폭 | 이름 | 뜻 | 엔진 필드 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `+0x34` | u16 | command_troops | 지휘병사 |  | DM | 확정 |
| `+0x36` | u8 | salary | 봉록 |  | DM | 확정 |
| `+0x37` | u8 | title | 관작 |  | DM | 확정 |
| `+0x38..+0x3C` | u8 x5 | ability_bonus | 통솔·무력·지력·정치·매력 가산 | Map::office_stats | DM; 능력치.md | 확정 |
| `+0x3D` | u8 | system | 체계 |  | DM | 확정 |

### 3.21 GAME — 게임 진행 상태

- RTTI `(+0x871E8)` · 표: world+0x871E8 포인터 (5744B) · 크기: 0x1670 · 앵커: +0x0
- 출처: DM 게임 진행 상태; lane_L3 C2; difficulty.md
- 에디터 stride 5744, 직접 지휘 무장 설정(COMMAND)과 같은 객체 후반부.

| 오프셋 | 폭 | 이름 | 뜻 | 엔진 필드 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `+0x34` | u16 | year | 년 | Data::year | DM | 확정 |
| `+0x36` | u8 | month | 월 | Data::month | DM | 확정 |
| `+0x37` | u8 | day | 일(1..30) | Data::day | DM | 확정 |
| `+0x3A` | u8 | player_force | 플레이어 세력(`2337B0`이 비교) | player_forces | DM; DF | 확정 |
| `+0x450` | u32 | day_counter | 일(경과 일 카운터) |  | DM; L3 C2 | 확정 |
| `+0x454` | u8/u32 | turn_counter | 순(旬) 카운터(순 첫날 +1). 충성 분기(>36), 도적(>18) 문턱 | Data::elapsed | L3 C2; CA #f | 확정 |
| `+0x484` | state | state_code | 진행 상태(8이면 청크 대기), +0x4B8 청크 수 |  | L4 주 | 확정 |
| `+0x165E..` | u16[5] | command_list | 직접 지휘 무장 목록 5칸(전법 3순 무장 간격) |  | L3 | 확정 |
| `+0x169C` | bitmask | ethnic_mask | 이민족 복속 비트마스크 |  | sim.h R6 | 확정 |
| `+0x165D` | u8 | gap_list_len | 전법 3순 간격 목록 길이(최대 5; `2F0500` 이 관직 순위 레코드 +0xB3 으로 설정, 플레이어 세력일 때만) |  | L2 2·3차 | 확정 |
| `+0x1668` | u8[5]/u16[5] | gap_stamp | 직접 지휘 무장 5명의 순 스탬프(`170150`·`2C7340` 이 순 카운터 `+0x454` 와 비교해 간격 3 충족 판정). 쓰는 곳 `174F40` 계열 | | L2 2·3차 | 확정(읽기)/추정(쓰기처) |
| `+0x454` | u32 | ten_day_counter | 열흘(순) 카운터 |  | L1 4차 | 확정 |

### 3.22 SETTINGS — 게임 설정 객체

- RTTI `-` · 표: RVA 0x1A49C90 (옛 0x1A46CA0), 0xF00B · 크기: 0xF00 · 앵커: +0x0
- 출처: difficulty.md §1; WB §6.2
- 설정 객체가 게임 모드·난이도·60개 설정을 가진다. 표준 모드는 난이도만 선택, 숙련 모드(+0xE58==0)는 항목별 값 배열.

| 오프셋 | 폭 | 이름 | 뜻 | 엔진 필드 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `+0x28` | u32 | difficulty | 난이도 값 0 초급..4 궁극 |  | DF §1 | 확정 |
| `+0x134` | u32 | difficulty_std | 표준 모드 난이도(`3E9E60`(새 3EC370)이 `+0xE58`에 따라 둘 중 하나 반환) |  | DF §1 | 확정 |
| `+0xD8` | u32 | combo_const | 연계 상수 10 기본 분기 |  | DF | 추정 |
| `+0xE0` | u32 | supply_cut_level | 병참단절 효과 단계 0/1/2(표준 1) |  | W §2.2 | 확정 |
| `+0xEC` | u32 | morale_const | 사기 상수 200/300 기본 분기(`3E9F70`) |  | DF | 확정 |
| `+0x14C+24*n` | 60 entries | settings | 설정 60개(#20 병참단절효과 %, #26 지형 비용 %, #27 사기 감소 %, #41 군량 소비 % 등) |  | WB §6.2; W §0.4 | 확정 |
| `+0xE58` | u32 | mode | 게임 모드: 1 표준(일반 진행), 0 숙련. `3EB2A0` 읽기, `3EF660` 쓰기, `607000`이 1을 씀 |  | DF §1 | 확정 |

### 3.23 PATH_NODE — 경로 탐색 노드

- RTTI `-` · 표: - · 크기: - · 앵커: -
- 출처: mechanisms_20261017/이동경로.md (옛 빌드 주소)
- `183A30`(새 184D60)은 목표→시작 역방향 확장; 경유지는 구간별로 호출 후 결합(`1843E0`, 새 185710).

| 오프셋 | 폭 | 이름 | 뜻 | 엔진 필드 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `+0x10` | ptr | link | 연결(경로 표시 비트를 붙이며 따라감) |  | 이동경로.md | 확정(옛 REA) |
| `+0x0C (경로 구조체)` | u32 | cumulative_cost | 누적 비용 필드(capacity 아님) |  | mechanisms README 바로잡은 점 | 확정 |
| `+0x20` | u32 | cost | 구간 노드 누적 비용(+0x20) |  | 이동경로.md | 확정 |
| `+0x24` | u32 | priority | 우선값 — 가장 작은 것을 꺼냄 |  | 이동경로.md | 확정 |

### 3.24 DOCTRINE_ITEM — 주의(신념) 항목(`world+0x85F20`, fixdata 표 41)

- 출처: L1 4차(`lane_L1_4.md`), L1 5차(`lane_L1_5.md`), rules_people.md 9.6
- 항목 80개. 항목 id가 곧 효과 id. 채택 `2EF700`, 검사 `2C6590`, 비용 `324E00`, 개수 `22DA10`, 효과값 읽기 `22DB30`. 명령서 +2~+8·E3 세력 합산·ability() 신념 항의 원천(항목 37 = +8, 52·53 = 6·10, 능력 +1).
- 5차에서 엔진 구현됨: 채택 명령(`ActionType::Doctrine`), 경험 6칸·작위 상한, 해금 그래프는 인접 값 = **효과 코드**(항목 id 아님, 덤프 10,048/10,048 일치), 레코드 필드 대응(칸1·비용1·칸2·비용2·효과값·제한 플래그·효과 코드·인접 6칸)은 `lane_L1_5.md` 표에 있다.

| 오프셋 | 폭 | 이름 | 뜻 | 엔진 필드 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `+0x44` | s16 | effect_value | 효과값 |  | L1 4차 | 확정 |
| `+0x47` | u8 | kind | 종류 |  | L1 4차 | 확정 |
| `+0x48` | u8 x6 | adjacent | 인접 항목 6칸 |  | L1 4차 | 확정 |

- **항목 0x30 = 「지세활용」(2026-11-12 확인, 현재 Steam 빌드 fixdataexce 표 41 + 디컴파일)**: 효과값 5. 세력이 이 항목을 채택했으면(`22DB30(세력, 0x30)` = 세력 `+0x1CB` 채택 비트, `+0x1D5` 차단 비트 아님) 부대가 서 있는 칸의 지형 분류(`지형 런타임 +0x42`)가 2(산: 저산·중산·고산·산길) 또는 4(대하·격류)일 때 부대 능력 다섯 함수에 `(100 + 5) / 100`을 곱한다: 공군 `2B4460`, 공성 `2B4750`, 방어 `2AC0A0`, 파성 `2AC5A0`, 기동 `2B2550`. 즉 전 능력 +5%. 이전 기록의 "효과 0x30은 모든 표에서 0이라 휴면", "정책 효과 0x30", "4함수"는 틀렸다: 정책 효과 표(26)가 아니라 주의 항목 표(41)의 값이고, 파성 `2AC5A0`까지 다섯 곳이다.
- **패치 전 fixdata 를 현재 EXE 에 쓰면(2026-11-12 사용자 제작 시나리오 묶음 대조)**: 패치 전 표 41 은 항목 0x30 이 「안민포고」(값 90), 0x40 이 「조선술」(값 20)이고 「지세활용」이 없다. 현재 EXE 는 0x30 을 지형 배율로 읽으므로 그 파일로는 「안민포고」를 채택한 세력의 부대가 산·대하·격류에서 다섯 능력 ×1.90 이 된다(화면 실측 파성 12→23, 기동 17→32). 같은 파일은 표 39(공적 보상) 3단계가 `01 e8 03`(병력 +1000)이고 현재 판은 `03 01 00`(시정 Lv+1)이며, 견인불발 10(현재 25)·상산사세 2(현재 3) 등 값도 다르다. 시나리오 파일(sceda)은 표 41·39 를 싣지 않는다(개수만 있는 표시). 개성 사본 표 22 는 싣는다.
- 표 41 파일 레코드(37B): `+0` 이름(UTF-16 11자), `+22` 칸1, `+23` 비용1, `+24` 칸2, `+25` 비용2, `+27` 효과값(s16), `+29` 제한 플래그, `+30` 효과 코드, `+31` 인접 6칸. 예: 0x20 공격계전법강화 20, 0x21 원거리계전법강화 20, 0x26 상산사세 3, 0x28 견인불발 25, 0x30 지세활용 5.

### 3.25 5차 묶음 구조 보강 (L1 주의, L2 단기접전, lane_L1_5.md·lane_L2_5.md)

- 작위 레코드(fixdata 표 15): 파일 바이트 157..161 = 군주 능력 항(황제 5/5/5/5/0 … 없음 0), 165 = 최대 채택 수(황제 36 / 왕·공 33 / 대사마 30 / 대장군 24 / 중랑장 20 / 주목 14 / 주자사 10 / 없음 6, 항목 1·74..79 제외). 엔진 `RANK_ABILITY`·`RANK_DOC_CAP`.
- 군단 `+0x14`(명령서)는 주의 항목 채택 허용량이기도 하다(항목 1개당 1).
- 세력 `+0x1E9..+0x213` = `+0x1C5..+0x1EE`(경험 6칸·채택/해금 비트·작위)의 백업. 저장 `225A20`, 복원 `236F90`.
- fixdata 표 42 파일 바이트 28 = 승급 1회당 위계 3..6 단계별 주의 경험치(데이터).
- 무장 능력 경험: 능력값 `+0xEC..+0xF0`(u8 5칸)과 경험 `+0x104`(u32 5칸). 임계는 `0000/experience_data_exce.bin`(101레벨 × 5칸)에서 온다(`3E61F0` 파일표 2번 → `32A7B0`). 레벨 L의 경험은 그 표 `T[L]`과 같고, `2BC0D0`이 `T[L+1]`과 비교해 오른다.
- 세계 `+0x871E8` 객체 `+0x1698` = 순 단기접전 카운터(0..3), `+0x48` = 시나리오·모드 값. 접전 장면 객체 `+0x5B8` = 그 순의 쌍 목록, `+0x4AC..` = 결과 블록(칸당 0x58B: 체력 `+6`, 라운드 피해 `+0xE..`, 종류 `+0x14..`).
- **전투 컨텍스트 `16E890`의 교전 쌍 목록(2026-11-08)**: 컨테이너는 `+0x90`(범용 연결 리스트 클래스)이고 필드는 `+0x10` 사용 헤드(= 컨텍스트 `+0xA0`)·`+0x18` 꼬리·`+0x20` 빈 노드 헤드·`+0x28` 노드 배열·`+0x30` 개수·`+0x40` 잠금이다. 노드는 0x40 B(배열 stride 0x40, `16C4C0`가 `개수<<6` 할당)이고 `+0x30` next·`+0x38` prev로 잇는다. 노드 페이로드: `+0x00` 레코드 포인터, `+0x08` u16 부대·`+0x0C` u32 종류(초기 0xff), `+0x10`·**`+0x14` 칸(u32)**·`+0x18`·`+0x1C`·`+0x20`·`+0x24`·`+0x28`·`+0x2C` u32. 생성은 `171820`이 `17E0A0(ctx+0x90,1,0)`로 빈 노드를 붙인 뒤 656~666행에서 직접 채운다(호출자 `171160` 3곳).

## 4. fixdata 표 등록부 (`0010_KO/fixdataexce.s14`, LWC 압축해제 본문 367,805B)

| 표 | 이름 | 본문 오프셋 | 레코드 | 개수 | 런타임 위치 | 출처 |
|---|---|---|---|---|---|---|
| 8 | 지형 | (미기재) | 51B(포장) | 31(id 1..30) | world+0x73860 (0x48B 객체) | W §0.4 |
| 9 | 시설 | 0x2CD9E | 53B | 31 | world+0x73958 (104B) | W §3.1 |
| - | 진형 | 0x2D419+id*152 | 152B | 21 | world+0x77428 (0xC8) | formation_mapping.md |
| 12 | 전법 | 0x2E099 | 94B | 201 | table +0x774D0 | WB §5.1 |
| - | 명품 | 0x32A6F | 22B | 202(유효 1~151) | world+0x77B18 (0x80) | WB §5.4 |
| 18 | 정책 | 0x3A8DE | 148B | 121 | world+0x78D50 (0xA8) | WB §5.3 |
| 22 | 개성 | 0x405CD | 170B | 356 | world+0x7DD18 (232B) | WB §5.2 |
| 26 | 정책 효과 | 0x4F255 | 134B | 101 | index world+0x80880 | WB §5.3 |
| 39 | 공적 보상 | (미기재) | 4B x 7 | 7 | world+0x85DF0 | CA §15 항목 5 |

파일·본문 해석 도구: `San14Sim/tools/extract/fidelity_tables.py`, `tools/worldmap_tables.py`(부록 `worldmap/appendix_*.md`, `facility_table.json`, `area_fac_cap.json`, `treasure_table.json`). 데이터 파일 형식 문서는 `reference_mod/Modding_DOCS/format/`(DATA 통합 담당 범위).

## 5. 엔진 대응 요약

이 절은 별도 San14Sim 시뮬레이터의 구현 비교였으므로 공개 원작 사양에서 제외했다. 원작 규칙은 이 문서 앞 절의 RVA·데이터 근거를 따른다.

## 6. 충돌 (둘 다 기록, 출처 표기)

| # | 구조체 | 종류 | 내용 | 출처 |
|---|---|---|---|---|
| S1 | WORLD | 충돌 | +0x85F20 표 이름: BUILD_25953386_COMBAT는 '기술 0x85F20', dump_measurements는 '표 0x85F20 +0x44 = 주의 항'. 같은 주소를 달리 부름(내용은 주의/기술 계열 표로 추정). | BUILD_25953386_COMBAT.md §1; dump_measurements.md:191 |
| S2 | HEX | 해소(L3b) | hex+0x16: 1권(worldmap_spec §0.2)은 '경로 예약 표지, 덤프에서 항상 0', command_audit §15는 같은 +0x16을 타일 화염값(u16 0..720)으로 사용(엔진 hex_fire). 화염 계열 함수(43E660 등) 추적이 있어 화염 용도일 가능성이 높으나 덤프 대조로 확정되지 않음. **해소(L3b)**: `2A3CF0` 이 칸마다 매 틱 +0x16 을 `DAT_141A4C070` 만큼 줄이는 u16 카운터이고 `43E660`·`2A3510`·`2E5DA0` 이 읽는다: 화염값. 덤프에서 항상 0 이던 것은 화염 없는 덤프였기 때문 | worldmap_spec.md §0.2 vs command_audit.md §15 / sim.h 주석 |
| S3 | TERRAIN | 충돌 | 정기 사기 감소 위치: worldmap_spec §0.4는 `+0x30 u8(런타임 +0x40)`을 사기 감소 기본값, `+0x2F`를 거침 등급으로 적었다. command_audit §15는 `+0x2F`가 곧 사기 감소 기본값(런타임 +0x40)이고 `+0x30`은 화염 계열이라고 정정(덤프 근거). 정정본을 본문에 채택, 옛 해석은 정정 기록. | worldmap_spec.md §0.4 vs command_audit.md §15 |
| S4 | FACILITY_DEF | 미해결 | 효과1/효과2(종류·값·값2)의 레코드 내 정확한 오프셋과 효과 종류 1/2/3/8/15/16/17의 의미는 추정(1 원거리 피해, 8 부대 회복, 15 군악대 사기 회복; 18 군량 소비 감면=확정). | worldmap_spec.md §3.1 |
| S5 | AREA | 충돌 | 지역 개발값 위치: 에디터(DM)는 +0x2A/+0x2C/+0x2E를 상업/농업/병영 값으로 선언, 능력치.md는 개발 진행값이 +0x3C/+0x3E/+0x40이고 에디터 수치와 다른 저장칸이라고 명시. 본문은 코드 근거(+0x3C/+0x3E/+0x40)를 따름. | REA_Analysis/data_model.md 지역 표 vs mechanisms_20261017/능력치.md |
| S6 | CITY | 해소(L3b) | 도시 +0x50: 에디터(DM)는 부상병 u16, pre6_occupation·dump_parse는 부상병 풀=+0x40이고 +0x50은 officer_alloc_50. 덤프 근거로 +0x40 채택. **해소(L3b)**: `2BDCD0` 이 +0x3C(병력)·+0x44(사기 u8)와 함께 풀 +0x40 을 부상병으로 쓴다(L2 3차 확정): +0x40 채택, +0x50 은 officer_alloc_50 | REA_Analysis/data_model.md vs pre6_occupation.md; dump_measurements.md:69 |
| S7 | CITY | 해소(L3b) | 도시 사기 +0x44 폭: 에디터 도시 스키마 u16, 관문 스키마/코드 후보 u8. 값이 같아 보이는 검증만으로 상위 바이트 의미 미확정. **해소(L3b)**: `2BDCD0` 이 +0x44 를 byte 로 읽는다: u8 채택(도시·관문 동일) | REA_Analysis/data_model.md 정정·충돌 |
| S8 | FORCE | 해소(L3b) | 동맹 위치 +0xEA(코드, W §2.1·CA) vs +0xEB(에디터 DM). 코드 근거를 채택. **해소(L3b)**: +0xEA 배열을 세력 번호로 인덱싱(`+0xEA + 번호`, 조건 16 코드)하며 번호 0 이 미사용이므로 에디터의 +0xEB 는 번호 1 원소의 위치: 같은 배열, 기준 +0xEA | worldmap_spec.md §2.1 vs REA_Analysis/data_model.md |
| S9 | FORCE | 해소(L3b) | 전법서 재고 +0x120(CA) vs +0x122(DM): 31칸 idx1이 +0x122이면 동일 표. **해소(L3b)**: `22DB30` 같은 전법서 재고 u16[31] 배열이 +0x120 기준이고 idx 0 미사용이면 idx 1 = +0x122 와 같다. 같은 배열로 해소(확정 아님: 읽는 함수 직접 확인은 안 함) | command_audit.md vs data_model.md |
| S10 | ARMY | 충돌 | army +0x58: 에디터 u8 '출발도시' vs 코드 u16 소속 군세 ID. 후자 채택(정정 기록). | REA_Analysis/data_model.md 정정·충돌 |
| S11 | ARMY | 해소(L3b) | army +0x1F8: 에디터 '목적칸', approx_inventory A2는 '경로 캐시 +0x1F8'. 같은 용도(목적지 기반 경로 캐시)일 가능성이 있으나 미확정. **해소(L3b)**: `303EA0` 이 +0x1F8 에 경로 끝 칸(없으면 0xBD10)을 쓰고 읽는다: 에디터 "목적칸"과 같은 용도의 경로 캐시 | data_model.md vs approx_inventory.md A2 |
| S12 | PERSON | 해소(L3b) | 공적 +0x1BE 부호: 에디터 u16, 헤더 설명 i16, 엔진은 -1000..12000 사용. 명령어 기반 부호 검증 미완료. **해소(L3b)**: 판단표·여러 코드의 +0x1BE 접근은 모두 `short`(부호 있음; 읽기 55곳 + undefined2 8곳, ushort 0곳): s16 채택 | REA_Analysis/data_model.md 정정·충돌 |
| S13 | PERSON | 충돌 | 무장 개성 칸 수: 에디터 `+0x118 u16[9]`(traits9) vs 옛 `+0x118[5]`(CA #23). 새 빌드 모드는 traits9 사용. | command_audit.md vs worldmap_spec_b.md §5.2 |
| S14 | FORMATION | 정정 | 과거 `formation_defense=2B2690`, `defense_stat_formula=2B2440`, `siege=2A9E50` 라벨은 폐기. 방어 입력 생산자는 `2A9E50`과 부대 +0x4D, 공성 입력 생산자는 `2B2440`. | formation_mapping.md; data_model.md 말미 |
| S15 | POLICY_EFFECT | 미해결 | 효과 id 46~100은 이름 없음(0 자리표시)이나 코드가 0x47까지 읽는다. 의미 대부분 미상. | worldmap_spec_b.md §5.3 |
| S16 | SETTINGS | 충돌 | 설정 객체 주소: BUILD_25953386_COMBAT는 `설정 객체 3E9C90 (+0x8 = 1A46CA8) → 1A49C98`, worldmap_spec_b는 `settings(새 RVA 0x1A49C90, 옛 0x1A46CA0)`. 8바이트 차(객체 시작 vs +0x8 필드)이며 같은 객체로 해석. | BUILD_25953386_COMBAT.md §1 vs worldmap_spec_b.md §6.2 |
| S17 | ARMY | 충돌 | 부대 +0x3C(u8)/+0x3E(u16): L4 는 "사후 목표"(퇴각·주둔 등), L2 2·3차는 "도발 시전자(종류·id)"(덤프 대조). 부대정보 항목 9/10 이 같은 칸을 종류/번호 쌍으로 읽음. 같은 칸을 도발 중에는 시전자, 아니면 사후 목표로 겸용할 가능성 | L4; L2 2·3차; L3b |
| S18 | PERSON | 해소(L3b 3차) | 무장 +0x162 u16: 에디터 "사관금지", L1 2차 "옛 군주". **해소(L3b 3차)**: `279DE0`(등용 평가)이 +0x162 를 등용하는 군주 id 와 비교해 같으면 불가로 하므로 옛 군주가 정답(금지 기간 +0x164 와 짝) | DM; L1 2차 |

## 7. 정정 기록 (옛 해석 → 정정본)

| 대상 | 옛 해석 | 정정본(본문 채택) | 출처 |
|---|---|---|---|
| 지형 +0x2F/+0x30 | +0x30=사기 감소 기본값, +0x2F=거침 등급 (W §0.4) | 레코드 +0x2F=사기 감소 기본값(런타임 +0x40), +0x30=화염 계열(+0x41), +0x31=분류(+0x42). 지형 객체는 레코드 +0x10/+0x11 이동 | command_audit.md §15 (덤프 확인) |
| army +0x58 | 에디터: 출발도시 u8 | 소속 군세 ID u16 | data_model.md 정정·충돌; siege_logistics/분석근거.md:80,94 |
| 도시 인접거점 +0x58 | u16[10] (seed) | u8[10] | data_model.md |
| 도시 +0x40/+0x50 | 에디터: 부상병 +0x50 | 부상병 풀 +0x40 (+0x50 = officer_alloc_50) | pre6_occupation.md 용어; dump_measurements.md:69 |
| 진형 방어 슬롯 | 방어 = +0x85 가설, 라벨 formation_defense=2B2690 등 | 공군 +0x83 / 공성 +0x84 / 파성 +0x85 / 방어 +0x86; 방어 입력 생산자 2A9E50(+army +0x4D), 공성 입력 생산자 2B2440(+army +0x4C) | formation_mapping.md; data_model.md |
| hex +0x14 의미 | 단순 소유 | 세력(마스터 ID). 군단 슬롯·진행상태 +0x3A와 같은 숫자라도 같은 인덱스가 아님 | data_model.md 주소 기준점 |
| 공적 +0x1BE 위계 배분 | S16: '위계 단계당 능력 +1' | 표 ID 39 `공적 보상`(지휘병사 500/500/1000, 담당 지역 +1/+1, 정책 등급 +1). 능력치에는 영향 없음 | command_audit.md §15 항목 5 |
| 거점 부대 회복 25C460 | '거점 부대 회복'(RULES.md:39 이전 명명) | 도적 출현 판정(옛 25C460=새 25DE00). 입력 +0x54는 부대가 아니라 지역 치안 | difficulty.md:102 · build_remap.md:651 · command_audit.md §4 |
| army +0x4C | '방어 일시보정' | 공성 입력 생산자 2B2440의 일시보정 후보. 방어는 +0x4D(2A9E50) | data_model.md 추가 기존 코드 관측 |
| 사인 +0xB0 | u16 death_cause(에디터) | u8 death_kind 0/1(졸년 + 10~13년 사망, 질병 임계 +10) | L1 3차 |
| 도시/관문 +0x50 | 부상병(에디터) | officer_alloc_50(부상병 풀은 +0x40) | L2 3차; L3b |

## 8. 미해결 목록 (시도한 경로 포함)

| # | 항목 | 시도된 경로 | 상태 |
|---|---|---|---|
| U1 | HEX 파일 칸 +8~+15 용도(시각 속성 후보) | 런타임 객체에 복사되지 않음 확인; 월드맵 규칙엔 영향 없음으로 추정 | 미해결 |
| U2 | HEX +0x16 용도(예약 표지 vs 화염) | 덤프에서 항상 0, 화염 함수 43E660/2A3CF0/2A3510/2E5DA0 읽기만 확인 | 해소(L3b): 화염 카운터 u16(`2A3CF0` 틱마다 감소). S2 참조 |
| U3 | 시설 정의 효과 종류 1/2/3/8/15/16/17 의미, +0x32 하위종류 | 소비 함수 191760·16A780·300970 호출자 추적 제안만(미실행) | 미해결 |
| U4 | AREA +0x66 마스크 비트 의미, +0x6D, +0x1E(hex) | 집계 사용처만 확인(2B07C0/2B2A90) | 미해결 |
| U5 | FORCE +0x1BE/+0x1C5 의미, +0x193 비트 이름 | 사용처(2255F0 22곳, 진형 분기)만 확인 | 미해결 |
| U6 | PERSON +0x15E 비트별 이름·+0x184 마스크 | 쓰기·읽기처 grep(`0x15e)` 400건) 후 비트 3·4·7·9·10·11 의 쓰기 함수를 읽어 위 flags 행에 정리(L3 5차). 비트 5는 위임 중 전법 사용 불가로 확인(`170150`). 비트 1·2·6·8·12와 +0x184 마스크는 남음 | 부분 해소 |
| U7 | 지역 시설 상한 +0x6E의 fixdata 원본 위치 | area_fac_cap.json 대조 제안 | 미해결 |
| U8 | 숨은 물건 목록 world+0x85A90 | 정적 데이터 없음, 덤프에 위치가 있으면 대조 | 해소(L3b 2차): `world+0x85A90`(101칸, 간격 0x78) = 명승(Scenery) 표다(명승정보 getter `8FFA0`: 번호 = `(객체-표)/0x78`, `+0x5C` 칸, `+0x5F` bit0, `+0x64`/`+0x66`/`+0x68`/`+0x6C` 필드; 안내문 41568 "지도상에는 총 100여곳의 명승"). 숨은 물건 목록이 아님 |
| U9 | 관직 순위 표 world+0x78490 | 엔진 미추출(approx_inventory S8/D3) | 미해결 |
| U10 | 설정 객체 60개 설정의 이름·단계 이름(+0xE0 0/1/2) | settings 블록 덤프 제안(WB §6.2) | 미해결 |
| U11 | 정책 효과 id 46~100 이름 | 사용처별 코드 확인 필요 | 미해결 |
| U12 | 공적 +0x1BE 부호·도시 사기 +0x44 폭 | 명령어 기반 부호 검증 미완료 | 해소(L3b): 공적 +0x1BE = s16(모든 접근이 short), 도시 사기 +0x44 = u8(`2BDCD0`) |

## 9. 출처 목록과 낡음/대체 확인 결과

읽은 문서(STRUCT 묶음): read_first 1 + 낡음 12 + 오프셋 풍부 문서 + 엔진 `core/sim.h` 주석. 확인 방법: 문서의 5~7자리 16진 토큰을 `rva_map/functions.tsv`로 옛/새 함수 시작에 대조(m1_doccheck), 문서 내 정정 선언 줄 확인. **'옛 시작'이 대부분이면 옛 번호 체계(1fbe6be7)**다.

| 문서 | 확인 결과 | 판정 | 대체 문서 |
|---|---|---|---|
| `San14Sim/docs/fidelity/worldmap_spec.md` | RVA 109개: 새 시작 59, 옛 시작 48(겹침 4). '새/옛' 병기 표가 많음 | 현재 | — |
| `AI_TacticsMod/docs/NATIVE_FUNCTIONS.md` | 옛 번호 체계(1fbe6be7; 문서가 SHA 1fbe6be7·87ed4e 명시). 함수 시작 RVA 444개 중 옛 시작 318 / 새 시작 18(=번호 겹침 16). 새 빌드는 BUILD_25953386_REMAP.md가 대체 | 낡음 확인(옛 빌드) | BUILD_25953386_REMAP.md + build_remap.md/json + rva_map/functions.tsv |
| `AI_TacticsMod/research/ui_atlas/CHECKPOINT.md` | RVA 3개 전부 옛 시작 | 낡음 확인(옛 빌드) | ui_native.md(M5) |
| `AI_TacticsMod/research/ui_atlas/README.md` | RVA 16개 중 옛 시작 16, changed 1, unmatched 1(UI vtable 목록). UI는 ui_native.md(M5)가 다룸 | 낡음 확인(옛 빌드) | ui_native.md(M5 담당) |
| `REA_Analysis/data_model.md` | RVA 3개 전부 옛 시작·changed 3. 에디터 AST 선언 오프셋(87ed4e 기준). 필드 오프셋은 새 빌드에서도 유지(build_remap.md §1) — 단, 코드 근거로 정정된 항목(도시 +0x40, 동맹 +0xEA, army +0x58 등)이 있어 본문은 structs 절 우선 | 오프셋은 유효·해석은 일부 정정(structs.md에 반영) | structs.md, worldmap_spec.md, command_audit.md |
| `REA_Analysis/data_model.pseudo.cpp` | RVA 4개 전부 옛 시작·changed 3 | 낡음 확인 | structs.md |
| `REA_Analysis/formation_mapping.md` | RVA 23개 중 옛 시작 14, changed 3(2A9E50 등 입력 생산자). 진형 오프셋(+0x83~0x86)은 유효, 라벨 정정 포함 | 오프셋 유효·RVA는 옛 번호(변환 필요) | structs.md FORMATION 절 |
| `REA_Analysis/mechanisms_20261017/CHECKPOINT.md` | RVA 3개 전부 옛 시작. 해제본 1fbe6be7·원본 87ed4e 명시 | 낡음 확인(옛 빌드) | build_remap.md |
| `REA_Analysis/mechanisms_20261017/README.md` | RVA 8개 전부 옛 시작, changed 2. 16행 표가 41C140 별칭을 정정 | 옛 번호 확인. 정정 내용(41C140은 통솔 조회 아님)을 본문에 채택 | functions.md 개성·정책 절 |
| `REA_Analysis/mechanisms_20261017/능력치.md` | RVA 24개 전부 옛 시작, changed 4(22FCE0·2A9E50·2B21A0 등) | 옛 번호 확인(식은 기본적으로 유효, 22FCE0는 새 빌드에서 bit14 검사 추가) | functions.md 능력치 절 |
| `REA_Analysis/mechanisms_20261017/이동경로.md` | RVA 7개 전부 옛 시작, changed 0 — 경로 함수 본문은 불변. 단 183A30(새 184D60)의 호출 사슬은 변경(2B0290에 0x30 지형 항 추가, build_remap.md §2) | 옛 번호만 변환하면 유효 | build_remap.md §2(183A30→184D60 등) |
| `REA_Analysis/mechanisms_20261017/출진과요격.md` | RVA 12개 중 옛 시작 10, changed 4 | 옛 번호 확인 | functions.md AI 절 |
| `REA_Analysis/mechanisms_20261017/함수별_증거.md` | RVA 표 39행 전부 옛 번호(8자리 0.. 표기) | 옛 번호 확인 | functions.json의 old 필드로 새 RVA 조회 |

읽기만 하고 별도 검증은 하지 않은 보조 출처: `San14Sim/docs/fidelity/command_audit.md`(§12·15 지형·개성), `lane_L1~L4.md`, `dump_measurements.md`, `difficulty.md`, `approx_inventory.md`, `San14Sim/docs/RULES.md`(상단 표는 낡음: worldmap_s8.md:5), `San14Sim/engine/core/sim.h`(필드 대응), `REA_Analysis/mechanisms_20261017/*`, `BUILD_25953386_COMBAT.md`.

**SOURCES.md 낡음 추정 중 STRUCT 해당분 확인 요약**: NATIVE_FUNCTIONS.md·ui_atlas·REA data_model/formation/mechanisms 12개는 모두 옛 번호 체계 확인(낡음 판정 유지). 단 오프셋 자체는 새 빌드에서 유효(§1)하므로 *오프셋 표는 폐기 대상이 아니라 RVA만 변환 대상*이다. data_model.md는 정정된 항목 6건을 위 7절에 반영.
