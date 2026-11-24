# 원작 AI 행동 트리·룰베이스 통합 (K2)

작성 2026-11-07. 기준 빌드: Steam buildid 25953386, 해제본 `1a4a447d`(AI_TacticsMod/docs/SESSION_RULES.md 7절). 게임·REA·Codex 미실행. 판단표 `0000/bt_exce.bin` 을 **현재 파일에서 재파싱**했고, 조건 함수는 `ghidra_full.py` 현재 빌드 추출본을 직접 읽었다. 시뮬은 원작 AI 판단을 복제하지 않으므로(RULES) 이 자료는 조사·참고용이다.

확신도: **확정**(판단표 노드·코드 직접 확인) / **추정**(구조+문맥) / **미해결**. 새 확정 사실은 해당 절·파일에 추가한다.

## 0. 먼저 알아둘 것 (이번 통합의 핵심 발견)

1. **원본 판단표가 바뀌었다.** 현재 `0000/bt_exce.bin`(SHA `315f16d0f27cf511...`)은 옛 분석 파일과 다르다. 군단 트리 10,312 -> **10,790**(+478), 세력·군세·부대는 동일. 옛 문서의 군단 N번호는 모두 어긋난다(예: 옛 N711 = 현재 N722, 옛 N1883 = 현재 N1917). 변환표: `ai/diff_bt_exce.md`. 노드 종류는 그대로 232종, 조건 op 13·14(모병·훈련 담당관 있음)만 새로 쓰인다.
2. **조건 함수 132종의 의미를 정리했다.** 확정 53 / 추정 57 / 미해결 22(이전에는 미해석 107종; L3b·L3 5차에서 확정 계열 116 / 순수 추정 16 / 미해결 0 으로 갱신: ai/conditions.md). 옛 RVA(`C2610` switch)는 현재 `C36A0` 으로 바뀌어 대부분의 개별 조건 함수 주소가 달라졌다. 전수표 `ai/conditions.md`.
3. 군단 판단표는 **행동설정 0(또는 플레이어 소속)/1/2 세 분기**(N722/N4513/N8015)가 같은 역할 묶음을 반복하고, 일반 거점 공격 5노드(방식 8/9/10/11/22)는 분기 0 에만 있다.
3-1. 교차 검증: K3 의 `origlib.load_bt()` 파서(San14Sim/origlib/misc0000)와 이 문서의 재파싱(REA 파서)을 4개 트리 11,495 노드 전부 대조해 종류·부모·자식 수·인수(부호 있는 값은 32비트로 환산)가 일치함(불일치 0, 실행 확인). 노드 수 10,790 은 K3 통지와 같다.
4. **AI 판단표는 0002 rdb·fixdata 가 아니라 평문 `0000/bt_exce.bin`, 수식은 `0000/param_s.bin` 에 있다.** AI 모드는 두 파일을 쓰지 않는다. 형식·위치: `ai/data_locations.md`.
5. **충돌 2건**: (a) 문서(rules_tribes.md, lane_L3.md)의 호출 사슬 `442200 -> 44F2F0 -> 43DCB0` 은 현재 빌드에서 AI 관리자로 이어지지 않는다(§8), (b) 조건 110 은 코드가 군단 +0x17(방침)을 읽는데 ai_trace 문서는 "중시항목"으로 추정했다.

## 1. AI 영역 한눈에

| 영역 | 트리·구동 | 규모 | 세부 문서 |
|---|---|---|---|
| 세력 전략(공략·친선 대상, 행동방침, 정책패널·시정·관직 자동 설정, 전법 습득) | 세력 판단표 | 246 노드 | ai/roles.md 1절, ai/pseudo_세력.txt |
| 군단(수비·요격·수송·공격·내정·인사·외교·모략) | 군단 판단표 | 10,790 노드 | ai/roles.md 2절, ai/pseudo_군단_*.txt |
| 내정(지역 개발·담당관·모병훈련) | 군단 판단표 안 + 세력 N156~N199 | 군단 클러스터 | ai/roles.md 3절 |
| 인사(담당관·등용·탐색·포상·전법) | 군단 판단표 안 + 세력 N202~N245 | - | ai/roles.md 4절 |
| 외교·모략(친선·동맹·교환·계략·교역) | 세력(대상 선정) + 군단(명령) | 111+ 명령 노드 | ai/roles.md 5절, ai/command_index.tsv |
| 군세(점령·지역공격·요격·시설공격·건설) | 군세 판단표 | 348 노드 | ai/roles.md 6절, ai/pseudo_군세.txt |
| 부대 전투(화계·위보·병참·이동) | 부대 판단표 | 111 노드 | ai/roles.md 7절, ai/pseudo_부대.txt |
| 이민족·도적 | 판단표 없음. 세력 턴 상태 `44DD30` 의 하드코딩 경로 | - | ai/roles.md 8절, rules_tribes.md |
| 호출 주기·구동 | `4403E0` (옛 `43E030`), `440B30`, 초기화 `C11E0` | - | ai/schedule.md |
| 임계값·가중치·수식 | 판단표 상수 + param_s.bin 100식 + EXE 상수 | thresholds.tsv 2969행 | ai/rulebase.md, ai/formulas.md |

## 2. 자료 위치 요약 (상세: ai/data_locations.md)

- 판단표: `0000/bt_exce.bin`(CE, 473,468 B, 4개 트리, JBTP v2/KTBT v1), 기본판 `0000/bt.bin`. 수식: `0000/param_s.bin`.
- 실행 코드: 노드 클래스별 실행 함수(node_kinds.md), 조건 dispatch `C36A0`(167칸, conditions.md), 초기화 `C11E0`, 갱신 `4403E0`.
- 데이터 표(세력·군단·무장·도시·지역·칸·부대): 메모리 표 위치만 기록, 형식은 K3 몫.

## 3. 판단표 구조와 노드 종류 (상세: ai/node_kinds.md)

- 노드 11495개(세력 246 / 군단 10,790 / 군세 348 / 부대 111), 노드 종류 232종(구조 노드 5종: 루트, 선택·순서·전체검토 묶음, 조건, 반복, 작업묶음).
- 조건 노드 1,896+개는 AND/OR 묶음·개별 NOT·전체 NOT 로 개별 조건을 조합한다(core_ai.pseudo.cpp 3절).
- 변수는 판단 문맥(AI 관리자 +0xC0, 1,000,000 B)에 저장되며 `보조값NNNN` 은 읽기용 이름이다. 반복 노드는 목록 순회(수집모드·반복종류 인수)다.

## 4. 호출 주기 요약 (상세: ai/schedule.md)

- `4403E0` 이 세력 판단 -> 군단 판단(`D4D70`) -> 군세 판단(`D4E20`) -> 부대 판단(`D4D00`, 필터 `234DE0`·`2CB6C0` 통과 시) 순으로 호출. 호출자는 정적으로 없음(`std::function` 썽크 경유; `COtherStrategyState` 슬롯 5 `44DD30` 이 세력마다 작업 큐로 제출, ai/schedule.md). 날짜 상태기계 `44DEE0` 은 AI 를 부르지 않는다.
- 세력 판단표 안에서 `일자내부값 == 1`(= 매달 1일) 인 날만 공략·친선 대상을 다시 고른다. 군단은 `게임경과카운터`·난수·AI 설정 단계(0~4)로 공격 검토를 제어한다.

## 5. 조건 요약 (상세: ai/conditions.md)

- 현재 판단표에서 쓰는 조건 132종, dispatch 167칸 중 미사용 35칸. 객체종류 코드·판단 주체(AgentType)·명령 가용성 함수(70xxxx)·대상 후보 목록(6Dxxxx) 계열로 나뉜다.
- 사용 횟수 상위: 조건 20(변수>상수) 690, 21 310, 28 170, 18 144, 23 157, 24 152, 22 135, 65 190 (군단 편중).

## 6. 룰베이스 요약 (상세: ai/rulebase.md)

- 공격 검토 확률표(군주 성향34 -> 100/90/80/65/50/40), 공격검토시작기준 8/5/-1, 세력 공략 대상 수 규칙(성향13 20/10), 새 공격 통과 210/100(170/100)+추가보정 40/100, 공격 방식 비율 200/400 -> 방식 10/9/8, 수송 기준(2000+100x성향16 등), 지역 개발 가중치 25/50/75, 군단 방침 기준 62/15/5, 군세 재판단 10회, 요구 병력 탐색 1000+500, BT 엔진 설정표 13칸.
- 판단표의 모든 숫자 비교·대입은 ai/thresholds.tsv (비교 1,459 + 대입 1,510 행).

## 7. 영역별 AI (상세: ai/roles.md)

세력·군단·내정·인사·외교·군세·부대·이민족의 진입 노드, 한국어 의사코드, 명령별 가용성 조건, 역할별 노드 위치를 `ai/roles.md` 에 모았다. 전체 의사코드는 `ai/pseudo_*.txt` 7개 파일(군단 5분할), 모든 명령 노드와 조건 사슬은 `ai/command_index.tsv`.

## 8. 정정·충돌 기록

### 정정 (본문은 현재 해석, 옛 해석은 여기)

| # | 옛 해석 | 현재(정정본) | 근거 |
|---|---|---|---|
| C1 | 판단표는 4트리 11,017 노드, 군단 10,312 | 현재 파일은 11,495 노드, 군단 10,790 | `0000/bt_exce.bin` 재파싱(해시 불일치), ai/diff_bt_exce.md |
| C2 | 조건 130종 중 107종 미해석 | 사용 조건 132종, 확정 53·추정 57·미해결 22 | 현재 빌드 함수 본문 직접 읽기(ai/conditions.md) |
| C3 | 조건 dispatch 는 `C2610` | 현재 `C36A0`. 개별 조건 함수 RVA 대부분 변경 | `rva_remap.py map C2610` -> C36A0 (changed), C36A0 switch 직접 추출 |
| C4 | 조건 76/77 은 UNKNOWN | 전법 습득 명령 가용성·후보(70C3E0/6DE230), 세력 N210~N245 문맥 | 세력 트리 문맥(추정) |
| C5 | AI 갱신 함수 `43E030` 의 진행 호출자 `44F2F0`(문서) | 현재 빌드 호출자 없음, `44F2F0` 이 부르는 `43DCB0` 은 다른 함수 | callees/callers 직접 확인(ai/schedule.md 3절) |
| C6 | 조건 113·114·117 의 "관계 목록(`2320D0`)", 조건 128 "부대 진형 지형 적합" | `2320D0` 은 무장의 개성 9칸 목록(world+0x7DD18[356]). 113 = 개성 효과 id, 114 = 개성 번호, 117 = 필요 효과 일치, 128 = 지형 특기 개성(수전·산전·숲전·오환·선비·흉노·강저·산월·남만, 번호 68~76)과 지형 id 대응 | `2320D0` 본문, `A9D50` asm(L3 5차) |
| C7 | 조건 122 "공격 실행 경로 가능"(`282230` = 근접 적 부대) | 탐색 결과 사전 판정: `282230` 재야 발견, `2826B0` 명승 발견, `281480` 옥새·동작·명품·전법서 발견 | `B0AC0`·`282230`·`2826B0`·`281480`(L3 5차) |
| C8 | 조건 139 "지역이점 경합" 의 소속 구조 | 거점 -> 도시 -> 주(도시 +0xCE, W+0xDC80[23]) -> 지방 이점(주 +0x30 = geo, W+0x85990[18]); cap = 지방 이점 기준 도시 수 | `A5B10`·`935F0`·`92AE0`·`93480`·`2C9120`(L3 5차) |
| C9 | `234880` = 혐오(conditions 162, functions 3차 묶음) | `234880` = 친애 목록(+0xC0), 혐오는 `2343A0`(+0xD0). 이간 불가는 친애 관계 | `234880`/`2343A0` 본문(L3 5차) |

### 충돌 (둘 다 기록, 해결 안 됨)

| # | 문서 A | 문서 B / 코드 | 상태 |
|---|---|---|---|
| X1 | rules_tribes.md:44, lane_L3.md:15: AI 관리자 `43DCB0`/`43E030` 호출자는 `442200 -> 44F2F0` | 현재 빌드 `43DCB0` 은 B6F90·D4xxx 를 안 부름, 옛 `43DCB0` = 현재 `440060`(`43FE30`+0x230) | 충돌(추정: 주소 혼용) |
| X2 | ai_trace/원작_수송판단_군단방침_조건84_20261020.md: 조건110 을 군단 중시항목(+0x1A)으로 추정 | AB2B0 코드: 군단 +0x17(data_model 라벨 방침) == sel+1 | 충돌(코드 확정, 의미 라벨 미해결) |
| X3 | REA 문서: 판단표 SHA c90ef6da... 불변 확인 | 현재 파일 SHA 315f16d0... | 충돌 해소: 파일이 갱신됨(2026-11-05) |

## 9. 미해결 (상세: ai/unresolved.md)

- L3b(2026-11-07) 해결: 의미를 못 정한 조건 22종(conditions.md 로 이동), `일자내부값`(= 일 == 1), `4403E0`/`440B30` 호출 객체(`COtherStrategyState`/`CUserStrategyState` 슬롯 5 가 작업 큐로 제출), BT 엔진 설정표 13칸(메모리 풀), 70xxxx 가용성 함수의 명령(conditions.md 전수표). 정보 조회 항목 105쌍은 전부 판독(ai/unresolved.md 3절). 군단 행동설정 +0x15 는 UI 설정이 아니라 판단표가 쓰는 군단 행동방침(0/1/2)으로 확정(ai/unresolved.md 4절).

## 10. ai/ 폴더 파일 목록

| 파일 | 내용 | 크기 |
|---|---|---|
| ai/command_index.tsv | 명령 노드 297개와 조건 사슬 | 113 KB |
| ai/conditions.md | 조건 167칸 전수표(사용 132종 의미·확신도·RVA·사용처) | 31 KB |
| ai/data_locations.md | 판단표·수식 파일 형식·위치, 메모리 표 위치 | 4 KB |
| ai/diff_bt_exce.md | 옛 판단표 대비 변경 구간·N번호 변환표 | 7 KB |
| ai/formulas.md | param_s.bin 수식 100개와 판단표 사용처 | 3 KB |
| ai/node_kinds.md | 노드 종류 232종 전수표(클래스·현재/옛 RVA·트리별 개수) | 20 KB |
| ai/pseudo_군단_00_공통준비.txt | 군단 N0~N720 | 81 KB |
| ai/pseudo_군단_01_행동설정0.txt | 군단 N722~N4512 | 513 KB |
| ai/pseudo_군단_02_행동설정1.txt | 군단 N4513~N8014 | 467 KB |
| ai/pseudo_군단_03_행동설정2.txt | 군단 N8015~N10483 | 326 KB |
| ai/pseudo_군단_04_군세목적갱신.txt | 군단 N10484~N10789 | 39 KB |
| ai/pseudo_군세.txt | 군세 판단표 전체 | 39 KB |
| ai/pseudo_부대.txt | 부대 판단표 전체 | 11 KB |
| ai/pseudo_세력.txt | 세력 판단표 전체 의사코드 | 24 KB |
| ai/roles.md | 영역별 AI 구조·의사코드·역할별 노드 위치 | 20 KB |
| ai/rulebase.md | 임계값·가중치·확률표·군세 행동표 | 10 KB |
| ai/schedule.md | 호출 주기·구동 구조·호출 사슬 충돌 | 6 KB |
| ai/thresholds.tsv | 판단표의 모든 숫자 비교·대입(2,969행) | 367 KB |
| ai/unresolved.md | 미해결·추정 목록 | 8 KB |

## 11. 출처 목록 (이 주제의 원본 자료와 상태)

| 자료 | 상태 | 쓴 내용 |
|---|---|---|
| 0000/bt_exce.bin | 현재 | 판단표 원본(CE). 재파싱한 1차 자료 |
| 0000/bt.bin | 현재 | 기본판 판단표(구조 수치만 대조) |
| 0000/param_s.bin | 현재 | 수식 100개 파일(해시 불변 확인) |
| REA_Analysis/verify_behavior_trees.py | 현재 | JBTP/KTBT 파서(코드 재사용, 파일 수정 없음) |
| REA_Analysis/behavior_trees_current.json | 낡음(옛 bt_exce 10312 군단 노드) | 노드 클래스·옛 실행 RVA·조건 옛 RVA 대응표로만 재사용. N번호는 쓰지 않음 |
| REA_Analysis/behavior_tree_validation.json | 낡음(옛 해시 c90ef6da) | 조건 130종·미해석 107종 기록. 현재는 132종, 확정/추정 아래 표로 대체 |
| REA_Analysis/README.md, ai_mechanisms.md | 개념 유효 / 수치 낡음 | 판단 순서·성공 의미·AI 전투력. N번호·노드 수는 낡음 |
| REA_Analysis/core_ai.pseudo.cpp | 개념 유효 | 선택/순서/전체검토 전환, 조건식 평가, 군세 재판단 10회, 요구전투력 탐색. RVA 는 옛 빌드 |
| REA_Analysis/*_행동트리.pseudo.cpp (4개) | 낡음 | 구조 래퍼 11,017 노드. 현재는 ai/pseudo_*.txt 로 대체 |
| REA_Analysis/predicates_recovered.md, predicates_partial.md, condition137_score.md | 현재와 일치 확인 | 조건 118/121/137/138/146 필드 해석(현재 빌드 코드로 재확인: 118=+0x11, 121=bit1, 137, 138, 146=+0x140) |
| REA_Analysis/data_model.md | 현재 | 객체 필드 표(세력·군단·무장·도시·지역·부대) |
| San14Sim/docs/fidelity/node_kinds.md, node_kinds.json | 옛 빌드 RVA | kind->클래스 목록. 현재 RVA 는 ai/node_kinds.md 로 대체 |
| San14Sim/docs/fidelity/conditions.json | 옛 빌드(C2610) | 조건 switch 167칸 호출 대상. 현재 C36A0 에서 다시 뽑음(op 2 의 옛 ACD10 -> 현재 ADC70 등 대부분 바뀜) |
| San14Sim/docs/fidelity/lane_L3.md, lane_L4.md | 현재(단, 43DCB0 호출 사슬은 충돌) | 날짜 상태기계 44DEE0, 이민족 호출 구조 |
| San14Sim/docs/fidelity/build_remap.md, rva_map/functions.tsv | 현재 | 옛->현재 RVA 변환 |
| AI_TacticsMod/research/AI_Analysis/all_behaviors/render_all_trees.py, node_catalog.json, recovered_node_map.json, 한국어변수대응.json | 재사용 | 한국어 표기 규칙·변수 이름·노드 클래스 한국어. 현재 트리에 다시 적용 |
| AI_TacticsMod/research/AI_Analysis/all_behaviors/AI_행동패턴_읽기.md, *_의사코드.txt | 개념 유효 / 군단 N번호 낡음 | 영역별 흐름·수치. 번호는 diff_bt_exce.md 로 변환 |
| AI_TacticsMod/research/AI_Analysis/deep/분석근거.md, formula_expressions.json | 유효 | 전투력·성향·수식 100개 |
| AI_TacticsMod/research/AI_Analysis/attack_decisions/, AI_공격판단_쉽게읽기.md, AI_전투력과_출진억제_쉽게읽기.md | 개념 유효 / N번호 낡음 | 공격 방식·억제 플래그 |
| AI_TacticsMod/research/AI_Analysis/upper/scheduler_callers.json | 옛 빌드 | 판단 진입 함수 호출자(옛 RVA) |
| AI_TacticsMod/research/ai_trace/*.md | N번호 낡음 | 플레이어 군단 공통 분기·요격·수송·조건84·조건108 설명 |
| AI_TacticsMod/tools/ghidra_full.py (현재 빌드 추출본) | 현재 | 조건 함수 본문·호출 관계(이번에 새로 읽음) |
| 분석용/*.md, graphify-out | 열지 않음 | 참고 모드 분석 문서(제목 확인). 원작 AI 트리 근거 아님 |

원본 문서는 수정·이동·삭제하지 않았다. 이 문서·`ai_behavior.json`·`ai/` 만이 K2 산출물이다. 재생성 스크립트는 저장소에 넣지 않았다(작업 임시 폴더).

## 12. 읽는 순서

1. 이 문서 0절 -> 2. ai/roles.md(찾는 영역) -> 3. ai/conditions.md(조건 의미) -> 4. ai/rulebase.md(수치) -> 5. ai/pseudo_*.txt(원문 흐름) -> 6. ai/diff_bt_exce.md(옛 문서의 N번호를 읽을 때).
