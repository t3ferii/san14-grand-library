# 조사 중복을 줄이는 AI 작업 순서

1. `docs/orig/README.md`에서 분야를 고른다. `rg -n '주제|한글이름|RVA' docs/orig`로 작은 후보를 찾는다.
2. 관련 절과 확신도·정정 기록을 읽는다. `functions.json`, `structs.json`은 검색 가능한 조사 요약이다. 완전한 함수 목록이나 전체 원본 코드가 아니다.
3. 데이터 값이면 `library.ps1 data tables`, `library.ps1 data table trait 5`, `library.ps1 data scenario 3 city 3`으로 읽는다. 구조체 뜻은 다른 모드 소스 주석이 아니라 원작 문서·실제 쓰는 함수로 확인한다.
4. 코드 근거가 더 필요하면 `library.ps1 func <RVA> --limit 120`, `callers`, `callees`, `xref`, `str`, `vtable`, `find`, `grep`를 사용한다. 검색 결과를 좁힌 뒤 필요한 함수만 읽는다. 주소는 RVA 또는 `0x140000000 + RVA`를 받을 수 있다.
5. `library.ps1 bytes <RVA> --length 32`는 검증된 로컬 분석 사본의 파일 바이트를 읽는다. 실행 중 게임 메모리를 읽거나 쓰지 않는다. vtable 검색은 Ghidra 후보 표라 완전한 클래스 의미를 보장하지 않는다.
6. 조사 문서에서 답이 확인되면 멈춘다. 더 조사해야 할 때는 미해결 질문·필요한 근거·확인 범위를 먼저 정한다. 이미 있는 전체 분석을 반복하지 않는다.
7. 새로운 사실은 해당 주제의 기존 절을 고치고 PR을 만든다. 로컬 캐시는 올리지 않는다.

예시: 등용 성공률이 궁금하면 인사 문서에서 등용 절을 찾고 → 해당 함수 RVA 조회 → 호출자가 넘기는 조건 확인 → 기존 설명과 다를 때만 정정한다. 처음부터 EXE를 열어 "등용 관련 함수 전부 찾기"를 반복하지 않는다.

초기 이관 문서에 남아 있는 `San14Sim/`, `AI_TacticsMod/`, `research/`, `fidelity/`, `REA_Analysis/` 경로는 과거 조사 출처의 이름이다. 이 공개 저장소의 실행 경로가 아니다. 실행 명령은 이 문서와 SETUP을 따른다. 공개하지 않은 자료 링크는 `ARCHIVE_REFERENCES.md`에서 어떤 출처가 빠졌는지 확인한다. 없는 출처를 읽었다거나 재검증했다고 보고하지 않는다.
