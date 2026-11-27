# 군단 판단표 교체 경계 (백엔드 설계 재료)

작성 2026-11-27. 기준 빌드 Steam `1a4a447d`. 목적: 군단 판단표 전체를 새 백엔드로 바꿀 때 경계에 걸리는 원작 사실을 한곳에 모은다. 새 조사는 거의 없다. 출처는 대도서관 문서(`ai_behavior.md`, `ai/*.md`), 턴 주기 측정(`materials/cycle_functions.tsv`, `docs/orig/cycle/`), 원작만 추적 기록(`AI_TacticsMod/data/ai_trace/trace_original_*.csv`, 13판)이다.

확신도: **코드** = 디컴파일·바이트 확인, **실측** = 추적 기록·리프트 측정, **추정**, **미확인**. 「대량」 표시 이름은 턴 주기 B층(작업자 묶음, 교차 확인 오답 1.8%, 「추정」 행 약 55%)이며 손으로 검토하지 않았다.

비용은 모두 리프트(기계 번역본) 안의 상대값이다. 세이브 하나에서 10일째 차례 → 전략 → 진행 10일 → 20일째 차례 한 주기를 쟀다(`recon/lift/PLAN.md` 6·8절). 재귀·다른 스레드 때문에 포함 비용의 합은 100%를 넘을 수 있다.

## 0. 한눈에

- 군단 판단표는 데이터다. `0000/bt_exce.bin`의 군단 트리 10,790 노드를 원작 실행기가 돌린다. 원작 코드는 노드 종류 232종의 실행 함수와 조건 132종(dispatch `C36A0`)이다(`ai_behavior.md` 3·5절, 코드).
- **교체 경계는 `D4D70(AI 관리자, 군단)` 한 함수다**(코드, `ai/schedule.md` 2절). 플레이어 직할 군단이면 바로 돌아오고, 아니면 `B6730`(군단 판단표 실행)을 한 번 부른다. `B6730`의 호출자는 `D4D70` 하나다.
- 군단 판단표가 게임에 남기는 것은 명령 노드 49종과 그 밖의 쓰기 노드 17종(2절), 판단 뒤에도 남는 상태(4절)다. 백엔드는 이 출력을 대신 만들어야 한다. 2절은 `ai/node_kinds.md`에서 군단 열이 0보다 큰 종류를 모두 훑고 읽기·목록·산술 종류를 뺀 결과다. 4절은 확인된 것이고 전수는 아니다.
- 비용: 군단 판단표(`D4D70`)의 포함 비용은 한 주기 전체의 **45.2%**다. 세력 판단표는 0.02%, 군세 1.37%, 부대 1.03%다. 군단 판단표 안에서는 이동 비용 노드 `8F5A0`이 15.8%, 조건 평가 `C36A0`이 10.5%다(5절, 실측).
- 기록 범위의 한계: 리프트 한 주기에서 군단 트리의 명령 노드 49종 중 25종만 돌았다. 외교·계략 명령은 0번이다. 원작만 추적 기록 13판에서도 외교는 드물고 계략 7종은 한 번도 없다(6절).

## 1. 진입과 주기

| 사실 | 근거·확신도 |
|---|---|
| `44DD30`(`COtherStrategyState` 슬롯 5)이 세력마다 작업 큐로 `4403E0`을 제출한다. 날짜 상태기계 `44DEE0`은 판단표를 부르지 않는다 | `ai/schedule.md` 3·4절, 코드 |
| `4403E0`(세력 하나)의 순서: AI 관리자 `+0xC0` 이동 비용 캐시를 지움 → 세력 판단표 `D4DE0` → 군단마다 `C1790` + `D4D70` → 그 군단의 군세마다 `D4E20` → 부대마다 `D4D00` → 끝에 `B2D30`(군단 재편 검사) | `ai/schedule.md` 2절 코드, `ai/roles.md` 6-7절 1 실측(272회 모두 이 순서) |
| `4403E0`은 순(10일)마다 세력마다 한 번, 매번 새 스레드에서 돈다. 세력끼리 동시에 도는지는 | 실측(스레드 재사용 0) / 동시 실행 여부 **미확인** |
| `4403E0`은 플레이어 세력에는 돌지 않는다 | `ai/roles.md` 6-7절 11, 실측 |
| `D4D70`은 플레이어 직할 군단(`330B50(world+0x871E8)`과 군단 번호 `22F650`이 같음)이고 `334C30()==0`이면 돌아온다 | `ai/schedule.md` 2절, 코드 |
| 위임 군단: 변형 `440B30`이 플레이어 군단 확인(`330B90`, `235300`) 뒤 `D4D70`을 부른다. 위임 군단 재판단용으로 보인다 | 추정 |
| 판단표 안에서도 「플레이어소속군단」 분기가 있다: N9, N722(`행동설정 == 0 또는 플레이어소속군단`) | `ai/roles.md` 2절, 코드(정적) |
| 군단 트리 안의 주기: N5 `군단판단난수`(상한 100, 입력 군단 ID·경과카운터), N56 `목표검토난수`. AI 설정 단계별 공격 검토 시작 기준 8/5/-1 | `ai/schedule.md` 3절, 코드(구조) |
| 세력 판단표는 매달 1일에만 공략·친선 대상을 다시 고른다 | `ai/schedule.md` 3절, 확정 |
| 군단 트리의 큰 틀: N0~N720 공통 준비 → N721 선택(행동설정 0/1/2 세 분기 N722/N4513/N8015) → N10484~N10789 군세 목적 갱신. 일반 거점 공격 5노드는 분기 0에만 있다 | `ai/roles.md` 2절, 코드(정적) |
| 이민족·도적(세력 46~50)은 판단표를 쓰지 않는다 | `ai/schedule.md` 3절 |

## 2. 출력: 군단 트리의 명령 노드

열 설명:
- 「군단 트리 노드 수」 = `ai/node_kinds.md`의 군단 열.
- 「리프트 한 주기 실행」 = 그 노드 종류의 실행 함수가 한 주기에 불린 횟수(실측). 군단 13개가 판단했다. 실행 함수를 다른 트리와 같이 쓰는 종류도 있다.
- 「추적 기록 언급 줄」 = 원작만 추적 기록 13판(턴 약 199개, 대부분 관전)에서 그 노드 이름이 나온 줄 수. 실행 횟수가 아니고 「돌았는가」의 표시로만 본다(실측).
- 출진 명령이 실제로 부르는 원작 함수(예: 거점 공격 `2FE10` → `C0390` → `43A50` → `1EDC30`)와 26칸 출진 명령은 `ai/roles.md` 2-3-3·2-3-6·6-3·6-3a·6-3b절에 있다.
- 명령마다 인수와 조건 사슬은 `ai/command_index.tsv`(명령 노드 297개), 가용성(합법성) 함수 70xxxx와 후보 목록 함수 6Dxxxx는 `ai/conditions.md`에 있다.

### 군사 출진

| 노드 종류 | 실행 RVA | 군단 트리 노드 수 | 리프트 한 주기 실행 | 추적 기록 언급 줄 | 대도서관 이름(출처) |
|---|---|---|---|---|---|
| `CCommandFootholdAttackDepatureNode` | `2FE10` | 5 | 4 | 27879 | CCommandFootholdAttackDepatureNode Execute (거점 공격 출진) (함수 지도) |
| `CCommandAreaOccupyDepatureNode` | `29BA0` | 9 | 13 | 61836 | CCommandAreaOccupyDepatureNode Execute (지역 점령 출진 명령 BT 노드) (함수 지도) |
| `CCommandAreaTryGetDepartureNode` | `2AB90` | 1 | 0 | 0 | (측정 없음) |
| `CCommandAutoPaintDefenseDepartureNode` | `2CBC0` | 3 | 3 | 548 | 자동 방어 출진 노드 실행 (대량·추정) ※잘림 |
| `CCommandTransportDepatureNode` | `32D90` | 6 | 13 | 14855 | 수송 출발 노드 실행 (대량·추정) ※잘림 |
| `CCommandFrontFootholdTransportDepatureNode` | `30EF0` | 3 | 13 | 13803 | 거점 수송 출발 노드 실행 (대량·추정) ※잘림 |
| `CDepartureNode` | `35A70` | 19 | 1 | 16116 | CDepartureNode Execute (부대편성출진) (함수 지도) |
| `CDepartureTroopsCreateNode` | `365A0` | 19 | 1 | 2920 | CDepartureTroopsCreateNode Execute (군세생성) (함수 지도) |
| `CSpecifiedTroopsSetPurposeNode` | `6F070` | 22 | 1 | 6161 | CSpecifiedTroopsSetPurposeNode Execute (지정 부대 임무 설정 BT 노드) (함수 지도) |

### 군단 방침·상태

| 노드 종류 | 실행 RVA | 군단 트리 노드 수 | 리프트 한 주기 실행 | 추적 기록 언급 줄 | 대도서관 이름(출처) |
|---|---|---|---|---|---|
| `CDistrictSetPurposeNode` | `36D00` | 4 | 13 | 2991 | 군단 목적 설정 노드 실행 (대량·추정) |
| `CCautionTroopsListAddNode` | `28D20` | 1 | 4 | 1046 | 경계 부대 목록 추가 노드 (대량·추정) ※잘림 |
| `CCautionTroopsListAddUniqueNode` | `29190` | 3 | 0 | 833 | (측정 없음) |
| `CCautionTroopsRemoveNode` | `29990` | 1 | 0 | 911 | (측정 없음) |
| `CCautionTroopsClearNode` | `28CC0` | 2 | 0 | 23 | (측정 없음) |
| `CCautionTroopsUpdateStatusNode` | `29B40` | 3 | 1 | 427 | 경계군세 상태 갱신 노드 (대량·코드) |
| `CCautionArmyAddUniqueNode` | `283F0` | 6 | 9 | 3977 | 경계 군대 기록 추가 노드 (대량·추정) |
| `CSetCautionTroopsVirtualTargetFootholdNode` | `85F70` | 1 | 0 | 1610 | (측정 없음) |

### 내정·배치

| 노드 종류 | 실행 RVA | 군단 트리 노드 수 | 리프트 한 주기 실행 | 추적 기록 언급 줄 | 대도서관 이름(출처) |
|---|---|---|---|---|---|
| `CDomesticOfficerSetNode` | `36E80` | 6 | 137 | 189 | 무장 지역 설정 변경 노드 (대량·추정) |
| `CDomesticPriorityDevelopmentSelectNode` | `7B0B0` | 6 | 137 | 189 | 우선 개발 항목 선택 노드 (대량·추정) |
| `CRecruitOfficerSetNode` | `3E750` | 6 | 10 | 181 | CRecruitOfficerSetNode Execute (등용 담당관 설정 BT 노드) (함수 지도) |
| `CTrainingOfficerSetNode` | `3EF50` | 6 | 2 | 176 | CTrainingOfficerSetNode Execute (훈련 담당관 설정 BT 노드) (함수 지도) |
| `CSceneryInvestSetNode` | `3E890` | 3 | 3 | 181 | 명승 투자 설정 노드 (대량·추정) |
| `CSpyHomeOfficerSetNode` | `3EBC0` | 18 | 8 | 189 | 첩보 담당 무장 설정 노드 (대량·추정) |
| `CSpyHomeOfficerRemoveNode` | `3EAA0` | 36 | 14 | 189 | 첩보 슬롯 비우기 노드 (대량·추정) |
| `CForceCommandMoveNode` | `55310` | 3 | 11 | 2410 | 군단 거점 간 무장 이동 노드 (함수 지도) |

### 인사·실행 명령

| 노드 종류 | 실행 RVA | 군단 트리 노드 수 | 리프트 한 주기 실행 | 추적 기록 언급 줄 | 대도서관 이름(출처) |
|---|---|---|---|---|---|
| `CCommandExecutionEmployNode` | `2D720` | 3 | 8 | 125 | CCommandExecutionEmployNode Execute (임용 명령 실행 BT 노드) (함수 지도) |
| `CCommandExecutionHireNode` | `2DAB0` | 3 | 1 | 81 | 등용 실행 노드(컴퓨터) (대량·추정) |
| `CCommandExecutionPrizeNode` | `2EEA0` | 3 | 8 | 174 | 포상 실행 노드 (대량·추정) |
| `CCommandExecutionSearchNode` | `54AD0` | 6 | 26 | 189 | 탐색 명령 실행 노드 (대량·코드) |
| `CCommandExecutionSpyAwayNode` | `54BC0` | 3 | 2 | 106 | 첩보 명령 실행 노드 (대량·코드) |
| `CCommandExecutionInspectNode` | `2DCD0` | 3 | 0 | 146 | (측정 없음) |
| `CCommandExecutionCreditGiveNode` | `2D2A0` | 3 | 0 | 26 | (측정 없음) |
| `CCommandExecutionCreditRankUpNode` | `2D440` | 3 | 0 | 149 | (측정 없음) |
| `CCommandExecutionMerchantNode` | `2E410` | 6 | 0 | 35 | (측정 없음) |
| `CCommandExecutionItemNode` | `54250` | 3 | 0 | 5 | (측정 없음) |
| `CCommandExecutionTradeNode` | `54CE0` | 3 | 0 | 0 | (측정 없음) |

### 외교

| 노드 종류 | 실행 RVA | 군단 트리 노드 수 | 리프트 한 주기 실행 | 추적 기록 언급 줄 | 대도서관 이름(출처) |
|---|---|---|---|---|---|
| `CCommandExecutionGoodwillNode` | `53930` | 2 | 0 | 30 | (측정 없음) |
| `CCommandExecutionAllianceNode` | `52990` | 4 | 0 | 2 | (측정 없음) |
| `CCommandExecutionAnnulNode` | `52B60` | 3 | 0 | 3 | (측정 없음) |
| `CCommandExecutionAttackRequestNode` | `52CA0` | 2 | 0 | 0 | (측정 없음) |
| `CCommandExecutionExchangeNode` | `53530` | 12 | 0 | 2 | (측정 없음) |
| `CCCommandExecutionPrisonerReturnNode` | `548D0` | 3 | 0 | 20 | (측정 없음) |

### 계략

| 노드 종류 | 실행 RVA | 군단 트리 노드 수 | 리프트 한 주기 실행 | 추적 기록 언급 줄 | 대도서관 이름(출처) |
|---|---|---|---|---|---|
| `CCCommandExecutionEstrangeNode` | `533F0` | 2 | 0 | 0 | (측정 없음) |
| `CCommandExecutionDualDestructionNode` | `53270` | 2 | 0 | 0 | (측정 없음) |
| `CCCommandExecutionHiddenPoisonNode` | `54110` | 2 | 0 | 0 | (측정 없음) |
| `CCCommandExecutionPlacationNode` | `545D0` | 2 | 0 | 0 | (측정 없음) |
| `CCommandExecutionRumorNode` | `2F080` | 2 | 0 | 0 | (측정 없음) |
| `CCommandExecutionBuildingDestructionNode` | `52EC0` | 12 | 0 | 0 | (측정 없음) |
| `CCommandExecutionUnattendedHomeNode` | `54F50` | 2 | 0 | 0 | (측정 없음) |


### 그 밖의 쓰기 노드 (명령은 아니지만 객체나 목록을 바꿈)

| 노드 종류 | 실행 RVA | 군단 트리 노드 수 | 리프트 한 주기 실행 | 무엇을 바꾸나 | 확신도 |
|---|---|---|---|---|---|
| `CSetTargetForceListNode` | `58C90` | 1 | 1 | 세력 `+0x17A` u8[5] 공략 대상 세력 목록 | 코드(`ai/unresolved.md` 3절 Force 27) |
| `CClearTargetForceListNode` | `52950` | 1 | 1 | 같은 목록 지우기 | 대량·추정 |
| `CCallScriptNode` | `5D760` | 12 | 72 | 스크립트 호출. 무엇을 부르고 무엇을 바꾸는지 | **미확인** |
| `CSelectPersonTacticsNode` | `85BE0` | 14 | 1 | 출진 무장의 전법 3개 선택 | `ai/roles.md` 2-3-7 |
| `CRemoveNoInterceptPersonNode` | `85810` | 3 | 1 | 요격 불가 무장을 후보 목록에서 뺌 | `ai/roles.md` 2-3-7 |
| `CRecruitOfficerRemoveNode` | `3E6B0` | 6 | 0 | 모병 담당 해제 | 이름만(측정 없음) |
| `CTrainingOfficerRemoveNode` | `3EEB0` | 3 | 0 | 훈련 담당 해제 | 이름만(측정 없음) |
| `CItemSelectNode` | `80A10` | 3 | 0 | 물품 선택 | 이름만(측정 없음) |
| `CTradePriorityCountrySelectNode` | `860C0` | 3 | 0 | 교역 우선 상대 선택 | 이름만(측정 없음) |
| `CMiscSet{Foothold,Person,Area}EvaluationNode`, `CSet{CautionTroops,Formation,Force}EvaluationNode` | `6EFD0`, `85580` | 29+119+10+9+14+37 | 1,329 / 439 | 평가값 쓰기. 경계군세는 객체 `+0x08` 점수 칸(`ai/roles.md` 2-3-4). 거점·무장·세력·진형 쪽이 객체에 남는지 블랙보드에만 있는지 | 경계군세 코드 / 나머지 **미확인** |
| `CCautionTroopsSortNode`, `CCautionTroopsListRemoveNullUnit` | `29A90`, `29390` | 2, 2 | 4, 26 | 경계군세 목록 정렬·빈 부대 제거 | 대량 |

## 3. 입력: 군단 트리가 읽는 것

| 무엇 | 어디에 | 한 주기 실측 |
|---|---|---|
| 정보 노드(`CVariableGet*InfoNode` 등): 무장·거점·지역·군단·세력·부대·칸·진형·명승 정보 항목 | 항목 105쌍 판독: `ai/unresolved.md` 3절. 노드 종류: `ai/node_kinds.md` | 무장 정보 `8F810` 6,211회, 지역 `86720` 4,124회, 거점 `8B190` 3,901회, 부대 `90110` 570회, 세력 `8CAE0` 429회 |
| 조건 132종(객체 종류·판단 주체·명령 가용성 70xxxx·후보 목록 6Dxxxx) | `ai/conditions.md` | 조건식 평가 `B319B0` 28,050회, 개별 조건 dispatch `C36A0` 43,127회 |
| 이동 비용·거리 | `CVariableGetMoveCostNode` `8F5A0`(AI 관리자 `+0xC0` 지역 간 비용 캐시 `int[500][500]`, 세력마다 지움), `CGetAreaDistanceNode` `7B6D0`, `CVariableGetDistanceNode` `886F0` | `8F5A0` 370회, 포함 비용 15.8% |
| 전투력 평가 | `CGetFootholdFightingStrengthNode` `7EBA0`, `CGetHexAroundFightingStrengthNode` `7EF50`, `CGetBattlePowerSoldierNumNode` `7BE80` | 136·32·1회 |
| 판단표 상수·수식 | 비교·대입 2,969행 `ai/thresholds.tsv`, 수식 100개 `0000/param_s.bin`(`ai/formulas.md`), 확률표·기준 `ai/rulebase.md` | — |
| 난수 | `CVariableSetRandomNumberNode` `92870`(진행값 기반 난수) | 291회 |

## 4. 판단 뒤에도 남는 상태 (백엔드가 같이 만들어야 하는 것)

군단 트리가 끝난 뒤 다른 판단표, 날짜 진행, 다음 순이 읽는 것이다. 여기서 빠진 것이 있으면 군단 판단표를 꺼도 게임이 이상하게 돈다.

| # | 상태 | 쓰는 곳 | 읽는 곳 | 확신도 |
|---|---|---|---|---|
| 1 | 군단 `+0x15` 행동방침(0 공세·확장 / 1 보급·내실 / 2 모병·재편) | `CDistrictSetPurposeNode` `36D00`(N705~N720) | 다음 순 군단 트리의 세 분기 선택(조건 26). 판단표 밖에서 읽는 곳은 | 쓰기·분기 코드(`ai/unresolved.md` 4절) / 판단표 밖 읽기 **미확인** |
| 2 | 군세 `+0x14` 종류, `+0x16` 목표(거점 번호 또는 경계군세 번호) | `CDepartureTroopsCreateNode` `365A0`(새 군세), `CSpecifiedTroopsSetPurposeNode` `6F070`(N10484~ 군세 목적 갱신) | 군세 판단표 `D4E20`이 종류별로 행동을 정한다(`ai/roles.md` 6절) | 코드(`ai/roles.md` 6-2b) |
| 3 | 경계군세 레코드: world `+0x80BA8` 포인터 표 501칸(객체 `0x48`바이트) | 경계 자료 노드 14종(`28D20`, `283F0`, `29B40` 등) | 군세 종류 1·0x13의 목표, 다음 순의 경계 판단 | 코드(`ai/roles.md` 2-3-4) |
| 4 | 출진으로 생긴 군세·부대(게임 객체)와 26칸 출진 명령 | 출진 노드 → `43A50` → `1EDC30` | 군세·부대 판단표, 날짜 진행 `44DEE0`의 이동·전투 | 코드(`ai/roles.md` 6-3) |
| 5 | 수송(병력·금·군량 이동) | `32D90`·`30EF0` → `201C20` → `2DAFC0` | 날짜 진행(수송 부대 도착) | 코드(`ai/roles.md` 2-3-6) |
| 6 | 무장 배치: 지역 담당관·개발 우선 항목·모병·훈련 담당·첩보 담당·명승 투자·거점 간 이동 | 내정·배치 노드 8종(2절) | 날짜 진행의 내정 처리, 다음 순 판단 | 노드 이름은 대량·추정이 많다. 쓰는 필드 손 확인 **미확인** |
| 7 | 판단 인스턴스: AI 관리자 `+0x90` 맵(키 = 군단 포인터), 인스턴스 `+0x18` 블랙보드, `+0x28~+0x38` 문맥 스택 | `BB2E0`, `C1790`, `B27D70` | 같은 군단의 다음 판단. 군단 트리 변수가 순을 넘어 남는지는 | 구조 코드(`ai/schedule.md` 1절) / 순 간 유지 **미확인** (군세 요격 노드 상태는 순을 넘어 유지됨, `ai/roles.md` 6-7절 6) |
| 8 | 재실행 플래그 군단 `+0x2A` | `CSetBehaviortreeRestartFlagNode` `85EC0`(`AgentType` 값으로 대상 선택) | `B6730` | 코드. 다만 `ai/node_kinds.md`의 군단 열은 0이다(군단 트리에 이 노드가 없음) |
| 9 | 군단 `+0x17`(방침, 조건 110이 읽음), `+0x1A`(내정 중시 항목으로 추정) | 쓰는 노드 | 판단표 조건, 내정 처리 | 읽기 코드(`ai_behavior.md` 8절 X2) / 쓰는 곳 **미확인** |

판단표 밖에서 군단 판단 결과를 덮어쓰는 원작 코드도 있다: 외톨이 군세의 플레이어 부대 기습 `CE7E0`(`ai/roles.md` 6-5), 부대 명령 일일 검사 `273AC0`(6-4a), 군세 판단표 진입 `B6B00`이 직접 쓰는 경유점(6-7절 3). 백엔드가 명령을 내도 이 코드는 그대로 돈다.

## 5. 비용 (한 주기, 리프트 상대값, 실측)

| 함수 | 뜻 | 호출 | 포함 % |
|---|---|---|---|
| `4403E0` | 세력 하나 판단(세력·군단·군세·부대 전체) | 10 | 37.8 |
| `D4D70` / `B6730` | 군단 판단표 | 13 | 45.2 |
| `D4E20` | 군세 판단표 | 42 | 1.37 |
| `D4D00` | 부대 판단표 | 18 | 1.03 |
| `D4DE0` | 세력 판단표 | 10 | 0.02 |
| `8F5A0` | 이동 비용 노드(군단 트리 안) | 370 | 15.8 |
| `C36A0` | 조건 dispatch | 43,127 | 10.5 |
| `185710` | 경유지 결합 길찾기(최대 5경유). 전략 917회 + 진행 510회 | 1,427 | 48.6 |
| `44DEE0` | 날짜 진행 상태기계 | 479 | 8.5 |

- `D4D70` 13회 중 12회는 `4403E0`, 1회는 위임 군단 변형 `440B30`(포함 10.3%)에서 불렸다. 그래서 `D4D70`(45.2%)이 `4403E0`(37.8%)보다 크다(실측). `440B30`은 위임 군단 재판단 변형으로 추정한다(1절).
- `C36A0`(조건 dispatch)은 네 판단표 모두의 조건을 맡는다. 10.5%가 모두 군단 트리 몫은 아니다.
- 한 주기 자체 비용 1위는 길찾기 `185710`(25.3%)과 A* `184D60`(7.1%)이다. 군단 트리의 이동 비용 질의가 이 길찾기를 부르는 비율은 `prof_edges.tsv`로 더 나눌 수 있다(이번에 안 함).

## 6. 기록 범위의 한계

- 리프트 한 주기(세이브 하나, 10일): 군단 트리 명령 노드 49종 중 25종이 돌았다. 외교 6종·계략 7종·인사 일부(감찰·관직·상인·물품·교역)는 0번이다.
- 원작만 추적 기록 13판(턴 약 199개): 군사 출진·수송·요격은 수백~수천 줄이다. 외교는 친선 30줄, 동맹 2줄, 파기 3줄, 교환 2줄, 포로 반환 20줄뿐이다. 계략 7종(이간·이호경식·은독·회유·유언·시설 파괴·무인 도시)과 공격 요청·교역은 0줄이다.
- 그래서 외교·계략 쪽은 판단표 의사코드(`ai/pseudo_군단_*.txt`)와 정적 해석만 있다. 실제로 어느 조건에서 도는지 실측이 없다.
- 군단 판단표의 첫 줄 주기(매달 1일 대상 재선정)를 포함한 리프트 주기는 아직 없다. 지금 스냅숏은 10일째 차례다.

## 7. 판단표 노드 실행 함수의 해석 상태

- 리프트에서 돈 판단표 노드 실행 함수는 모두 이름과 한 줄 역할이 있다(턴 주기 B층, `docs/orig/cycle/ai.md`).
- 2절 표에서 「대량·추정」이고 「※잘림」인 것(`2CBC0`, `32D90`, `30EF0`, `28D20`)은 150줄까지만 읽혔다. 다만 `32D90`·`30EF0`·`2CBC0`은 `ai/roles.md` 2-3-5·2-3-6절에 손 판독이 따로 있다.
- 내정·배치 노드 8종과 인사 실행 노드는 대량 해석만 있다. 무엇을 어디에 쓰는지 손으로 확인하지 않았다(4절 6번).
- 턴 주기 C층 후보 786개(`materials/cycle_tierc.tsv`)를 이어서 읽는다(사용자 2026-11-27). 위 「대량」 이름은 C층에서 손 검토된 이름으로 바뀐다.
