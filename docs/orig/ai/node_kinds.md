# 판단표 노드 종류 전수표 (현재 빌드)

- 노드 종류(kind)는 bt_exce.bin 의 32비트 해시다. 클래스 이름은 실행 파일 RTTI 와 옛 연구(AI_TacticsMod/research/AI_Analysis/all_behaviors/node_catalog.json) 대응이며, 실행 함수 RVA 는 옛 빌드 값을 `AI_TacticsMod/research/rva_map/1fbe6be7_to_1a4a447d/functions.tsv` 로 현재 빌드에 옮겼다.
- 노드 종류 232종. 노드 총수 11495 (세력 246 / 군단 10790 / 군세 348 / 부대 111).
- 구조 노드(UNKNOWN 클래스) 5종은 엔진 공통 노드이며 클래스 이름이 없을 뿐 의미는 알려져 있다(선택/순서/전체검토, 조건, 반복, 작업묶음, 루트). 확신도: 클래스 이름 확정(RTTI), 한국어 설명은 기존 연구 재사용.

| kind | 클래스 | 현재 실행 RVA | 옛 RVA | 대응 | 세력 | 군단 | 군세 | 부대 | 비고 |
|---|---|---|---|---|---|---|---|---|---|
| 0x2252b2cb | UNKNOWN_0x2252b2cb | - | - | - | 42 | 1861 | 79 | 17 | 조건 노드(조건식 평가 B2F0D0(옛)=B319B0 -> 개별 조건 dispatch C2610(옛)=C36A0) |
| 0x416d418c | UNKNOWN_0x416d418c | - | - | - | 27 | 1819 | 59 | 10 | 선택/순서/전체검토 묶음(args[1]=0 선택,1 순서,2 전체검토; 엔진 공통 노드 B2C260/B2C090/B2C180 -> 현재 B2EB30/B2E960/B2EA50) |
| 0xc7f0763d | CVariableCreateNode | 864B0 | 85480 | same | 21 | 754 | 11 | 2 |  |
| 0x78f9c619 | UNKNOWN_0x78f9c619 | - | - | - | 12 | 548 | 15 | 5 | 반복(목록 순회; args: 수집모드, 반복종류, 입력목록, 출력변수) |
| 0xbb9f92d | CVariableGetPersonInfoNode | 8F810 | 8E7C0 | same | 13 | 396 | 0 | 0 |  |
| 0x513bad95 | CVariableGetFootholdInfoNode | 8B190 | 8A160 | changed | 1 | 385 | 4 | 2 |  |
| 0x543eff68 | CListClearNode | 83420 | 82480 | changed | 9 | 325 | 2 | 4 |  |
| 0x8b144fcd | CVariablePlusValueNode | 92270 | 91220 | same | 9 | 230 | 0 | 0 |  |
| 0xd826aec4 | CVariableMultiValueNode | 92130 | 910E0 | same | 4 | 228 | 0 | 1 |  |
| 0x73b8b0c8 | CListGetItemByIndex | 83DE0 | 82E40 | changed | 4 | 215 | 0 | 4 |  |
| 0x32a550f8 | CListSortEvaluationNode | 84CB0 | 83D10 | changed | 4 | 214 | 0 | 2 |  |
| 0xd426860e | CVariableDivideValueNode | 86540 | 85510 | same | 3 | 212 | 0 | 1 |  |
| 0xbd1bada3 | UNKNOWN_0xbd1bada3 | - | - | - | 6 | 174 | 4 | 0 | 작업묶음(변수 범위 단위) |
| 0x70368754 | CVariableGetDistrictInfoNode | 88780 | 87750 | changed | 0 | 173 | 3 | 0 |  |
| 0xc75905a | CVariablePlusVariableNode | 922F0 | 912A0 | same | 1 | 157 | 1 | 1 |  |
| 0xebbf8c69 | CVariableGetForceInfoNode | 8CAE0 | 8BAB0 | changed | 11 | 146 | 0 | 0 |  |
| 0xd8d3b168 | CListAddPersonNode | 825F0 | 81650 | same | 1 | 141 | 0 | 0 |  |
| 0xd67cbd65 | CVariableGetArmyInfoNode | 871D0 | 861A0 | changed | 0 | 98 | 21 | 19 |  |
| 0xecf09fb7 | CVariableGetListLengthNode | 8EF60 | 8DF10 | changed | 3 | 121 | 2 | 4 |  |
| 0xf523ad06 | CGetMyselfDistrictNode | 3DB40 | 3CFE0 | same | 0 | 124 | 0 | 0 |  |
| 0x6d4fb04e | CVariableMinusVariableNode | 92080 | 91030 | same | 4 | 117 | 0 | 0 |  |
| 0x74e23c32 | CMiscSetPersonEvaluationNode | 6EFD0 | 3DF40 | same | 1 | 119 | 0 | 0 |  |
| 0x6ab07e75 | CVariableGetAreaInfoNode | 86720 | 856F0 | changed | 0 | 108 | 6 | 0 |  |
| 0x7b9d3e14 | CGetMyselfDistrictInfoNode | 3C330 | 3B7D0 | changed | 0 | 107 | 3 | 0 |  |
| 0x1c972788 | CVariableSetVariableSpecifiedTypeNode | 92990 | 91940 | same | 2 | 103 | 4 | 0 |  |
| 0x9b97aa1 | CVariableGetTroopsInfoNode | 90110 | 8F0C0 | changed | 0 | 72 | 34 | 0 |  |
| 0xa5bf7be1 | CVariableSetRandomNumberNode | 92870 | 91820 | same | 1 | 98 | 0 | 0 |  |
| 0xecb0696b | CListRemovePersonNode | 84BC0 | 83C20 | same | 0 | 96 | 0 | 0 |  |
| 0x261904c6 | CVariableClearNode | 86480 | 85450 | same | 0 | 78 | 1 | 0 |  |
| 0x9cdb6038 | CGetMyselfForceInfoNode | 56BD0 | 55F50 | changed | 12 | 62 | 0 | 0 |  |
| 0x82ed7fd7 | CVariableMultiVariableNode | 921C0 | 91170 | same | 1 | 67 | 0 | 0 |  |
| 0xab7aea8 | CMiscBreakNode | 850D0 | 84130 | same | 0 | 60 | 5 | 0 |  |
| 0xd3b17b34 | CVariableGetGameDataNode | 8EB70 | 8DB40 | changed | 6 | 58 | 0 | 0 |  |
| 0xc01282ea | CVariableGetCautionTroopsInfoNode | 882E0 | 872B0 | same | 0 | 59 | 2 | 0 |  |
| 0xccbbf66d | CMiscLogNode | 85110 | 84170 | changed | 4 | 56 | 0 | 0 |  |
| 0xc9ec061b | CSpecifiedTroopsSetPurposeNode | 6F070 | 6E190 | changed | 0 | 22 | 23 | 0 |  |
| 0x1da4240a | CSetForceEvaluationNode | 85580 | 57F10 | same | 2 | 37 | 0 | 0 |  |
| 0xcd0ccd48 | CListAddForceNode | 81EB0 | 80F10 | same | 8 | 28 | 0 | 0 |  |
| 0xb5a524e2 | CSpyHomeOfficerRemoveNode | 3EAA0 | 3DFE0 | same | 0 | 36 | 0 | 0 |  |
| 0xc9413e99 | CVariableGetHexInfoNode | 8ED40 | 8DCF0 | same | 0 | 29 | 5 | 1 |  |
| 0xc288df3b | CVariableMinusValueNode | 92000 | 90FB0 | same | 1 | 33 | 0 | 0 |  |
| 0x11813f8 | CListAddAreaUniqueNode | 812A0 | 80300 | same | 0 | 31 | 2 | 0 |  |
| 0x888447d8 | CListAddFootholdUniqueNode | 81D30 | 80D90 | same | 0 | 32 | 0 | 0 |  |
| 0x5947faef | CVariableGetFormationInfoNode | 8EA40 | 8DA10 | changed | 0 | 32 | 0 | 0 |  |
| 0xead69e50 | CListAddFootholdNode | 81BF0 | 80C50 | same | 1 | 30 | 0 | 0 |  |
| 0xb56310ae | CVariableGetBuildingInfoNode | 87FE0 | 86FB0 | same | 0 | 28 | 0 | 1 |  |
| 0x9e22d65a | CMiscSetFootholdEvaluationNode | 6EFD0 | 3DF40 | same | 0 | 29 | 0 | 0 |  |
| 0x9bd46caa | CGetMyselfForceNode | 58B40 | 57EC0 | same | 5 | 23 | 0 | 0 |  |
| 0x8239d75b | CVariableDivideVariableNode | 865D0 | 855A0 | same | 2 | 26 | 0 | 0 |  |
| 0x2e15019b | CVariableGetDistanceNode | 886F0 | 876C0 | same | 0 | 24 | 1 | 1 |  |
| 0x13be7c11 | CMiscDummyNode | 85100 | 84160 | same | 0 | 23 | 3 | 0 |  |
| 0x26623630 | CListAddAreaNode | 81160 | 801C0 | same | 0 | 24 | 0 | 0 |  |
| 0x8b432df4 | CGetForceFriendshipNode | 56AC0 | 55E40 | same | 0 | 24 | 0 | 0 |  |
| 0x8e682f08 | CListAddArmyUniqueNode | 81550 | 805B0 | same | 0 | 23 | 0 | 0 |  |
| 0xaa147130 | CVariableMinVariableNode | 91F40 | 90EF0 | same | 0 | 23 | 0 | 0 |  |
| 0xe1685ef | CVariableMaxValueNode | 91B50 | 90B00 | same | 0 | 21 | 0 | 0 |  |
| 0x184b7500 | CGetFootholdFightingStrengthNode | 7EBA0 | 7DC00 | same | 0 | 19 | 1 | 0 |  |
| 0x5de944ee | CDepartureNode | 35A70 | 34F10 | changed | 0 | 19 | 0 | 0 |  |
| 0xd6821309 | CDepartureTroopsCreateNode | 365A0 | 35A40 | changed | 0 | 19 | 0 | 0 |  |
| 0xcdd3c2e4 | CGetHexAroundFightingStrengthNode | 7EF50 | 7DFB0 | same | 0 | 14 | 1 | 3 |  |
| 0xfb5e2f3c | CSpyHomeOfficerSetNode | 3EBC0 | 3E100 | same | 0 | 18 | 0 | 0 |  |
| 0x6e83418b | CListRemoveForceNode | 84BC0 | 83C20 | same | 0 | 18 | 0 | 0 |  |
| 0x84836d20 | CListAddArmyNode | 81420 | 80480 | same | 0 | 15 | 0 | 2 |  |
| 0x72e99c29 | CCallScriptNode | 5D760 | 5CBF0 | same | 3 | 12 | 0 | 0 |  |
| 0xdfb6775d | CVariableMinValueNode | 91DF0 | 90DA0 | same | 0 | 15 | 0 | 0 |  |
| 0x51f79e63 | CSetFormationEvaluationNode | 6EFD0 | 3DF40 | same | 0 | 14 | 0 | 0 |  |
| 0x3f57c668 | CSelectPersonTacticsNode | 85BE0 | 84BB0 | same | 0 | 14 | 0 | 0 |  |
| 0xbf7b2a0b | CVariableGetMoveCostNode | 8F5A0 | 8E550 | same | 0 | 13 | 0 | 0 |  |
| 0xf45930db | CCommandExecutionExchangeNode | 53530 | 528C0 | same | 0 | 12 | 0 | 0 |  |
| 0xabe1bb51 | CVariableGetSceneryInfoNode | 8FFA0 | 8EF50 | same | 0 | 12 | 0 | 0 |  |
| 0xba6009da | CCommandExecutionBuildingDestructionNode | 52EC0 | 52250 | same | 0 | 12 | 0 | 0 |  |
| 0x37e75ba6 | CVariableGetCautionArmyInfoNode | 88140 | 87110 | same | 0 | 11 | 0 | 0 |  |
| 0xad7b8bf8 | CListAddHexNode | 82170 | 811D0 | same | 0 | 9 | 0 | 2 |  |
| 0x7928c3ba | CMiscSetAreaEvaluationNode | 85580 | 57F10 | same | 0 | 10 | 0 | 0 |  |
| 0x5fadace2 | CVariableGetForceFriendshipNode | 8CA00 | 8B9D0 | same | 0 | 10 | 0 | 0 |  |
| 0xfa3891bf | CListAddUniqueCautionTroopsNode | 831A0 | 82200 | same | 0 | 9 | 0 | 0 |  |
| 0xd4b115ce | CSetCautionTroopsEvaluationNode | 6EFD0 | 3DF40 | same | 0 | 9 | 0 | 0 |  |
| 0x9c3384c2 | CCommandAreaOccupyDepatureNode | 29BA0 | 295B0 | same | 0 | 9 | 0 | 0 |  |
| 0xad9a15d | CGetDelegationTargetNode | 7C680 | 7B6E0 | same | 0 | 7 | 1 | 0 |  |
| 0xd8747fc2 | CVariableMaxVariableNode | 91CA0 | 90C50 | same | 0 | 8 | 0 | 0 |  |
| 0x4657905f | CArmySetArmyActionNode | 61B10 | 60FA0 | same | 0 | 0 | 8 | 0 |  |
| 0x28abf995 | CGetCompatibilityNode | 7C5B0 | 7B610 | same | 1 | 6 | 0 | 0 |  |
| 0xa7e41c85 | CVariableCreateSpecifiedTypeNode | 864E0 | 854B0 | same | 0 | 5 | 2 | 0 |  |
| 0x6b472bec | CGetMyselfTroopsNode | 6E760 | 6D920 | same | 0 | 0 | 7 | 0 |  |
| 0x317c7f54 | CCautionArmyAddUniqueNode | 283F0 | 27E00 | same | 0 | 6 | 0 | 0 |  |
| 0x33390d21 | CGetSearchAreaNode | 7F990 | 7E9F0 | same | 0 | 6 | 0 | 0 |  |
| 0x594ca732 | CGetSearchDataNode | 3DCD0 | 3D170 | same | 0 | 6 | 0 | 0 |  |
| 0x97229b60 | CCommandExecutionSearchNode | 54AD0 | 53E50 | same | 0 | 6 | 0 | 0 |  |
| 0xc1145d20 | CGetTargetForcePrisonerListNode | 801D0 | 7F230 | same | 0 | 6 | 0 | 0 |  |
| 0xd75d0097 | CCommandExecutionMerchantNode | 2E410 | 2D8B0 | same | 0 | 6 | 0 | 0 |  |
| 0xcabf74d1 | CGetExchangeConditionsNode | 7E930 | 7D990 | same | 0 | 6 | 0 | 0 |  |
| 0x28f35a4a | CCommandTransportDepatureNode | 32D90 | 32230 | same | 0 | 6 | 0 | 0 |  |
| 0xd10625e5 | CRecruitOfficerRemoveNode | 3E6B0 | 3DB50 | same | 0 | 6 | 0 | 0 |  |
| 0x16bf303f | CRecruitOfficerSetNode | 3E750 | 3DBF0 | same | 0 | 6 | 0 | 0 |  |
| 0x5733c979 | CTrainingOfficerSetNode | 3EF50 | 3E490 | same | 0 | 6 | 0 | 0 |  |
| 0xc75809c0 | CListAddPersonUniqueNode | 82720 | 81780 | same | 0 | 6 | 0 | 0 |  |
| 0x874694d6 | CDomesticPriorityDevelopmentSelectNode | 7B0B0 | 7A110 | same | 0 | 6 | 0 | 0 |  |
| 0xa8131535 | CDomesticOfficerSetNode | 36E80 | 36320 | same | 0 | 6 | 0 | 0 |  |
| 0x816d8e08 | CDiplomacyPriorityConditionSelectNode | 7AFA0 | 7A000 | same | 0 | 6 | 0 | 0 |  |
| 0x8a87531a | CGetPersonFormationParamNode | 7F5E0 | 7E640 | same | 0 | 6 | 0 | 0 |  |
| 0xe5ab49e1 | CGetArroundEnemyListNode | 7BA50 | 7AAB0 | same | 0 | 3 | 0 | 3 |  |
| 0x62feccb0 | CForceSetPurposeNode | 56A40 | 55DC0 | same | 5 | 0 | 0 | 0 |  |
| 0x1446a1fd | CGetDiplomacyConditionAreaNode | 7C850 | 7B8B0 | same | 0 | 5 | 0 | 0 |  |
| 0xb6ffa11b | CCommandFootholdAttackDepatureNode | 2FE10 | 2F2B0 | same | 0 | 5 | 0 | 0 |  |
| 0x465f73fa | CGetMyselfTroopsInfoNode | 6D310 | 6C4D0 | changed | 0 | 0 | 5 | 0 |  |
| 0x1d19a64 | CExecuteFootholdOccupyNode | 69AB0 | 68CE0 | changed | 0 | 0 | 5 | 0 |  |
| 0x33bb60bd | CExecuteAreaAttackNode | 65A60 | 64E10 | changed | 0 | 0 | 5 | 0 |  |
| 0xc22c23ba | CArmySetTargetArmyNode | 61D30 | 611C0 | same | 0 | 0 | 5 | 0 |  |
| 0xf3836309 | UNKNOWN_0xf3836309 | - | - | - | 1 | 1 | 1 | 1 | 판단표 시작(루트) |
| 0x8e1f7c5e | CGetAreaDistanceNode | 7B6D0 | 7A730 | same | 0 | 4 | 0 | 0 |  |
| 0x9cf455ea | CDistrictSetPurposeNode | 36D00 | 361A0 | same | 0 | 4 | 0 | 0 |  |
| 0x2472653b | CGetRemainAlliancePeriodNode | 7F780 | 7E7E0 | same | 0 | 4 | 0 | 0 |  |
| 0xbb940c54 | CAllianceSuccessConditionNode | 525C0 | 51950 | same | 0 | 4 | 0 | 0 |  |
| 0xf52793af | CCommandExecutionAllianceNode | 52990 | 51D20 | same | 0 | 4 | 0 | 0 |  |
| 0xdfcc26c6 | CGetBuildingDestructionDataNode | 370D0 | 36570 | same | 0 | 4 | 0 | 0 |  |
| 0xe7b02d30 | CListAddHexUniqueNode | 822B0 | 81310 | same | 0 | 3 | 1 | 0 |  |
| 0x40182782 | CAttackFootholdRelayAreaAttackNode | 61F10 | 613A0 | changed | 0 | 0 | 4 | 0 |  |
| 0xf5c1d1e0 | CListAddForceUniqueNode | 81FF0 | 81050 | same | 2 | 1 | 0 | 0 |  |
| 0x487cd1d8 | CGetAllFootholdNeedFoodNode | 7B450 | 7A4B0 | same | 0 | 3 | 0 | 0 |  |
| 0xa6176ffa | CCGetAllFootholdNeedMoneyNode | 7B590 | 7A5F0 | same | 0 | 3 | 0 | 0 |  |
| 0x9c94a216 | CCautionTroopsListAddUniqueNode | 29190 | 28BA0 | same | 0 | 3 | 0 | 0 |  |
| 0xa424c232 | CGetPlayerForceNode | 7F720 | 7E780 | same | 0 | 3 | 0 | 0 |  |
| 0xf758192b | CCommandExecutionHireNode | 2DAB0 | 2CFE0 | changed | 0 | 3 | 0 | 0 |  |
| 0xa8b8d8d6 | CForceCommandMoveNode | 55310 | 54690 | same | 0 | 3 | 0 | 0 |  |
| 0x1870191c | CGetCanServePersonListNode | 7C300 | 7B360 | same | 0 | 3 | 0 | 0 |  |
| 0x9fadd1cc | CGetEmployDataNode | 39FF0 | 39490 | same | 0 | 3 | 0 | 0 |  |
| 0x6a4f6b51 | CCommandExecutionEmployNode | 2D720 | 2CC50 | same | 0 | 3 | 0 | 0 |  |
| 0x1e4882c4 | CPrisonerReturnSuccessConditionNode | 85610 | 845E0 | same | 0 | 3 | 0 | 0 |  |
| 0x452f1680 | CCCommandExecutionPrisonerReturnNode | 548D0 | 53C60 | changed | 0 | 3 | 0 | 0 |  |
| 0xdc9908b1 | CCommandExecutionPrizeNode | 2EEA0 | 2E340 | same | 0 | 3 | 0 | 0 |  |
| 0x96442506 | CVariableMinVariableCalculationNode | 91E80 | 90E30 | same | 0 | 3 | 0 | 0 |  |
| 0xe4b69d5f | CCommandExecutionCreditRankUpNode | 2D440 | 2C970 | same | 0 | 3 | 0 | 0 |  |
| 0x31d0e0b5 | CCommandExecutionCreditGiveNode | 2D2A0 | 2C7D0 | same | 0 | 3 | 0 | 0 |  |
| 0xf220b6d4 | CItemSelectNode | 80A10 | 7FA70 | same | 0 | 3 | 0 | 0 |  |
| 0xa686b94b | CCommandExecutionItemNode | 54250 | 535E0 | same | 0 | 3 | 0 | 0 |  |
| 0xaa8f32c6 | CGetTransactionDataNode | 3DF60 | 3D400 | same | 0 | 3 | 0 | 0 |  |
| 0xd985fd80 | CCommandExecutionAnnulNode | 52B60 | 51EF0 | same | 0 | 3 | 0 | 0 |  |
| 0x81a2ae3e | CGetSpecifedStrategyDistrictTroopsNode | 3DDB0 | 3D250 | same | 0 | 3 | 0 | 0 |  |
| 0xcfd1a3cc | CListAddTroopsUniqueNode | 83020 | 82080 | same | 0 | 3 | 0 | 0 |  |
| 0xe05b2ece | CGetAroundLandTypeNode | 7B7B0 | 7A810 | same | 0 | 3 | 0 | 0 |  |
| 0x5c744aee | CRemoveNoInterceptPersonNode | 85810 | 847E0 | same | 0 | 3 | 0 | 0 |  |
| 0xb1fc9c34 | CGetFormationNode | 7EEE0 | 7DF40 | same | 0 | 3 | 0 | 0 |  |
| 0x339cbcee | CGetBattlePowerSoldierNumNode | 7BE80 | 7AEE0 | same | 0 | 3 | 0 | 0 |  |
| 0x6bf6a84f | CCautionTroopsUpdateStatusNode | 29B40 | 29550 | same | 0 | 3 | 0 | 0 |  |
| 0xadfb412d | CGetTransportSoldierNode | 804F0 | 7F550 | same | 0 | 3 | 0 | 0 |  |
| 0xbf3a68e1 | CCommandFrontFootholdTransportDepatureNode | 30EF0 | 30390 | same | 0 | 3 | 0 | 0 |  |
| 0x635d4d76 | CGetUserArmyListNode | 80560 | 7F5C0 | same | 0 | 3 | 0 | 0 |  |
| 0x9549348b | CCommandAutoPaintDefenseDepartureNode | 2CBC0 | 2C230 | changed | 0 | 3 | 0 | 0 |  |
| 0xf08d3d6b | CGetOfficerCandidateNode | 7F4F0 | 7E550 | same | 0 | 3 | 0 | 0 |  |
| 0xe5cb8893 | CTrainingOfficerRemoveNode | 3EEB0 | 3E3F0 | same | 0 | 3 | 0 | 0 |  |
| 0x964b046e | CCommandExecutionSpyAwayNode | 54BC0 | 53F40 | same | 0 | 3 | 0 | 0 |  |
| 0x23117676 | CSceneryInvestSetNode | 3E890 | 3DD30 | same | 0 | 3 | 0 | 0 |  |
| 0x9c2ab073 | CCommandExecutionInspectNode | 2DCD0 | 2D170 | same | 0 | 3 | 0 | 0 |  |
| 0xcbd7b4f7 | CTradePriorityCountrySelectNode | 860C0 | 85090 | same | 0 | 3 | 0 | 0 |  |
| 0xc27030b9 | CGetTradeNeedFoodNode | 803D0 | 7F430 | same | 0 | 3 | 0 | 0 |  |
| 0xcfbd6f14 | CCommandExecutionTradeNode | 54CE0 | 54060 | same | 0 | 3 | 0 | 0 |  |
| 0xf1771d23 | CGetSpecifiedArmyFlagArmyListNode | 7FC10 | 7EC70 | changed | 0 | 3 | 0 | 0 |  |
| 0x96319dce | CSetBehaviortreeRestartFlagNode | 85EC0 | 84E90 | same | 0 | 0 | 3 | 0 |  |
| 0x5d3a57aa | CClearTargetForceListNode | 52950 | 51CE0 | same | 1 | 1 | 0 | 0 |  |
| 0xd7073835 | CSetTargetForceListNode | 58C90 | 580A0 | same | 1 | 1 | 0 | 0 |  |
| 0x5551802c | CCommandExecutionDoctrinePanelAutoNode | 52FC0 | 52350 | same | 2 | 0 | 0 | 0 |  |
| 0x2130d8ab | CCautionTroopsListRemoveNullUnit | 29390 | 28DA0 | same | 0 | 2 | 0 | 0 |  |
| 0x3f469a49 | CListAddCautionTroopsNode | 816D0 | 80730 | same | 0 | 2 | 0 | 0 |  |
| 0x2dac8ea | CListRemoveCautionTroopsNode | 84BC0 | 83C20 | same | 0 | 2 | 0 | 0 |  |
| 0x9ffa7c94 | CCautionTroopsClearNode | 28CC0 | 286D0 | same | 0 | 2 | 0 | 0 |  |
| 0xa7e276a9 | CCautionTroopsSortNode | 29A90 | 294A0 | same | 0 | 2 | 0 | 0 |  |
| 0x517d81b4 | CAttackRequestSuccessConditionNode | 7AC40 | 79CA0 | same | 0 | 2 | 0 | 0 |  |
| 0xb9e83570 | CCommandExecutionAttackRequestNode | 52CA0 | 52030 | same | 0 | 2 | 0 | 0 |  |
| 0xbdc29194 | CGetCandidateFacilityListNode | 37210 | 366B0 | same | 0 | 2 | 0 | 0 |  |
| 0x73ed3a57 | CGetEarthenStoneWallBuildHexNode | 7CB80 | 7BBE0 | same | 0 | 2 | 0 | 0 |  |
| 0xe90ef890 | CGetFacilityCandidateHexListNode | 3A200 | 396A0 | same | 0 | 2 | 0 | 0 |  |
| 0x8994d82e | CListAddPossibleFacilityNode | 828A0 | 81900 | same | 0 | 2 | 0 | 0 |  |
| 0xa6d71cb | CGoodwillSuccessConditionNode | 80730 | 7F790 | same | 0 | 2 | 0 | 0 |  |
| 0xdb09cf87 | CCommandExecutionGoodwillNode | 53930 | 52CC0 | same | 0 | 2 | 0 | 0 |  |
| 0x2449e088 | CGetHiddenPoisonDataNode | 3C1F0 | 3B690 | same | 0 | 2 | 0 | 0 |  |
| 0x59d7e58a | CCCommandExecutionHiddenPoisonNode | 54110 | 534A0 | same | 0 | 2 | 0 | 0 |  |
| 0x4fbad743 | CGetEstrangeDataNode | 3A0C0 | 39560 | same | 0 | 2 | 0 | 0 |  |
| 0x92b6086f | CCCommandExecutionEstrangeNode | 533F0 | 52780 | same | 0 | 2 | 0 | 0 |  |
| 0x50c13cbf | CGetPlacationDataNode | 3DB90 | 3D030 | same | 0 | 2 | 0 | 0 |  |
| 0xed4f2f01 | CCCommandExecutionPlacationNode | 545D0 | 53960 | same | 0 | 2 | 0 | 0 |  |
| 0x5c2752cc | CCommandExecutionRumorNode | 2F080 | 2E520 | same | 0 | 2 | 0 | 0 |  |
| 0x6c659fe9 | CGetUnattendedhomeDataNode | 3E400 | 3D8A0 | same | 0 | 2 | 0 | 0 |  |
| 0x7e31c149 | CCommandExecutionUnattendedHomeNode | 54F50 | 542D0 | same | 0 | 2 | 0 | 0 |  |
| 0xd004322 | CCommandExecutionDualDestructionNode | 53270 | 52600 | same | 0 | 2 | 0 | 0 |  |
| 0xc4ecfc1b | CSetRelayHexListNode | 6EE30 | 6DFF0 | same | 0 | 0 | 2 | 0 |  |
| 0x6f68feac | CMiscSetHexEvaluationNode | 85580 | 57F10 | same | 0 | 0 | 0 | 2 |  |
| 0xa16b21a8 | CGetFireStrategySuccessFireStrategyNode | 7EAC0 | 7DB20 | same | 0 | 0 | 0 | 2 |  |
| 0x219365ea | CCommandExecutionFireStrategyNode | 1F2A0 | 1F2C0 | same | 0 | 0 | 0 | 2 |  |
| 0xd27b5fb7 | CClearFriendForceListNode | 52910 | 51CA0 | same | 1 | 0 | 0 | 0 |  |
| 0x9914df82 | CSetFriendForceListNode | 58B90 | 57FA0 | same | 1 | 0 | 0 | 0 |  |
| 0x94124819 | CCommandExecutionExpansionNode | 53790 | 52B20 | same | 1 | 0 | 0 | 0 |  |
| 0x9a6f523b | CCommandExecutionGovernmentAutoNode | 53B80 | 52F10 | same | 1 | 0 | 0 | 0 |  |
| 0x888b722a | CCommandExecutionPostAutoNode | 54710 | 53AA0 | same | 1 | 0 | 0 | 0 |  |
| 0x85c9ff2c | CDistributeSpyPointNode | 550B0 | 54430 | same | 1 | 0 | 0 | 0 |  |
| 0x6e10a61 | CListAddTacticsBookNode | 82C70 | 81CD0 | same | 1 | 0 | 0 | 0 |  |
| 0x1f906b | CSetTacticsBookEvaluationNode | 6EFD0 | 3DF40 | same | 1 | 0 | 0 | 0 |  |
| 0xe05a5bf4 | CCommandExecutionLearnNode | 54330 | 536C0 | same | 1 | 0 | 0 | 0 |  |
| 0x25f8e49e | CCautionTroopsListDedupeNode | 4F90C0 | 42B570 | same | 0 | 1 | 0 | 0 |  |
| 0x24aea91c | CVariableGetFindItemIndexNode | 89FB0 | 88F80 | changed | 0 | 1 | 0 | 0 |  |
| 0xdf1b4f83 | CCautionTroopsRemoveNode | 29990 | 293A0 | same | 0 | 1 | 0 | 0 |  |
| 0x9ea63aa3 | CSetCautionTroopsVirtualTargetFootholdNode | 85F70 | 84F40 | same | 0 | 1 | 0 | 0 |  |
| 0xb331a3e6 | CCautionTroopsListAddNode | 28D20 | 28730 | same | 0 | 1 | 0 | 0 |  |
| 0x4efba2a9 | CVariableGetAdvantageInfoNode | 86680 | 85650 | same | 0 | 1 | 0 | 0 |  |
| 0x34a7d69f | CGetAdvantageOwnFootholdNode | 7B1B0 | 7A210 | same | 0 | 1 | 0 | 0 |  |
| 0xef1f7383 | CListRemoveFootholdNode | 84BC0 | 83C20 | same | 0 | 1 | 0 | 0 |  |
| 0xc48bfb68 | CCommandAreaTryGetDepartureNode | 2AB90 | 2A5A0 | changed | 0 | 1 | 0 | 0 |  |
| 0x73547ae5 | CExecuteInterceptNode | 6AA10 | 69BD0 | same | 0 | 0 | 1 | 0 |  |
| 0x80a285a7 | CExecuteFacilityAttackNode | 69740 | 68970 | same | 0 | 0 | 1 | 0 |  |
| 0xce0850fa | CExecuteConstructNode | 69420 | 68650 | same | 0 | 0 | 1 | 0 |  |
| 0xa1763cb3 | CExecuteAutoPaintDefenseNode | 69240 | 68590 | changed | 0 | 0 | 1 | 0 |  |
| 0x2ef6f2b8 | CSetFootholdAttackRelayHexNode | 6E950 | 6DB10 | same | 0 | 0 | 1 | 0 |  |
| 0x886255d | CTroopsOrderDesutructionFacilityNode | 6F5F0 | 6E710 | same | 0 | 0 | 1 | 0 |  |
| 0x9f649845 | CArmySetRetreatNode | 61C90 | 61120 | same | 0 | 0 | 1 | 0 |  |
| 0x503972a4 | CGetMyselfArmyNode | 1FE00 | 1FE20 | same | 0 | 0 | 0 | 1 |  |
| 0x7ae49aac | CClearArmyAIActionNode | 1F160 | 1F180 | same | 0 | 0 | 0 | 1 |  |
| 0xcf856e80 | CSetRelayHexEvadeFlameHexNode | 201C0 | 201E0 | same | 0 | 0 | 0 | 1 |  |
| 0x845574ad | CClearRelayHexNode | 1F1A0 | 1F1C0 | same | 0 | 0 | 0 | 1 |  |
| 0x32e366f | CGetNearCapitalNode | 1FE50 | 1FE70 | same | 0 | 0 | 0 | 1 |  |
| 0x8c4788df | CResolutionFakeNewsNode | 20100 | 20120 | same | 0 | 0 | 0 | 1 |  |
| 0xc067d4e | CGetFakeNewsSuccessProbabilityNode | 7E9E0 | 7DA40 | same | 0 | 0 | 0 | 1 |  |
| 0xcfb335e6 | CGetSpecifiedRangeTrapListNode | 80090 | 7F0F0 | same | 0 | 0 | 0 | 1 |  |
| 0xc160610b | CCommandExecutionFakeNewsNode | 1F1D0 | 1F1F0 | same | 0 | 0 | 0 | 1 |  |
| 0x7f07545c | CGetAttackTargetFootholdNode | 1FAA0 | 1FAC0 | same | 0 | 0 | 0 | 1 |  |
| 0x8aea0861 | CRecoverLogisticsNode | 20040 | 20060 | same | 0 | 0 | 0 | 1 |  |
| 0xf715bb7f | COccupyNeighborSceneryNode | 1FFC0 | 1FFE0 | same | 0 | 0 | 0 | 1 |  |
| 0xb553b8d4 | COccupyNeighborCapitalNode | 1FF40 | 1FF60 | same | 0 | 0 | 0 | 1 |  |
| 0xddc7f4d7 | CAvoidPoisonNode | 1F100 | 1F120 | same | 0 | 0 | 0 | 1 |  |
| 0x6532e2bf | CCutLogisticsNode | 1F380 | 1F3A0 | same | 0 | 0 | 0 | 1 |  |
| 0x79eb5c74 | CMoveAdvantagePositionNode | 1FE80 | 1FEA0 | same | 0 | 0 | 0 | 1 |  |
| 0x472b6ddd | CMoveObjectAttackingArmyPositionNode | 1FEE0 | 1FF00 | same | 0 | 0 | 0 | 1 |  |
| 0xa7551ed2 | CExclusionUserArmyAttachedFootholdNode | 1F760 | 1F780 | same | 0 | 0 | 0 | 1 |  |
| 0xa18cf428 | CRepairNeigoborObjectNode | 200A0 | 200C0 | same | 0 | 0 | 0 | 1 |  |

## 출진 노드의 보조 함수 (2026-11-25, 조사 목록 D03·D07·D06)

- `27A00`은 노드 클래스 Execute가 아니라 **지역 점령 출진 노드 `CCommandAreaOccupyDepatureNode`(`29BA0`, kind `0x9c3384c2`)가 편성 함수 4개(`43D10`·`441E0`·`446A0`·`44B60`)를 거쳐 부르는 실행 보조 함수**다. 군세 종류 0xD~0x10(13~16) 군세를 만든다(자세한 칸 쓰기는 functions.md 2.15 `27A00` 행). 확신도 코드+호출 자리 E8 바이트.
- `28030`도 보조 함수다. **`CCommandAutoPaintDefenseDepartureNode`(`2CBC0`, kind `0x9549348b`, 위 표 156행)가 자리 `2D1CC`에서 부르고**, 군세 종류 23(자동 영역 방어)을 만든다. 확신도 코드+바이트.
- 이 두 함수와 `2AB90`(`CCommandAreaTryGetDepartureNode`, kind `0xc48bfb68`: 종류 0x15 지역 군세와 종류 5 건설 군세)은 `35A70`(CDepartureNode)·`365A0`(CDepartureTroopsCreateNode)을 거치지 않고 `1EDC30`(출진 실행)으로 직접 부대를 만든다. 반대로 `35A70`·`365A0` 쌍은 판단표의 `부대편성출진`·`군세생성` 노드 19개씩(군단 트리)이 쓴다.
- `CDepartureNode` 인수 14개 가운데 `[6..10]` 정수 다섯이 `35A70`이 읽는 네 칸(`+0x50..+0x5C`)과 어떻게 짝지어지는지는 미해결이다(functions.md 2.15 `35A70` 행, ai/roles.md 6-4절 「출진 노드 인수」). 판단표 쪽 값은 요격 노드 N1789 `(2,1,1,2,1)`, N1790 `(2,0,1,2,1)`, 이동 N1837 `(1,0,0,1,0)`, 건설 N3380 `(1,1,1,1,0)`이다(origlib `Node.params[6:11]`).

## 판단표에 없는 노드 클래스 (2026-11-25)

- 실행 파일 RTTI에서 뽑은 행동 트리 노드 클래스는 284개다(출처: AI_TacticsMod/src/ai_trace_nodes.h, 생성기 `tools/gen_ai_trace_nodes.py`; 실행 함수는 vtable 16번 칸). 위 표의 232종과 이름·실행 RVA로 대조하면 **51개는 이름도 실행 RVA도 위 표에 없다** = 현재 `0000/bt_exce.bin`이 쓰지 않는 클래스다. 13개는 이름만 다르고 실행 RVA가 위 표에 있다(같은 실행 함수를 나눠 쓰거나 철자 차이). 확신도: 대조는 기계적(확정), 「쓰지 않는다」는 현재 CE 판단표 기준이며 기본판 `0000/bt.bin`에서의 사용 여부는 미해결.
- 아래 클래스의 본문 동작은 판독하지 않았다(이름만). 여러 개가 부대 행동·목표·경유점 쓰기 함수의 호출자다([함수 지도](../functions.md) 3.6절).
- 수송 출진: 위 표에 있는 것은 `CCommandTransportDepatureNode` `32D90`과 `CCommandFrontFootholdTransportDepatureNode` `30EF0`이고, 아래의 `CDepartureTransportNode` `362D0`은 표에 없다. `362D0`은 `1EDC30`(출진 실행)을 직접 부르지 않는다.

| 클래스 | 실행 RVA | vtable 실행 칸 |
|---|---|---|
| CCutSupplyNode | `1F5C0` | `1346D48` |
| CGetAttackTargetArmyListNode | `1F7C0` | `1346EB0` |
| CCautionArmyRemoveNode | `28690` | `1348920` |
| CCautionFootholdAddUniqueNode | `28940` | `13489D0` |
| CCautionFootholdRemoveNode | `28AC0` | `1348A88` |
| CCautionTroopsAddNode | `28BB0` | `1348B40` |
| CCommandExecutionGovernmentNode | `2D7F0` | `1349490` |
| CCommandExecutionMoveNode | `2ECE0` | `1349600` |
| CDefendFootholdAddUniqueNode | `35720` | `13499B0` |
| CDefendFootholdRemoveNode | `35880` | `1349A68` |
| CDepartureTransportNode | `362D0` | `1349BC8` |
| CDistrictListAddTacticsNode | `36BD0` | `134A8E0` |
| CDomesticOfficerRemoveNode | `36D70` | `1349DE0` |
| CLoopListElementNode | `59CD0` | `134D498` |
| CArmySetRelayNode | `61B70` | `134DE70` |
| CDecideAreaOccupyRouteNode | `651E0` | `134E0E8` |
| CExecuteAreaOccupyNode | `66AE0` | `134E300` |
| CExecuteAttackAreaBuildingNode | `678D0` | `134E6E0` |
| CExecuteAttackBuildingNode | `68080` | `134E5D0` |
| CExecuteAttractNode | `68600` | `134E7F0` |
| CGetRelayHexListNode | `6E7B0` | `134ECD0` |
| CTroopsSetPurposeNode | `6FE00` | `134F058` |
| CTroopsSetTargetTroopsNode | `6FFC0` | `134DD08` |
| CGetAvailableTacticsListNode | `7BCB0` | `1350498` |
| CGetBuildingNode | `7C140` | `134FD68` |
| CGetFootholdNeedFoodNode | `7EDA0` | `1350828` |
| CGetFootholdNeedMoneyNode | `7EE40` | `13508E0` |
| CGetScopeTimeNode | `7F860` | `13506C8` |
| CGetSpecificForceDataNode | `7FAA0` | `1350610` |
| CListAddDistrictNode | `81800` | `13512B0` |
| CListAddDistrictUniqueNode | `81940` | `1351360` |
| CListAddFacilityNode | `81AC0` | `1351418` |
| CListAddNumberValueNode | `82430` | `13518E8` |
| CListAddNumberVariableNode | `82500` | `1351998` |
| CListAddTacticsNode | `82DA0` | `1351D20` |
| CListAddTroopsNode | `82EE0` | `1351DD0` |
| CListAddUniqueNumberValueNode | `83310` | `1351F38` |
| CListPersonExtractionNode | `84890` | `1352148` |
| CSetParentTroopsNode | `86010` | `1352FF0` |
| CVariableGetForceDistrictListNode | `8C8F0` | `1353CF0` |
| CVariableMaxValueCalculationNode | `91AC0` | `13544E0` |
| CVariableMaxVariableCalculationNode | `91BE0` | `1354658` |
| CVariableMinValueCalculationNode | `91D60` | `1354930` |
| CVariablePowerValueNode | `923A0` | `1354E38` |
| CVariablePowerVariableNode | `92440` | `1354EE8` |
| CVariableRoundDownValueNode | `92500` | `1354FA0` |
| CVariableRoundUpValueNode | `92620` | `1355058` |
| CVariableRoundValueNode | `92740` | `1355110` |
| CVariableSqrtNode | `92A50` | `1355338` |
| CGetUnusedTroopsIndexNode | `4171E0` | `134A828` |
| CJuicyLeafNode | `101C1B8` | `134D100` |

이름만 다르고 실행 RVA가 위 표에 있는 것: CSetDistrictEvaluationNode(`85580`), CSetOrderListNode(`4F90C0`), CCommandExecutionEstrangeNode(`533F0`), CCommandExecutionHiddenPoisonNode(`54110`), CCommandExecutionPlacationNode(`545D0`), CCommandExecutionPrisonerReturnNode(`548D0`), CSetTroopsEvaluationNode(`6EFD0`), CGetAllFootholdNeedMoneyNode(`7B590`), CListRemoveAreaNode(`84BC0`), CListRemoveArmyNode(`84BC0`), CListRemoveDistrictNode(`84BC0`), CListRemoveHexNode(`84BC0`), CListRemoveTroopsNode(`84BC0`).

### 위 51개 클래스의 사용 여부 (2026-11-25, 조사 목록 N06; 확신도 코드)

방법: 클래스 이름 -> 판단표 kind 해시는 옛 연구 `AI_TacticsMod/research/AI_Analysis/upper/node_factory_map.json`(해시와 클래스 이름 대응만 사용, 주소는 쓰지 않음)에서 가져왔고, 현재 빌드 노드 공장 `1ADF0`(`ghidra_full.py grep <해시>`)에서 표본 4개(`0xc976c91d`->생성자 `1E660`->vtable `1346CC8`, `0xd56a18d9`->`77560`->`13552B8`, `0xfe2d8e2`->`76510`->`1351868`, `0x78f9c619`->`59A90`->`134D418`)의 해시 -> 생성자 -> vtable을 확인했다(vtable +0x80 = 위 표의 「vtable 실행 칸」과 일치). 나머지 해시는 json 대응만 신뢰한 것(미검증). 사용 횟수는 `origlib.load_bt(False/True)`로 4트리(세력/군단/군세/부대) 노드의 kind를 센 것이다. 직접 호출자는 `ghidra_full.py callers <실행 RVA>` 결과(51개 모두 직접 E8 호출 0건; 실행 칸은 vtable로만 도달).

| 클래스 | kind 해시 | bt_exce.bin(세력/군단/군세/부대) | bt.bin(기본판) | 직접 호출자 | 판정 |
|---|---|---|---|---|---|
| CCutSupplyNode | `0xc976c91d` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CGetAttackTargetArmyListNode | `0x8a8bce6e` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CCautionArmyRemoveNode | `0x6241b9ff` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CCautionFootholdAddUniqueNode | `0x50fbf24` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CCautionFootholdRemoveNode | `0x8611ac4f` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CCautionTroopsAddNode | `0xc1407d68` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CCommandExecutionGovernmentNode | `0x2a432f0e` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CCommandExecutionMoveNode | `0x1ae782e` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CDefendFootholdAddUniqueNode | `0xb0085ea5` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CDefendFootholdRemoveNode | `0x27cea01a` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CDepartureTransportNode | `0x6749dcb8` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CDistrictListAddTacticsNode | `0xbb9523fe` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CDomesticOfficerRemoveNode | `0x36aad44f` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CLoopListElementNode | `0x78f9c619` | 12/548/15/5 | 11/388/15/1 | 없음 | **사용 중 = 위 전수표의 UNKNOWN_0x78f9c619(반복) 노드의 클래스** (아래 정정) |
| CArmySetRelayNode | `0x9d091cfb` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CDecideAreaOccupyRouteNode | `0x6a79ce39` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CExecuteAreaOccupyNode | `0x3d36144` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CExecuteAttackAreaBuildingNode | `0x6e0a0754` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CExecuteAttackBuildingNode | `0x903aace` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CExecuteAttractNode | `0xfa20b664` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CGetRelayHexListNode | `0x8ea4010f` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CTroopsSetPurposeNode | `0x802eb28a` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CTroopsSetTargetTroopsNode | `0x6f4510ba` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CGetAvailableTacticsListNode | `0xaf686835` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CGetBuildingNode | `0x64fc2739` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CGetFootholdNeedFoodNode | `0x4b89b99a` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CGetFootholdNeedMoneyNode | `0x96dcb8bc` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CGetScopeTimeNode | `0x1e166cbd` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CGetSpecificForceDataNode | `0x2b62684d` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CListAddDistrictNode | `0x1c8a2f8f` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CListAddDistrictUniqueNode | `0xb245a1b9` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CListAddFacilityNode | `0x3c9b041a` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CListAddNumberValueNode | `0xfe2d8e2` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CListAddNumberVariableNode | `0xbdf62a2f` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CListAddTacticsNode | `0xdc87df58` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CListAddTroopsNode | `0xbf160cdc` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CListAddUniqueNumberValueNode | `0x208e6506` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CListPersonExtractionNode | `0x2e1b014c` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CSetParentTroopsNode | `0x48905203` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CVariableGetForceDistrictListNode | `0x8e011fb0` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CVariableMaxValueCalculationNode | `0xdf5951d9` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CVariableMaxVariableCalculationNode | `0xc4a43398` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CVariableMinValueCalculationNode | `0xb0f94347` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CVariablePowerValueNode | `0x27aaf550` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CVariablePowerVariableNode | `0xd271c663` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CVariableRoundDownValueNode | `0x6ab2bf7b` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CVariableRoundUpValueNode | `0xcf694cb4` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CVariableRoundValueNode | `0x48fa3919` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CVariableSqrtNode | `0xd56a18d9` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CGetUnusedTroopsIndexNode | `0x412b972e` | 0/0/0/0 | 0/0/0/0 | 없음 | 미사용 |
| CJuicyLeafNode | (해시 없음) | - | - | 없음 | 노드 종류가 아님: 실행 칸 `101C1B8`은 57바이트 중단 처리기(`abort()` 호출, 코드 확인); 리프 노드 추상 기반 클래스로 보임(가설) |

- 결론(확신도 코드): 50개 클래스는 `bt_exce.bin`(CE)과 `bt.bin`(기본판) 어느 쪽에도 노드가 없고(0000 폴더에는 이 두 파일뿐, 다른 `bt*.bin` 없음) 직접 호출자도 없다. 따라서 이 클래스들의 실행 함수가 부르는 부대 행동·목표·경유점 쓰기 경로([함수 지도](../functions.md) 3.6절)는 현재 빌드에서 도달하지 않는 경로다. 여기서 「도달하지 않음」은 vtable 간접 호출 자리(모든 노드 실행의 공통 호출)가 판단표 노드 kind로만 이 클래스를 만든다는 가정에 기댄다(공장 `1ADF0` 외 생성 경로는 이 클래스들의 vtable 참조를 `xref`로 점검하지 않음).
- **정정(앞의 「51개는 이름도 실행 RVA도 위 표에 없다 = 쓰지 않는 클래스」와 충돌)**: `CLoopListElementNode`(`59CD0`, vtable 실행 칸 `134D498`)는 쓰이는 클래스다. 노드 공장 `1ADF0`이 kind `0x78f9c619`로 생성자 `59A90`(vtable `134D418`; `134D418+0x80 = 134D498`)을 부르고, 이 kind가 위 전수표의 `UNKNOWN_0x78f9c619`(반복: 목록 순회; CE 12/548/15/5)다. 그 전수표 행의 「클래스 - / 실행 RVA -」는 클래스 이름이 안 붙은 것일 뿐이다. `59CD0` 본문은 `+0x2C` 반복 종류(case 1~0x11 이상)로 분기해 종류별 순회 함수(`5C480`, `5A3C0`, `5D230`…)를 부르고, 노드 인수는 `5D640`이 `+0x28` 수집 모드, `+0x2C` 반복 종류, `+0x30`, `+0x40`에 옮긴다(코드; 종류별 의미는 미판독). 따라서 「쓰지 않는 클래스」는 50개다. 기존 문장은 고치지 않고 둔다.
- 기본판에만 있는 kind 1종: `0x48be4fa3`(`CListRemoveAreaNode`, 실행 `84BC0`, 위 「이름만 다르고…」 목록에 있음)이 `bt.bin` 군단 트리에 3개 있고 `bt_exce.bin`에는 없다. kind 종류 수는 기본판 199, CE 232(기본판 kind 중 CE에 없는 것은 이 1종뿐, CE에만 있는 것 34종). `bt.bin` 노드 수는 세력/군단/군세/부대 = 211/6781/348/55, CE 246/10790/348/111(코드, `origlib.load_bt`).

## 「군사」 표시 노드 한 줄 설명 (2026-11-25, 조사 목록 N01; 확신도는 줄마다)

방법: 각 실행 RVA를 `decomp_cache.py get`으로 읽고(전부 `ghidra_full` 디컴파일, 본문 확인), 인수 개수·종류는 `origlib.load_bt()`의 실제 노드 `params`와 판단표 의사코드(`pseudo_*.txt`)의 호출 모양으로 교차했다. 이 절은 부록 A(조사 목록) 「군사」 표시 55개 클래스를 모두 다룬다(위 전수표 비고 칸은 비워 두고 이 절이 비고를 대신한다). 인수 `[0]`=`+0x38`, `[1]`=`+0x3C`, `[2]`=`+0x40`… 인수 값은 변수 id 또는 정수 상수이며 `B28D20`(변수 읽기)로 풀린다. 「목록 종류 코드」는 `14001A250` 세 번째 인수: 2 군세, 3 부대, 4 무장, 5 거점, 6 지역, 7 HEX, 0xB 경계군세, 0xD 전법, 0xF 경계부대(`CCautionArmy`), 0x10 시설 정의, 0x11 전법서(위 [unresolved.md](unresolved.md) 3-2절 표기와 같음). 판단 주체 변환은 `B7100`(부대)·`B72F0`(군세)·`B7170`(군단)·`B7210`(세력)이 `"AgentType"`으로 한다(conditions.md 서문, 코드).

**공통 모양 (코드)**

- 목록 추가 계열은 인수 2개 `[0]`=넣을 값(변수), `[1]`=목록(변수; 없으면 종류 코드로 새로 만듦). 「중복 제외(Unique)」는 같은 값이 이미 있으면 넣지 않고 성공(1)을 돌려준다(본문 `+0x38`~`+0x3C` 읽기와 해시 목록 비교 루프 확인; 크기 374바이트 vs 일반 303/313바이트). 모두 성공 시 1, 읽기 실패 시 2.
- `6EFD0`·`85580`은 본문이 같다: `[0]`이 가리키는 평가 객체의 `+8`(정수)에 `[1]`(수치 변수)을 쓴다. 이름만 다르다(아래 「평가점수 저장」 4종). 점수는 `CListSortEvaluationNode`(`84CB0`) 정렬 키로 쓰인다(기존 표).
- `84BC0`은 목록에서 값을 지우는 공통 본문(`[0]`=값, `[1]`=목록; 목록에 있으면 `21A350`으로 제거, 없어도 성공 1). 클래스 이름은 목록 종류별로 다르다.

| 클래스 | 실행 RVA | 인수(판단표 실측) | 하는 일 한 줄 | 확신도 |
|---|---|---|---|---|
| CListAddFootholdNode / CListAddFootholdUniqueNode | `81BF0` / `81D30` | 2개: 거점, 목록(종류 5) | 거점 목록에 거점 추가(Unique는 중복 제외) | 코드 |
| CListAddArmyNode / CListAddArmyUniqueNode | `81420` / `81550` | 2개: 부대, 목록(종류 3) | 부대 목록에 부대 추가(Unique는 중복 제외) | 코드 |
| CListAddTroopsUniqueNode | `83020` | 2개: 군세, 목록(종류 2) | 군세 목록에 중복 없이 추가 | 코드 |
| CListAddHexNode / CListAddHexUniqueNode | `82170` / `822B0` | 2개: HEX, 목록(종류 7) | HEX 목록에 칸 추가(Unique는 중복 제외) | 코드 |
| CListAddCautionTroopsNode / CListAddUniqueCautionTroopsNode | `816D0` / `831A0` | 2개: 경계군세, 목록(종류 0xB) | 경계군세 목록에 추가(Unique는 중복 제외) | 코드 |
| CListAddTacticsBookNode | `82C70` | 2개: 전법서, 목록(종류 0x11) | 전법서 목록에 추가 | 코드 |
| CListRemoveCautionTroopsNode / CListRemoveFootholdNode | `84BC0` | 2개: 값, 목록 | 목록에서 값 제거(공통 본문, 위 「공통 모양」) | 코드 |
| CMiscSetFootholdEvaluationNode / CSetFormationEvaluationNode / CSetCautionTroopsEvaluationNode / CSetTacticsBookEvaluationNode / CMiscSetHexEvaluationNode | `6EFD0`(앞 4) / `85580`(HEX) | 2개: 대상 객체, 수치 | 대상 객체의 평가 점수(`+8`)를 저장 | 코드 |
| CListAddPossibleFacilityNode | `828A0` | 3개: 칸(HEX), 건설 주체(무장), 출력 목록(종류 0x10 시설 정의) | 시설 정의 표(`world+0x73958`부터) 가운데 `27A8D0`(건설 가능 최종 판정, functions.md)을 통과한 시설을 목록에 담는다. 이름은 「건설가능시설목록추가」 | 코드(`27A8D0` 인수 모양 확인; 칸 지형 비트(`+0x1C`)로 거르는 첫 분기는 미판독) |
| CGetFacilityCandidateHexListNode | `3A200` | 7개(`+0x38`~`+0x50`): 거점, 무장, 시설 종류, 출력 HEX 목록(종류 7), 변수 2개, 수치 1개 | 시설을 지을 칸 후보 목록 조회. 반경 안 칸을 `185710`(길찾기)·`27A8D0`으로 걸러 담는 8KB 함수(판단표 N3387: 무장 `검사중인무장`, 시설 종류 4) | **가설**: 인수 모양과 호출 함수만 확인, 걸러내는 식은 미판독 (강한 모델 검토 필요) |
| CGetPersonFormationParamNode | `7F5E0` | 4개: 무장, 평가 종류(판단표 값 3), 출력 진형 객체, 출력 점수 | 무장이 쓸 수 있는 진형(`233CF0`) 20종마다 `C00E0(무장, 진형, 평가 종류)` 점수를 구해 최고 점수 진형과 그 점수를 내놓는다 | 코드 |
| CGetFormationNode | `7EEE0` | 2개: 진형 번호(상수), 출력 객체 | 진형 표(`world+0x77430`부터)에서 번호의 진형 객체를 꺼낸다(`BE040`; 6번은 없음) | 코드 |
| CSelectPersonTacticsNode | `85BE0` | 3개: 무장, 진형, 출력 전법 목록(종류 0xD) | 전법 최대 3개를 골라 담는다: 전법 표(200종)에서 `235090` 참·무장 보유(`93770`)·진형 허용 비트(`+0x6C`)를 만족하는 것을 먼저, 부족하면 무장의 전법 칸 10개(`22BD60`)에서 진형 허용인 것을 채운다. 출진 명령 전법 3칸(`D3C70`, functions.md D04)의 입력 | 코드 |
| CGetBuildingDestructionDataNode | `370D0` | 2개: 출력 무장 목록(종류 4), 출력 지역 목록(종류 6) | 판단 주체 군단의 건물 파괴 계략용 자료 생성: 실행 무장 후보 `6DD230`과 대상 지역 후보 `6E08E0` | 코드(두 보조 함수 본문은 미판독) |
| CCommandExecutionBuildingDestructionNode | `52EC0` | 3개: 군단, 지역, 무장 | 계략 명령 종류 `0x14`(건물 파괴, rules_diplomacy.md 5.4)의 명령 구조체를 채워 `1FA5C0`으로 실행. 금 상한 `1E0110` | 코드(명령 번호는 상수 `0x14` 직접 확인) |
| CCommandExecutionDualDestructionNode | `53270` | 4개: 군단 등 객체 4개 | 명령 종류 `10`의 구조체를 채워 `1FA5C0` 실행. 조건 79 `이호경식명령가능`이 이 노드의 하위(conditions.md)이므로 이호경식 실행 노드로 읽힌다. 거점 `+0x14`가 임계값(`DAT_141A4B740`) 이상일 때만 실행 | 코드(종류 10) / 가설(이름 = 이호경식, 조건 79 문맥) |
| CCommandExecutionAttackRequestNode | `52CA0` | 5개: 군단, 거점, 선택값(0/1/2), 무장, 값 | 외교 명령 종류 `9`(공격 요청, rules_diplomacy.md 3.5)의 구조체를 채운다. 군단(`230270`) `+0x14`가 임계값(`DAT_141A4B668`) 미만이면 실패. 선택값 0/1/2에 따라 `[4]`가 수치(+0x68 또는 +0x64)나 객체(+0x70)로 쓰인다 | 코드(종류 9); 선택값별 구조체 칸 의미는 미판독 |
| CAttackRequestSuccessConditionNode | `7AC40` | 7개(`+0x38`~`+0x50`) | 공격 요청 성립 조건 검사. 인수 객체의 번호가 게임 진행 객체(`world+0x871E8`)의 플레이어 세력(`330B90`) 번호와 다르면 곧바로 실패(2) — 요청 상대가 플레이어일 때만 진행하는 것으로 읽힌다. 나머지는 `9DB10`(요청 비용)으로 금·병력 요구량과 보유량을 비교 | **가설**(인수 0이 세력인지 군단인지 미확인; 본문 일부만 읽음) |
| CCommandTransportDepatureNode | `32D90` | 5개: 출발 거점 목록, 도착 후보 거점 목록, 값 3개(판단표 `수송출진명령`) | 수송 출진 명령 작성(10KB) | **가설**: 인수와 호출 모양만(`ghidra_full callees`: 직접 호출 55·간접 25), 본문 미판독 (강한 모델 검토 필요) |
| CGetTransportSoldierNode | `804F0` | 4개: 거점 목록, 상수 3개(판단표 24, 6, 6) | 목록의 각 거점마다 `9F410`(필요량)을 계산해 거점 `+0x90`에 부호 있는 수송 병력 값을 저장(`D3A90`) | 코드(저장 위치); 부호 의미는 미판독 |
| CGetAllFootholdNeedFoodNode | `7B450` | 4개: 군단, 상수 3개(24, 6, 6) | 군단 소속 세력의 거점 전부에 `9F410(거점, …)`으로 필요 군량을 계산해 거점 `+0x94`에 쓴다(정보 조회 Foothold 항목 38이 이 값을 읽는다: `8B190` case 0x26) | 코드 |
| CCGetAllFootholdNeedMoneyNode | `7B590` | 2개: 군단, 상수(6 또는 4) | 같은 방식으로 필요 금(`9F670`)을 거점 `+0x98`에 쓴다(항목 39) | 코드 |
| CGetMyselfTroopsNode | `6E760` | 1개: 출력 | 판단 주체(군세 트리)의 군세 객체를 변수에 넣는다(`B72F0`) | 코드 |
| CGetMyselfTroopsInfoNode | `6D310` | 2개: 항목 번호, 출력 | 판단 주체 군세의 정보 조회(getter, 5KB). 항목 0 군세 번호, 1 종류(`+0x14`), 2·3 소속 부대 목록, 4 목표 객체(종류 `+0x14`별로 거점·지역·시설·경계군세 표를 골라 `+0x16`으로 변환), 6 객체 번호(`+8`), 7 소속 군단, 10 병사 합(부대 `+0x16`), 13 전력 합(`B6F50`), 14 경유 HEX 목록(`+0x18` u16[10]), 15 소유 세력(`22E560`) | 코드(0~4·6·7·10·13~15); 5·8·9·11·12는 **가설**(부대 필드 합산: `+0x5C`·`+0x60`·`+0x172`·능력 합 등, 의미 미판독) — 강한 모델 검토 필요 |
| CVariableGetCautionArmyInfoNode | `88140` | 3개: 경계부대 항목, 항목 번호(상수), 출력 | 경계부대(`CCautionArmy`; 표 `world+0x81B50` 간격 0x18) 정보: 0 항목 번호(`22F4F0`), 1 그 부대 전력(`B6F50`), 2 관련 거점(`+0x12`, `32E3B0`), 3 적 부대(`+0x10` 번호 -> 부대 표), 4 `+8` 정수 | 코드 |
| CCautionArmyAddUniqueNode | `283F0` | 3개: 적 부대, 거점, 출력 경계부대 목록(종류 0xF) | 적 부대가 목록에 이미 있으면 성공만 하고, 없으면 빈 경계부대 칸(`world+0x81B50` 표)에 (부대 번호 `+0x10`, 거점 번호 `+0x12`, 상한 0x3D)을 채워 목록에 넣는다. 부대가 자기 거점 칸 위이면 실패, 거점 소유 세력이 판단 주체와 다르면 `26D660`(외교 관계)을 통과해야 한다 | 코드 |
| CCautionTroopsListAddNode | `28D20` | 4개: 경계군세 목록(종류 0xB), 부대 목록, 대상 거점, 값 | 새 경계군세를 만든다: 빈 칸(`world+0x80BA8` 표, 간격 0x48)을 잡아 부대 목록을 복사하고 대상 거점(`+0x1A`, 상한 0x3D), 번호(`+0x18` = 목록 안 안 쓴 최소 번호), 소속 군단(`+0x14` = 판단 주체 군단 번호)을 쓴다. 부대가 이미 다른 경계군세에 있으면 실패(2) | 코드 |
| CCautionTroopsListAddUniqueNode | `29190` | 3개: 경계군세 목록, 순번(수치), 부대 | 목록의 순번째 경계군세의 소속 부대 목록(`+0x30`)에 부대를 중복 없이 추가 | 코드 |
| CCautionTroopsRemoveNode | `29990` | 2개: 경계군세, 부대 | 경계군세의 소속 부대 목록(`+0x30`)에 부대가 있으면 `+0x28` 쪽 목록에서 제거 | 코드(두 목록의 관계 미확인) |
| CCautionTroopsListRemoveNullUnit | `29390` | 1개: 경계군세 목록 | 각 경계군세의 소속 부대 가운데 유효하고 명령(`+0x37`)이 `0xB`·`0xC`(퇴각)가 아닌 부대만 남기고, 부대가 하나도 안 남은 경계군세는 `32D180`(삭제)로 지운다 | 코드 |
| CCautionTroopsClearNode | `28CC0` | 1개: 경계군세 | 경계군세를 삭제(`32D180`, functions.md T01) | 코드 |
| CCautionTroopsSortNode | `29A90` | 1개: 경계군세 목록 | 목록 내부 정렬(헬퍼 7개 호출) | **가설**(정렬 기준 미판독) |
| CCautionTroopsUpdateStatusNode | `29B40` | 2개: 경계군세, 상수(1) | 경계군세 `+0x3C` = (인수 == 1). 경계군세 정보 항목 3(`+0x3C`)이 읽는 상태 값 | 코드 |
| CSetCautionTroopsVirtualTargetFootholdNode | `85F70` | 2개: 경계군세, 거점 | 경계군세 `+0x1A` = 거점 `+0x4E`(상한 0x3D). 정보 항목 4가 읽는 값(unresolved.md 3-2절 충돌 표시 참고) | 코드 |
| CArmySetArmyActionNode | `61B10` | 2개: 부대, 행동 번호(상수 1~3) | `2ECEA0(부대, 행동)`: 부대 행동 쓰기(functions.md 3.5절). 군세 판단표 8곳에서 쓴다 | 코드 |
| CArmySetRetreatNode | `61C90` | 1개: 부대 | 부대가 자기 거점 칸 위(`2CB6C0`)이면 행동 `0xD` + 목표 `9`(`+0x48` 값), 아니면 `2EC570`(퇴각 명령 1) | 코드 |
| CGetMyselfArmyNode | `1FE00` | 1개: 출력 | 판단 주체(부대 트리)의 부대 객체를 변수에 넣는다(`B7100`) | 코드 |
| CClearRelayHexNode | `1F1A0` | 0개 | 판단 주체 부대의 경유 칸 5개를 `0xBD10`(없음)으로 지운다(`A3370` -> `2F05A0` 5회) | 코드 |
| CGetAttackTargetFootholdNode | `1FAA0` | 2개: 부대, 출력 거점 | 부대(`+0x26` 비트0 = 설정된 부대일 때) 현재 칸 반경 3 안(`2A9C90`)의 칸마다 지역의 거점을 구해, 그 거점 중심 칸과 칸이 같고 적대(`2C7400`)이며 거리(`2ACB80`)가 성 2·관문 3 이하(`거점 +0x4E < 0x34`면 성)인 거점을 내놓는다. 없으면 0 | 코드 |
| CSetRelayHexListNode | `6EE30` | 2개: 군세, HEX 목록 | 군세 `+0x18`의 u16 10칸을 `0xBD10`으로 지우고 목록 앞 10칸의 칸 번호(`22F830`)를 채운다. 정보 조회 Troops 항목 14가 읽는 곳 | 코드 |
| CGetArroundEnemyListNode | `7BA50` | 3개: 부대, 반경(상수), 출력 부대 목록(종류 3) | 부대 현재 칸 반경 안(`B9A00`)의 부대 가운데 판단 주체와 적대(`2CC630`)인 부대 목록 | 코드 |
| CGetUserArmyListNode | `80560` | 2개: 명령 번호(상수 4), 출력 부대 목록(종류 3) | 플레이어 세력(`world+0x871E8` -> `330B50`)의 부대 중 명령(`+0x37`)이 인수와 같고, 자기 거점 칸 위가 아니거나 `234DE0`이 거짓인 부대 목록 | 코드(`234DE0` 본문 미판독) |
| CGetSpecifiedArmyFlagArmyListNode | `7FC10` | 3개: 군세, 플래그 번호(0~3), 출력 부대 목록(종류 3) | 군세 소속 부대(`22BB50`) 가운데 부대 `+0x26`의 비트(플래그 0 비트0, 1 비트1(+자기 거점 칸 위가 아님), 2 비트2, 3 비트3)가 선 부대 목록 | 코드(비트의 뜻은 미확인) |
| CGetSpecifedStrategyDistrictTroopsNode | `3DDB0` | 2개: 군세 종류(상수, 판단표 17), 출력 군세 목록(종류 2) | 판단 주체 군단의 군세 중 종류(`+0x14`)가 인수와 같은 군세 목록. 이름의 「Strategy」는 종류 코드(rulebase.md 4절 표)를 뜻하는 것으로 보인다 | 코드(이름 풀이는 가설) |
| CRemoveNoInterceptPersonNode | `85810` | 1개: 무장 목록 | 요격 무장 후보 목록에서 걸러 새 목록으로 바꾼다. 남기는 조건(코드): 5능력 최대 실효값 `231770(…,0,0xFFF)` < 21 이거나, 사용 가능 진형 중 종류(`+0x7E`)가 1이고 비트1이 꺼졌으며 번호가 7이 아닌 진형이 있는 무장 | 코드(조건) / 가설(「요격 부적합」이라는 의미 해석) |
| CGetAdvantageOwnFootholdNode | `7B1B0` | 2개: 거점, 출력 수치 | 거점이 속한 주(`도시 +0xCE`)의 지방 이점 객체(`world+0xDC80`)의 이점 대상 거점 목록(`2AED70`) 가운데 소유 세력 번호(vcall `+0xB0`)가 판단 주체 세력 번호와 같은 거점의 개수를 낸다(이름의 「조회」는 수 반환). 판단 주체는 `B7100`·`B72F0`·`B7170`·`B7210` 모두에서 세력으로 환산 | 코드 |
| CExecuteAutoPaintDefenseNode | `69240` | 0개(판단 주체 = 군세) | 군세 종류 `0x17`(영역 방어)일 때: 목표 지역의 소유 세력이 군세 소유 세력과 같으면 종류를 0(임무 없음)으로 해제한다. 다르면 하드코딩된 지역 번호 표(`0xC2`, `0xEA`, `2`, `0xF6`, `0x1B`, `0xD1`, `0x2F`, `0x23`, `0x5D`, `8`…마다 거점·지역 번호 3개 조합)로 `70FB0`(군단의 종류 8~0xB·0x16 군세가 그 목표를 이미 노리는지 검사)을 두 번 확인해 둘 다 0이면 종류를 0으로 해제한다 | 코드(구조); 지역 표의 뜻과 `70FB0` 본문은 미판독 |
| CTroopsOrderDesutructionFacilityNode | `6F5F0` | 0개(판단 주체 = 군세) | 군세 종류 4(시설 공격, 목표 `+0x16` = 시설 번호)의 부대에 시설 파괴 이동 명령을 쓰는 실행 노드(2KB): `185710`(길찾기)·`2ECEA0`(행동 쓰기)을 부른다. functions.md 3.5·3.6절의 쓰기 지점(`6F5F0` -> 종류 4)과 일치 | 코드(호출 목록) / 가설(경로 선정 식 미판독) |
| CGetHexAroundFightingStrengthNode | `7EF50` | 6개 | 칸 주변 전투력 조회: functions.md 2.15 `7EF50`(D14)가 인수·동작을 정리했다 | 해당 문서 참조 |
| CCommandAutoPaintDefenseDepartureNode | `2CBC0` | 1개 | 성 자동 방어 출진: 위 「출진 노드의 보조 함수」 절과 functions.md 2.15 `28030`(D03)이 정리했다 | 해당 문서 참조 |

- 이 절의 「코드」는 디컴파일 본문과 판단표 인수 모양을 읽은 수준이고 호출 자리 바이트(E8)는 확인하지 않았다. 「가설」 줄은 최종 보고의 「강한 모델 검토 필요」 후보이며, 특히 4KB 이상 본문(`32D90`, `3A200`, `6D310`의 일부 항목)은 읽은 범위만 적었다.
- 부록 A 「군사」 표시 가운데 `CListRemoveFootholdNode`·`CListRemoveCautionTroopsNode`는 `84BC0` 한 본문을 공유한다(이 절 표에 한 줄로 묶음).
- 조사 중 확인: 경계군세 +0x1A는 `32E3B0`(번호 -> 거점)으로 거점 객체가 되므로 [unresolved.md](unresolved.md) 3-2절의 「CautionTroops 4 = 대장 무장 객체」와 충돌한다(같은 파일 3-3절에 정리).

## 더미 노드 `CMiscDummyNode`의 결과값 — 옛 의사코드 이름표가 거꾸로다 (2026-11-25, 지휘 세션, 확신도: 확정(바이트))

- **사실**: kind `0x13be7c11` `CMiscDummyNode`는 인수 하나를 결과로 돌려준다.
  - 인수 적재 vtable 칸 `456D0`은 `mov eax,[rdx]; mov [rcx+0x38],eax`(인수[0] → `+0x38`)다.
  - 실행 `85100`은 `xor eax,eax; cmp [rcx+0x38],1; setne al; inc eax; ret`이다. 즉 **인수 1이면 결과 1, 그 밖이면 결과 2**를 돌려준다.
  - vtable은 `1352990` 근처이고, 그 실행 칸이 `85100`이다.
- **결과 규약**: 선택 노드 `B2EB30`(자식 완료 처리)은 자식 결과 1이면 자기도 1로 끝낸다. 결과 2이면 다음 자식(vtable `+0x38` 진입 검사가 참인 것)으로 넘어가고, 다 실패하면 2다. 계획 노드도 성공 1 / 실패 2다(roles.md 7-1). 따라서 **결과 1 = 성공, 2 = 실패**다.
- **정정**: 옛 생성기 `AI_TacticsMod/research/AI_Analysis/all_behaviors/render_all_trees.py` 232행은 `'실패반환' if a[0]==1 else '성공반환'`로 적었다. 이것은 **거꾸로**다.
  - 의사코드 파일(`군단_전체_의사코드.txt`, `군세_전체_의사코드.txt`, `공격_신규와증원_의사코드.txt`, pseudo_군단_*.txt 등)의 「실패반환」은 실제로 **성공 반환**이고, 「성공반환」은 **실패 반환**이다.
  - 이 문서들을 근거로 한 해석(조건 → 「실패반환」을 「이 경우 탈락」으로 읽은 것)은 방향을 뒤집어 다시 읽어야 한다.
- **영향 노드 전수**(`origlib load_bt()`, kind `0x13be7c11`): 세력·부대 트리 0개, 군단 트리 23개(값 1이 20, 값 0이 3), 군세 트리 3개(모두 값 1). 군단 쪽은 요격 블록이 세 벌 복사돼 있다.

  | 트리 | 노드(값) | 부모 → 조부 | 뜻(정정 후) |
  |---|---|---|---|
  | 군단 | N1362(1)·N5153(1)·N8655(1) | 조건 op20 → 선택(1/2번째) | 조건이 참이면 선택이 성공으로 끝나 둘째 자식을 건너뜀 |
  | 군단 | N1366(0)·N5157(0)·N8659(0) | 순서 → 조건 op20 | 순서 맨 앞에서 실패를 돌려 그 순서 전체를 실패로 만듦 |
  | 군단 | N1586(1)·N5377(1)·N8879(1) | 조건 op19 → 선택 N1584 등(1/3) | 요격 동원 문턱 통과 시 성공, 셋째 자식(거점 목록 추가 `CListAddFootholdNode` + 변수 생성)을 건너뜀 |
  | 군단 | N1588(1)·N5379(1)·N8881(1) | 조건 → 같은 선택(2/3) | 위와 같은 구조의 둘째 통과 조건 |
  | 군단 | N1600(1)·N5391(1)·N8893(1) | 조건 op7 → 선택 N1598 등(1/2) | 조건이 참이면 플레이어 직할 대상 추가 제한(N1601~)을 건너뜀 |
  | 군단 | N1606(1)·N5397(1)·N8899(1) | 조건 → 선택(1/2) | 추가 제한 안의 통과 조건 |
  | 군단 | N1612(1)·N5403(1)·N8905(1) | 조건 → 순서(3/3) | 순서 끝 성공 |
  | 군단 | N3385(1)·N6867(1) | 순서 → 조건 | 조건이 참일 때 순서가 성공으로 끝남 |
  | 군세 | N173(1)·N218(1) | 조건 op23 → 반복(3/6) | 반복 안에서 조건이 참이면 성공. 반복 노드가 자식 결과를 어떻게 쓰는지(계속/중단)는 미확인 |
  | 군세 | N205(1) | 조건 op110 → 순서(5/6) | 순서 중간 성공 |

- **고칠 곳**: ai/roles.md 6-4절 1b항(D06)에 정정을 덧붙였다. `AI_TacticsMod/research/AI_Analysis/attack_decisions/군세방식8_결정로직.md`의 「반복 안의 실패 반환」(군세 N162~197)도 이 정정 대상이다. 옛 연구 문서는 읽기 전용 참고 자료라 고치지 않는다.
- 남은 것: 반복 노드(`CLoopListElementNode`, 실행 `59CD0`은 수집 방식 분기만 함)가 자식 결과 1·2를 받았을 때 계속하는지 끊는지. 군세 N173·N218의 뜻이 여기에 달려 있다.
