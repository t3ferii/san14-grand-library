# 빌드 간 주소 변환 요약 (BUILD ADDRESSES)

> **이 문서에서 찾는 법**: 1 빌드 신원 · 2 규모·구간 델타 · 3 변환 방법(도구·절차) · 4 불변/변경 판정 요약 · 5 공식이 바뀐 함수 · 6 데이터·전역 주소 · 7 구조체 오프셋 불변 근거 · 8 모드 훅 지점 · 9 충돌 · 10 정정 기록 · 11 미해결 · 12 출처.
> **새 확정 사실은 이 문서의 해당 절에 추가한다.** 기계가 읽는 변환은 `functions.json`의 `old`/`new` 필드와 `AI_TacticsMod/research/rva_map/1fbe6be7_to_1a4a447d/functions.tsv`.

작성 2026-11-07 (M1). 현재 기준판은 SESSION_RULES.md §7: **Steam buildid 25953386, `1a4a447d…`**. 옛 `1fbe6be7…` 이전 분석 자료·주소는 변환 후 사용.

## 1. 빌드 신원

| 항목 | 현재 기준(새) | 옛 |
|---|---|---|
| 해제본 SHA-256 | `1a4a447d14e68c40ad2a5107c29c7341c10eee8fc297a7b35032900c341dbcaa` | `1fbe6be7466a66466fe97cf3ab7d49392913346879c7d40de7f4eaf86eef81c6` |
| TimeDateStamp | 0x6AD06F53 (1792044883) | 0x6A983C25 (1788361765) |
| 이미지 크기 | 44,048,384 (0x2A02000) | 44,036,096 (0x29FF000) |
| 원본(디스크, Steam 암호화) | — | `87ed4e46590e…2d6a` (REA 옛 문서의 '원본 EXE') |
| 비고 | Steam buildid 25953386(2026-11-05). 사용자 지시: 이 빌드만 유효 | Editor83 Steamless 해제본. 분석 문서(pre6·r4·r5·mechanisms 등)의 RVA 체계 |

원작 EXE는 REA로 열지 않는다(SESSION_RULES §7). 원작 함수 조회는 `ghidra_full.py`(새 빌드, `--build 1fbe6be7`로 옛 빌드)·영구 DB `ghidra_persistent.ps1 -Action Export`.

## 2. 규모·구간 델타

- 함수 단위(.pdata 75,189 + leaf 25,190 = 옛 100,379 / 새 100,406): **same 97,839 / changed 1,610 / unmatched 930**, 새 빌드 전용 1,012. same은 `명령어열(rel32·RIP·점프테이블 칸 마스킹) 동일`이다 — **본문은 같고 주소만 이동**.
- 델타가 다른 구간 1,727종(+0xFE0 ~ +0x2900대). **.text 앞쪽(0x21DAF 이전)은 불변, 그 뒤는 구간마다 다르다. 모든 모드 RVA는 한 번 이상 움직였다고 본다.**
- vtable 후보(연속 코드 포인터 3개 이상) 6,583개: 슬롯 전부 대응 5,076 / 일부 1,506 / 못 찾음 1.
- 데이터(.rdata/.data 16바이트 행 정렬): .rdata 동일 3.66MB·다름 2.55MB·미대응 0.99MB, .data 동일 0.91MB·다름 0.20MB·미대응 0.18MB. 델타는 +0x3000 고정이 아니라 .rdata 대부분 +0x3020, .data +0x3010/+0x3050 등.

### 2.1 함수 델타 앵커 (옛 RVA 구간 → 새 − 옛)

델타는 구간마다 계속 바뀐다(함수 델타 1,727종). 아래는 규모·방향 확인용이며 **환산에는 쓰지 말고 반드시 functions.tsv/rva_remap.py로 확정**한다.

| 옛 RVA 구간 시작 | 가장 가까운 함수 옛→새 | 델타(새−옛) |
|---|---|---|
| 0x0 | 1000→1000 | +0x0 |
| 0x100000 | 100010→100FF0 | +0xFE0 |
| 0x200000 | 200500→2018E0 | +0x13E0 |
| 0x300000 | 300C30→303020 | +0x23F0 |
| 0x400000 | 4000B0→4023E0 | +0x2330 |
| 0x500000 | 5001B0→502A10 | +0x2860 |
| 0x600000 | 600000→602830 | +0x2830 |
| 0x700000 | 700790→702AA0 | +0x2310 |
| 0x800000 | 800030→8024C0 | +0x2490 |
| 0x900000 | 9001A0→902640 | +0x24A0 |
| 0xA00000 | A00050→A02830 | +0x27E0 |
| 0xB00000 | B00190→B02FC0 | +0x2E30 |
| 0xC00000 | C00000→C02780 | +0x2780 |
| 0xD00000 | D000C0→D02000 | +0x1F40 |
| 0xE00000 | E00130→E02760 | +0x2630 |
| 0xF00000 | F00791→F02C01 | +0x2470 |
| 0x1000000 | 1000094→10029A4 | +0x2910 |
| 0x1100000 | 11002B0→11027E0 | +0x2530 |
| 0x1200000 | 12004B0→1202C80 | +0x27D0 |
| 0x1300000 | 1300000→13027D0 | +0x27D0 |

### 2.2 연속 구간(같은 델타가 800함수 이상 이어지는 구간)

| 옛 시작 | 옛 끝 | 델타 | 함수 수 |
|---|---|---|---|
| D52F0 | 130830 | +0xFE0 | 1975 |
| 14E660 | 153900 | +0xFE0 | 872 |
| 11ADBC0 | 11D4A30 | +0x2780 | 960 |
| 12FDDE0 | 13020F6 | +0x27D0 | 1055 |
| 1335AE0 | 133F94C | +0x2780 | 1729 |

### 2.3 데이터 구간 델타 (data.tsv, 구간 바이트 합)

| 섹션 | 델타 | 상태 | 바이트 |
|---|---|---|---|
| .rdata | +3020 | eq | 2,106,592 |
| .rdata | +0 | unmatched | 994,400 |
| .rdata | +3100 | diff | 561,712 |
| .data | +3050 | eq | 474,016 |
| .rdata | +3090 | eq | 439,456 |
| .rdata | +3080 | diff | 335,264 |
| .rdata | +30A0 | eq | 306,592 |
| .data | +3010 | eq | 298,624 |
| .rdata | +3090 | diff | 237,648 |
| .data | +0 | unmatched | 175,312 |
| .rdata | +3020 | diff | 158,928 |
| .rdata | +2FA0 | eq | 134,816 |

## 3. 변환 방법

1. **함수 시작 주소**: `functions.tsv`(열: old, new, size_old, size_new, status, evidence, kind) — 옛 RVA 정렬. 함수 안 중간 주소는 같은 크기이면 같은 오프셋이 유지된다(`same-asm(mid)`). 이 폴더의 `functions.json` 키가 새 RVA, `old` 필드가 옛 RVA.
2. **도구**: `python -X utf8 AI_TacticsMod/tools/rva_remap.py map <RVA>`(함수·내부 주소·vtable 슬롯·데이터), `rva_remap.py all`(대응표 재생성 약 2분), `San14Library/archive/tools/build_remap.py`(문서가 인용한 RVA 전수 대응·렌더), `tools/pe_const.py`(양쪽 PE 상수).
3. **판정 순서**: 수동 판정(`b_verdicts.json`, BUILD_25953386_REMAP §5.1)이 자동 대응보다 우선. 예: `BF7A40→1137FF0`은 자동 대응이 틀렸고 수동 판정으로 고정(5바이트 getter, 쌍둥이 `BFA210` 아님).
4. **모드 DLL의 주소 관리**: 중앙 주소표 도입이 REMAP §4의 권고이고, 현재는 `tools/gen_signatures.py`가 `b_verdicts.json`을 읽어 빌드별 RVA·바이트 가드(§5.4)를 낸다. 모르는 빌드에서는 probe 불일치로 해당 기능만 꺼진다(PATCH_RESILIENCE.md).

## 4. 불변/변경 판정 요약 (규칙 함수 인용분 build_remap.md §2)

- 규칙 공식 함수 중 **본문 불변** 다수(명령어열·상수 동일). 단 **호출 사슬 변경** 표시가 붙은 것은 하위 호출이 바뀐 것: 대표 4종 ① `22FCE0→231770` 능력 getter에 bit14/item 7B 검사 추가(무해) ② `2B07C0→2B2A90` 인접 모드 게이트 ③ `2B21A0/2B2440/2A9E50/2AA2E0/2B0290` 정책 효과 0x30 지형 항(현 표 e=0이라 휴면) ④ `185B30→186E60` 소유 변경에 알림 호출 +1(이벤트만).
- 상수: 규칙 함수·호출 사슬에서 값이 바뀐 **.data 상수는 `266C50`(새 268600)의 3개(300→360)뿐**. 인용 .data/.rdata 상수 173개는 짝지은 새 주소에서 같은 값.
- `same` 641 / `data_pair` 166 / `not_rva` 33 / `changed_aligned` 28 / `manual:same-asm` 16 / `manual:same-hook` 13 / `data_eq` 12 / `same-asm(mid)` 11 / `data_ref` 11 / `changed_unaligned` 7 / `data_diff` 4 / `unmatched` 1 / `data_assumed` 1 (build_remap.json 944 항목 집계).

## 5. 공식·동작이 바뀐 함수 (build_remap.md §2에서 '변경' 판정)

| 옛 | 새 | 내용(요약) |
|---|---|---|
| `22FCE0` | `231770` | ability getter (callee of most formulas): person word +0x15E bit 14 now gates the item-0x7B "stat = 100" override (ability index 4); the inline "difficulty / computer-force" test became the helper 407E0 (+0xE6 != 1, 234AB0 == 0, bit 14 == 0, byte +0x1BC) = same logic. |
| `266C50` | `268600` | domestic development (commerce/agriculture/barracks): instruction-identical, but the three multipliers DAT_141a49f78/6C/84 (old) -> DAT_141a4cfe0/D4/EC (new) changed 300 -> 360 (x1.2 growth). `22FCE0`->`231770`: ability getter bit-14/item 7B (see 22FCE0) |
| `2695D0` | `26AF80` | supply consumption: the old subtracted term int(policy effect 0x40 x base/100) for unit classes 11..13 on terrain 14/24 is gone; the rest (base 40/30/10, tile reduction +0x19, effect 0xB/0x14 terms, 0x43 foreign-territory term, 3EA400 expert term) is the same. |
| `29EDE0` | `2A0CF0` | unit enters a site: the type-2 follow-up block (second capacity clamp + experience award) now only runs when officer word +0xE2 != army word +0x4E; the troop/wounded clamps are instruction-identical. Condition meaning unknown. |
| `2A9E50` | `2AC0A0` | defender B: same NEW (100 + e)/100 term after "+ 1.0 / durability" and before the flank factor (param_5 != 0); constants identical; inert. |
| `2AA2E0` | `2AC5A0` | pasung (army siege power): same NEW term after max(1, ...) (no param_5 test); constants identical (100.0 kept in a register instead of reloaded); inert. |
| `2B0290` | `2B2550` | move cost: same NEW (100 + e)/100 term (e = effect 0x30, terrain byte +0x42 in {2,4}); the 0x3B/0x3C force-effect block is unchanged (its "(flags>>1)&1" test became the helper 711B0(unit,1)); constants identical. |
| `2B07C0` | `2B2A90` | adjacent-region effect: the computer-force override (difficulty 3 -> 16, 4 -> 24 percent) no longer tests 3EB2A0 (standard-mode flag), so it also applies in expert mode; for the standard mode the values are identical (4 / 16 / 24, constants re-read). Prologue push r15 -> r14. |
| `2B21A0` | `2B4460` | unit attacker A: NEW last factor (100 + e)/100, e = policy effect 0x30 (22DB30) of the force, only if e > 0 and terrain byte +0x42 of the tile object in {2,4} and param_5 != 0 (unit participants only); constants identical. e = 0 in every table -> inert. |
| `2B2440` | `2B4750` | siege attack input of a unit: same NEW (100 + e)/100 term as 2B4460; constants identical; inert. |

규칙 영향 요약: 새 빌드 규칙 변경 = ①지역 개발 증가 300→360(`268600`) ②정책 효과 0x30 지형 항 4함수(휴면) ③부대 군량 `26AF80`에서 효과 0x40 감소 항 삭제 ④인접효과 `2B2A90` 숙련 모드 적용 범위 확대 ⑤`2A0CF0`(옛 29EDE0) 입성 후속 블록 조건 변경. 그 외 규칙은 본문 불변(build_remap.md §2).

## 6. 데이터·전역 주소 (새 / 옛)

| 이름 | 새 | 옛 | 뜻 | 출처 |
|---|---|---|---|---|
| 세계 루트 포인터 | image+0x2780F60 | image+0x277DF18 | world 객체. 필드 오프셋 22종은 두 빌드에서 동일 | build_remap.md §1 |
| 설정 객체 | RVA 0x1A49C90 (+0x8 = 0x1A49C98) | RVA 0x1A46CA0 (+0x8 = 0x1A46CA8) | 0xF00B. 난이도·모드·60 설정 | worldmap_spec_b.md §6.2; BUILD_25953386_COMBAT.md §1 |
| 게임 모드 플래그(E58) | 0x1A4AAE8 | 0x1A47AF8 | 설정 +0xE58(1 표준/0 숙련), data_eq | BUILD_25953386_COMBAT.md §1 |
| ai_max_aggression 슬롯 | 0x1B98D10 | 0x1B95CC0 | C36A0(옛 C2610) 포인터. 싱글톤 접근자 205F0(옛 20610) | BUILD_25953386_REMAP.md §5.1 |
| 싱글톤 전역 | 0x214624C | 0x21431FC | 접근자 1A47C0(옛 1A34C0) | BUILD_25953386_REMAP.md §5.1 |
| 날짜 상태기계 참조 전역 | 0x1A4AC10 | 0x1A47C20 | 44DEE0(옛 44BCA0) 참조 8곳 일치 | BUILD_25953386_REMAP.md §5.1 |
| traits9 데이터 | 0x1A33810 / 0x1A4AB88 | 0x1A30830 / 0x1A47B98 | traits9 코어 5곳(local10 G3) | BUILD_25953386_REMAP.md §5.1 |
| ZOC 상수 300 / 5 / 5 | 141A4BC78 / 141A4BC84 / 141A4BC98 (+런타임 1427D55F8=5) | 141A48C2C / 141A48C38 / 141A48C4C | 2B7BC0 항: 인접 적 300, 반경 2~3·적대 칸 5 | worldmap_spec.md §4.3; dump_measurements.md:180 |
| 단절 사기 가산 9 | 141A4C044 | (옛 값 미기재) | 268070 단절 +9 | worldmap_spec.md §2.3 |
| 순 카운터 문턱 36 / 월 3 | 141A4C748 / 141A4C784 | (옛 미기재) | 충성 분기 하락 29F380 | command_audit.md §3a |
| 불 감쇠 상수 | 141A4C070 | (옛 미기재) | 타일 화염 감쇠(틱당 -1 계열) | command_audit.md §15 |
| 난이도 표(지역 월 금 수입 배율 등) | 141A47D60/6C/78/84 (플), 141A47DF0/DFC (컴) 등 | (옛과 동일 표기. difficulty.md는 새 주소로 기재) | difficulty.md 3절에 항목별 전수 | difficulty.md §3 |
| 인접효과 기본/컴 값 | 141A4A6B8 / 141A47D00(특급 16) / 141A47D24(궁극 24) | (미기재) | 2B2A90 항 | difficulty.md 항 35 |
| 전법 대기 가중 상수 | 141A48A78/84/90 | (미기재) | 173DD0 AI 선택 가중치 | worldmap_spec_b.md §5.1 |
| 행동트리 단계/조건 표 | 141A64050 / 141A642D0 | (미기재) | 42FDC0 월 이벤트 단계(0..0x4E) | command_audit.md §2 |
| 주(州) 표 / 지방 이점 표 | world+0xDC80[23] / world+0x85990[18] | (옛 미기재) | 도시 +0xCE -> 주, 주 +0x30(geo) -> 이점 객체(+0x95 = 기준 도시 수) | L3 5차: A5B10·935F0·92AE0·93480 |
| 탐색 발견 상수 | 141A4BF74=3 / 141A4BF80=30 (재야), 141A4B618=2 / 141A4B624=200 (명승), 141A4BF50=60 / BF5C=10 / BF68=5 / BF8C=90 / BF98=1 / BFA4=5 / BFB0=5 / BFBC=5 (명품·전법서), 141A4BFD4=1 (개성 0x3F 배율) | (옛 미기재) | EXE 정적 초기값(실행 중 설정이 덮어쓰는지는 미확인) | L3 5차: 282230·2826B0·281480 |
| 등용 점수 상수 | 141A4CB9C=10 / 141A4CBA8=5 / 1427D567C(런타임) (플레이어 가산), 141A4BC30=1, 1413A3958=1.5f / 1413B193C=1.3f / 141345B9C=1.1f / 141345B98=1.0f (의리 배율) | (옛 미기재) | 279DE0 | L3 5차 |
| 명승 단계 문턱 | 1413A9DDC = {100, 300, 600, 1000} | (옛 미기재) | 22C5F0 개발 3종 단계화 | L3 5차 |
| 개성 객체 표 | world+0x7DD18[356](232B) = 개성 객체, 개성 번호 68~76 = 지형 특기 | 옛 문서와 같은 오프셋 | 조건 113·114·117·128 | L3 5차 |

(상수·표 주소는 `141A4…`처럼 이미지 가상주소(0x140000000+RVA)로 적힌 문서가 많다. 같은 문서에 옛/새 상수가 섞이면 `data.tsv`로 대조.)

## 7. 구조체 오프셋은 변하지 않았다 (근거)

world 구조체(`image+0x277DF18`→`image+0x2780F60`)의 필드 오프셋 22종은 두 빌드 C 추출본 전체 스캔에서 사용 횟수와 값이 같다(build_remap.md §1). army/troops/pair/record 필드와 표 `0x7E838/0x73860/0x73958`, 기술 `0x85F20`은 사용 함수 asm 대조로 변경 없음(BUILD_25953386_COMBAT.md §1). 결론: **structs.md의 오프셋은 빌드 간 공통, RVA만 변환한다.**

## 8. 모드 훅 지점 → 모드 문서

모드 훅 지점의 옛→새 빌드 판정표는 원작 사실이 아니어서 `AI_TacticsMod/docs/MOD_CHANGES_VS_ORIGINAL.md` 2절로 옮겼다(2026-11-15).

**새 원본 전용 변화**: `27D490`(공격 부대 구성원을 적 요새 공격 action 6/kind 11로 재배정), `2A3E30` — 옛 빌드엔 없음(BC §3 충돌 2).

## 9. 충돌

| # | 내용 | 출처 |
|---|---|---|
| B1 | worldmap_spec.md §3.2가 해방 조건 합계를 `41E7B0`(옛 `41C200`)으로 적음 vs build_remap.json은 `41C200→41E570`. 실제로는 두 함수가 별개(41E7B0=옛 41C440, 호출자 2C6D40 확인). 문서의 '옛 41C200'만 오기 | worldmap_spec.md §3.2; build_remap.json |
| B2 | worldmap_spec.md §1.1 `22CC00/22E260` 쌍: 옛 22CC00의 새 번호는 22E650, 22E260은 옛 22C810의 새 번호 — 새/옛 쌍이 아님 | worldmap_spec.md §1.1; functions.tsv |
| B3 | 설정 객체: BUILD_25953386_COMBAT는 `3E9C90 +0x8=1A46CA8→1A49C98`, worldmap_spec_b는 `0x1A49C90(옛 0x1A46CA0)` — 객체 시작 vs +0x8 필드(8바이트 차)로 같은 객체 | BUILD_25953386_COMBAT.md; worldmap_spec_b.md §6.2 |
| B4 | `2D95F0`(옛)/`2DB9A0`(새)처럼 한 문서가 새 번호로 쓰던 것을 다른 문서가 옛 번호로 쓰는 혼용(lane_L4.md:15의 `43E030`은 옛, :84의 `44DD30`은 새) | lane_L4.md; functions.tsv 검증 |

## 10. 정정 기록

| 대상 | 옛 판정/서술 | 정정본 | 출처 |
|---|---|---|---|
| 자동 대응 `BF7A40` | remap이 쌍둥이 `BFA210`(+0x58)을 골라 짝이 틀림 | 수동 판정: 5바이트 getter `return [rcx+0x18]`, `BF7A40→1137FF0`(35A40→365A0 호출 자리 확인) | BUILD_25953386_REMAP.md §5.1 |
| 2A9E50·2AA2E0·2B21A0·2B2440 끔 유지 | `param_5!=0`일 때 상태를 건드리는 블록이라 피해 예측 끔 | 틀렸다: 그 블록은 store 없는 순수 보정항 → local10 G4에서 켜짐(damage_preview) | BUILD_25953386_REMAP.md §5.2 정정 |
| `2B02A0`·`1F9DE0/1FA607` 끔 유지 | path_fast는 비용식 재현이라 끔; 건설 완료 본문 재구성 불확실 | path_fast는 비용 함수를 호출만 함 → 켜짐(G2). building_destruction_all도 same-hook으로 켜짐 | BUILD_25953386_REMAP.md §5.1~5.2 |
| 새 빌드 모듈 켜짐 서술(A단계) | tooltip_collab·battle_deaths·scenery_skip·traits9가 다시 켜진다 | 틀렸다(local2 실게임 실패 후 정정). 통합패치에서 가져온 TraitHover·BattleDeaths 기계어는 옛 EXE TimeDateStamp/SizeOfImage만 받아 새 빌드에서 0을 돌려줌 → local10 G3·G5로 재배치 후 켜짐 | BUILD_25953386_REMAP.md §5.3 |
| 설치본 동작 판정(§3) | 옛 RVA DLL이 새 EXE를 만나면 시작 단계에서 전부 꺼짐(probe 0/12) | A단계 시점 판정. 이후 중앙 주소표·재배치로 대부분 켜짐(최종 꺼짐: ccz_sprites뿐, 검사기 한계) | BUILD_25953386_REMAP.md §3, §5.3 |
| `2E111D`(옛 2E110C 근방) captive_either_force | 새 원작 `2E3441`이 `r15` 후 `r14`를 판정(모드와 같은 동작) | 기능과 옛 빌드 지원을 모드에서 삭제(사용자 결정 2026-11-06) | BUILD_25953386_REMAP.md §5.2 |

## 11. 미해결

- U1 unmatched 함수 930개(옛) 중 모드가 쓰는 것은 `1F8E90` 1건뿐(문서에만 있음; build_remap.md §1). 나머지는 미조사.
- U2 vtable 슬롯 부분 대응 1,506개 — 훅이 vtable 슬롯을 쓰는 경우만 b_verdicts.json로 확정.
- U3 데이터 unmatched 약 1.2MB와 `data_assumed`/`data_diff`(근사값). 상수 주소를 새로 쓸 때는 PE에서 값을 다시 읽는다(pe_const.py).
- U4 모든 판정은 정적 분석(실게임 확인 아님). 일부 훅(옛 EXE 해시 87ed4e를 확인하는 verify_*.py)은 새 빌드와 맞지 않아 별도 정리 대상(REMAP §5.6).
- U5 함수 경계 오류: `ghidra_full.py`의 시작이 틀린 곳(170D80/173DD0/174F40/1798B0)은 중간 지점이므로 이 표에서 함수 시작으로 쓰지 말 것.

## 12. 출처

- 기준·방법: San14Library/archive/fidelity/build_remap.md(.json) · AI_TacticsMod/docs/BUILD_25953386_REMAP.md · BUILD_25953386_COMBAT.md · SESSION_RULES.md §7 · GHIDRA_PERSISTENT.md · AI_TacticsMod/research/rva_map/1fbe6be7_to_1a4a447d/{functions.tsv,data.tsv,addr_table.json,summary.json,b_verdicts.json,impact_summary.json}.
- 오래된 서술(변환 필요): AI_TacticsMod/docs/NATIVE_FUNCTIONS.md(444 RVA 중 옛 시작 318, changed 35), REA_Analysis/*, pre6_*·combat6·r4/r5·calendar. 상태 판정은 functions.md §8 / structs.md §9.
