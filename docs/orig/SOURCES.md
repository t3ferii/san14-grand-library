# 출처 색인

초기 공개 자료는 2026-11-24 로컬 대도서관에서 이관했다. 파일별 원래 논리 경로, 원본 SHA256, 공개용 변환은 [PROVENANCE.json](../PROVENANCE.json)에 기록한다. 현재 공개 문서의 해시가 원본 해시와 같아야 한다는 뜻은 아니다. 이관 후의 수정과 검토는 Git 이력과 PR에서 관리한다.

## 어디서 찾나요?

- 원작 사실: [분야별 목차](README.md)
- 원작 데이터 읽기: [origlib](../../origlib/README.md)
- 캐시 생성·조회: [SETUP](../SETUP.md), [AI_WORKFLOW](../AI_WORKFLOW.md)
- 공개하지 않은 역사 출처: [ARCHIVE_REFERENCES](../ARCHIVE_REFERENCES.md)
- 모드 간 협력 규약: [MOD_COMPATIBILITY](../MOD_COMPATIBILITY.md)

기존 개인 자료 전체를 색인한 SOURCES.json은 공개 패키지에 그대로 복사하지 않았다. 그 목록에는 비공개·과거 빌드·모드 구현·참고 모드 자료가 섞여 있다. 공개 문서의 근거가 빠졌으면 빠졌다고 취급하고, 기여자가 자신의 대상 빌드에서 재현 가능한 RVA·조회 명령·해석을 보완한다.

원본 연구에서는 원작 EXE를 다시 분석하는 대신 저장된 Ghidra 추출을 읽었다. 이 공개 도구도 최초 준비 이후 같은 캐시를 재사용한다. 단, 최초 분석·함수 추출의 완전성과 개별 해석의 정확성은 별개다.
