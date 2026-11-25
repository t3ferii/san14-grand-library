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
| 0x5551802c | CCommandExecutionDoctrinePanelAutoNode | 52FC0 | 52350(현 빌드 `522B0`=후보 목록 만들기 안쪽, 함수 시작점 아님) | same | 2 | 0 | 0 | 0 |  |
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
- `CDepartureNode` 인수 14개 가운데 `[6..10]` 정수 다섯이 `35A70`이 읽는 네 칸(`+0x50..+0x5C`)과 어떻게 짝지어지는지는 가설 A(`[6..9]` → `+0x50..+0x5C`, `[10]`은 칸 없음)로 채택했다(2026-11-25 3차 추적 실측; functions.md 2.15 `35A70` 행, ai/roles.md 6-4절 「출진 노드 인수」). 판단표 쪽 값은 요격 노드 N1789 `(2,1,1,2,1)`, N1790 `(2,0,1,2,1)`, 이동 N1837 `(1,0,0,1,0)`, 건설 N3380 `(1,1,1,1,0)`이다(origlib `Node.params[6:11]`).

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
- `84BC0`은 목록에서 값을 지우는 공통 본문(`[0]`=값, `[1]`=목록; 목록에 있으면 `21A350`이 머리부터 끝까지 돌며 **같은 값인 모든 항목을 제거**하고(다음 노드를 미리 저장, 남은 원소 순서 유지), 없어도 성공 1). 읽기 실패만 2이고 목록을 새로 만들지 않는다. 종류 코드 인수가 없어 두 클래스가 구분되지 않는다. 클래스 이름은 목록 종류별로 다르다 [Sonnet 판독 2026-11-25·미검증].
- **목록 풀·핸들·추가 규칙 [Sonnet 판독 2026-11-25·미검증, 코드]**: 모든 목록은 전역 풀 `DAT_1427d4130`의 ID별 이중 연결 목록이다(`+0x10` 머리 배열 `1427D4140`, `+0x18` 꼬리 배열, `+0x20` 빈 노드 자유 목록, `+0x28` ID별 개수표 `1427D4158`, `+0x30` 전체 개수, `+0x40` ID 한도; 노드 `+0x00` 원소 8바이트·`+0x08` 다음·`+0x10` 이전). 목록 변수는 16바이트 객체이고 `+0x08`이 가리키는 uint가 목록 ID이며, `+0x08`이 널이면 ID `0x14000`(널 목록 칸)을 쓴다. 변수가 없으면 추가·비우기 노드는 `1A250(키, 종류, …)`으로 새 목록을 만들어 변수에 쓰는데, 저장소에 `HeapListInfo` 변수가 없으면 아무것도 못 만들어 결과 2다. 종류 코드: 0 세력, 3 군세(부대), 4 무장, 5 거점, 6 지역, 7 칸, 0xB 경계군세, 0xE 정수 목록(별도 풀 `141B5F9E0`). **추가 `18D50(풀, ID, 플래그)`**: ID ≥ 한도이거나 자유 노드가 없으면 아무것도 안 하고(노드는 그래도 1), 플래그 ≠ 0이면 **꼬리 추가**, 0이면 머리 추가이며 `CListAdd…` 18종 모두 플래그 1(꼬리 추가)로 부른다. 따라서 머리부터 돌면 추가 순서와 같다(FIFO, 순번 0 = 가장 먼저 추가된 원소). `CListAdd…` 계열은 원소 값 8바이트를 널·유효 검사 없이 그대로 넣고(포인터 동일성이 정체성), 중복을 허용하며(`…Unique`는 머리부터 8바이트가 같은 항목이 있으면 추가 없이 1), 읽기 실패만 2이고 풀이 가득 차 추가가 안 돼도 1이다. `331780(원소)` 호출은 비Unique 추가 노드(거점 `81BF0`·칸 `82170`·세력 `81EB0`·지역 `81160`)에만 있고(추가 뒤 부르며 결과를 쓰지 않는다), Unique 노드(`81D30`·`822B0`·`81FF0`·`812A0`)와 부대·무장 추가 노드에는 없다(코드 확인, 지휘 세션 2026-11-25; 5차 정정, 출처 표시). `CListAddUniqueCautionTroopsNode`(`831A0`)만 목록 핸들 `+8`이 널이면 중복 조회 없이 무조건 추가한다(다른 Unique 노드는 널 핸들이면 ID `0x14000`을 조회). 제거 `189B0`은 앞뒤를 이어 붙이고 노드를 자유 목록으로 돌려 상대 순서를 유지하며, 전체 비우기 `186D0`은 체인 전체를 자유 목록에 붙이고 개수를 0으로 한다. 난수는 목록 노드 18종 모두 없다.

| 클래스 | 실행 RVA | 인수(판단표 실측) | 하는 일 한 줄 | 확신도 |
|---|---|---|---|---|
| CListAddFootholdNode / CListAddFootholdUniqueNode | `81BF0` / `81D30` | 2개: 거점, 목록(종류 5) | 거점 목록에 거점 추가(Unique는 중복 제외) (꼬리 추가·Unique는 중복이면 추가 없이 1) [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CListAddArmyNode / CListAddArmyUniqueNode | `81420` / `81550` | 2개: 부대, 목록(종류 3) | 부대 목록에 부대 추가(Unique는 중복 제외) (꼬리 추가·Unique는 중복이면 추가 없이 1) [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CListAddTroopsUniqueNode | `83020` | 2개: 군세, 목록(종류 2) | 군세 목록에 중복 없이 추가 | 코드 |
| CListAddHexNode / CListAddHexUniqueNode | `82170` / `822B0` | 2개: HEX, 목록(종류 7) | HEX 목록에 칸 추가(Unique는 중복 제외) (꼬리 추가·Unique는 중복이면 추가 없이 1) [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CListAddCautionTroopsNode / CListAddUniqueCautionTroopsNode | `816D0` / `831A0` | 2개: 경계군세, 목록(종류 0xB) | 경계군세 목록에 추가(Unique는 중복 제외) (꼬리 추가·Unique는 널 핸들이면 조회 없이 무조건 추가) [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CListAddTacticsBookNode | `82C70` | 2개: 전법서, 목록(종류 0x11) | 전법서 목록에 추가 | 코드 |
| CListRemoveCautionTroopsNode / CListRemoveFootholdNode | `84BC0` | 2개: 값, 목록 | 목록에서 값 제거(공통 본문, 위 「공통 모양」) (같은 값 모든 항목 제거, 항상 1(읽기 실패만 2)) [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CMiscSetFootholdEvaluationNode / CSetFormationEvaluationNode / CSetCautionTroopsEvaluationNode / CSetTacticsBookEvaluationNode / CMiscSetHexEvaluationNode | `6EFD0`(앞 4) / `85580`(HEX) | 2개: 대상 객체, 수치 | 대상 객체의 평가 점수(`+8`)를 저장 | 코드 |
| CListAddPossibleFacilityNode | `828A0` | 3개: 건설 주체(무장), 칸(HEX), 출력 목록(종류 0x10 시설 정의)(순서는 무장이 먼저; 5차 정정, [Codex 판독 2026-11-25·미검증] c9) | 시설 정의 표(`world+0x73958`부터) 가운데 `27A8D0`(건설 가능 최종 판정, functions.md)을 통과한 시설을 목록에 담는다. 이름은 「건설가능시설목록추가」 | 코드(`27A8D0` 인수 모양 확인; 후반의 `+0x1C`는 칸 지형 비트가 아니라 무장 소속 군단의 시설 허용 비트이고(플레이어 군단 허용 비트로 목록 포인터 제거), 칸 지형은 `+0x10`이다 — 5차 정정, [Codex 판독 2026-11-25·미검증] c9) |
| CGetFacilityCandidateHexListNode | `3A200` | 7개(`+0x38`~`+0x50`): 거점, 무장, 시설 종류, 출력 HEX 목록(종류 7), 변수 2개, 수치 1개 | 시설을 지을 칸 후보 목록 조회(8KB; 판단표 N3387: 무장 `검사중인무장`, 시설 종류 4). 인수 실제: `[0]` 대상 **지역**(중심 칸 `+0x3A` 사용), `[1]` 무장, `[2]` 시설 종류 n(`BB500` → 정의, 정의 `+0x2C` 계열 1/2/3), `[3]` 출력 칸 목록, `[4]` 거점 후보 컨테이너, `[5]` 시설 정의 대체 포인터(유효한 객체가 읽히면 `[2]`로 얻은 정의를 덮어씀; 거점 목록 변수가 아님 — 5차 정정, [Gemini 판독 2026-11-25·미검증] g49·[Codex 판독 2026-11-25·미검증] c14), `[6]` 수치(0이면 아래 A 갈래 허용). **골격(2026-11-25 3차)**: (A) 대상 지역이 무장 소속 거점(`+0xE2`)의 진입 지역(도시 `+0xB0`)이 아니고 `[6]`==0이면, 대상 지역(소속 거점 지역 `22B880`이면 인접 지역 `230AF0`까지)의 칸(`233850`)에서 이미 있는 건축물의 정의 계열을 세고, 정의 계열 3이면 반경(`2A9C90`) 안 같은 계열 시설이 없는 건설 가능(`27A8D0`) 칸을, 계열 2이고 `2345D0(정의,1)`이면 반경 1로 같은 일을 해 담는다. (B) 그 밖: 기점 = 소속 거점의 진입 지역이 대상이면 위협 거점(도시 `+0xA8`), 아니면 소속 거점 100칸 안(`2ACB80` < 0x65) 적대(`2CC630`) 도시 중 병력 `+0x3C` 최대, 또는 `[4]` 후보 중 대상 지역 중심에 가장 가까운 거점. 대상 지역 칸 중 칸 `+0x10`이 2·0xE이고 `27A8D0` 통과한 칸을 모은 뒤 기점에서 대상 지역으로 `185710` 경로를 내어 고른다. 토석벽 칸 `7CB80`과 같은 기점 규칙. **B 갈래 경로 이후 [Sonnet 판독 2026-11-25·미검증]**: `[6]`은 수치이자 **경로 방향 플래그**다(0이면 시작 = `22F190(기점 거점)`·목표 = 지역 중심 칸, 0이 아니면 반대; 호출 `185710(&경로, &결과정보, 시작, &목표, 1, 1, 2)`). 경로 실패(0)이면 결과 2, 아니면 후보가 0개여도 1. ① 후보 수집(경로 전, `233850` 칸 순회 순): 칸 `+0x10`이 2 또는 0xE(제한 플래그 켜졌을 때만)이고 `27A8D0`(건설 가능)≠0인 칸을 후보 C에 추가. ② 진입 칸 E = 경로를 **앞(첫 칸)부터** 훑어 칸 `+0x12`(소속 지역)가 대상 지역 번호(`22F470`)와 처음 같아지는 칸(없으면 없음). ③ 정렬(안정 삽입 정렬, 마지막이 최우선): (a) 정의 `+0x2C`==3이면 `23BE0` — 지형 비용(`2304F0` → `world+0x73860` → `BF1B0`) `before(X,Q) = (X의 칸 종류==2 && Q의 종류≠2) || 비용(X) < 비용(Q)`(부호 있는 정수 비교; 「종류 2 우선 뒤 비용」 사전식 정렬이 아니고 양방향이 모두 참일 수 있어 엄격 순서·안정성이 보장되지 않으며, 같은 종류·같은 비용은 순서 유지 — 5차 정정, [Codex 판독 2026-11-25·미검증] c14), (b) E가 유효하면 `23EF0` — `2ACB80(후보, E)` 거리 오름차순(`<`, 동점은 앞선 것 유지). 동점은 (a) → 수집 순서. ④ 재필터: 후보마다 `27A8D0`을 한 번 더 불러 0이면 제거(숨은 인수는 추정). ⑤ 출력: C를 앞에서 뒤로 돌며 **지역 중심 칸(`22B8E0(h)+0x3A == h`)은 제외**하고 출력 목록에 추가. 난수 없음 | 코드(골격·경로 이후 고르기) / 추정(`23BE0` 종류 2 우선, 재필터 검사 내용) |
| CGetPersonFormationParamNode | `7F5E0` | 4개: 무장, 평가 종류(판단표 값 3), 출력 진형 객체, 출력 점수 | 무장이 쓸 수 있는 진형(`233CF0`) 20종마다 `C00E0(무장, 진형, 평가 종류)` 점수를 구해 최고 점수 진형과 그 점수를 내놓는다 | 코드 |
| CGetFormationNode | `7EEE0` | 2개: 진형 번호(상수), 출력 객체 | 진형 표(`world+0x77430`부터)에서 번호의 진형 객체를 꺼낸다(`BE040`; 0번·6번·17 이상·음수는 없음(0 반환). 표 배열 인덱싱이 아니라 명시적 `if` 분기 매핑이라 9~11은 `world+0x77480~+0x77490`, 12~14는 `+0x77468~+0x77478`, 15~16은 `+0x774C0~+0x774C8`의 비연속 오프셋을 읽는다) | 코드 (5차 정정, 출처 표시: [Gemini 판독 2026-11-25·미검증] g48) |
| CSelectPersonTacticsNode | `85BE0` | 3개: 무장, 진형, 출력 전법 목록(종류 0xD) | 전법 최대 3개를 골라 담는다: 전법 표(200종)에서 `235090` 참·무장 보유(`93770`)·진형 허용 비트(`+0x6C`)를 만족하는 것을 먼저, 부족하면 무장의 전법 칸 10개(`22BD60`)에서 진형 허용인 것을 채운다. 출진 명령 전법 3칸(`D3C70`, functions.md D04)의 입력 | 코드 |
| CGetBuildingDestructionDataNode | `370D0` | 2개: 출력 무장 목록(종류 4), 출력 지역 목록(종류 6) | 판단 주체 군단의 건물 파괴 계략용 자료 생성: 실행 무장 후보 `6DD230`과 대상 지역 후보 `6E08E0` | 코드(두 보조 함수 본문은 미판독) |
| CCommandExecutionBuildingDestructionNode | `52EC0` | 3개: 세력(읽기만 하고 이후 미사용), 무장, 지역(5차 정정, [Codex 판독 2026-11-25·미검증] c9) | 계략 명령 종류 `0x14`(건물 파괴, rules_diplomacy.md 5.4)의 명령 구조체를 채워 `1FA5C0`으로 실행. 투입량 `1E0110`은 금 상한이 아니라 군단 `+0x24`(군정) 투입량(5차 정정, [Codex 판독 2026-11-25·미검증] c9) | 코드(명령 번호는 상수 `0x14` 직접 확인) |
| CCommandExecutionDualDestructionNode | `53270` | 4개: 군단 등 객체 4개 | 명령 종류 `10`의 구조체를 채워 `1FA5C0` 실행. 조건 79 `이호경식명령가능`이 이 노드의 하위(conditions.md)이므로 이호경식 실행 노드로 읽힌다. **실행 무장의 군단**(`40C20`: 무장 `+0xE0` → `world+0xE0D0`) `+0x14`(명령서)가 임계값(`DAT_141A4B740`) 이상일 때만 실행(거점 `+0x14`가 아님). 인수 4개(`+0x38` 유효성만, `+0x3C` 실행 무장, `+0x40` 대상 A, `+0x44` 대상 B) 전부 유효해야 한다. 구조체 {종류 10, 실행 무장, 대상 A, 비용 `1E0110`, 대상 B} → `1FA5C0(S, 0)`이 명령 객체(0x80B)를 만들어 명령 관리자에 등록하고 `1F8AE0`이 채우며 무장 `+0x15E |= 1`, 군단 `+0x14 = clamp(명령서 − 종류별 비용, 0, 200)`, 군단 자금 감소를 쓴다. 비용 `1E0110` = 군단 자금 F × 40/100 (종류 10)을 `1E2EF0` 상한과 비교한 최솟값, [0,F] 클램프. 반환 1 = `1FA5C0`까지 감(안에서 등록 실패해도 1), 2 = 인수 무효 또는 명령서 부족. 효과(적 사이 이간)는 완료 시점 처리로 추정. 난수·정렬 없음(직접 호출 기준) [Sonnet 판독 2026-11-25·미검증] | 코드(종류 10·노드 본문) / 가설(이름 = 이호경식, 효과 시점) |
| CCommandExecutionAttackRequestNode | `52CA0` | 5개: 세력 T(요청받는 쪽), 무장 W(사자), 대가 종류 k(0 금·1 군량·2 명품·4 지역), 대가 값(k=0·1 정수, k=2·4 객체), 목표 거점 B(5차 정정, [Codex 판독 2026-11-25·미검증] c9; 옛 「군단, 거점, 선택값, 무장, 값」 표기와 다름) | 외교 명령 종류 `9`(공격 요청, rules_diplomacy.md 3.5)의 구조체를 채운다. 요청받는 세력 T의 군단(`230270(T)`; 인수로 받은 군단이 아님) `+0x14`가 임계값(`DAT_141A4B668`) 미만이면 실패(5차 정정, [Codex 판독 2026-11-25·미검증] c9). 선택값 0/1/2에 따라 `[4]`가 수치(+0x68 또는 +0x64)나 객체(+0x70)로 쓰인다 | 코드(종류 9); 선택값별 구조체 칸 의미는 미판독 |
| CAttackRequestSuccessConditionNode | `7AC40` | 7개(`+0x38`~`+0x50`) | **플레이어 세력에 보내는 동맹 공격 요청의 대가 지불 가능 검사**(2026-11-25 3차, 판단표 N3113 → N3114 `동맹공격요청명령`). 인수: `[0]` 요청 받는 세력(= 플레이어 세력이어야 함, 아니면 2; N3078 `플레이어세력조회`로 채움), `[1]` 사자 무장, `[2]` 대가 종류(0 금, 1 군량, 2 명품; N3108 `외교우선조건선택`), `[3]` 출력(대가 양 또는 명품 객체; N3113 `보조값0349`), `[4]` 목표 거점(N3113 `보조값0562` 객체종류 5, `9DB10` 마지막 인수; 4차 정정 — 3차는 [3]·[4]를 거꾸로 적음), `[5]`·`[6]` 금·군량 남길 양(군주 소재 거점 정보 39·38; 0 이하이면 보유량에 더해 해석). `9DB10(요청 세력, …)`이 요구량을 내고 종류 0·1이면 `230350(요청 세력)` 객체의 금(vcall `+0x90`)·군량(`+0xA0`) − 요구량 > 남길 양일 때 성공하며 요구량을 출력, 종류 2는 명품 표(`world+0x77B18`[202])의 항목을 출력 | 코드 |
| CCommandTransportDepatureNode | `32D90` | 5개: 출발 거점 목록, 도착 후보 거점 목록, 값 3개(판단표 `수송출진명령`) | 수송 출진 명령 작성(10KB). 3차(2026-11-25) 판독: 도착 후보를 `21840`(비교 `25BF0`) 뒤 `219A0`(비교 `25CE0`, 군량 20000 미만 우선)로 정렬하고, 공급 거점을 `216E0`(비교 `25B10`, 거리)으로 고른다(정렬 함수와 비교 함수 대응은 코드 확인, 지휘 세션 2026-11-25). 이어 `201C20` 호출 뒤 군세 `+0x14 = 0xC`·`+0x16 = 목표 거점 번호`를 직접 쓴다. 인수 `[0]` 출발(공급) 후보 목록, `[1]` 도착 후보 목록, `[2]`~`[4]` 최소 잔류 군량·금·병사 기준(5차 정정, [Gemini 판독 2026-11-25·미검증] g47) — ai/roles.md 2-3-6 | 코드(ai/roles.md 2-3-6) |
| CGetTransportSoldierNode | `804F0` | 4개: 거점 목록, 상수 3개(판단표 24, 6, 6) | 목록의 각 거점마다 `9F410`(필요량)을 계산해 거점 `+0x90`에 부호 있는 수송 병력 값을 저장(`D3A90`) | 코드(저장 위치); 부호 의미는 미판독 |
| CGetAllFootholdNeedFoodNode | `7B450` | 4개: 군단, 상수 3개(24, 6, p4). 세 번째 상수 p4는 6만이 아니라 N13 6·N15 4·N17 8(5차 정정, [Sonnet 판독 2026-11-25·미검증] s8) | 군단 소속 세력의 거점 전부에 `9F410(거점, …)`으로 필요 군량을 계산해 거점 `+0x94`에 쓴다(정보 조회 Foothold 항목 38이 이 값을 읽는다: `8B190` case 0x26) | 코드 |
| CCGetAllFootholdNeedMoneyNode | `7B590` | 2개: 군단, 상수 p2(6·4·8: N20 6·N22 4·N24 8; 대도서관의 「6 또는 4」에 8이 빠짐, 5차 정정, [Sonnet 판독 2026-11-25·미검증] s8) | 같은 방식으로 필요 금(`9F670`)을 거점 `+0x98`에 쓴다(항목 39) | 코드 |
| CGetMyselfTroopsNode | `6E760` | 1개: 출력 | 판단 주체(군세 트리)의 군세 객체를 변수에 넣는다(`B72F0`) | 코드 |
| CGetMyselfTroopsInfoNode | `6D310` | 2개: 항목 번호, 출력 | 판단 주체 군세의 정보 조회(getter, 5KB). 항목 0 군세 번호, 1 종류(`+0x14`), 2·3 소속 부대 목록, 4 목표 객체(종류 `+0x14`별로 거점·지역·시설·경계군세 표를 골라 `+0x16`으로 변환), 6 객체 번호(`+8`), 7 소속 군단, 10 병사 합(부대 `+0x16`), 13 전력 합(`B6F50`), 14 경유 HEX 목록(`+0x18` u16[10]), 15 소유 세력(`22E560`) | 코드(전 항목, 2026-11-25 3차): 대장 = 소속 부대 중 능력 0(`231770(무장,0,0xFFF)`) 최고 부대의 대장(`58D90`). 5 = 병사 합 S(부대 `+0x16`) + S × `DAT_141A4AFD8` × 대장 적성 `+0x16A` / 10000(세력정보 4와 같은 상수), 8 = 금 합(부대 `+0x5C`), 9 = 군량 합(부대 `+0x60`), 11 = 군량 합 F − F × 대장 적성 `+0x170` × `DAT_141A4AFFC` / 10000, 12 = F − F × 대장 적성 `+0x172` × `DAT_141A4B008` / 10000(상수 `141A4AFD8`·`AFFC`·`B008` = EXE 초기값 150, 직접 쓰기 xref 없음; 4차) |
| CVariableGetCautionArmyInfoNode | `88140` | 3개: 경계부대 항목, 항목 번호(상수), 출력 | 경계부대(`CCautionArmy`; 표 `world+0x81B50` 간격 0x18) 정보: 0 항목 번호(`22F4F0`), 1 그 부대 전력(`B6F50`), 2 관련 거점(`+0x12`, `32E3B0`), 3 적 부대(`+0x10` 번호 -> 부대 표), 4 `+8` 정수 | 코드 |
| CCautionArmyAddUniqueNode | `283F0` | 3개: 적 부대, 거점, 출력 경계부대 목록(종류 0xF) | 적 부대가 목록에 이미 있으면 성공만 하고, 없으면 빈 경계부대 칸(`world+0x81B50` 표)에 (부대 번호 `+0x10`, 거점 번호 `+0x12`, 상한 0x3D)을 채워 목록에 넣는다. 부대가 자기 거점 칸 위이면 실패, 거점 소유 세력이 판단 주체와 다르면 `26D660`(외교 관계)을 통과해야 한다 | 코드 |
| CCautionTroopsListAddNode | `28D20` | 4개: 경계군세 목록(종류 0xB), 부대 목록, 대상 거점, 값 | 새 경계군세를 만든다: 빈 칸(`world+0x80BA8` 표, 간격 0x48)을 잡아 부대 목록을 복사하고 대상 거점(`+0x1A`, 상한 0x3D), 번호(`+0x18` = 목록 안 안 쓴 최소 번호), 소속 군단(`+0x14` = 판단 주체 군단 번호)을 쓴다. 부대가 이미 다른 경계군세에 있으면 실패(2) | 코드 |
| CCautionTroopsListAddUniqueNode | `29190` | 3개: 경계군세 목록, 순번(수치), 부대 | 목록의 순번째 경계군세의 소속 부대 목록(`+0x30`)에 부대를 중복 없이 추가 | 코드 |
| CCautionTroopsRemoveNode | `29990` | 2개: 경계군세, 부대 | 경계군세의 소속 부대 목록(`+0x30`)에 부대가 있으면 `+0x28` 쪽 목록에서 제거 | 코드(두 목록의 관계 미확인) |
| CCautionTroopsListRemoveNullUnit | `29390` | 1개: 경계군세 목록 | 각 경계군세의 소속 부대 가운데 유효하고 명령(`+0x37`)이 `0xB`·`0xC`(퇴각)가 아닌 부대만 남기고, 부대가 하나도 안 남은 경계군세는 `32D180`(삭제)로 지운다 | 코드 |
| CCautionTroopsClearNode | `28CC0` | 1개: 경계군세 | 경계군세를 삭제(`32D180`, functions.md T01) | 코드 |
| CCautionTroopsSortNode | `29A90` | 1개: 경계군세 객체 하나(목록이 아님 — 5차 정정, [Gemini 판독 2026-11-25·미검증] g48·[Codex 판독 2026-11-25·미검증] c14) | 그 경계군세 하나의 적 부대 목록(`+0x28`)을 헬퍼 7개로 연속 정렬(반환 1, 인수 읽기 실패 시 2, 난수 없음). 키: ① 대장 무장 번호 ② 무장 `+0xEA` ③ 능력 1 ④ 능력 0 ⑤ 대장 `+0xE7`로 고른 `world+0x784F8` 표 항목 비교(`259D0`) ⑥ 대장 소속 군단(`22D3C0`) ⑦ 부대 세력의 군주 번호(`230400(22E2A0)`) — ai/roles.md 2-3-4. **방향·안정성**: ① `22D30`/`22DB0`은 오름차순·안정 삽입 정렬이고 마지막에 건 정렬이 최우선 키다 — 확정(코드, 지휘 세션 대조 2026-11-25). ②③④ **내림차순**(5차 정정, 코드 확인 — 지휘 세션 2026-11-25: ① `22DB0`은 `key(X) < key(prev)`이면 X를 앞으로(오름), ② `23500`·③ `23730`·④ `23290`은 `key(prev) < key(X)`이면 X를 앞으로(내림), 모두 `≤`에서 멈추는 안정 삽입; 첫 판독 Codex c14. 앞 차수의 「오름차순」은 틀림), ⑤ **내림차순**(`259D0(a,b) = key(b) < key(a)`), 모두 안정 삽입 정렬 [Sonnet 판독 2026-11-25·미검증]. ⑥⑦은 정렬이 아니라 **조건 분할 이동**(⑥ 대장 소속 군단의 `+0x12` == 부대 `+0x12`, 즉 군단장이 대장인 부대를 목록 앞으로 / ⑦ 대장이 군주 번호와 같은 부대를 앞으로)이며, 만족 원소끼리의 순서는 뒤집힐 수 있다(추정). 합성 순서: 앞 = 군주가 대장인 부대(⑦) → 군단장이 대장인 부대(⑥) → ⑤ 값 내림차순 → ④ 능력 0 내림 → ③ 능력 1 내림 → ② `+0xEA` 내림 → ① 무장 번호 오름 | 코드(①~④ 방향 확정, ⑤ 키·방향·안정성) / 추정(⑥⑦ 만족 원소 간 순서, ⑤ 키의 뜻) |
| CCautionTroopsUpdateStatusNode | `29B40` | 2개: 경계군세, 상수(1) | 경계군세 `+0x3C` = (인수 == 1). 경계군세 정보 항목 3(`+0x3C`)이 읽는 상태 값 | 코드 |
| CSetCautionTroopsVirtualTargetFootholdNode | `85F70` | 2개: 경계군세, 거점 | 경계군세 `+0x1A` = 거점 `+0x4E`(상한 0x3D). 정보 항목 4가 읽는 값(unresolved.md 3-2절 충돌 표시 참고) | 코드 |
| CArmySetArmyActionNode | `61B10` | 2개: 부대, 행동 번호(상수 1~3) | `2ECEA0(부대, 행동)`: 부대 행동 쓰기(functions.md 3.5절). 군세 판단표 8곳에서 쓴다 | 코드 |
| CArmySetRetreatNode | `61C90` | 1개: 부대 | 부대가 자기 거점 칸 위(`2CB6C0`)이면 행동 `0xD` + 목표 `9`(`+0x48` 값), 아니면 `2EC570`(퇴각 명령 1) | 코드 |
| CGetMyselfArmyNode | `1FE00` | 1개: 출력 | 판단 주체(부대 트리)의 부대 객체를 변수에 넣는다(`B7100`) | 코드 |
| CClearRelayHexNode | `1F1A0` | 0개 | 판단 주체 부대의 경유 칸 5개를 `0xBD10`(없음)으로 지운다(`A3370` -> `2F05A0` 5회) | 코드 |
| CGetAttackTargetFootholdNode | `1FAA0` | 2개: 부대, 출력 거점 | 부대(`+0x26` 비트0 = 설정된 부대일 때) 현재 칸 반경 3 안(`2A9C90`)의 칸마다 지역의 거점을 구해, 그 거점 중심 칸과 칸이 같고 적대(`2C7400`)이며 거리(`2ACB80`)가 성 2·관문 3 이하(`거점 +0x4E < 0x34`면 성)인 거점을 내놓는다. 없으면 0 | 코드 |
| CSetRelayHexListNode | `6EE30` | 2개: 군세, HEX 목록 | 군세 `+0x18`의 u16 10칸을 `0xBD10`으로 지우고 목록 앞 10칸의 칸 번호(`22F830`)를 채운다. 정보 조회 Troops 항목 14가 읽는 곳 | 코드 |
| CGetArroundEnemyListNode | `7BA50` | 3개: 부대, 반경(상수), 출력 부대 목록(종류 3) | 부대 현재 칸 반경 안(`B9A00`)의 부대 가운데 입력 부대 `[0]`의 세력(`22E690`)과 주변 부대의 세력을 `2CC630`에 넘겨 적대인 부대 목록(판단 주체와 비교하는 것이 아님) | 코드 (5차 정정, 출처 표시: [Gemini 판독 2026-11-25·미검증] g47) |
| CGetUserArmyListNode | `80560` | 2개: 명령 번호(상수 4), 출력 부대 목록(종류 3) | 플레이어 세력(`world+0x871E8` -> `330B50`)의 부대 중 명령(`+0x37`)이 인수와 같고, 자기 거점 칸 위가 아니거나 `234DE0`이 거짓인 부대 목록 | 코드(`234DE0` 본문 미판독) |
| CGetSpecifiedArmyFlagArmyListNode | `7FC10` | 3개: 군세, 플래그 번호(0~6, 판단표 사용은 6), 출력 부대 목록(종류 3) | 군세 소속 부대(`22BB50`) 가운데 부대 `+0x26`의 비트(플래그 0 비트0, 1 비트1(+자기 거점 칸 위가 아님), 2 비트2, 3 비트3, 4 비트4(`0x10`), 5 비트5(`0x20`), 6 `2CB6C0==0`이고 비트1 꺼짐; `case`마다 `break`가 없어 0~5는 아래 `case`로 fall-through)가 선 부대 목록 | 코드(비트의 뜻은 미확인) (5차 정정, 출처 표시: [Gemini 판독 2026-11-25·미검증] g48) |
| CGetSpecifedStrategyDistrictTroopsNode | `3DDB0` | 2개: 군세 종류(**정수 직접값**, 판단표 17), 출력 군세 목록(`world+0x7F8D8` 슬롯 501개를 주소 오름차순으로 훑어 판단 군단 소속이고 `+0x14`==종류인 군세를 추가, 정렬·중복 제거 없음, 비어도 1, 군단 무효·목록 확보 실패 2 [Codex 판독 2026-11-25·미검증])(종류 2) | 판단 주체 군단의 군세 중 종류(`+0x14`)가 인수와 같은 군세 목록. 이름의 「Strategy」는 종류 코드(rulebase.md 4절 표)를 뜻하는 것으로 보인다 | 코드(이름 풀이는 가설) |
| CRemoveNoInterceptPersonNode | `85810` | 1개: 무장 목록 | 요격 무장 후보 목록에서 거른다. **제거** 조건: 통솔(능력 0, `231770(…,0,0xFFF)`) < 21이거나, 진형 번호 i=1..19 중 `233CF0` 참이고 진형 유효·`+0x7E`==1·비트1 꺼짐·번호 ≠ 7인 것이 하나도 없는 무장. 이런 무장을 임시 목록에 모은 뒤 원목록에서 `21A350`(같은 포인터 모두)으로 지운다(남은 원소 순서 유지, 정렬·난수·쓰기 없음). 옛 서술 「남기는 조건: 5능력 최대 < 21 …」은 방향과 능력 종류를 잘못 읽었다 | 확정(코드, 지휘 세션 대조 2026-11-25; Codex c7) / 가설(「요격 부적합」이라는 의미 해석) |
| CGetAdvantageOwnFootholdNode | `7B1B0` | 2개: 거점, 출력 수치 | 거점이 속한 주(`도시 +0xCE`)의 지방 이점 객체(`world+0xDC80`)의 이점 대상 거점 목록(`2AED70`) 가운데 소유 세력 번호(vcall `+0xB0`)가 판단 주체 세력 번호와 같은 거점의 개수를 낸다(이름의 「조회」는 수 반환). 판단 주체는 `B7100`·`B72F0`·`B7170`·`B7210` 모두에서 세력으로 환산 | 코드 |
| CExecuteAutoPaintDefenseNode | `69240` | 0개(판단 주체 = 군세) | 군세 종류 `0x17`(영역 방어)일 때: 목표 지역의 소유 세력이 군세 소유 세력과 같으면 종류를 0(임무 없음)으로 해제한다. 다르면 하드코딩된 지역 번호 표(`0xC2`, `0xEA`, `2`, `0xF6`, `0x1B`, `0xD1`, `0x2F`, `0x23`, `0x5D`, `8`…마다 거점·지역 번호 3개 조합)로 `70FB0`(군단의 종류 8~0xB·0x16 군세가 그 목표를 이미 노리는지 검사)을 두 번 확인해 둘 다 0이면 종류를 0으로 해제한다 | 코드(구조); 지역 표의 뜻과 `70FB0` 본문은 미판독 |
| CTroopsOrderDesutructionFacilityNode | `6F5F0` | 0개(판단 주체 = 군세) | **군세 종류 7에서 호출되어 종류 4(시설 공격)로 바꾸는** 노드(판단표 N254 → N256; 진입 시 종류 4 검사는 없다): 구성 부대 목록 비면·대표 부대 진형 7·병력 ≤ 999이면 2, 대표 무장 거점까지 `185710` 경로가 지나는 지역 중심 칸 중 군세 세력 소유 지역의 시설(종류 ≠ 1·2, 소유·칸 소유가 군세 세력과 다르고 `2CC630` 적대, 정의 `+0x2C` ∉ {1,3,4})을 고르되 시설 반경 5칸에 적대 부대가 하나라도 있으면 탈락하고, **적합 시설을 찾아도 바깥 지역 순회는 계속해 뒤 지역의 적합 시설이 선택을 덮어쓴다**(내구·거리·공격력 비교 없음, 시설 번호 0·범위 밖 칸을 만나면 선택이 있는 상태에서는 그 지역 칸 루프 중단). 쓰기: 군세 `+0x14=4`, `+0x16=시설 번호`, 구성 부대마다 `2ECEA0(부대,6)`·`2ECF00(부대,11,시설 번호)`(`+0x140==0`일 때만), 경유점·`26E260`·내구 직접 감소 없음 [Codex 판독 2026-11-25·미검증]. 이전 서술: `185710`(길찾기)·`2ECEA0`(행동 쓰기)을 부른다. functions.md 3.5·3.6절의 쓰기 지점(`6F5F0` -> 종류 4)과 일치 | 코드(호출 목록) / 가설(경로 선정 식 미판독) |
| CGetHexAroundFightingStrengthNode | `7EF50` | 6개 | 칸 주변 전투력 조회: functions.md 2.15 `7EF50`(D14)가 인수·동작을 정리했다. `2A9C90` 호출 뒤 중심 칸이 목록에 없으면 꼬리에 직접 추가하므로 반경 칸 목록은 **중심 칸을 포함**한다(5차 정정, 코드 확인 — 지휘 세션 2026-11-25: `18D50(풀, 목록, 1)`로 더함; 첫 판독 Gemini g47. `2A9C90` 자체는 중심 제외) | 해당 문서 참조 |
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
- 남은 것: 반복 노드(`CLoopListElementNode`, 실행 `59CD0`은 수집 방식 분기만 함)가 자식 결과 1·2를 받았을 때 계속하는지 끊는지. 군세 N173·N218의 뜻이 여기에 달려 있다. (부분 답, [Sonnet 판독 2026-11-25·미검증]: 반복 함수는 원소마다 자식을 실행한 직후 `IsLoopBreak`만 검사하고, 자식 결과 1·2의 구분은 이번 판독 범위 밖이다. `CMiscBreakNode` 행 참조.)

## 「내정·기타」 표시 노드 한 줄 설명 (2026-11-25, 조사 목록 N05)

조사 목록 부록 A의 「내정·기타」 99종. 대부분 범용 변수·목록 노드와 내정·인사·외교·계략 실행 노드라 군단 출진·야전 판단(새 전투 DLL 범위) 밖이다. 확신도 「이름」은 RTTI 클래스 이름과 판단표 쓰임 수(세력/군단/군세/부대)만으로 쓴 것이고 실행 본문은 읽지 않았다. 「문서 참조/쓰임」은 다른 절·문서에서 본문 또는 판단표 쓰임을 확인한 것이다. 실행 RVA가 같은 클래스(`6EFD0`·`84BC0`·`85580`)는 객체 종류만 다른 공용 함수다.

**변수·기타 노드 공통 규칙 [Sonnet 판독 2026-11-25·미검증, 코드]**: 문맥 `1137FF0(ctx)` = `*(ctx+0x18)` = 변수 저장소(블랙보드). 노드 인수는 `+0x38`부터 4바이트씩([0]=`+0x38`, [1]=`+0x3C`, …). 저장소 항목은 0x30바이트(키 int `+0x00`, 값 8바이트 `+0x10`, 종류 태그 `+0x20` = 1 객체/포인터, 2 정수). 정수 읽기 `B28BB0`는 키가 같은 첫 항목의 태그가 2일 때만 하위 4바이트를 돌려주고(객체로 저장돼 있으면 실패 → 노드 결과 2), 객체 읽기 `B28D20`은 태그 1일 때만 성공한다. 정수 쓰기 `B29250`·객체 쓰기 `B29460`은 저장소 `+0x18` 바이트 플래그가 0이 아니면 같은 키의 첫 항목을 덮어쓰고(종류도 바뀜) 없으면 끝에 추가하며, **플래그가 0이면 항상 끝에 추가**(읽기는 첫 항목이므로 갱신이 안 보임; 플래그 값은 **1(덮어쓰기)**: 판단표 파일 `bt_exce.bin` 4개 구역·`bt.bin` 4개 구역의 `IBBG` 청크 헤더 `+0x10` 바이트가 모두 1이고 `B28E90`이 이를 저장소 `+0x18`로 복사하는 체인(서식 → 인스턴스 `B29DF0`)과 일치. 실행 중 메모리로는 미확인이고 이 바이트가 청크 개수 필드와 겹쳐 보이는 점이 걸린다 [Sonnet 판독 2026-11-25·미검증, s2 Q2]). 노드 결과 = 쓰기 성공 1 / 실패 2. 산술은 모두 32비트 `int`(2의 보수 래핑, 포화 없음)이고 실수·난수는 이 표의 변수 노드에 없다. 키 해시 `B293C0(ctx, "문자열", 값)`: h=1에서 문자마다 `h *= 31` 후 `key += (signed char)c × h`, 그 키로 정수 쓰기.

| 클래스 | 실행 RVA | 쓰임 세력/군단/군세/부대 | 한 줄 설명 | 확신도 |
|---|---|---|---|---|
| CVariableMultiValueNode | `92130` | 4/228/0/1 | `v = 상수 × v`(int32 곱, 래핑, 포화·반올림 없음). 읽기·쓰기 실패 2 [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CVariableCreateNode | `864B0` | 21/754/11/2 | `[0]` 키에 정수 `[1]`(상수)을 쓴다(int32 → 8바이트 칸 zero-extend, 읽을 때 하위 4바이트). 쓰기 실패 2 [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CVariablePlusValueNode | `92270` | 9/230/0/0 | `[0] = [0] + 상수`(int32 래핑, 읽기·쓰기 실패 2) [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CListGetItemByIndex | `83DE0` | 4/215/0/4 | 인수 [0] 목록 종류, [1] 목록 변수, [2] **인덱스 정수 변수 키**, [3] 결과 키. 머리부터 0 기준 순번이 인덱스와 같은 첫 노드의 원소를 결과 키에 쓴다(순번 0 = 가장 먼저 추가된 원소, 정렬했다면 정렬 결과 첫 원소). **인덱스가 범위 밖이거나 음수면 결과 키에 객체 0을 쓰고 2**, 인덱스·목록 변수 읽기 실패·코드 0~0x12 밖도 2. 종류 0xE는 정수 목록에서 4바이트 정수를 정수로 쓴다. 종류 0xB의 결과 쓰기는 디컴파일에 8바이트 값이 아니라 스택 임시 변수 주소를 넘기는 것으로 보인다(추정: 아티팩트 또는 원본 결함, 바이트 확인 필요) [Sonnet 판독 2026-11-25·미검증] | 코드(0xB 쓰기는 추정) |
| CListSortEvaluationNode | `84CB0` | 4/214/0/2 | 인수 [0] 목록 종류(0~0xD·0xF~0x12, **0xE 미지원 → 2**), [1] 목록 변수, [2] **방향 상수**(변수 키 아님). `23D40`이 연결 목록 제자리 **안정 삽입 정렬**: 키 = 원소를 포인터로 보아 `*(int32*)(원소+8)`(평가점수, 부호 있는 32비트; `평가점수 저장` 노드 `6EFD0`·`85580`이 쓰는 값), 비교 `98450` 엄격 부등호 — **[2]==0이면 오름차순(작은 값 먼저), [2]≠0이면 내림차순(큰 값 먼저)**, 동점은 기존 상대 순서 유지. 읽기 실패 2(목록을 새로 만들지 않음), 널 핸들이면 아무것도 안 하고 1. 원소가 평가 객체인지는 검사하지 않는다. 판단표에서 [2]의 실제 사용 값 분포는 미확인 [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CListClearNode | `83420` | 9/325/2/4 | 인수 [0] 목록 종류(0~0x12 밖이면 2), [1] 목록 변수. ID의 **목록 전체를 비운다**(`37DF00` → `186D0`; 변수가 없으면 새 목록을 만들고 실패하면 2, 핸들 `+8` 널이면 아무것도 안 하고 1). 종류 0xE는 정수 목록 풀 `141B5F9E0`을 비운다. **종류 0xF만 비우기 전에** 원소마다 부대 표(`world+0x7E838`)로 조회해 무효이면 `32D0E0`으로 세계 객체 `+0x128` 목록에서 그 원소를 제거한다(세계 상태에 닿는 유일한 비우기 종류, 추정) [Sonnet 판독 2026-11-25·미검증] | 코드(0xF는 추정) |
| CVariableDivideValueNode | `86540` | 3/212/0/1 | `v = (int64)v / (int64)상수`의 몫 하위 32비트(0쪽 절사, `INT_MIN/−1`은 `INT_MIN`). **제수 0이면 결과 2(쓰기 안 함)**. 디컴파일에 보이는 나머지 계산은 효과 없음 [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CVariablePlusVariableNode | `922F0` | 1/157/1/1 | `[0] = [0] + [1]`(int32 래핑, 읽기 순서 [0]→[1], 하나라도 정수로 못 읽으면 2) [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CListAddPersonNode | `825F0` | 1/141/0/0 | 목록에 무장 추가 (꼬리 추가·중복 허용) [Sonnet 판독 2026-11-25·미검증] | 이름 |
| CVariableGetListLengthNode | `8EF60` | 3/121/2/4 | 인수 [0] 목록 종류 코드(0~0x12, 밖이면 2), [1] 목록 변수 키(객체), [2] 결과 키. **순회로 세지 않고 저장된 개수**(`4FCA0` → 전역 개수표 `1427D4158[ID×8]` 하위 32비트)를 [2]에 정수로 쓴다(핸들 널이면 ID 0x14000). 종류 0xE만 다른 표 `141B5FA08`(정수 목록용으로 추정). 객체 포인터가 널이면 접근 위반 가능(검사 없음) [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CGetMyselfDistrictNode | `3DB40` | 0/124/0/0 | 판단 주체 군단 객체를 `[0]` 키에 객체로 저장(저장 성공 1, 실패 2). `B7170`: `AgentType` 읽기 실패 또는 4(세력 트리)이면 0(저장되는 값은 널), 3(군단 트리)이면 주체 그대로, 2(군세)이면 `22D4E0`, 1(부대)이면 `22D3C0`으로 군단을 얻는다. 난수 없음 [Gemini 판독 2026-11-25·미검증] | 코드 |
| CVariableMinusVariableNode | `92080` | 4/117/0/0 | `[0] = [0] − [1]`(int32 래핑, 실패 조건은 `922F0`과 같음) [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CMiscSetPersonEvaluationNode | `6EFD0` | 1/119/0/0 | 무장 평가 점수 저장(실행 `6EFD0` 공용 — 거점·진형·경계군세 평가 저장과 같은 함수) | 문서 참조/쓰임 |
| CGetMyselfDistrictInfoNode | `3C330` | 0/107/3/0 | 판단 주체 군단 정보 항목 조회(군단정보 getter, ai/unresolved.md 3절) | 문서 참조/쓰임 |
| CVariableSetVariableSpecifiedTypeNode | `92990` | 2/103/4/0 | 인수 [0] 종류 코드(0xE = 정수, 그 밖 = 객체), [1] 대상 키, [2] 원본 키. 0xE면 정수 복사, 아니면 객체 8바이트(포인터·핸들)를 **그대로 복사**(목록 핸들이면 핸들만 복사, 내용은 같은 목록 공유). 종류가 0xE가 아닌데 원본이 정수면 2 [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CVariableSetRandomNumberNode | `92870` | 1/98/0/0 | 범위 안 난수를 변수에 | 이름 |
| CListRemovePersonNode | `84BC0` | 0/96/0/0 | 목록에서 무장 제거(실행 `84BC0` 공용) (같은 값 모든 항목 제거, 항상 1) [Sonnet 판독 2026-11-25·미검증] | 문서 참조/쓰임 |
| CVariableClearNode | `86480` | 0/78/1/0 | 키에 **정수 0**을 쓴다(객체·목록 변수였어도 정수 0으로 바뀜, 목록 비우기는 `CListClearNode 83420`). **쓰기 실패해도 항상 결과 1** [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CGetMyselfForceInfoNode | `56BD0` | 12/62/0/0 | 판단 주체 세력 정보 항목 조회. 인수 `[0]` 항목 번호 0..39(**정수 직접값**), `[1]` 출력 키(항목별 정수/객체/목록), 자기 세력 F는 `B7210`. 항목 20은 출력 없이 1, 미지원 항목·F 무효·쓰기 실패 2. 항목 4 전력 = 세력 군단(world+0xD0 목록 순)마다 거점 목록 전체에서 소속 군단이 같은 거점의 `v=+0x3C`, `m=+0x44`로 `T(m×(T(v×DAT_141A4AFD8×군주 +0x16A/10000)+v)/100)`을 합한 값(**합 0을 1로 고치지 않음**). 항목 5 = `v + T(DAT_141A4AFE4×v×h/10000)`, v = `F+0x13+자기 번호`(F와 F2가 같은 자기 세력), h = 군세면 구성원 중 통솔 최대자(동점 첫 무장)의 `+0x16C`, 군단·세력이면 군주의 `+0x16C`. 항목 27 = `+0x17A` u8[5]를 **5칸 끝까지**(중간 0은 종료 아님) 값 ≠ 0만 세력으로. 항목 37 = `59060(F,i)` i=0..2의 **`+0x196` u16[3]** 무장(정책 패널 아님). 항목 23(`B9C70`) = 군주 거점에서 방향 1..6 직선(각 최대 200칸) + x 감소·증가 방향 총 8방향에서 처음 만나는 타세력, 거리순 정렬 아님. 그 밖 항목(0 세력 번호, 1 `+0x4B`, 2 군주 무장, 3 `26A600`, 6 `+0x17A` 첫 세력, 7 `+0x17F`, 8 `F+8`, 9·10·17·19·21·22·25·26·28·31·33~35·38·39 목록류, 11 `590A0` 성공, 12..16 정책 칸수 − `22ED90`, 18 `230270`, 24 군사, 29·30·32, 36 군정 등급)는 해당 표를 따른다 [Codex 판독 2026-11-25·미검증] | 코드 |
| CVariableMultiVariableNode | `921C0` | 1/67/0/0 | `[0] = [1] × [0]`(int32 곱, 래핑) [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CMiscBreakNode | `850D0` | 0/60/5/0 | 정수 변수 키 `0xB9CCCA0F`(문자열 `IsLoopBreak`의 해시: h=1에서 문자마다 h×=31 후 key += c×h)에 정수 1을 쓴다(성공 1, 실패 2). 반복 노드 `CLoopListElementNode`(`59CD0`)의 종류별 반복 함수(`59FC0`·`5A040`·`5A3C0`·`5A790`·`5AD40`·`5B070`·`5B510`·`5B840`·`5BA30`·`5BC00`·`5BFD0`·`5C480`·`5C7D0`·`5CB70`·`5D060`·`5D230`)가 **원소 하나를 처리한 직후마다** `IsLoopBreak`를 읽어 값 > 0이면 0으로 되돌리고 반복을 즉시 끝낸다(읽기 실패면 계속). 즉 현재 원소를 끝까지 처리한 뒤 다음 원소 전에 종료. 전역 목록 형태의 순회는 본문 실행 뒤에 다음 노드를 읽으므로(미리 저장하지 않음) 본문이 현재 원소를 지우면 순회가 어긋나고, 본문이 같은 목록 꼬리에 추가한 원소는 같은 반복 안에서 방문된다(`5A3C0` 첫 갈래). 키 문자열 사용처 17곳 확인(`ghidra_full.py str IsLoopBreak`) [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CMiscLogNode | `85110` | 4/56/0/0 | 게임 상태·저장소를 바꾸지 않는 읽기 전용 노드(로그 출력 호출이 코드에 없음, 릴리스에서 제거된 것으로 추정). 모드 인수 [1]==0이면 **항상 1**, ≠0이면 대상 변수 읽기 실패 시 2, 아니면 1 [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CSetForceEvaluationNode | `85580` | 2/37/0/0 | 세력 평가 점수 저장(실행 `85580` 공용) | 문서 참조/쓰임 |
| CListAddForceNode | `81EB0` | 8/28/0/0 | 목록에 세력 추가 (꼬리 추가·중복 허용) [Sonnet 판독 2026-11-25·미검증] | 이름 |
| CSpyHomeOfficerRemoveNode | `3EAA0` | 0/36/0/0 | 인수 `[0]` 정수 = **1부터 세는 첩보 슬롯**(판단 주체 = 군단). 군단 명령서 < `DAT_141A4B440`이면 2, 세력 무효 2, 슬롯 범위 밖이어도 1(무변경). 슬롯(`세력 +0x19C[i]` 대상 세력 byte, `+0x196[i]` 담당 무장 u16) 중 하나라도 0이 아니면 둘 다 0으로 쓰고 명령서 `−DAT_141A4B21C`(사전 검사 B440과 다른 상수). 둘 다 0이면 차감 없음 [Codex 판독 2026-11-25·미검증] | 코드 |
| CVariableMinusValueNode | `92000` | 1/33/0/0 | `[0] = [0] − 상수`(int32 래핑) [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CListAddAreaUniqueNode | `812A0` | 0/31/2/0 | 목록에 지역 추가(중복 제외) (꼬리 추가·중복이면 추가 없이 1) [Sonnet 판독 2026-11-25·미검증] | 이름 |
| CGetMyselfForceNode | `58B40` | 5/23/0/0 | 판단 주체 세력 객체를 `[0]` 키에 저장(성공 1, 실패 2). `B7210`: `AgentType` 읽기 실패이면 0, 4(세력 트리)이면 주체 그대로, 3(군단)이면 주체 `+0x10`(byte)이 0x34 미만일 때 세력 표 `world+0xDF30[+0x10]`(0x34 이상이면 0번 칸), 2이면 `22E560`, 1이면 `22E2A0`. 난수 없음 [Gemini 판독 2026-11-25·미검증] | 코드 |
| CClearFriendForceListNode | `52910` | 1/0/0/0 | 판단 주체 세력 `+0x17F..+0x183` 5바이트를 0으로 비운다. 인수 없음, 항상 1 [Gemini 판독 2026-11-25·미검증] | 코드 |
| CSetFriendForceListNode | `58B90` | 1/0/0/0 | `[0]` 세력 목록의 앞 5개 원소(가상 함수 `+0x60` = 세력 번호로 보임)를 [0, 0x33]으로 자르고 중복 검사 없이 세력 `+0x17F..`에 순서대로 쓴다(남는 칸은 비우지 않음). 목록이 비어도 1, 목록 읽기 실패·널이면 2 [Gemini 판독 2026-11-25·미검증] | 코드(`+0x60` = 세력 번호는 상한 0x33에 근거한 추정) |
| CClearTargetForceListNode | `52950` | 1/1/0/0 | 판단 주체 세력 `+0x17A..+0x17E` 5바이트를 0으로 비운다. 항상 1 [Gemini 판독 2026-11-25·미검증] | 코드 |
| CSetTargetForceListNode | `58C90` | 1/1/0/0 | `58B90`과 같은 구조로 세력 `+0x17A..+0x17E`에 앞 5개를 쓴다(자르기 [0, 0x33], 남는 칸 유지) [Gemini 판독 2026-11-25·미검증] | 코드(`+0x60` = 세력 번호는 추정) |
| CVariableDivideVariableNode | `865D0` | 2/26/0/0 | `86540`과 같은 64비트 부호 있는 나눗셈, 몫 하위 32비트를 [0]에. **제수 변수가 0이면 2** [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CVariableGetDistanceNode | `886F0` | 0/24/1/1 | 인수 [0]·[1] 첫째 객체 종류·키, [2]·[3] 둘째, [4] 결과 키. 각 객체를 `BFBC0`로 칸 번호(없음 = 0xBD10)로 바꿔 `2ACB80`(220열 헥스 거리)을 [4]에 쓴다. **첫째 칸이 없으면 2, 둘째 칸이 없어도 검사 없이 0xBD10으로 계산**한다. 종류 → 칸 변환: **0 세력 객체 → 군주(`+0x10` u16)의 소속 거점(`230350`: 무장표 `world+0x158` 또는 `world+0x73A50`의 무장 `+0xE2` → `32E3B0`) → `22F190`, 1 군단 객체 → 군단장(`+0x12` u16)의 소속 거점(`22EDF0`, 같은 구조) → `22F190`**(정정, 이 문서 「정정 기록」 참조; 디컴파일 `decomp_cache.py get BFBC0·230350·22EDF0`, structs.md 세력 `+0x10` 군주·군단 `+0x12` 군단장·conditions.md 객체종류 코드 0 세력·1 군단과 일치), 2 `22FC40` 결과 `+0x2A`, 3 객체 `+0x2A`, 4 `22EFD0`→`22F830`, 5·8·9 `22F190`, 6 객체 `+0x3A`, 7 `22F830`, 10 객체 `+0x10`, 0x12 객체 `+0x5C`, 그 밖 0xBD10(1~4 일부 세부는 하위 함수 일부만 읽음) [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CMiscDummyNode | `85100` | 0/23/3/0 | 아무 일 없이 결과만 돌려줌(결과값은 아래 「더미 노드」 절) | 문서 참조/쓰임 |
| CListAddAreaNode | `81160` | 0/24/0/0 | 목록에 지역 추가 (꼬리 추가·중복 허용) [Sonnet 판독 2026-11-25·미검증] | 이름 |
| CGetForceFriendshipNode | `56AC0` | 0/24/0/0 | 원시 우호도가 아니라 **자기 군주 성향 보정항**만 `[1]`에 정수로 쓴다: `(DAT_141A4AFE4 × u8(A+0x13+상대 번호)) × 군주 +0x16C ÷ 10000`(상대 번호 ≥ 0x34이면 v=0, 32비트 곱, 포화 없음, v를 더하지 않음). 자기 세력 A는 키가 아니라 실행 인수. 확정(코드, 지휘 세션 대조 2026-11-25). `ai/unresolved.md` 세력정보 항목 5(`8CAE0` case 5, v+보정항)는 다른 함수 [Codex 판독 2026-11-25·미검증] | 코드 |
| CVariableMinVariableNode | `91F40` | 0/23/0/0 | `[0] = min([0], [1])` 부호 있는 32비트 비교 [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CVariableMaxValueNode | `91B50` | 0/21/0/0 | `[0] = max([0], 상수)` 부호 있는 비교 [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CSpyHomeOfficerSetNode | `3EBC0` | 0/18/0/0 | 인수 `[0]` 첩보 **대상 세력 T**, `[1]` 무장 P, `[2]` 슬롯(1부터). 조기 1: T 자체의 슬롯 값이 이미 T 번호·P 번호(코드는 F가 아니라 T의 슬롯을 읽음). 일반: 슬롯 < 3, 0 < T 번호 < 52, 1 ≤ P 번호 ≤ 6000, 군단 명령서 ≥ B440, F·T·P 유효. 쓰기: P의 기존 첩보 슬롯 해제(`22B1E0`), P가 도시 모병/훈련 담당이면 **소속 거점**(`P+0xE2`, `32E3B0(world, u16(P+0xE2))`; 현재 위치 `+0xE4`가 아님 — 5차 정정, [Codex 판독 2026-11-25·미검증] c10)의 `+0xCA/+0xCC`=0, 지역 담당 전부 해제(`29DE10(P,0,0)`, 방침 유지), 슬롯에 T 번호(0..51)·P 번호(0..6000) 기록, 명령서 `−B21C`. 이미 같은 배치여도 T 기준 조기 비교를 통과하지 못하면 비용을 낼 수 있다 [Codex 판독 2026-11-25·미검증] | 코드 |
| CListRemoveForceNode | `84BC0` | 0/18/0/0 | 목록에서 세력 제거(실행 `84BC0` 공용) (같은 값 모든 항목 제거, 항상 1) [Sonnet 판독 2026-11-25·미검증] | 문서 참조/쓰임 |
| CCallScriptNode | `5D760` | 3/12/0/0 | `0000/param_s.bin` 수식표(`C11E0`이 읽음)의 n번 수식 계산. 판단표 밖 스크립트가 아니라 수식 호출(ai/formulas.md·ai/data_locations.md; 2026-11-25 4차). `[0]` 정수 즉값 = 수식 번호, `[1]` 결과 키이고 정수 입력 7개를 읽는다(사용 횟수 열의 3/12/0/0은 트리별 노드 수이지 인수 개수가 아님). 나눗셈에서 나누는 값이 0이면 식 결과 1, 입력 읽기 실패 2 | 코드 (5차 정정, 출처 표시: [Sonnet 판독 2026-11-25·미검증] s16) |
| CVariableMinValueNode | `91DF0` | 0/15/0/0 | `[0] = min([0], 상수)` 부호 있는 비교 [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CMiscSetAreaEvaluationNode | `85580` | 0/10/0/0 | 지역 평가 점수 저장(실행 `85580` 공용) | 문서 참조/쓰임 |
| CVariableGetForceFriendshipNode | `8CA00` | 0/10/0/0 | `[2] = u8(A+0x13+B 번호)`(A→B 우호도 바이트 그대로, B 번호 ≥ 0x34이면 0). 인수 [0]=A, [1]=B, 둘 다 유효해야 함(아니면 2) [Codex 판독 2026-11-25·미검증] | 코드 |
| CGetDelegationTargetNode | `7C680` | 0/7/1/0 | 위임목표조회(현재군단, 객체종류 출력, 목표 객체 출력): 군단 `[0]`의 위임 목표 번호 `+0x18`·종류 `+0x19`를 객체로 바꾼다. 종류 2 → 거점(`32E3B0`; `[2]` 거점, `[1]` = 5), 7 → 세력(`world+0xDF30`; `[1]` = 0), 8 → 군단(`world+0xE0D0`; `[1]` = 1, 군단이 무효면 출력 없이 성공), 그 밖 종류 → 2(실패). 판단표 공통 준비 N173·N631·N645 (2026-11-25 4차) | 코드 |
| CVariableMaxVariableNode | `91CA0` | 0/8/0/0 | `[0] = max([0], [1])` 부호 있는 비교 [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CGetCompatibilityNode | `7C5B0` | 1/6/0/0 | 인수 `[0]`·`[1]` 두 무장 객체(둘 다 유효해야 함), `[2]` 결과 키. `2A8010`: `d = |무장A +0xBE − 무장B +0xBE|`, `d = min(d, 150 − d)`, `min(d, 75)`를 `[2]`에 정수로 쓴다(객체 무효 시 0이 아니라 노드가 2). 값이 작을수록 상성이 가깝다. 난수 없음 [Gemini 판독 2026-11-25·미검증] | 코드 |
| CVariableCreateSpecifiedTypeNode | `864E0` | 0/5/2/0 | 종류 코드(0xE = 정수, 그 밖 = 객체)와 대상 키. 0xE면 정수 0, 아니면 널 핸들(객체 0)을 쓴다(기존 값은 덮어씀: 저장소 덮어쓰기 플래그가 켜졌을 때) [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CGetSearchAreaNode | `7F990` | 0/6/0/0 | 세력 F의 탐색 지역 목록 `[1]`: 재야 → 숨은 명품(`+0x50==2`) → 명승 → 전법서 순서(각 원본 목록 순서)로 소유 지역을 중복 없이 꼬리 추가. 빈 목록도 1, F 무효 2(목록은 이미 비워짐), 난수·정렬 없음 [Codex 판독 2026-11-25·미검증] | 코드 |
| CGetSearchDataNode | `3DCD0` | 0/6/0/0 | 탐색 후보 **무장** 목록만 채운다(지역 인수 없음): 현재 군단 무장 중 `+0x161<2`·`+0x15E` bit0 없음·`234AB0==0`·`233BE0==0`, 전역 무장 연결목록 순서. 반환은 항상 1 [Codex 판독 2026-11-25·미검증] | 코드 |
| CCommandExecutionSearchNode | `54AD0` | 0/6/0/0 | 탐색 등록: 지역 Z·무장 A, `1F1430`(지역 소유 = 무장 소속)·명령서 ≥ `B5B8`이면 `1F3F50`(명령서 `−B5B8`, 금·군정 직접 차감 없음), 등록 때 조언 사전 검사 `2F7D80`(재야 → 명승 → 명품·책 단락, 날짜 해시 기반 고정 섞기). 상세 rules_diplomacy.md 5.5절 [Codex 판독 2026-11-25·미검증] | 코드 |
| CGetTargetForcePrisonerListNode | `801D0` | 0/6/0/0 | A 관련 포로 후보를 목록 `[2]`의 **꼬리**에 추가(정렬·상한·중복 검사 없음, 목록 없으면 생성, 비어도 1). 후보 = 신분 `+0xE6`==6, 소속 거점(`+0xE2`)의 소유 세력 == B, 군단 세력 `22E870`==A(반복자 거름이 먼저 요구하므로 `+0x165`==A만으로는 통과하지 못함; 5차 정정, [Sonnet 판독 2026-11-25·미검증] s9), 소재 종류가 5 도시·6 관문·0x1B 부대(종류 10 이동 형식 제외). 무장 목록 iterator의 vtable 슬롯 미확정(추정 `335540`) [Codex 판독 2026-11-25·미검증] | 코드 |
| CCommandExecutionMerchantNode | `2E410` | 0/6/0/0 | 군량 매매(상인). 인수 `[1]` **정수 직접값**(0/비0), `[2]` 금 과부족, `[3]` 군량 과부족, `[4]` 후보 무장 목록. **노드 `[1]`==0이 실제 명령 방향 1(매입), 비0이 방향 0(매각)** — 리터럴과 방향이 반대다. 게이트 `70FF80`(도시 번호<52, 군단 명령서 ≥ `B44C`, 도시 `+0xC9` bit0=1·bit2=0, 거래 가능, 가능 무장 있음). 후보는 목록 순서대로 가능 무장(`6DA1B0`)만 채택해 지력+정치 실효 능력 합 `A(p)`를 누적하며 거래량 `26A450`/`26A6A0` 상한(10명 상한, 같은 거래량이면 마지막 1명 제거는 방향 1(매입)에서만이고 방향 0(매각)에는 없음; 5차 정정, [Sonnet 판독 2026-11-25·미검증] s9)을 채우고 `1F2370`으로 실행: 무장 `+0x15E|=1`, 공적 `16A4E0(p, A/S×량×…)`, 금·군량 이동(방향 0: 금 `+량×10/r`·군량 `−량`, 방향 1: 금 `−(b+(량−1)×10)/b`·군량 `+량`), 명령서 `−B44C`, 도시 `+0xC9 |= 4`. 실행이 실패해도 노드는 1. 일부 나눗셈에 0 보호 없음. 난수 없음 [Codex 판독 2026-11-25·미검증] | 코드 |
| CGetExchangeConditionsNode | `7E930` | 0/6/0/0 | **포로 교환 조건이 아니라 자원 가치 변환기**: `[0]` 직접값 0이면 `x>0 ? B3B4×x/10 : 0`, 1이면 `x>0 ? x×10/B3B4 : 0`을 `[2]`에(B3B4=50이면 ×5, ÷5) [Codex 판독 2026-11-25·미검증] | 코드 |
| CRecruitOfficerRemoveNode | `3E6B0` | 0/6/0/0 | 인수 `[0]` 거점만 읽음(판단표의 둘째 인수는 미사용). 거점 `+0xCA`==0이면 1, 거점 군단 명령서 < `DAT_141A4B434`이면 2, 아니면 `1F34F0({거점, ID 0})`을 불러 반환을 무시하고 1. `1F34F0`: 명령서 `−B434`(0..200)를 치르고 **0번 무장**을 기준으로 거점 `+0xCA/+0xCC`가 그 무장이면 0, 첩보 담당·지역 담당 해제, 마지막 `+0xCA=0` — 기존 담당 무장을 넘겨 해제하는 함수가 아니다 [Codex 판독 2026-11-25·미검증] | 코드 |
| CRecruitOfficerSetNode | `3E750` | 0/6/0/0 | 인수 `[0]` 거점, `[1]` 무장. `거점 +0xCA == 무장 +0x10`이면 1(비용·유효 검사 없음), 아니면 **무장 소속 군단** 명령서 < `DAT_141A4B434`이면 2, 둘 다 유효하면 `1F34F0({거점, 무장})`(반환 0이면 2; 명령서는 **거점의 군단**에서 차감, 노드 사전 검사 군단과 다를 수 있음): 새 무장이 거점 `+0xCA/+0xCC`에 있으면 먼저 0, 첩보 슬롯(`279890`)·지역 담당(`29DE10(무장,1)`) 해제, `+0xCA = clamp(ID,0,6000)`. 모병 담당 배치이며 등용(Employ)이 아니다 [Codex 판독 2026-11-25·미검증] | 코드 |
| CTrainingOfficerSetNode | `3EF50` | 0/6/0/0 | `3E750`과 같은 구조이되 사전 검사 군단이 **거점 군단**(명령서 < `DAT_141A4B440`이면 2)이고 `201A80({거점, 무장})`으로 `+0xCC = clamp(ID,0,6000)`. 무장 능력·훈련 효율 평가는 노드에 없다 [Codex 판독 2026-11-25·미검증] | 코드 |
| CSceneryInvestSetNode | `3E890` | 0/3/0/0 | 명승 투자 시작: 판단 군단 무효 2. 명승 `+0x5F` bit0, `+0x64`==1, `+0x6C`가 1..5, `+0x66`==0, `+0x68`<1, 소유 세력·지역·도시 유효, 도시 군단 번호 == 판단 군단, 비용 C=`22C5F0` ≤ 도시 금이고 군단 명령서 ≠ 0이어야 한다. 통과 후 `+0x64=2`, 기간 d=`22C810`, 오늘 t, `+0x66`·`+0x68` 기록, 도시 금 `−C`(0..상한), 명령서 `−1`. `+0x66` 저장은 디컴파일이 `d≥1이면 0, d<1이면 (s16)(t+d)`로 읽혀 의도(`max(0,d)`)와 달라 원작 재현 미확정(디컴파일 아티팩트일 수 있음), `+0x68 = max(0,t+d)`. 비용 `22C5F0`·기간 `22C810` 식은 functions.md 기록과 일치 [Codex 판독 2026-11-25·미검증] | 코드 |
| CGetCanServePersonListNode | `7C300` | 0/3/0/0 | **군단 판단표 3회**. 등용 **대상** 후보 목록 `[1]`을 만든다: 전역 무장 연결목록 순서로 `1F0A30(P, 군단)`(이 조건과 순회는 하위 `6DF810` 안에 있는 것으로 보이나 `6DF810`을 아무도 읽지 않아 판정 보류 — 미해결; 5차 정정, [Gemini 판독 2026-11-25·미검증] g52): `233BE0`이 아니고, 신분 ≠ 1, 소속 군단 번호가 46..51이 아니며, `234AB0==0`·`+0x15E` bit 0x4000 없음, 그리고 소속 세력이 군단 세력에 적대(신분 1..4) / 신분 5(재야)면 현재 칸 지역 소유가 우리 세력 / 신분 6(포로)면 `+0xE4` 거점의 소유가 우리 세력인 무장을 추가. 마지막으로 **같은 세력이 이미 내린 등용 명령**(명령 관리자 목록, 종류 2, 첫 대상이 무장)의 대상을 `21A350`으로 목록에서 전부 제거. 정렬 없음 [Codex 판독 2026-11-25·미검증] | 코드 |
| CCommandExecutionEmployNode | `2D720` | 0/3/0/0 | **군단 판단표 3회**(세력 아님). 인수 `[0]` 실행 무장 E, `[1]` 등용 대상 T, 둘 다 유효해야 하고 `1EECC0`({T,E,mode 0})을 불러 **결과와 무관하게 1**. 등록 `1F71B0`: E `+0x15E |= 1`, 소재를 이동 형식으로, 군사 조언 `2F5AA0`, 도착일 `232F70`/`2331F0`, 출발 거점 군단 명령서 `−6D5A50()`(0..200)을 쓰며 판정은 `279DE0(T,E,&roll)`(인수 순서 T,E)이다. 난수: `2F5AA0`의 `3FDAF0(100,10,E,T,0,0)` 1회(군사 유효 시) + `279DE0`의 `3FDAF0(100,1,E,T,0,0)` 1회(조기 종료 아니면). 지연 실행 `1DBD80`·소속 변경 `273100`의 vtable 연결은 추정 [Codex 판독 2026-11-25·미검증] | 코드 |
| CCommandExecutionHireNode | `2DAB0` | 0/3/0/0 | 인수 `[0]` 거점, `[1]` 템플릿 무장 목록. 군단 명령서 `−DAT_141A4BC0C`가 음수이거나 인원 문턱(`uint64(N + (200−R) − C) ≤ 200−Q` 꼴, signed로 바꾸면 안 됨)·금(`보유 − N×DAT_141A4BC00` < 0)에 걸리면 2. 목록을 연결 순서로 `331310`: 무장 ID 4201..4400(0x1069..0x1130) 중 **최초 빈 슬롯**을 골라 템플릿을 복제(`31DEE0`)·소속 편입(`29FB50`: 신분 4, 충성 `26A270`, `+0xE7=0x49`)·템플릿 `227D30`으로 초기화. 중간 실패 시 앞서 만든 무장은 되돌리지 않고 명령서·금 차감만 생략. 목록 비어도 명령서 차감. 난수 직접 호출 없음(가상 `+0x40` 2회 내부 미확정) [Codex 판독 2026-11-25·미검증] | 코드 |
| CListAddPersonUniqueNode | `82720` | 0/6/0/0 | 목록에 무장 추가(중복 제외) (꼬리 추가·중복이면 추가 없이 1) [Sonnet 판독 2026-11-25·미검증] | 이름 |
| CDomesticPriorityDevelopmentSelectNode | `7B0B0` | 0/6/0/0 | 인수 `[0]` 지역, `[1]` 결과 키(선택 항목 1 상업·2 농업·3 병영 추정, 0 = 선택 없음), `[2..4]` 즉치 가중치(판단표 25·50·75). 군단(`B7170`; 무효면 지역 거점의 군단)의 `B2AF0`: ① 군단 `+0x1A`가 3이고 지역 `+0x3C`≠1000이면 1, 2이고 `+0x3E`≠1000이면 2, 4이고 `+0x40`≠1000이면 3을 우선 선택하며 그 값이 지역 현재 방침 `+0x72`와 같으면 0으로 바꾸고 끝낸다(담당관 검사 없음). ② 아니면 군단 `+0x12`가 가리키는 군단장 무장(군주 무장이 아님)의 `+0x170/+0x172/+0x174`(a1..a3; 5차 정정, [Sonnet 판독 2026-11-25·미검증] s9), 개발값 `+0x3C/+0x3E/+0x40`을 4문턱(`13A9DDC`, 기존 기록 {100,300,600,1000})으로 단계 L1..L3(1..5)로 바꿔 `Si = Li×(ai+100)×wi/100`(개발값 ≥ 1000이면 50000)의 **최솟값** 항목을 고르고(전부 50000이면 0, 동점은 1→2→3), 선택이 `+0x72`와 같으면 담당관(`+0x36`)이 유효할 때 0, 무효이면 같은 항목을 다시 낸다. 난수·목록 없음 [Codex 판독 2026-11-25·미검증] | 코드 |
| CDomesticOfficerSetNode | `36E80` | 0/6/0/0 | 인수 `[0]` 지역, `[1]` 무장, `[2]` 개발 방침(정수 키; 키가 0이거나 읽은 방침 값 v가 0이면 변경 없이 결과 **2**: 코드는 `if(key!=0){읽기; if(v!=0){…return 1}} return 2`; 5차 정정, [Sonnet 판독 2026-11-25·미검증] s10). 이미 같은 담당·방침이면 1. 무장 소속 군단 명령서 `+0x14` < `DAT_141A4B428`이면 2. 그 뒤 `25330`으로 지역·무장·방침 병렬 목록 명령을 만들어 `1EE630`을 실행(결과와 무관하게 1): `2ABF60(무장,2)>0`이고 `43800`(담당 수가 한도 도달)일 때만 무장의 기존 담당 지역(`+0x1D0`) 첫 유효 1개를 해제 항목으로 먼저 넣고 새 지역을 추가한다(조건 누락 정정, [Sonnet 판독 2026-11-25·미검증] s10). 쓰기 3단계: (A) 대상 무장의 거점 모병·훈련 담당(`+0xCA/+0xCC`)과 첩보 슬롯을 0으로, 같은 무장의 다른 지역 담당(`2ABF60(무장,2)==0`일 때 첫 지역) 해제, (B) 명령 대상 지역 전부 담당 0·방침 0, (C) 목록 순서대로 새 담당(0..6000)·방침(0..3) 기록. 명령서 `+0x14 = clamp(기존 − k×B428, 0, 200)`(k = 바뀐 지역 수, 노드 사전 검사 군단과 다를 수 있음). 난수 없음 [Codex 판독 2026-11-25·미검증] | 코드 |
| CDiplomacyPriorityConditionSelectNode | `7AFA0` | 0/6/0/0 | 외교 대가 종류 우선 선택(동맹 공격 요청 N3108에서 대가 종류 0 금·1 군량·2 명품을 고름; 위 N01 `7AC40`) | 문서 참조/쓰임 |
| CGetDiplomacyConditionAreaNode | `7C850` | 0/5/0/0 | 인접 상대 B에게 넘길 지역 후보 중 **최소 지역 번호** 하나를 `[3]`에, 제안 종류 4를 `[2]`에 쓴다(후보 없음·쓰기 실패 때도 `[2]`=4는 남음). 필터·정렬은 rules_diplomacy.md 3.7절 [Codex 판독 2026-11-25·미검증] | 코드 |
| CGetAreaDistanceNode | `7B6D0` | 0/4/0/0 | 인수 `[0]`·`[1]` 첫째 대상 종류·객체, `[2]`·`[3]` 둘째, `[4]` 결과 키. 각 대상을 `BFBC0`으로 칸 번호(종류 변환표는 위 `CVariableGetDistanceNode`)로 바꿔 **하나라도 0xBD10이면 2**, 아니면 칸 `+0x12`(소속 지역 번호) 둘로 `B73C0`을 부른다: 같은 지역이면 0, 다르면 `98F80`으로 지역 사이 거리를 구하고 실패하면 `0x7FFFFFFF`. 결과를 `[4]`에 정수로 쓴다(`CVariableGetDistanceNode`와 달리 둘째 칸 없음도 2). `98F80` 내용 미판독이라 거리 단위(지역 단위)는 사용 예와 폴백 값에 근거한 추정. 난수 없음(`98F80` 하위 미확인) [Gemini 판독 2026-11-25·미검증] | 코드 / 추정(`98F80` 의미) |
| CGetRemainAlliancePeriodNode | `7F780` | 0/4/0/0 | `[2] = u8(A+0xEA+B 번호) & 0x7F`(동맹 관계 바이트 하위 7비트, 범위·날짜 환산·동맹 여부 판정 없음) [Codex 판독 2026-11-25·미검증] | 코드 |
| CAllianceSuccessConditionNode | `525C0` | 0/4/0/0 | 동맹 제안 자원 검사: 비플레이어 T는 금 ≥ 1000이고 `금−1000 > rg`이면 `[3]`=1000 고정, 플레이어 T는 `9D930`(기간 비용 `324180` ≤ 제공 가능 가치, `3240F0` 우호 부족 가산 없음). 보존량 양수는 보유량 전체로 치환. 수락 난수 없음. 상세 rules_diplomacy.md 3.7절 [Codex 판독 2026-11-25·미검증] | 코드 |
| CCommandExecutionAllianceNode | `52990` | 0/4/0/0 | 제안 종류 5(동맹)를 구성해 `1EE460` 제출(기간 `[4]` 직접값, 대가 k 0 금/1 군량/2 명품/4 지역). **제출이 실패해도 결과 1**, 자원 여유 검사 없음. 효과는 도착 후 결과 단계 [Codex 판독 2026-11-25·미검증] | 코드 |
| CListAddForceUniqueNode | `81FF0` | 2/1/0/0 | 목록에 세력 추가(중복 제외) (꼬리 추가·중복이면 추가 없이 1) [Sonnet 판독 2026-11-25·미검증] | 이름 |
| CGetPlayerForceNode | `7F720` | 0/3/0/0 | 플레이어 세력 조회(동맹 공격 요청 N3078) | 문서 참조/쓰임 |
| CGetEmployDataNode | `39FF0` | 0/3/0/0 | 등용을 **실행할** 소속 무장 후보 목록 `[0]`(대상 목록은 앞 `CGetCanServePersonListNode`)을 만든다(비어도 1, 군단 유효 검사 없음). `6DCBB0`이 전역 무장 연결목록 순서로 조건 `335300`(소속 군단 번호 = 현재 군단, 신분 1..4)과 단락 순서 `+0x161 < 2` → `+0x15E` low byte bit0 == 0 → `234AB0==0` → `233BE0==0`(소재가 소속 거점과 같고 진행 중 명령 없음)을 통과한 무장을 추가. 정렬·난수·쓰기 없음 [Codex 판독 2026-11-25·미검증] | 코드 |
| CPrisonerReturnSuccessConditionNode | `85610` | 0/3/0/0 | 포로 목록 `[1]`의 가치합(`26C510`)이 군주 거점 금 예산에 안 맞으면 **목록 꼬리부터 제거**(최소 1명 남김, 복원 없음)하고 마지막 `r < G−C && C ≤ G`이면 1, `[2]`에 남은 가치합. 입력 목록을 파괴적으로 줄이는 부작용이 있다 [Codex 판독 2026-11-25·미검증] | 코드 |
| CCCommandExecutionPrisonerReturnNode | `548D0` | 0/3/0/0 | 제안 종류 8(포로 반환) 제출: 군단 명령서(`230270(S)+0x14`)==0이면 2, 원본 목록에서 신분 6 무장만 임시 목록으로 복사(원본 불변), 비면 2, 그 밖 `1EE460` 후 항상 1. `1F1000` 검증은 포로 ≤3명·군주 거점 금 ≥ 가치합 [Codex 판독 2026-11-25·미검증] | 코드 |
| CCommandExecutionExchangeNode | `53530` | 0/12/0/0 | 제안 종류 0x13(19, 교환) 제출: 인수 `[2]`·`[4]`는 정수 **직접값**(제공·요구 종류 0 금/1 군량/4 지역), `[3]`·`[5]` 양 또는 지역 객체, **받을 쪽부터 읽는다**. 제공 금·군량이 군주 거점 보유보다 크면 2(같으면 통과), T/P 유효 검사는 노드에 없고 `1F1000`이 한다. 제출 실패해도 1. 명품 교환 분기는 없다(받는 금·군량·지역은 명령 `+0x84/+0x88`에만 기록, 실제 수령은 도착 후 `81F290`). 쓰임 12는 사용 횟수이지 인수 수가 아니다 [Codex 판독 2026-11-25·미검증] | 코드 |
| CVariableMinVariableCalculationNode | `91E80` | 0/3/0/0 | `[2] = min([0], [1])`(결과만 [2]에 쓰고 피연산자 키는 그대로, 부호 있는 32비트) [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CItemSelectNode | `80A10` | 0/3/0/0 | 군주 소유 명품 중 `bit0`·`!bit3`·가치 `min(+0x49,50)<11`(10 이하)만 후보, 우선 분기(말 2개 이상·능력 ≥ 79/80 종류별)마다 가치가 **엄격히** 큰 첫 항목. 난수 없음, 실패 시 출력 키에 이전 값 유지. rules_diplomacy.md 5.5절 [Codex 판독 2026-11-25·미검증] | 코드 |
| CCommandExecutionItemNode | `54250` | 0/3/0/0 | 하사 **즉시 실행**(명령 객체 없음): 이전 소유자 군단 명령서 ≥ `B5B8`이면 `1F16B0`, 이전 소유자 충성 조건부 감소·받는 무장 충성 조건부 증가·명품 소유자 변경·**수령자 직할 군단** 명령서 차감. 실행 결과를 반환에 반영(1/2). rules_diplomacy.md 5.5절 [Codex 판독 2026-11-25·미검증] | 코드 |
| CGetTransactionDataNode | `3DF60` | 0/3/0/0 | 거래 가능 **도시 목록** `[0]`과 그 도시들의 거래 가능 무장 합집합 `[1]`을 만든다: 군단 거점(world+0x80 순서, `70FF80` 통과)의 거래 도시를 중복 없이 꼬리 추가, 이어 도시마다 `6DA1B0` 무장을 `[1]`에 중복 없이 추가. 두 목록을 먼저 비우므로 둘째 생성 실패 시 첫 목록이 비워진 채 2. 정렬·난수·쓰기 없음(목록 외) [Codex 판독 2026-11-25·미검증] | 코드 |
| CCommandExecutionAnnulNode | `52B60` | 0/3/0/0 | 제안 종류 6(동맹 파기) 제출: **실제 대상은 `[2]`**, `[0]` 세력은 유효성 확인만. 동맹·우호도·명령서 검사 없음, 제출 실패해도 1. 파기 효과(`+0xEA`·우호도·충성)는 도착 후 결과 단계 [Codex 판독 2026-11-25·미검증] | 코드 |
| CGetAroundLandTypeNode | `7B7B0` | 0/3/0/0 | 인수 `[0]` 기준 위치 객체(무효면 2), `[1]` 반경(칸 수), `[2]` 결과 키. `2A9C90`으로 기준 칸 둘레 링 1~반경(중심 제외, 버퍼 `(r+1)·r·6/2`칸)의 칸 중 칸 번호 < 0xBD10이고 칸 표 `world+0xE270`에 유효한 칸을 모은 뒤, 칸마다 지형 정의(`233310`, 표 `world+0x73860`)가 (정의 `+0x2A` ≠ 0) 이고 지형 번호가 0x10도 0x11도 아닐 때 그 번호의 카운트(30칸 배열)를 올린다. 번호 0부터 29까지 `<`로 최댓값을 찾으므로 **동점이면 작은 번호**. 최빈 번호가 0이면(전부 제외·0칸 포함) 결과 키에 널(0)을 쓰고 1, 아니면 표에서 가져온 지형 정의 객체를 쓴다(저장 실패 2). 표 접근식 `표 + 번호×8`은 **포인터 배열**이라는 뜻이고(`233310`: 번호 < 0x1F 아니면 0번), 가리키는 지형 정의 객체가 0x48바이트다 — 충돌이 아니다(정정 기록 참조). 난수 없음 [Gemini 판독 2026-11-25·미검증; 표 접근식은 [Sonnet 판독 2026-11-25] + 작성자 디컴파일 대조: `decomp_cache.py get 233310`] | 코드 |
| CGetOfficerCandidateNode | `7F4F0` | 0/3/0/0 | 거점 `[0]`의 후보 무장 목록 `[1]`(비었으면 성공 1): `6D8E00`이 먼저 도시의 무장, 이어 그 도시에 속한 관문 순서대로 각 관문의 무장을 전역 무장 연결목록 순서로 추가. 조건 `3353E0`(거점 번호 1..61, `무장 +0xE2 == 거점 +0x4E`, 신분 `+0xE6` 1..4) 그리고 `234AB0(무장,0)==0`(특정 무장 번호대 `2C9230`·소재 1..61·세력 46..50 밖이면 제외)이며 건강 필터가 아니다. 정렬·난수·중복 제거 없음 [Codex 판독 2026-11-25·미검증] | 코드 |
| CTrainingOfficerRemoveNode | `3EEB0` | 0/3/0/0 | `3E6B0`과 같은 구조: `+0xCC`==0이면 1, 거점 군단 명령서 < `DAT_141A4B440`이면 2, 아니면 `201A80({거점,0})` 후 1(둘째 인수 미사용). 쓰기 순서는 `1F34F0`과 같고 비용만 B440, 마지막 `+0xCC=0` [Codex 판독 2026-11-25·미검증] | 코드 |
| CCommandExecutionSpyAwayNode | `54BC0` | 0/3/0/0 | **정찰(kind 21)**, 대상 세력 T·무장 A·기간 d ∈ {5,10,15}: A 군단 명령서 ≥ `B60C`, `1F14A0` 검증 후 `1FA100`. 명령서 `−B21C`·본거점 금 `−6DDF10(d)`, 군정 미사용. 난수 최대 3회(조언·성공·부상). rules_diplomacy.md 5.5절 [Codex 판독 2026-11-25·미검증] | 코드 |
| CCommandExecutionInspectNode | `2DCD0` | 0/3/0/0 | **순시(kind 25)**(시찰·정찰 아님): 군정 < 500이면 실행 없음, 거점·무장 후보가 각각 둘 이상일 때 점수 내림차순(안정) 첫 항목, 기간 난수 1회(r<80 10일, <92 20일, 그 밖 30일). rules_diplomacy.md 5.5절 [Codex 판독 2026-11-25·미검증] | 코드 |
| CTradePriorityCountrySelectNode | `860C0` | 0/3/0/0 | 교역 국가 선택: 군단 `230270`, 후보 = 지역 이점 표 5도시 중 `22F740`≠0·`2C8530(세력,2,번호)` 참·진행 중 교역 없음(`711BE0`), 그리고 다른 5도시 대비 `C+0x28+번호` 바이트가 1이 아닌 항목이 있으면 삭제. 정렬: 친밀도(세력 `+0x184+2×번호`) < 1000인 쪽 먼저 → 친밀도 큰 쪽 → 부족 번호 작은 쪽(안정). 선두 하나를 `[1]`에. 난수 없음. `2C8530` 제4인수 ABI 미확정 [Codex 판독 2026-11-25·미검증] | 코드 |
| CGetTradeNeedFoodNode | `803D0` | 0/3/0/0 | 교역 필요 군량 `[2]`: 비용 `T(T(T(T(h×k×a×2/100)×b/10)×c/100)×d/100)`(h=`B9E4`, k=`230A30(도시)`, a=`max(1, 병사/CF80×CF98/10)`, b=10 또는 무장 능력 합 < `B9FC`이면 `B9F0`, c=100 또는 특성 검사 참이면 `BA04`, d=지역 이점 존재면 `BA10` 아니면 100). 단계마다 정수 버림이라 한 분수로 합치면 안 됨. 무장 목록은 사본으로 쓰며 게임 물자는 바꾸지 않는다. 난수 없음 [Codex 판독 2026-11-25·미검증] | 코드 |
| CSetBehaviortreeRestartFlagNode | `85EC0` | 0/0/3/0 | 판단표 재시작 표식: 블랙보드 `"AgentType"`이 4(세력)이면 세력 `+0x20D`(1바이트), 3(군단)이면 군단 `+0x2A`, 2(군세)이면 군세 `+0x38`을 1로 쓰고 1을 돌려준다(읽기 실패 2, 1(부대)은 쓰기 없이 1). 군세 트리에만 3곳(structs 3.12) | 코드 확인(지휘 세션 2026-11-25; 5차 정정, 출처 표시) |
| CGoodwillSuccessConditionNode | `80730` | 0/2/0/0 | 친선 제안 자원 검사: `9F180`이 요구 가치 `324F20`(우호도·혐오·관계 감면·정치 보정·개성을 포함하는 고정 절삭 식, 상세 rules_diplomacy.md 3.7절)과 제공 가능 가치를 비교하고 `보유 − 양 > 보존량`일 때 `[3]`에 금·군량 양 또는 명품. 수락 난수 없음 [Codex 판독 2026-11-25·미검증] | 코드 |
| CCommandExecutionGoodwillNode | `53930` | 0/2/0/0 | 제안 종류 4(친선) 제출: k=0/1이면 `보유 − 양 > rg/rf`(입력 정수 그대로, `80730`과 달리 보유량으로 치환하지 않음)일 때만, 아니면 2. 제출 실패해도 1. 우호도 증가는 도착 후 [Codex 판독 2026-11-25·미검증] | 코드 |
| CGetHiddenPoisonDataNode | `3C1F0` | 0/2/0/0 | 계략(HiddenPoison, 이름 직역 「숨은 독」) 실행 자료 조회 — 실행 무장 후보는 `6DD230` 공유(ai/conditions.md 조건 80). 같은 노드가 목표 지역 목록 `[1]`도 만든다(`6E0D60`·`7143A0`: 인접 거점이고 타 비동맹·비이민족 세력 소유인 지역; 목록이 없으면 새로 만들고 항상 1) | 문서 참조/쓰임 (5차 정정, 출처 표시: [Sonnet 판독 2026-11-25·미검증] s12) |
| CCCommandExecutionHiddenPoisonNode | `54110` | 0/2/0/0 | **매복·지독(계략 14)** 등록: 인수 F(유효성만)·무장 A·지역 Z, A 군단 명령서 ≥ `B718`이면 군정 30% 상한으로 `1FA5C0`, 등록 실패도 1. 효과(치안·개발 감소)는 후일 `1FC530`. 상세 rules_diplomacy.md 5.5절 [Codex 판독 2026-11-25·미검증] | 코드 |
| CGetEstrangeDataNode | `3A0C0` | 0/2/0/0 | 이간 실행 자료 조회(`6DD230` 공유). 두 번째 목록 `[1]`은 이간 목표 무장 후보(`6E2440`·`714E20`: 타 비동맹 세력의 신분 2~4 무장 등, 목록 종류 4) | 문서 참조/쓰임 (5차 정정, 출처 표시: [Sonnet 판독 2026-11-25·미검증] s12) |
| CCCommandExecutionEstrangeNode | `533F0` | 0/2/0/0 | **이간 = 계략 12** 등록(종류 10 아님): A 군단 명령서 ≥ `B720`, 군정 70% 상한. 효과(목표 충성 하위 8비트 감소)는 후일 `1FF7B0`. rules_diplomacy.md 5.5절 [Codex 판독 2026-11-25·미검증] | 코드 |
| CGetPlacationDataNode | `3DB90` | 0/2/0/0 | 계략(Placation, 이름 직역 「회유」) 실행 자료 조회(`6DD230` 공유). 두 번째 목록 `[1]`은 회유 대상 후보(`6E0ED0`; 원소 정체는 가설), 정렬 없음 | 문서 참조/쓰임 (5차 정정, 출처 표시: [Sonnet 판독 2026-11-25·미검증] s13) |
| CCCommandExecutionPlacationNode | `545D0` | 0/2/0/0 | **회유 = 계략 13** 등록: A 군단 명령서 ≥ `B72C`, 군정 50% 상한. 성공률 `1E1A60`(14용 `1E1370`과 구분), 효과(칸 소유 변경)는 후일 `1FD930`. rules_diplomacy.md 5.5절 [Codex 판독 2026-11-25·미검증] | 코드 |
| CCommandExecutionRumorNode | `2F080` | 0/2/0/0 | 유언(소문) 계략 실행(`6DD230` 공유): 계략 종류 `0x18` 요청을 등록한다. 국경 거점 적 무장 점수 내림차순 1위가 목표, 우리 무장 지력−이동일 점수 1위가 실행 무장이며 둘 다 2명 이상일 때만 등록. 인수 없음 | 문서 참조/쓰임 (5차 정정, 출처 표시: [Sonnet 판독 2026-11-25·미검증] s13) |
| CGetUnattendedhomeDataNode | `3E400` | 0/2/0/0 | 계략(UnattendedHome, 이름 직역 「빈집」) 실행 자료 조회(`6DD230` 공유). 두 번째 목록 `[1]`(종류 6)은 대상 거점 후보(`6E27C0` → `714900` 필터; 후반 가설), 정렬 없음 | 문서 참조/쓰임 (5차 정정, 출처 표시: [Sonnet 판독 2026-11-25·미검증] s13) |
| CCommandExecutionUnattendedHomeNode | `54F50` | 0/2/0/0 | **구호탄랑 = 계략 11** 등록: 도시(`C+0x4E<52`)를 `22C1F0`로 정규화한 거점을 대상으로, A 군단 명령서 ≥ `B734`, 군정 80% 상한. 등록은 결과 > 1만 저장. 효과는 후일 `2000F0`. rules_diplomacy.md 5.5절 [Codex 판독 2026-11-25·미검증] | 코드 |
| CGetFireStrategySuccessFireStrategyNode | `7EAC0` | 0/0/0/2 | 화계 성공 확률(부대 판단표; ai/roles.md 7-5) | 문서 참조/쓰임 |
| CCommandExecutionFireStrategyNode | `1F2A0` | 0/0/0/2 | 화계 실행(ai/roles.md 7-5) | 문서 참조/쓰임 |
| CCommandExecutionExpansionNode | `53790` | 1/0/0/0 | 세력 정책 패널 추가 칸: 예산 `22EC90`만큼 반복하며 종류 0..4 중 목표−현재 부족분이 최대인 종류(동점 작은 번호)의 `세력+0x70+0x1E×i`를 `min(7,old+1)`로 쓴다. 비용·난수 없음, 예산→레벨 매핑 미확정 [Codex 판독 2026-11-25·미검증] | 코드 |
| CCommandExecutionPostAutoNode | `54710` | 1/0/0/0 | 관직 자동 배치: 세력 소속 무장 중 `233BE0==0`·신분 ≠ 1·6·`234AB0==0`·`+0x15E` bit14 없음 등을 모아 모두 기본 관직(0x49) 예정으로 만들고, 계급(세력 `+0x47`)이 허용하는 관직(`world+0x784F8..` 순, 번호 ≠ 0x49)마다 보정 4항(`1EF620`)이 가리키는 목록(총합/무관/문관: **기본 u8 능력** 합 + AI 보정 `T((+0x166×C9C8+1)/10)`, 내림차순, 동점 무장 번호 오름차순, 안정)에서 첫 후보를 배정한다. 이미 그 관직을 가진 사람이 있으면 건너뜀. 적용 `1F2B10`은 무장 포인터 오름차순, 충성 변화 `d`는 하위 8비트만 반영(명령서·금 차감 없음). 읽기 실패만 2, 그 밖 항상 1. 난수 없음 [Codex 판독 2026-11-25·미검증] | 코드 |
| CCommandExecutionTradeNode | `54CE0` | 0/3/0/0 | 교역 출발 등록: 본거지 금·군량·병사가 요구량을 **모두 엄격히 초과**할 때만 `1EBC60`(행상 행동 `CCmdActionCaravan`) 호출, 발행 실패도 노드 1. 출발 거점 군단 명령서 `−목록 수×B7A8`, 본거지 자원 차감(0..상한 포화), 무장 소재 이동·`+0x15E|=1`. 난수(날짜 해시) 2회: 조언 `2F5AA0`의 `R(100,10,…)`, `vt+0x130` 뒤 `R(100,10,현재일수,첫 무장 번호,?,?)`로 행동 `+0x81`(r ≤ `B84C`→2, ≤ `B858`→3, ≤ `B864`→4, ≤ `B870`→5, 그 밖 0). 도착 후 처리는 별도 [Codex 판독 2026-11-25·미검증] | 코드 |
| CCommandExecutionPrizeNode | `2EEA0` | 0/3/0/0 | 포상: 지급 거점 `22EDF0(군단)`, 예산 B = min([1], 거점 금)에서 목록 순서대로 `B −= 100`을 먼저 하고 B > 0일 때만 대상에 포함(딱 100이면 0명, 200이면 1명). 실행 `1F3C90`: 유효 무장마다 충성 `min(100, 충성 + min(9, (75−상성)/B558 + 3 + r))`(`r = 3FDAF0(2,1,군주,대상,0,0)`, 충성 > 100이면 100으로 내려갈 수 있음), `+0x15E|=2`, 금 `−100×n`(무효 대상도 n에 포함), 군단 명령서 `−B458` **한 번**. 노드 반환: 선정 대상 수(`DAT_141B5FA08[슬롯]`)가 0이면 `1F3C90`을 부르지 않고 **2**, 1명 이상이면 `1F3C90`을 부르고(반환 무시) 1이라서 「실행 성공과 무관하게 1」은 틀림. `1F3C90`: 충성 `+0xE8 = min(100, 충성 + min(9, (75 − 상성 2A8010(지급자,대상))/B558 + 3 + 3FDAF0(2,1,지급자 +0x10,대상 +0x10,0,0)))`, 대상 `+0x15E`에 `0x2000` 비트가 있으면 충성 = `0xFF`(255), 대상 `+0x15E |= 2`, 지급 거점 금 `−100×대상 수`(`27660`) [Codex 판독 2026-11-25·미검증] / 반환·`0x2000`·충성식은 코드 확인(지휘 세션 2026-11-25; 5차 정정, 출처 표시) | 코드 |
| CCommandExecutionCreditGiveNode | `2D2A0` | 0/3/0/0 | 공적 부여: 게이트 `u64(B8B8×n) ≤ 금`(n = 원래 목록 수, 무효·중복 포함)·`B8D0 ≤ 군단 명령서`(n 곱 아님). 유효 무장만 임시 ID 목록(중복 허용)에 넣고 실행 `1ED620`: 무장마다 `+0x1BE`(s16 공적)에 `B8C4`를 가산(상·하한 포화), `0407E0==1`이고 새 공적 ≥ 기준이면 위계 `+0x1BC=2`와 `+0x1C4 = 0`, `+0x15E|=0x8000`이고 `235150(소속 세력)≠0`이면 `3218E0(무장)`도 부름(5차 정정, [Gemini 판독 2026-11-25·미검증] g53). 금 `−m×B8B8`(m = 유효 수), 명령서 `−B8D0` 한 번. 난수 없음 [Codex 판독 2026-11-25·미검증] | 코드 |
| CCommandExecutionCreditRankUpNode | `2D440` | 0/3/0/0 | 공적 승급: 게이트 `u64(B894×n) ≤ 금`·`B8A0×n ≤ 명령서`(n = 원래 목록 수). 승급 단계 `040830` = 위계표에서 `+0x2C ≤ 공적`인 최고 단계와 `현재+1`의 최솟값(한 번에 1단계), 보상 니블은 지력·정치와 통솔·무력 합 비교로 high/low 증가(동점 low). 실행은 무장 **번호 오름차순**, 유효 대상 하나라도 `1F0950` 재검사에 실패하면 그 자리에서 0 반환(앞서 쓴 것은 되돌리지 않음), 금·명령서(`B894×m`, `B8A0×m`, m = 고유 유효 수)는 끝에서만 차감. 게이트를 통과하면 `1ED8F0` 결과와 무관하게 노드는 항상 1(5차 정정, [Gemini 판독 2026-11-25·미검증] g53). 난수 없음 [Codex 판독 2026-11-25·미검증] | 코드 |
| CDistributeSpyPointNode | `550B0` | 1/0/0/0 | 군단에 첩보 포인트(군단 군정 `+0x24`) 배분(structs 3.10) | 문서 참조/쓰임 |
| CCommandExecutionLearnNode | `54330` | 1/0/0/0 | 전법 습득 실행(세력 판단표; 대상 거름은 조건 78 「전법습득가능」). 무장 `+0xE0` → 군단(`world+0xE0D0`, `40C20`)의 `+0x14`(명령서) < `DAT_141A4B5CC`이면 2(functions.md의 「관직 rank ≥ …」는 틀림) | 코드 확인(지휘 세션 2026-11-25; 5차 정정, 출처 표시) |
| CVariableGetFindItemIndexNode | `89FB0` | 0/1/0/0 | 인수 [0] 목록 종류, [1] 찾을 항목 키(종류 0xE는 정수), [2] 목록 변수 키, [3] 결과 키. 연결 목록(머리표 `1427D4140[ID×8]`)을 **앞에서부터** 돌며 8바이트 포인터가 같은 **첫** 항목의 0 기준 순번을 [3]에 쓴다(정수 목록 0xE는 4바이트 비교). 찾지 못함·항목 무효(`331780`)·읽기 실패는 2. 목록 순서가 추가 순서와 같은지 미확인 [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CGetNearCapitalNode | `1FE50` | 0/0/0/1 | 「가까운 수도」가 아니라 **이번 이동 경로 위 지역 중심 칸 보충**: `9CC90(부대, 2)`를 항상 부르고(반환 무시) 결과는 항상 1. 경유점을 `CDE60`이 시뮬레이션한 경로 위 칸 반경 2의 「소유가 다르고 거점 없는 지역 중심 칸」으로 최대 5개 다시 쓴다(상세 functions.md 3.6절 `9CC90`) [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CResolutionFakeNewsNode | `20100` | 0/0/0/1 | 위보 해소(ai/roles.md 7-5 `CF150`) | 문서 참조/쓰임 |
| CGetFakeNewsSuccessProbabilityNode | `7E9E0` | 0/0/0/1 | 위보 성공 확률(ai/roles.md 7-5) | 문서 참조/쓰임 |
| CGetSpecifiedRangeTrapListNode | `80090` | 0/0/0/1 | 범위 안 함정 목록(ai/roles.md 7-5) | 문서 참조/쓰임 |
| CCommandExecutionFakeNewsNode | `1F1D0` | 0/0/0/1 | 위보 실행(ai/roles.md 7-5) | 문서 참조/쓰임 |
| CCommandExecutionDoctrinePanelAutoNode | `52FC0` | 세력 2 | **주의(교리) 판 자동 채택, 반복 노드** — 명령 1회가 아니라 후보를 정렬해 군주 군단 명령서(`+0x14`)가 닳거나 후보가 끝날 때까지 여러 항목을 채택한다(`2EF700(군주군단, 항목, 0)`). 인수 `+0x38`≠0이면 먼저 주의 판 환불·초기화(`337380`·`236F10`; 항목 1 무료 채택), 0이면 현재 상태에서 이어 채택(세력 트리 N167 `(1)` = 월 1·7월 1일, N169 `(0)` = 그 밖의 달 1일). 읽기: 군주 군단 = `230270(세력)`, 명령서 < `DAT_141A4B6B4`(항목 1개 비용)이면 1로 끝. 후보 = 항목 2..79를 id 오름차순으로 `2C6590(군주군단, id, 0)==0`(채택 가능)인 것. 정렬 `50450` = 안정 삽입 정렬, 비교자 `50FB0` 우선순위: ① 제한 플래그(`+0x46`)≠0·칸1(`+0x3D`)≠0·칸1==군주 주의번호인 항목이 앞 ② `52480` 점수 내림차순(칸1·칸2 비용 합 + 군주 주의와 같은 칸 가산 `A6A8` + 세력 무장 최다 다른 주의 `22B360`와 같은 칸 가산 `A69C`) ③ 선호 항목 직접 일치 가산 합 내림 ④ 선호 항목 인접 효과코드 일치 가산 합 내림 ⑤ 항목 id 오름차순(완전 전순서). 선호 항목 `+0x88`/`+0x90`은 노드에 남아 다음 실행에 쓰인다(상태 있음). 끝에 채택 비트가 백업과 다르면 `229A70`이 `군주군단+0x14 = clamp(명령서 − 새 채택 비용, 0, 200)` 확정. 난수 없음. `+0x50`/`+0x54`(항목 종류 키 2개)의 출처 미확인 [Sonnet 판독 2026-11-25·미검증] | 코드 / 가설(`+0x50`·`+0x54` 출처, 루프 내 `6DE100` 3번째 인수) |
| CCommandExecutionGovernmentAutoNode | `53B80` | 세력 1 | **시정(관직) 5줄 + 군사 자동 배치**(내정 명령이 아님). 인수 `+0x38` = 대상 세력. `263520`(12.8KB, 고르기 순서 rules_domestic §8.1a)이 시정 5줄(행 0..4 × 열 0..6)의 새 배치안과 새 군사 후보를 만들고, 비용 `51FF0` = (군사 변경이면 1) + 행마다 현재 배치에 없는 무장 수의 합. 군주 군단 명령서(`+0x14`)가 0이거나 비용보다 작으면 **행 0부터 현재 배치로 되돌려** 비용이 명령서 이하가 될 때까지 줄이고(군사 변경 비용은 되돌리지 않음), 끝까지 줄여도 모자라면 결과 2(적용 없음). 적용 = 행마다 `2EFA70`, 군사는 `2F1780` 또는 해임 `2EB110`, 명령서 `+0x14 = clamp(명령서 − 비용, 0, 200)`. 군사 선택: 능력 2(지력, `231770(무장,2,0xFFE)`) ≥ `DAT_141A4B570`인 세력 무장 중 삽입 정렬 `24F570` — 능력 2 내림(엄격) → 현재 군사 가산 점수(100) 내림 → 입사년(`+0x166`) 오름 → 무장 번호 오름, 맨 앞이 새 군사. 난수 없음 [Sonnet 판독 2026-11-25·미검증] | 코드(노드·정렬·`263520` 골격, Gemini g15 + 지휘 세션 대조 2026-11-25) / 가설(행 이름 뜻, 상수 값) |
| CForceCommandMoveNode | `55310` | 군단 3 | 군단 거점 사이 무장 이동 명령(종류 1, `1F2630`)을 최대 3건 등록(골격). 인수: 객체 `+0x38` 거점 목록 L0, 정수 `+0x44`/`+0x48`/`+0x4C` = L0 소속·L0 밖·관문류(종류 `+0x4E−0x34 < 10`) 거점 가중치, `+0x50` 키 ≠ 0이면 대상 **세력**을 그 변수로 교체(기본값은 `B7210`(판단 주체 세력), 교체 결과가 무효(`331780`==0)이면 다시 `B7210`; 군단이 아님 — 코드 확인, 지휘 세션 2026-11-25; 5차 정정, 출처 표시). 거점 원소 {점수 = `231DB0`, 하한, 가중치, L0 소속 플래그}를 안정 병합 정렬 3연속(마지막이 최우선): 점수 내림 → 소속 플래그 0 먼저 → (점수 − eff) 내림, 동점은 앞 순서 유지. 원소 수 < 2이면 2. 루프(원소 수/2회, 이동 3회에서 중단): 맨 앞 A(점수−하한 ≥ 1)와 짝 B로 A의 무장(`6DA4D0`)을 `1F2630`으로 이동, 성공마다 군단 `+0x14 = clamp(명령서 − DAT_141A4B4D0, 0, 200)`. 난수 없음. [Sonnet 판독 2026-11-25·미검증 → 작성자 디컴파일 대조(`decomp_cache.py get 55310`): 평균 보정식 `(Σ무장 수 − Σ목표 인원)/(도시 수+1)`, 정렬 3회, 이동 가능 인원 식(`max(목표, 하한)` 선택), 최대 3건(`2 < 발행 수`), 명령서 소모, 2차 경로 `+0xE7 != 'I'`] **채움(이동 인원·후보 필터·보조 갈래)**: 거점 원소 = {거점 `+0x10`, 무장 수(`231DB0`) `+0x18`, 하한 `+0x1C`(도시는 도시 내 항목 수(`22BA10`, 추정)+2, 관문은 1+2), 목표 인원 `+0x20`, L0 소속 플래그 `+0x24`}. 목표 인원은 거점이 L0이면 `+0x44`, 아니면 `+0x48`, 관문류면 `+0x4C`이다(위 「가중치」는 이 목표 인원이다). 이동 중인 무장(vcall `+0x98 == 1`)은 출발 거점 무장 수에서 1을 빼고 도착 거점에 1을 더해 센다. 도시마다 목표 인원에 `max(0, (무장 수 총합 − 목표 인원 총합) / (도시 수+1))`(정수 나눗셈)을 더한다(관문 제외). 정렬 3연속 뒤 루프는 원소 수/2회, 매회 목록의 **마지막(부족이 가장 큰 곳)** 을 도착, **첫 원소**를 출발로 한다. 도착의 부족량(목표−현재) < 1이거나 반복 수가 한도를 넘으면 끝, 도착 거점 세력이 플레이어 쪽(`235150`)이면 출발 후보를 vcall `+0x78` 값이 도착과 같은 쪽 먼저로 재배치한다. **이동 가능 인원**: 출발이 L0 소속이고 도착의 현재 무장이 0명이면 `max(1, 무장 수 − max(목표, 하한))`, 도착이 비어 있지 않으면 `무장 수 − max(목표, 하한)`(하한 클램프 없음), L0 소속이 아니면 `무장 수 − 목표`; 출발 무장 수 < 2 또는 이동 가능 인원 < 1이면 실패 카운터만 올린다. **무장 선택**: 출발 거점의 무장 목록(`6DA4D0`)을 앞에서부터 보며, 컴퓨터 쪽 무장이 군단장도 거점 대표도 아니면(플레이어 쪽이거나 군단장·대표이면 군단 `+0x11`이 거점 대표 `+0x11`과 같을 때만) 후보 검증에 올리고, 관계 목록에 `233BE0 == 0`·`234AB0(,0) == 0`·`+0x15E` bit14 = 0인 다른 무장이 없으면 순회 전체를 중단하며, `22EFD0 ≠ 0`이고 `22BAB0(무장,1)`이 무효(부대 없음)면 선택 목록 꼬리에 넣는다. 선택 수는 「부족량 잔여」와 「이동 가능 인원」 두 한도에 모두 걸려 중단한다(실효 상한은 두 값 중 작은 쪽 쯤, 코드 두 비교를 합친 해석). 선택이 있으면 `1F2630(목록,0)`(새 객체 `0x78`바이트를 `world+0x871E0` 쪽 관리자에 등록, 도착 거점이 선택 무장의 소속 `+0xE4`와 다를 때만 발행)을 부르고, 발행마다 군단 `+0x14` 소모 뒤 발행 3건에서 멈춘다. **이동 0건이면 2차 경로**: 목록이 2개 이상일 때 복사본에서 원소 수/2회, 마지막을 도착으로 하여 출발 거점 대표의 `+0x14 == 0`이면 끝내고, 출발 무장 중 `+0xE7 != 'I'`(0x49, 관직 값)인 무장을 `+0xE7 == 'I'`인 무장 수만큼 골라 같은 검증 뒤 `1F2630`으로 발행한다. 소모량 `DAT_141A4B4D0`=1(rules_people.md). 명령서 이름은 이미 확정된 `+0x14` 쪽을 따른다(g31의 「행동 포인트일 가설」은 쓰지 않음) | 코드(인수·정렬·이동 인원 식·`1F2630` 경로) / 가설(하한 뜻, 2차 경로의 `+0xE7` 뜻, 선택 상한 해석) |
| CRepairNeigoborObjectNode | `200A0` | 0/0/0/1 | 이웃 건물 보수(부대 판단표) | 이름 |

## 노드 실행 함수 다섯 항목 (2026-11-25, 5차 판독)

보고서 원문(비공개, [이전 출처 안내](../../ARCHIVE_REFERENCES.md)): `San14Library/reports/2026-11-25_판독/`(`sonnet/sN.md`·`codex/cN.md`·`gemini/gN.md`, 판독 범위 표 `coverage_all.tsv`).

범위: 판단표에 쓰이는 노드 232종 = 구조 노드 5종(UNKNOWN, 위에 기록) + 실행 함수가 있는 227종이고, 227종 모두 판독 보고서가 있다(이 5차 표 + 기존 기록). 이 표는 부록 A 158종 가운데 판독 보고서가 있는 클래스(Sonnet s5~s16, Codex c9~c11·c14와 앞 차수 c3, Gemini g40~g49)와, 2차로 덧붙인 부록 A 밖 69종(Gemini g50~g55, 표 맨 끝에 RVA 오름차순)이다. 다섯 항목은 읽는 필드, 쓰는 필드, 난수, 순서·정렬·Unique, 부르는 실행 함수이고 반환을 함께 적는다. 같은 실행 RVA를 쓰는 클래스는 한 행으로 묶고, 행은 군사 → 내정·기타 순에 각각 RVA 오름차순이다(군사·내정 양쪽 클래스가 한 RVA를 공유하면 군사 쪽 행에 둔다). 노드가 아닌 부대 판단 하위 함수를 판독한 c12·c13은 이 표에 넣지 않았다. `22E2A0`은 군단이 아니라 세력(`world+0xDF30` 세력 표)을 돌려주므로 Gemini g55의 「같은 군단(`22E2A0`)」은 「같은 세력」으로 적었다. 변수 읽기·쓰기 표기는 이 문서 공통이다(객체 읽기 `B28D20`, 정수 읽기 `B28BB0`, 객체·정수 쓰기 `B29460`·`B29250`, 객체 유효성 `331780`).

확신도 표시: 「코드 확인」은 지휘 세션이 코드로 직접 확인한 것(`85EC0`의 AgentType 4=세력 `+0x20D`·3=군단 `+0x2A`·2=군세 `+0x38`, `331780` 호출은 비Unique 추가 노드 `81BF0`·`82170`·`81EB0`·`81160`에만 있고 Unique `81D30`·`822B0`·`81FF0`·`812A0`에는 없음, `548D0`이 무장 `+0xE6`==6(포로)만 고름, `92870`의 `3FDAF0` 난수)뿐이다. 그 밖은 줄마다 출처를 붙였고, 보고서가 가설이라 한 것은 「가설」, 값을 못 읽은 상수(`DAT_…`)는 「값 미확인」이다. 보고서끼리 다르면 둘 다 적고 「판독 불일치」라 썼다.

| 클래스 | 실행 RVA | 인수 | 읽는 것 | 쓰는 것 | 난수 | 순서·정렬·Unique | 부르는 함수 | 반환 | 확신도·출처 |
|---|---|---|---|---|---|---|---|---|---|
| CClearRelayHexNode | `1F1A0` | 0개 | AgentType==1 판단 주체 부대 | 경유 칸 5개를 `0xBD10`(없음)으로 초기화 | 없음 | 5칸 순서대로 | `A3370` → `2F05A0` | 항상 1 | 코드 [Gemini 판독 2026-11-25·미검증] g49 |
| CGetAttackTargetFootholdNode | `1FAA0` | `[0]` 부대, `[1]` 출력 거점 | 부대 `+0x26` 비트0, 반경 3칸의 지역·거점·적대·거리 | `[1]`에 적대 거점(없으면 0) | 없음 | 반경 3칸 순회, 성은 거리 ≤ 2·관문은 거리 ≤ 3 | `2A9C90`·`2C7400`·`2ACB80` | 1(조건 불충족·비트0 꺼짐도 `[1]`=0을 쓰고 1), 2는 `[1]` 쓰기 실패뿐 | 코드 [Gemini 판독 2026-11-25·미검증] g49 |
| CGetMyselfArmyNode | `1FE00` | `[0]` 출력 키 | AgentType | AgentType==1이면 주체(부대), 아니면 null을 `[0]` 변수에 | 없음 | — | `B29460` | 1(부대가 아니어도 null 저장 성공이면 1), 쓰기 실패 2 | 코드 [Sonnet 판독 2026-11-25·미검증] s8 |
| CCautionArmyAddUniqueNode | `283F0` | `[0]` 적 부대, `[1]` 거점, `[2]` 경계부대 목록(종류 0xF) | 목록의 같은 적 부대 번호, 거점 소유 세력 | 빈 경계부대 슬롯에 적 부대·거점을 채워 목록에 추가 | 없음 | 적 부대 번호로 중복 검사 후 추가(Unique) | `2CB6C0`(자기 거점 칸 위면 실패)·`26D660`(거점 소유 세력이 다를 때 외교 검사) | 1(이미 있거나 등록 성공), 2(인수 읽기 실패·`2CB6C0`≠0·부대 무효·거점 소유 세력 0·목록 생성 실패·빈 슬롯 없음) | 코드 [Gemini 판독 2026-11-25·미검증] g47 |
| CCautionTroopsClearNode | `28CC0` | `[0]` 경계군세 | — | 경계군세 삭제 | 없음 | — | `32D180` | 1(객체가 0이어도 읽기 성공이면 1), 읽기 실패 2 | 코드 [Gemini 판독 2026-11-25·미검증] g48 |
| CCautionTroopsListAddNode | `28D20` | `[0]` 경계군세 목록(종류 0xB), `[1]` 부대 목록, `[2]` 대상 거점, `[3]` 출력 | 부대 목록, 기존 경계군세의 부대, `26D660` | 빈 슬롯(`world+0x80BA8`, 500칸)을 잡아 부대 목록 복사·세계 등록(`320F90`), 새 경계군세를 `[3]`에 씀 | 없음 | 중복 부대·외교 검사 | `320F90`·`26D660`·`B29460` | 1, 2(읽기·생성 실패·500칸 만석·부대가 기존 경계군세에 이미 있음·거점 무효) | 코드 [Gemini 판독 2026-11-25·미검증] g49 |
| CCautionTroopsListAddUniqueNode | `29190` | `[0]` 경계군세 목록, `[1]` 순번(정수 키), `[2]` 부대 | 목록 길이(순번이 음수여도 부호 없는 비교로 길이 이상이면 2) | `[1]`번째 경계군세 `+0x30` 목록의 꼬리에 부대 추가 | 없음 | 부대 포인터 일치로 중복 검사, 꼬리 추가 | — | 1(이미 있거나 추가), 2(읽기 실패·순번 범위 밖·부대 무효) | 코드 [Gemini 판독 2026-11-25·미검증] g48 |
| CCautionTroopsListRemoveNullUnit | `29390` | `[0]` 경계군세 목록 | 경계군세마다 소속 부대 | 무효·퇴각(명령 `+0x37`==0xB·0xC) 부대 제거, 부대 0개가 된 경계군세 삭제 | 없음 | 목록 순서 | `32D180` | 1, 목록 읽기 실패 2 | 코드 [Gemini 판독 2026-11-25·미검증] g48 |
| CCautionTroopsRemoveNode | `29990` | `[0]` 경계군세, `[1]` 부대 | `+0x30` 목록(핸들)과 `+0x28` 목록 | 부대가 `+0x30` 목록에 있으면 `+0x28` 목록에서 제거 | 없음 | 같은 포인터 전부 제거 | `21A350` | 1(부대가 목록에 있든 없든), 2(읽기 실패·`331780`==0) | 코드 [Gemini 판독 2026-11-25·미검증] g49 |
| CCautionTroopsSortNode | `29A90` | `[0]` 경계군세 객체 하나(목록 아님) | `+0x28` 목록 핸들, 부대 `+0x12` 대장 ID, 대장 `+0xE7`·`+0xE0`·`+0xEA`·능력, 관직 `+0x34`, 군단장 `+0x12`, 세력의 군주 | `+0x28` 목록의 연결 순서만 | 직접 호출·읽은 정렬 본문에 없음(관직 가상 getter 내부는 미판독) | ① 부대 `+0x12` 오름 ② 대장 `+0xEA` ③ `231770(대장,1,0xFFF)` ④ `231770(대장,0,0xFFF)` ⑤ `259D0` 관직 key 내림, 모두 엄격 비교 안정 삽입, 마지막 정렬이 최우선. ②③④는 **내림**(코드 확인 — 지휘 세션 2026-11-25: ① `22DB0`은 `key(X) < key(prev)`이면 X를 앞으로(오름), ② `23500`·③ `23730`·④ `23290`은 `key(prev) < key(X)`이면 X를 앞으로(내림), 모두 `≤`에서 멈추는 안정 삽입; 첫 판독 Codex c14, 앞 차수 Sonnet 「오름」은 틀림). ⑥⑦은 정렬이 아니라 조건 분할 이동: 변환 = `reverse(시작 목록[1:] 중 조건 참) + [시작 머리] + (조건 거짓)`, ⑥ 조건 = 대장 ID가 대장 군단의 군단장 ID, ⑦ 조건 = 대장 ID가 군주 ID, ⑥ 결과에 ⑦을 적용, 시작 머리는 검사 대상이 아님. 단순 합성 키로 쓰면 머리 예외와 역전이 사라져 틀림 | `22D30` → `23480` → `236B0` → `23210` → `22B80` → `22EA0` → `23050`(래퍼) | 1, 객체 읽기 실패 2(유효성 검사 없음) | 코드(정렬·방향·역전) / 가설(관직 vtable `+0x58` 효과) [Codex 판독 2026-11-25·미검증] c14 |
| CCautionTroopsUpdateStatusNode | `29B40` | `[0]` 경계군세, `[1]` 정수 직접값 | 경계군세 | 경계군세 `+0x3C = ([1] == 1)` | 없음 | — | — | 1, 2(읽기 실패·`331780`==0) | 코드 [Gemini 판독 2026-11-25·미검증] g48 |
| CCommandAutoPaintDefenseDepartureNode | `2CBC0` | `[0]` 대상 거점(도시) | 거점 `+0x4E`, 11개 경계 거점 조건, 적 군세 경로 | 종류 `0x17` 자동 방어 출진 | 없음 | 경계 거점 11곳 `switch` | `27920`·`276C0`(경로 확인)·`28030`(출진) | 1(거점 `+0x4E` > 0x33·군단 `+0x14`==0·미해당 거점·이미 그 지역 소유 등), 2(읽기 실패·무효) | 코드(`28030` 내부 일부 미확인) [Gemini 판독 2026-11-25·미검증] g48 |
| CCommandTransportDepatureNode | `32D90` | `[0]` 출발(공급) 후보 목록, `[1]` 도착 후보 목록, `[2]`~`[4]` 최소 잔류 군량·금·병사 기준 | 군단 `+0x14` 플래그, 목록 길이 | 수송 부대 출진, 군세 `+0x14 = 0xC`·`+0x16 = 목표 거점 번호` | 없음 | 부족·잉여 거점 정렬·매칭: 도착 후보 정렬 `21840`(`25BF0`)·`219A0`(`25CE0`), 공급 거점 기준 정렬 `216E0`(`25B10`) — ai/roles.md 2-3-6 | `201C20` | 1(부족한 도착 후보 ≥ 1 수집 뒤 계획·실행 루프 완료), 2(군단 플래그 0·목록 읽기 실패·길이 0·후보 0) | 코드 [Gemini 판독 2026-11-25·미검증] g47 |
| CGetBuildingDestructionDataNode | `370D0` | `[0]` 출력 무장 목록(종류 4), `[1]` 출력 지역 목록(종류 6) | 판단 주체 군단(`B7170`) | 두 목록을 확보·비운 뒤 후보를 채움 | 없음 | — | `6DD230`(무장)·`6E08E0`(지역) | 1, 2(목록 확보 실패) | 코드(`6DD230`·`6E08E0` 본문 미확인) [Gemini 판독 2026-11-25·미검증] g48 |
| CGetFacilityCandidateHexListNode | `3A200` | `[0]` 지역 R, `[1]` 무장 P, `[2]` 시설 정의 번호(정수 즉값, `BB500`), `[3]` 출력 HEX 목록(종류 7), `[4]` 거점 후보 컨테이너, `[5]` 시설 정의 대체 포인터, `[6]` 경로 방향 플래그 F(읽기 실패 0) | P `+0xE2`·거점 `+0xB0`·`+0xA8`, 칸 `+0x10`·`+0x12`, 정의 `+0x2C`·`+0x32` | 출력 목록(진입 때 비우고 필요 시 `1A250`으로 생성)에 칸 추가 | 없음(`23BE0`·`23EF0`·`27A8D0` 등에도 없음, 경로 엔진 내부는 미확인) | A 갈래(F==0이고 R이 진입 지역이 아님): 지역·인접 지역의 기존 시설 반경 1칸. B 갈래: 기점 → 지역(F≠0이면 반대) `185710` 경로, 경로 앞부터 처음 R 소속인 칸 E, 정의 `+0x2C`==3이면 `23BE0`(비대칭 비교 `before`), E 유효하면 `23EF0` 거리 오름 안정 삽입(동점은 `23BE0` 결과 유지), `27A8D0` 재필터, 지역 중심 칸 제외 | `185710`·`27A8D0`·`23BE0`·`23EF0`·`BB500`·`BF1B0` | 1(경로 성공이면 0개도 1, A 갈래에서도 조기 1), 2(인수·정의·기점 무효·출력 생성 실패·경로 실패) | 코드(경로 뒤 고르기) / 가설(`27A8D0`의 생략 인수) [Gemini 판독 2026-11-25·미검증] g49, [Codex 판독 2026-11-25·미검증] c14 |
| CGetSpecifedStrategyDistrictTroopsNode | `3DDB0` | `[0]` 정수 직접값 K(군세 종류), `[1]` 출력 군세 목록 | 주체 군단(`B7170`), 군세 `+0x14`(u16) | 출력 목록을 매 실행 비운 뒤 채움(키가 없으면 생성) | 없음 | 슬롯 오름차순, 정렬·중복 제거 없음 | `B7170`, 술어 `335350`(추정) | 1(비어도), 2(군단 무효·AgentType 4 등·목록 못 얻음) | 코드(술어 추정) [Sonnet 판독 2026-11-25·미검증] s8 |
| CCommandExecutionAttackRequestNode | `52CA0` | `[0]` 요청받는 세력 T, `[1]` 사자 무장 W, `[2]` 대가 종류 k, `[3]` 대가 값(k=0·1 정수, k=2 객체 명품, k=4 객체 지역), `[4]` 목표 거점 B | T의 군단(`230270`) `+0x14` ≥ `DAT_141A4B668`, 세력 관계 | 세력에 사자 파견·대가를 먼저 차감, 응답 뒤 공격 요청 필드·우호도·대가 정산 | 사전 조언 해시 1~2회, 응답의 방어 목표·수락 해시 | — | `1EE460(Q,0)`·`230270`·`823E50`·`81F290` | 1(접수 거절·자원 부족·응답 거절도 노드는 1), 2(읽기 실패·T/W/B 무효·T 군단 명령서 부족·k별 `[3]` 읽기 실패) | 코드; 군정 협상 실수식·일부 확장 분기 미확정 [Codex 판독 2026-11-25·미검증] c9 |
| CCommandExecutionBuildingDestructionNode | `52EC0` | `[0]` 세력(읽기만), `[1]` 실행 무장 W, `[2]` 대상 지역 A | 군단 `+0x24`(군정) 투입량 `1E0110` | 지역 파괴 계략(종류 `0x14`) 제출·군정 소모·사자 임무; 결과별 시설 내구 감소·등급 2 추가 파괴·삭제 대기열 | 하위 계산에서 `3FDAF0` 반복, 전역 상태형 직접 호출 없음 | — | `1FA5C0` | 1(세 읽기가 성공하면 접수 여부와 무관), 2(읽기 하나라도 실패) | 코드; 실수 성공률·큰 목록 동점 정렬·숨은 인수 미확정 [Codex 판독 2026-11-25·미검증] c9 |
| CCommandExecutionDualDestructionNode | `53270` | `[0]` 유효성만 볼 객체, `[1]` 실행 무장, `[2]` 대상 A, `[3]` 대상 B | 실행 무장 군단(`40C20`) `+0x14` ≥ `DAT_141A4B740` | 종류 10(이호경식) 명령 등록, 비용 `1E0110` | 없음 | — | `1E0110`·`1FA5C0` | 1(`1FA5C0`까지), 2(읽기 실패·무효·명령서 부족) | 코드 [Gemini 판독 2026-11-25·미검증] g49 |
| CArmySetArmyActionNode | `61B10` | `[0]` 부대, `[1]` 행동 번호(정수 직접값) | — | 부대 행동 번호 | 없음 | — | `2ECEA0` | 1, 2(읽기 실패·`331780`==0) | 코드 [Gemini 판독 2026-11-25·미검증] g47 |
| CArmySetRetreatNode | `61C90` | `[0]` 부대 | 부대가 자기 거점 위인지(`2CB6C0`) | 거점 위면 행동 `0xD`·목표 `9`(`+0x48`), 아니면 `2EC570(부대,1,0,…)` 퇴각 | 없음 | — | `2CB6C0`·`2EC570` | 1, 2(읽기 실패·null) | 코드 [Gemini 판독 2026-11-25·미검증] g49 |
| CExecuteAutoPaintDefenseNode | `69240` | 0개(판단 주체=군세) | 군세 종류 `0x17`, 목표 지역 소유, 하드코딩 10개 지역 표 | 목표 지역이 아군이거나 짝 공격 군세(`70FB0`)가 없으면 군세 종류 0 | 없음 | 지역 표 순서 | `70FB0` | 항상 1 | 코드 [Gemini 판독 2026-11-25·미검증] g49 |
| CGetMyselfTroopsInfoNode | `6D310` | `[0]` 항목 번호 0..15(정수 직접값), `[1]` 출력 키 | `B72F0`로 얻은 군세 | 항목별 정수·객체·목록 변수 | 없음 | — | `B72F0` | 1, 2(군세 무효·항목 범위 밖·목록 생성·쓰기 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g47 |
| CGetMyselfTroopsNode | `6E760` | `[0]` 출력 키 | `B72F0` | 현재 군세 객체를 변수에 | 없음 | — | `B72F0`·`B29460` | 1(쓰기 성공), 2 | 코드 [Gemini 판독 2026-11-25·미검증] g47 |
| CSetRelayHexListNode | `6EE30` | `[0]` 군세, `[1]` 칸 목록 | 칸 목록(핸들 `+8`) 앞 10칸, 군세 소속 첫 부대(`224950`) | 군세 `+0x18..+0x2B` 10칸을 `0xBD10`으로 비운 뒤 칸 번호 u16 직접 쓰기 | 없음 | 목록 앞에서 최대 10칸 | `0xBD10` 초기화, `22F4A0`(반환 안 씀) | 1, 2(읽기 실패; `331780` 검사 없음) | 코드 [Gemini 판독 2026-11-25·미검증] g49 |
| CMiscSetFootholdEvaluationNode / CSetFormationEvaluationNode / CSetCautionTroopsEvaluationNode / CSetTacticsBookEvaluationNode(+ CMiscSetPersonEvaluationNode·CSetTroopsEvaluationNode도 같은 RVA) | `6EFD0` | `[0]` 대상 객체, `[1]` 정수 점수 | `[0]` 객체 포인터 ≠ 0 | `[0]` 객체 `+0x08`에 4바이트 정수 | 없음 | — | `B28D20`·`B28BB0`(`331780` 호출 없음) | 1, 2(읽기 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g47 |
| CTroopsOrderDesutructionFacilityNode | `6F5F0` | 0개(판단 주체=군세) | 대표 부대 → 거점 `185710` 경로의 아군 지역·시설·반경 5칸 적 부대 | 군세 `+0x14 = 4`·`+0x16 = 시설 번호`, 부대 명령 `6`/`0xB` | 없음 | 지역 순회: 한 지역에서 첫 적합 시설을 찾으면 그 지역 칸 순회를 끝내고 다음 지역으로, 뒤 지역의 적합 시설이 앞 선택을 덮어씀 | `185710` | 1(적합 시설 ≥ 1), 2(부대 목록 비음·대표 부대 진형 `+0x1B`==7 또는 병력 ≤ 999·길찾기 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g49 |
| CAttackRequestSuccessConditionNode | `7AC40` | `[0]` 요청받는 세력(플레이어여야 함), `[1]` 사자 무장, `[2]` 대가 종류 k, `[3]` 출력(k=0·1 정수, k=2 명품 객체), `[4]` 목표 거점, `[5]` 남길 양 외(7개) | 플레이어 세력 비교(`330B90`), 보유 잔액, 남길 양(양수 입력은 보유량 전체로 치환) | `[3]`에 대가 양 또는 명품 객체 | 확인된 본문에 없음(확률 추첨 노드가 아님) | — | `9DB10`·`330B90`·`230350` | 1(k=2 출력 성공·k=0·1 잔액이 기준보다 엄격히 클 때), 2(필수 읽기 실패·무효·플레이어 세력 아님·`9DB10` 거짓·잔액 조건 실패·쓰기 실패) | 코드; 변수표 번호·일부 하위 getter 미확정 [Codex 판독 2026-11-25·미검증] c9 |
| CGetAdvantageOwnFootholdNode | `7B1B0` | `[0]` 거점, `[1]` 정수 출력 | 거점이 속한 주의 이점 거점 목록, 소유 세력 | 같은 주 안 판단 주체 소유 거점 개수를 `[1]`에 | 없음(확인 본문) | — | `22C1F0`·`B29250` | 1(쓰기 성공), 2(읽기 실패·거점 무효·`22C1F0` null·쓰기 실패) | 코드; 변수표 번호 미확정 [Codex 판독 2026-11-25·미검증] c9 |
| CGetAllFootholdNeedFoodNode | `7B450` | `[0]` 군단, `[1]` p2=24, `[2]` p3=6, `[3]` p4=6/4/8(N13 6·N15 4·N17 8) | 군단 세력의 소유 거점마다 병력 합·거점 `+0xA4`·현재 군량·오는 수송 군량(도시는 군단 `+0x10`/`+0x11` 조건 `22E760`도 만족해야 함) | 거점 `+0x94 = ((병력합×p2/100)×p3 − (거점 +0xA4/3)×p4) − 현재 군량 − 오는 수송 군량`(`9F410`) | 없음 | 거점 순회 | `9F410`·`2695D0`·`2B4CA0`(의미는 가설)·`331780` | 항상 1(거점 0개여도), 2(군단 읽기 실패·`331780(군단)`==0) | 코드(`2695D0`·`2B4CA0` 의미는 가설) [Sonnet 판독 2026-11-25·미검증] s8 |
| CCGetAllFootholdNeedMoneyNode | `7B590` | `[0]` 군단, `[1]` p2=6/4/8(N20 6·N22 4·N24 8) | 같은 순회: 현재 금·거점 `+0xA0`·오는 수송 금 | 거점 `+0x98 = -(현재 금 + p2×(거점 +0xA0/3) + 오는 수송 금)`(`9F670`, 음수 방향) | 없음 | 거점 순회 | `9F670`·`331780` | `7B450`과 같음(1 / 2) | 코드 [Sonnet 판독 2026-11-25·미검증] s8 |
| CGetArroundEnemyListNode | `7BA50` | `[0]` 중심 부대, `[1]` 반경(정수 직접값), `[2]` 출력 부대 목록(종류 3) | 입력 부대 세력(`22E690`)과 주변 부대 세력 | 적대 부대 목록(적대 0개여도 1) | 없음 | 반경 칸 순회 | `B9A00`·`2CC630`·`22E690` | 1, 2(읽기 실패·무효·목록 생성 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g47 |
| CGetFormationNode | `7EEE0` | `[0]` 진형 번호(정수 직접값), `[1]` 출력 진형 객체 | `BE040`의 명시적 `if` 분기 매핑 | 유효하면 출력 키에 저장 | 없음 | — | `BE040`·`B29460` | 1, 2(무효·쓰기 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g48 |
| CGetHexAroundFightingStrengthNode | `7EF50` | `[0]` 중심 칸, `[1]` 출력 전투력 합, `[2]` 출력 병력 합, `[3]` 반경(정수 직접값), `[4]` 기준 세력, `[5]` 출력 부대 목록(종류 3) | 반경 칸의 같은 세력 부대, 부대 `+0x16` 병사 | `[1]`·`[2]` 정수, `[5]` 목록 | 없음 | 반경 칸 목록에 중심 칸 포함(`2A9C90` 뒤 없으면 꼬리 추가) | `2A9C90`·`18D50` | 1, 2(읽기·`331780`·목록 확보 실패) | 코드 확인(중심 칸 포함, 지휘 세션) / 그 밖 [Gemini 판독 2026-11-25·미검증] g47 |
| CGetPersonFormationParamNode | `7F5E0` | `[0]` 무장, `[1]` 평가 종류(정수 직접값), `[2]` 출력 진형 객체, `[3]` 출력 점수 | 무장 가용 진형(0~19, `233CF0`) | 최고 점수 진형·점수 | 없음 | 진형 순서대로 최고 점수 | `C00E0` | 1, 2(읽기·`331780`·쓰기 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g47 |
| CGetSpecifiedArmyFlagArmyListNode | `7FC10` | `[0]` 군세, `[1]` 플래그 번호(판단표는 6), `[2]` 출력 부대 목록(종류 3) | 군세 소속 부대(`22BB50`), 부대 `+0x26` 비트 | 출력 목록(비운 뒤 추가) | 없음 | 플래그 0~5는 `break` 없이 아래 `case`로 fall-through, 6은 `2CB6C0`==0 이고 비트1 꺼짐 | `22BB50`·`2CB6C0` | 1, 2(군세 읽기 실패·무효·목록 확보 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g48 |
| CGetTransportSoldierNode | `804F0` | `[0]` 거점 목록, `[1]`~`[3]` 정수 직접값 24·6·6 | 목록의 거점마다 `9F410`·`vtable+0xC8` | 거점 `+0x90`에 수송 병력 값: `9F410` < 1이면 `vtable+0xC8`을 0 이상으로, ≥ 1이면 0 이하(`min(0,v)`)로 클램프 | 없음 | 목록 순서 | `D3A90`·`9F410`(본문 미확인) | 1, 2(읽기 실패·목록 포인터 0) | 코드(`9F410` 미확인) [Gemini 판독 2026-11-25·미검증] g48 |
| CGetUserArmyListNode | `80560` | `[0]` 명령 번호(정수 4), `[1]` 출력 부대 목록(종류 3) | 플레이어 세력(`330B50`)의 군단 부대, 명령 `+0x37`, `2CB6C0`, `234DE0` | 출력 목록(비운 뒤 꼬리 추가) | 없음 | 부대 순서, 조건 = 명령 `+0x37`==`[0]` 이고 `2CB6C0`==0 또는 `234DE0`==0 | `330B50`·`224710`·`2CB6C0`·`234DE0` | 1, 2(목록 확보 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g48 |
| CListAddArmyNode | `81420` | `[0]` 부대, `[1]` 목록(종류 3) | 변수 항목, 목록 ID | 목록이 없으면 생성, 풀 노드 추가 | 없음 | 꼬리 추가(`18D50` 플래그 1), 중복 허용, 정렬 없음 | `18D50`·`1A250` | 1, 2(읽기·목록 생성 실패) | 코드 [Sonnet 판독 2026-11-25·미검증] s5 |
| CListAddArmyUniqueNode | `81550` | `[0]` 부대, `[1]` 목록(종류 3) | 변수 항목, 풀 머리 체인 | 중복이 없을 때만 풀 노드 추가 | 없음 | 포인터(8바이트) 일치로 중복 검사 후 꼬리 추가, 중복이면 추가 없이 1 | `18D50`·`1A250` | 1, 2 | 코드(`331780` 없음) [Sonnet 판독 2026-11-25·미검증] s5 |
| CListAddCautionTroopsNode | `816D0` | `[0]` 경계군세, `[1]` 목록(종류 0xB) | 변수 항목 | 풀 노드 추가 | 없음 | 꼬리 추가, 중복 허용 | `18D50`·`1A250` | 1, 2 | 코드 [Sonnet 판독 2026-11-25·미검증] s6 |
| CListAddFootholdNode / CListAddFootholdUniqueNode | `81BF0` / `81D30` | `[0]` 거점, `[1]` 목록(종류 5) | 변수 항목, 목록 ID | 목록이 없으면 생성, 풀 노드 추가 | 없음 | 둘 다 꼬리 추가. `81BF0`은 중복 허용이고 추가 직후 `331780(원소)`(원소 vtable `+0x18` 호출, 결과 안 씀·상태 변경 여부 미확인)을 부름. `81D30`은 8바이트 같은 항목이 있으면 추가 없이 1이고 `331780`을 부르지 않음 | `18D50`·`1A250`·(`81BF0`만) `331780` | 1, 2(읽기 실패·목록 생성 실패) | `331780` 호출 여부는 코드 확인(지휘 세션 2026-11-25), 나머지는 [Sonnet 판독 2026-11-25·미검증] s5 |
| CListAddHexNode | `82170` | `[0]` 칸, `[1]` 목록(종류 7) | 변수 항목 | 풀 노드 추가 | 없음 | 꼬리 추가, 중복 허용, 추가 뒤 원소 vtable `+0x18` 호출(반환 버림) | `18D50`·`331780` | 1, 2 | `331780` 호출은 코드 확인(지휘 세션 2026-11-25), 나머지 [Sonnet 판독 2026-11-25·미검증] s6 |
| CListAddHexUniqueNode | `822B0` | `[0]` 칸, `[1]` 목록(종류 7) | 변수 항목 | 같은 8바이트 값이 없을 때만 추가 | 없음 | 중복이면 추가 없이 1, 아니면 꼬리 추가 | `18D50` | 1, 2 | `331780` 없음은 코드 확인(지휘 세션 2026-11-25), 나머지 [Sonnet 판독 2026-11-25·미검증] s6 |
| CListAddPossibleFacilityNode | `828A0` | `[0]` 무장 W, `[1]` 칸 H, `[2]` 출력 목록 L(종류 0x10 시설 정의) | W 소속 군단(`40C20`), 칸 `+0x10` 지형·`+0x1A` 시설 ID·`+0x1E` 명승 ID, 시설 정의 | 시설 정의 0..30 가운데 후보를 목록 뒤에 추가, 플레이어 군단 허용 비트(`+0x1C`)로 포인터 제거 | 확인된 본문에 없음 | 정의 번호 순서대로 후보 | `27A8D0`·`40C20`·`1A250` | 1(후보 0개·할당 실패도 1), 2(W/H 읽기 실패·무효·L 확보 실패) | 코드; 목록 초기화 수신자·슬롯·사용처 미확정 [Codex 판독 2026-11-25·미검증] c9 |
| CListAddTacticsBookNode | `82C70` | `[0]` 전법서, `[1]` 목록(종류 0x11) | 변수 항목 | 풀 노드 추가 | 없음 | 꼬리 추가, 중복 허용 | `18D50`·`1A250` | 1, 2 | 코드 [Sonnet 판독 2026-11-25·미검증] s6 |
| CListAddTroopsUniqueNode | `83020` | `[0]` 군세, `[1]` 목록(종류 2) | 변수 항목 | 중복이 없을 때만 추가 | 없음 | 중복 없이 꼬리 추가 | `18D50`·`1A250` | 1, 2 | 코드 [Sonnet 판독 2026-11-25·미검증] s6 |
| CListAddUniqueCautionTroopsNode | `831A0` | `[0]` 경계군세, `[1]` 경계군세 목록(종류 0xB) | 변수 항목, 목록 핸들 | 포인터 중복이 없을 때 꼬리에 추가 | 없음 | 포인터 중복 검사(핸들 `+8`이 널이면 조회 없이 추가) | `18D50`·`1A250` | 1(이미 있어도), 2 | 코드 [Gemini 판독 2026-11-25·미검증] g47 |
| CListRemoveFootholdNode / CListRemoveCautionTroopsNode(+ CListRemovePersonNode·CListRemoveForceNode도 같은 본문) | `84BC0` | `[0]` 값(8바이트 포인터), `[1]` 목록 | 변수 항목 2개, 목록 ID, 머리 체인 | 목록에서 같은 값 항목 전부 제거(남은 순서 유지) | 없음 | 머리부터 확인한 뒤 `21A350`으로 같은 값 전부 제거(이중 순회), 종류 검사 없음, 목록을 새로 만들지 않음 | `21A350` → `189B0` | 항상 1(목록에 없어도), 읽기 실패 2 | 코드 [Sonnet 판독 2026-11-25·미검증] s5 |
| CMiscSetHexEvaluationNode(+ CSetForceEvaluationNode·CMiscSetAreaEvaluationNode도 같은 RVA) | `85580` | `[0]` 평가 객체, `[1]` 정수 점수 | `[0]` 객체 ≠ null | `[0]` 객체 `+8`에 `[1]` | 없음 | — | `B28D20`·`B28BB0` | 1, 2 | 코드 [Gemini 판독 2026-11-25·미검증] g49 |
| CRemoveNoInterceptPersonNode | `85810` | `[0]` 무장 목록 | 통솔(`231770`)·진형 1..19 가용 | 부적합 무장을 임시 목록에 모아 원목록에서 제거 | 없음 | 통솔 < 21이거나 유효 육상 진형(1..19, ≠ 7, 비트1=0)이 없는 무장 제거, 남은 순서 유지 | `231770`·`233CF0`·`21A350` | 1(빈 목록도), 2(읽기 실패·목록 0) | 코드 [Gemini 판독 2026-11-25·미검증] g48 |
| CSelectPersonTacticsNode | `85BE0` | `[0]` 무장, `[1]` 진형, `[2]` 출력 전법 목록(종류 0xD) | 전법 표(1~199), 진형 허용, 무장 보유 | 전법 최대 3개 | 없음 | 전법 표 2회 순회 | `235090`·`93770`·`22BD60` | 1(3개 미만이어도), 2 | 코드 [Gemini 판독 2026-11-25·미검증] g47 |
| CSetCautionTroopsVirtualTargetFootholdNode | `85F70` | `[0]` 경계군세, `[1]` 거점 | 거점 `+0x4E` | 경계군세 `+0x1A = min(거점 +0x4E, 0x3D)` | 없음 | — | — | 1(두 읽기 성공이면, 값 0이어도), 2 | 코드 [Gemini 판독 2026-11-25·미검증] g49 |
| CVariableGetCautionArmyInfoNode | `88140` | `[0]` 경계부대, `[1]` 항목 0..4(정수 직접값), `[2]` 출력 | 경계부대 레코드 | 항목 0 번호·1 전력·2 거점·3 적 부대·4 평가를 `[2]`에 | 없음 | — | `B6F50`·`32E3B0` 등 | 1, 2(읽기·`331780`·범위 밖·쓰기 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g47 |
| CCommandExecutionFakeNewsNode | `1F1D0` | `[0]` 실행 부대, `[1]` 대상 부대, `[2]` 대상 칸 | 부대 `+0x13E`·`+0x140`(보류) | `2EF910` 호출: 부대 행동 `0x11`, 목표(`0x1B`, 대상 번호), `+0x13E` 칸(`+0x140`==0일 때) | 없음 | — | `2EF910` | 1(내부에서 아무것도 안 써도 1), 2(읽기 실패·`[0]` 무효) | 코드 [Sonnet 판독 2026-11-25·미검증] s16 |
| CCommandExecutionFireStrategyNode | `1F2A0` | `[0]` 부대, `[1]` 칸 | 칸 `+0x16` | 칸 `+0x16`==0이면 부대 행동 `0x10`·목표 종류 9·칸 번호(`+0x140`==0일 때), 경로 재계산 | 없음 | — | — | 2(칸 `+0x16` ≠ 0), 그 밖 1(읽기 실패 반환을 검사하지 않고 진행, 칸 포인터 0이면 크래시하나 판단표상 도달 불가 — 가설) | 코드 [Sonnet 판독 2026-11-25·미검증] s14 |
| CGetNearCapitalNode | `1FE50` | 인수 없음 | AgentType, 이번 이동 경로 위 칸 반경 2의 지역 소유·거점 | 경유점(기존 경로상 경유점 + 새 중심 칸, 최대 5)을 다시 씀 | 없음 | — | `9CC90(부대,2)`(반환 무시) | 항상 1 | 코드 [Sonnet 판독 2026-11-25·미검증] s15 |
| CRepairNeigoborObjectNode | `200A0` | 판단표 인수 없음(부대는 호출 규약의 3번째 인수) | AgentType==1 부대의 행동 13·1, 목표 칸 고리 1 안 자기 세력 비거점 시설 내구 | 첫 시설에 수리 명령(`+0x37`=9, 목표 0xB·시설 번호), 임시 추격 목표 초기화 | 없음 | 첫 해당 시설 | — | 수리 명령을 썼으면 1, 그 밖 2 | 코드 [Sonnet 판독 2026-11-25·미검증] s16 |
| CResolutionFakeNewsNode | `20100` | `[0]` 대상 부대 T, `[1]` 나(M), `[2]` 정수 상수 n | — | `CF150(M,T,n)`: 더 빠른 내가 함정으로 가는 대상의 예측 위치로 `CF570` 경유점 끼우기 | 없음 | 반복 12n은 해석 | `CF150`·`CF570` | 1(`CF150` ≠ 0), 2(읽기 실패·무효·`CF150`==0) | 코드(반복 12n은 해석) [Sonnet 판독 2026-11-25·미검증] s15 |
| CCommandExecutionInspectNode | `2DCD0` | 인수 없음 | 군단 `+0x24`(군정, 부호 있음) ≥ 500, 거점 후보 ≥ 2·무장 후보 ≥ 2, 위협·인원·충성·치안 점수, 무장 지력·이동일 점수 | 순시(kind `0x19`) 제출, 명령서·금(군단장 거점)·군정 소비 | 해시형 `3FDAF0(100,1,…)` 1회(기간 10/20/30일) | 점수 내림차순(안정) 첫 거점, 점수 최고 무장 | `B7170`·`1FA1B0` | 1(군정 < 500·후보 < 2·실행 뒤), 2(군단 무효·후보 객체 무효) | 코드(이웃 조건 의미 가설) [Sonnet 판독 2026-11-25·미검증] s11 |
| CCommandExecutionMerchantNode | `2E410` | `[0]` 도시, `[1]` 정수 직접값 L, `[2]` 금 과부족 g, `[3]` 군량 과부족 f, `[4]` 후보 무장 목록 | 게이트 `70FF80`, 군단 명령서, 거점 `+0xC9`, 거래량 상한 | `1F2370`으로 금·군량 이동·명령서 −`B44C`·거점 `+0xC9` bit2·무장 `+0x15E` | 없음 | 후보 순서대로 가능 무장 채택(최대 10명), 같은 거래량이면 마지막 1명 제거는 방향 1(매입)에서만 | `70FF80`·`4FCA0`·`1F2370` | 1(`1F2370`을 부른 경우만), 2(게이트·목록·명령서 0·g/f 부호 조건 등) | 코드(매각 cap 단위·상수 값은 가설) [Sonnet 판독 2026-11-25·미검증] s9 |
| CCommandExecutionRumorNode | `2F080` | 인수 없음 | 국경 거점의 적 무장 점수, 우리 무장 지력−이동일 점수 | 유언(kind `0x18`) 요청 등록 | 노드 본문 해시형 1회(결과 무시)·하위 해시형 `3FDAF0`, 전역 상태형 없음 | 적 무장 점수 내림차순 1위=목표, 우리 무장 점수 1위=실행 무장, 둘 다 2명 이상일 때만 | `6DD230`계·`6E1F40`(일부 가설)·`1F1540` | 1(실행 또는 후보 부족), 2(군단 무효·무장 무효·요청 무효) | 코드 / 가설(능력치 이름, `6E1F40` 일부) [Sonnet 판독 2026-11-25·미검증] s13 |
| CDomesticOfficerSetNode | `36E80` | `[0]` 지역 R, `[1]` 무장 P, `[2]` 방침 v(정수 키) | 군단 명령서, `2ABF60(P,2)`, `43800` | `1EE630` 실행: 담당 0..6000·방침 0..3, 명령서 −`B428`×변경 수(0..200) | 없음 | 필요할 때만 기존 지역 1개를 해제 항목으로, 새 항목 추가 | `1EE630`·`2ABF60`·`43800` | 이미 같으면 1, 명령서 < `B428`이면 2, 키가 0이거나 v==0이면 2, 그 밖 1 | 코드(일부 인수 표기 가설) [Sonnet 판독 2026-11-25·미검증] s10 |
| CGetEmployDataNode | `39FF0` | `[0]` 무장 목록(변수 284, 종류 4) | 소속 무장 | 목록을 비우고 등용 실행 가능한 소속 무장 포인터를 꼬리 추가 | 읽은 경로 없음 | 전역 무장 목록 순서 | `1A250` | 목록 포인터 0이면 2, 그 밖 항상 1 | 코드, 일부 가상 함수·부수 경로 미독 [Codex 판독 2026-11-25·미검증] c10 |
| CGetEstrangeDataNode | `3A0C0` | `[0]` 출력 무장 후보(종류 4), `[1]` 출력 이간 목표 무장(종류 4) | — | 두 목록(실행 무장 `6DD230`, 목표 `6E2440`·`714E20`) | 없음 | — | `6DD230`·`6E2440`·`714E20` | 1(빈 목록도), 2 | 코드(신분 6 분기 의미는 가설) [Sonnet 판독 2026-11-25·미검증] s12 |
| CGetHiddenPoisonDataNode | `3C1F0` | `[0]` 출력 무장 후보 목록(종류 4), `[1]` 출력 목표 지역 목록(종류 6) | 군단 가용 무장, 인접 거점·타 비동맹 비이민족 세력 소유 | 두 목록(없으면 새로 만듦) | 없음 | — | `6DD230`·`6E0D60`·`7143A0` | 1(빈 목록도), 2(목록 확보 실패) | 코드 [Sonnet 판독 2026-11-25·미검증] s12 |
| CGetMyselfDistrictInfoNode | `3C330` | `[0]` 항목 번호(0~20, 3 제외), `[1]` 출력 | 현재 군단 | 군단 ID·소속 세력·군단장·수입·거점·부대·군세·주의 목록·등급 등 20종 | 없음 | — | `B7170`·`331780` | 1, 2(군단 무효·미지원 항목·쓰기 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g45 |
| CGetMyselfDistrictNode | `3DB40` | `[0]` 출력 키 | AgentType | 군단 객체를 변수에: 3이면 주체 그대로, 2·1은 군단 표 조회(`22D4E0`·`22D3C0`), 그 밖은 null | 없음 | — | `B7170` | 1(null 저장도), 2(쓰기 실패) | 코드 [Sonnet 판독 2026-11-25·미검증] s8 |
| CGetPlacationDataNode | `3DB90` | `[0]` 무장 목록(출력), `[1]` 두 번째 목록(출력) | — | 무장 후보(`6DD230`)와 회유 대상 후보(`6E0ED0`) | 없음 | 정렬 없음 | `6DD230`·`6E0ED0` | 1, 2(목록 못 읽고 못 만듦) | 코드 / 가설(`6E0ED0` 원소 정체) [Sonnet 판독 2026-11-25·미검증] s13 |
| CGetSearchDataNode | `3DCD0` | `[0]` 목록(종류 4) | 현재 군단 무장 | 탐색 후보 무장 목록 | 없음(본체) | — | `1406DCD20` | 1, 2(목록 확보 실패) | 코드(`1406DCD20` 미확인) [Gemini 판독 2026-11-25·미검증] g46 |
| CGetTransactionDataNode | `3DF60` | `[0]` 거래 도시 목록(변수 0325), `[1]` 거래 무장 목록(변수 0290) | 군단 거점 | 두 목록을 비우고 채움(첫 목록은 둘째 확보 실패 전에 이미 비워짐) | 확인 본문 없음, 간접 경로 미확정 | 거래 가능한 군단 거점에서 처음 나오는 도시, 무장 포인터 합집합 | `70FF80`계·`6DA1B0`·`1A250` | 1(후보 0개도), 2(목록 확보 실패) | 코드 / 일부 flag·iterator 가설 [Codex 판독 2026-11-25·미검증] c11 |
| CGetUnattendedhomeDataNode | `3E400` | `[0]` 무장 목록(출력), `[1]` 두 번째 목록(출력, 종류 6) | — | 무장 후보(`6DD230`)와 대상 거점 후보(`6E27C0` → `714900` 필터) | 없음 | 정렬 없음 | `6DD230`·`6E27C0`·`714900` | 1, 2 | 코드 / 가설(`714900` 후반) [Sonnet 판독 2026-11-25·미검증] s13 |
| CRecruitOfficerRemoveNode | `3E6B0` | `[0]` 거점 B(판단표 둘째 인수는 안 읽음) | B `+0xCA`(u16 모병 담당), B의 군단 명령서 | 거점 `+0xCA`를 비움(ID 0 모병 담당 변경) | 읽은 경로 없음 | — | `1F34F0` | `+0xCA`==0이면 즉시 1, 명령서 < `B434`이면 2, 그 밖 1(`1F34F0` 결과 무시, B 무효여도 1) | 코드, `29DE10` 제3인수·변수 번호 미확인 [Codex 판독 2026-11-25·미검증] c10 |
| CSpyHomeOfficerRemoveNode | `3EAA0` | `[0]` 첩보 슬롯(정수 키, 1부터) | 군단 명령서 `+0x14`, 세력 슬롯 | 슬롯 `세력 +0x19C[i]`·`+0x196[i]`를 0으로, 바뀌면 군단 명령서 차감(`B21C`) | 읽은 경로 없음 | — | — | 2(정수 읽기 실패·명령서 < `B440`·세력 무효), 그 밖 1(범위 밖·빈 슬롯도 무변경 1) | 코드, 상수 수치 미확인 [Codex 판독 2026-11-25·미검증] c10 |
| CSpyHomeOfficerSetNode | `3EBC0` | `[0]` 목표 세력 T(변수 513), `[1]` 담당 무장 P(514), `[2]` 슬롯 s(501) | T의 슬롯 값, P 번호(`+0x10`), 군단 명령서 | 지정 첩보 슬롯에 T 번호·P 번호 배치, 기존 담당 해제, P가 소속 거점(`+0xE2`)의 모병·훈련 담당이면 해제, 명령서 차감 | 읽은 경로 없음(후보 조건·난수 추첨 근거 없음) | 슬롯 < 3, 0 < T 번호 < 52, P 번호 1..6000 검사 | `22B1E0`·`32E3B0(world,u16(P+0xE2))`·`29DE10`·`045760` | 읽기 실패 2, 이미 같은 배치면 생존·비용 검사보다 먼저 1, 일반 경로 1 | 코드 중심, `045760` 실제 인수 미복구 [Codex 판독 2026-11-25·미검증] c10 |
| CTrainingOfficerRemoveNode | `3EEB0` | `[0]` 거점 B(둘째 인수는 안 읽음) | B `+0xCC`, B의 군단 명령서 | 거점 `+0xCC`를 비움(ID 0 훈련 담당 변경) | 읽은 경로 없음 | — | `201A80` | `+0xCC`==0이면 1, 명령서 < `B440`이면 2, 그 밖 1(B 무효여도 1) | 코드, `29DE10` 제3인수·변수 번호 미확인 [Codex 판독 2026-11-25·미검증] c10 |
| CAllianceSuccessConditionNode | `525C0` | `[0]` 대상 세력 T, `[1]` 사자 무장 P, `[2]` 대가 종류 k, `[3]` 출력, `[4]` 보존량(직접값) | 군주 거점 금·군량, 보존량, 제안 기간 비용 | `[3]` = 금·군량 비용 또는 명품 객체 | 없음 | 비플레이어 T는 금 ≥ 1000 이고 금−1000 > rg′면 `[3]`=1000, 플레이어 T는 `9D930` 뒤 금·군량 보존량 검사 | `9D930`·`22E450`·`324180` | 1(쓰기 성공), 2(읽기 실패·무효·금 < 1000·보존량 조건·`9D930` 거짓) | 코드(목록 함수 의미 가설) [Sonnet 판독 2026-11-25·미검증] s10 |
| CCommandExecutionAllianceNode | `52990` | `[0]` 대상 세력 T, `[1]` 사자 P, `[2]` 대가 종류 k, `[3]` 대가 값, `[4]` 기간(직접값) | 제안 구조 D | D(종류 5, T·P·금/군량/명품/지역·기간)를 채워 제출 | 노드 없음(제출 경로 `3FDAF0` 해시형만) | — | `1EE460`·`1F1000`(거절) | 1(거절돼도 항상), 2(읽기 실패·무효) | 코드 [Sonnet 판독 2026-11-25·미검증] s10 |
| CCommandExecutionAnnulNode | `52B60` | `[0]` 아군 세력(유효성만), `[1]` 사자 P, `[2]` 대상 세력 T | — | 동맹 파기(kind 6) 명령 제출, 사자 임무 표식·명령서 −`B650`·거점 금·군량 clamp(파기 효과는 도착 후) | 제출 단계 `3FDAF0` 1회(미사용), 결과 단계 `3FDFF0` 무장당 1회 | — | `1F1000` | 1(제출 실패여도), 2(읽기·유효 실패) | 코드(결과 단계 세부 가설) [Sonnet 판독 2026-11-25·미검증] s11 |
| CCCommandExecutionEstrangeNode | `533F0` | `[0]` 아군 세력(유효성만), `[1]` 실행 무장 A, `[2]` 목표 무장 T | A의 군단 명령서 ≥ `DAT_141A4B720` | 이간(종류 `0xC`) 요청 등록, 군정 70% 상한 | 해시형 `3FDAF0`만(`1E4F70`·`1E2680`·결과 `1ED1D0`), 전역 상태형 없음 | — | `1FA5C0` | 1(등록 실패여도), 2 | 코드(상수 값 미확인) [Sonnet 판독 2026-11-25·미검증] s13 |
| CCommandExecutionExpansionNode | `53790` | `[0]` 세력 | 세력 `+0x70+0x1E×i`, 등급표 `[L]+0x14` | 예산(`등급표[L]+0x14 − Σ 세력 +0x70+0x1E×i`)만큼, 부족이 최대인 종류의 레벨을 `min(7,old+1)`로 | 확인 본문 없음 | 종류 0..4 중 부족 최대(동점 작은 번호) | `32DFC0`(2번째 인수는 유추) | 1(부족분 없음·예산 0 포함), 2(읽기 실패·세력 무효) | 코드 [Sonnet 판독 2026-11-25·미검증] s14, [Codex 판독 2026-11-25·미검증] c3 |
| CCommandExecutionGoodwillNode | `53930` | `[0]` 대상 무장 T, `[1]` 제안 무장 P, `[2]` 대가 종류 k, `[3]` 양(k=0·1)·객체(k=2·4), `[4]` 금 보존량 rg | k=0·1은 `보유 − 양 > 보존량` | 제안 구조 D(kind 4)를 만들어 `1EE460(D,0)` 제출 | 노드엔 없음, 제출 성공 시 `2F5AA0`·`326ED0`의 해시형 `3FDAF0`(조언 정확도 1회·수락 판정 1회, 친선 특례·관계 등급 5 분기) | — | `1EE460`·`2F5AA0`·`326ED0` | 1(제출 실패도), 2(읽기 실패·무효·k=0·1에서 `보유 − 양 ≤ 보존량`) | 코드(`1F67B0` 후반·`2F5AA0` 전체는 대도서관 신뢰) [Sonnet 판독 2026-11-25·미검증] s12 |
| CCCommandExecutionHiddenPoisonNode | `54110` | `[0]` 아군 세력(유효성만), `[1]` 실행 무장 A, `[2]` 목표 지역 Z | A의 군단 명령서 ≥ `B718`, 군정 | 계략 14(매복·지독) 요청을 `1FA5C0`으로 등록(A 이동·명령서·비용·군정 차감, 투입 군정 = min(필요량, 군정×30%)) | 노드엔 없음, 등록 중 사전 성공률 `1E1370`의 해시형 `3FDAF0` 2회(성공률 > 99면 재계산) | — | `1FA5C0`·`1E1370`·`40C20`·`22EDF0` | 1(등록 실패도), 2(읽기 실패·무효·명령서 < `B718`) | 코드(비용 자원·일부 하위 가설) [Sonnet 판독 2026-11-25·미검증] s12 |
| CCommandExecutionPlacationNode | `545D0` | `[0]` 아군 세력(유효성만), `[1]` 실행 무장 A, `[2]` 목표(지역 계열 객체) | A의 군단 명령서 ≥ `DAT_141A4B72C` | 회유(종류 `0xD`) 요청 등록, 군정 50% 상한 | 해시형 `3FDAF0`만(`1E4290`·`1E1A60`·결과 `1ED040`), 전역 상태형 없음 | — | `1FA5C0`·`1F1540` | 1(등록 실패여도), 2 | 코드(상수 값 미확인) [Sonnet 판독 2026-11-25·미검증] s13 |
| CCommandExecutionLearnNode | `54330` | `[0]` 무장, `[1]` 전법서(종류 17) | 무장 군단 `+0x14`(order_count) ≥ `DAT_141A4B5CC`, 전법 10칸 | `1F18E0`: 전법 추가·정렬, 서 재고 −1, 세력 `+0x164` 가산, 주력 군단 명령서 −상수 | 없음 | 전법 10칸의 빈 칸 | `1F18E0` | 1(`1F18E0` ≠ 0), 2(읽기 실패·무효·군단 `+0x14` 부족·전법 10칸 만석·`1F18E0`==0) | 코드 확인(무장 군단 `+0x14` < `B5CC`이면 2, 지휘 세션 2026-11-25; functions.md:933의 「관직 rank」는 틀림) / 상수 값·일부 하위는 가설 [Sonnet 판독 2026-11-25·미검증] s15 |
| CCommandExecutionPostAutoNode | `54710` | `[0]` 세력 | 세력 소속 무장 후보, 계급 | 후보 전원을 기본 관직 `0x49` 예정으로, 관직 번호 순으로 능력 정렬 목록(총합·무관·문관) 첫 사람을 배정하고 포인터 순으로 적용, 충성 d 가감 | 없음 | 관직 번호 순 | `1DF5F0` | 2(키 읽기 실패), 그 밖 항상 1 | 코드(일부 하위 함수 미판독) [Sonnet 판독 2026-11-25·미검증] s14 |
| CCCommandExecutionPrisonerReturnNode | `548D0` | `[0]` 대상 세력 T, `[1]` 사자 P, `[2]` 금(앞 노드가 쓴 가치합), `[3]` 포로 목록 L | `230270(22E450(P))`의 군단 명령서 `+0x14`, L | 제안 D(종류 8, 금 `D+0x20`)를 `1EE460`으로 제출, 임시 목록(`D+0x30`)에 L의 머리 → 꼬리 순서로 신분 6 무장만 복사(원본 L 불변) | 노드 없음(제출 경로 `3FDAF0` 해시형만) | 정렬·중복 제거·개수 제한 없음 | `1EE460`·`93C30` | 1(읽기·유효·명령서·임시 목록 검사를 지난 뒤 항상), 2(읽기 실패·무효·명령서 0·임시 목록 비음) | 신분 6(`+0xE6`==6)만 고름은 코드 확인(지휘 세션 2026-11-25), 나머지 코드(명령 객체 저장 가설) [Sonnet 판독 2026-11-25·미검증] s10 |
| CCommandExecutionSearchNode | `54AD0` | `[0]` 탐색 지역 Z, `[1]` 탐색 무장 A | 지역 소유=무장 소속(`1F1430`), 군단 명령서 ≥ `B5B8` | 탐색 명령 객체를 풀에 등록(`1F3F50`: 무장 `+0x15E` bit0, 소재 이동 형식 10, 명령서 −`B5B8` 0..200 클램프) | 노드엔 없음, 등록 때 조언 사전 검사만 해시형 `3FDAF0`(전역 상태 불변), 실제 발견은 도착 후 | — | `1F1430`·`1F3F50` | 1(`1F3F50` 호출까지 간 경우만, 등록 실패도 1), 2(읽기 실패·무효·`1F1430` 거짓·명령서 < `B5B8`) | 코드(하위 일부 가설) [Sonnet 판독 2026-11-25·미검증] s9 |
| CCommandExecutionSpyAwayNode | `54BC0` | `[0]` 대상 세력 T, `[1]` 파견 무장 A, `[2]` 기간 d(5·10·15) | A의 군단 명령서 ≥ `B60C`, `1F14A0` 검증 | 정찰(kind `0x15`) 제출(명령서 −`B21C`, 본거점 금 −`6DDF10(d)`), 도착 시 성공이면 군정 + 보상, 실패면 −10%·부상 판정, 우호도 하락 | 해시형 `3FDAF0` 성공 1회·부상 1회(결과 시), 조언 1~2회(미사용) | — | `1F14A0`·`1FA100` | 1(조건 통과), 2(읽기 실패·명령서 < `B60C`·d가 5·10·15 아님) | 코드(상수·보상식 가설) [Sonnet 판독 2026-11-25·미검증] s11 |
| CCommandExecutionUnattendedHomeNode | `54F50` | `[0]` 아군 세력(유효성만), `[1]` 실행 무장 A, `[2]` 목표 거점(도시) C | `C+0x4E` < `0x34`, A의 군단 명령서 ≥ `DAT_141A4B734` | 구호탄랑(계략 11) 요청을 `1FA5C0`으로 등록(군정 80% 상한) | 해시형 `3FDAF0`만(필요량·성공률·결과 내부), 상태형 없음 | — | `1FA5C0`·`22C1F0` | 1(등록이 조용히 무시돼도), 2(읽기 실패·무효·`C+0x4E` ≥ `0x34`·명령서 부족) | 코드(상수·`1E2AB0` 두 번째 출력 미확인) [Sonnet 판독 2026-11-25·미검증] s14, [Codex 판독 2026-11-25·미검증] c3 |
| CDistributeSpyPointNode | `550B0` | 인수 없음(`+0x38` 이후 안 읽음) | 세력 군단들의 군정 `+0x24`, AgentType | 군단 군정 합 30% 유보, 주력 군단 M의 초과분을 거점 수 비례로 가장 부족한 군단 1곳에 한 번 이전(양쪽 0..상한) | 없음 | 주력 군단 M → 최부족 군단 1곳 | — | 1(F·M 유효, 옮길 것이 없어도), 2 | 코드 [Sonnet 판독 2026-11-25·미검증] s15 |
| CGetForceFriendshipNode | `56AC0` | `[0]` 대상 세력, `[1]` 출력 | 현재 세력(`param_3`)의 `+0x13+대상 번호`, 군주 `+0x16C`, `DAT_141A4AFE4` | `[1]`에 `(DAT_141A4AFE4 × 우호 바이트) × 군주 +0x16C ÷ 10000` | 없음 | — | — | 1, 2(읽기·무효) | 코드 [Gemini 판독 2026-11-25·미검증] g45 |
| CGetMyselfForceInfoNode | `56BD0` | `[0]` 항목 번호(0~39, 정수 직접값), `[1]` 출력 | 현재 세력 | 세력 정보 40종 | 없음 | — | `B7210` | 1, 2(세력 무효·0~39 밖·쓰기 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g45 |
| CGetMyselfForceNode | `58B40` | `[0]` 출력 | AgentType | 현재 세력 객체를 `[0]`에 | 없음 | — | `B7210`·`B29460` | 쓰기 성공 1, 실패 2 | 코드 [Gemini 판독 2026-11-25·미검증] g45 |
| CCallScriptNode | `5D760` | `[0]` 정수 즉값(수식 번호), `[1]` 결과 정수 키, 정수 입력 7개 | 수식표(`0000/param_s.bin`) `[0]`번 식 | 결과를 `[1]`에 | 없음(현재 수식 1~13은 난수 연산을 쓰지 않음) | — | `C11E0` | 1(출력 쓰기 결과는 무시), 2(입력 슬롯 정수 읽기 실패); 나눗셈에서 나누는 값 0이면 식 결과 1 | 코드 [Sonnet 판독 2026-11-25·미검증] s16 |
| CDiplomacyPriorityConditionSelectNode | `7AFA0` | `[0]` 자기 세력 F, `[1]` 정수 출력(대가 종류 0 금·1 군량·2 명품), `[2]` 상대 세력 T | 세력 자원·군주 성향·명품 평가 | `[1]`에 종류, 전역 `DAT_142781208`에도 씀 | 확인된 평가·선택에 없음 | 보정 점수 최대 선택, 동점은 금 → 군량 → 명품 | — | 1(`B29250` 성공), 2(읽기 실패·F 무효) | 코드 / 반복자 연결·상수 미확정 [Codex 판독 2026-11-25·미검증] c11 |
| CDomesticPriorityDevelopmentSelectNode | `7B0B0` | `[0]` 지역 Z, `[1]` 정수 출력, `[2]`~`[4]` 가중치(직접값, 판단표 25·50·75) | 군단 방침, 지역 `+0x3C/+0x3E/+0x40`, 군단 `+0x12` 군단장 무장 `+0x170/+0x172/+0x174`, 담당관 `+0x36` | 선택 항목 0..3(0=선택 없음) | 난수·목록 없음 | 군단 방침(3/2/4)별 우선 항목 1/2/3, 아니면 군단장 능력 보정×단계×가중치 최소 항목(동점 1→2→3, 완료 지역 50000), 현재 방침과 같으면 담당관이 유효할 때 0 | `B7170` | 1(읽기·지역 유효·쓰기 성공), 2(읽기 실패·지역 무효·쓰기 실패) | 코드(항목 이름은 가설) [Sonnet 판독 2026-11-25·미검증] s9 |
| CGetAreaDistanceNode | `7B6D0` | `[0]`·`[1]` 첫째 객체, `[2]`·`[3]` 둘째 객체, `[4]` 결과 키 | 두 객체가 속한 칸의 지역(`+0x12`) | 지역 거리를 `[4]`에(불가 시 `0x7FFFFFFF`) | 없음 | — | `BFBC0`·`B73C0` | 1, 2(칸 번호가 `0xBD10`인 경우·쓰기 실패) | 코드(일부 가설) [Gemini 판독 2026-11-25·미검증] g42 |
| CGetAroundLandTypeNode | `7B7B0` | `[0]` 기준 객체, `[1]` 반경(정수 리터럴), `[2]` 결과 키 | 반경 안 칸의 지형 | 최빈 지형 객체를 `[2]`에 | 없음 | 지형 16·17 제외, 동점은 작은 번호 우선 | `2A9C90`·`B29460` | 1, 2(읽기·무효·쓰기 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g46 |
| CGetCompatibilityNode | `7C5B0` | `[0]` 무장 A, `[1]` 무장 B, `[2]` 정수 출력 | 두 무장 `+0xBE` | `d = ΔBE의 절댓값`, `min(d,150−d)`, `min(·,75)`를 `[2]`에(부호 있는 계산이라 Δ > 150이면 음수 가능) | 없음 | — | `2A8010`·`331780` | 1, 2(읽기 실패·무효·쓰기 실패) | 코드 [Sonnet 판독 2026-11-25·미검증] s8 |
| CGetDelegationTargetNode | `7C680` | `[0]` 군단, `[1]` 정수 출력(종류), `[2]` 객체 출력(목표) | 군단 `+0x19` 종류, `+0x18` 번호 | 종류 2/7/8의 번호를 객체로 바꿔 `[2]`에, 종류값 5/0/1을 `[1]`에(무효면 일부 생략) | 없음 | — | `32E3B0`·`world+0xDF30` | 1(종류 7은 세력이 무효여도 `[1]`=0을 쓰고 1, 종류 2는 거점이 무효면 `[1]`=5도 안 씀), 2(읽기 실패·군단 무효·종류 2/7/8 아님·쓰기 실패) | 코드 [Sonnet 판독 2026-11-25·미검증] s16 |
| CGetDiplomacyConditionAreaNode | `7C850` | `[0]`·`[1]` 세력, `[2]` 출력(4), `[3]` 출력 지역 | `world+0xB0` | 후보 정렬 뒤 첫 항목을 `[3]`에, `4`를 `[2]`에 | 없음(본체) | `334C50` 조건 후보를 모아 `75770`으로 정렬 | `334C50`·`75770`·`98390` | 1, 2(읽기·유효 실패·`[2]` 쓰기 실패·후보 0) | 코드(`98390` 미확인) [Gemini 판독 2026-11-25·미검증] g46 |
| CGetExchangeConditionsNode | `7E930` | `[0]` 직접 정수 모드 m(0·1), `[1]` 입력 x 키, `[2]` 출력 키 | x, `DAT_141A4B3B4` | m=0: x>0 ? `B3B4×x/10` : 0, m=1: x>0 ? `x×10/B3B4` : 0 을 `[2]`에(m이 0·1이 아니면 0) | 없음 | — | `3242D0`·`324320` | 1, 2(x 읽기 실패·쓰기 실패); 나눗셈 0 보호 없음 | 코드 [Sonnet 판독 2026-11-25·미검증] s9 |
| CGetFakeNewsSuccessProbabilityNode | `7E9E0` | `[0]` 시전 부대 P, `[1]` 대상 부대 T, `[2]` 정수 출력 | 두 부대 지력·개성 `0x76`·면역 | `283410(P,T)`: 지력차×계수+개성 `0x76`, 클램프·난이도 보정(0..100)을 `[2]`에(지력 ≥ 100이거나 면역 개성이면 0) | 해시형 `3FDAF0`을 부르나 결과(bool)를 버려 영향 없음 | — | `283410` | 1, 2(읽기 실패·무효·쓰기 실패) | 코드(상수·설정 객체는 가설) [Sonnet 판독 2026-11-25·미검증] s15 |
| CGetFireStrategySuccessFireStrategyNode | `7EAC0` | `[0]` 부대, `[1]` 칸, `[2]` 정수 출력 | 면역·지력·지형·상태, 개성 효과 `0x1A` 합, 정책 `0x2F` | `269BC0(부대,칸,0)`을 `[2]`에(면역 0·공격자 면역 100·지력차/2+지형항+상태항 하한, 개성 효과 id `0x1A` 합 보정, 정책 `0x2F` 가산) | 없음 | — | `269BC0`·`26BBE0(부대,0x1A,out)` | 1, 2(읽기 실패·무효·쓰기 실패) | 코드(상수 값 미확인) [Sonnet 판독 2026-11-25·미검증] s14 |
| CGetOfficerCandidateNode | `7F4F0` | `[0]` 거점 B, `[1]` 후보 목록 L(종류 4) | 도시 무장, 소속 관문 무장, 무장 `+0xE2`(소속 거점) | L을 비우고 후보 추가 | 확인 본문 없음 | 도시 무장 → 소속 관문 무장, 전역 무장 연결목록 순서(관문 추가 flag는 가설) | `6D8E00`·`3353E0`·`234AB0`·`1A250` | 1(L 확보 뒤 후보가 없어도), 2(B 읽기 실패·무효·L 확보 실패) | 코드 / 관문 flag·predicate 가설 [Codex 판독 2026-11-25·미검증] c11 |
| CGetPlayerForceNode | `7F720` | `[0]` 출력 | game `+0x3A` | 세력 객체(번호 ≥ 0x34는 0번)를 변수에 | 없음 | — | `B29460` | 1(쓰기 성공), 2 | 코드(의미는 가설) [Sonnet 판독 2026-11-25·미검증] s8 |
| CGetRemainAlliancePeriodNode | `7F780` | `[0]`·`[1]` 세력, `[2]` 출력 | 기준 세력 `+0xEA + 상대 번호` 바이트 | `[2]` = 바이트 `& 0x7F` | 없음 | — | — | 1, 2(읽기·유효 실패·쓰기 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g46 |
| CGetSearchAreaNode | `7F990` | `[0]` 세력(주체), `[1]` 출력 목록 | 세력·주체 관할 지역, 4개 소스 조건 | 탐색 가능 지역을 `[1]` 목록에 수집 | 없음 | 소스 순서 | `C4F90`·`331780` | 1, 2(읽기·목록 확보 실패·`331780`==0) | 코드 [Gemini 판독 2026-11-25·미검증] g46 |
| CGetSpecifiedRangeTrapListNode | `80090` | `[0]` 기준 부대, `[1]` 출력 목록(종류 10 시설) | 부대 칸의 지역에서 인접 2단계 지역의 자기 세력 시설(정의 분류 4, `+0x16` bit0) | 출력 목록(비우고 재사용) | 없음 | 풀 순서 | `331780` | 1(결과가 비어도), 2(읽기 실패·부대 무효·목록 생성 실패) | 코드(일부 가설) [Sonnet 판독 2026-11-25·미검증] s16 |
| CGetTargetForcePrisonerListNode | `801D0` | `[0]` 세력 A, `[1]` 세력 B(목표), `[2]` 출력 목록 | 무장 전체 연결목록 | 거름(군단 세력==A, 신분 6) 뒤 소속 거점 소유==B, 소재 종류 5·6·0x1B인 무장을 목록 꼬리에 추가 | 없음 | 무장 전체 연결목록 순서, 비우지 않음·중복 검사 없음·정렬 없음 | `22E870`·`335540`(거름)·`1A250` | 항상 1(목록이 비어도), 2(읽기 실패·목록 생성 실패) | 코드(거름 슬롯은 추론) [Sonnet 판독 2026-11-25·미검증] s9 |
| CGetTradeNeedFoodNode | `803D0` | `[0]` 교역 국가 C(변수 0667), `[1]` 병사 수(0670), `[2]` 출력(0671), `[3]` 파견 무장 목록(0292) | 국가 계수·병사 단계 몫·무장 능력 5개 합·특성·첫 무장 세력의 이점 | `[2]`에 필요 군량 | 확인된 계산에 없음 | — | `B29250` | 1(쓰기 성공, 값이 0·음수여도), 2(C 읽기 실패·무효·목록 0개·쓰기 실패) | 코드 / 효과·생략 인수·상수 미확정 [Codex 판독 2026-11-25·미검증] c11 |
| CGoodwillSuccessConditionNode | `80730` | `[0]` 대상 무장 T, `[1]` 제안 무장 P, `[2]` 대가 종류 k, `[3]` 출력 | 세력 거점 합, 명품 최고 가치, 군주 거점 보유·보존량 | `[3]`에만 씀(친선 대가 금·군량·명품) | 없음 | `9F180`이 요구 가치 `324F20`을 제공 가능 가치와 비교, k=0·1은 `3242D0`으로 양 환산 | `9F180`·`324F20`·`3242D0` | 1(`[3]` 쓰기 성공), 2(읽기·무효·`9F180` 거짓·`보유−양 ≤ 보존량`·쓰기 실패) | 코드(필터 일부 가설) [Sonnet 판독 2026-11-25·미검증] s12 |
| CItemSelectNode | `80A10` | `[0]` 군주 R(명품 보유자), `[1]` 받을 무장 A, `[2]` 출력 객체 키 | R의 명품(bit0·!bit3·가치 ≤ 10), A의 능력 | 고른 명품 객체를 `[2]`에 | 없음 | 후보를 꼬리 순서로 모아, 우선 분기(말 2개 이상·통솔/무력 ≥ 80·장비 특수효과 없음 → 무력 → 통솔 → 정치 → 지력 → 매력)에서 가치가 엄격히 큰 첫 항목 | `331780`·`234FF0` | 1(출력 쓰기 성공), 2(읽기 실패·무효·R 신분 ≠ 1·후보 없음·쓰기 실패) | 코드(반복자 소유자 판정은 간접 근거) [Sonnet 판독 2026-11-25·미검증] s11 |
| CListAddAreaNode | `81160` | `[0]` 지역, `[1]` 목록(없으면 종류 6 생성) | 변수 항목 | 풀 노드 추가 | 없음 | 꼬리 추가, 중복 허용, 추가 뒤 생존 판정 호출(결과 무시) | `18D50`·`331780` | 1, 2 | `331780` 호출은 코드 확인(지휘 세션 2026-11-25), 나머지 [Sonnet 판독 2026-11-25·미검증] s7 |
| CListAddAreaUniqueNode | `812A0` | `[0]` 지역, `[1]` 목록(종류 6) | 변수 항목 | 중복이 없을 때만 추가 | 없음 | 포인터 중복 제외 꼬리 추가 | `18D50` | 1, 2 | `331780` 없음은 코드 확인(지휘 세션 2026-11-25), 나머지 [Sonnet 판독 2026-11-25·미검증] s7 |
| CListAddForceNode | `81EB0` | `[0]` 세력, `[1]` 목록(없으면 종류 0 생성) | 변수 항목 | 풀 노드 추가 | 없음 | 꼬리 추가, 중복 허용, 추가 뒤 생존 판정 호출(결과 무시) | `18D50`·`331780` | 1, 2 | `331780` 호출은 코드 확인(지휘 세션 2026-11-25), 나머지 [Sonnet 판독 2026-11-25·미검증] s7 |
| CListAddForceUniqueNode | `81FF0` | `[0]` 세력, `[1]` 목록(종류 0) | 변수 항목 | 중복이 없을 때만 추가 | 없음 | 포인터 중복 제외 꼬리 추가 | `18D50` | 1, 2 | `331780` 없음은 코드 확인(지휘 세션 2026-11-25), 나머지 [Sonnet 판독 2026-11-25·미검증] s7 |
| CListAddPersonNode | `825F0` | `[0]` 무장, `[1]` 목록(없으면 종류 4 생성) | 변수 항목 | 풀 노드 추가 | 없음 | 꼬리 추가, 중복 허용 | `18D50`·`1A250` | 1(풀 노드 확보 실패 포함), 2(읽기·목록 확보 실패) | 코드 [Sonnet 판독 2026-11-25·미검증] s7 |
| CListAddPersonUniqueNode | `82720` | `[0]` 무장, `[1]` 목록(종류 4) | 변수 항목 | 중복이 없을 때만 추가 | 없음 | 포인터 동일 항목이 있으면 추가 없이 1, 아니면 꼬리 추가 | `18D50` | 1, 2 | 코드 [Sonnet 판독 2026-11-25·미검증] s7 |
| CListGetItemByIndex | `83DE0` | `[0]` 목록 종류, `[1]` 목록, `[2]` 인덱스, `[3]` 결과 | 목록 | `[1]` 목록의 `[2]`번째(0 기준) 원소를 `[3]`에(범위 밖이면 객체 0을 쓰고 2) | 없음 | 머리부터 순번 | — | 1, 2(인덱스·목록 읽기 실패·범위 밖·종류 범위 밖) | 코드(일부 가설: `0xB`·`0xF` 스택 버퍼 전달 의미) [Gemini 판독 2026-11-25·미검증] g43 |
| CListSortEvaluationNode | `84CB0` | `[0]` 목록 종류, `[1]` 목록, `[2]` 방향 플래그(`[2]==0`과 함께 전달) | 목록 | 목록 순서(`0xE` 제외) | 본체 없음(`140023D40` 미확인) | `1400758A0` → `140023D40`로 정렬 | `1400758A0`·`140023D40` | 1, 2(종류 `0xE`·범위 밖·목록 읽기 실패) | 코드(노드 제어) / 가설(방향·점수 기준은 `140023D40` 미확인) [Gemini 판독 2026-11-25·미검증] g43 |
| CMiscBreakNode | `850D0` | 인수 없음 | — | 실행 문맥에 `"IsLoopBreak"` = 1 | 없음 | — | `B293C0` | 1(쓰기 성공), 2 | 코드(일부 가설) [Gemini 판독 2026-11-25·미검증] g42 |
| CMiscDummyNode | `85100` | `[0]` 정수 | 디컴파일 누락 | — | 미확인 | — | — | **판독 불일치**: [Gemini 판독 2026-11-25·미검증] g44는 사용 예 기준 가설로 `[0]==0`이면 성공(1)·`[0]==1`이면 실패(2)로 추정했으나, 이 문서 「더미 노드」 절은 바이트로 인수 1이면 결과 1·그 밖이면 2라고 확정했다(그쪽을 따름) | 가설(Gemini) / 확정(바이트, 기존 절) |
| CMiscLogNode | `85110` | `[1]` 모드, `[2]` 대상 변수·목록 | `[2]` 읽기·순회만 | 없음(게임 상태 불변, 로그 출력 호출 없음) | 없음 | — | — | `[1]==0`이면 항상 1, ≠ 0이면 대상 읽기 실패 시 2·아니면 1 | 코드(일부 가설) [Gemini 판독 2026-11-25·미검증] g42 |
| CPrisonerReturnSuccessConditionNode | `85610` | `[0]` 세력 B(유효성만), `[1]` 포로 목록 L, `[2]` 출력 정수(가치합 C), `[3]` 금 보존량 rg | 군주 거점 금 G, 포로 가치(`26C510`) | 맞으면 `[2]`=C; 목록 L은 파괴적으로 줄어듦 | 없음 | 가치합 C가 예산(G−C > rg′)에 안 맞으면 목록 꼬리부터 제거(최소 1명) | `9F7E0`·`7B3910`·`7B3250` | 1(`rg′ < G − C && C ≤ G`이고 쓰기 성공), 2(읽기 실패·무효·L 포인터 0·조건 거짓) | 코드 [Sonnet 판독 2026-11-25·미검증] s10 |
| CSetBehaviortreeRestartFlagNode | `85EC0` | 인수 없음 | 블랙보드 `"AgentType"` | AgentType 4(세력)이면 세력 `+0x20D`, 3(군단)이면 군단 `+0x2A`, 2(군세)이면 군세 `+0x38`을 1(1바이트)로 | 없음 | 독립된 `if` 셋(서로 배타) | `B7210`·`B7170`·`B72F0` | 1(AgentType 1·그 밖은 쓰기 없이 1), 2(AgentType 읽기 실패) | 코드 확인(지휘 세션 2026-11-25) |
| CTradePriorityCountrySelectNode | `860C0` | `[0]` 자기 세력 F, `[1]` 출력 국가 객체 C(변수 0667) | 국가 표 `world+0x85A20`(5칸, stride 0x38), 친밀도 | `[1]`에 선두 국가, 전역 `DAT_142781208` | 선택·정렬에 없음, 간접 명령 검사 미확정 | 후보를 제약으로 제거한 뒤 친밀도 < 1000 우선·친밀도 내림·번호 오름의 선두 | `22F740`·`2C8530`·`711BE0` | 1(선두 쓰기 성공), 2(F 읽기 실패·무효·후보 생성 0·빈 목록·쓰기 실패; 이전 값은 비우지 않음) | 코드 / 후보 제4인수 미확정 [Codex 판독 2026-11-25·미검증] c11 |
| CVariableClearNode | `86480` | `[0]` 변수 | — | `[0]` = 정수 0 | 없음 | — | `B29250`(반환 안 봄) | 항상 1 | 코드 [Gemini 판독 2026-11-25·미검증] g40 |
| CVariableCreateSpecifiedTypeNode | `864E0` | `[0]` 종류 코드, `[1]` 대상 키 | — | 종류 0xE면 정수 0, 아니면 객체 0 | 없음 | — | `B29250`·`B29460` | 1(쓰기 성공), 2 | 코드 [Gemini 판독 2026-11-25·미검증] g44 |
| CVariableDivideValueNode | `86540` | `[0]` 변수, `[1]` 정수 리터럴 | `[0]` | `[0]` = 정수 나눗셈 몫 | 없음 | — | `B28BB0`·`B29250` | 1, 2(읽기 실패·제수 0·쓰기 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g40 |
| CVariableDivideVariableNode | `865D0` | `[0]`·`[1]` 정수 변수 | `[0]`·`[1]` | `[0] /= [1]`(부호 있는 0 방향 버림, 제수 0이면 쓰기 없이 2) | 없음 | — | `B28BB0`·`B29250` | 1, 2(읽기 실패·제수 0·쓰기 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g44 |
| CVariableGetDistanceNode | `886F0` | `[0]`·`[1]` 첫째 종류·키, `[2]`·`[3]` 둘째, `[4]` 결과 | 두 객체의 칸 번호(`BFBC0`), `220×220` 격자 | `[4]`에 칸 거리 | 없음 | — | `BFBC0`·`2ACB80` | 1, 2(첫째 칸이 `0xBD10`·`[4]` 쓰기 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g42 |
| CVariableGetFindItemIndexNode | `89FB0` | `[0]` 목록 종류(0~0x12), `[1]` 원소, `[2]` 목록, `[3]` 결과 | 목록 | `[3]`에 원소의 0 기준 인덱스 | 없음 | 머리부터 첫 일치 | `B29250` | 1, 2(종류 범위 밖·읽기·유효성 실패·저장 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g44 |
| CVariableGetForceFriendshipNode | `8CA00` | `[0]` 기준 세력 A, `[1]` 대상 세력 B, `[2]` 출력 | A `+0x13 + B 번호` 바이트 | `[2]` = 우호도 바이트(B 번호 ≥ 0x34이면 0) | 없음 | — | `331780` | 1, 2(읽기 실패·무효) | 코드 [Gemini 판독 2026-11-25·미검증] g45 |
| CVariableGetListLengthNode | `8EF60` | `[0]` 목록 종류, `[1]` 목록, `[2]` 결과 | 저장된 개수(`0xE`는 정수 목록) | `[2]`에 길이 | 없음 | — | `4FCA0` | 1, 2(종류 범위 밖·읽기·쓰기 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g43 |
| CVariableMaxValueNode | `91B50` | `[0]` 변수, `[1]` 정수 상수 | `[0]` | `[0]` = max(`[0]`, 상수)(32비트 부호 있음) | 없음 | — | `B28BB0`·`B29250` | 1, 2(읽기·쓰기 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g41 |
| CVariableMaxVariableNode | `91CA0` | `[0]`·`[1]` 변수 | `[0]`·`[1]` | `[0]` = max(`[0]`, `[1]`) | 없음 | — | `B28BB0`·`B29250` | 1, 2 | 코드 [Gemini 판독 2026-11-25·미검증] g41 |
| CVariableMinValueNode | `91DF0` | `[0]` 변수, `[1]` 정수 상수 | `[0]` | `[0]` = min(`[0]`, 상수) | 없음 | — | `B28BB0`·`B29250` | 1, 2 | 코드 [Gemini 판독 2026-11-25·미검증] g41 |
| CVariableMinVariableCalculationNode | `91E80` | `[0]`·`[1]` 정수 변수, `[2]` 출력 | `[0]`·`[1]` | `[2]` = min(`[0]`, `[1]`)(피연산자 유지) | 없음 | — | `B28BB0`·`B29250` | 1, 2(읽기·쓰기 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g42 |
| CVariableMinVariableNode | `91F40` | `[0]`·`[1]` 변수 | `[0]`·`[1]` | `[0]` = min(`[0]`, `[1]`) | 없음 | — | `B28BB0`·`B29250` | 1, 2 | 코드 [Gemini 판독 2026-11-25·미검증] g41 |
| CVariableMinusValueNode | `92000` | `[0]` 변수, `[1]` 정수 상수 | `[0]` | `[0]` = `[0]` − 상수(32비트) | 없음 | — | `B28BB0`·`B29250` | 1, 2 | 코드 [Gemini 판독 2026-11-25·미검증] g41 |
| CVariableMinusVariableNode | `92080` | `[0]`·`[1]` 변수 | `[0]`·`[1]` | `[0] -= [1]`(32비트) | 없음 | — | `B28BB0`·`B29250` | 1, 2 | 코드 [Gemini 판독 2026-11-25·미검증] g40 |
| CVariableMultiValueNode | `92130` | `[0]` 정수 변수, `[1]` 상수 | `[0]` | `[0]` = `[0]` × 상수 | 없음 | — | `B28BB0`·`B29250` | 1, 2 | 코드 [Gemini 판독 2026-11-25·미검증] g43 |
| CVariableMultiVariableNode | `921C0` | `[0]`·`[1]` 변수 | `[0]`·`[1]` | `[0] *= [1]`(32비트) | 없음 | — | `B28BB0`·`B29250` | 1, 2 | 코드 [Gemini 판독 2026-11-25·미검증] g40 |
| CVariablePlusVariableNode | `922F0` | `[0]`·`[1]` 정수 변수 | `[0]`·`[1]` | `[0] += [1]` | 없음 | — | `B28BB0`·`B29250` | 1, 2 | 코드 [Gemini 판독 2026-11-25·미검증] g43 |
| CVariableSetRandomNumberNode | `92870` | `[0]` 출력 변수, `[1]` 상한 n(`+0x3C`), `[2]`~`[5]` 변수 | `[2]`~`[5]` 값(못 읽으면 0으로 대체, 실패하지 않음) | 해시 난수 `[0..n-1]`을 `[0]`에 | `3FDAF0(n, 1, 변수 [2]~[5] 값)` 해시형 1회 | — | `3FDAF0`(`FUN_14032ec60` 미확인) | 1(`[0]` 쓰기 성공), 2(쓰기 실패) | 코드 확인(지휘 세션 2026-11-25) / [Gemini 판독 2026-11-25·미검증] g40 |
| CVariableSetVariableSpecifiedTypeNode | `92990` | `[0]` 종류 코드, `[1]` 대상 키, `[2]` 원본 키 | 원본 변수 | `[0]`==14(0xE)이면 정수, 아니면 객체 8바이트를 `[1]`에 복사 | 없음 | — | `B28BB0`·`B29250`·`B28D20`·`B29460` | 1, 2(읽기·쓰기 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g44 |
| CAvoidPoisonNode | `1F100` | 인수 없음(부대 판단 주체) | 부대, 주장 개성 `0x4D`, 좌표 범위 | `9D870`이 독 칸 회피 경유점을 씀 | 없음 | — | `B7100`·`9D870`(`9C170` 반환을 확인하지 않고 조건 통과 시 무조건 1)·`26E260` | 1(`9D870` ≠ 0), 2(부대 무효·좌표 범위 밖·주장이 개성 `0x4D` 보유) | 코드(`9C170` 내부 미판독) [Gemini 판독 2026-11-25·미검증] g55 |
| CClearArmyAIActionNode | `1F160` | 인수 없음 | `B7100`으로 얻은 부대 | 부대 `+0x1F0`(u16)을 0으로 | 없음 | — | `B7100` | 1, 2(부대 무효) | 코드 [Gemini 판독 2026-11-25·미검증] g54 |
| CCutLogisticsNode | `1F380` | 인수 없음 | 부대, 군세 `+0x14`, 주장 능력 0·2(`231770`) | 병참선 절단 이동(`D1760`), 군세 무효 시 `+0x1F4 = 0` | 없음 | 게이트: 군세 `+0x14` ≠ 8, 주장 능력 0 또는 2가 `> 0x40` | `D1760`·`231770`·`22F4A0` | 1, 2(부대 무효·군세 `+0x14`==8·능력 0·2 모두 ≤ `0x40`·`D1760`==0) | 코드(`D1760` 내부 미판독) [Gemini 판독 2026-11-25·미검증] g55 |
| CExclusionUserArmyAttachedFootholdNode | `1F760` | 인수 없음 | 부대, `22E2A0(부대)`(세력), 도시 곁 플레이어 부대 칸 | 도시 곁 플레이어 부대 칸을 `CF570` 경유점으로 넣음(이름의 「제외」와 다른 동작) | 없음 | — | `B6230`·`235150`·`CF570` | 1(`B6230` ≠ 0), 2 | 코드 [Gemini 판독 2026-11-25·미검증] g55 |
| CMoveAdvantagePositionNode | `1FE80` | 인수 없음 | 부대, 인접 `0x1B` 목표 부대, 개성별 지형, 반경 5 아군·중립 시설, 반경 3 적 시설 | 경유점 이동 | 없음 | `C5AC0` 3단계: 인접 목표 부대 게이트 → 개성별 지형 이동 → 반경 5 시설 → 반경 3 적 시설 회피 | `C5AC0`·`26E260` | 1(`C5AC0` ≠ 0), 2 | 코드 [Gemini 판독 2026-11-25·미검증] g55 |
| CMoveObjectAttackingArmyPositionNode | `1FEE0` | 인수 없음 | 부대 `+0x26`·`+0x3A`, 병과 표 `+0xA6` 비트1, 같은 세력(`22E2A0` = `world+0xDF30` 세력 표) 아군 | 이동·경유점(`C9680`) | 없음 | `C9680`은 자기 부대 `+0x26 & 1` ≠ 0일 때만 진입, 관문 분기는 병과 `+0xA6` 비트1==0일 때만(공성 병과는 바로 0 반환이라 2차 탐색도 비공성 병과만), 관문 1차 비교는 내 위력 + `DAT_141345C20`(= 5.0, PE 읽음) 여유를 넘는 아군만, 후보 아군은 같은 세력·`+0x26 & 1`==0·같은 목표(`+0x3A`), 시설(`0xB`) 분기 후보는 `+0x38`==5 | `C9680`·`22E2A0`·`26E260` | 1(`C9680` ≠ 0), 2 | 코드 확인(지휘 세션 2026-11-25; roles.md:972·1015 보강) / [Gemini 판독 2026-11-25·미검증] g55 |
| COccupyNeighborCapitalNode | `1FF40` | 인수 없음 | 부대 | 이웃 수도(거점) 점령 이동(`CD5F0`) | 없음 | — | `CD5F0` | 1, 2 | 코드 [Gemini 판독 2026-11-25·미검증] g55 |
| COccupyNeighborSceneryNode | `1FFC0` | 인수 없음 | 군세 `+0x14`==0xD 게이트, 반경(`2AF8B0`/10) | 이웃 명승 점령 이동(`CD5F0` 연쇄·`CF570`) | 없음 | 머리부터 첫 칸 선택 | `CD990`·`CD5F0`·`CF570` | 1, 2 | 코드 [Gemini 판독 2026-11-25·미검증] g55 |
| CRecoverLogisticsNode | `20040` | 인수 없음 | 부대 `+0x26 & 2`==0 게이트, 주장 능력(`231770(주장,2,0xFFF)/10 − 4`, 최소 2) | 병참 회복 이동: 거리 1이면 `CF570`, 비인접이면 `2ECEA0(1)`·`2ECF00(9,칸)`·경유점 5칸 `0xBD10`·`26E260` | 없음 | — | `B7100`·`CED10` | 1(`CED10` ≠ 0), 2(부대 무효·AgentType ≠ 1) | 코드 [Gemini 판독 2026-11-25·미검증] g55 |
| CSetRelayHexEvadeFlameHexNode | `201C0` | 인수 없음 | 부대 주장 개성(`0x19`·`0x1A`·`0x66`·`+0xB6`), 이동력 | 화염 칸 회피 경유점(`9AFB0`, `99140`) | 없음 | `9AFB0` 예산 = 이동력 × `0x78`(재탐색 `0xF0`), 임계 `비용 ≤ (예산 값 × 3)/2`, 추출 간격 총칸수/6, `99140` 행동 13이면 마지막 적 부대 칸 | `2320D0`·`9AFB0`·`99140`·`26E260` | 1, 2(부대 무효·주장 개성에 `0x19`·`0x1A`·`0x66`·`9AFB0`/`99140` 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g55 |
| CCommandAreaOccupyDepatureNode | `29BA0` | `[0]` 후보 지역 목록, `[1]` 잔류 병력, `[2]` 실행 시 `BB0D0(군단)` 결과 13..16으로 덮어씀, `[3]` 출진 판단 기준, `[5]` ≠ 0이면 군세 종류 `0xD`, `[6]` 경계 거점 목록 | 군단 명령서, 군단 세력 `+0xEA` 관계 바이트 | 지역 점령 출진(`9F860` 취소) | 없음 | `world+0xC0` 세력 중 `(세력 +0xEA + 상대 ID) & 0x7F` ≠ 0 세력을 모음 | `BB0D0`·`2A9C90`·`2CC630`·`9F860` | 1, 2(목록 읽기 실패·비어 있음·군단 명령서 0 등) | 코드 [Gemini 판독 2026-11-25·미검증] g51 |
| CCommandAreaTryGetDepartureNode | `2AB90` | `[0]` 출발 거점, `[1]` 목표 거점 | 군단 명령서, 지역 시설 | 1단계 출진 + 2단계 건설 출진(플레이어 군단이면 `군단 +0x1C` 30비트 마스크로 시설 필터) | 해시형 `3FDAF0` 최대 2회(`3FDAF0(후보 시설 수,1,지역 +0x10,0)` 등) | 적대 종류 2 건물이 남은 채 못 채우면 `9F860(군세)` 뒤 2 | `3FDAF0`·`9F860`·`40C50`·`235150` | 1(`iVar9 < 1` 또는 `iVar9 ≤ uVar27`이고 1단계에서 ≥ 1부대 출진), 2(읽기·유효 실패·명령서 0 등) | 코드(앞 절반은 roles.md:271-272와 일치) [Gemini 판독 2026-11-25·미검증] g54 |
| CCommandExecutionCreditGiveNode | `2D2A0` | `[0]` 공적 부여 대상 무장 목록 | 군단 금·명령서, 목록 | 무장마다 `+0x1BE` 공적, 새 공적 ≥ `world+0x85DC8`의 `+0x2C`이면 `+0x1BC = 2`·`+0x1C4 = 0`, `235150(소속 세력)≠0`이면 `3218E0(무장)`, 금 `−m×B8B8`·명령서 `−B8D0` | 없음 | 유효 무장만 중복 허용 임시 목록 | `1ED620`·`3218E0`·`22EDF0` | 1(게이트 통과 시 `1ED620` 결과와 무관), 2(군단 무효·읽기 실패·지급 거점 무효·게이트 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g53 |
| CCommandExecutionCreditRankUpNode | `2D440` | `[0]` 승급 대상 무장 목록 | 군단 금·명령서, 위계표 | 공적 승급(보상 니블: 지력+정치 > 통솔+무력이면 high `+0x1C3`, 아니면 low `+0x1C2`) | 없음 | 무장 번호 오름차순 | `1ED8F0`·`1F0950`·`040830` | 항상 1(게이트 통과 시 `1ED8F0`과 무관), 2(군단·지급 거점 무효·읽기 실패·게이트 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g53 |
| CCommandExecutionEmployNode | `2D720` | `[0]` 실행 무장 E, `[1]` 등용 대상 T | 두 무장 유효성 | `1EECC0(&{T,E,0}, 0)` 호출(E `+0x15E`의 비트0 켜기 등) | 없음(`1F71B0`·`2F5AA0`·`279DE0` 등 하위는 미입력) | — | `1EECC0` | 1(두 무장 유효, `1EECC0` 결과와 무관), 2 | 코드 [Gemini 판독 2026-11-25·미검증] g52 |
| CCommandExecutionHireNode | `2DAB0` | `[0]` 거점, `[1]` 템플릿 무장 목록 | 군단 명령서, 금 | 목록 원소마다 `331310`으로 등용(명령서·금 차감) | 없음 | 목록 순서, 중간 실패 시 롤백 없음, 목록이 비어도 명령서 차감, 인원 문턱은 unsigned 비교 | `331310`·`31DEE0`·`29FB50`·`227D30` | 1(끝까지 성공), 2(읽기 실패·거점/군단 무효·명령서·금 부족) | 코드 [Gemini 판독 2026-11-25·미검증] g52 |
| CCommandExecutionPrizeNode | `2EEA0` | `[0]` 포상 대상 무장 목록, `[1]` 예산 상한(정수) | 거점 `22EDF0(군단)` 금, 예산 | `1F3C90`: 충성 `+0xE8`(`0x2000` 비트가 있으면 255), `+0x15E`의 비트1 켜기, 금 `−100×대상 수` | `1F3C90`의 `3FDAF0(2,1,지급자 +0x10,대상 +0x10,0,0)` 1회(대상마다) | `B −= 100`을 먼저 하고 B > 0일 때만 대상에 포함 | `1F3C90`·`27660`·`2A8010` | 1(대상 ≥ 1명이면 `1F3C90`을 부르고 반환 무시), 2(선정 대상 수 0이면 `1F3C90`을 안 부름·읽기 실패·무효) | 코드 확인(지휘 세션 2026-11-25; 「실행 성공과 무관하게 1」은 틀림) / [Gemini 판독 2026-11-25·미검증] g53 |
| CCommandFootholdAttackDepatureNode | `2FE10` | `[0]` 공격 목표 거점, `[1]` 출발 후보 목록, `[2]` 잔류 병력(기본 0), `[3]` 최소 잔류 병사, `[4]` 최소 잔류 금, `[5]` 출진 방식(8·9·10·11·22) | 군단 명령서, 출발 거점 | 출진(`9F860` 취소) | 없음 | 출발 거점 거름·방식 분기·전투력 합 검사 | `4B830`·`C2C60`·`B9A00`·`9F860` | 1, 2(군단 명령서 0 등) | 코드(roles.md:190-204와 일치) [Gemini 판독 2026-11-25·미검증] g52 |
| CCommandFrontFootholdTransportDepatureNode | `30EF0` | 인수 없음 | 군단 명령서, 군단 소속 거점, 수송 상한(`9F250`·`9F2F0`·`9F390`) | 수송 출진 명령(정수 15칸: `[0]` 무장 번호, `[1]` 병사, `[2]` `2B7AF0(22E450(무장))`, `[3]` 금, `[4]` 군량, `[5..9]` `0xBD10`, `[10]` 2/3, `[11]` 5/6 …), 군세 `+0x14 = 0xC`·`+0x16 = 목표 +0x4E` | 없음 | 거점 필터·잉여/부족 임계 | `9F250`·`9F2F0`·`9F390`·`2350F0` | 1(군단 소속 거점 ≥ 1이면 출진 0회여도), 2(군단 명령서 0 등) | 코드 [Gemini 판독 2026-11-25·미검증] g53 |
| CDepartureNode | `35A70` | `[0]` 출발 무장, `[1]` 편성 병력, `[2]` 진형, `[3]` 전법 목록, `[4]` 명령 종류(1..8·10·0xE), `[5]` 목표 객체, `[6..9]` → `+0x50..+0x5C`, `[11]` 출력 | 무장, 군단 명령서 `+0x14`, 주체 세력(`B7210`) | 26칸 정수 명령 구조 초기화(`[8..12]=0xBD10`, `[14]=0xFF`, `[20..23]=DAT_14134B3D0`, `[24..25]=0xBD10`) 후 `1EDC30`으로 출진 부대 생성, 출력 변수에 부대 | 없음 | — | `1EDC30`·`2D9530`·`2A26B0` | 1(`1EDC30`이 유효 부대를 돌려주고 쓰기), 2(무장 무효·군단 명령서 0·세력 불일치 등) | 출력 변수(`B29460`)는 출발 무장이 `2D9530`+`2A26B0` 목록에 있을 때 `1EDC30` 결과를 먼저 쓰고, 결과 무효면 그 값(null)이 쓰인 채 2; 그 앞 단계 실패는 쓰기 없이 2 — 코드 확인(지휘 세션 2026-11-25 재정정; roles.md:639 기존 기록이 맞음, Gemini g51 「쓰지 않음」은 틀림) / [Gemini 판독 2026-11-25·미검증] g51 |
| CDepartureTroopsCreateNode | `365A0` | `[0]` 편성할 부대 목록, `[1]` 군세 행동 종류(`+0x14`), `[2]` 목표 객체(`+0x16`에 종류별 색인), `[3]` 출력(≠ 0일 때만) | 부대 `+0x13C`, 부대 `+0x58`의 기존 군세 | 새 군세 생성(`2DB610`)·종류·목표 기록, 기존 군세에서 부대 분리, `[3]`에 군세 | 없음 | 목록 머리부터 순회 | `2DB610` | 1, 2(목록 읽기 실패·핸들 null·원소 0·부대 `+0x13C` ≠ 0) | 코드(roles.md:585 ①~⑤와 일치) [Gemini 판독 2026-11-25·미검증] g51 |
| CDistrictSetPurposeNode | `36D00` | `[0]` 군단 행동방침 값(정수) | — | 군단 `+0x15`에 `-128..127` 클램프 값 | 없음 | — | — | 항상 1(군단 무효여도 2가 아니라 1) | 코드 [Gemini 판독 2026-11-25·미검증] g52 |
| CGetCandidateFacilityListNode | `37210` | `[0]` 출력 후보 시설 정의 목록, `[1]` 정수(입력: 특수 분기 플래그, 출력 있음), `[2]` 건설 주체 거점, `[3]` 건설 대상 지역, `[4]` 정수 출력(특정 시설 단독 추천 여부) | 거점·지역 | 후보 시설 정의 목록 | 없음 | — | `41E7B0`·`40090` | 1(빈 목록도), 2(목록 생성·읽기 실패) | 코드(기존에는 미판독이던 본문) [Gemini 판독 2026-11-25·미검증] g53 |
| CRecruitOfficerSetNode | `3E750` | `[0]` 거점, `[1]` 무장 | 거점 `+0xCA`, 무장 `+0x10` | `1F34F0({거점,무장})`로 모병 담당 배치 | 없음 | — | `1F34F0` | 1(이미 같거나 `1F34F0` ≠ 0, 거점/무장 무효면 `1F34F0`을 안 부르고 1), 2(읽기 실패·명령서 부족·`1F34F0`==0) | 코드 [Gemini 판독 2026-11-25·미검증] g51 |
| CSceneryInvestSetNode | `3E890` | `[0]` 투자할 명승 | 명승 `+0x5F` bit0·`+0x64`==1·`+0x6C` 1..5·`+0x66`==0·`+0x68` < 1, 도시 군단 | 투자 시작 상태(`+0x66` 등; `+0x66`은 덮어쓰기 뒤 `d ≥ 1`이면 0) | 없음 | — | `22E4D0`·`22B910`(명승 `+0x5C` 칸 → 지역 객체)·`40060`·`22C5F0` | 1, 2(군단 무효·명승 무효·조건 불충족) | 코드 [Gemini 판독 2026-11-25·미검증] g53 |
| CTrainingOfficerSetNode | `3EF50` | `[0]` 거점, `[1]` 무장 | 거점 `+0xCC`, 무장 `+0x10`, 거점 군단 명령서 | `201A80({거점,무장})`: `+0xCC = clamp(ID,0,6000)`, 명령서 `−B440`(0..200) | 없음 | — | `201A80`·`29DE10`·`279890` | 1(이미 같거나 거점/무장 무효 또는 `201A80` ≠ 0), 2(읽기 실패·명령서 부족·`201A80`==0) | 코드 [Gemini 판독 2026-11-25·미검증] g52 |
| CClearFriendForceListNode | `52910` | 인수 없음 | — | 세력 `+0x17F..+0x183` 5바이트를 0으로 | 없음 | — | `B7210` | 항상 1 | 코드 [Gemini 판독 2026-11-25·미검증] g54 |
| CClearTargetForceListNode | `52950` | 인수 없음 | — | 판단 주체 세력 `+0x17A..+0x17E` 5바이트를 0으로 | 없음 | — | `B7210` | 항상 1 | 코드 [Gemini 판독 2026-11-25·미검증] g53 |
| CCommandExecutionDoctrinePanelAutoNode | `52FC0` | `[0]` 정수(≠ 0이면 먼저 주의 판 환불·초기화 `337380`) | 세력(`B7210`), 군주 군단 명령서(< `DAT_141A4B6B4`이면 조기 종료) | 후보를 정렬해 여러 항목 채택(`2EF700(군주군단, 항목, 0)`) | 없음 | 정렬자 `50450`·`50FB0`·`52480`(미입력) | `522B0`·`230270`·`337380`·`2EF700` | 1(명령서 부족 조기 종료 또는 루프 완료), 2(세력·군주 군단 무효·후보 항목 포인터 0 등) | 코드(정렬자·선호 항목 선택 미대조) [Gemini 판독 2026-11-25·미검증] g53 |
| CCommandExecutionExchangeNode | `53530` | `[0]` 대상 객체, `[1]` 임무 담당 무장, `[2]` 제공 종류(0 금·1 군량·4 지역), `[3]` 제공 양·지역, `[4]` 요구 종류, `[5]` 요구 양·지역 | 제안 구조 | 제안 구조 `cmd[0] = 0x13`(19)·`cmd[2]=[0]`·`cmd[4]=[1]`을 채워 `1EE460(cmd,0)` 제출 | 없음 | **받을 쪽(`[4]`,`[5]`)부터** 읽음, `331780` 검사 없음 | `1EE460`·`230350` | 1(조건 통과 시 항상), 2(읽기 실패·`[4]`가 0·1일 때 `[5]` 읽기 실패 등) | 코드 [Gemini 판독 2026-11-25·미검증] g51 |
| CCommandExecutionGovernmentAutoNode | `53B80` | `[0]` 대상 세력 | 군주 군단 명령서 | 시정 5행 + 군사 배치 적용(비용 `51FF0`) | 없음(`53B80`·`51FF0`·`2EFA70`·`2F1780`·`2EB110` 범위) | — | `263520`·`51FF0` | 1(비용 지불·적용 완료), 2(읽기·유효 실패·군주 군단 명령서 0 등) | 코드 [Gemini 판독 2026-11-25·미검증] g54 |
| CCommandExecutionItemNode | `54250` | `[0]` 받을 무장, `[1]` 하사할 명품 | 이전 소유자(`58FD0`) 군단(`40C20`) 명령서 ≥ `DAT_141A4B5B8` | `1F16B0`(즉시 실행: 충성 증감·명품 소유자 변경·명령서 차감) | 없음 | — | `1F16B0`·`58FD0`·`40C20` | 1(`1F16B0` ≠ 0), 2(읽기 실패·무효·명령서 부족·`1F16B0`==0) | 코드 [Gemini 판독 2026-11-25·미검증] g53 |
| CCommandExecutionTradeNode | `54CE0` | `[0]` 교역 대상(지역·이민족, `22F740`), `[1]` 파견 무장 목록, `[2]` 요구 금, `[3]` 요구 군량, `[4]` 요구 병사 | 본거지(`230350(B7210)`) 금·군량·병사 | 요구량을 모두 엄격히 초과할 때만 `1EBC60`(행상 행동) 호출 | `1EBC60` 내부 난수 `R(100,10,…)` 2회(이번 입력에 없어 미대조) | — | `1EBC60`·`22F740` | 1(`1EBC60` 호출), 2(읽기·무효·자원 부족) | 코드(`1EBC60` 하위 미대조) [Gemini 판독 2026-11-25·미검증] g53 |
| CForceCommandMoveNode | `55310` | `[0]` 목표 거점 목록 L0, `[3]` L0 소속 도시 목표 인원 가중치, `[4]` L0 밖 도시 가중치, `[5]` 관문류 가중치, `+0x50` 키(≠ 0이면 대상 세력 교체) | 대상 세력(기본 `B7210`, 교체 결과 무효(`331780`==0)면 다시 `B7210`) — 군단이 아니라 세력, 원소 `+0x1C` 하한 = `(도시 ? 22BA10(지역) : (관문 ? 1 : 0)) + 2` | 무장 이동 명령(`1F2630`) 최대 3건 | 없음 | 정렬 3연속 | `1F2630`·`6DA4D0`·`231DB0` | 1(대상 세력 거점 ≥ 2이면 루프를 마친 뒤, 발행 0건도 1), 2(L0 읽기 실패·거점 < 2) | 코드 확인(세력, 지휘 세션 2026-11-25) / [Gemini 판독 2026-11-25·미검증] g52 |
| CForceSetPurposeNode | `56A40` | `[0]` 세력 행동방침 값(정수) | `B7210` 세력 | 세력 `+0x4A`에 기록 | 없음 | — | `B7210` | 1, 2(세력 무효) | 코드 [Gemini 판독 2026-11-25·미검증] g52 |
| CSetFriendForceListNode | `58B90` | `[0]` 친선 대상 세력 목록 | 목록 앞 5개(`vtable+0x60`) | 세력 `+0x17F..`에 `[0, 0x33]`로 잘라 기록(남는 칸 유지) | 없음 | 목록 앞 최대 5 | — | 1(빈 목록도), 2(읽기 실패·`local_res8`==0) | 코드 [Gemini 판독 2026-11-25·미검증] g54 |
| CSetTargetForceListNode | `58C90` | `[0]` 공략 대상 세력 목록 | 목록 앞 5개 | 세력 `+0x17A..+0x17E`에 `[0, 0x33]`로 기록(남는 칸 유지) | 없음 | 목록 앞 최대 5 | `B7210` | 1(빈 목록도), 2 | 코드 [Gemini 판독 2026-11-25·미검증] g53 |
| CArmySetTargetArmyNode | `61D30` | `[0]` 대상 부대, `[1]` 목표 객체 | 부대 행동 종류 | 행동 종류에 따라 목표를 부대에 기록(건너뛰기도 있음) | 없음 | — | `331780` | 1(부대 유효), 2(읽기 실패·부대 무효) | 코드(functions.md:819와 일치) [Gemini 판독 2026-11-25·미검증] g52 |
| CAttackFootholdRelayAreaAttackNode | `61F10` | `[0]` 미사용, `[1]` 점령률 기준값, `[2]`~`[4]` 불리언(`+0x1C` 병참선 확보·`+0x1D` 주변 적 요격·`+0x1E` 재집결 이동) | 군세 `+0x16` 목표 거점·`2CC630` | 군세 `+0x18` 경유 직접 갱신, `CC160`, `27D490`(모드 8·9·10·22) | 없음 | — | `CC160`·`27D490`·`32E3B0` | 1, 2(목표 거점 세력이 군세 세력과 다르고 비적대 등) | 코드(roles.md:426-447과 일치) [Gemini 판독 2026-11-25·미검증] g52 |
| CExecuteAreaAttackNode | `65A60` | `[0]` 점령률 기준값, `[1]`~`[3]` 미사용 | 군세 `+0x14` | `CCDF0`·`CAA60`·`CC160` 분기, 모드 21(`0x15`)이면 `27D490`, 모드 3·13(인수 0==0)이면 `71B00` | 없음 | — | `27D490`·`71B00`·`CCDF0`·`CC160`·`2DDD80` | 1(작업 목록이 비었거나 진행 중 유효), 2(군세 `+0x14`가 0·7·17·18) | 코드(roles.md:447의 `27D490` 조건 「모드 3·13·14」는 다름: 실제는 모드 21) [Gemini 판독 2026-11-25·미검증] g52 |
| CExecuteConstructNode | `69420` | 인수 없음(판단 주체=군세) | 군세 `+0x14`==5, 건설 칸 `+0x16` | 비건설 구성원 퇴각 등 건설 실행 | 없음 | — | — | 1(칸에 건물 없어 비건설 구성원 퇴각·적대 건물 처리 등), 2(군세 `+0x14` ≠ 5 등) | 코드(roles.md:562·574와 일치) [Gemini 판독 2026-11-25·미검증] g54 |
| CExecuteFacilityAttackNode | `69740` | 인수 없음 | 군세 `+0x14`==4, 노드 상태 `+0x0A` 칸의 목표 시설 | 시설 공격 실행 | 없음 | — | — | 3(목표 시설이 칸에 여전히 있고 유효·적대 등), 2(군세 `+0x14` ≠ 4) | 코드(roles.md:573과 일치) [Gemini 판독 2026-11-25·미검증] g54 |
| CExecuteFootholdOccupyNode | `69AB0` | 인수 없음 | 군세 `+0x14`(모드) | `A33B0`·`A33E0`·`A3370`·`C0390`·`27D490` 연동, `27D490`은 모드 8·9·10·22(`(모드 − 8) < 3` 또는 `0x16`)일 때 | 없음(`5DF20` 내부는 미확인) | — | `27D490`·`C0390` | 1(정상 완료), 2(모드가 0 또는 7) | 코드(roles.md:447의 「모드 2·8·9·10」은 다름) [Gemini 판독 2026-11-25·미검증] g52 |
| CExecuteInterceptNode | `6AA10` | `[0]` 경유점 설정 플래그, `[1]` 선봉 부대 선택·정렬 플래그(3번째 인수는 안 읽음) | 군세 `+0x14`·`+0x16`(경계군세 ID, `world+0x80BA8 + id×8`), 부대 `+0x1B`(병과) | 요격 군세 구성원 가운데 병과 7..10인 부대에만 `2EC570(부대,1,0)` 호출(한 곳뿐). 요격이 풀릴 때는 군세 `+0x14`를 7 또는 0(비적대 시)으로 바꿀 뿐 `2EC570`을 안 부름 | 없음 | — | `2EC570` | 1(적 부대 목록 비음·목표 거점 변경·적 부대 목표 거점 이탈 등), 2(군세 `+0x14` ∈ {0,7,17,18}(`0x60081`) 등) | 코드 확인(지휘 세션 2026-11-25; roles.md:560·715 부분 정정) / [Gemini 판독 2026-11-25·미검증] g54 |
| CSetFootholdAttackRelayHexNode | `6E950` | `[0]` 군세, `[1]` 공격 목표 거점 | 구성원 부대 `+0x13C` | 지역 중심 칸(`C0390`)을 군세 작업 목록(`+0x18..+0x2B`)에 기록, 목록 첫 칸은 대표 부대 | 없음 | 길찾기 후 지역 중심 칸 추출 | `C0390`·`185710` | 1(길찾기 성공), 2(읽기·`331780` 실패·구성원 `+0x13C` ≠ 0) | 코드(roles.md:425·545와 일치) [Gemini 판독 2026-11-25·미검증] g54 |
| CSpecifiedTroopsSetPurposeNode | `6F070` | `[0]` 군세, `[1]` 목적 종류(0..0x17), `[2]` 목표 객체 | 구성원 부대 `+0x13C` | 군세 `+0x14`·`+0x16`: 종류 0·0x11·0x12 → `+0x14 = min(종류,0xFFFF)`·`+0x16` = 거점 `+0x4E`(구성원 초기화), 1·0x13 → `+0x14 = 1`·경계군세 색인, 2·8~12·0x16 → 거점 `+0x4E`, 3·0xD~0x10·0x15·0x17 → 지역 번호(`22F470`), 4·0x14 → `+0x14 = 4`·건축물 색인, 5·6·7 → `+0x14` = 5/6/7·칸 색인 | 없음 | 구성원 부대 순회 | `22BB50`·`22F470`·`22F520`·`22F930`·`22F830`·`1402F03D0`(일부 인수 미상) | 1(`[2]` 무효면 `+0x16`에 0을 쓰는 경우도 1), 2(군세 무효·구성원 부대 `+0x13C` ≠ 0) | 코드(roles.md:395·576-577과 일치; `case 1/0x13`은 `+0x14 = 1`, `case 4/0x14`는 4로 강제 — 추가 확인) [Gemini 판독 2026-11-25·미검증] g51 |
| CGetBattlePowerSoldierNumNode | `7BE80` | `[0]` 무장, `[1]` 요구 전투력, `[2]` 출력(편성 병력) | 무장 지휘 병력(< 1000이면 결과 0) | 요구 전투력을 채우는 편성 병력 수를 `[2]`에 | 없음 | — | `331780` | 1(`[2]` 쓰기 성공), 2(읽기 실패·무효·쓰기 실패) | 코드(기존 기록에는 상세 본문이 없었음) [Gemini 판독 2026-11-25·미검증] g53 |
| CGetCanServePersonListNode | `7C300` | `[0]` 군단, `[1]` 출력 등용 대상 후보 목록 | 명령 관리자 목록(종류 2, 같은 세력, 첫 대상 종류 1) | 후보 수집 후 이미 내린 등용 명령의 대상을 `21A350`으로 제거 | 없음(`6DF810` 내부 미확인) | 같은 세력 명령 순회 | `6DF810`·`1F0A30`·`21A350` | 1, 2(군단 읽기 실패·무효·목록 확보 실패) | 코드(명령 관리자 순회·제거는 기존 기록과 일치; `1F0A30`·전역 무장 순회 조건은 `6DF810` 안일 것으로 추정되나 아무도 `6DF810`을 읽지 않아 판정 보류 — 미해결) [Gemini 판독 2026-11-25·미검증] g52 |
| CGetEarthenStoneWallBuildHexNode | `7CB80` | `[0]` 대상 지역, `[1]` 기준 무장, `[2]` 시설 정의, `[3]` 선택적 세력(적대 세력 초기값), `[4]`·`[5]` 출력 칸 1·2 | 무장 소속 거점 `+0xB0`·`+0xA8`, 위협 거점·최단 거리 거점 | 시설 ID 9·10(또는 `0x10`)에서 조건을 만족하는 건설 칸 2개를 `[4]`·`[5]`에 | 없음 | — | `331780`·`185710` | 1(칸 2개를 찾았을 때), 2(`[0]`~`[2]` 읽기·유효 실패·적대 세력 없음·출발 무효 등) | 코드(unresolved.md:175와 일치) [Gemini 판독 2026-11-25·미검증] g54 |
| CGetFootholdFightingStrengthNode | `7EBA0` | `[0]` 대상 거점, `[1]` 출력 전투력, `[2]` 주변 아군 포함 거리 상한(직접값), `[3]` 잔류 병력, `[4]` 부대 위치 판정 플래그, `[5]` 제외 플래그 | 거점 `+0x3C`, 거점 무장, `22E3E0(거점)`(소속 세력 객체이지 부대 목록이 아님)의 부대 목록(`224B00`·`224880`) | 전투력(정수)을 `[1]`에 | 없음 | 거점 무장 목록을 머리부터(제외 플래그가 있으면 `2D9530` 목록의 무장만) | `BBEC0`·`22E3E0`·`224B00`·`224880` | 1(쓰기 성공), 2(거점 무효·쓰기 실패) | 코드(functions.md:495와 세부 차이 2건) [Gemini 판독 2026-11-25·미검증] g51 |
| CListClearNode | `83420` | `[0]` 목록 종류(0..0x12), `[1]` 목록 | 변수·목록 | 목록 전체 비우기(`37DF00` → `186D0`); 종류 0xE는 정수 풀 `141B5F9E0`, 종류 0xF는 비우기 전에 원소마다 `92B10`→`331780`==0이면 `32D0E0(world, 원소)` | 없음 | — | `37DF00`·`186D0`·`92B10`·`32D0E0`·`1A250` | 1, 2(종류 범위 밖·목록 확보 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g50 |
| CVariableCreateNode | `864B0` | `[0]` 정수 변수 키, `[1]` 정수 상수 | — | `[0]`에 4바이트 정수 | 없음 | — | `B29250` | 1(쓰기 성공), 2 | 코드 [Gemini 판독 2026-11-25·미검증] g50 |
| CVariableGetAdvantageInfoNode | `86680` | `[0]` 지역 이점 레코드, `[1]` 조회 항목(직접값, 0만 지원), `[2]` 출력 정수 | 지역 이점 객체 | `[2]`에 결과 | 없음 | — | `B28D20`·`B29250` | 1, 2(읽기 실패·무효·항목 ≠ 0·쓰기 실패) | 코드(unresolved.md:159와 일치) [Gemini 판독 2026-11-25·미검증] g54 |
| CVariableGetAreaInfoNode | `86720` | `[0]` 지역, `[1]` 항목(0~0x18), `[2]` 출력 | 지역 객체 | 항목별 값: `case 0` = `22F470`; `case 9`는 무동작 1, `case 0x11`은 `22F3F0`·AgentType 조회를 버린 뒤 `case 0xE`(`+0x54`)로 합류 | 없음 | — | `22F470` | 1, 2(읽기 실패·무효·범위 밖·쓰기 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g50 |
| CVariableGetArmyInfoNode | `871D0` | `[0]` 부대, `[1]` 항목(0~0x1D), `[2]` 출력 | 부대 객체 | 항목별 값; `case 0x13`의 미지원 종류·`case 0x18`(가장 가까운 적대 거점 없음)은 `[2]`에 안 쓰고 1 | 없음 | — | — | 1, 2(읽기 실패·무효·범위 밖·`case 0xD/0xE/0xF`에서 AgentType 읽기 실패·쓰기 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g50 |
| CVariableGetBuildingInfoNode | `87FE0` | `[0]` 건물, `[1]` 항목(0..4), `[2]` 출력 | 건물 객체 | `case 0` = HEX(`70CC0`: 건물 `+0x10` < `0xBD10`이면 `world+0xE270` 칸), `case 2` = 세력(`92B40`), 1·3·4 추가 | 없음 | — | `70CC0`·`92B40` | 1, 2(읽기·무효·범위 밖·쓰기 실패) | 코드(unresolved.md:82·83과 일치) [Gemini 판독 2026-11-25·미검증] g51 |
| CVariableGetDistrictInfoNode | `88780` | `[0]` 군단, `[1]` 항목(0..2·4..0x14), `[2]` 출력 | 군단 객체 | 항목별 값(`case 0` = `22F650`, `case 0x14` = `232CC0`, `case 0x13` = `26D660`); `case 3` 없음(2), `case 0x12` 끝에 `break`가 없어 `case 0x13`으로 fall-through | 없음 | — | `22F650`·`232CC0`·`26D660`·`40C50` | 1, 2(읽기 실패·항목 3 또는 > 0x14·`case 8..0xB`에서 `B28DE0` 실패 등) | 코드 [Gemini 판독 2026-11-25·미검증] g50 |
| CVariableGetCautionTroopsInfoNode | `882E0` | `[0]` 경계군세 자료, `[1]` 항목(0..8), `[2]` 출력 | 경계군세 | 항목 0 = `+0x18`, 1 = `+0x20` float 캐시·`B6F50` 합, 3 = `+0x3C`, 4 = `32E3B0(world,+0x1A)`, 6 = `+0x08`, 5·7·8 추가 확인 | 없음 | — | `B6F50`·`32E3B0` | 1(`case 5`에서 객체 무효면 0을 쓰고 1), 2(읽기 실패·무효·범위 밖·쓰기 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g50 |
| CVariableGetFootholdInfoNode | `8B190` | `[0]` 거점, `[1]` 항목(0..0x2D), `[2]` 출력 | 거점 객체 | 항목별 값(`case 0x26` = 거점 `+0x94`, `case 0xB` = 병사 + 상수 × 성향 `+0x16A` × 병사 ÷ 10000, `case 3` = `22E3E0`) | 없음 | — | `9935F0`(`case 0x2B`)·`22E3E0`(`case 0x2D`) 등 | 1, 2(읽기·무효·범위 밖·`case 0x2B`에서 `1400935F0`==0·`case 0x2D`에서 `22E3E0` 무효 등) | 코드(`DAT_141A4AFD8`·`AFFC`·`B008` 값 미확인) [Gemini 판독 2026-11-25·미검증] g50 |
| CVariableGetForceInfoNode | `8CAE0` | `[0]` 세력, `[1]` 항목(0..0x27), `[2]` 출력 | 세력 객체 | `case 4` = 세력 군단별 `world+0x80` 거점 전력합(0이면 1), `case 5` = 우호도 바이트 × `(1 + DAT_141A4AFE4 × 의리 +0x16C / 10000)`, `case 8` = 세력 `+0x08` | 없음 | — | `B7210`(`case 5`) | 1(`case 0x14`는 무동작 1), 2(읽기·무효·범위 밖·`case 5`에서 `B7210` 결과 무효·`case 0x1C` 등) | 코드 [Gemini 판독 2026-11-25·미검증] g50 |
| CVariableGetFormationInfoNode | `8EA40` | `[0]` 진형, `[1]` 항목(0..5), `[2]` 정수 출력 | 진형 객체, 현재 주체 세력(`B7210`: AgentType 4 직접·3 `world+0xDF30`·2 `22E560`·1 `22E2A0`) | 항목 값(`case 2`·`3`은 이번에 추가 확인) | 없음 | — | `B7210`·`2B24D0`(`+0x7F` 읽기는 하위 미포함) | 1, 2(무효·범위 밖·쓰기 실패) | 코드(unresolved.md:121-124와 일치) [Gemini 판독 2026-11-25·미검증] g51 |
| CVariableGetGameDataNode | `8EB70` | `[0]` 항목(0..6), `[1]` 출력 | 게임 데이터 | `case 0` 년, 1 월, 2 일, 3 순 카운터 `G+0x454`, 4·5 `G+0x1656`·`G+0x1657` 세력 객체, 6 옵션 41(미활성 시 100) | 없음 | — | `31E7A0`·`3EC1A0`·`3ED810`·`7AB6A0`·`3EC920`(내부 미입력) | 1, 2(범위 밖·쓰기 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g50 |
| CVariableGetHexInfoNode | `8ED40` | `[0]` 칸, `[1]` 항목(0..6), `[2]` 출력 | 칸 객체 | `case 0` = `22F830`(칸 번호), `case 1` = 지역(`22B8E0`), `case 6` = 건물(`2315A0`), 2·3·4·5 추가 | 없음 | — | `22F830`·`22B8E0`·`2315A0` | 1(`case 5`에서 유효 거점을 못 찾으면 쓰지 않고 1인 경우 포함), 2(무효·범위 밖·쓰기 실패) | 코드(unresolved.md:125·126과 일치) [Gemini 판독 2026-11-25·미검증] g51 |
| CVariableGetMoveCostNode | `8F5A0` | `[0]` 출발 객체 종류(0..10·0x12), `[1]` 출발 객체, `[2]` 도착 종류, `[3]` 도착 객체, `[4]` 출력 이동 비용 | 칸(`BFBC0`), 지역 중심 칸 500×500 캐시(`DAT_141B9D4F0 + 0xC0`) | 이동 비용(정수)을 `[4]`에 | 없음(`8F5A0`·`BFBC0`·`9DA10` 기준) | — | `BFBC0`·`9DA10` → `185710` | 1(쓰기 성공), 2(출발·도착 칸이 `0xBD10`·쓰기 실패) | 코드(functions.md:405는 `9DA10`을 거쳐 `185710`을 부름) [Gemini 판독 2026-11-25·미검증] g51 |
| CVariableGetPersonInfoNode | `8F810` | `[0]` 무장, `[1]` 항목(0..0x26), `[2]` 출력 | 무장 객체 | 항목별 값(`case 5` = `+0xE6`, `case 6` = `+0xE8`, 13 = `+0x16A`, 14 = `+0x16C`, 29 = `22D280`) | 없음 | — | `22D280` 등 | 1, 2(읽기 실패·`331780`==0·범위 밖·쓰기/목록 확보 실패) | 코드(`DAT_141A4D1D4` 값 미확인) [Gemini 판독 2026-11-25·미검증] g50 |
| CVariableGetSceneryInfoNode | `8FFA0` | `[0]` 명승, `[1]` 항목(0..7), `[2]` 출력 | 명승 객체, 명승 `+0x5C` 칸(`world+0xE270`, `0xBD10` 미만)의 칸 `+0x12` | `case 0` `22FAD0`, `case 3` `+0x6C`, `case 6` `22C5F0`; `case 5` = `22B910`: 칸 `+0x12` < `0x1F5`이면 `world+0x6CAF0` 지역 객체, 아니면 `world+0x6CAF0` 0번 칸(부대 객체가 아님) | 없음 | — | `22FAD0`·`22B910`·`22C5F0` | 1, 2(읽기·무효·범위 밖·쓰기 실패) | `22B910` 정정은 코드 확인(지휘 세션 2026-11-25; unresolved.md:132 정정), 나머지 [Gemini 판독 2026-11-25·미검증] g51 |
| CVariableGetTroopsInfoNode | `90110` | `[0]` 군세, `[1]` 항목(0..0xF), `[2]` 출력 | 군세 객체, 항목 4 목표 종류별 표(0·2·8~12·17·18·22 = 거점 `32E3B0`, 1·19 = 경계군세 `world+0x80BA8`, 3·13~16·21·23 = 지역 `world+0x6CAF0`, 4·20 = 건축물 `world+0x6DA98`, 5·6·7 = 칸 `world+0xE270`) | 항목별 값(항목 3 = `22BB50`) | 없음 | — | `22BB50`·`32E3B0` | 1(`case 4`에서 종류·번호 범위 밖이어도 1 포함), 2(읽기·무효·범위 밖·`case 5/0xB/0xC`에서 AgentType 읽기 실패·쓰기 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g50 |
| CVariablePlusValueNode | `92270` | `[0]` 정수 변수, `[1]` 정수 상수 | `[0]` | `[0] = [0] + 상수`(32비트 래핑) | 없음 | — | `B28BB0`·`B29250` | 1, 2(읽기·쓰기 실패) | 코드 [Gemini 판독 2026-11-25·미검증] g50 |
| CCautionTroopsListDedupeNode | `4F90C0` | `[0]` 경계군세 목록(노드 정의상; 실행 함수는 읽지 않음) | — | 없음(스텁 구현, 판단표 주석 「현재구현은성공반환」) | 없음 | — | — | 항상 성공(1) | 코드(스텁; node_kinds.md:206·309와 일치) [Gemini 판독 2026-11-25·미검증] g54 |

판독 불일치와 남은 것:

- `29A90` ②③④ 정렬 방향: Codex c14(내림)와 앞 차수 Sonnet(오름)이 갈렸으나 지휘 세션이 코드로 **내림**으로 판정했다(2026-11-25, `23500`·`23730`·`23290`의 비교 방향이 ① `22DB0`과 반대).
- `85100`: Gemini g44의 가설(`[0]==0`이면 성공)은 이 문서 「더미 노드」 절의 바이트 확정(인수 1이면 결과 1)과 반대다. 후자를 따른다.
- `7EF50` 반경 칸 목록: Gemini g47의 「중심 칸 포함」을 지휘 세션이 코드로 확인했다(2026-11-25). `2A9C90` 자체는 중심을 빼고, 노드 본문이 없으면 더한다. ai/roles.md·functions.md도 같이 고쳤다.
- 가설로 남긴 것: `81BF0`이 부르는 `331780`의 가상 함수 부작용, `7B450` 안의 `2695D0`·`2B4CA0` 의미, `29A90`의 관직 vtable `+0x58`, `3A200`의 `27A8D0` 생략 인수, `84CB0` 정렬 방향(`140023D40` 미확인). 값 미확인 상수: `DAT_141A4B720`·`B72C`·`B734`·`B21C`·`B434`·`B440`·`B718`·`B60C` 등 명령서 임계값·비용(`B5CC` = 1은 PE 읽음).

## 정정 기록

| 옛 해석 | 정정본 | 근거 |
|---|---|---|
| `53270`: 거점 `+0x14`가 임계값 이상일 때만 실행 | 실행 무장의 **군단** `+0x14`(명령서)가 `DAT_141A4B740` 이상일 때 | [Sonnet 판독 2026-11-25·미검증] s3 |
| `52FC0`(functions.md 577): 주의 채택 명령 1회 실행, 옛 RVA `52350` | 후보를 정렬해 명령서가 닳을 때까지 여러 항목 연속 채택하는 반복 노드. 옛 RVA `52350`은 현 빌드에서 `522B0` 안쪽(함수 시작점 아님) | [Sonnet 판독 2026-11-25·미검증] s3 |
| `53B80`: 내정 자동 명령 | 시정 5줄 + 군사 자동 배치(명령서로 비용 지불, 모자라면 되돌림) | [Sonnet 판독 2026-11-25·미검증] s3 |
| `29A90`: 정렬 헬퍼 7개 모두 정렬, 방향 미해결 | ①~④ 오름·⑤ 내림, 모두 안정 삽입(마지막이 최우선); ⑥⑦은 조건 분할 이동(군단장·군주가 대장인 부대를 앞으로, 만족 원소는 역순, 원래 머리 원소는 미검사로 그 뒤) | ①·⑥⑦ 확정(코드, 지휘 세션 대조 2026-11-25); ②~⑤ [Sonnet 판독 2026-11-25·미검증] s3. **5차 재정정: ②③④는 내림(코드 확인, 지휘 세션 2026-11-25)** |
| `3A200` 인수 `[6]`: 수치(0이면 A 갈래 허용) | 그 값은 B 갈래 경로 방향 플래그도 겸한다(0: 기점→지역, 그 밖: 지역→기점) | [Sonnet 판독 2026-11-25·미검증] s3 |
| `1FE50`: 가까운 본거 조회 | 이번 이동 경로 위 지역 중심 칸을 경유점에 보충(`9CC90`) | [Sonnet 판독 2026-11-25·미검증] s4 |
| `2D720`·`7C300`: 세력 BT 3회(functions.md) | 군단 판단표 3회(사용 횟수 열이 군단) | [Codex 판독 2026-11-25·미검증] |
| `3E750`(CRecruitOfficerSetNode): 등용 담당관 설정 | 거점 `+0xCA` 모병 담당관 배치(Remove `3E6B0`도 같은 필드, 0번 무장 기준 해제) | [Codex 판독 2026-11-25·미검증] |
| `3E6B0`·`3EEB0`: 판단표 둘째 인수(현재 모병/훈련 담당관)를 노드가 소비 | 코드는 첫 인수(거점)만 읽는다 | [Codex 판독 2026-11-25·미검증] |
| `3EAA0`: 사전 검사와 차감이 같은 상수 | 사전 검사 `DAT_141A4B440`, 실제 차감 `DAT_141A4B21C`(다른 상수) | [Codex 판독 2026-11-25·미검증] |
| `BFBC0` 종류 0·1: 둘 다 「무장」 → 소속 거점(`230350`·`22EDF0`) | **0 = 세력 객체**(`+0x10` u16 = 군주 무장 번호) → 군주 소속 거점 칸, **1 = 군단 객체**(`+0x12` u16 = 군단장 무장 번호) → 군단장 소속 거점 칸. 두 함수는 같은 구조이나 읽는 필드가 다르다 | [Sonnet 판독 2026-11-25·미대조] g30 → 작성자 디컴파일 대조(`BFBC0`·`230350`·`22EDF0` 본문, structs.md 세력·군단 절) |
| `7B7B0`: 표 접근식 `표+번호×8`이 정의 크기 `0x48`과 맞지 않음(미확인) | 충돌 아님: `world+0x73860`은 포인터 배열, 가리키는 지형 정의 객체가 0x48바이트(structs.md 「지형 객체 표」와 같은 뜻) | [Sonnet 판독 2026-11-25·미대조] g30 → 작성자 디컴파일 대조(`233310`) |
| (5차 판독 요약) 「공통 모양」의 「추가 뒤 `331780`」, `828A0`·`52EC0`·`52CA0`·`32D90`·`7B450`·`7B590`·`7BA50`·`7EEE0`·`7EF50`·`7FC10`·`29A90`·`3A200`·`36E80`·`3C1F0`·`3A0C0`·`3DB90`·`3E400`·`2F080`·`3EBC0`·`801D0`·`7B0B0`·`2E410`·`5D760`·`85EC0` 한 줄 설명 | `331780`은 비Unique 추가 노드(`81BF0`·`82170`·`81EB0`·`81160`)에만; 인수 순서·상수·읽는 필드·반환값·두 번째 목록 등을 위 「노드 실행 함수 다섯 항목」 표대로 고침(고친 줄마다 「5차 정정, 출처 표시」). `29A90` ②③④ 방향과 `85100` 결과값은 판독 불일치로 둘 다 적음 | [Sonnet 판독 2026-11-25·미검증] s5~s16, [Codex 판독 2026-11-25·미검증] c9~c11·c14, [Gemini 판독 2026-11-25·미검증] g40~g49, 지휘 세션 코드 확인(`85EC0`·`331780`·`548D0`·`92870`) |
| (5차 판독 2차분 요약) `2EEA0` 「실행 성공과 무관하게 1」, `55310` 「대상 군단 교체」, `54330` 「관직 rank」(functions.md), `2D2A0`·`2D440`, `7C300` 한 줄 설명; 표에 부록 A 밖 69종(g50~g55) 추가 | `2EEA0`은 선정 대상 수 0이면 `1F3C90`을 안 부르고 2, 1명 이상이면 1; `1F3C90` 충성식·`0x2000`이면 255; `55310`은 군단이 아니라 세력(`B7210`, 무효면 재설정); `54330`은 무장 군단 `+0x14` < `B5CC`이면 2; `35A70` 출력 쓰기는 `1EDC30` 결과가 무효여도 먼저 씀(기존 기록 유지, Gemini g51 「안 씀」은 틀림 — 같은 날 재정정); `6AA10`의 `2EC570` 호출은 병과 7..10 구성원 한 곳뿐; `8FFA0`의 `22B910`은 지역 객체; `7C300`의 `1F0A30` 조건은 `6DF810`이 미판독이라 판정 보류. `7EF50`의 중심 칸 포함·`29A90` ②③④ 내림은 지휘 세션 코드 확인 | 지휘 세션 코드 확인(위 항목들, 2026-11-25), [Gemini 판독 2026-11-25·미검증] g50~g55 |
