# origlib - 원본 삼국지14 데이터 읽기 라이브러리

하위 에이전트는 원본 파일(0000, 0001_KO, 0004, 0010_KO, DLC)을 직접 파싱하지 말고 이 라이브러리로 읽는다.
범위: 한국어(KO)와 언어 무관 폴더만. 형식·필드 근거는 `docs/orig/data_formats_game.md`(자동 생성), 아카이브(0002·0005)는 `docs/orig/data_formats_archives.md`.
실행 위치: `San14Sim/` (또는 sys.path 에 San14Sim 추가). Python 3.12+, 표준 라이브러리만. 한 번 로드에 0.1~0.3초.

## API

```python
import origlib
fx = origlib.load_fixdata()            # {'trait': [dict...], 'tactic': ..., 'city': ...}  (키 목록: python -m origlib tables)
fx['trait'][5]['effect1']              # 필드는 영어 식별자, 각 레코드에 _id, _raw(원본 바이트)
s = origlib.load_scenario(3)           # Scenario: .name .year .month .chain  .table('city'|'general'|'force'|'region'...)
origlib.load_scenario(3, 'general')    # == s.table('general');  s.generals() = 비어있지 않은 무장 슬롯
origlib.scenario_ids()                 # CE 시나리오 50개 번호
origlib.msg(40044, 'msggame')          # 메시지 id = 구간*10000+번호 ; 기본 표 msggame_exce
origlib.msg(10000 + 0x5FA, 'msgdata_exce')  # 관문정보(원작 UI 키 0x5FA)
origlib.find_text('조조')               # [(표, id, 문장)] (msgdata*/msggame* 전체)
origlib.load_map().cell(i)             # 220x220 지도 칸 (terrain, area ...)
origlib.events('EventTutorial')        # EventFile: .events(), .event(i).conditions/.actions, .speech(ev)
origlib.load_bt()                      # bt_exce.bin 행동 트리 (.tree(i) -> (hash, [Node]))
origlib.dlc.load_dlc_scenario('scedaexce32.s14')   # XOR 풀린 Container (header/body)
origlib.rdb.open(name), origlib.bin0005.open(n)    # K4 아카이브 모듈 (rdb.open 은 내장 open 을 가리므로 import * 금지)
origlib.bin0005.portrait_location(6100, 10)        # (1, 15): 001.bin의 작은 초상화
origlib.bin0005.portrait_identity(1, 15)          # (6100, 10)
```

## CLI
`python -X utf8 -m origlib tables | table <키|한글이름> [N] | unresolved <키> | scenarios | scenario <id> [블록 [N]] | msg <id> [표] | find <문자열> | events [파일 [번호]] | map [칸] | misc | bt | dlc | rdb <이름> | layout [논리 이름] | bin0005 <n>`

`layout cmn_footer_re_cn`은 이름 해시, 래퍼 ID, 설정 객체 ID, 최종 ScreenLayout KTID를 순서대로 출력한다. `layout`은 설치본의 등록표 전체를 출력한다. Python에서는 `from origlib import rdb` 후 `rdb.read_layout_registry()[rdb.layout_name_hash('cmn_footer_re_cn')]`로 같은 행을 읽는다.

`portrait_location`의 얼굴 종류 9·10·11은 각각 2048×1024·512×512·1024×1024 그룹이다. 번호 6215~6244는 이 설치본에서 `DLC/0005/003.bin`에 있으며 `origlib.bin0005.open(3, origlib.bin0005.ROOT / 'DLC' / '0005')`처럼 해당 디렉터리를 지정해 읽는다. 이 함수는 게임의 DLC 가용성 검사를 대신하지 않는다.

## 시험
`python -X utf8 tests/test_origlib.py` : 기존 data/tables/*.json·data/scenarios/*.json·data/map.json·worldmap 표와 일치, 표 연쇄 완주, 서명, 메시지 수, 이벤트 대사, DLC 복호 확인 (15개, 약 25초).

## 문서 재생성
`python -X utf8 -m origlib.gen_doc` -> docs/orig/data_formats_game.md (스펙은 fixdata.py / scenario.py / misc0000.py 의 TABLES·SPECS 에 한 곳으로 모여 있다. 필드 의미를 새로 확정하면 그 스펙에 한 줄 추가하고 재생성).

## 알아둘 것
- stride 는 파일에 없어 DFS 로 찾는다(힌트 표 내장). 새 패치로 표가 늘면 `STRIDES_CE` 힌트 없이도 동작한다.
- 지역(scenario 표 6)은 청크 base-2 에서 레코드가 시작한다(스펙의 skew).
- 대용량 산출물은 `origlib_out/` (git 무시).
