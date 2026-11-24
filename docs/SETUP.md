# 자동 준비와 복구

## 자동으로 하는 일

`bootstrap.ps1`은 Git 없이 저장소 소스를 내려받고 `prepare.ps1`을 실행한다. `prepare.ps1`은 고정한 embedded Python을 검증해 실행한다. Python 프로그램이 Steam registry → `libraryfolders.vdf` → appmanifest 872410 순서로 설치 경로를 찾고 지원 EXE 해시를 확인한다. 여러 설치본이 있으면 임의 선택하지 않고 경로 지정을 요청한다.

Python 프로그램은 고정 Java JDK, Ghidra, Steamless ZIP을 공식 출처에서 내려받아 SHA256을 확인한다. 이미 설치한 도구의 파일 목록과 해시가 일치하면 재사용한다. 관리자 설치·PATH·레지스트리·시스템 Python·Steam 파일은 바꾸지 않는다. Windows 10/11에 포함된 .NET Framework 4.7.2 이상을 확인한다. 없다면 Windows Update 완료가 필요하며, 시스템 구성요소 설치를 몰래 수행하지 않는다.

원작 EXE는 `%LOCALAPPDATA%/San14GrandLibrary/builds/<분석해시16>/input/game.exe`에 복사한다. Steamless 옵션은 `--keepbind --keepstub --recalcchecksum`으로 고정한다. 현재 기준 빌드에서 이 조합이 기존 대도서관 분석 EXE와 **전체 SHA256까지 일치**하는 것을 확인했다. 설치본 EXE는 읽기만 하며 언패킹 전후 해시를 확인한다. 해제본을 게임 폴더로 옮기거나 실행하지 않는다.

최초 Ghidra 분석은 영구 프로젝트에 저장한다. 그 다음 읽기 전용·`-noanalysis`로 함수를 샤드별 추출한다. 함수 표, 호출관계, 데이터 참조, 문자열, 심볼, vtable 후보, import, 실패 목록을 만든다. SQLite에는 메타데이터와 함수 본문 위치만 저장한다. 준비 도구·의존성·빌드·스크립트가 같고 캐시가 유효하면 재분석하지 않는다.

## 시간과 공간

의존성 다운로드는 약 800 MB다. 압축 해제·영구 DB·분석 캐시를 위해 여유 공간 8 GiB 이상을 요구한다. 실제 검증 환경에서는 최초 분석 약 22분, 전체 함수 추출 약 44분으로 최초 준비에 1시간 이상 걸렸다. 저장장치·CPU·네트워크에 따라 달라진다. 메모리 heap 기본값은 4 GiB, CPU는 최대 4개다. 게임 실행 중 관찰을 필요로 하지 않는다.

## 명령

```powershell
# 진단: 설치 경로, 빌드, 해시, 여유 공간. 전체 분석 없음.
.\prepare.ps1 -Doctor
# 기본 준비. 실패한 뒤에도 같은 명령을 재실행한다.
.\prepare.ps1
# 준비 결과 검증만. 다운로드/분석 없음.
.\prepare.ps1 -VerifyOnly
# 비표준 Steam 설치 위치
.\prepare.ps1 -GamePath 'D:\SteamLibrary\steamapps\common\Romance_of_the_Three_Kingdoms_14'
# 별도 캐시 위치 (게임 설치 폴더와 checkout 안에는 둘 수 없다)
.\prepare.ps1 -CacheRoot 'D:\San14Library'
$env:SAN14_LIBRARY_CACHE = 'D:\San14Library'
.\library.ps1 status
```

같은 캐시에 대한 준비 작업은 OS 파일 잠금으로 하나만 실행한다. 중단 후 잠금은 OS가 해제하므로 `.lock` 파일을 수동 삭제할 필요가 없다. 중단된 최초 분석은 기존 프로젝트를 다시 처리한다. 분석 완료 보고서가 없으면 분석을 완료로 간주하지 않는다. 추출은 완료된 샤드를 건너뛰고 중단된 샤드부터 다시 만든다.

캐시 검증 실패를 강제로 무시하지 않는다. 도구 파일이 변조되었거나 산출물이 훼손되면 기존 폴더를 보존한 채 새 `-CacheRoot`에서 준비한다. 새 게임 패치가 나오면 기존 캐시를 새 해시에 연결하지 않는다. appmanifest buildid와 EXE 해시를 Issue에 보고하고 새 프로필의 검증을 기다린다.

## 고급: 이미 있는 로컬 추출본 재사용

`prepare.ps1 -ReuseExport '<로컬 추출 폴더>'`는 동일한 전체 EXE SHA256의 완료 manifest를 가진 **자기 PC의** 기존 추출본을 새 캐시에 가져온다. 기본 사용자 흐름에서는 쓰지 않는다. 이 경우도 Steam 설치본에서 언패킹해 동일 해시를 확인하고 새 검색 색인과 표본 검증을 수행한다. `ready.json`의 `reused_export`로 새 분석과 구분한다. 생성된 원작 캐시를 온라인에서 다운로드하거나 배포하는 기능은 없다.

## 잘 알려진 환경 제한

- Windows x64만 자동 준비를 지원한다. Linux/macOS에서 원작 문서와 순수 Python 검사 도구를 읽을 수는 있다.
- Ghidra의 Windows batch launcher 제약 때문에 캐시 경로에 `()!%&^`가 있으면 다른 경로를 지정해야 한다. 게임 설치 경로의 괄호는 사본을 staging하므로 문제가 없다.
- 방화벽·사내 프록시가 공식 다운로드를 차단하거나 Windows 시스템 구성요소 설치가 필요한 경우에는 원인이 출력된다. 완료했다고 보고하지 않는다.
- 사용자가 Steam 게임과 필요한 콘텐츠를 설치해야 한다. 준비 도구는 게임 구매·DLC 가용성을 대신하지 않는다.
