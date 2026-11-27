# 삼국지14 대도서관: 원작 지식 목차

삼국지14 PK CE 한국어판의 함수·구조체·데이터 형식·게임 규칙·AI·UI 조사 결과를 모은다. 초기 통합 조사 문서를 공개용으로 이관했으며, 이관 자체가 모든 주장을 새로 검증했다는 뜻은 아니다. 각 문서의 확신도·정정·미해결을 함께 읽는다.

현재 기준: Steam buildid **25953386**, 분석 EXE SHA256 `1a4a447d14e68c40ad2a5107c29c7341c10eee8fc297a7b35032900c341dbcaa`. 옛 `1fbe6be7` 빌드의 주소는 비교 자료다. [빌드 간 주소](build_addresses.md)를 확인한다.

## 찾는 순서

1. 아래 분야 문서에서 주제를 찾는다. 함수 이름·RVA는 함수 지도, 필드 뜻은 구조체 문서에서 찾는다.
2. 원본 데이터 값은 `library.ps1 data ...` 또는 `origlib`로 읽는다.
3. 코드 근거가 더 필요하면 준비된 로컬 캐시를 `library.ps1 func|callers|callees|xref|bytes ...`로 조회한다.
4. 답이 없을 때만 필요한 부분을 추가 조사한다. 새 사실은 해당 문서의 기존 절에 추가하고 정정 기록을 남긴다.

## 분야별 문서

| 분야 | 문서 |
|---|---|
| 출처와 이관 | [SOURCES.md](SOURCES.md), [파일별 출처](../PROVENANCE.json) |
| 데이터 형식 | [게임 규칙 파일](data_formats_game.md), [아카이브·자원](data_formats_archives.md) |
| 함수 | [functions.md](functions.md), [functions.json](functions.json) |
| 구조체·필드 | [structs.md](structs.md), [structs.json](structs.json) |
| 빌드 간 주소 | [build_addresses.md](build_addresses.md) |
| 턴 주기 함수 전수(리프트 실행 기록: 호출 수·비용) | [cycle/README.md](cycle/README.md) — 10일 턴 → 컴퓨터 전략 → 10일 진행에서 돈 함수 3,937개 전부, 해석은 분류별 쪽에 합쳐 있다 |
| 전투 | [교전·피해식](rules_combat.md), [전법·개성·효과](rules_combat_effects.md) |
| 이동·병참 | [이동](rules_movement.md), [병참·보급](rules_movement_supply.md) |
| 날짜·이벤트 | [날짜 처리](rules_time.md), [이벤트 opcode 색인](event_opcodes.json) |
| 내정·인사 | [내정](rules_domestic.md), [인사](rules_people.md) |
| 외교·이민족 | [외교](rules_diplomacy.md), [이민족·도적](rules_tribes.md) |
| 원작 AI | [통합 해석](ai_behavior.md), [AI 자료 위치](ai/data_locations.md), [조건](ai/conditions.md), [노드](ai/node_kinds.md), [역할](ai/roles.md), [룰베이스](ai/rulebase.md), [일정](ai/schedule.md), [수식](ai/formulas.md), [변경 조사](ai/diff_bt_exce.md), [미해결](ai/unresolved.md) |
| 원작 UI | [구조·생명주기](ui_native.md), [레이아웃 색인](ui_layouts.json) |

## 초기 이관 자료의 한계

기존 조사에서 인용한 `San14Sim/docs/fidelity`(2026-11-25부터 `San14Library/archive`), `San14Library/reports`, `AI_TacticsMod/research`, `REA_Analysis` 등은 공개 패키지에 포함되지 않는다. 문서 안의 경로는 역사 출처를 식별하기 위한 것이며 실행할 지침이 아니다. [이전 출처 안내](../ARCHIVE_REFERENCES.md)를 따른다. 전수 AI 트리·원작 대량 추출물은 로컬 데이터 리더로 조회한다.

함수 의미·오프셋을 모드에 쓸 때는 문서의 서술뿐 아니라 대상 빌드의 바이트·호출자·ABI를 확인한다. [대도서관 규칙](../LIBRARY_RULES.md)과 [AI 조회 순서](../AI_WORKFLOW.md)를 따른다.
