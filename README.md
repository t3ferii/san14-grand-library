# 삼국지14 대도서관 · San14 Grand Library

**Steam 삼국지14 PK CE 한국어판을 위한 공동 원작 지식과 AI 모딩 도구입니다.**
각 모더는 자기 모드를 만들고, 원작을 조사한 지식은 이곳에 모읍니다. 게임 파일과 코드 캐시는 각자의 정품 설치본으로 로컬에서 만듭니다. 같은 함수·데이터 형식을 매번 새로 조사하는 비용을 줄이는 것이 목표입니다. 비공식 커뮤니티 프로젝트이며 게임 제작사와 관계없습니다.

## GitHub 주소만 AI에게 주세요

```text
https://github.com/t3ferii/san14-grand-library
이 대도서관의 AGENTS.md와 README를 읽고 내 PC에서 준비 작업을 자동 실행해 줘.
Steam에 설치한 삼국지14 CE 한국어판으로 로컬 캐시를 만들고 조회까지 확인해 줘.
준비되면 내가 만들 모드에 필요한 기존 조사부터 찾아 줘.
```

내 PC에서 PowerShell 명령을 실행할 수 있는 AI 에이전트를 전제로 합니다. AI는 아래 **두 줄을 실행하고 완료 상태를 확인**하면 됩니다. Git, Python, Java, Ghidra, Steamless를 미리 설치하거나 사용자가 경로를 알아낼 필요가 없습니다. Windows 10/11 x64와 PowerShell 5.1+, 인터넷, Steam 게임 설치본, 여유 공간 8 GiB 이상이 필요합니다. 준비 프로그램은 관리자 권한을 요구하지 않습니다.

```powershell
Invoke-WebRequest 'https://raw.githubusercontent.com/t3ferii/san14-grand-library/main/bootstrap.ps1' -OutFile "$env:TEMP\san14-library-bootstrap.ps1" -UseBasicParsing
& "$env:TEMP\san14-library-bootstrap.ps1"
```

현재 PowerShell 세션이 로컬 스크립트 실행을 제한하면 두 번째 줄을 다음으로 실행합니다. 시스템 실행 정책은 변경하지 않습니다.

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "$env:TEMP\san14-library-bootstrap.ps1"
```

준비 도구는 기존 Python과 버전이 확인되는 Java·Ghidra·Steamless를 우선 사용하고, 부족한 도구만 고정 공식 배포본과 SHA256으로 확인해 사용자 전용 폴더에 준비합니다. Steam 라이브러리에서 CE 한국어판을 찾아 **별도 사본만 언패킹**하고 최초 분석 → 함수·호출관계 추출 → SQLite 색인 → 표본 조회 검사까지 실행합니다. 게임 EXE를 실행하거나 설치본을 덮어쓰지 않습니다. Steam 구입 여부 자체를 인증하는 도구는 아닙니다.

캐시 검증까지 성공하면 프로그램이 새로 받은 **Java·Ghidra·Steamless와 설치 ZIP을 자동 정리**합니다. 기존 도구·기존 파일·수정된 도구는 보존하고, 실패·중단 시에는 재시도용 파일을 남깁니다. Python은 조회에도 필요하므로 기존 것을 사용하거나, 없으면 최소 embedded Python만 유지합니다. 캐시·색인·분석 프로젝트·작업 사본·도서관 소스는 그대로 남습니다. [기존 도구 재사용과 정리 기준](docs/SETUP.md#기존-도구-재사용과-완료-후-정리)

최초 분석·디컴파일은 오래 걸릴 수 있습니다. 진행 로그 경로와 도구 생존 상태가 출력됩니다. 이후에는 동일한 명령을 실행해 캐시를 재사용합니다. 준비 과정에서 AI가 분석 코드를 새로 작성할 필요는 없습니다. 토큰 사용은 저장소 안내를 읽고 명령과 결과를 확인하는 데만 필요하며, 실제 다운로드·분석은 프로그램이 수행합니다.

## 이미 저장소를 받은 경우

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\prepare.ps1
.\library.ps1 status
.\library.ps1 func 862030 --limit 100
.\library.ps1 callers 862030 --limit 30
.\library.ps1 bytes 862030 --length 32
.\library.ps1 data tables
```

Steam 설치가 여러 개거나 자동 탐색에 실패한 경우에만 `prepare.ps1 -GamePath 'D:\SteamLibrary\steamapps\common\Romance_of_the_Three_Kingdoms_14'`로 지정합니다. 기본 작업 폴더는 `%LOCALAPPDATA%\San14GrandLibrary`입니다. 변경하려면 준비에 `-CacheRoot 'D:\San14Library'`, 조회 세션에 `$env:SAN14_LIBRARY_CACHE='D:\San14Library'`를 사용합니다. [자세한 준비·복구 안내](docs/SETUP.md)

## 무엇을 먼저 읽나요?

이미 설치했다면 [업데이트 확인·갱신 안내](docs/UPDATING.md)를 읽습니다. Git 작업본은 원격 커밋 비교로 새 변경을 감지할 수 있습니다. 자동 설치본은 최초 명령을 다시 실행해 새 공개본을 받으며, 현재 전용 업데이트 감지·알림 기능은 없습니다. 문서 갱신 때문에 원작 캐시를 지우지 않습니다.

| 목적 | 문서 |
|---|---|
| AI의 첫 읽기 순서 | [AGENTS.md](AGENTS.md) |
| 원작 함수·구조체·게임 규칙 | [대도서관 목차](docs/orig/README.md) |
| 기존 조사 검색 | [검색 안내](docs/AI_WORKFLOW.md), [출처 색인](docs/orig/SOURCES.md) |
| 문서 작성·정정 기준 | [대도서관 규칙](docs/LIBRARY_RULES.md) |
| 조사 기여와 검토 | [CONTRIBUTING.md](CONTRIBUTING.md) |
| 모드 간 충돌 방지 | [호환 규약](docs/MOD_COMPATIBILITY.md), [매니페스트 예제](examples/example-mod.json) |
| 로컬 생성물과 공개 범위 | [자료 범위](docs/DISTRIBUTION.md), [출처·라이선스](LICENSE.md) |
| 이번 도구의 실제 검증 | [검증 기록](docs/VALIDATION.md) |

호환 규약을 따르면 원작의 호출 흐름을 바탕으로 **각 모드가 바꾸는 입력·출력·상태와 체인 순서를 명시해 함께 검토**하기 쉬워집니다. [호출·입출력 변경 계약 템플릿](examples/HOOK_CONTRACT.md)을 자기 모드에 작성해 주세요. 모든 모드의 변경 범위를 자동으로 알아내거나 자동 체이닝하는 기능은 아니며, 정적 충돌 검사와 조합별 실게임 확인을 구분합니다.

## 함께 지식을 보완하는 방법

기존 문서 → 자기 로컬 캐시 순서로 근거를 찾고 문서를 수정해 PR을 보내 주세요. 게임 빌드, RVA 또는 데이터 위치, 확인 방법, 확신도, 미확인 부분을 적습니다. 유지관리자가 검토한 PR을 병합합니다. 자동 검사는 링크·자료 범위·형식·도구 회귀를 검사하며 **원작 해석의 정확성을 보증하지 않습니다**.

처음 기여한다면 [AI에게 맡기는 기여·PR 절차](CONTRIBUTING.md#처음-기여하는-사람-커밋-요청은-pr입니다)를 읽어 주세요. AI가 모드 개발 중 새 원작 사실이나 오류를 발견하면 수정안을 준비하고 공유 의사를 한 번 확인한 뒤, 승인된 범위의 fork·커밋·PR 제출과 검토 반영까지 처리하도록 [AGENTS.md](AGENTS.md)에 지시했습니다.

함수 이름과 디컴파일 결과는 가설입니다. 실제 훅·원작 함수 호출에는 바이트·호출자·ABI·스레드 검증이 추가로 필요합니다. 캐시에는 디컴파일 실패 함수가 있을 수 있으며 준비 결과에 실패 수가 표시됩니다. 실패 함수는 의사코드가 있다고 간주하지 않습니다.

초기 원작 조사 기준은 Steam buildid **25953386**, 분석 EXE SHA256 **`1a4a447d14e68c40ad2a5107c29c7341c10eee8fc297a7b35032900c341dbcaa`**입니다. 지원하지 않는 EXE에는 분석을 시작하지 않고 빌드와 해시를 보고합니다. 다른 게임판·패치의 주소를 그대로 적용하지 않습니다.
