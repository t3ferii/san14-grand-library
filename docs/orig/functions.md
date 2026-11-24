# 원작 함수 지도 통합 (FUNC)

> **이 문서에서 찾는 법**: 1 개요·표기 · 2 분류별 함수표(역할·입출력·엔진 위치·근거·확신도) · 3 호출 체인(날짜 상태기계 32 case, 월 이벤트, 교전 단계표, 칸 소유 호출자) · 4 충돌 · 5 정정 기록 · 6 미해결 · 7 자동 색인(미정리 함수) · 8 출처와 낡음 확인.
> **새 확정 사실은 이 문서의 해당 절에 추가한다.** 기계가 읽는 사본은 `functions.json`(새 RVA→역할·분류·입출력·엔진 위치·근거). 주소 변환은 `build_addresses.md`.

작성 2026-11-07 (M1). 정리한 함수 218개(큐레이션) + 자동 색인 690개. 기준 빌드 `1a4a447d`(Steam buildid 25953386). **모든 RVA는 `새(옛)`로 적는다.**

## 1. 개요·표기

- **주소 체계가 문서마다 다르다.** 새 빌드(1a4a447d)와 옛 빌드(1fbe6be7)는 .text 구간마다 +0xFE0~+0x2900대로 밀려 있어 거의 모든 RVA가 한 번 이상 움직였다(build_addresses.md). 같은 문서 안에서도 새/옛이 섞이는 곳이 있다(예: lane_L4.md는 15행에서 옛 `43E030`, 84행에서 새 `44DD30`을 적음). 이 문서의 큐레이션 항목은 `rva_map/functions.tsv`로 검증해 새 함수 시작 주소로 통일했고, 각 줄에 옛 번호를 병기한다(검증 실패 2건은 옛 번호로 정정함).
- 확신도: **확정**(코드+덤프), **코드**(코드만 읽음), **추정**, **미해결**. 근거는 `문서 절`(약어: CA=command_audit.md, W/WB=worldmap_spec(_b).md, L1~L4=lane_L1~L4.md, DMs=dump_measurements.md, DF=difficulty.md, BR=build_remap.md, BC=BUILD_25953386_COMBAT.md, MECH=REA_Analysis/mechanisms_20261017).
- 원작 함수를 직접 볼 때: `python -X utf8 AI_TacticsMod/tools/ghidra_full.py func|grep|callers|callees|xref|str <새 RVA>`(게임 루트에서; SESSION_RULES §7). `ghidra_full.py`의 함수 시작이 틀린 곳이 있다(170D80, 173DD0, 174F40, 1798B0은 각각 170870, 172E20, 174E30, 1798A0 안의 중간 지점; DMs:99) — 그 경우 `callers`의 둘째 열이 호출 지점이다.
- 옛→새 변환: `python -X utf8 AI_TacticsMod/tools/rva_remap.py map <RVA>` 또는 `rva_map/functions.tsv`(옛 RVA 정렬, 새 RVA·크기·상태). 이 문서의 `functions.json`에는 큐레이션·인용 함수 모두 `old` 필드가 있다.

### 분류별 개수

| 분류 | 개수 |
|---|---|
| 시간·상태기계 | 8 |
| 이동·경로 | 21 |
| 보급·병참 | 12 |
| 점령·칸소유 | 16 |
| 시설·건설 | 18 |
| 전투·피해 | 30 |
| 전법 | 21 |
| 개성·정책 효과 | 11 |
| 능력치 | 3 |
| 내정·경제 | 18 |
| 인사 | 19 |
| 외교 | 9 |
| 계략 | 3 |
| 이민족·도적 | 3 |
| AI 판단 | 12 |
| 난이도·설정 | 4 |
| 난수 | 2 |
| 데이터 접근 | 5 |
| UI | 3 |

## 2. 분류별 함수표

### 2.1 시간·상태기계

| 새 RVA (옛) | 이름 | 역할·식 | 입출력 | 엔진 위치 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `2CCC60` (2CA8B0) | 단기접전 생성기(case 5, 옛 "무작위 이벤트 발생기" 정정) | 하루 1회 일반 교전 앞에서 접전 후보·상대를 골라 `376020`→`3747A0`을 부른다. 날짜 +0x37 대신 `44DEE0` case 5에서 진입 | - |  | lane_L2_5.md 1 | 확정 |
| `301AF0` (2FF700) | 부대 목록 청소·갱신(case 0x1A) | 2901A0과 함께 부대 목록(+0x70, 283ED0) 청소 | - |  | lane_L4.md §2 | 확정 |
| `305390` (302FA0) | 순 시작 거점 순회 | 거점별 수입·순 군량 지불(수비병 → 부대)·내정·훈련·수리, 월초 추가 처리와 카운터 초기화. 전체 호출 순서는 [날짜·순](rules_time.md) 4절 | - |  | `431824 → 305390` 및 본문 | 확정 |
| `32DD00` (32BA50) | 날짜식 | 한 달 30일·한 해 360일, 매달 1·11·21일 결정을 정의 — 옛 32BA50 | - |  | RULES.md(32BA50 옛) | 코드 |
| `42FDC0` (42DAB0) | 월 1일 이벤트 단계기계 | 단계표 141A64050/조건표 141A642D0의 0..0x4E 단계를 차례로 호출(단계 19=42A430→29F380 충성 분기 하락, 21=429000→25DE00 도적 출현, 25=42BB80→2A5140, 2=429030→25F060) | 상태 +4 플래그 |  | command_audit.md §2 | 확정 |
| `44BAD0` (449880) | 세력 행동 순서 결정 | 플레이어가 있고 난이도 3 이상이면 플레이어 선두, 그 밖에는 자연 순서 — 엔진: apply() 순서(플레이어 전용) | - | ai/agent.cpp:196, rules/difficulty.h:43 | difficulty.md 항 37 | 확정 |
| `44DD30` (44BAF0) | 세력 턴 상태 | 세력 턴 상태 2(이민족 세력 +0x60-0x2E<5)에서 세력마다 순당 1회 2C4D40→2607E0→259310(이민족 공격)을 호출 | - | rules/battle.cpp:411, rules/battle.cpp:416, rules/battle.cpp:432 | lane_L4.md §3 | 확정 |
| `44DEE0` (44BCA0) | 날짜 진행 상태기계(day state machine) | 하루 12칸(s=0..11) 시계로 case 0..0x1F를 차례로 돌며 이동·교전·건설·사기감소·점령 등 일 단위 처리를 호출한다 — case 7·8 이동(2DB9A0), 0xB 몸 모양 칠하기(301D00), 0xD 교전 하루 1회(17B9E0, 칸 5), 0xE 쌍 목록(18F9D0), 0xF 건설 착공(28A200), 0x10 건설 진행(2EA410), 0x12 5일 사기 감소(272720), 0x16 함정, 0x1C 부대 옵션(273AC0) 등. 옛 44BCA0 | 입력: 날짜 상태(+0x450 일/+0x454 순/+0x484 상태). 출력: 부대·지역·시설 상태 변경 | rules/battle.cpp:13, rules/battle.cpp:16, rules/battle.cpp:162 | lane_L4.md §2 | 확정 |

### 2.2 이동·경로

| 새 RVA (옛) | 이름 | 역할·식 | 입출력 | 엔진 위치 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `BF1B0` (BE120) | 지형 이동 비용 getter | 지형 객체 +0x2A 반환. 숙련이면 지형 3~14·24에 설정 #26 %를 곱해 [225,999]로 자름 — 옛 BE120 | 입력: 지형 객체 | core/init.cpp:28, core/path.cpp:8, rules/battle.cpp:179 | worldmap_spec.md §0.4 | 확정 |
| `184D60` (183A30) | A* 한 구간 경로 탐색 | 목표에서 시작으로 확장(역방향). 칸당 비용: 이동이면 2B0A20=BF1B0(+예약표지 x50), 정규화 187880; 보급·단순(플래그 0/8)은 균일 10000. 막힘: 지형 비용 0, 2C8AB0 계열, 클래스 2·3 시설(플래그 0x40이면 허용), 독늪 +10000, 점유 칸 — 옛 183A30(2,466B); 엔진 core/path.cpp Map::path | 입력: 시작, 목표목록, 옵션 플래그. 출력: 연결 경로 | core/path.cpp:9, core/path.cpp:12, rules/battle.cpp:190 | worldmap_spec.md §4.1; mechanisms_20261017/이동경로.md | 확정 |
| `185710` (1843E0) | 경유지 결합 경로(최대 5경유) | 구간마다 184D60 호출, 합 비용 +0xC. 출력 칸 수가 양수이면 성공(실패 구간이 있어도 계속) — 옛 1843E0 | - |  | worldmap_spec.md §4.1; mechanisms_20261017/README | 확정 |
| `187880` (1864F0) | 이동력에 따른 한 칸 비용 보정 | 부대 기동(2B2550) 배율로 정규화 — 옛 1864F0 | - |  | worldmap_spec.md §4.1 | 확정 |
| `18C330` (18AFA0) | 경로 목적지 후보 초기화·목표 검증 | 목적지 각 칸을 열린 후보에 넣고 허용 검사. 적대 거점이 목표가 아니면 실패 — 옛 18AFA0(REA 증거표 '목적지 후보 초기화') | - |  | mechanisms_20261017/이동경로.md; worldmap_spec.md §4.1 | 확정 |
| `26AB00` (269150) | 하루 이동 점수(갱신당) | int(100 x 2B2550 / (100 + 2B7BC0)), 상한 1000. 부대 누산기 +0x14에 더하고 다음 칸 비용 이상이면 한 칸 이동 — 옛 269150 | 입력: 부대. 출력: 점수 | rules/battle.cpp:179, rules/battle.cpp:180, rules/battle.cpp:185 | worldmap_spec.md §4.2 | 확정 |
| `26E260` (26C940) | 이동 명령 부대 경로 계산·이동량 상위 | 엔진 Map::path 역할 주석에 나오는 상위 함수(명령 처리 일부) — 옛 26C940 | - | ai/agent.cpp:14, rules/battle.cpp:155 | FIDELITY.md; agent.cpp:14 | 추정 |
| `273AC0` (272190) | 부대 상시 옵션·목표 유효성(핵심) | 매 칸 부대마다: 행동(+0x37)·목표 유효성, 옵션 +0x26 bit2(사기<40/병력<1000/단절이면 퇴각 2EC570), +0x40==2(3칸 안 적 교전), 명령 종료 2A2C90→2A3470(사후명령) 등 — 옛 272190; case 0x1C(276250 경유) | 입력: 부대 | rules/battle.cpp:160, rules/battle.cpp:162, rules/battle.cpp:169 | lane_L4.md §2.1 | 확정 |
| `2A9A80` (2A7890) | 헥스 이웃 열거(열 오프셋 평탑) | 짝수 x/홀수 x 방향표(1413afd88)로 이웃 6칸, 범위 0..48399 — 옛 2A7890; 엔진 core/hex.h | 입력: 칸, 방향. 출력: 이웃 칸 | ai/schema.cpp:16, core/hex.h:4, core/hex.h:35 | worldmap_spec.md §0.3 | 확정 |
| `2A9C90` (2A7AA0) | 헥스 링 열거 | 링 k = 6k칸, 반경 k 합 (k+1)k*6/2 (중심 제외) — 옛 2A7AA0 | - | core/hex.h:5, core/hex.h:9, core/init.cpp:88 | worldmap_spec.md §0.3 | 확정 |
| `2B0A20` (2AE6F0) | 헥스 이동 비용 | BF1B0(지형 객체) + (hex+0x16≠0이면 x5000/100) [+ 불 칸 x5000/100] — 옛 2AE6F0 | - | core/path.cpp:13, rules/battle.cpp:190 | worldmap_spec.md §4.1; command_audit.md §15 | 확정 |
| `2B2390` (2B00D0) | 부대 수집(이동 case 7·8 앞) | 이동 갱신 앞에서 부대를 모아 2DC550(50개 청크)에 넘김 | - |  | lane_L4.md §2 | 확정 |
| `2B24D0` (2B0210) | 진형 기동력 | 진형 +0x7F(mobility) 또는 특수 진형이면 가상함수+0x48(상한 30); 세력+0x193 bit1 && 진형5면 +2 — 옛 2B0210 | - | rules/battle.cpp:185 | dump_measurements.md:176 | 확정 |
| `2B2550` (2B0290) | 부대 기동력 계산(이동점수 입력 F) | F=(정책% x 진형기동/100) x (1+5 x clamp(능력변경 슬롯 4+19,±10)/100) x (1+5 x army+0x4A/100) x (240/BF1B0(지형1)) x 2B6F80 x (세력+0x193 bit3 …) x (설정 130/100 수상). 새 빌드에 효과 0x30 지형 항 추가 — 옛 2B0290 | 입력: 부대. 출력: float F | core/path.cpp:12, rules/battle.cpp:157, rules/battle.cpp:180 | dump_measurements.md:175~; build_remap.md | 확정 |
| `2B7450` (2B50D0) | 부대 목표 칸 산출 | 목표 종류(5 거점·6·9 칸·0xB·0x1B 부대 id)를 읽어 매번 목표 칸을 재산출 — 옛 2B50D0 | - |  | approx_inventory.md | 확정 |
| `2B7BC0` (2B5840) | ZOC 점수 | ZOC=300·n1+5·(n2-n1)+5·(n3-n2)+5·(H-n3). 개성 효과 51 있으면 0. n=반경 1,2,3 적 부대 수(26D240), H=반경 1~3 적대 소유 칸 수 — 옛 2B5840; 상수 141A4BC78=300, 141A4BC84=5(옛 141A48C2C/C38) | 입력: 부대. 출력: ZOC | core/sim.h:108, rules/battle.cpp:147, rules/battle.cpp:180 | worldmap_spec.md §4.3 | 확정(덤프 이동량 반감) |
| `2DB9A0` (2D95F0) | 부대 일 처리 이동 갱신(한 걸음) | 이동점수 누적·칸 비용·경로 재계산·도착 분기·말미 29F660(적령개발감소) 처리. 막히면 +0x48=0xBD10 후 303EA0 재설정 — 옛 2D95F0; 엔진 update_units 이동 | 입력: 부대 | rules/battle.cpp:15, rules/battle.cpp:16, rules/battle.cpp:162 | lane_L4.md §2; worldmap_spec.md §4.1 | 확정 |
| `2DC550` (2DA1A0) | 이동 50개 청크 호출 | 2B2390(부대 수집) 뒤 부대를 50개 청크로 2DB9A0에 넘김 — 옛 2DA1A0 | - |  | lane_L4.md §2 | 확정 |
| `2E3BC0` (2E1800) | 보류 명령 확정(case 4) | 부대의 보류 명령(+0x140..0x142)을 행동·목표(+0x37/+0x38/+0x3A)로 확정 | - |  | lane_L4.md §2 | 확정 |
| `2EC570` (2EA1B0) | 퇴각 명령 설정(행동 0xB/0xC) | 사후명령 1 퇴각을 행동으로 설정 — 옛 2EA1B0 | - |  | lane_L4.md | 확정 |
| `303EA0` (301AB0) | 다음 칸·경로 캐시 재계산 | 막힘 시 다음 칸 +0x48·경로 캐시 재계산(하루 한 번 우회) | - |  | approx_inventory.md A2; worldmap_spec.md §4.1 | 확정 |

### 2.3 보급·병참

| 새 RVA (옛) | 이름 | 역할·식 | 입출력 | 엔진 위치 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `234DE0` (233440) | 특정 목록 소속 부대 면제 판정 | 보급·정기 사기 감소·ZOC 판정에서 면제되는 부대 목록 | - |  | worldmap_spec.md §2.1 | 추정(목록 의미 미해독) |
| `268070` (2666C0) | 정기 사기 감소량 | 감소 = 지형 정기 감소값(2B2330, 칸의 지형 +0x40; 숙련이면 설정 #27 %) + 단절이면 9(141A4C044). 정책 효과 0x2B가 난수보다 크고 2CACA0 참이면 0 — 옛 2666C0 | 입력: 부대, 연결 여부. 출력: 감소량 |  | worldmap_spec.md §2.3; command_audit.md §15 | 확정 |
| `26AD80` (2693D0) | 부대 군량 소비 캐시(모드 1) | 2DEE10→26AD80→26AF80 경로의 부대별 캐시 | - | rules/battle.cpp:29, rules/battle.cpp:32, rules/battle.cpp:139 | lane_L2.md | 코드 |
| `26AF80` (2695D0) | 부대 군량 소비 | 기본 max(1,(병사+부상병)x40/30/10) x (100-칸 +0x19)/100 → 정책 0xB·부대 0x14 항 → 적 영토 항(정책 0x43 x 난이도 배수 1.5/2.0) → 숙련이면 설정 #41 %. 새 빌드에서 효과 0x40 항 삭제 — 옛 2695D0 | 입력: 부대. 출력: 소비 군량 | core/sim.h:128, rules/battle.cpp:29, rules/battle.cpp:32 | worldmap_spec.md §2.3; build_remap.md §2 | 확정 |
| `272720` (270E00) | 5일 주기 사기 감소 | 44DEE0 case 0x12에서 날짜%5==0 && 칸 11이면 모든 부대(종류 1·2, 2CB6C0·234DE0 면제 제외)에 사기 -= 268070(부대, 연결?) — 옛 270E00 | 입력: 부대 목록. 출력: 사기(0이면 25A880 격파) |  | worldmap_spec.md §2.3 | 확정 |
| `278290` (276960) | 병참 연결 판정·효과(army_supply_update) | 연결 여부가 바뀔 때만 효과: 연결→단절 사기 -x(lv1 -15)·저지 40·혼란 60, 단절→연결 +15. 판정은 길 찾기 A*(185710→184D60)를 플래그 8로 — 옛 276960; 엔진 supply_link/supply_probe | 입력: 부대(+0x26 bit1). 출력: 사기·+0x23/+0x24 | rules/people.cpp:34 | worldmap_spec.md §2.1~2.2 | 확정(덤프 99.77 %) |
| `2AB620` (2A9430) | 무장 소속 거점 중심 칸 조회 | 무장 +0xE2 소속 거점 → 건물 +0x10(칸). 병참 연결 판정의 목적지 — 옛 2A9430 | 입력: 무장. 출력: 칸 | rules/worldmap.h:86 | worldmap_spec.md §2.1 | 확정 |
| `2B2330` (2B0070) | 지형 정기 사기 감소 getter | 칸의 지형 객체 +0x40(레코드 +0x2F)을 반환. 숙련이면 설정 #27 %. 268070이 호출 — 옛 2B0070 | 입력: 칸/지형. 출력: 감소 기본값 | core/sim.h:59 | worldmap_spec.md §0.4; command_audit.md §15 | 확정 |
| `2C8C00` (2C6850) | 보급 경로 칸 통과 조건 | 지형 비용≠0 이고 칸 소유자가 부대 세력에 적대가 아니어야 통과(목표 칸은 무검사) — 옛 2C6850 | 입력: 칸, 부대 세력 | rules/worldmap.h:81 | worldmap_spec.md §2.1 | 확정 |
| `2CB6C0` (2C9310) | 부대가 자기 거점 칸 위인가(보급 면제) | 거점 칸 위 부대는 보급·정기 사기 감소 면제 — 옛 2C9310 | 입력: 부대 | rules/worldmap.h:90, rules/worldmap.h:141 | worldmap_spec.md §2.1 | 확정 |
| `2DEAC0` (2DC790) | 거점 수비병 군량 정산 | 기본 X=max(1,((병+부상병)x10/30)/10), 태수 합 v(개성 0x46)로 감소 — 옛 2DC790 | - | core/sim.h:128, rules/battle.cpp:29, rules/battle.cpp:55 | lane_L1.md 개성 70; lane_L2.md | 확정 |
| `2DEE10` (2DCAE0) | 거점이 부대 군량 지불 | 거점 단위 부대 군량 정산 — 옛 2DCAE0 | - | core/sim.h:128, rules/battle.cpp:29, rules/battle.cpp:46 | lane_L2.md U1 | 확정 |

### 2.4 점령·칸소유

| 새 RVA (옛) | 이름 | 역할·식 | 입출력 | 엔진 위치 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `186E60` (185B30) | 칸 소유 쓰기 입구 set_owner | 막힘 판정(2C8AB0) 통과 시 242C70으로 소유 쓰기, 지역 갱신 비트(DAT_142144b30), 화면 이펙트. 거점 칸이면 이벤트 0x1E/0x1F·242340 — 옛 185B30(+1 알림 호출); 엔진 Game::paint | 입력: 지도관리자, 칸, 새 세력, 이전 거점 세력, 표지. 출력: 변경 여부 | core/sim.h:108, rules/facility_game.h:30, rules/worldmap.h:17 | worldmap_spec.md §1.2 | 확정 |
| `1FD930` (1FC550) | 지역 점령 확정(지역 중심 + 링 1) | 지역 중심 칸 + 링 1(6칸)을 칠함. 링 칸 조건: 소유 다름·2C5C50 거짓·2C8AB0(지역필수=1) 통과. 담당관(+0x36)·개발방향(+0x72)·+0x6D 초기화. 계략 13의 실행(대상 종류 7 지역)과 같은 함수 — 옛 1FC550(호출자 1FA530/1F91A0) | 입력: 지역. 5,669B |  | worldmap_spec.md §1.2; command_audit.md 항목 4 | 확정 |
| `22E260` (22C810) | 대상 소속 세력 조회(지역이면 중심 칸 소유) | 지역 소유 = 지역 중심 칸(+0x3A) 소유 세력. 1FD930이 대상 종류 7(지역)에서 이 함수로 세력을 얻음 — 옛 22C810(자동 대응). worldmap_spec은 '22CC00/22E260 계열'로 적음 — 22CC00은 이 함수의 옛 번호가 아님(충돌 참조); 엔진 region_owner | - |  | worldmap_spec.md §1.1; command_audit.md 항목 4 | 확정(호출 관계)/추정(함수 경계) |
| `22E650` (22CC00) | 지역/칸 소유 세력 조회(옛 문서 표기 22CC00 계열) | 지역 소유 = 지역 중심 칸 소유 세력. 옛 문서(pre6_occupation §4)의 함수 — 새 22E650(자동 대응) | - | rules/battle.cpp:84 | worldmap_spec.md §1.1; pre6_occupation.md | 추정 |
| `242340` (2409A0) | 소속 거점 갱신 | 마을·도시·관문·항(지형 15~18) 칸 소유 변경 시 거점 소유 연동 | - |  | worldmap_spec.md §1.2 | 코드 |
| `242C70` (2412D0) | 칸 소유 raw 쓰기 | 0x33 중립은 0, 이민족 0x2E~0x32는 조건부로 hex+0x14에 씀 | - |  | worldmap_spec.md §1.2 | 확정 |
| `26EEB0` (26D590) | 거점 점령(함락) 적용 | 거점 함락 시 소유·시설 이전·링 칠하기(2E1A50) 호출 본체(1,720줄) — 옛 26D590 | - | rules/battle.cpp:75, rules/battle.cpp:84, rules/combat_formulas.h:169 | worldmap_spec.md §1.2; pre6_occupation.md | 확정 |
| `285DB0` (284010) | 세력 멸망·청소 처리 | 멸망 시 칸·부대 청소 — 옛 284010 | - | rules/battle.cpp:67, rules/battle.cpp:69 | worldmap_spec.md §1.2 | 코드 |
| `294670` (292760) | 외교 변화 칸 재칠하기·보급 재판정 | 동맹·종전 등 변화 시 상대 칸 위 부대 칸을 새 관계로 다시 칠하고 모든 부대 보급 재판정(278290) — 옛 292760 | - |  | worldmap_spec.md §1.2 | 코드 |
| `29F660` (29D750) | 적령개발감소(정책 효과 0x16) | 부대 한 걸음마다 서 있는 칸 지역이 비동맹 세력의 것이면 상업·농업·병영(+0x3C/+0x3E/+0x40)을 141A4BCB0 % x 효과값만큼 감소 — 엔진 미구현 | - |  | lane_L4.md 20 | 확정 |
| `2AF740` (2AD410) | 몸 모양 병력 단계 임계 | 진형 +0x70/+0x71(레코드; 객체 +0x80/0x81) x100 임계로 1/3/5칸 단계 결정(지휘관 개성 0xE로 하향) — 엔진 Map::formation_n0/n1 | - | core/sim.h:59, rules/worldmap.h:47 | sim.h 주석; RULES.md S1 | 확정 |
| `2C8AB0` (2C6700) | 칸 막힘/칠 가능 판정 claimable | 지형 비용 0 불가; 격류(24)는 세력+0x15E∈{12,13,17,18}만; 거점 건물은 중심 칸·비적대; 함정(클래스4) 외 시설 칸은 불가(방벽은 표지7≠0 예외) — 옛 2C6700; 엔진 Game::claimable | 입력: 칸, 지역필수, 세력, 시설허용 | core/path.cpp:11, core/sim.h:108, rules/facility_game.h:31 | worldmap_spec.md §1.2 | 확정 |
| `2D53F0` (2D3040) | 부대 생성(출진) | 새 부대가 선 그 칸 1개를 칠함 — 옛 2D3040 | - |  | worldmap_spec.md §1.2 | 확정 |
| `2DA030` (2D7C80?) | 새 세력 생성(독립) | **정정(2026-11-17, 새 빌드 디컴파일)**: `2DA030(무장, 거점, 1, 0, 지정 번호)` = 빈 슬롯 `2AB710`을 골라 그 무장을 군주로 새 세력을 만들고, 거점 태수(`+0x2E`)를 바꾸고 거점 칸 소유를 넘김(`186E60` 호출은 이 이전 때문). 호출자 `2A6730`·`2E8100`(독립 추정)·이벤트 `SExecNewForce` `3A30A0`·`SExecNewForceResult` `3B5890`. 옛 "지역 없는 칸 위 부대 칠하기"는 옛→새 주소 대응 오류로 보임 | - |  | rules_tribes.md 16절 | 확정 |
| `2E1A50` (2DF720) | 거점 함락 링 칠하기 | 거점 중심에서 링 N(도시 4·관문 3)과 점령 지역 중심 링 R_area, 같은 지역 번호 칸만 — 옛 2DF720; 엔진 paint_disk_same_area | 입력: 중심 칸, 세력, 반경 | core/sim.h:108, rules/battle.cpp:84, rules/worldmap.h:19 | worldmap_spec.md §1.2 | 확정 |
| `301D00` (2FF910) | 부대 몸 모양 칠하기 | case 0xB(303020 경유): 병력 단계 1/3/5칸을 자기 칸 + 뒤쪽 칸에 칠함(18A190 footprint) — 엔진 paint_footprint | - | rules/worldmap.h:46 | lane_L4.md §2; RULES.md S1 | 확정 |

### 2.5 시설·건설

| 새 RVA (옛) | 이름 | 역할·식 | 입출력 | 엔진 위치 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `43720` (42B40) | 시설 지형 허용 비트마스크 판정 | 시설 정의 +0x2E(u32)를 지형 id 비트로 판정 — 옛 42B40 | - |  | worldmap_spec.md §3.1 | 확정 |
| `18F9D0` (18E640) | 교전 쌍·시설 효과 일일 처리(case 0xE) | 190BC0 초기화 → 190E10이 완성 class 2 수집 → 192110 | - | rules/facility_game.h:69 | lane_L3.md; lane_L4.md | 확정 |
| `18FB90` (18E800) | 함정 처리(case 0x16, 12회/일) | 190F60이 완성 class 4 수집 → 2B0460(칸, 범위)로 범위 안 군대에 2CC630 판정 후 효과 — 효과 종류 의미 일부 추정 | - | core/sim.h:44, rules/battle.cpp:194, rules/facility_game.h:51 | lane_L3.md | 확정 |
| `190E10` (18FA80) | 완성 class 2 시설 수집 | 18F9D0 하위: 완성(+0x16 bit0)된 class 2 시설을 모음 | - | rules/facility_game.h:70 | lane_L3.md | 확정 |
| `192110` (190D80) | 시설 효과 적용(class 2, 시설마다) | 18F9D0→190E10이 모은 완성 class 2 시설마다 호출 | - |  | lane_L3.md | 확정 |
| `192AF0` (191760) | 시설 효과 처리 관리(class 2) | 완성된 class 2 시설을 모아 시설마다 192110: 2AD8F0이 대상 목록, 거리 범위 [+0x2B, +0x2C] — 옛 191760 | - | rules/facility_game.h:71, rules/facility_game.h:95, rules/l1_effects.h:87 | lane_L3.md | 확정(구조)/미해결(효과 의미) |
| `1F5680` (1F42B0) | 건물 내구 설정(set_durability) | +0x14 = clamp(값, 0, 최대). 새 내구값(증감 아님), 호출 95,313건/23년 — 옛 1F42B0 | 입력: 건물, 값 | rules/battle.cpp:400 | dump_measurements.md:8; worldmap_spec.md §3.2 | 확정(trace) |
| `27A8D0` (278FA0) | 건설 가능 최종 판정 | def+0x32가 0 아니면 건설 담당 목록에서 번호(석병팔진 49) 검색. 시설 정의는 world+0x73958[id] — 옛 278FA0 | 입력: builder ctx, 칸, 시설 정의 | ai/agent.cpp:25, core/sim.h:111, rules/facility.h:2 | worldmap_spec.md §3.2 항 9 | 확정(위치)/미해결(의미) |
| `27AAC0` (279190) | 건설 가능 칸 판정 | 칸 유효·시설 정의 지형 마스크·기존 시설(함정만 적 소유 덮어쓰기)·칸 소유(자기·적대·무주)·지역 시설 수<+0x6E·함정은 지역이 자기·간격(27DAF0)·해방 조건(2C6D40) — 옛 279190; 엔진 Game::can_build | 입력: 군단/부대 ctx, 칸, 정의. 출력: bool | ai/agent.cpp:25, core/sim.h:111, rules/facility.h:2 | worldmap_spec.md §3.2 | 확정 |
| `27DAF0` (27BD50) | 시설 간격 검사 | 새 시설 칸 거리 1~4 링의 기존 시설 중 클래스 ∉{3,4}의 간격값 ≥ 거리면 불가 | - | rules/facility.h:2, rules/facility.h:16, rules/facility.h:26 | worldmap_spec.md §3.2 항 7 | 확정 |
| `28A200` (288460) | 건설 착공 | 건물 레코드 생성(내구 1), 터 칸 칠하기, 비용 차감(2AD6C0, 부대 출발 거점 금) — 옛 288460; case 0xF(28A890) | - | core/sim.h:111, rules/facility_game.h:2, rules/facility_game.h:30 | worldmap_spec.md §3.2; worldmap_s4s6.md | 확정 |
| `2AD6C0` (2AB390) | 시설 건설 비용 | 시설 정의 +0x1F 비용을 부대 출발 거점(22BFE0) 금에서 차감(음수는 0) — 옛 2AB390 | - | ai/schema.cpp:200, rules/facility_game.h:2, rules/facility_game.h:18 | worldmap_s4s6.md | 확정 |
| `2AD8F0` (2AB5C0) | 시설 효과 대상 목록 생성 | 효과 칸 0·1의 대상 목록. 거리 범위 [+0x2B,+0x2C], id 15·17은 종류 10 대상 제외, 적대 종류 {1,2,3,4,10..14,0x10}=2CC630 — 옛 2AB5C0 | - | rules/facility_game.h:70, rules/facility_tables.h:6 | lane_L3.md | 확정 |
| `2B0460` (2AE130) | 범위 안 군대 수집 | 칸·반경 안 군대 모음(함정 판정) — 옛 2AE130 | - |  | lane_L3.md | 확정 |
| `2C6D40` (2C4990) | 시설 해방 조건 | 정책 효과 id(+0x23) 합(41E570)이 임계(+0x33) 이상일 것 (check_unlock=1일 때) — 옛 2C4990; 합계는 41E7B0이 계산(호출자 확인) | - | rules/facility.h:2, rules/facility.h:4, rules/facility.h:16 | worldmap_spec.md §3.2 항 8 | 확정 |
| `2CC1E0` (2C9E30) | 지역 시설 상한 검사 | 지역의 클래스 2·3·4 시설 수 < 지역 +0x6E — 옛 2C9E30 | - | rules/facility.h:25 | worldmap_spec.md §3.2 항 5 | 확정 |
| `2EA410` (2E8050) | 건설 일일 진행 | 건설 부대가 일하는 동안 매일 내구 증가: 진·요새 23, 망루 23~24, 군악대 21~24, 토성 32, 석벽 34, 함정 1 (부대 병력 약 3000, 정책 42 가능) — 옛 2E8050; 공급 9 x 증가 내구 x 10 / {90계열 3, 2계열 4, 50} 비용 항(CA) | - | core/sim.h:111, rules/facility_game.h:2, rules/facility_game.h:38 | worldmap_spec.md §3.2 | 확정(덤프 trace) |
| `300970` (2FE580) | 시설 효과 18 군량 감면 갱신 | 매 갱신 hex+0x19를 지우고 진·요새의 효과 18(30 %, 반경 2)을 범위 칸에 다시 씀 — 옛 2FE580 | - |  | worldmap_spec.md §2.5 | 확정 |
| `192AF0` (-) | 시설 효과 1 피해 | - | - |  | L2 3차 | 확정 |

### 2.6 전투·피해

| 새 RVA (옛) | 이름 | 역할·식 | 입출력 | 엔진 위치 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `16AC00` (169C50) | 교전 단계표 디스패처 | 169F2C 간접 분기표 단계 1~7: 175B70 → 16AFE0 → 16BB00 → 16B940 → 16B730 → 170D80 → 175950 — 옛 169C50; 단계 호출 지점 169F32/44/55/66/77/8B/9D = 새 16AEE2/16AEF4/16AF05/16AF16/16AF27/16AF3B/16AF4D(+0xFB0 환산; 16AEF4·16AF3B만 BUILD_25953386_COMBAT가 확인) | - | rules/battle.cpp:13, rules/battle.cpp:218, rules/battle.cpp:266 | REA combat_inputs.md; combat6.md §1; dump_measurements.md | 확정 |
| `16AFE0` (16A030) | 단계2 양쪽 능력 입력 M | 양쪽 M(통솔·병력·사기 공통 배율) — 옛 16A030 | - | rules/battle.cpp:266 | dump_measurements.md | 확정 |
| `16B180` (16A1D0) | 일반 공격 피해 normal_base | 공통 배율 x A 와 B로 한 방향 피해. 정책 효과 0x15(도시반격강화)·개성 0x44(견뢰)·0x38(등갑 반감) 항 — 옛 16A1D0 | 입력: A,B 등. 출력: 피해(word) | rules/battle.cpp:219, rules/battle.cpp:221, rules/battle.cpp:267 | combat6.md; lane_L1.md 개성 68; formation_mapping.md | 확정 |
| `16B730` (16A780) | 단계5 교환 | 16B180(normal_base)로 자기→상대 한 방향 피해, 결과를 출력 +0x20에 저장 — 옛 16A780 | - | rules/battle.cpp:267 | dump_measurements.md; combat6.md | 확정 |
| `16B940` (16A990) | 단계4 방어 입력 B | 양쪽 B: 2AC0A0. 도발 중 다른 부대에게 맞으면 방어 x0.8 — 옛 16A990 | - | rules/battle.cpp:266, rules/combat_formulas.h:69 | dump_measurements.md | 확정 |
| `16BB00` (16AB50) | 단계3 공격 입력 A | 양쪽 A: 상대가 부대면 2B4460(공군), 거점이면 2B4750(공성). 도발 대상에게 x1.5(+0x25>0) — 옛 16AB50 | - | rules/battle.cpp:266, rules/combat_formulas.h:38 | dump_measurements.md; command_audit.md | 확정 |
| `170D80` (16FDD0) | 단계6 전법 호출 | 전법(173DD0)을 일반 피해가 대상 병력보다 작을 때만 호출. 모드 CCZ 사이트(16AF3B) — 옛 16FDD0; 함수 경계 주의(ghidra_full: 170870 안 중간 지점) | - | rules/battle.cpp:306 | combat6.md; BUILD_25953386_COMBAT.md | 확정 |
| `171160` (1701B0) | 교전 참가자 만들기 | 병력>0, 상태 바이트 필터 후 교전 대상 수집 — 옛 1701B0 | - |  | lane_L3.md | 확정 |
| `171820` (170870) | 교전 대상 수집·선정(4,811B) | 반경 안 적대 군대·거점·시설 후보 생성. 처리 순서·집중/측면은 미해독 — 옛 170870 | - |  | approx_inventory.md C1; lane_L3.md | 확정(후보)/미해결(순서) |
| `175950` (1749A0) | 단계7 피해 적용 combat_apply_damage | 교전 결과를 병력·사기·부상병에 적용 — 옛 1749A0 | - |  | BUILD_25953386_COMBAT.md §1 | 확정 |
| `175B70` (174BC0) | 단계1 거점 내구 피해 | 대상이 거점이면 파성 내구 피해(2A0750→2BB240), 부대면 통과 — 옛 174BC0 | - | rules/battle.cpp:395, rules/battle.cpp:400, rules/combat_formulas.h:182 | combat6.md | 확정 |
| `17B9E0` (17AA30) | 일일 교전 단계표 러너 | 171160(참가자 만들기)→16AC00 단계표를 하루 1회 돌림(case 0xD, 칸 5) — 옛 17AA30 | - | rules/battle.cpp:266 | lane_L3.md; lane_L4.md | 확정 |
| `25A880` (258EE0) | 부대 격파(소멸) | 사기 0이면 즉시 호출; 격파 점수 1000(141A4CD64 x 10) — 옛 258EE0 | - | rules/battle.cpp:121, rules/battle.cpp:213, rules/battle.cpp:377 | command_audit.md; lane_L4.md U8 | 확정 |
| `2A0750` (29E840) | 내구 피해(공성·시설 전법) | 점수=141A4CD5C(18) x 피해 x 10/100, 원천 4 → 2BB240 종류 1 — 옛 29E840 | - | rules/battle.cpp:395, rules/battle.cpp:400, rules/battle.cpp:401 | command_audit.md §15 | 확정 |
| `2A3510` (2A15E0) | 타일 불 확산 | 타는 칸의 이웃(반경 1, 중심 제외=2A9C90) 중 계열≠0 이거나 부대가 선 칸이 후보. P=round(비율 x 이웃 최대 불/800) | - | core/sim.h:90, rules/battle.cpp:450, rules/battle.cpp:478 | command_audit.md §15 | 확정(식)/중간(배치) |
| `2A3CF0` (2A1DC0) | 타일 불 감쇠 | 모든 불 칸 -1(141A4C070), 틱당 감쇠 — 엔진 hex_fire | - | core/sim.h:90, rules/battle.cpp:450, rules/battle.cpp:474 | command_audit.md §15 | 확정 |
| `2AAF30` (2A8D40) | 전투 공통 배율 | 통솔·병력·사기 기반 공통 배율. 새 빌드에서 2B2A90(인접효과)을 호출 — 옛 2A8D40 | 입력: 부대/무장. 출력: float | rules/battle.cpp:218, rules/battle.cpp:224, rules/battle.cpp:266 | mechanisms_20261017/능력치.md | 확정 |
| `2AC0A0` (2A9E50) | 방어 입력 B | 양측 방어 입력(진형 방어 getter 2AC010 경유). 새 빌드 0x30 항 추가 — 옛 2A9E50 | - | rules/battle.cpp:219, rules/battle.cpp:256, rules/battle.cpp:266 | combat_inputs.md; build_remap.md | 확정 |
| `2AC5A0` (2AA2E0) | 파성 입력(군 공성력) | 파성 계열 입력. 새 빌드 0x30 항 추가(param_5 검사 없음) — 옛 2AA2E0 | - | rules/battle.cpp:256, rules/battle.cpp:399, rules/combat_formulas.h:8 | build_remap.md | 확정 |
| `2B2A90` (2B07C0) | 인접 지역 효과(adjacency) | 지역마다 100 x +0x68/+0x76 점수(+동맹 판정·마스크 +0x66). 컴퓨터 세력 난이도 값 4/4/4/16/24 %. 새 빌드: 숙련 모드에서도 난이도 값 적용(옛은 표준 모드만) — 옛 2B07C0(첫 5바이트 push r15→r14 변경); 엔진 adjacency_multiplier | 입력: 칸, 세력. 출력: 배율 | rules/battle.cpp:224, rules/difficulty.h:37 | difficulty.md 항 35; build_remap.md; BUILD_25953386_COMBAT.md 충돌 1 | 확정 |
| `2B4460` (2B21A0) | 공격 입력 A(부대 대상) | 상대 종류 27(공군) 공격 입력. 새 빌드: 정책 0x30 지형 항 (100+e)/100 추가(param_5!=0, e>0, 지형 +0x42∈{2,4}) — 옛 2B21A0 | 입력: param_5 | rules/battle.cpp:218, rules/battle.cpp:256, rules/battle.cpp:266 | combat_inputs.md; build_remap.md | 확정 |
| `2B4750` (2B2440) | 공성 입력(거점 대상) | 상대 종류 5/6 거점형 공격 입력(공성). 새 빌드 0x30 항 추가 — 옛 2B2440 | - | rules/battle.cpp:218, rules/battle.cpp:256, rules/battle.cpp:266 | combat_inputs.md; build_remap.md | 확정 |
| `2E56C0` (2E3300) | 단기접전(행동 0x11, case 3) | 거리 ≤3, 결과로 사기 ±20(141A4BD28/BD34)을 271E70으로 적용, 0이면 격파 | - | rules/l1_effects.h:9 | lane_L4.md §2 | 확정 |
| `2E5DA0` (2E39E0) | 타일 점화 | 타일 화염 점화(전법 17 178B80이 호출) | - | core/sim.h:90, rules/battle.cpp:326, rules/battle.cpp:349 | command_audit.md §15 | 확정 |
| `3045F0` (302200) | 부대 게이지·능력변경 갱신 | 혼란·저지·도발과 능력 변경 기간 감소. 병참 연결 부대의 전법 게이지 `+0x20..+0x22`도 `225710`으로 감쇠(rules_combat_effects.md 전법 게이지 감쇠) | - | rules/worldmap.h:144 | `30484B`·`3048B7` 및 `225710` | 확정 |
| `41E330` (41BFC0) | 진형별 계수 선택 | 반환 = 100 + 집계값 x 진형계수. 무효 소속·진형 0x13/0x14는 100 — 옛 41BFC0 | - | rules/combat_formulas.h:166 | mechanisms_20261017/능력치.md | 확정 |
| `41E4B0` (41C140) | 진형 소속 계수 진입 | 소속 객체·진형 번호를 골라 41E330에 위임. 통솔이 아니라 100 기준 계수(정정) — 옛 41C140 | - | rules/battle.cpp:185, rules/combat_formulas.h:40, rules/combat_formulas.h:166 | mechanisms_20261017/README.md(41C140 별칭 정정) | 확정 |
| `43E660` (43C2C0) | 불 피해(case 0x17) | B 칸(s∈{5,11})에 타일 불이 있는 칸 위 부대 피해 | - | core/sim.h:90, rules/battle.cpp:451, rules/battle.cpp:507 | command_audit.md §15; lane_L4.md | 확정 |
| `43F4C0` (43D120) | 독 늪 피해(case 0x18) | 독늪(지형 7) 위 부대 피해 | - | rules/battle.cpp:451, rules/battle.cpp:522 | command_audit.md §15; lane_L4.md | 확정 |
| `457C90` (455AA0) | 게이지·능력변경 기록 갱신(case 2) | 부대마다 3045F0(게이지·능력 변경 기록 갱신)·지역마다 304360. 게이지 하루 -4 감쇠 — 엔진 status_decay | - |  | lane_L4.md §2 | 확정 |
| `175DE0` (-) | 공격 후 효과 | 지역 황폐(치안 +0x54 쓰기)·우호도 | - |  | L2 2차 | 확정 |
| `233D70 / 233DA0` (-) | 소속 판정 | 233D70(무장) 소속 세력이 도적인가, 233DA0(무장) 소속 없는 이민족 무장인가 | - |  | L2 2차 | 확정 |
| `2B1B10` (-) | 연계 count 수집 | 연계(전법) 참가자 수 | - |  | L2 2차 | 확정 |
| `2BDFB0 / 2BDCD0` (-) | 부상병 전환 | 2BDFB0 전 거점 순회(`44DEE0` case 0x13, 날짜 % 10 이 3·6·9 인 소칸 1), 2BDCD0(거점) 풀 `+0x40` -> 병력 `+0x3C`(식 `min(풀, ((풀/400+20)*150)/20)` + 개성 0x2C, 사기 `+0x44` 혼합) | - |  | L2 3차; L3b | 확정 |
| `278990 / 429050 / 304090 / 16B180` (-) | 병참·월 경계 보조 | 278990 전 부대 병참 재판정(+정기 사기), 429050 월 1일 이벤트 단계(`25FA40`->`303020`->`278990(0)`->`2901A0`), 304090 칸 목표 행동 9 경로 지정(약탈 효과 아님), 16B180 꼬리 적용 범위(도시 공격 기술자 한정) | - |  | L2 2차 | 확정 |
| `374440` (-) | 단기접전 위력 산출 | 무력·나이·개성·능력변경 항. 식은 rules_combat.md §9.5 | - |  | lane_L2_5.md 1 | 확정(식) |
| `3747A0` (-) | 단기접전 해결 본체 | 후보 `2C6930`·상대 `2C6AE0`·일격 `376CC0`·라운드 `37BC70`·결과 `375340` | - | Game::duel_fight | lane_L2_5.md 1 | 확정 |
| `37BC70 / 375340` (-) | 단기접전 라운드 표 / 결과 | 5라운드 표를 먼저 만들고 합산, 사망·포획 굴림 | - | Game::duel_fight | lane_L2_5.md 1 | 확정 |
| `2CCC60` (-) | 단기접전 생성기 | `44DEE0` case 5, 하루 1회, 일반 교전 앞 — 옛 "무작위 이벤트" 오독 정정 | - | Game::duel_day | lane_L2_5.md 1 | 확정 |

### 2.7 전법

| 새 RVA (옛) | 이름 | 역할·식 | 입출력 | 엔진 위치 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `16C740` (16B790) | 전법 상성(적) | 적 대상 상성 계수. 아군·일부 효과의 16C5F0은 1 + (무력 또는 지력)/150(rules_combat_effects.md E3) — 옛 16B790; 16C5F0=옛 16B640 | - | rules/battle.cpp:220, rules/battle.cpp:327, rules/combat_formulas.h:156 | command_audit.md §12a | 확정 |
| `16E5E0` (16D630) | 전법 위력(치1) | 효과 치1 +0x66+칸. 치2는 16E670(+0x68+칸) — 옛 16D630 | - |  | command_audit.md §12a | 확정 |
| `16E820` (16D870) | 전법 상태 계수 | 시전 군대 +0x21≠0이면 1.0, +0x22≠0이면 141A4BBE4/100=1.4, 아니면 141A4BF0/100=1.8 — 옛 16D870 | - | rules/battle.cpp:220, rules/battle.cpp:312, rules/battle.cpp:327 | lane_L3.md C4 | 확정 |
| `170150` (16F1A0) | 전법 사용 게이트 | 순 간격(G+0x454≥3), 전법 자료 +0x15E&0x20, 시전 부대 +0x23(혼란), 170280(사정 안 대상), +0x20 — 옛 16F1A0; 엔진은 '쓸모 있을 때' 검사 제거 | - |  | lane_L3.md C3; worldmap_spec.md §5.1 | 확정 |
| `170280` (16F2D0) | 전법 대상 범위 | 시전 부대 칸 중심, 반경 1(자기 영역이면 2)의 후보 ∩ 전법 범위 집합(16BE90) — 옛 16F2D0 | - |  | worldmap_spec.md §1.4 | 확정 |
| `176F10` (175F60) | 전법 계략형(23) | 양=int(위력 x 상성 x 단계 x 16E820 x (170770(세력,2)?120:100)/100)을 세 게이지에 — 옛 175F60 | - | rules/battle.cpp:327, rules/battle.cpp:368 | command_audit.md §12a | 확정 |
| `1772D0` (176320) | 전법 사기 상승(15) | 양=int(위력 x 1.0 x 단계 x 16E820), 사기=min(세력 최대, 사기+양) — 옛 176320 | - | rules/battle.cpp:326 | command_audit.md §12a | 확정 |
| `177530` (176580) | 전법 능력 상승/하락(5~14) | 능력 칸 i=종류-5/종류-10, 기간=int(치1 x 상성 x 단계 x 16E820 x (1+정책 0x22/0x23/100)), 단계 ±치2, 병합 2EE790 — 옛 176580 | - |  | command_audit.md §12a | 확정 |
| `1778A0` (1768F0) | 전법 5능력 전체(21/22) | 5개 능력 칸 전부에 상승/하락 — 옛 1768F0 | - | rules/battle.cpp:326 | command_audit.md §12a | 확정 |
| `177B30` (176B80) | 전법 효과1 병사 피해 | 병사 피해(효과 종류 1). 칸 3 능력 변경 단계 x(1-5·단계/100) 항 — 옛 176B80 | - | rules/battle.cpp:219, rules/battle.cpp:222, rules/battle.cpp:258 | command_audit.md §12a | 확정 |
| `178530` (177580) | 전법 효과18 시설 피해 | 시설 내구 피해 — 옛 177580 | - |  | command_audit.md §12a | 확정 |
| `1788B0` (177900) | 전법 사기 하락(16) | 양=int(위력 x 상성 x 단계 x 16E820), 사기=max(0,사기-양) — 옛 177900 | - | rules/battle.cpp:326 | command_audit.md §12a | 확정 |
| `178B80` (177BD0) | 전법 화염(17) | 타일 화염 부여: int(위력 x (1+능력/150) x 1.8) + int(그 값 x 정책 0x13/100) — 옛 177BD0 | - | rules/battle.cpp:326, rules/battle.cpp:349 | command_audit.md §15 | 확정 |
| `178DF0` (177E40) | 전법 치료(20) | f=부상병 x 1.0/max(1,20-치1), f≤500이면 500, f x 단계 x 16E820, 병력+=f — 옛 177E40 | - | rules/battle.cpp:326 | command_audit.md §12a | 확정 |
| `179210` (178260) | 전법 상태 해제(19) | 혼란·저지·도발 게이지를 0으로 — 옛 178260 | - |  | command_audit.md §12a | 확정 |
| `179420` (178470) | 전법 상태 부여(혼란·저지·도발) | 양=int(위력 x 상성 x 단계 x 16E820 x (세력비트2?120:100)/100), 상한 120 + 2F0E50 저항 — 옛 178470 | - |  | command_audit.md §12a | 확정 |
| `1798B0` (178900) | 전법 효과 종류 분기 dispatch | switch(16E4C0(자료,칸))으로 종류별 처리: 1 피해, 2~4 상태, 5~9/10~14 능력 상승/하락, 15 사기↑, 16 사기↓, 17 화염, 18 시설, 19 정화, 20 치료, 21/22 5능력, 23 계략형 — 옛 178900 | 입력: 전법 대상 1건. 함수 경계 주의(1798A0 안 중간) | rules/battle.cpp:302, rules/battle.cpp:325 | command_audit.md §12a | 확정 |
| `179DE0` (178E30) | 전법 출력 적용(178E30 계열) | 전법 결과를 적용하는 출력 단계 — 옛 178E30 | - | rules/battle.cpp:287, rules/battle.cpp:379, rules/battle.cpp:385 | BUILD_25953386_COMBAT.md | 확정 |
| `2C5B00` (2C3780) | 상태 면역 판정(전 게이지) | 개성 면역(2C3780) — 옛 2C3780 | - | rules/battle.cpp:368, rules/combat_formulas.h:179 | command_audit.md §12 | 확정 |
| `2EE790` (2EC3D0) | 능력 변경 기록 병합(전법 5~14) | 능력 칸 하나: 단계 lv(+0x4A+i, -10..10)·기간 ld(+0x50+i, 0..0xF0). 같은 부호 (ld_old lv_old²+ld_new lv_new²)/lv², 반대 부호 /A+B//lv² — 엔진 combat::ability_change | - | core/sim.h:55, rules/battle.cpp:325, rules/combat_formulas.h:196 | command_audit.md §12a | 확정 |
| `2F0E50` (2EEA60) | 상태이상 저항 판정 | r=(대상 슬롯9 + 종류 슬롯 10/11/..) 기반 저항 — 옛 2EEA60 | - | rules/battle.cpp:313, rules/combat_formulas.h:178 | command_audit.md §12 | 확정 |
| `170150 / 173D00 / 174F40` (-) | 전법 사용 게이트·요청·실행 본체 | 170150 사용 검증(순 간격 3; 5번째 검사 `+0x20 == 0`), 173D00 요청 처리, 174F40 실행 본체(대상 부대 `+0x20..+0x22` 기록) | - |  | L2 2·3차 | 확정 |
| `2F0500 / 2C7340` (-) | 전법 간격 목록 | 2F0500 목록 길이 설정(관직 순위 레코드 `+0xB3`, 최대 5, 플레이어 세력만; `G+0x165D`), 2C7340(무장) 목록 안 + 간격 충족 판정 | - |  | L2 3차 | 확정 |
| `376CC0` (-) | 단기접전 발생 판정 | - | - |  | L2 3차 | 확정 |

### 2.8 개성·정책 효과

| 새 RVA (옛) | 이름 | 역할·식 | 입출력 | 엔진 위치 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `22DB30` (22C0F0) | 정책 효과 값 getter(person/force, id) | 특기·정책 효과 값(예: id 0x30). 방책판은 22C0F0 경로 — 옛 22C0F0 | - | rules/battle.cpp:223, rules/battle.cpp:328, rules/combat_formulas.h:9 | build_remap.md; worldmap_spec_b.md §5.3 | 확정 |
| `22DFD0` (22C590) | 정책 레벨 → 값 | 효과 표(표 26)에서 레벨의 값 — 옛 22C590 | - |  | worldmap_spec_b.md §5.3 | 확정 |
| `22E070` (22C630) | 개성 같은 효과 id 합산 병합 | 같은 효과 id를 첫 일치 값 [-100,2000]으로 잘라 합산 — 옛 22C630 | - | core/init.cpp:59 | worldmap_spec_b.md §5.2 | 확정 |
| `26BBE0` (26A2C0) | 부대 개성 효과 합산 26BBE0 | 부대 개성 슬롯 127(무장 + 부대 +0x64 36)칸 합산, 값 -100..2000 자름. +0xB4==-1이거나 27FCB0 참일 때 — 새 26BBE0 | 입력: 부대, 효과, 버퍼, 모드 | rules/battle.cpp:256, rules/battle.cpp:269, rules/combat_formulas.h:40 | lane_L1.md; command_audit.md §12b | 확정 |
| `26C070` (26A750) | 무장 개성 효과 합산(단독판) | 무장 +0x184 비트마스크 기반 합 | - | rules/l1_effects.h:89 | lane_L1.md | 확정 |
| `26C340` (26AA20) | 세력 정책 효과 합 계산 | 활성 군사·시정 무장 정책 레벨 합산 — 옛 26AA20 | - | core/init.cpp:110 | worldmap_spec_b.md §5.3 | 추정 |
| `27FCB0` (27DF10) | 개성 조건 평가기 | 0x65칸 함수 포인터 표(조건 바이트 +0xA4, 값 +0xA8)로 (종류, 값, 부대, 번호) 평가, 표가 NULL이면 거짓. 표는 34칸만 채워짐 — 옛 27DF10 | 입력: 무장, 개성, 칸, 목록 | core/init.cpp:67 | command_audit.md §12b | 확정 |
| `2AD610` (2AB2E0) | 효과를 가진 개성 객체 찾기 | 호출처가 +0xB4==-1을 따로 검사 — 옛 2AB2E0 | - | rules/battle.cpp:462, rules/combat_formulas.h:118, rules/l1_effects.h:45 | lane_L1.md | 확정 |
| `2B5120` (2B2DA0) | 개성 효과 합(주변 무장, 효과 id) | 효과 id별 개성 값 합. 군 효과 0x65 건너뜀 미구현(CA) — 옛 2B2DA0 | - | core/init.cpp:59, rules/l1_effects.h:25, rules/l1_effects.h:89 | command_audit.md #7; mechanisms_20261017/ | 확정 |
| `41E570` (41C200) | 소속 정책 효과 집계 | 세력 활성 정책 레벨 합(world+0x80880 index 표, 22DFD0 레벨→값). 시설 해방 조건·진형 효과가 사용 — 옛 41C200. 시설 해방 조건의 합계 함수는 이것이 아니라 41E7B0(아래). 두 함수 모두 26C340(세력 정책 효과 합 계산)을 호출 | 입력: 연결 객체, 효과 id | core/init.cpp:110, rules/rules.cpp:10 | formation_mapping.md; worldmap_spec_b.md §5.3 | 확정 |
| `41E7B0` (41C440) | 정책 효과 합(부호 없는 합 변형, 시설 해방 조건용) | (세력/연결 객체 vtbl+0x60, 효과 id)로 26C340을 불러 합을 반환. 호출자 2C6D40(시설 해방)·37210·40090·26E5E0·27BF20·2EA250 등. ghidra_full 확인(2026-11-07) — 옛 41C440(자동 대응; 지도 §3.2는 '옛 41C200'이라 적었으나 41C200의 새 번호는 41E570) | 입력: 세력/연결 객체, 효과 id. 출력: u64 합 |  | worldmap_spec.md §3.2 항 8; ghidra_full callers | 확정(호출 관계) |
| `2C6590` (-) | 주의 항목 채택 가능 검사 | 2EF700 채택 전 검사 | - |  | lane_L1_4.md; rules_people.md 9.6 | 확정 |
| `324E00` (-) | 주의 항목 비용 구조 | (항목, 군주) 비용 | - |  | lane_L1_4.md | 추정(비용 바이트) |
| `1DF490` (-) | 세력 경험 슬롯 가산 | (세력, 종류, 증가) 세력 +0x1C5+종류-1, 상한 99 | - |  | lane_L1_4.md | 확정 |

### 2.9 능력치

| 새 RVA (옛) | 이름 | 역할·식 | 입출력 | 엔진 위치 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `22FCD0` (22E240) | 부대 능력(S = 22E240(army,0)) | army 대장 무장의 능력 idx 0(통솔)을 22FCE0로 얻는 래퍼 — 옛 22E240(≒ 22FCE0 래퍼) | - | core/init.cpp:105, rules/combat_formulas.h:16, rules/combat_formulas.h:184 | dump_measurements.md:79 | 확정 |
| `231770` (22FCE0) | 실효 능력 조회 ability(person, idx, mask) | 기본 u8(+0xEC+idx) x 부상 계수(100/80/50/20) x 별도상태 + 명품(최대 1개, ≤10)+작위·관직·주의 가산; 매력+123번 레코드면 100; [1, 상한]. 새 빌드에 bit14 검사 추가 — 옛 22FCE0 | 입력: 무장, 능력 idx, 반영마스크(보통 0xFFF) |  | mechanisms_20261017/능력치.md; build_remap.md | 확정 |
| `2B50A0` (2B2D20) | 효과를 반영한 능력 | 능력 + 개성·정책 효과 반영 — 옛 2B2D20 | - | ai/schema.cpp:203, rules/people.cpp:21, rules/people.cpp:84 | mechanisms_20261017/함수별_증거.md | 추정 |

### 2.10 내정·경제

| 새 RVA (옛) | 이름 | 역할·식 | 입출력 | 엔진 위치 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `22C1F0` (22A7B0) | 거점 지불자(도시) | 관문의 부대·수비병 군량은 관문 칸이 속한 지역의 도시가 낸다 — 새 22C1F0 | - | rules/battle.cpp:30 | lane_L2.md | 확정 |
| `25FA40` (25E0A0) | 일일 지역 순회 | 지역 담당관마다 265F10(+거점 항 상한 25)을 구해 개체에 경험 지급 — 옛 25E0A0 | - |  | RULES.md P6 | 확정 |
| `2678C0` (265F10) | 난이도 일일 가산 | 컴퓨터 난이도 4일 때 + min(130% x 기본, 24)을 개체 경험으로(25E0A0 일일 지역 순회가 호출) — 옛 265F10 | - |  | difficulty.md 항 43; RULES.md | 확정(코드)/엔진 미구현 |
| `2684C0` (266B10) | 지역 개발 최종 보정 | 담당관·정책 보정 — 옛 266B10 | - | rules/rules.cpp:57 | lane_L1.md 개성 33~39 | 확정 |
| `268600` (266C50) | 지역 개발 기초 증가 | 상업·농업·병영 증가 배율 300→360(새 빌드 x1.2). 호출자 297070 — 옛 266C50 | - |  | build_remap.md §2; RULES.md | 확정 |
| `269760` (267DB0) | 거점 금·군량·병력 상한 | 도시 규모 +0xB8(1..4)로 금 50000x크기, 군량 100000x크기, 병력 {50000,70000,100000,150000}(이민족 본거지 250000/500000/300000). 엔진은 근사 한 가지 — 옛 267DB0 | 입력: 거점 |  | lane_L2.md S1 | 코드 |
| `26C760` (26AE40) | 치안 최종 보정 | 치안 최종 — 옛 26AE40 | - |  | mechanisms_20261017/함수별_증거.md | 확정 |
| `26C8C0` (26AFA0) | 치안 기초값(통솔) | 치안 기초값은 통솔 조회 — 옛 26AFA0 | - | core/init.cpp:65, rules/domestic_formulas.h:57, rules/rules.cpp:57 | mechanisms_20261017/능력치.md | 확정 |
| `297070` (295160) | 지역 개발 호출자(월 내정) | 지역 개발 종류 1/2/3은 지력/정치/무력 능력 사용 — 옛 295160 | - |  | mechanisms_20261017/능력치.md; command_audit.md §2 | 확정 |
| `2B5F50` (2B3BD0) | 소속도시 내구회복 특출(개성 43) | 내구 회복량 A=clamp(2 x (능력+난수),40,400)에 상주 무장 중 첫 non-zero 효과 — 옛 2B3BD0 | - | rules/l1_effects.h:120, rules/rules.cpp:66, rules/rules.cpp:70 | lane_L1.md | 확정 |
| `2BDFB0` (2BBC30) | 지역 병영 풀→병력 전환(case 0x13) | 2BDCD0이 거점 부상병 풀 +0x40 → 병력 전환 — 옛 2BBC30 | - |  | lane_L4.md; lane_L1.md | 확정 |
| `2BE030` (2BBCB0) | 거점 월 수입·모병 합산 | 지역 수입 합 → 세력 효과 가산(14032E430) → 담당관 정액(0x47/0x48) → 상한(금 vtbl+0xB8, 군량 +0xC0) — 옛 2BBCB0 | - | rules/rules.cpp:20, rules/rules.cpp:24, rules/rules.cpp:25 | dump_measurements.md:114 | 확정 |
| `2BECD0` (2BC950) | 지역 월 군량 수입 | 농업 기준 +0x46·담당관 정치·특성 0x25·정책 0x34·가을(월 7~9) x125/100·시설 플래그 +0x38&0x10 — 옛 2BC950 | - | rules/difficulty.h:13, rules/domestic_formulas.h:92, rules/rules.cpp:17 | dump_measurements.md:109~ | 확정 |
| `2BF200` (2BCE80) | 지역 월 금 수입 | 인구·치안(하한 50)·상업 기준 +0x44·영유칸 +0x68/+0x76·담당관 지력(겸임 배율)·특성 0x24·정책 0x35·난이도 배율 — 옛 2BCE80 | - | rules/difficulty.h:13, rules/domestic_formulas.h:73, rules/domestic_formulas.h:92 | dump_measurements.md:109~ | 확정 |
| `2BF6E0` (2BD360) | 지역 징병량 | (sqrt(인구) x 치안/100 + 단계계수 x 병영기준 +0x48 x (무력+100)/1000) x 영유/전체 / 부재 나눗수 x 5 x 순수/100. 엔진 약 0.5~0.6배(G1 미달 원인, 미확정) — 옛 2BD360; 엔진 domestic_formulas.h | 입력: 지역, 담당관(231770 무력) | rules/difficulty.h:20, rules/difficulty.h:25, rules/domestic_formulas.h:16 | lane_L2.md E2; RULES.md | 코드(식 구조)/미해결(일치) |
| `2E9640` (2E7280) | 거점 내구 수리(순마다) | 금 ≥100(141A499D4)이고 최대 미만·적 없음이면 금 100 써서 수리, 능력=max(태수 정치, …) — 옛 2E7280(호출 302FA0) | - | rules/rules.cpp:66 | dump_measurements.md:146 | 확정 |
| `303240` (300E50) | 훈련 처리 | 훈련 상승(540/270) — 옛 300E50 | - |  | command_audit.md #5 | 확정 |
| `304D70` (302980) | 지역 인구 갱신(월) | 월 내정 성장 중 인구 — 옛 302980 | - | rules/domestic_formulas.h:36, rules/rules.cpp:36 | command_audit.md §2; calendar.md | 확정 |

### 2.11 인사

| 새 RVA (옛) | 이름 | 역할·식 | 입출력 | 엔진 위치 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `16A4E0` (169530) | 공적 가산 AddMerit | 대기 점수에 난이도·정책 가산 포함, 호출 27곳(전법 명중 1798B0, 시설 건설 2EA410, 탐색 1DD4B0 등) — 옛 169530 | 입력: 무장, 점수 | core/sim.h:119, rules/people.cpp:328, rules/people.cpp:340 | command_audit.md §13~15 | 확정 |
| `1DD4B0` (1DC320) | 탐색 명령 | 탐색 실행(시간 비용 600 계열 가산 AddMerit 포함) — 옛 1DC320 | - | rules/people.cpp:1, rules/people.cpp:33, rules/people.cpp:35 | command_audit.md #11 | 확정 |
| `1ED620` (1EC280) | 공훈 지급 | 금 2500 + 명령서 1(최대 3명) | - | ai/schema.cpp:375, core/sim.h:27, core/sim.h:119 | sim.h S16; command_audit.md #9 | 확정(식) |
| `1ED8F0` (1EC550) | 공훈 승진 | 100금 + 명령서 1/명 | - | ai/schema.cpp:375, core/sim.h:27, core/sim.h:119 | sim.h S16; command_audit.md | 확정(식) |
| `1F16B0` (1F0300) | 명품 하사 | 명령서 1장, 받는 이 충성=min(100, L+min(50,가치)), 이전 소유자(군주 아님)는 L-가치-5. 충성식 2B20C0 — 옛 1F0300 | - | ai/schema.cpp:344, rules/people.cpp:70 | command_audit.md #22 | 확정 |
| `1F18E0` (1F0520) | 학습(전법 습득) | 무장 +0x130[10] 전법 습득, 전법서 재고 의존 | - | ai/schema.cpp:375, core/sim.h:28, core/sim.h:119 | command_audit.md #23 §13c | 확정(함수)/엔진 일부 구현(S16) |
| `1F2B10` (1F1750) | 관직 임명 루프 | 충성 += (옛 관직 rank - 새 rank) x 2(141A4B62C), 상승 100까지, 군주가 혈연·애호 아니거나 미워할 때만(충성 증감 1EEE10) — 옛 1F1750 | - | ai/schema.cpp:341, rules/people.cpp:64 | command_audit.md #7 | 확정 |
| `1F3C90` (1F28C0) | 포상 실행 | 충성 += min(9,(75-상성)/15+3+난수(0/1)), 상한 100, 금 100 + 명령서 1(2E340→1F28C0 옛) — 옛 1F28C0; 대상 선정 2EEA0(옛 2E340) | - |  | command_audit.md #8; RULES.md | 확정 |
| `233420` (231A10) | 후계자 선정(AI 룰베이스) | 5능력치 합 최대 선택 — 옛 231A10 | - |  | FIDELITY.md | 확정 |
| `279DE0` (2784B0) | 등용 판정(점수식) | 매력항·난이도 저항 e(60/65/70/70/70)·플레이어 가산(+10/+5/0). 상성·친족 항은 엔진 중립 — 옛 2784B0 | 입력: 군주, 대상. 출력: 성패 | rules/difficulty.h:31, rules/people.cpp:1, rules/people.cpp:23 | command_audit.md #10; difficulty.md 항 32 | 확정(식)/APPROX(상성) |
| `2801C0` (27E420) | 포박(포획) 확률 | 확률 배율(플레이어 포획자 3 이상 70%); 개성 0x39 포박확률증가, 0x36 포박 무효 — 옛 27E420 | - | rules/battle.cpp:88, rules/battle.cpp:121, rules/combat_formulas.h:147 | difficulty.md 항 34; lane_L1.md | 확정 |
| `282230` (280490) | 탐색 판정(재야 발견식) | 탐색 확률식. 명승·명품·금·경험치는 엔진에 없음 — 옛 280490 | - |  | command_audit.md #11 | 확정(식) |
| `28DF20` (28C180) | 후계 지명·수명 사망 계승 | 수명·사망·계승(덤프 보정 APPROX) — 옛 28C180; 28F910(옛 28DB70) 보조(알림 호출 추가) | - | python/bindings.cpp:29, rules/people.cpp:2, rules/people.cpp:281 | command_audit.md #26 | 코드 |
| `29F380` (29D470) | 충성 분기 하락 | 월%3==0, 경과 순 +0x454>36 인 월 1일(단계 19)에 충성<0x65·플래그 0x6000 없음·상태 조건 무장 0~3(미움 3~6) 하락. 혈연 제외(2CAE70 배우자, 2CBF80 의형제, 2CAE20 부모자식, 234880 애호, 278110) — 호출 42A430; 손실량 2690A0 | - | ai/agent.cpp:88, core/sim.h:85, rules/people.cpp:139 | command_audit.md #a | 확정 |
| `2A8010` (2A5E20) | 상성(원형 거리) | 원형 거리 최대 75, 충성 하락 제외 조건(<20) — 옛 2A5E20 | - | rules/people.cpp:23 | command_audit.md #a | 확정 |
| `2B20C0` (2AFE00) | 충성식(하사) | 하사 시 충성 변화 계산 | - | rules/people.cpp:70 | command_audit.md #22 | 확정 |
| `2DD610` (2DB260) | 턴당 공적 변환 | 대기 점수 → 공적 변환(자동) — 2DD7C0 동반 | - | core/sim.h:119, rules/people.cpp:328, rules/people.cpp:345 | sim.h S16 | 확정(함수) |
| `2DF350` (2DD020) | 장수 병력 배분(거점)·이탈 처리 | 거점 장수 병력 배분(DMs: 부상병 전환 아님). 0x4000 무장 충성 0 이탈 목록 처리(CA) — 옛 2DD020; 두 문서가 같은 함수를 다른 용도로 기술(충돌 아님·다기능) | - | rules/battle.cpp:126, rules/worldmap.h:19, rules/worldmap.h:30 | dump_measurements.md:9; command_audit.md §2 | 확정 |
| `2FA7C0` (2F83D0) | 포로 처분 | 포로 석방·처형·등용 — 옛 2F83D0 | - | rules/people.cpp:36 | command_audit.md #12 | 코드 |
| `2E9980` (-) | 포로 해방·귀환 | 포로를 원세력 군주 소속 거점으로 되돌리고 상태 4 로(호출 `823A50`·`2A1530`) | (포로, 표시) |  | L1 2차 | 확정 |
| `2A1530` (-) | 포로 월 탈출 판정 | 월 1일 이벤트 `42ABA0` 에서 부름. 확률 `2694A0`, 태수 개성 0x6B 포로 도주 저지 `27BE80` | - |  | L1 2차 | 확정 |
| `235F60 / 233600 / 22E450 / 230350 / 22C1F0 / 22DB30` (-) | 위치·소속 조회 모음 | 235F60 위치가 도시·관문인가, 233600 위치 분류(id = 위치 - 0x3D, 종류 0x1B), 22E450 무장 군단의 세력, 230350 세력 군주의 소속 거점, 22C1F0 장소 -> 지역 거점, 22DB30(세력, 효과) 세력 효과 값(세력 비트열 `+0x1CB/+0x1D5` + 효과별 고정 값) | - |  | L1 2·3차; L2 3차 | 확정 |
| `255F40` (-) | 포로 정렬 비교자 | +0xE8 충성이 낮은 쪽 우선, 같으면 `2694A0` 탈출 확률, 같으면 `+0x166` 입사연. 용도 미확인 | (a, b) |  | L1 2차 | 코드 |
| `27E480` (-) | 월 경계 건강 틱 | 무장 목록을 돌며 `26B920`(발병)·`26B5D0`(회복)·`26B500`(빈사 사망)을 굴리고 알림 목록 생성, 사망자는 `2979B0`(무장 제거·알림). 단계표 `141A64050` 8번 항목 `429C80` 이 tail-jump. 3.5KB | - |  | L1 3차 | 확정 |
| `2A8090 / 22EE70 / 233BE0 / 3FDAF0 / 3FDAE0` (-) | 인사 보조 함수 | 2A8090 나이(연 - 생년 + 1), 22EE70(무장, 종류) 소유 명품 종류 일치 값의 최댓값/합(상한 10), 233BE0 무장이 제 위치에 없음(부대·이동 중 등; 판단표 무장정보 항목 30), 3FDAF0(n, 분할, a, b, c, d) 날짜·카운터·인자 해시 난수 % n, 3FDAE0(a, b) a < b | - |  | L1 3차; L3b | 확정 |
| `2EF700 / 236F10` (-) | 세력 특전 항목 부여·초기화 | 2EF700(세력, 항목 id, 종류) 세력 `+0x1CB/+0x1DF` 비트열 부여(쓰는 곳 하나), 236F10 세력 초기화(비트열 비움 + 항목 1) | - |  | L1 3차 | 확정 |
| `2B6D90` (-) | 무장별 거점 병력 배분량 | `2DF350`(병력 배분·이탈 처리)·`2FAFD0`·UI 가 소비 | (무장) |  | L1 3차 | 확정 |
| `2331F0 / 26CB00 / 2BC0D0 / 22C0B0 / 297070` (-) | 효과 소비 함수 모음 | 2331F0(날수, 무장, 대상) 등용·탐색 일수 식(효과 0x12), 26CB00(세력, 무장) 첩보 비용(효과 0x77, 정책 0x26), 2BC0D0 능력 경험 가산(효과 0x4B), 22C0B0 지역 명성(효과 0x7B), 297070(거점, 모드, 출력) 소속 무장의 효과 0x2D·0x4A 최댓값 수집 후 지역 내정 | - |  | L1 3차 | 확정 |
| `26B920 / 26B5D0 / 26B500` (-) | 건강 판정 3종 | 발병 / 회복 / 빈사 사망 판정식(rules_people.md 9.1) | - |  | L1 3차 | 확정 |
| `27F250` (-) | 전투 후 무장 운명 | (무장, 종류, 공격 부대, 사망금지) 부대 괴멸 시 부상 등급 상승·전사 판정. 설정값 3ECFD0=0·사망 빈도=1 근사 | - | rules/people.cpp | lane_L1_4.md; rules_people.md 9.5 | 확정(구조·상수)/근사(설정값) |
| `27DD40 / 26B3F0` (-) | 월 자연사 판정 / 사망 확률 | 월 1일 자연사 굴림(첫 37턴 제외). 옛 사망연도 해시 근사를 대체 | - | rules/people.cpp | lane_L1_4.md; rules_people.md 9.2 | 확정 |
| `2979B0` (-) | 무장 사망 처리 | 사망 공용 처리(엔진 person_die) | - | rules/people.cpp | lane_L1_4.md | 확정 |
| `2B6D90` (-) | 무장 배분 병력(효과 0x2E) | 식 확정, 엔진에 무장별 배분 상태가 없어 미구현 | - |  | lane_L1_4.md | 확정(식) |
| `2BC0D0` (-) | 능력 경험 가산(효과 0x4B) | 식 확정, 구현 보류(덤프 23년 1인당 +0.4점) | - |  | lane_L1_4.md | 확정(식) |
| `266780` (-) | 무장 거점 복귀 | (무장,0,0) 소속 거점 +0xE2로 복귀 — 교역 귀환(CCmdActionCaravan)도 이 경로 | - |  | lane_L1_4.md | 확정 |

### 2.12 외교

| 새 RVA (옛) | 이름 | 역할·식 | 입출력 | 엔진 위치 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `235150` (2337B0) | 현재 플레이어 세력 판정 | 세계+0x871E8의 플레이어 세력과 같은 세력인가(난이도 분기·60일 재요청 제한) — 옛 2337B0 | - |  | difficulty.md | 확정 |
| `2719C0` (2700A0) | 우호도 변경 | 우호도 += delta, 0..200 clamp. 변경 함수는 이것→25A080 한 곳 — 옛 2700A0 | - | rules/facility_game.h:74, rules/people.cpp:206 | command_audit.md §2 | 확정 |
| `2C5C50` (2C38D0) | 같은 세력·동맹·속국 여부 | 계략 대상 세력 제외·지역 점령 링 칠하기 조건 등에서 쓰는 비적대 관계 판정 — 옛 2C38D0 | - | ai/schema.cpp:204, rules/people.cpp:91 | command_audit.md #19 | 추정 |
| `2CC630` (2CA280) | 적대 판정 hostile(owner, force) | 소유 0(무주)=적대 취급, 중립 0x33 적대, 이민족(0x2E~0x32)은 외교 상태 없으면 적대, 자기·동맹·정전·속국(force+0xEA+상대 하위 7비트≠0 / +0x194)은 비적대 — 옛 2CA280; 엔진 supply_hostile | 입력: 소유자, 세력. 출력: bool | ai/schema.cpp:67, core/init.cpp:97, rules/battle.cpp:148 | worldmap_spec.md §2.1 | 확정 |
| `2EE080` (2EBCC0) | 동맹 기간(force+0xEA+상대) 쓰기 | 하위 7비트=개월 | - | ai/agent.cpp:14, rules/people.cpp:228 | command_audit.md §2 | 확정 |
| `324540` (3224D0) | 외교 명령 디스패처(성공률) | type 4 친선·5 동맹·8 포로 반환·9 공격 요청·7 항복 권고 분기, 성공률·요구치 | - |  | command_audit.md #13~17 | 확정 |
| `324BC0` (322B30) | 외교 비율 함수 | 새 빌드에서 8번째 int 인자 추가(0이 아니면 투입 항 x [1A4B884]=70/100) — 옛 322B30 | - |  | BUILD_25953386_REMAP.md §5.1 | 확정 |
| `3261B0` (324100) | 공격 요청 병력 항 | 요청받은 세력 병력>3000 x 도시 수, 군량>30000 x 도시 수 | - | rules/people.cpp:238 | command_audit.md #15 | 확정 |
| `326ED0` (324E20) | 외교 수락 | 판정(808930) 후 수락, 효과 81F290이 종류별 함수 호출 — 옛 324E20 | - | rules/people.cpp:1, rules/people.cpp:204 | command_audit.md #a | 확정 |
| `824310 / 81F290` (-) | 외교 종류 0x13 효과 / 외교 결과 분기 | 외교 결과 분기 종류 4·5·6·7·8·9·0x13 | - |  | L1 3차 | 확정 |
| `2719C0 / 25A080` (-) | 우호도 변경 | 2719C0(자기, 대상, 변화량, 알림, 억제) 우호도 변경 + 알림, 25A080(세력, 세력, 변화량) 양방향 가감(0..200) | - |  | L2 2차 | 확정 |

### 2.13 계략

| 새 RVA (옛) | 이름 | 역할·식 | 입출력 | 엔진 위치 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `1E0440` (1DF2B0) | 계략 방어 항 | 진행 중 순찰 무장 방어 항(엔진 구현) | - | rules/people.cpp:86, rules/people.cpp:93 | command_audit.md §13g | 확정 |
| `1E0EB0` (1DFD20) | 계략 성공률 판정 | 성공 문턱(141A4BF**, 141A4C0**) 식 vs 난수 3FDAF0(100,…): 0 실패/1 성공/2 대성공. 결과 함수 1ECC20(10)/1ED280(11)/1ED1D0(12)/1ED040(13)/1ECF40(14)/1ECD20(0x14)/1ED110(0x18) | - | rules/people.cpp:82 | command_audit.md §10 | 확정(식 위치)/미해결(pow 인자) |
| `1FA530` (1F91A0) | 계략 종류 분기 | 종류(+0x70) 10→1FA640, 11→2000F0, 12→1FF7B0, 13→1FD930, 14→1FC530, 0x14→1FB170, 0x18→1FEF60. 상위 1DEBE0(CCmdActionStrategic 단계 22) → 합법성 1EB1C0 — 옛 1F91A0 | - | rules/people.cpp:82 | command_audit.md #19 | 확정 |
| `1FB170 / 1FC530 / 1FEF60 / 1ECD20` (-) | 계략 0x14·14·0x18 효과 | 1FB170 계략 0x14(지역 건물 내구), 1FC530 계략 14(지역 개발 최대 항목·치안), 1FEF60 계략 0x18(인발 표식 `+0x1C6..`), 1ECD20 계략 0x14 결과 구간 | - |  | L2 2·3차 | 확정 |
| `2F5AA0` (2F36B0) | 군사 조언(명령 창 문구) | (전략 문맥, action, *권함, *등급, params, 실행무장 id, 대상 id, …) → 문구 버퍼(UTF-16, 호출자가 `AC4B30`(short*)로 잰다). 메시지 하나를 골라 `30C380`/`30FC40`로 이름을 채우고 `197E50`로 쓴다. action 0x14(건물파괴): 대상 = 지역 id(< 0x1F5, `+0x6CAF0`), 등급 = `1ECD20`(실행무장, 지역, 0)(효과와 같은 함수), 등급 0이면 0x3336(불가), 아니면 0x3326(가능), 군사 정확도 난수(`3FDAF0`/`3FDAE0`)가 틀리면 반대 문구. 첫 명령 5바이트 `4C 89 4C 24 20`(mov [rsp+20],r9). 직접 호출자 26곳(명령 생성 `1F5870`·`1F67B0`·`1F71B0`·`1F7E10`·`1F8240`, 창 `0079B800..0079CD90` 등) | 입력: 위. 출력: 문구, 권함, 등급 | - | ghidra_full 1a4a447d 디컴파일·calls.tsv; AI_TacticsMod local128 훅(`native_building_destruction.inl` advice) | 확정(코드)/게임 미확인 |
| `1E0890` (-) | 계략 0x14 성공률 | 엔진 종류 20 구현(대성공 base 30 근사) | - | rules/people.cpp strat_* | lane_L2_4.md | 확정 |
| `1E1370` (-) | 계략 14 성공률 | 1E0890과 같은 꼴, 상수 미판독 | - |  | lane_L2_4.md | 미해결(상수) |
| `1FD930` (-) | 계략 13 효과 | 칸 소유 입구 186E60의 직접 호출자(5.7KB) | - |  | lane_L2_4.md | 확정(위치)/미해결(본문) |

### 2.14 이민족·도적

| 새 RVA (옛) | 이름 | 역할·식 | 입출력 | 엔진 위치 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `25DE00` (25C460) | 도적 출현 판정 | 월 1일 단계 21. 날짜 상태 +0x454>18, 도적·이민족 부대 7개 이하일 때 후보. 거점별 지역 치안(+0x54) 최저값으로 확률 clamp((100-최저)/나눗수,2,..)(나눗수 난이도 15/8/5/5/5); 후보 게이트 2AA640 — 옛 25C460. difficulty.md·RULES.md의 '거점 부대 회복'/'부대 +0x54' 명명은 정정됨(= 도적 출현·지역 치안) | - | rules/people.cpp:172 | command_audit.md §2, §4; difficulty.md 항 44(정정) | 확정(코드) |
| `25E7D0` (25CE30) | 도적 부대 생성 | 지역 치안 <61이면 3, <71이면 2, 아니면 1개 부대. 병력=250 x clamp(난수(n+10)…) — 옛 25CE30 | - |  | command_audit.md §4 | 확정 |
| `2607E0` (25EE30) | 이민족 공격 | 원작 상수 + APPROX(주기). 호출 2C4D40→2607E0→259310(세력 턴 상태 2) — 옛 25EE30(경과 턴 게이트 18/36/48/72는 difficulty 항 30) | - | rules/battle.cpp:404, rules/battle.cpp:411, rules/battle.cpp:426 | command_audit.md §2; lane_L4.md | 코드 |

### 2.15 AI 판단

| 새 RVA (옛) | 이름 | 역할·식 | 입출력 | 엔진 위치 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `1F380` (1F3A0) | BT 노드 cut(병참 절단) | 통솔≤64 그리고 지력≤64이면 실패하는 문턱 + 군세 행동 종류 8 제외 + 경로 설정 성공 조건 — 옛 1F3A0(노드 vtable 슬롯) | 입력: node, context |  | mechanisms_20261017/능력치.md; BUILD_25953386_COMBAT.md | 확정(문턱) |
| `37210` (366B0) | AI 건설 후보 함수(비용·구분·요구 조건 필터) | 별도 건설 군세(방식 5)의 후보. 세부 임계 미상 — 옛 366B0 | - |  | worldmap_spec.md §3.2 | 추정 |
| `43A50` (42E70) | 출진 명령 생성 | 군단 판단표 → 출진 명령 — 옛 42E70 | - | core/sim.h:25 | worldmap_spec.md §3.4 | 확정 |
| `61F10` (613A0) | 성 공략 군세(지역 공략) 계획 | 성 공략 군세 안: 진 건설 준비(72D30), 매 턴 구성원 초기화 전제(새 빌드에서 낡음) — 옛 613A0; 훅 안전(same-hook) | - |  | worldmap_spec.md §3.4; BUILD_25953386_COMBAT.md | 확정 |
| `69AB0` (68CE0) | 전투 DLL city_node(거점 점령 노드 Execute) | CExecuteFootholdOccupyNode.Execute. 새 빌드 본문에 troops 모드 8~10·0x16 분기 추가(동작 전제 변경) — 옛 68CE0(changed same-hook); 새 전용 27D490이 공격 부대 구성원을 적 요새 공격(action 6/kind 11)으로 재배정 | 입력: node, context, troops |  | BUILD_25953386_COMBAT.md §3 충돌 2; BUILD_25953386_REMAP.md | 확정 |
| `6AA10` (69BD0) | 요격·출진 실행 | 요격 실행(69BD0) — 옛 69BD0 | - |  | mechanisms_20261017/출진과요격.md; FIDELITY.md | 확정 |
| `72D30` (71D50) | 건설 준비(진 고정) | 시설=3(진) 고정, 후보 칸 BA100, 71140 명령 갱신 — 옛 71D50 | - |  | worldmap_spec.md §3.4 | 확정 |
| `B6F50` (B5EC0) | AI 부대 전력 | 2AAF30 공통 배율 x 병력/1000. 통솔 50 병력 10,000 사기 100 → 3,660 — 옛 B5EC0 | 입력: 부대. 출력: 전력 |  | mechanisms_20261017/능력치.md | 확정 |
| `BA100` (B9070) | 건설 후보 칸 선택 | 성 공략 건설 후보 칸 — 옛 B9070 | - |  | worldmap_spec.md §3.4 | 추정 |
| `173DD0` (172E20) | 부대 AI 전법 선택(750줄) | 후보 점수(효과 종류 가중 141A48A78/84/90)로 전법 선택. 규칙이 아니라 선택 가중치 — 옛 172E20 | - | rules/battle.cpp:329 | worldmap_spec_b.md §5.1 | 확정 |
| `1EDC30` (1EC890) | 출진 명령 실행 | 43A50이 만든 출진 명령을 실행 — 옛 1EC890; 모드 UI는 4AE150 | - | core/sim.h:25, rules/battle.cpp:63 | worldmap_spec.md §3.4; sim.h | 확정 |
| `4403E0` (43E030) | AI 관리자 초기화·활성 검사 | 세력→군단→군세→부대 순으로 행동트리를 돌리는 AI 관리자 입구. 정적 호출자 0건(작업 큐에 제출되는 `std::function` 썽크 `4590C0` 경유; 제출처 `44DD30`(COtherStrategyState 슬롯 5). 진행 상태 44DEE0은 부르지 않음; L3b 확정, 옛 "442200→44F2F0" 사슬 표기는 정정) — 순 도중 AI 재명령 없음(L4 A0) | - |  | lane_L4.md A0; calendar.md | 확정 |
| `4590C0 / 4591A0 (썽크)` (-) | AI 갱신 람다 썽크 | `mov rcx,[rcx+8]; jmp 4403E0`(4590C0) / `jmp 440B30`(4591A0). `std::function<void()>` `_Func_impl` vftable `13DB940`/`13DB908` 의 call 슬롯이며 ghidra 가 함수로 잡지 못해 `4403E0`·`440B30` 의 정적 호출자가 0건으로 보였다 | - |  | L3b(L3b 직접 바이트 스캔) | 확정 |
| `44DD30` (-) | COtherStrategyState 슬롯 5 (세력 턴 상태) | vtable `13DA440` 슬롯 5. 세력 객체 `+0x478`, 상태 `+0x470`: 0 = 작업 큐(`140934D60`, 객체 +0x480)에 `4403E0` 제출(이민족 세력 46~50 제외, 상태 -> 1), 1 = 완료 대기(`1409355E0`) 후 `FUN_140935D40`, 2 = 이민족 공격 `2C4D40`->`2607E0`->`259310` | - |  | L3b | 확정 |
| `44ED30 / 43C1A0` (-) | CUserStrategyState 슬롯 5 / 플레이어 쪽 AI 제출 | `44ED30`(vtable `13D9430` 슬롯 5) 상태 3 에서 `43C1A0` 호출: 상태 +0x66C 0 = 작업 큐(객체 +0x678)에 `440B30` 제출(`CGameState` +0x480 갱신·`CStrategyState +0x48C = 1`), 1 = 완료 대기 후 +0x470 = 4 | - |  | L3b | 확정 |
| `8EB70` (-) | CVariableGetGameDataNode | 게임정보 항목: 0 년, 1 월, 2 일(date +0x37), 3 순 카운터(G+0x454), 4/5 `G+0x1656/0x1657` 바이트가 가리키는 세력, 6 AI 설정 비율 | (항목, 컨텍스트) |  | L3b | 확정 |
| `B2CF40 / B2CC80` (-) | BT 엔진 초기화 / 고정 풀 구성 | 13칸 표(크기, 개수, 정렬 비트) = 메모리 풀. rulebase.md 7절 | - |  | L3b | 확정 |
| `56A40` (-) | CForceSetPurposeNode 실행 | 세력 `+0x4A` 에 행동방침(s8)을 쓴다 | (세력, 값) |  | L3b | 확정 |
| `70BE20..710250` (-) | 명령 가용성 함수 전수 | conditions.md "명령 가용성 함수 70xxxx 전수표"(사유 메시지 id 로 명령 확정, 메뉴 슬롯 순서) | - |  | L3b | 확정 |
| `6DA660 / 6DA980 / 6DCA10 / 6DCEF0 / 6DE230 / 6DFB50 / 6D8750 / 6D9DB0 / 6E0390 / 6E0540 / 6E0B40 / 6E1620 / 6E1BE0 / 6E2950 / 6DD230 / 6E06F0 / 6DEE10` (-) | 명령별 대상 목록 생성 | 포상 대상 / 첩보담당관 후보 / 외교 사자 후보 / 정찰 파견 무장 / 전법 습득 후보 / 정찰 대상 / 첩보 대상 / 명품 대상 / 동맹 대상 / 동맹 파기 대상 / 친선 대상 / 포로반환 대상 / 공격 요청 대상 / 교환 대상 / 이호경식 대상 1·2 / 공격 요청 대상 2(conditions.md) | - |  | L3b | 추정 |
| `6B0E70 / 6B5980 / 199E0 / 69DDA0` (-) | 정책 선택 비교자·적성 복사 | 6B0E70(a, b) 정책 항목 비교: 유효 분류 일치, 군주 칸 값(6B5980: 분류 3 max(+0x16A,+0x17C), 4 +0x17E, 5 +0x16E, 6 +0x180) 큰 쪽 우선, 같으면 분류별 가중(+8+분류*4)·1406CB660·1406CB420·정의 순서. 199E0 = 무장 적성 칸 0..9 를 구조체로 복사, 69DDA0 = 이 비교자로 정렬 삽입 | (a, b) |  | L3b 3차 | 확정 |
| `279DE0` (-) | 등용 평가 | 등용 성공 판정 전체 식(조건 53): 조기 종료(충성 100 이상·옛 군주·군주 신분·혈연) 뒤 `max(30,매력')x3/5 + (a25-aE)/5 - ((k+4)/2+18) x e x 5/100 + 45+(d0 mod 5) + 호감항(혐오 +15·친애 -15·포로 +15·혈연 +15) + 플레이어 가산(+10/+5/0) [+ 재야·포로 정책효과 10]` x m(의리 칸 k=-4/-3/-2 이면 1.5/1.3/1.1), 0..100 clamp, 성공 <=> d0 < 최종. 세부는 ai/conditions.md 53행 | (대상, 실행 무장, 난수 입출력) | rules/people.cpp recruit_chance(상성·혈연·의리 항은 중립 APPROX) | L3 5차 | 확정(식)/추정(혈연 분기 순서) |
| `282230 / 2826B0 / 281480 / 282060` (-) | 탐색 결과(재야·명승·명품·전법서·금) | 282230 재야 발견, 2826B0 명승 발견, 281480 명품·전법서 후보와 확률, 282060 금 발견. 조건 122(`B0AC0`)는 앞 3개를 사용. 종류별 식은 rules_people.md 5.1절 | (무장, 지역, 결과 출력) | rules/people.cpp | 현재 빌드 각 본문, `1DD4B0` 호출부, 한국어 메시지 0xC39F | 확정 |
| `22C5F0` (-) | 명승 값(발전 단계 환산) | 명승 객체: 칸 소유 지역의 개발 3종(+0x3C/+0x3E/+0x40)을 문턱 {100,300,600,1000}(`1413A9DDC`)으로 1..5 단계화해 합 s(3..15); 값 = max(1, int(b[Lv+1] x (100 - r[s]) / 100)); r = `244300`(+0x11 byte, 표 `337C40()+0x3C0[s]`), b = `244310`(난이도별 +0x16/+0x1A, 표 `+0x388[Lv+1]`); 정책 효과 0x13 이 켜져 있으면 x 효과/100. 호출자 `3E890`·`8FFA0`·`6D05F0`·`6DB750`·`6DD5C0`·`791400`·`7915D0`·`79A100` | (명승) -> int | - | L3 5차 | 확정(식)/추정(값의 용도: 발전 비용·소요 후보) |
| `92AE0 / 935F0 / 93480 / 2ABCD0 / 2ACDD0 / 2C9120 / 22C1F0` (-) | 주·지방 이점 조회 | `22C1F0` 지역 -> 도시(W+0xDD38); `935F0` 도시 +0xCE -> 주 표(W+0xDC80[23]); `92AE0` 주 +0x30(geo) -> 이점 표(W+0x85990[18]); `93480` 이점 기준 도시 수 cap(+0x95 또는 5원소 목록이면 vcall +0x48); `2ABCD0` 주의 도시 목록(W+0x90 중 +0xCE 일치); `2ACDD0(세력, 주)` 세력 소유 도시 수; `2C9120` 도시 획득 직후 소유 수 == cap 이면 `2C9B50`(달성 처리, 플레이어 알림) | - | - | L3 5차; ai/conditions.md 139행 | 확정(구조)/추정(이점 효과) |
| `2320D0 / 232030` (-) | 무장 개성 목록(9칸) | `232030(무장, i)` = i 번째 개성 번호, `2320D0` 이 0..8 칸을 W+0x7DD18[356] 개성 객체로 모아 목록으로 반환(번호 < 0x164 만). 조건 113·114·117·128 이 사용 — 이전 문서의 "관계 목록"은 오독. 원작 상한(2026-11-18 바이트 확인): `232030` 은 `2320AA` 의 `cmp ebx,5` 로 i>4 이면 0(칸 0..4 만 읽음), 개성 보유 검사 `2346A0` 은 9번 돌지만 `234737` 의 `cmp rbx,5` 로 칸 5 이상을 0 으로 본다, `226FBF` `cmp r12d,5`, 개성 선택 상태 `4A90B3`·`4A96D3` `mov [rbp-0x24],5`. 무장 읽기 `321FB4` 는 처음부터 9칸(`cmp edi,9`)을 복사한다. 개성 객체 표 `[2780F60]+0x7DD18+id*8`, id > 0x163 이면 칸 0. 모드의 9칸은 이 다섯 바이트를 9 로 바꾼다 | (무장, 출력 목록) | Map::trait_* | L3 5차 | 확정 |
| `A9D50` (-) | 조건 128 본문 | 지형 특기 개성 번호 68~76(수전·산전·숲전·오환·선비·흉노·강저·산월·남만)과 지형 id(`22FB60`) 대응표: 수전 14, 산전·오환·선비·흉노·강저 8~11, 숲전·남만 5·6, 산월 5·6·4·12·14 | (무장, 칸) | - | L3 5차 | 확정 |
| `234880 / 2343A0` (-) | 친애·혐오 판정 | `234880(a, b)` b 가 a 의 친애 목록(+0xC0 u16[8]) 에 있음; `2343A0(a, b)` b 가 a 의 혐오 목록(+0xD0 u16[8]) 에 있음. (이전 문서의 "혐오 234880" 은 오기) | (무장, 무장) | - | L3 5차 | 확정 |
| `2CB6C0 / 234250 / 234150 / 2341C0 / 2340D0 / 2342C0` (-) | 부대 거점 위 판정 / 이민족 소속 검사 5종 | 2CB6C0 부대가 거점 칸 위(주둔); 234250 세력, 234150 군단, 2341C0 거점, 2340D0 부대, 2342C0 무장의 소속이 이민족(세력 번호 46~50)인가(조건 135) | - |  | L3b | 확정 |
| `1EC080 / 1EC1C0 / 1EBE90 / 1EBF00` (-) | 무장 관계 판정(조건 161~164) | 의형제 2CBF80·배우자 2CAE70·부모자식 2C7FF0·형제 2CAE20·친애 234880(혐오는 2343A0) + `+0x16C >= 10` & 충성 `<= 98`; 1EBE90 은 항상 0; 1EBF00 은 칸/지역 제외 조건 | - |  | L3b | 추정 |

### 2.16 난이도·설정

| 새 RVA (옛) | 이름 | 역할·식 | 입출력 | 엔진 위치 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `3EC1A0` (3E9C90) | 설정 객체 접근 | 설정 객체(RVA 0x1A49C90) 접근자(+0x8 = 1A49C98) — 옛 3E9C90 | - |  | BUILD_25953386_COMBAT.md | 확정 |
| `3EC370` (3E9E60) | 난이도 getter | *(설정+0xE58)==0이면 설정+0x134, 아니면 +0x28. 0 초급..4 궁극. 호출자 47개 — 옛 3E9E60 | - | core/sim.h:105, rules/difficulty.h:4, rules/difficulty.h:6 | difficulty.md §1 | 확정 |
| `3EC920` (3EA400) | 숙련 옵션 항목별 값 배열 | 설정1·설정2 항목별 값 배열(기본값 3EEFE0, 거의 100) — 옛 3EA400 | - | rules/difficulty.h:13 | difficulty.md §1; BUILD_25953386_COMBAT.md | 확정 |
| `3ED7C0` (3EB2A0) | 게임 모드 읽기 | 설정 +0xE58(1 표준, 0 숙련). 쓰기 3EF660, 3ED810은 '==0' 판정 — 옛 3EB2A0; 3ED810=옛 3EB2F0 | - | rules/difficulty.h:6, rules/difficulty.h:38 | difficulty.md §1 | 확정 |

### 2.17 난수

| 새 RVA (옛) | 이름 | 역할·식 | 입출력 | 엔진 위치 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `3FDAF0` (3FB600) | 난수 roll(100, …) | 계략·충성 등 판정용 난수 굴림 — 옛 3FB600 | - | rules/battle.cpp:405, rules/battle.cpp:411, rules/battle.cpp:427 | command_audit.md | 확정 |
| `3FDFF0` (3FBB00) | 난수 bounded(n) | 32비트 프로세스 전역 상태 기반. 초기 시드·다른 소비처 미확보(엔진 Rng: seed 매핑 APPROX) — 옛 3FBB00 | - | core/sim.h:21, rules/rules.cpp:38, rules/rules.cpp:67 | sim.h 주석 | 코드 |

### 2.18 데이터 접근

| 새 RVA (옛) | 이름 | 역할·식 | 입출력 | 엔진 위치 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `22F830` (22DDA0) | 칸 번호 계산 | (객체 - 표[0]) >> 5 | - |  | worldmap_spec.md §0.2 | 확정 |
| `2AC010` (2A9DC0) | 진형 방어 getter | 진형 객체 +0x86(방어), 1..40 — 옛 2A9DC0 | - |  | formation_mapping.md | 확정 |
| `2B4A10` (2B2690) | 진형 공성 getter | 진형 객체 +0x84(공성), 1..70 — 옛 2B2690 | - | rules/combat_formulas.h:54 | formation_mapping.md | 확정 |
| `2B4AA0` (2B2720) | 진형 공군 getter | 진형 객체 +0x83(공군), 동적 경로 1..45 clamp — 옛 2B2720 | - |  | formation_mapping.md | 확정 |
| `2B4B30` (2B27B0) | 진형 파성 getter | 진형 객체 +0x85(파성), 1..60. 옛 REA는 '후보'였으나 DMs 80에서 확정 사용 — 옛 2B27B0(2B280C 분리 unwind 구간 주의) | - | rules/combat_formulas.h:185 | formation_mapping.md; dump_measurements.md | 확정 |
| `2A8C90 / 2A8D50 / 2B1DF0 / 2CA530 / 2CBF80 / 2CAE70 / 2C7B30 / 2C92A0 / 2CAE20 / 2C5ED0 / 2A8010 / 2343A0` (-) | 무장 관계 함수군 | 2A8D50(p1, p2, 플래그) 관계 점수, 2A8C90 상성 등급(경계 11/30/47), 2B1DF0 친족 배율(2), 2CA530 "서로 애호·혐오 없음 + 의형제 아님", 2CBF80 의형제, 2CAE70 배우자, 2C7B30/2C92A0 부/모 일치, 2CAE20(a, b) b 가 a 의 부모, 2C5ED0 형제, 2A8010 상성 격차(원형, 최대 75), 2343A0(a, b) b 가 a 의 혐오 목록 | - |  | L2 3차 | 확정 |

### 2.19 UI

| 새 RVA (옛) | 이름 | 역할·식 | 입출력 | 엔진 위치 | 근거 | 확신도 |
|---|---|---|---|---|---|---|
| `61D30` (611C0) | 부대 명령 목표 종류→행동 매핑 | 부대 명령 대상 종류를 행동(+0x37)으로 매핑 — 옛 611C0 | - | core/sim.h:30 | command_audit.md #2 | 확정 |
| `2F05A0` (2EE1E0) | 부대 경유지 채움 | relay 슬롯 Army+2C..+34(최대 5)를 채움 — 옛 2EE1E0 | - | core/sim.h:29, rules/battle.cpp:154 | sim.h 주석; command_audit.md #2 | 확정 |
| `7C8050` (7C5BA0) | CArmyButtonMenu(부대 명령 메뉴) | 부대 버튼 메뉴 10 행동 종류 — 옛 7C5BA0 | - | core/sim.h:30 | sim.h 주석 | 확정 |
| `2EE750 / 1C2610` (-) | 부대 방향 연출 | 방향 후보 중 현재 각도와 가장 가까운 것 — 규칙 아님 | - |  | lane_L2_4.md | 확정 |
| `1A0430` (-) | CArmyInfoLayout 초기화(지도 부대 깃발) | 슬롯 63, 레이아웃 `00_81_07_0400_unit_flag` 로드(870470) | 입력: 깃발 | - | ui_native.md §4.13 | 코드 |
| `1B00D0` (-) | 깃발 관리자 추가(vt+0x148) | 331780·14DAE0+0x210 확인 → 슬롯 42로 옛 깃발 제거 → 0x278 할당·19BB20·vt+0x1F8·vt+0x38 → +0x98 목록 | 입력: 관리자, 부대 | - | ui_native.md §4.13 | 코드 |
| `1B0B00` (-) | 깃발 관리자 제거(vt+0x150) | +0x98 목록에서 flag+0x1F0==부대 노드를 찾아 해제 | 입력: 관리자, 부대 | - | ui_native.md §4.13 | 코드 |
| `25DA10` (-) | 부대 등장 | +0x56 지연 1 감소(0 아니면 미등장) → 칸 결정 → 관리자 있으면 깃발 추가 → 1A4F50 → +0x26\|=0x42 → 칸+0x1C에 부대 번호(243610) | 입력: 부대, 0xBD10 | - | ui_native.md §4.13 | 코드 |
| `508270` (-) | 불러오기 레이아웃 재구성 상태 | 3번 단계: 2CB6C0()==0인 부대마다 깃발 관리자 vt+0x148 | 입력: 상태 | - | ui_native.md §4.13 | 코드 |
| `1B4750` (-) | 부대 행동 패널(unit_action_ot) | 지도 깃발이 아님; 1B4823에서 얼굴 1BA4E0 | - | - | ui_native.md §4.13 | 코드 |
| `375430` (-) | 표정 분류 | 0x13/0x15/0x18 상수 반환원 — 외교 종류 아님 | - |  | lane_L1_4.md | 확정 |
| `86E920` (-) | 레이아웃 리소스 로더 | 이름 해시 → common setting KTID → 자원 작업. 동기 경로는 완료와 초기화 슬롯을 처리 | 레이아웃, 논리 이름, 동기/비동기 | - | ui_native.md §2.1 | 확정 |
| `1A4FB0 / 869690 / 86CCF0` (-) | UI 이벤트 등록·디스패치 | 이벤트와 functor를 등록하고 이벤트 코드로 콜백 탐색 | 컨트롤, 이벤트 번호, functor | - | ui_native.md §3.1 | 확정 |
| `45D850` (45B620) | 무장 선택창 준비 | 원본 설정을 복사해 유형별 창에 저장 | 설정, 종류 | - | ui_native.md §4.3 | 확정 |
| `45E090` (45BE60) | 무장 선택창 열기 | `460F70`으로 열기 상태를 큐에 등록하고 `574750`을 지나 종료 결과 읽기 | 설정, 종류 → 결과 | - | ui_native.md §4.3 | 확정 |
| `217900` (216090) | 확인창 열기 | `2047F0`으로 확인 상태를 큐에 등록하고 `574750`을 지나 종료 결과 읽기 | 확인 메시지 → bool | - | ui_native.md §4.3 | 확정 |
| `574750 / 572FB0` (-) | 모달 응답 대기·완료 | 작업이 있으면 대기. 완료 시 상태 종료 값을 응답 객체의 결과로 변환 | 응답 객체, 완료 시 종료 상태 | - | ui_native.md §4.3 | 확정 |
| `885720` (-) | 메인 HUD 부모 초기화 | 작위 조건 조회, 3개 자식 구성 | CMainCmdLayout | - | ui_native.md §4.5 | 확정 |
| `885970` (883670) | 메인 HUD 자식 초기화 | 버튼·커서·강조·연결선 생성, 표시 순번과 논리 ID 매핑 | CMainCmdLayoutBase | - | ui_native.md §4.5 | 확정 |
| `881E70 / 88EBD0 / 88F1C0` (-) | 메인 HUD 접기/펼치기 | 상태 플래그, 6/7개 전용 연출, 토글 버튼 문자열 전환 | CMainCmdLayoutBase | - | ui_native.md §4.5 | 확정 |
| `4EAA10 / 52F8B0` (-) | 타이틀 메뉴 생성·클릭 분기 | 레이아웃 노드 8개에 행을 만들고 각 노드 번호를 클릭 값으로 사용 | CTitleState, 클릭된 버튼의 ID | - | ui_native.md §4.6 | 확정 |
| `44F9E0 / 881640 / 8816A0` (-) | 전략 HUD 입력 처리 | 그룹 버튼의 포인터를 찾고 하위 메뉴의 선택값을 입력 상태에 기록 | CUserStrategyLayout, UI 선택 컨트롤 | - | ui_native.md §4.9 | 확정 |
| `894DE0 / 88FCE0` (-) | 전략 HUD 하위 메뉴 | 7개 그룹별 항목을 구성하고 선택값을 하위 메뉴 `+0x31C`에 저장 | CSubCmdLayoutBase, 그룹과 행·선택값 | - | ui_native.md §4.9 | 확정 |
| `44ED30 / 451550` (-) | 전략 HUD 상태 전환 | 선택값을 소비하여 0A..32 명령의 전략 상태 또는 하위 자료를 생성 | CUserStrategyState, 선택값 | - | ui_native.md §4.9 | 확정 |
| `7EBE90` (7E9890) | 부대 명령값 선택 | 메뉴 ID와 대상 종류로 내부 명령을 구성 | CStrategyUnitTargetState, 메뉴 | - | ui_native.md §4.8 | 확정 |
| `27AC40` (-) | 매 순 건강 회복 | 특수 무장의 회복 확률을 굴리고 건강 등급을 한 단계 낮춤 | 세계 무장·명령 목록 | - | rules_people.md §9.1 | 확정 |

### 2.20 5차 묶음 추가 함수 (L1 주의, L2 단기접전·계략, lane_L1_5.md·lane_L2_5.md)

| 새 RVA (옛) | 이름 | 역할·식 | 엔진 위치 | 근거 | 확신도 |
|---|---|---|---|---|---|
| `2EF700` | 주의 항목 채택 | 세력 +0x1CB/+0x1DF 비트를 세우고 경험 칸·명령서를 지불(항목 1은 무료) | Game::doc_adopt | lane_L1_5.md | 확정 |
| `2C6590 / 324E00` | 채택 검사 / 비용 | 해금·경험 칸·명령서·제한 플래그·작위 상한 술어. 반환 1·2·3·4·7 구분 | Game::doc_check | lane_L1_5.md | 확정 |
| `22DA10 / 225E70 / 229A70` | 채택 수 / 구간 채택 수 / 확정 | 22DB30 56곳 중 채택 수·구간 수·군주 확정 경로 | Game::doc_count / doc_adopt | lane_L1_5.md | 확정 |
| `225A20 / 236F90` | 체크포인트 저장 / 복원 | 세력 +0x1C5..+0x1EE를 +0x1E9..+0x213에 백업·복원 | (저장 상태) | lane_L1_5.md | 확정 |
| `22AC70 / 2FCDB0 / 430500` | 마스크 해제 이벤트 | 채택 불가 항목의 마스크 해제 경로 | Game::doc_* | lane_L1_5.md | 확정 |
| `1F3C90 / 52FC0` | 포상 실행 / 주의 채택 명령 실행 | 포상은 명령 거점이 금 100×대상 수 + 명령서 1회당 1 | Game::reward / doctrine_action | lane_L1_5.md | 확정 |
| `3ECFD0 / 3EC410` | 설정 getter | +0xD0 표준 모드 옵션, UI 문구 10141 '부상 발생 유무' | - | lane_L1_5.md | 중간(필드 대응) |
| `376020 / 376A70 / 376FB0 / 376540` | 접전 장면 진입 / 사망 판정·허용 | 사망은 hp 0 뒤 허용 술어(혈연·애호·군주·포로 등) | Game::duel_fight | lane_L2_5.md | 확정 |
| `376CC0 / 374440 / 37BC70 / 375340` | 일격 확률 / 위력 / 5라운드 / 결과 | 5라운드 표 합산 뒤 사망·포획 굴림 | Game::duel_fight | lane_L2_5.md | 확정 |
| `376940 / 37CAE0 / 37BB90` | 쌍 목록 | 순 안 재대결 방지 목록 조회·추가·비움 | Game::duel_paired / duel_meta | lane_L2_5.md | 확정 |
| `430520 / 44B920 / 42FFA0→2E98F0→2E9820` | 순 시작 카운터 / 쌍 초기화 / 체력 회복 | 회복 = +clamp(무력/3, 5, 30), 등급별 상한 100/80/50/30 | Game::duel_turn_start / duel_recover | lane_L2_5.md | 확정 |
| `37AA90 / 37AB70 / 37B170 / 37AD40 / 2BBED0 / 225240` | 결과 적용 | 무승부 +15, 승자 +40, 패자 −30..−70, 경험·공적, 사기 가산 | Game::duel_apply | lane_L2_5.md | 확정 |
| `2C6930 / 2C6AE0 / 2A9680` | 후보 부대 / 상대 판정 / 반경 목록 | 반경·적대·부대 종류 술어 | Game::duel_day | lane_L2_5.md | 확정 |
| `234880 / 2343A0 / 2346A0 / 2C7810 / 2AD610 / 2A8090` | 애호·혐오·개성·나이 조회 | 접전 보정 항의 원천 | Game::duel_* | lane_L2_5.md | 확정 |
| `2B4750` | 공성 공격 입력(float) | 진형 공성값 × 진형계수 × M × 0.05 × (1+5×clamp(개성칸2+2A8160, ±10)/100) × (1+5×+0x4C/100) × 지형·정책 0x30 항. 시설 사격 `192AF0` 인자 확정: `2B4750`/`2AC0A0` 모두 rcx=rdx=대상 부대, r8=0, r9=부대 record, xmm0=M(2AAF30), stack `0x20`=1, `0x28`=0. `16B180` 호출: xmm0=A(2B4750 float), xmm1=`min(1, 내구/최대) × 191220(효과값) × 100`, xmm2=부대 int 값(내구 등), stack `0x20`=A, `0x28`=B(2AC0A0), `0x30`=피해 출력 포인터 | (기본 꺼짐 `TU_L3` 256; APPROX: M 문맥·정책 꼬리) | lane_L2_5.md 2; `192D48..192E08` asm | 확정(식·인자)/구현(기본 꺼짐) |
| `1E2170 / 1ED110 / 1FEF60` | 계략 0x18 | 성공률·결과·표식(+0x1C6 30일)·충성 −1·우호도 −5 | Game::strat_action 24 | lane_L2_5.md 3a | 확정 |
| `1E1370 / 1ECF40 / 1FC530` | 계략 14 | 성공률·결과·효과(개발 최대값 −X, 치안 −Y). 엔진 구현(기본 꺼짐 `TU_L2` 4096) | Game::strat_rate / strat14_action | lane_L2_5.md 3b; 2026-11-08 | 확정 |
| `42CF50` | 세력 순 시작 가상 슬롯 | 현재 세력을 골라 플레이어면 `2D6460`, 아니면 `2C3BD0`. 두 함수는 `186E60`을 직접 부르지 않고 점령 전이 `2A44C0`을 부른다 → 순마다 자유 칸을 칠하는 별도 규칙은 확인되지 않음(S9 모델은 근사 유지) | (미구현) | lane_L2_5.md 4b; 2026-11-08 재판독 | 중간 |
| `1E02A0` | 계략 14 감소량 X·Y | 성공 X = rand%(base+(지력−30)/dx)+b+5, Y = rand%(base+(지력−30)/dy)+b+4; 실패 Y만. 상수 `141A4C200..C284` | (미구현) | rules_diplomacy 5.3 | 확정 |
| `1FD930 / 1ED040` | 계략 13 효과·결과 | 담당관 `+0x36` 해임, `+0x72`·`+0x6D` 초기화, 중심+반경 1 칸을 시전 세력 소유로 (`186E60`). 엔진 구현(기본 꺼짐 `TU_L2` 8192) | Game::strat_rate / strat13_action | rules_diplomacy 5.3; 2026-11-08 | 확정 |
| `1EDC30` | 부대 act 14(약탈) 분기 | 목표 거점이 있으면 `2ECF00(부대, 9, 목표)`로 명령을 바꾼다. 자원 약탈 식은 없음 | (미구현) | rules_tribes 9 | 확정 |
| `32A7B0 / 337C40 / 2442F0` | 능력 경험 임계표 | `0000/experience_data_exce.bin`을 읽어 전역 `142780F50`에 101×5 u32 임계를 만든다 | (미구현) | rules_people 9.7 | 확정 |

### 2.21 일기토 장면·결과 보조 함수 (모드 수동 일기토 작업, 2026-11-22~23)

| 새 RVA (옛) | 이름 | 역할·식 | 엔진 위치 | 근거 | 확신도 |
|---|---|---|---|---|---|
| `37B170 / 37AD40 / 37AB70 / 2BBED0` | 결과 보조: 승자 / 패자 / 무승부 / 능력 경험(종류 0 승·1 패·2 무승부) | `37AA90`이 나눠 부른다. 인자·문턱은 rules_combat §9.5 "결과 보조 함수" | Game::duel_apply | rules_combat.md §9.5 | 확정 |
| `37B420 / 37B260` | 일기토 보고 / 기록 | 보고는 `37AD40`(넷째 인자 0·1)과 `37AB70`(무승부)이 부른다. 기록은 `37B170`·`37AB70`이 조건부로 부른다 | (장면) | rules_combat.md §9.5 | 확정(호출) / 역할 이름은 추정 |
| `37D040 (37ACF0) / 44AE60 (448C10)` | 일기토 끝 / 진행 중이면 끝내기 | 끝: 관리자 `*2786780`의 `+0x588`·`+0x10`을 0, `+0x590`·`+0x5A0`을 놓음. `44AE60`은 `+0x10`이 켜져 있으면 `37D040` | (장면) | ui_native.md §4.12 | 확정 |
| `37D930` | 일기토 칸 이동 | 칸 행동 `+0x10`으로 이동 목표 쪽·방향각 쪽(fps 보정 / 고정 걸음)·정지를 정한다. 방향각 이동은 높이에 상수만 더함 | (장면) | ui_native.md §4.12 | 확정 |
| `37A820` | 합 진행 상태 고르기 | 지금 합(`+0x4A8`)의 두 행 코드에 3이 있으면 0xE, 1이면 0xD, 그 밖 0xB → `374E00(관리자, 상태, 1)` | (장면) | ui_native.md §4.12 | 확정 |
| `809110 / 89D800 / 30E1B0 / 859660` | 대기 체력바 사본 / 개성 보임 검사 / 개성 글자 / 개성 색 | 사본의 개성 칸: 번호 1~0x163, `89D800(0x10, 번호)` 참, 0x57 제외, 최대 5개 | (장면) | ui_native.md §4.12 | 확정 |
| `8269A0 / 827D70 / 931B20 / BAAF50` | 체력바 갱신 / 합 숫자 / 그림 노드 / 땅 높이 | 일기토 게이지·그림 노드 | (장면) | ui_native.md §4.12 | 확정 |

## 3. 호출 체인

### 3.1 날짜 상태기계 `44DEE0`(옛 `44BCA0`) 전 case (lane_L4.md §2, 확정)

한 호출이 case 0..0x1F를 차례로 돈다(하루 12칸 시계, 칸 s=0..11). 조건: A=s∈{2,5,8,11}, B=s∈{5,11}, C=s==5, D=s==11이고 날짜%5==0, E=s==0이고 날짜%10==1, F=s==1이고 날짜%10∈{3,6,9}.

| case | 조건 | 새 RVA | 하는 일 |
|---|---|---|---|
| 0 | 매칸 | 2035D0 | 날짜 상태 비트 8·0x16일 때 이벤트 목록(1EC7D0) |
| 1 | E | 405A40 | 순 시작 결정 블록(1·11·21일) |
| 2 | A | 457C90 | 부대 3045F0(게이지·능력변경 기록 갱신)·지역 304360·+0x150 목록 33EB40 — 게이지 감쇠(엔진 status_decay 하루 1회 -4); s==3이면 458520 추가 |
| 3 | 매칸 | 2E38E0→2E56C0 | 단기접전(행동 0x11, 거리≤3): 사기 ±20(271E70) |
| 4 | 매칸 | 2E3BC0 | 보류 명령(+0x140..0x142)을 행동·목표로 확정 |
| 5 | C | 2CCC60 | 단기접전 생성기(하루 1회, 옛 "무작위 이벤트" 정정 — lane_L2_5) |
| 6 | 매칸 | 441F50/17B920 | 상태·UI 인터럽트 확인 |
| 7·8 | 매칸 | 2B2390→2DC550→2DB9A0 | 이동 한 걸음(50개 청크) |
| 9 | 칸 0 | 43C9F0 | 출진 대기열 부대 등장(CAppearArmyState) |
| 0xA | 매칸 | 2E6E00 | 병력<1000·사기<40 알림(규칙 없음) |
| 0xB | 매칸 | 303020→301D00 | 부대 몸 모양 칠하기 |
| 0xC | C | 2EA1D0→2EA130/296AA0 | 행동 10(지역 점령형) 지역 인수(덤프 0건) |
| 0xD | C | 17B9E0(→17AA30) | 일반 교전 하루 1회 |
| 0xE | C | 18F9D0(→18E640) | 시설 효과(class 2) 처리 [L3] / 교전 쌍 목록 처리 [L4] — 충돌 F6 |
| 0xF | 매칸 | 28A890→28A200 | 건설 착공 |
| 0x10 | C | 2EABE0→2EA410 | 건설 진행(일일 내구) |
| 0x11 | 매칸 | 2FF450 | 개성 조건(27FCB0) 부대 처리(미해독) |
| 0x12 | D | 272720 | 5일 사기 감소 |
| 0x13 | F | 2BDFB0→2BDCD0 | 지역 병영 풀→병력(징병) |
| 0x14 | A | 2A3CF0/2A3510 | 타일 불 감쇠·확산 |
| 0x15 | C | 2E6BD0→2E62E0 | 행동 0x10(철거) 처리 |
| 0x16 | 매칸 | 18FB90 | 함정(class 4) 처리 |
| 0x17 | B | 43E660 | 불 피해 |
| 0x18 | B | 43F4C0 | 독 늪 피해 |
| 0x19 | 매칸 | 4512A0 | 격파·점령 대기열 비우기(286B00/285DB0/25A880) |
| 0x1A | 매칸 | 2901A0·301AF0 | 부대 목록 청소·갱신 |
| 0x1B | 매칸 | 2902C0 | 소멸 부대 정리 |
| 0x1C | 매칸 | 276250→273AC0 | 부대 상시 옵션·목표 유효성(핵심) |
| 0x1D | D1 | 2FEE70 | 개성/능력 부대 처리(미해독) |
| 0x1E | 매칸 | 2D4630 | 미해독 |
| 0x1F | 매칸 | 1D4950/1D30C0 | 알림 큐 |

### 3.2 월 1일 이벤트 단계기계 `42FDC0`

단계표 `141A64050`/조건표 `141A642D0`의 0..0x4E 단계를 차례로 호출. 단계 2=`429030`→`25F060`, 19=`42A430`→`29F380`(충성 분기 하락), 21=`429000`→`25DE00`(도적 출현), 25=`42BB80`→`2A5140`. 조건 함수는 상태 +4 플래그(CA §2, 확정).

### 3.3 교전 단계표 `16AC00`(옛 `169C50`, 간접 분기표 `169F2C`)

`17B9E0`(case 0xD) → `171160` 참가자 → `16AC00`: ①`175B70` 거점 내구 피해/부대 통과 → ②`16AFE0` 입력 M → ③`16BB00` 공격 입력 A(`2B4460`/`2B4750`) → ④`16B940` 방어 입력 B(`2AC0A0`) → ⑤`16B730` 교환(`16B180`로 한 방향 피해→출력+0x20) → ⑥`170D80` 전법(`173DD0`, 일반 피해<대상 병력일 때만) → ⑦`175950` 피해 적용. 출처: combat_inputs.md 단계표, combat6.md §1, DMs. 새 빌드: ②~④와 `2AAF30`에 정책 0x30 지형 항 추가(BR §2), ⑦ 불변.

### 3.4 칸 소유(`186E60`) 호출자 (W §1.2, 확정)

부대 생성 `2D53F0`(그 칸 1개) · 거점 함락 `26EEB0`→`2E1A50`(링 N: 도시 4/관문 3) · 지역 점령 확정 `1FD930`(중심+링1, 호출자 `1FA530`) · 새 세력 생성(독립)의 거점 이전 `2DA030`(2026-11-17 정정, rules_tribes.md 16절) · 외교 변화 `294670` · 멸망·청소 `2A44C0`·`285DB0`·`28A200`. 날짜 상태기계에서 닿는 것: 몸 모양(case 0xB `301D00`)·건설 착공(0xF `28A200`)·진행(0x10 `2EA410`). 한 걸음마다 칠하는 사슬은 `303020 → 301D00 → 18A190 → 187450 → 186E60`(2026-11-17 해결, rules_tribes.md 16절). `18A190`은 `2CC630(22E690(부대), 칸 주인)`이 0(비적대)인 칸을 건너뛴다.

### 3.5 부대 명령 쓰기 경로 (2026-11-17, ghidra 1a4a447d 디컴파일 판독, 실게임 미확인)

- `2ECEA0(부대, 행동)`은 보류 명령 `+0x140`이 0일 때만 행동을 쓴다. 플레이어 보류 명령은 case 4 `2E3BC0`가 setter를 거치지 않고 `+0x37/+0x38/+0x3A`에 직접 확정한다. `2ECF00(부대, u8 종류, u16 목표)`가 목표를 쓴다.
- 명령 끝 처리 `2A3470` → `2EC570`(퇴각)·`2FFB00`(가까운 거점 목표, `2ECF00` 사용)·`306AF0`(제자리). `2EC570`·`306AF0`은 setter 없이 직접 쓴다. 자동 교전 `273AC0` → `2903E0`은 `+0x3C`(추격 목표)를 직접 쓴다.
- 게임 목록 준비 `1AC60(&목록)`: 목록 = {vtable `1346670`, handle 포인터}. `1FC530` 안의 인라인 준비와 같다. 해제 `1BFFF0(&목록)`.
- `2D53F0(지역 객체, 규모, &목록, 세력)` → 부대 또는 null. 지역 객체는 world `+0x6CAF0` 포인터 표(8바이트 칸, id ≤ 500, 객체 크기 0x98)에서 얻는다. `1FC530`: `2AA9E0(지역, &목록)` → `2D53F0(지역, 1, &목록, 세력)`.
- `22E690(부대)` 반환은 32비트: 끝이 `movzx eax, byte [rbx+10h]` 또는 `xor eax,eax`이고, 호출자 `22E2A0`(부대의 세력 객체)은 `cmp eax,33h; jg; cdqe; mov rax,[rbx+rax*8+0DF30h]`로 EAX 전체를 부호 있는 색인으로 쓴다(바이트만 맞고 윗자리가 더러우면 음수 색인 접근 위반). `2AA9E0(지역,&목록)`의 목록 값은 칸 객체(world `+0xE270` 포인터 표와 같은 객체, 색인은 `22F830(칸)`), 할당은 `18D50(27D4130, *handle, 1)`을 `27D4100`이 켜져 있으면 `27D4108` 임계 구역 안에서. `2D53F0`은 그 목록에서 지역이 맞는 칸을 `2B06B0` 순서로 정렬한 첫 칸에 부대를 놓으므로 칸 하나만 담은 목록을 주면 그 칸에 놓는다(디컴파일 판독, 실게임 미확인).
- `186E60`은 u64를 돌려주며 0이면 칸을 쓰지 않은 것. `25A880(부대, 죽인 부대, p3, int, int)`은 그 부대가 이미 제거 목록에 있으면 바로 돌아온다. 원작 이벤트 `3B2890`(SExecAnnihilateArmyUnit): `25A880(부대, 0, 0, 0, 4)` → `2901A0()` → `276250()`.
- 날짜 상태기계 호출 지점: `44E3A3`→`2E3BC0`(case 4), `44E4B0`→`2DC550`(case 8 이동, `2DC550`의 유일한 호출자), `44E517`→`303020`(case 0xB 몸 모양 칠하기 → `301D00`), `44E723`→`2901A0`, `44E736`→`276250`.
- `268070(부대, 연결?)` → 정기 사기 감소량(int), `2F03D0(부대, 종류, 값)`: 종류 0 = `+0x40`(접근 시 교전 0~2), 1 = 자주퇴각, 3 = 명령 끝난 뒤 행동(뜻은 디컴파일 추정).

## 4. 충돌 (둘 다 기록)

| # | 대상 | 한쪽 | 다른 쪽 | 판정·메모 | 출처 |
|---|---|---|---|---|---|
| F1 | 하루 점수 규칙 | 사용자 규칙: 하루 점수 = 표시 기동 | 코드·덤프: 하루 점수 = 12 x 갱신당 점수(표시 기동은 갱신 1회당) | 충돌(미해결): 표시 기동=갱신당 점수로 정정하면 모두 맞음. 엔진은 지시대로 TICKS_PER_DAY 36 유지; 권고 12 | dump_measurements.md:183 |
| F2 | `22CC00/22E260` | W §1.1: 지역 소유 조회 `22CC00/22E260` 계열 | resolver: 옛 22CC00→새 22E650, 새 22E260=옛 22C810 | 새/옛 쌍이 틀림. 함수 후보 둘 다 정리(추정) | worldmap_spec.md §1.1; functions.tsv |
| F3 | `41E7B0` vs `41E570` | W §3.2: 해방 조건 합계 `41E7B0`(옛 41C200) | build_remap: 41C200→41E570(변경 없음) | 두 함수가 모두 존재(41E7B0=옛 41C440). 해방 조건 합은 41E7B0(호출자 2C6D40 확인), 전투 소속 집계는 41E570. 지도 §3.2의 '옛 41C200'만 오기 | worldmap_spec.md §3.2; ghidra_full callers 41E7B0(2026-11-07) |
| F4 | `25C460`(새 25DE00) | difficulty.md:44·RULES.md:39: '거점 부대 회복/난수 이벤트 선택기', 입력 부대 +0x54 | command_audit.md §4: 도적 출현, 입력 지역 치안 +0x54 | 같은 함수. 도적 출현이 정정본(difficulty.md:102·build_remap.md:651도 같은 방향) | difficulty.md; command_audit.md §4 |
| F5 | `2DD020`(새 2DF350) | DMs:9: 거점 장수 병력 배분(부상병 전환 아님) | CA §2: 0x4000 무장 충성 0 이탈 목록 처리 | 한 함수가 두 용도를 가졌을 수 있음 — 미해결 | dump_measurements.md:9; command_audit.md §2 |
| F6 | `18F9D0` case 0xE | lane_L3.md: 완성 class 2 시설 효과 수집→192110 | lane_L4.md §2: 교전 쌍 목록 처리(병력·사기) | L3가 하위 호출(190E10)까지 추적했으므로 시설 효과로 채택; L4 라벨은 거침 | lane_L3.md; lane_L4.md |
| F7 | ZOC 점수 | dump_measurements.md:180(옛 해석): 인접 적 +300, 2~3칸 +5 | worldmap_spec.md §4.3: + 적대 소유 칸 항 5·H | 1권(코드+덤프)이 정정본. 적 영토 안 속도가 절반 이하 | worldmap_spec.md §4.3 |
| F8 | 파성 getter `2B27B0` | formation_mapping.md: '후보 진입점'(분리 unwind 구간) | dump_measurements.md:80: 상한 0x3C 사용 확인 | 사용 확인으로 확정, 진입점은 2B27B0(새 2B4B30) | formation_mapping.md vs dump_measurements.md |
| F9 | `2B07C0` 인접 효과 | 옛 combat6 앞 절의 의미 | combat6.md:55 정정(난이도 의존) | 정정본 채택. 새 빌드(2B2A90)는 숙련 모드에서도 난이도 값 적용(BC 충돌 1) | combat6.md:55; BUILD_25953386_COMBAT.md |

## 5. 정정 기록

| 대상 | 옛 해석 | 정정본 | 출처 |
|---|---|---|---|
| `41C140` | 통솔 조회(combat_defense 별칭) | 소속 객체·진형 번호 선택 + 효과 집계로 100 기준 계수. 통솔 조회는 `2A8D40→22FCE0(idx 0)`. 체인 41C140→41BFC0→41C200 | mechanisms_20261017/README.md:16; CHECKPOINT.md:9 |
| `combat_historical.md` | 과거 캡처 기반 전투 해석 | combat_rea_verified.md·combat_defense.md·능력치.md 우선 | REA_Analysis/README.md:19 |
| `2B2440`·`2B2690`·`2A9E50` | formation_defense=2B2690, defense_stat_formula=2B2440, siege=2A9E50 | 방어 입력 생산자 2A9E50(+army +0x4D), 공성 입력 생산자 2B2440 | formation_mapping.md |
| `25C460` | 거점 부대 회복 | 도적 출현 판정(새 25DE00), 구현 안 함→후보 게이트 구현 | difficulty.md:102; command_audit.md §4 |
| `1F42B0`·`2DD020`·`176B80` 이름 | 내구 증감·부상병 전환 등 | 1F42B0=내구 설정, 2DD020=장수 병력 배분, 176B80=전법 피해(trace 재확정) | dump_measurements.md:7-11 |
| `1843E0` 경로 | 성공이면 모든 경유지 도달 | 출력 칸 수가 양수이면 성공; 실패 구간이 있어도 루프 계속. `183A30`은 목적지→시작 역방향. `+0C`는 capacity가 아니라 누적 비용 | mechanisms_20261017/README.md |
| 표시 기동 | '약 10배'(4차 추정) | 표시 기동 ≈ 진형 기동 x 1.07 | dump_measurements.md:178 |
| 우호도 | 변경 105 고정·+10 고정 | `2719C0→25A080` += delta, 0..200 clamp | command_audit.md:99 |
| 진·요새 일 단위 부상병 회복 | 이전 엔진 규칙 | 원작에 없음(능력 칸 3 상승) | lane_L3.md:48 |
| 거점 점령 자원 | pre6_occupation 7번·1차 실측 | 중립 점령 자원 금≈4900 등 | FIDELITY.md:138; dump_measurements.md:26 |
| 통일 속도 목표 | approx_inventory J2 (206년 생존≤4) | 폐기: 규칙은 원작대로·판단은 복제 안 함 | worldmap_s9.md 0절; DESIGN.md:308 |
| RULES.md 상단 표 | 지휘한계·180일 재출진 등 장치 | 현재 코드에 없음. RULES.md 42절·53절과 command_audit.md 따름 | worldmap_s8.md:5 |

## 6. 미해결 목록 (시도된 경로 포함)

| # | 항목 | 시도된 경로 | 다음 한 걸음 |
|---|---|---|---|
| U1 | (해결 2026-11-17) 부대가 한 걸음마다 칸을 칠하는 호출의 소재: `303020 → 301D00 → 18A190 → 187450 → 186E60`, rules_tribes.md 16절 | 186E60 호출자 34개 중 날짜 상태기계에서 닿는 것 확인(몸 모양 301D00, 건설 28A200/2EA410 등); 2DB9A0/2D95F0 직접 피호출에 186E60 없음; 2A0CF0/2B75C0 하위 미해독 | 덤프 DLL에 set_owner 호출자 추적 추가(WB §6.2) |
| U2 | 전법 효과 5~23 결과식·지속 일부 | 처리기 10개 중 상당수는 CA §12a에서 확정됨(5~16·19~23). 17 화염은 구현. 연계·동시 발동 미해독 | `G+0x454` 순 카운터와 3순 간격 목록(`G+0x165E`) 기록 쪽 추적 |
| U3 | 교전 후보 사이 처리 순서·집중/측면 항(+0x25/+0x3E)·단계표 점프 테이블 | 170870(4,811B) 읽기, 16AC00 중간 간접 점프 | 점프 테이블 해독(lane_L3 C1) |
| U4 | 시설 효과 종류 1/2/3/8/15/16/17 의미 | 192110·2AD8F0 구조까지 확인 | 효과 소비 함수 추적(191760·16A780·300970 호출자) |
| U5 | 병참 판정 주기(매일/이동 때/순 경계) | 278290 호출자 다수; 판정 이벤트만 확인 | `278290` 추적(WB §6.2) |
| U6 | 경로 재탐색 정확한 트리거 | 2DB9A0이 막히면 0xBD10로 비우고 303EA0 재설정까지 확인 | 추적 훅(이동 갱신 전·후 사본) |
| U7 | 개성 조건 평가기 표 66칸 미채움(34칸만 채워짐), 효과 소비처 다수 | 27FCB0 표 해독(CA §12b), 효과 id별 소비처 조사 일부 | CA §15 점검표 항목별 |
| U8 | 계략 13·14·0x14·0x18 규칙 | 대상이 지역(13 → 1FD930이 22E260으로 세력 획득, 14/0x14는 지역 개발 3값 setter 243440/2424C0/242A60)임까지 확인 | 성공률 1E1A60(13) 등 상수·pow 인자(xmm1) 복원 |
| U9 | 징병량 2BF6E0 일치 | 식 구조·상수 PE 확인, 순수 환산 1.8~10.5 | 담당관 능력(231770) 보정·특성 0x24/0x25·정책 e 정밀화 |
| U10 | 도적 약탈 효과 | 25DE00 선택·25E7D0 생성까지 | 약탈 처리 함수 추적(CA §15 7) |
| U11 | AI 판단 영역(출진·요격·건설 후보 임계) | 행동트리 pseudo.cpp 4종(옛 빌드)·approx 목록 | 범위 밖(판단은 복제 안 함, DESIGN.md:308) |
| U12 | 조건 107종 의미(판단표) | L3b(2026-11-07): 미해결 22종 전부 코드로 해결(확정 13·추정 9), 추정 일부 확정 승격 — L3 5차 현재 확정 계열 116/순수 추정 16/미해결 0(122·128·139 등 이름 정정 포함). 정보 조회 항목은 105쌍 중 44쌍 판독 | 남은 추정·정보 항목은 ai/unresolved.md |

## 7. 자동 색인 (큐레이션 밖 함수 — 문서 인용 3회 이상만)

전체 목록은 `functions.json`(curated=false). 아래는 인용 횟수 ≥ 3인 함수의 한 줄 문맥(자동 추출, 해석 보증 없음).

| 새 RVA (옛) | 상태 | 인용 | 문맥(자동) |
|---|---|---|---|
| `1FAA0` (1FAC0) | same | 4 | 엔진/문서 인용: / 0x7f07545c / CGetAttackTargetFootholdNode / 0x1fac0 / 0 / 0 / 0 / 1 / 미확보 / |
| `1FF40` (1FF60) | same | 5 | 엔진/문서 인용: / 0xb553b8d4 / COccupyNeighborCapitalNode / 0x1ff60 / 0 / 0 / 0 / 1 / 미확보 / |
| `201C0` (201E0) | same | 7 | 문서 문맥: BUILD_25953386_COMBAT.md: / BT 노드 vtable 7개 (first_army 201E0, cut 1F3A0, retreat 61120, person_info 8E |
| `29BA0` (295B0) | same | 6 | 문서 문맥: FIDELITY.md:   - 출진 함수: 295B0, 2F2B0, 34F10, 32230/30390, 613A0, 68CE0, 69BD0. |
| `2AB90` (2A5A0) | changed | 4 | 문서 문맥: BUILD_25953386_REMAP.md: / 2A5A0→2AB90, 2C230→2CBC0, 2CFE0→2DAB0, 53C60→548D0, 613A0→61F10, 64E10→65A60 |
| `2CBC0` (2C230) | changed | 4 | 문서 문맥: BUILD_25953386_REMAP.md: native_adapter 6곳), 건물 파괴 `1F9DE0/1FA607`, AI 추적 `2C230/2CFE0/231B20/68590`, 출 |
| `2D720` (2CC50) | same | 8 | 엔진/문서 인용: / 0x6a4f6b51 / CCommandExecutionEmployNode / 0x2cc50 / 0 / 3 / 0 / 0 / 미확보 / |
| `2F080` (2E520) | same | 4 | 엔진/문서 인용: / 0x5c2752cc / CCommandExecutionRumorNode / 0x2e520 / 0 / 2 / 0 / 0 / 미확보 / |
| `2FE10` (2F2B0) | same | 21 | 문서 문맥: difficulty.md: / AI 대 플레이어 공격 보류(4일 때, 대상 지역이 플 소유) / `2F2B0` +0x30288 / 4에서 보류 / 보류 / 없음(AI 판단) / |
| `35A70` (34F10) | changed | 20 | 문서 문맥: FIDELITY.md:   - 출진 함수: 295B0, 2F2B0, 34F10, 32230/30390, 613A0, 68CE0, 69BD0. |
| `365A0` (35A40) | changed | 6 | 문서 문맥: BUILD_25953386_REMAP.md:  5바이트 getter. remap이 쌍둥이 BFA210(+0x58)을 잘못 골랐고, 새 35A40 대응(365A0)이 같은 호출 자리에서  |
| `36E80` (36320) | same | 4 | 엔진/문서 인용: / 지역 담당관 / 지역 → 무장 또는 해제 / 노드 `36320`, 해제 `29BF00(person,1,0)` / △ / |
| `3C330` (3B7D0) | changed | 4 | 엔진/문서 인용: / 0x7b9d3e14 / CGetMyselfDistrictInfoNode / 0x3b7d0 / 0 / 105 / 3 / 0 / 미확보 / |
| `3DCD0` (3D170) | same | 4 | 엔진/문서 인용: / 0x594ca732 / CGetSearchDataNode / 0x3d170 / 0 / 6 / 0 / 0 / 미확보 / |
| `3E750` (3DBF0) | same | 6 | 엔진/문서 인용: / 0x16bf303f / CRecruitOfficerSetNode / 0x3dbf0 / 0 / 6 / 0 / 0 / 미확보 / |
| `3EF50` (3E490) | same | 6 | 엔진/문서 인용: / 0x5733c979 / CTrainingOfficerSetNode / 0x3e490 / 0 / 6 / 0 / 0 / 미확보 / |
| `45790` (44A80) | changed | 16 | 문서 문맥: BUILD_25953386_REMAP.md: / 44A80→45790, 46B80→478A0, 48CE0→49900, 4BA50→4C6A0 (+검색 호출 8곳 46425→47145, 4 |
| `478A0` (46B80) | changed | 16 | 문서 문맥: BUILD_25953386_REMAP.md: / 44A80→45790, 46B80→478A0, 48CE0→49900, 4BA50→4C6A0 (+검색 호출 8곳 46425→47145, 4 |
| `49900` (48CE0) | changed | 15 | 문서 문맥: BUILD_25953386_REMAP.md: 1FA607`, AI 추적 `2C230/2CFE0/231B20/68590`, 출진 연결 `48CE0/4BA50`, 준비 확인 probe `2 |
| `4C6A0` (4BA50) | changed | 15 | 문서 문맥: BUILD_25953386_REMAP.md: `, AI 추적 `2C230/2CFE0/231B20/68590`, 출진 연결 `48CE0/4BA50`, 준비 확인 probe `2B07C0` |
| `52950` (51CE0) | same | 4 | 엔진/문서 인용: / 0x5d3a57aa / CClearTargetForceListNode / 0x51ce0 / 1 / 1 / 0 / 0 / 미확보 / |
| `53B80` (52F10) | same | 6 | 엔진/문서 인용: / 0x9a6f523b / CCommandExecutionGovernmentAutoNode / 0x52f10 / 1 / 0 / 0 / 0 / 미확보 / |
| `54110` (534A0) | same | 4 | 엔진/문서 인용: / 0x59d7e58a / CCCommandExecutionHiddenPoisonNode / 0x534a0 / 0 / 2 / 0 / 0 / 미확보 / |
| `54250` (535E0) | same | 5 | 문서 문맥: command_audit.md: / 22 / 명품 사용(하사) / 노드 54250 → **1F16B0**, 충성 **2B20C0** / **원작**: `ActionType::Gift`( |
| `54710` (53AA0) | same | 4 | 엔진/문서 인용: / 0x888b722a / CCommandExecutionPostAutoNode / 0x53aa0 / 1 / 0 / 0 / 0 / 미확보 / |
| `54BC0` (53F40) | same | 4 | 엔진/문서 인용: / 0x964b046e / CCommandExecutionSpyAwayNode / 0x53f40 / 0 / 3 / 0 / 0 / 미확보 / |
| `56BD0` (55F50) | changed | 6 | 문서 문맥: BUILD_25953386_REMAP.md: 9A0, 27C00→281F0, 2FA60→305C0, 35A40→365A0, 55F50→56BD0, 6C4D0→6D310, 7EB00→7F |
| `58B40` (57EC0) | same | 4 | 엔진/문서 인용: / 0x9bd46caa / CGetMyselfForceNode / 0x57ec0 / 5 / 23 / 0 / 0 / 미확보 / |
| `5D760` (5CBF0) | same | 4 | 엔진/문서 인용: / 0x72e99c29 / CCallScriptNode / 0x5cbf0 / 3 / 12 / 0 / 0 / 미확보 / |
| `61B10` (60FA0) | same | 5 | 엔진/문서 인용: / 0x4657905f / CArmySetArmyActionNode / 0x60fa0 / 0 / 0 / 8 / 0 / 미확보 / |
| `61C90` (61120) | same | 5 | 문서 문맥: BUILD_25953386_COMBAT.md: 드 vtable 7개 (first_army 201E0, cut 1F3A0, retreat 61120, person_info 8E7C0, f |
| `65A60` (64E10) | changed | 12 | 문서 문맥: BUILD_25953386_COMBAT.md: / 68CE0, 613A0, 64E10 (→ 69AB0 / 61F10 / 65A60) / 새 빌드 전용 함수 27D490 / 2A3E30( |
| `6D310` (6C4D0) | changed | 4 | 문서 문맥: BUILD_25953386_REMAP.md: C00→281F0, 2FA60→305C0, 35A40→365A0, 55F50→56BD0, 6C4D0→6D310, 7EB00→7FAA0, 83 |
| `6E760` (6D920) | same | 4 | 엔진/문서 인용: / 0x6b472bec / CGetMyselfTroopsNode / 0x6d920 / 0 / 0 / 7 / 0 / 미확보 / |
| `6EFD0` (3DF40) | same | 5 | 문서 문맥: BUILD_25953386_REMAP.md: 괴 `1F9DE0/1FA607` 변경 9) ai_trace_nodes 노드 4개 변경과 `3DF40/57F10` 대응 없음 10) 전역 데이 |
| `6F070` (6E190) | changed | 8 | 엔진/문서 인용: / 0xc9ec061b / CSpecifiedTroopsSetPurposeNode / 0x6e190 / 0 / 22 / 23 / 0 / 미확보 / |
| `733C0` (723E0) | same | 6 | 문서 문맥: command_audit.md: 지형 객체(0x48 B, `world+0x73860`)는 fixdata 레코드(51 B, 포장)에서 **+0x1C까지는 +0x10, 이후(u16 8칸 배 |
| `738A0` (728C0) | same | 6 | 문서 문맥: worldmap_spec.md: ·부대 ctx, 칸 객체, 시설 정의 객체)` → 참/거짓, 시설 정의는 `world+0x73958[id]` / / |
| `77410` (76470) | same | 7 | 문서 문맥: worldmap_spec.md: 송 17·18·20). 길 찾기가 두 진형을 모두 읽어(`184D60`이 `world+0x77428[+0x1B]`, `[+0x1C]`) 지형에 맞는 쪽을 |
| `774D0` (76530) | same | 4 | 문서 문맥: command_audit.md: 3C와 입력 3개를 비교하는 AI 판단, `54330`(학습): 기술 서가 10칸(`+0x774D0` 표)을 훑는 AI 판단 + 관직 rank ≥ `14 |
| `7B0B0` (7A110) | same | 5 | 엔진/문서 인용: / 0x874694d6 / CDomesticPriorityDevelopmentSelectNode / 0x7a110 / 0 / 6 / 0 / 0 / 미확보 / |
| `7BE80` (7AEE0) | same | 8 | 엔진/문서 인용: / 0x339cbcee / CGetBattlePowerSoldierNumNode / 0x7aee0 / 0 / 3 / 0 / 0 / 미확보 / |
| `7C300` (7B360) | same | 7 | 엔진/문서 인용: / 0x1870191c / CGetCanServePersonListNode / 0x7b360 / 0 / 3 / 0 / 0 / 미확보 / |
| `7CB80` (7BBE0) | same | 7 | 문서 문맥: worldmap_spec_b.md: 런타임 개성 객체 232바이트(`world+0x7DD18`[356]): `+0xA4/A5` 조건, `+0xA8/AC` 조건값, **`+0xB4` lp |
| `7EBA0` (7DC00) | same | 7 | 문서 문맥: BUILD_25953386_COMBAT.md: 1F3A0, retreat 61120, person_info 8E7C0, foothold 7DC00, variable_minus 91030 |
| `83420` (82480) | changed | 5 | 엔진/문서 인용: / 0x543eff68 / CListClearNode / 0x82480 / 9 / 315 / 2 / 4 / 미확보 / |
| `83DE0` (82E40) | changed | 5 | 엔진/문서 인용: / 0x73b8b0c8 / CListGetItemByIndex / 0x82e40 / 4 / 201 / 0 / 4 / 미확보 / |
| `84CB0` (83D10) | changed | 5 | 문서 문맥: BUILD_25953386_REMAP.md: 5A0, 55F50→56BD0, 6C4D0→6D310, 7EB00→7FAA0, 83D10→84CB0, 856F0→86720, 861A0→87 |
| `85580` (57F10) | same | 6 | 문서 문맥: BUILD_25953386_REMAP.md: DE0/1FA607` 변경 9) ai_trace_nodes 노드 4개 변경과 `3DF40/57F10` 대응 없음 10) 전역 데이터 직접 접 |
| `85EC0` (84E90) | same | 4 | 엔진/문서 인용: / 0x96319dce / CSetBehaviortreeRestartFlagNode / 0x84e90 / 0 / 0 / 3 / 0 / 미확보 / |
| `864B0` (85480) | same | 5 | 엔진/문서 인용: / 0xc7f0763d / CVariableCreateNode / 0x85480 / 21 / 710 / 11 / 2 / 미확보 / |
| `864E0` (854B0) | same | 4 | 엔진/문서 인용: / 0xa7e41c85 / CVariableCreateSpecifiedTypeNode / 0x854b0 / 0 / 5 / 2 / 0 / 미확보 / |
| `865D0` (855A0) | same | 4 | 엔진/문서 인용: / 0x8239d75b / CVariableDivideVariableNode / 0x855a0 / 2 / 25 / 0 / 0 / 미확보 / |
| `86720` (856F0) | changed | 4 | 문서 문맥: BUILD_25953386_REMAP.md: BD0, 6C4D0→6D310, 7EB00→7FAA0, 83D10→84CB0, 856F0→86720, 861A0→871D0, 86D70→87 |
| `871D0` (861A0) | changed | 7 | 문서 문맥: BUILD_25953386_REMAP.md: 4D0→6D310, 7EB00→7FAA0, 83D10→84CB0, 856F0→86720, 861A0→871D0, 86D70→87DA0, 87 |
| `8B190` (8A160) | changed | 8 | 문서 문맥: BUILD_25953386_REMAP.md: 1D0, 86D70→87DA0, 87750→88780, 88F80→89FB0, 8A160→8B190, 8BAB0→8CAE0, 8DF10→8E |
| `8EB70` (8DB40) | changed | 5 | 문서 문맥: BUILD_25953386_COMBAT.md: / 8DB40 / 옵션 41 비교값 변경 / 모드 미사용 / |
| `8ED40` (8DCF0) | same | 4 | 엔진/문서 인용: / 0xc9413e99 / CVariableGetHexInfoNode / 0x8dcf0 / 0 / 28 / 5 / 1 / 미확보 / |
| `8EF60` (8DF10) | changed | 5 | 문서 문맥: BUILD_25953386_REMAP.md: 780, 88F80→89FB0, 8A160→8B190, 8BAB0→8CAE0, 8DF10→8EF60, 8F0C0→90110, C2610→C3 |
| `8F5A0` (8E550) | same | 7 | 문서 문맥: FIDELITY.md:     - 군단 N1462/N1485의 이동 비용 `<=10000` 검사(`8E550 CVariableGetMoveCostNode`) |
| `8F810` (8E7C0) | same | 6 | 문서 문맥: BUILD_25953386_COMBAT.md: army 201E0, cut 1F3A0, retreat 61120, person_info 8E7C0, foothold 7DC00, vari |
| `90110` (8F0C0) | changed | 6 | 문서 문맥: BUILD_25953386_REMAP.md: FB0, 8A160→8B190, 8BAB0→8CAE0, 8DF10→8EF60, 8F0C0→90110, C2610→C36A0, C2F70→C4 |
| `92130` (910E0) | same | 4 | 엔진/문서 인용: / 0xd826aec4 / CVariableMultiValueNode / 0x910e0 / 4 / 223 / 0 / 1 / 미확보 / |
| `922F0` (912A0) | same | 4 | 엔진/문서 인용: / 0xc75905a / CVariablePlusVariableNode / 0x912a0 / 1 / 152 / 1 / 1 / 미확보 / |
| `92990` (91940) | same | 4 | 엔진/문서 인용: / 0x1c972788 / CVariableSetVariableSpecifiedTypeNode / 0x91940 / 2 / 100 / 4 / 0 / 미확보 / |
| `AFDC0` (AEE60) | same | 5 | 엔진/문서 인용: rvas.push('0x302fa0','0x43e030','0x8e550','0xaee60','0x69bd0'); |
| `C2C60` (C1BD0) | same | 4 | 문서 문맥: BUILD_25953386_REMAP.md: F10→8EF60, 8F0C0→90110, C2610→C36A0, C2F70→C4000, C2F73→C4003, D1A20→D2AB0, 16 |
| `C36A0` (C2610) | changed | 9 | 문서 문맥: BUILD_25953386_COMBAT.md: / ai_max_aggression 포인터 (슬롯 1B95CC0 → C2610) / 슬롯 → 1B98D10 / same-asm / 그대로  |
| `D1760` (D06D0) | same | 4 | 문서 문맥: BUILD_25953386_COMBAT.md: / 컷 판정 E8 / D2486 → D3516 / same / 그대로 / |
| `D4D00` (D3C70) | same | 5 | 엔진/문서 인용: * `43E030`: AI 관리자 초기화와 활성 검사 후 세력 `D3D50` → 해당 세력의 군단 `D3CE0` → 각 군단의 군세 `D3D90` → 각 군세의 부대 `D3C70` |
| `D4D70` (D3CE0) | same | 7 | 엔진/문서 인용: * `43E030`: AI 관리자 초기화와 활성 검사 후 세력 `D3D50` → 해당 세력의 군단 `D3CE0` → 각 군단의 군세 `D3D90` → 각 군세의 부대 `D3C70` |
| `D4DE0` (D3D50) | same | 5 | 엔진/문서 인용: * `43E030`: AI 관리자 초기화와 활성 검사 후 세력 `D3D50` → 해당 세력의 군단 `D3CE0` → 각 군단의 군세 `D3D90` → 각 군세의 부대 `D3C70` |
| `D4E20` (D3D90) | same | 5 | 엔진/문서 인용: * `43E030`: AI 관리자 초기화와 활성 검사 후 세력 `D3D50` → 해당 세력의 군단 `D3CE0` → 각 군단의 군세 `D3D90` → 각 군세의 부대 `D3C70` |
| `169DF0` (168E40) | same | 4 | 문서 문맥: dump_measurements.md: * 호출 구조: `169F2C` 간접 분기표 단계 1~7 = `174BC0`(공성·시설) -> `16A030`(입력) -> `16AB50`(공격  |
| `16E760` (16D7B0) | same | 5 | 엔진/문서 인용: atk_power = 16D630(공격자, param_2) ; r = 최대(0x46=70, 141A48AB0(=5) + 16D7B0(공격자)) |
| `174F40` (173F90) | same | 4 | 문서 문맥: command_audit.md: ). 범위 바이트 = 헥스 반경(0 = 단일). 아군 대상은 같은 세력(원작 대상 목록 `173F90`은 미해독). 피해(1·18)·상태(2~4)를 가진 |
| `175DE0` (174E30) | same | 6 | 문서 문맥: lane_L1.md:  (0x7C,0x7D) / 효과124·125 / 위치만 / `296AA0`(0x7C), `175DE0`(0x7D) / 함수 역할 미해독 / - / 하 / |
| `17E210` (17D1D0) | same | 8 | 문서 문맥: command_audit.md: 2 / 0:272 / not connected / wounded ratio: 179DE0 17E210 term not read / |
| `17E530` (17D4F0) | same | 4 | 문서 문맥: command_audit.md: 음, 부상·전사 47·53·82·111과 사기 13·79·80은 호출자 `179DE0`·`17E530` 주변 미해독, 성격형 1·2·3·83~87·99는 |
| `1D9DC0` (1D8C30) | same | 5 | 문서 문맥: command_audit.md:  54CE0 → 1EBC60(`CCmdActionCaravan`) → 1F5870, 도착 1D9DC0 / **없음**(S15 13절 b: 이민족 5부족  |
| `1EECC0` (1ED920) | same | 6 | 문서 문맥: worldmap_s9.md: 5% 합류 확률의 결정 요인(호감·군주 매력 등) 미확정. 등용 성공 확률식(1EFE60/1ED920 계통)은 추출본에서 UI 함수였고 확률식은 기존 279 |
| `1F1210` (1EFE60) | same | 5 | 문서 문맥: worldmap_s9.md: 8 무장의 45% 합류 확률의 결정 요인(호감·군주 매력 등) 미확정. 등용 성공 확률식(1EFE60/1ED920 계통)은 추출본에서 UI 함수였고 확률식은 |
| `1F42B0` (1F2EE0) | same | 7 | 문서 문맥: worldmap_spec.md: 42` 칸)가 일하는 동안 매일 내구가 오른다.** 23년 덤프의 `trace.bin`(`1F42B0` 내구 설정 함수 호출 95,374건, 건물 포인터 |
| `1FA5DA` (1F924A) | same | 3 | 문서 문맥: BUILD_25953386_REMAP.md: nnel, domestic, native_adapter 6곳), 건물 파괴 `1F9DE0/1FA607`, AI 추적 `2C230/2CFE0/ |
| `1FB170` (1F9DE0) | changed | 7 | 문서 문맥: command_audit.md: →1FA530(종류 분기)→1FA640·2000F0·1FF7B0·1FD930·1FC530·1FB170·1FEF60, 판정 1ECC20→1E0EB0 / * |
| `2035D0` (2021D0) | same | 4 | 문서 문맥: lane_L4.md: / 0 / 매칸 / `2035D0` / 날짜 상태 비트 8·0x16이 켜졌을 때 이벤트 목록(`1EC7D0`) / 없음 / - / |
| `22B8E0` (229EA0) | same | 6 | 엔진 주석: // 14 / 15 / 16 / 19 tile terrain byte +0x42 == 4 / == 3 / == 2 / != 4, 17 +0x42 in {3, 5}, 20 troops ( |
| `22CB80` (22B140) | same | 7 | 문서 문맥: dump_measurements.md:  0x3C). 지형 분류 비트 2(수상)면 army +0x1C 진형, 아니면 +0x1B(`22B140`). 세력 +0x193 비트 2이고 진형 5 |
| `22E110` (22C6D0) | same | 11 | 문서 문맥: lane_L3.md: 결**(이번에 열지 못함). 시도 경로만: C7 `179DE0`/`17E210`, C9 `22C6D0`, C10 지형 `+0x42` 추출 / — / — / — / |
| `22E2A0` (22C850) | same | 10 | 문서 문맥: BUILD_25953386_REMAP.md: ram_5` 블록(2AC35B..2AC3B4)은 store가 없는 순수 보정항이다(지휘관 22E2A0·유효성 331780·특기 getter  |
| `22E690` (22CC40) | same | 3 | 문서 문맥: BUILD_25953386_COMBAT.md: / 출력 적용 178E30, 적대 2CA280 → 2CC630, 세력 22CC40 → 22E690 / / same / 그대로 / |
| `22EF50` (22D500) | same | 4 | 엔진/문서 인용: - 점령 시 소유 이전은 `2DF720(anchor, 새 세력, 반경 N, …)`에서 일어난다. 호출: (a) `26D590` 0x22E행: `anchor = 22D500(site |
| `22F7A0` (22DD10) | same | 6 | 엔진/문서 인용: // when no special tile object), extra = 1.5 when the formation (22DD10 index) is 6 or 14 and the un |
| `230460` (22E9D0) | same | 5 | 엔진/문서 인용: // RVA 22E9D0 -> 268C50 (maximum morale of a force): (41C200(force, 10) x 141A49798(=1) + 100) x 141 |
| `232030` (2305D0) | same | 8 | 문서 문맥: command_audit.md:  부른다. **전법 = 무장 `+0x130[10]`**, 개성 = `+0x118[5]`(`232030`)로 구분되어 "개성 습득"은 해당 명령이 아니다. |
| `234880` (232EE0) | same | 6 | 문서 문맥: command_audit.md: , 혈연 제외(배우자 2CAE70·의형제 2CBF80·부모 자식 2CAE20·군주의 애호 234880, 혈연 판정 278110은 군주가 그를 미워하지 않 |
| `2593E0` (257990) | same | 4 | 문서 문맥: approx_inventory.md:  수: 정책 37 보유 군단에서 +2~+8 오차(166/221 일치) / R / 중 / `257990`/`265A60`/`267410` [문서].  |
| `2596A0` (257D00) | same | 4 | 문서 문맥: BUILD_25953386_REMAP.md: / 259682→25B022, 27D976→27F716, 25974B→25B0EB, 27DA09→27F7A9, 295C5F→297B6F /  |
| `267410` (265A60) | same | 4 | 문서 문맥: approx_inventory.md: +2~+8 오차(166/221 일치) / R / 중 / `257990`/`265A60`/`267410` [문서]. 정책 37 수준의 시나리오 이후  |
| `267710` (265D60) | same | 5 | 문서 문맥: lane_L1.md: C0`·`26C760`·`304D70`·`2BF200`·`2BECD0`·`2BF6E0`·`267710` / / `rules.cpp` / 상 / |
| `2695D0` (267C20) | same | 5 | 문서 문맥: worldmap_spec.md: 책 효과 0x43**×배수(난이도 3 ×1.5, 4 ×2.0) 가산 / `26AF80`/`2695D0` / 코드 / |
| `26A920` (268F70) | same | 4 | 문서 문맥: lane_L1.md: / 16 (0x10) / 훈련담당관효과 증가 / 구현(L1) / `26A920`(훈련 상승량) / `상승 = base + base x 합(0x10) / 100 +  |
| `271E70` (270550) | same | 4 | 문서 문맥: command_audit.md:  int(위력 x 상성 x 단계 x 16E820), 사기 = max(0, 사기 - 양)(`271E70`의 0 도달 표식 `+0x98`은 미반영) / 원작 |
| `27BF90` (27A660) | same | 4 | 엔진/문서 인용: / 개발 방향 / 지역 → 상업 1·농업 2·병영 3 / Area +0x72. 원작 `27A660`도 이 칸만 바꾼다 / △ / |
| `27D900` (27BB60) | same | 4 | 문서 문맥: BUILD_25953386_REMAP.md: / 259682→25B022, 27D976→27F716, 25974B→25B0EB, 27DA09→27F7A9, 295C5F→297B6F /  |
| `286B00` (284D60) | same | 6 | 문서 문맥: command_audit.md: `1F2370`, `1F9670`, `1FEF60`(계략 0x18), `25FA40`, `286B00`, `2A0CF0`, `2BB240`, `2BBED |
| `28A890` (288AF0) | same | 4 | 문서 문맥: lane_L4.md: / 0xf / 매칸 / `28A890` → `28A200` / 건설 착공 / 시설 생성 / S4 구현 / |
| `28F910` (28DB70) | changed | 5 | 문서 문맥: command_audit.md: / 수명·사망·계승 / 28C180, 28DB70 / APPROX(덤프 보정) / |
| `2956A0` (293790) | same | 6 | 문서 문맥: BUILD_25953386_REMAP.md: 022, 27D976→27F716, 25974B→25B0EB, 27DA09→27F7A9, 295C5F→297B6F / same-hook /  |
| `296AA0` (294B90) | same | 7 | 문서 문맥: worldmap_spec.md: +`1402412D0`, pre6_occupation §4). 파괴는 계략 「건물파괴」(`294B90`) 또는 시설 공격 전법(종류 18)으로 내구를 깎 |
| `2A0CF0` (29EDE0) | changed | 12 | 문서 문맥: command_audit.md: `1F9670`, `1FEF60`(계략 0x18), `25FA40`, `286B00`, `2A0CF0`, `2BB240`, `2BBED0`, `2BC03 |
| `2A8160` (2A5F70) | same | 8 | 문서 문맥: command_audit.md:  합산의 슬롯 5 / 6 / 7 / 8과 슬롯 19를 더해 +-10으로 자른 값을 쓴다(`2A8160`의 개성 97 / 31 항은 미반영: 보유자 8명  |
| `2A8D50` (2A6B60) | same | 5 | 문서 문맥: lane_L1.md: / 108 (0x6C) / 연계참가율 특출 / 엔진 주체 없음 / `2A8D50` / 공감값(연계 참가 확률)에 합을 더함; 엔진에 공감값 계산이 없다(S13 관측 |
| `2ABDE0` (2A9BB0) | same | 5 | 문서 문맥: command_audit.md: * 소비처: `2ABDE0`이 배분 수만큼 표 `world+0x85DF0`의 (능력 종류, 증가량)을 합산한다. 이 표는 읽을 수 있는 정적 자료에 없어 |
| `2ACB80` (2AA850) | same | 13 | 문서 문맥: lane_L3.md: 리 범위는 `[레코드 +0x2B, 범위(+0x2C)]`(`180870` = +0x2B, `2ACB80` 거리; 투석대 2..3, 나머지 1..2; id 15·17은 |
| `2AE4A0` (2AC170) | same | 5 | 엔진/문서 인용: / 설득·충성 문턱(`+0xE8`) / `AC580` +0x2AC5F9 / 플 대상 <100; 컴: 0 -> <86, 1 -> <91, 그 밖에 관계식 / 관계식 / 없음(AI 판 |
| `2AFAB0` (2AD780) | same | 5 | 문서 문맥: lane_L1.md: 탐색일수 단축 / 위치만 / `2331F0`(이동 일수) / `X = 35 x 거리 / (2AFAB0(세력,5)/2 + 10) / 12`, 일수 = `ceil(X) |
| `2B0070` (2ADD40) | same | 3 | 문서 문맥: BUILD_25953386_REMAP.md: 한 호출. 출진/캠페인은 호출·호출 지점 교체만 함. 공식을 재현하는 path_fast는 2B02A0을 끔 유지 / sortie/campai |
| `2B0AB0` (2AE780) | changed | 5 | 문서 문맥: BUILD_25953386_COMBAT.md: / 숙련 옵션 호출 2B0B69 E8 → 3EA400 / → 2B2E28 / 3EC920 / same-hook / same-asm / 그대 |
| `2B1B10` (2AF7E0) | same | 6 | 문서 문맥: dump_measurements.md: 16A990, 16A030, 16A1D0, 169F2C`; `2B2440, 2B07C0, 2AF7E0`, 모두 `-Build 1fbe6be7`)만 |
| `2B4CA0` (2B2920) | same | 6 | 문서 문맥: command_audit.md: 0, 부상병·부대 한도로 자름 -> 병력 += f, 부상병 -= f / 원작(병력 한도 `2B4CA0`은 미반영) / 높음 / |
| `2B6F80` (2B4C00) | same | 5 | 문서 문맥: dump_measurements.md:  army+0x4A(부호 바이트) / 100) x (240 / BE120(지형 1)) x 2B4C00 x (세력 +0x193 비트 3 + 수상 부 |
| `2C2BA0` (2C0820) | same | 5 | 엔진 주석: /* 178470 + 2EEA60 (confirmed): amount = int(power x matchup 1.0 x stage 1.0 x external 1.0 x force fac |
| `2CBCB0` (2C9900) | same | 4 | 문서 문맥: BUILD_25953386_REMAP.md: 3/C985D/C9952)가 모드와 같은 (…,1,0)으로 부르고 2B4460의 0x28/2CBCB0 블록은 param_5로 묶여 모드는 1 |
| `2CEBB0` (2CC800) | same | 4 | 문서 문맥: lane_L1.md: 기 가감 함수; 호출처 `179DE0`·`17E530`·`1932A0`·`272720`·`2CEBB0`·`2E56C0`·`431F20`) / 감소량 L에 대해 `b |
| `2ECEA0` (2EAAE0) | same | 5 | 엔진/문서 인용: uint64_t rules_hash(){const char* p="san14sim-rules-r9-v2;difficulty=std-mode-3e9e60-default4-player |
| `2ECF00` (2EAB40) | same | 6 | 엔진/문서 인용: uint64_t rules_hash(){const char* p="san14sim-rules-r9-v2;difficulty=std-mode-3e9e60-default4-player |
| `2EFA70` (2ED6B0) | same | 7 | 문서 문맥: command_audit.md: / 6 / 시정 / 2ED6B0, 051380 / 원작 + APPROX(추가 칸·활성 시점) / 예 / |
| `2F5AA0` (2F36B0) | same | 4 | 문서 문맥: lane_L1.md: 00 (0x64) / 지역담당관 시 회유 저지 / 엔진 주체 없음 / `1EBF00`, `2F5AA0` / 마을 대상 계략의 차단; 엔진에 마을 대상 계략 없음 / |
| `32E3B0` (32C130) | same | 6 | 엔진/문서 인용: * `178900`은 대상 종류가 부대(0x1B)이면 대상 부대 배열 `+0x7E838`(0x1F5=501개)에서, 거점 종류 5/6이면 `32C130`으로 객체를 얻는다(종류 6 |
| `331780` (32F500) | same | 16 | 문서 문맥: BUILD_25953386_REMAP.md: AC35B..2AC3B4)은 store가 없는 순수 보정항이다(지휘관 22E2A0·유효성 331780·특기 getter 22DB30(pers |
| `3ED810` (3EB2F0) | same | 8 | 문서 문맥: difficulty.md: * `설정+0xE58`(`3EB2A0` 읽기, `3EB2F0`은 "== 0", 쓰기 `3EF660`)는 게임 모드다. 시나리오 선택 화면 `607000`이 일 |
| `44B090` (448E40) | same | 5 | 엔진/문서 인용: {0x448E40, 5, {0x48,0x89,0x5c,0x24,0x08}, false, 64}, |
| `44C340` (44A0F0) | same | 7 | 엔진/문서 인용: {0x44A0F0, 11, {0x48,0x8b,0xc4,0x57,0x48,0x81,0xec,0xc0,0x00,0x00,0x00}, false, 64}, |
| `7FC700` (7FA230) | same | 5 | 엔진/문서 인용: - 교정 사항(r4/r5 반영 상 오류 가능성): **`16A1D0`의 호출자는 `16A780, 191760, 7FA230, 913E20`뿐**이고 `191760`의 `param_ |
| `806DA0` (804770) | changed | 3 | 문서 문맥: command_audit.md: ·0x13의 결과 경로, 플레이어 쿨다운(`+0x4c` 날짜), `808930`의 보너스 806DA0, 3261B0의 병력 항(2AF5E0). |
| `816240` (813B10) | same | 3 | 문서 문맥: BUILD_25953386_REMAP.md: A0E, 8162E1→818A4D, 816726→818E96, 816756→818EC6, 81675B→818ECB, 816806→818F76 |
| `818600` (815EA0) | changed | 4 | 문서 문맥: BUILD_25953386_REMAP.md: / 815970→8180C0, 815EA0→818600 / same-hook / 가상 호출(+0x1d0)과 콜리 하나에 0 인자 추가 외 동 |
| `82EB90` (82C510) | changed | 3 | 문서 문맥: BUILD_25953386_REMAP.md: - 새 주소에서도 guard가 틀어지는 기능(함수 자체가 바뀜): 외교 정보 `82C510/82C960/82CD60/82D170/804770 |
| `82F030` (82C960) | changed | 3 | 문서 문맥: BUILD_25953386_REMAP.md:  새 주소에서도 guard가 틀어지는 기능(함수 자체가 바뀜): 외교 정보 `82C510/82C960/82CD60/82D170/804770` |
| `82F490` (82CD60) | changed | 4 | 문서 문맥: BUILD_25953386_REMAP.md: 도 guard가 틀어지는 기능(함수 자체가 바뀜): 외교 정보 `82C510/82C960/82CD60/82D170/804770`, 피해 예측 |
| `82FD50` (82D570) | changed | 3 | 문서 문맥: BUILD_25953386_REMAP.md: / 82D570→830410, 82D880→82FD50, 82DB90→8300B0 / same-hook / **(local10 G4)** 옛 |
| `8300B0` (82D880) | changed | 3 | 문서 문맥: BUILD_25953386_REMAP.md: / 82D570→830410, 82D880→82FD50, 82DB90→8300B0 / same-hook / **(local10 G4)** 옛 |
| `830410` (82DB90) | changed | 3 | 문서 문맥: BUILD_25953386_REMAP.md: / 82D570→830410, 82D880→82FD50, 82DB90→8300B0 / same-hook / **(local10 G4)** 옛 |
| `8706D0` (86E320) | same | 4 | 문서 문맥: BUILD_25953386_REMAP.md: thon -X utf8 AI_TacticsMod/tools/rva_remap.py map 86E320  # 개별 조회(함수·내부 주소·vta |
| `8D0320` (8CDD40) | same | 3 | 문서 문맥: BUILD_25953386_REMAP.md: / 8DF198→8E1628, 8DF1F5→8E1685, 907294→909734, 8CDD40→8D0320, 8E0148→8E25D8, 8 |
| `8DFBC0` (8DD730) | same | 3 | 문서 문맥: BUILD_25953386_REMAP.md: 628, 8DF1F5→8E1685, 907294→909734, 8CDD40→8D0320, 8E0148→8E25D8, 8E01D0→8E2660 |
| `907990` (9054F0) | same | 3 | 문서 문맥: BUILD_25953386_REMAP.md: 734, 8CDD40→8D0320, 8E0148→8E25D8, 8E01D0→8E2660, 907D9C→90A23C, 2BF033→2C13B3 |
| `9332B0` (930D20) | changed | 10 | 문서 문맥: BUILD_25953386_REMAP.md: 하지 못한 참조 0건). 슬롯 152/152 대응, 호출 함수 36개 중 35개 same(930D20은 jump table만 다름) / ho |
| `BFA210` (BF7A40) | changed | 6 | 문서 문맥: BUILD_25953386_REMAP.md: fast, sortie, sortie_links, campaign_routes), 인사 `BF7A40`(personnel, domestic, |

(위 150개; 인용 ≥3 미만 540개는 JSON에만.)

## 8. 출처 목록과 낡음/대체 확인 결과

읽은 문서(FUNC read_first 9 + data 2): AI_TacticsMod/docs/BUILD_25953386_COMBAT.md · BUILD_25953386_REMAP.md · GHIDRA_PERSISTENT.md · SESSION_RULES.md · San14Sim/docs/FIDELITY.md · fidelity/build_remap.md(.json) · command_audit.md · worldmap_spec.md · worldmap_spec_b.md · rva_map/summary.json. 보조: lane_L1~L4.md, dump_measurements.md, difficulty.md, approx_inventory.md, RULES.md, REA_Analysis/{mechanisms_20261017/*, formation_mapping.md, data_model.md, combat_inputs.md}, 엔진 `core/sim.h` 주석, `SOURCES.json`의 `engine_rva`(457줄)·`rva_index_top`(400).

확인 방법: ① 문서의 5~7자리 16진 토큰을 `functions.tsv`로 옛/새 함수 시작에 대조 ② 문서 내 정정 선언 줄 확인 ③ 충돌 3건은 `ghidra_full.py`로 호출자 확인(F3).

| 문서 | 확인 결과 | 판정 | 대체 문서 |
|---|---|---|---|
| `AI_TacticsMod/docs/AI_TRACE.md` | RVA 7개 중 옛 시작 4(= 옛 번호). 새 빌드 대응 서술 없음 | 낡음 확인(옛 빌드, 소량) | build_remap.md |
| `AI_TacticsMod/docs/NAME_LOOKUP.md` | RVA 6개 전부 옛 시작(E09910 등). 새 빌드 서술 없음 | 낡음 확인(옛 빌드) | functions.tsv(옛→새) |
| `AI_TacticsMod/docs/NATIVE_FUNCTIONS.md` | 옛 번호 체계(1fbe6be7; 문서가 SHA 1fbe6be7·87ed4e 명시). 함수 시작 RVA 444개 중 옛 시작 318 / 새 시작 18(=번호 겹침 16). 새 빌드는 BUILD_25953386_REMAP.md가 대체 | 낡음 확인(옛 빌드) | BUILD_25953386_REMAP.md + build_remap.md/json + rva_map/functions.tsv |
| `AI_TacticsMod/research/HOOK_INVENTORY.md` | 1,093개 훅 RVA 목록(local49). 추출 정규식 상 5~7자리 대문자 16진 1개만 잡힘 — 형식이 달라 자동 검증 불가. 문서가 옛 빌드 훅 기준(SOURCES 판정) | 낡음(자동 검증 불가, SOURCES 판정 유지) | BUILD_25953386_REMAP.md §5.1 + addr_table.json |
| `REA_Analysis/README.md` | 진입점 문서. 19행이 '과거 자료는 정정 문서 우선'을 선언(combat_historical·combat_pseudocode → combat_rea_verified·combat_defense) | 현재 안내(내용은 옛 빌드 분석본 지도) | — |
| `REA_Analysis/REA_findings.md` | RVA 1개(검증 불가). 원본 EXE 87ed4e 분석 요약 | 낡음(옛 분석본) | mechanisms_20261017/*, command_audit.md |
| `REA_Analysis/analysis_memory.md` | RVA 11개 중 옛 시작 9. 원본 87ed4e·역사 캡처 해시 메모 | 낡음 확인 | build_remap.md |
| `REA_Analysis/combat_defense.pseudo.cpp` | RVA 6개 중 옛 시작 5, changed 1. 41C140 통솔 별칭은 mechanisms README 16행 표가 정정 | 낡음 확인(별칭 오류 포함) | mechanisms_20261017/능력치.md |
| `REA_Analysis/combat_historical.md` | RVA 29개 중 옛 시작 16, changed 3. README.md:19가 정정 문서 우선 선언 확인 | 낡음 확인 → combat_rea_verified.md·combat_defense.md·능력치.md | command_audit.md §15, lane_L3.md |
| `REA_Analysis/combat_inputs.pseudo.cpp` | RVA 15개 전부 옛 시작, changed 5(2B21A0·2B2440·2A9E50·2AA2E0·2A8D40 계열). 새 빌드에서 0x30 지형 항이 추가돼 본문이 달라짐 | 낡음 확인(changed 5) | build_remap.md §2 + BUILD_25953386_COMBAT.md |
| `REA_Analysis/condition137_score.md` | RVA 9개 중 옛 시작 7(조건 137). 87ed4e 기준 | 낡음 확인 | predicates_recovered.md(역시 옛 빌드) |
| `REA_Analysis/condition137_score.pseudo.cpp` | RVA 6개 전부 옛 시작 | 낡음 확인 | — |
| `REA_Analysis/core_ai.pseudo.cpp` | RVA 14개 중 옛 시작 13, changed 4 | 낡음 확인 | command_audit.md, lane_L4.md |
| `REA_Analysis/coverage.md` | RVA 2개 옛 시작 2, changed 1. 27개 질문 목록(범위 설정 문서) | 낡음(복사본 systems.md와 동일) | command_audit.md·lane_L1~L4 |
| `REA_Analysis/data_model.pseudo.cpp` | RVA 4개 전부 옛 시작·changed 3 | 낡음 확인 | structs.md |
| `REA_Analysis/domestic.pseudo.cpp` | RVA 13개 중 옛 시작 8 | 낡음 확인 | command_audit.md §2, lane_L2.md |
| `REA_Analysis/formation_stat_dispatch.pseudo.cpp` | RVA 2개 옛 시작 1 | 낡음 확인 | — |
| `REA_Analysis/formulas.pseudo.cpp` | RVA 없음(param_s.bin 수식 100개 AST) | 주소 무관(수식 표현) | — |
| `REA_Analysis/mechanisms_20261017/CHECKPOINT.md` | RVA 3개 전부 옛 시작. 해제본 1fbe6be7·원본 87ed4e 명시 | 낡음 확인(옛 빌드) | build_remap.md |
| `REA_Analysis/mechanisms_20261017/README.md` | RVA 8개 전부 옛 시작, changed 2. 16행 표가 41C140 별칭을 정정 | 옛 번호 확인. 정정 내용(41C140은 통솔 조회 아님)을 본문에 채택 | functions.md 개성·정책 절 |
| `REA_Analysis/mechanisms_20261017/능력치.md` | RVA 24개 전부 옛 시작, changed 4(22FCE0·2A9E50·2B21A0 등) | 옛 번호 확인(식은 기본적으로 유효, 22FCE0는 새 빌드에서 bit14 검사 추가) | functions.md 능력치 절 |
| `REA_Analysis/mechanisms_20261017/이동경로.md` | RVA 7개 전부 옛 시작, changed 0 — 경로 함수 본문은 불변. 단 183A30(새 184D60)의 호출 사슬은 변경(2B0290에 0x30 지형 항 추가, build_remap.md §2) | 옛 번호만 변환하면 유효 | build_remap.md §2(183A30→184D60 등) |
| `REA_Analysis/mechanisms_20261017/출진과요격.md` | RVA 12개 중 옛 시작 10, changed 4 | 옛 번호 확인 | functions.md AI 절 |
| `REA_Analysis/mechanisms_20261017/함수별_증거.md` | RVA 표 39행 전부 옛 번호(8자리 0.. 표기) | 옛 번호 확인 | functions.json의 old 필드로 새 RVA 조회 |
| `REA_Analysis/occupy_20261018/README.md` | RVA 18개 중 옛 시작 16, changed 1(거점 자동점령 연출 CEncirclingOccupationMovie) | 낡음 확인 | — |
| `REA_Analysis/perf_20261018/README.md` | RVA 43개 중 옛 시작 41, changed 2. 원본(모드 미설치) 진행 CPU 병목 조사 | 낡음 확인(성능 조사는 옛 빌드 측정) | — |
| `REA_Analysis/predicates_partial.md` | RVA 18개 중 옛 시작 12, changed 2. 문서 선언 대체 문서 predicates_recovered.md 존재 확인 | 낡음 확인 → predicates_recovered.md(역시 옛 빌드) | predicates_recovered.md |
| `REA_Analysis/predicates_partial.pseudo.cpp` | RVA 11개 전부 옛 시작, changed 1 | 낡음 확인 | predicates_recovered.pseudo.cpp |
| `REA_Analysis/predicates_recovered.md` | RVA 14개 중 옛 시작 11. 87ed4e 기준 조건 137/138/146 확장 복원 | 옛 빌드 분석본(새 빌드 변환 필요) | — |
| `REA_Analysis/predicates_recovered.pseudo.cpp` | RVA 3개 중 옛 시작 2 | 옛 빌드 분석본 | — |
| `REA_Analysis/seed_inventory.md` | RVA 9개 중 옛 시작 5, changed 2. 기존 자료 함수 주소 단서 목록(단서는 의미 검증이 아님) | 낡음 확인 | build_remap.md |
| `REA_Analysis/speed_20261018/README.md` | RVA 19개 중 옛 시작 18, changed 1(CChangeSpeedLayout, 44BCA0 하루 진행 프레임) | 낡음 확인 | lane_L4.md §2(44DEE0) |
| `REA_Analysis/stall_20261018/README.md` | RVA 19개 중 옛 시작 18, changed 1(턴 시작 멈춤) | 낡음 확인 | — |
| `REA_Analysis/tactic_damage.pseudo.cpp` | RVA 10개 중 옛 시작 5 | 낡음 확인 | command_audit.md §12a(전법 효과 종류) |
| `REA_Analysis/tactic_inputs_recovered.pseudo.cpp` | RVA 12개 중 옛 시작 6 | 낡음 확인 | command_audit.md §12a |
| `REA_Analysis/tactic_result_record.pseudo.cpp` | RVA 1개(검증 불가) | 낡음(주소 거의 없음) | — |
| `REA_Analysis/terms.md` | RVA 없음. 용어·시스템 조사표 | 주소 무관(용어 사전은 현재도 유효) | — |
| `REA_Analysis/군단_행동트리.pseudo.cpp` | RVA 패턴 없음(대용량 4.5MB 행동트리 의사코드). 노드 vtable/RVA 표기가 달라 자동 검증 불가 | 낡음(옛 빌드 판단표 해시 재사용 확인은 mechanisms/verification.json에 있음) | node_kinds.json, command_audit.md |
| `REA_Analysis/군세_행동트리.pseudo.cpp` | 동일(154KB) | 낡음 | node_kinds.json |
| `REA_Analysis/부대_행동트리.pseudo.cpp` | 동일(48KB) | 낡음 | node_kinds.json |
| `REA_Analysis/세력_행동트리.pseudo.cpp` | 동일(107KB) | 낡음 | node_kinds.json |
| `San14Sim/docs/fidelity/calendar.md` | RVA 25개 전부 옛 시작·changed 2. 본문이 '미완료·정적 자료 요약'이라 선언 | 낡음 확인 → command_audit.md §2 | command_audit.md §2 |
| `San14Sim/docs/fidelity/combat6.md` | RVA 56개 중 옛 시작 47(문서 첫머리가 1fbe6be7 명시), changed 6. 55행에 2B07C0=인접지역 효과 정정(2026-11-05) 존재 확인 | 낡음 확인(옛 RVA) → command_audit.md §3·15 + lane_L3.md | build_remap.md §2 |
| `San14Sim/docs/fidelity/node_kinds.md` | RVA 패턴 없음(노드 kind·class 표). '조사 중·해석 미완' 선언 | 낡음 → node_kinds.json·command_audit.md | — |
| `San14Sim/docs/fidelity/pre6_occupation.md` | RVA 71개 전부 옛 시작(문서가 1fbe6be7 명시), changed 4. FIDELITY.md:138이 7번(공성·점령 조건)을 정정함 확인 | 낡음 확인 → dump_measurements.md 2차 + worldmap_spec.md | worldmap_spec.md §1 |
| `San14Sim/docs/fidelity/pre6_tactics.md` | RVA 73개 중 옛 시작 69, changed 5(문서가 1fbe6be7 명시). 130행 '2-0 데이터 해석 정정' 존재 | 낡음 확인 → command_audit.md §12 + appendix_tactics.md | worldmap_spec_b.md §5.1 |
| `San14Sim/docs/fidelity/pre6_timing.md` | RVA 47개 중 옛 시작 46, changed 4(문서가 1fbe6be7 명시) | 낡음 확인 → command_audit.md §2 + dump_measurements.md | lane_L4.md §2 |
| `San14Sim/docs/fidelity/systems.md` | RVA 14개 전부 옛 시작, changed 5. coverage.md 복사본 | 낡음 확인 | command_audit.md · lane_L1~L4.md |

현재 문서(read_first)의 RVA 체계 확인:
- `AI_TacticsMod/docs/BUILD_25953386_COMBAT.md`: 기준판 전환 분석. RVA 65개(옛 34/새 17) → 현재
- `AI_TacticsMod/docs/BUILD_25953386_REMAP.md`: 기준판 전환 보고. RVA 331개 → 현재
- `AI_TacticsMod/docs/GHIDRA_PERSISTENT.md`: 도구 문서 → 현재
- `AI_TacticsMod/docs/SESSION_RULES.md`: 7절 원작 함수 조회 순서·기준판 선언 → 현재
- `San14Sim/docs/FIDELITY.md`: 문서가 1a4a447d 기준판 선언. RVA 50개 중 옛 시작 48(주로 옛 번호 서술), changed 20 — 일부 절이 옛 번호를 그대로 둠(138행 정정 포함) → 현재(기준판 선언). 본문 RVA는 옛 번호가 섞여 있으므로 변환 후 사용
- `San14Sim/docs/fidelity/build_remap.md`: 옛→새 전수 대응표(본문 자체가 변환표) → 현재
- `San14Sim/docs/fidelity/command_audit.md`: RVA 338개: 새 시작 275, 옛 시작 43(겹침 8). 새 번호(옛 번호) 병기 문서. 본문 일부(3a 충성 구간·계략 구간)에서 새·옛 혼용 확인 → 현재(새/옛 혼용 주의)
- `San14Sim/docs/fidelity/worldmap_spec.md`: RVA 109개: 새 시작 59, 옛 시작 48(겹침 4). '새/옛' 병기 표가 많음 → 현재
- `San14Sim/docs/fidelity/worldmap_spec_b.md`: RVA 53개: 옛 시작 37, 새 시작 15. 5장 일부 RVA(176B80 등)는 옛 번호 → 현재(옛 번호 병용)
- `AI_TacticsMod/research/rva_map/1fbe6be7_to_1a4a447d/summary.json`: 대응표 요약(함수 same 97,839/changed 1,610/unmatched 930) → 현재
- `San14Sim/docs/fidelity/build_remap.json`: 원자료(944 항목) → 현재

**SOURCES.md 낡음/대체 추정 확인 요약**: FUNC 낡음 목록 46개 중 자동 검증 가능한 문서는 모두 옛 번호 체계로 확인(낡음 유지). 정정 선언이 문서 안에서 확인된 것: combat_historical(README:19), predicates_partial(→recovered 존재), calendar(→CA §2), combat6(:55), pre6_occupation(FIDELITY:138), pre6_tactics(2-0절), mechanisms(README:16). 대체 관계가 *부분만* 성립하는 것: `systems.md`·`coverage.md`(27개 질문 범위표 — 대체 문서가 질문별 결과를 담지만 우선순위 가설 자체는 어디에도 없음), `node_kinds.md`(대체는 node_kinds.json). `REA_Analysis/README.md`는 낡음이 아니라 *현재 안내문*(내용이 옛 분석본을 가리킴).


## 원작 호출 계약 보강 (2026-11-23)

근거는 현재 기준판 `1a4a447d…`의 기존 Ghidra C 추출이다. 아래는 본문 관찰이며 새 ABI/실게임 검증이 아니다. 샤드 위치는 해당 추출 기준 byte offset이다. 모드 구현·개선 방향은 이 도서관의 사실 범위에 포함하지 않는다.

| RVA / 추출 위치 | 확인한 원작 동작 |
|---|---|
| `331780` / `c/0033.c` byte 42019 | 인수가 null이면 false, 아니면 객체의 vtable `+0x18`을 호출해 nonzero인지 반환한다. 주소 접근 가능성·해제 여부를 검사하는 함수는 아니다. |
| `21A350` / `c/0021.c` | 대상 값과 같은 링크를 발견할 때 다음 링크를 보관하고 삭제한 뒤 순회를 계속한다. 첫 일치 하나만 삭제하는 계약이 아니므로 중복 값의 다른 링크도 함께 해제할 수 있다. |
| `2CC630` / `c/002C.c` byte 269246 | 첫 세력의 가상 식별값이 0이면 false. 두 번째가 0이면 첫 세력이 0x33 또는 0x2E~0x32일 때 false이며, 그 밖에는 뒤 분기를 거친다. 같은 객체, 연합 조건, 양방향 종속 관계는 false; 일반 외교는 **첫 객체의** `+0xEA+둘째 식별값` 하위 7비트를 읽는다. 따라서 인수 순서를 무시한 대칭 관계표로 일반화할 수 없다. |
| `478A0` / `c/0004.c` byte 179297, 본문 상대 1120행 | 주변 적대 지역을 후보로 삼는 분기에서 입력 계획 객체(지역 변수 `local_4d0`) `+0x60`에 `32E3B0` 결과를 쓴다. |
| `4C6A0` / 같은 샤드 byte 291220, 상대 1141행 | 같은 형태의 분기에서 입력 계획 객체 `+0x60`에 새 목표를 쓴다. |
| `45790` / 같은 샤드 byte 126517, 상대 1147행 | 같은 형태의 분기에서 입력 계획 객체 `+0x60`에 새 목표를 쓴다. 위 세 계획 함수는 출력 반환값 외에 입력 객체도 변경한다. |
| `3FDAF0`, `32EC60` / `c/003F.c` byte 310275, `c/0032.c` byte 304732 | 전자는 인자 합·날짜 카운터·`32EC60` 결과로 지역 값을 섞는다. `32EC60`은 인수 객체 `+0x45C`의 32비트 값을 읽어 반환한다. 이 두 본문에 전역 난수 상태 쓰기는 없다. |
| `3FDFF0` / `c/003F.c` byte 317552 | `DAT_141A4AB80`을 읽고 다시 갱신하는 별도의 bounded 난수 함수다. 앞의 날짜/인자 해시와 구분한다. |

정정: 위 함수 표의 `2CC630`에서 “소유 0=적대”는 인수 방향을 생략한 요약이다. **첫 인수 식별값 0은 false**이며 둘째 인수 0에는 특수 세력 예외가 있다. 위 상세 분기를 우선한다. 가상 getter의 실제 대상·다른 훅의 부작용까지 이 본문만으로 순수 함수라고 확정하지 않는다.
