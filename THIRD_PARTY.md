# 외부 도구와 출처

이 저장소는 외부 도구 바이너리를 동봉하지 않는다. 사용자의 자동 준비 과정에서 다음 공식 릴리스를 내려받는다. 고정 URL·SHA256은 [의존성 잠금](tools/dependencies.lock.json)에 있다. 각 ZIP 안의 저작권·라이선스 고지를 유지한다.

| 도구 | 출처 | 라이선스·용도 |
|---|---|---|
| CPython embedded 3.12.10 | [Python 공식 릴리스](https://www.python.org/downloads/release/python-31210/) | PSF 및 포함 소프트웨어 조건. 로컬 스크립트 실행 |
| Eclipse Temurin JDK 21.0.13.1+2 | [공식 릴리스](https://github.com/adoptium/temurin21-binaries/releases/tag/jdk-21.0.13.1%2B2) | GPLv2 with Classpath Exception 및 포함 고지. Ghidra 실행 |
| Ghidra 12.1.4 | [NSA 공식 릴리스](https://github.com/NationalSecurityAgency/ghidra/releases/tag/Ghidra_12.1.4_build) | Apache-2.0 및 포함 타사 구성요소 조건. 정적 분석 |
| Steamless 3.1.0.5 | [atom0s 공식 프로젝트](https://github.com/atom0s/Steamless) | CC BY-NC-ND 4.0. 정품 소유 게임의 별도 작업 사본 언패킹. 원본 코드를 가져오거나 수정하지 않고 공식 배포본을 실행 |

초기 연구 문서·origlib 및 Ghidra 내보내기 스크립트는 프로젝트 소유자의 로컬 San14Sim·AI_TacticsMod에서 제공되었다. 세부 출처는 [PROVENANCE.json](docs/PROVENANCE.json)에 있다. 참고 모드 바이너리·타 모더 소스·도구 구현은 이관하지 않았다. 초기 문서의 역사 인용은 해당 자료를 이 저장소 라이선스로 재배포한다는 뜻이 아니다.

삼국지14 및 게임 데이터·코드·이미지·음원 등의 권리는 각 권리자에게 있다. 로컬 캐시를 포함한 원작 자료에는 이 프로젝트의 코드·문서 라이선스를 적용하지 않는다.
