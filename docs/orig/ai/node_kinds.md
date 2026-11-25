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
- **목록 풀·핸들·추가 규칙 [Sonnet 판독 2026-11-25·미검증, 코드]**: 모든 목록은 전역 풀 `DAT_1427d4130`의 ID별 이중 연결 목록이다(`+0x10` 머리 배열 `1427D4140`, `+0x18` 꼬리 배열, `+0x20` 빈 노드 자유 목록, `+0x28` ID별 개수표 `1427D4158`, `+0x30` 전체 개수, `+0x40` ID 한도; 노드 `+0x00` 원소 8바이트·`+0x08` 다음·`+0x10` 이전). 목록 변수는 16바이트 객체이고 `+0x08`이 가리키는 uint가 목록 ID이며, `+0x08`이 널이면 ID `0x14000`(널 목록 칸)을 쓴다. 변수가 없으면 추가·비우기 노드는 `1A250(키, 종류, …)`으로 새 목록을 만들어 변수에 쓰는데, 저장소에 `HeapListInfo` 변수가 없으면 아무것도 못 만들어 결과 2다. 종류 코드: 0 세력, 3 군세(부대), 4 무장, 5 거점, 6 지역, 7 칸, 0xB 경계군세, 0xE 정수 목록(별도 풀 `141B5F9E0`). **추가 `18D50(풀, ID, 플래그)`**: ID ≥ 한도이거나 자유 노드가 없으면 아무것도 안 하고(노드는 그래도 1), 플래그 ≠ 0이면 **꼬리 추가**, 0이면 머리 추가이며 `CListAdd…` 18종 모두 플래그 1(꼬리 추가)로 부른다. 따라서 머리부터 돌면 추가 순서와 같다(FIFO, 순번 0 = 가장 먼저 추가된 원소). `CListAdd…` 계열은 원소 값 8바이트를 널·유효 검사 없이 그대로 넣고(포인터 동일성이 정체성), 중복을 허용하며(`…Unique`는 머리부터 8바이트가 같은 항목이 있으면 추가 없이 1), 읽기 실패만 2이고 풀이 가득 차 추가가 안 돼도 1이다. 지역·세력·거점·칸 추가 노드는 추가 뒤 `331780(원소)`을 부르지만 결과를 쓰지 않는다. `CListAddUniqueCautionTroopsNode`(`831A0`)만 목록 핸들 `+8`이 널이면 중복 조회 없이 무조건 추가한다(다른 Unique 노드는 널 핸들이면 ID `0x14000`을 조회). 제거 `189B0`은 앞뒤를 이어 붙이고 노드를 자유 목록으로 돌려 상대 순서를 유지하며, 전체 비우기 `186D0`은 체인 전체를 자유 목록에 붙이고 개수를 0으로 한다. 난수는 목록 노드 18종 모두 없다.

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
| CListAddPossibleFacilityNode | `828A0` | 3개: 칸(HEX), 건설 주체(무장), 출력 목록(종류 0x10 시설 정의) | 시설 정의 표(`world+0x73958`부터) 가운데 `27A8D0`(건설 가능 최종 판정, functions.md)을 통과한 시설을 목록에 담는다. 이름은 「건설가능시설목록추가」 | 코드(`27A8D0` 인수 모양 확인; 칸 지형 비트(`+0x1C`)로 거르는 첫 분기는 미판독) |
| CGetFacilityCandidateHexListNode | `3A200` | 7개(`+0x38`~`+0x50`): 거점, 무장, 시설 종류, 출력 HEX 목록(종류 7), 변수 2개, 수치 1개 | 시설을 지을 칸 후보 목록 조회(8KB; 판단표 N3387: 무장 `검사중인무장`, 시설 종류 4). 인수 실제: `[0]` 대상 **지역**(중심 칸 `+0x3A` 사용), `[1]` 무장, `[2]` 시설 종류 n(`BB500` → 정의, 정의 `+0x2C` 계열 1/2/3), `[3]` 출력 칸 목록, `[4]`·`[5]` 거점 목록 변수, `[6]` 수치(0이면 아래 A 갈래 허용). **골격(2026-11-25 3차)**: (A) 대상 지역이 무장 소속 거점(`+0xE2`)의 진입 지역(도시 `+0xB0`)이 아니고 `[6]`==0이면, 대상 지역(소속 거점 지역 `22B880`이면 인접 지역 `230AF0`까지)의 칸(`233850`)에서 이미 있는 건축물의 정의 계열을 세고, 정의 계열 3이면 반경(`2A9C90`) 안 같은 계열 시설이 없는 건설 가능(`27A8D0`) 칸을, 계열 2이고 `2345D0(정의,1)`이면 반경 1로 같은 일을 해 담는다. (B) 그 밖: 기점 = 소속 거점의 진입 지역이 대상이면 위협 거점(도시 `+0xA8`), 아니면 소속 거점 100칸 안(`2ACB80` < 0x65) 적대(`2CC630`) 도시 중 병력 `+0x3C` 최대, 또는 `[4]` 후보 중 대상 지역 중심에 가장 가까운 거점. 대상 지역 칸 중 칸 `+0x10`이 2·0xE이고 `27A8D0` 통과한 칸을 모은 뒤 기점에서 대상 지역으로 `185710` 경로를 내어 고른다. 토석벽 칸 `7CB80`과 같은 기점 규칙. **B 갈래 경로 이후 [Sonnet 판독 2026-11-25·미검증]**: `[6]`은 수치이자 **경로 방향 플래그**다(0이면 시작 = `22F190(기점 거점)`·목표 = 지역 중심 칸, 0이 아니면 반대; 호출 `185710(&경로, &결과정보, 시작, &목표, 1, 1, 2)`). 경로 실패(0)이면 결과 2, 아니면 후보가 0개여도 1. ① 후보 수집(경로 전, `233850` 칸 순회 순): 칸 `+0x10`이 2 또는 0xE(제한 플래그 켜졌을 때만)이고 `27A8D0`(건설 가능)≠0인 칸을 후보 C에 추가. ② 진입 칸 E = 경로를 **앞(첫 칸)부터** 훑어 칸 `+0x12`(소속 지역)가 대상 지역 번호(`22F470`)와 처음 같아지는 칸(없으면 없음). ③ 정렬(안정 삽입 정렬, 마지막이 최우선): (a) 정의 `+0x2C`==3이면 `23BE0` — 지형 비용(`2304F0` → `world+0x73860` → `BF1B0`) 오름차순(`<`, 칸 종류 2 우선 처리는 엄밀하지 않아 추정), (b) E가 유효하면 `23EF0` — `2ACB80(후보, E)` 거리 오름차순(`<`, 동점은 앞선 것 유지). 동점은 (a) → 수집 순서. ④ 재필터: 후보마다 `27A8D0`을 한 번 더 불러 0이면 제거(숨은 인수는 추정). ⑤ 출력: C를 앞에서 뒤로 돌며 **지역 중심 칸(`22B8E0(h)+0x3A == h`)은 제외**하고 출력 목록에 추가. 난수 없음 | 코드(골격·경로 이후 고르기) / 추정(`23BE0` 종류 2 우선, 재필터 검사 내용) |
| CGetPersonFormationParamNode | `7F5E0` | 4개: 무장, 평가 종류(판단표 값 3), 출력 진형 객체, 출력 점수 | 무장이 쓸 수 있는 진형(`233CF0`) 20종마다 `C00E0(무장, 진형, 평가 종류)` 점수를 구해 최고 점수 진형과 그 점수를 내놓는다 | 코드 |
| CGetFormationNode | `7EEE0` | 2개: 진형 번호(상수), 출력 객체 | 진형 표(`world+0x77430`부터)에서 번호의 진형 객체를 꺼낸다(`BE040`; 6번은 없음) | 코드 |
| CSelectPersonTacticsNode | `85BE0` | 3개: 무장, 진형, 출력 전법 목록(종류 0xD) | 전법 최대 3개를 골라 담는다: 전법 표(200종)에서 `235090` 참·무장 보유(`93770`)·진형 허용 비트(`+0x6C`)를 만족하는 것을 먼저, 부족하면 무장의 전법 칸 10개(`22BD60`)에서 진형 허용인 것을 채운다. 출진 명령 전법 3칸(`D3C70`, functions.md D04)의 입력 | 코드 |
| CGetBuildingDestructionDataNode | `370D0` | 2개: 출력 무장 목록(종류 4), 출력 지역 목록(종류 6) | 판단 주체 군단의 건물 파괴 계략용 자료 생성: 실행 무장 후보 `6DD230`과 대상 지역 후보 `6E08E0` | 코드(두 보조 함수 본문은 미판독) |
| CCommandExecutionBuildingDestructionNode | `52EC0` | 3개: 군단, 지역, 무장 | 계략 명령 종류 `0x14`(건물 파괴, rules_diplomacy.md 5.4)의 명령 구조체를 채워 `1FA5C0`으로 실행. 금 상한 `1E0110` | 코드(명령 번호는 상수 `0x14` 직접 확인) |
| CCommandExecutionDualDestructionNode | `53270` | 4개: 군단 등 객체 4개 | 명령 종류 `10`의 구조체를 채워 `1FA5C0` 실행. 조건 79 `이호경식명령가능`이 이 노드의 하위(conditions.md)이므로 이호경식 실행 노드로 읽힌다. **실행 무장의 군단**(`40C20`: 무장 `+0xE0` → `world+0xE0D0`) `+0x14`(명령서)가 임계값(`DAT_141A4B740`) 이상일 때만 실행(거점 `+0x14`가 아님). 인수 4개(`+0x38` 유효성만, `+0x3C` 실행 무장, `+0x40` 대상 A, `+0x44` 대상 B) 전부 유효해야 한다. 구조체 {종류 10, 실행 무장, 대상 A, 비용 `1E0110`, 대상 B} → `1FA5C0(S, 0)`이 명령 객체(0x80B)를 만들어 명령 관리자에 등록하고 `1F8AE0`이 채우며 무장 `+0x15E |= 1`, 군단 `+0x14 = clamp(명령서 − 종류별 비용, 0, 200)`, 군단 자금 감소를 쓴다. 비용 `1E0110` = 군단 자금 F × 40/100 (종류 10)을 `1E2EF0` 상한과 비교한 최솟값, [0,F] 클램프. 반환 1 = `1FA5C0`까지 감(안에서 등록 실패해도 1), 2 = 인수 무효 또는 명령서 부족. 효과(적 사이 이간)는 완료 시점 처리로 추정. 난수·정렬 없음(직접 호출 기준) [Sonnet 판독 2026-11-25·미검증] | 코드(종류 10·노드 본문) / 가설(이름 = 이호경식, 효과 시점) |
| CCommandExecutionAttackRequestNode | `52CA0` | 5개: 군단, 거점, 선택값(0/1/2), 무장, 값 | 외교 명령 종류 `9`(공격 요청, rules_diplomacy.md 3.5)의 구조체를 채운다. 군단(`230270`) `+0x14`가 임계값(`DAT_141A4B668`) 미만이면 실패. 선택값 0/1/2에 따라 `[4]`가 수치(+0x68 또는 +0x64)나 객체(+0x70)로 쓰인다 | 코드(종류 9); 선택값별 구조체 칸 의미는 미판독 |
| CAttackRequestSuccessConditionNode | `7AC40` | 7개(`+0x38`~`+0x50`) | **플레이어 세력에 보내는 동맹 공격 요청의 대가 지불 가능 검사**(2026-11-25 3차, 판단표 N3113 → N3114 `동맹공격요청명령`). 인수: `[0]` 요청 받는 세력(= 플레이어 세력이어야 함, 아니면 2; N3078 `플레이어세력조회`로 채움), `[1]` 사자 무장, `[2]` 대가 종류(0 금, 1 군량, 2 명품; N3108 `외교우선조건선택`), `[3]` 출력(대가 양 또는 명품 객체; N3113 `보조값0349`), `[4]` 목표 거점(N3113 `보조값0562` 객체종류 5, `9DB10` 마지막 인수; 4차 정정 — 3차는 [3]·[4]를 거꾸로 적음), `[5]`·`[6]` 금·군량 남길 양(군주 소재 거점 정보 39·38; 0 이하이면 보유량에 더해 해석). `9DB10(요청 세력, …)`이 요구량을 내고 종류 0·1이면 `230350(요청 세력)` 객체의 금(vcall `+0x90`)·군량(`+0xA0`) − 요구량 > 남길 양일 때 성공하며 요구량을 출력, 종류 2는 명품 표(`world+0x77B18`[202])의 항목을 출력 | 코드 |
| CCommandTransportDepatureNode | `32D90` | 5개: 출발 거점 목록, 도착 후보 거점 목록, 값 3개(판단표 `수송출진명령`) | 수송 출진 명령 작성(10KB). 3차(2026-11-25) 판독: 도착 후보를 `25BF0` 뒤 `25CE0`(군량 20000 미만 우선)로 정렬, 공급 거점을 거리(`216E0`/`25B10`)로 고름 — ai/roles.md 2-3-6 | 코드(ai/roles.md 2-3-6) |
| CGetTransportSoldierNode | `804F0` | 4개: 거점 목록, 상수 3개(판단표 24, 6, 6) | 목록의 각 거점마다 `9F410`(필요량)을 계산해 거점 `+0x90`에 부호 있는 수송 병력 값을 저장(`D3A90`) | 코드(저장 위치); 부호 의미는 미판독 |
| CGetAllFootholdNeedFoodNode | `7B450` | 4개: 군단, 상수 3개(24, 6, 6) | 군단 소속 세력의 거점 전부에 `9F410(거점, …)`으로 필요 군량을 계산해 거점 `+0x94`에 쓴다(정보 조회 Foothold 항목 38이 이 값을 읽는다: `8B190` case 0x26) | 코드 |
| CCGetAllFootholdNeedMoneyNode | `7B590` | 2개: 군단, 상수(6 또는 4) | 같은 방식으로 필요 금(`9F670`)을 거점 `+0x98`에 쓴다(항목 39) | 코드 |
| CGetMyselfTroopsNode | `6E760` | 1개: 출력 | 판단 주체(군세 트리)의 군세 객체를 변수에 넣는다(`B72F0`) | 코드 |
| CGetMyselfTroopsInfoNode | `6D310` | 2개: 항목 번호, 출력 | 판단 주체 군세의 정보 조회(getter, 5KB). 항목 0 군세 번호, 1 종류(`+0x14`), 2·3 소속 부대 목록, 4 목표 객체(종류 `+0x14`별로 거점·지역·시설·경계군세 표를 골라 `+0x16`으로 변환), 6 객체 번호(`+8`), 7 소속 군단, 10 병사 합(부대 `+0x16`), 13 전력 합(`B6F50`), 14 경유 HEX 목록(`+0x18` u16[10]), 15 소유 세력(`22E560`) | 코드(전 항목, 2026-11-25 3차): 대장 = 소속 부대 중 능력 0(`231770(무장,0,0xFFF)`) 최고 부대의 대장(`58D90`). 5 = 병사 합 S(부대 `+0x16`) + S × `DAT_141A4AFD8` × 대장 적성 `+0x16A` / 10000(세력정보 4와 같은 상수), 8 = 금 합(부대 `+0x5C`), 9 = 군량 합(부대 `+0x60`), 11 = 군량 합 F − F × 대장 적성 `+0x170` × `DAT_141A4AFFC` / 10000, 12 = F − F × 대장 적성 `+0x172` × `DAT_141A4B008` / 10000(상수 `141A4AFD8`·`AFFC`·`B008` = EXE 초기값 150, 직접 쓰기 xref 없음; 4차) |
| CVariableGetCautionArmyInfoNode | `88140` | 3개: 경계부대 항목, 항목 번호(상수), 출력 | 경계부대(`CCautionArmy`; 표 `world+0x81B50` 간격 0x18) 정보: 0 항목 번호(`22F4F0`), 1 그 부대 전력(`B6F50`), 2 관련 거점(`+0x12`, `32E3B0`), 3 적 부대(`+0x10` 번호 -> 부대 표), 4 `+8` 정수 | 코드 |
| CCautionArmyAddUniqueNode | `283F0` | 3개: 적 부대, 거점, 출력 경계부대 목록(종류 0xF) | 적 부대가 목록에 이미 있으면 성공만 하고, 없으면 빈 경계부대 칸(`world+0x81B50` 표)에 (부대 번호 `+0x10`, 거점 번호 `+0x12`, 상한 0x3D)을 채워 목록에 넣는다. 부대가 자기 거점 칸 위이면 실패, 거점 소유 세력이 판단 주체와 다르면 `26D660`(외교 관계)을 통과해야 한다 | 코드 |
| CCautionTroopsListAddNode | `28D20` | 4개: 경계군세 목록(종류 0xB), 부대 목록, 대상 거점, 값 | 새 경계군세를 만든다: 빈 칸(`world+0x80BA8` 표, 간격 0x48)을 잡아 부대 목록을 복사하고 대상 거점(`+0x1A`, 상한 0x3D), 번호(`+0x18` = 목록 안 안 쓴 최소 번호), 소속 군단(`+0x14` = 판단 주체 군단 번호)을 쓴다. 부대가 이미 다른 경계군세에 있으면 실패(2) | 코드 |
| CCautionTroopsListAddUniqueNode | `29190` | 3개: 경계군세 목록, 순번(수치), 부대 | 목록의 순번째 경계군세의 소속 부대 목록(`+0x30`)에 부대를 중복 없이 추가 | 코드 |
| CCautionTroopsRemoveNode | `29990` | 2개: 경계군세, 부대 | 경계군세의 소속 부대 목록(`+0x30`)에 부대가 있으면 `+0x28` 쪽 목록에서 제거 | 코드(두 목록의 관계 미확인) |
| CCautionTroopsListRemoveNullUnit | `29390` | 1개: 경계군세 목록 | 각 경계군세의 소속 부대 가운데 유효하고 명령(`+0x37`)이 `0xB`·`0xC`(퇴각)가 아닌 부대만 남기고, 부대가 하나도 안 남은 경계군세는 `32D180`(삭제)로 지운다 | 코드 |
| CCautionTroopsClearNode | `28CC0` | 1개: 경계군세 | 경계군세를 삭제(`32D180`, functions.md T01) | 코드 |
| CCautionTroopsSortNode | `29A90` | 1개: 경계군세 목록 | 각 경계군세의 적 부대 목록(`+0x28`)을 헬퍼 7개로 연속 정렬(반환 1, 인수 읽기 실패 시 2, 난수 없음). 키: ① 대장 무장 번호 ② 무장 `+0xEA` ③ 능력 1 ④ 능력 0 ⑤ 대장 `+0xE7`로 고른 `world+0x784F8` 표 항목 비교(`259D0`) ⑥ 대장 소속 군단(`22D3C0`) ⑦ 부대 세력의 군주 번호(`230400(22E2A0)`) — ai/roles.md 2-3-4. **방향·안정성**: ① `22D30`/`22DB0`은 오름차순·안정 삽입 정렬이고 마지막에 건 정렬이 최우선 키다 — 확정(코드, 지휘 세션 대조 2026-11-25). ②③④ 오름차순, ⑤ **내림차순**(`259D0(a,b) = key(b) < key(a)`), 모두 안정 삽입 정렬 [Sonnet 판독 2026-11-25·미검증]. ⑥⑦은 정렬이 아니라 **조건 분할 이동**(⑥ 대장 소속 군단의 `+0x12` == 부대 `+0x12`, 즉 군단장이 대장인 부대를 목록 앞으로 / ⑦ 대장이 군주 번호와 같은 부대를 앞으로)이며, 만족 원소끼리의 순서는 뒤집힐 수 있다(추정). 합성 순서: 앞 = 군주가 대장인 부대(⑦) → 군단장이 대장인 부대(⑥) → ⑤ 값 내림차순 → ④ 능력 0 오름 → ③ 능력 1 오름 → ② `+0xEA` 오름 → ① 무장 번호 오름 | 코드(① 확정, ②~⑤ 키·방향·안정성) / 추정(⑥⑦ 만족 원소 간 순서, ⑤ 키의 뜻) |
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
| CGetSpecifedStrategyDistrictTroopsNode | `3DDB0` | 2개: 군세 종류(**정수 직접값**, 판단표 17), 출력 군세 목록(`world+0x7F8D8` 슬롯 501개를 주소 오름차순으로 훑어 판단 군단 소속이고 `+0x14`==종류인 군세를 추가, 정렬·중복 제거 없음, 비어도 1, 군단 무효·목록 확보 실패 2 [Codex 판독 2026-11-25·미검증])(종류 2) | 판단 주체 군단의 군세 중 종류(`+0x14`)가 인수와 같은 군세 목록. 이름의 「Strategy」는 종류 코드(rulebase.md 4절 표)를 뜻하는 것으로 보인다 | 코드(이름 풀이는 가설) |
| CRemoveNoInterceptPersonNode | `85810` | 1개: 무장 목록 | 요격 무장 후보 목록에서 거른다. **제거** 조건: 통솔(능력 0, `231770(…,0,0xFFF)`) < 21이거나, 진형 번호 i=1..19 중 `233CF0` 참이고 진형 유효·`+0x7E`==1·비트1 꺼짐·번호 ≠ 7인 것이 하나도 없는 무장. 이런 무장을 임시 목록에 모은 뒤 원목록에서 `21A350`(같은 포인터 모두)으로 지운다(남은 원소 순서 유지, 정렬·난수·쓰기 없음). 옛 서술 「남기는 조건: 5능력 최대 < 21 …」은 방향과 능력 종류를 잘못 읽었다 | 확정(코드, 지휘 세션 대조 2026-11-25; Codex c7) / 가설(「요격 부적합」이라는 의미 해석) |
| CGetAdvantageOwnFootholdNode | `7B1B0` | 2개: 거점, 출력 수치 | 거점이 속한 주(`도시 +0xCE`)의 지방 이점 객체(`world+0xDC80`)의 이점 대상 거점 목록(`2AED70`) 가운데 소유 세력 번호(vcall `+0xB0`)가 판단 주체 세력 번호와 같은 거점의 개수를 낸다(이름의 「조회」는 수 반환). 판단 주체는 `B7100`·`B72F0`·`B7170`·`B7210` 모두에서 세력으로 환산 | 코드 |
| CExecuteAutoPaintDefenseNode | `69240` | 0개(판단 주체 = 군세) | 군세 종류 `0x17`(영역 방어)일 때: 목표 지역의 소유 세력이 군세 소유 세력과 같으면 종류를 0(임무 없음)으로 해제한다. 다르면 하드코딩된 지역 번호 표(`0xC2`, `0xEA`, `2`, `0xF6`, `0x1B`, `0xD1`, `0x2F`, `0x23`, `0x5D`, `8`…마다 거점·지역 번호 3개 조합)로 `70FB0`(군단의 종류 8~0xB·0x16 군세가 그 목표를 이미 노리는지 검사)을 두 번 확인해 둘 다 0이면 종류를 0으로 해제한다 | 코드(구조); 지역 표의 뜻과 `70FB0` 본문은 미판독 |
| CTroopsOrderDesutructionFacilityNode | `6F5F0` | 0개(판단 주체 = 군세) | **군세 종류 7에서 호출되어 종류 4(시설 공격)로 바꾸는** 노드(판단표 N254 → N256; 진입 시 종류 4 검사는 없다): 구성 부대 목록 비면·대표 부대 진형 7·병력 ≤ 999이면 2, 대표 무장 거점까지 `185710` 경로가 지나는 지역 중심 칸 중 군세 세력 소유 지역의 시설(종류 ≠ 1·2, 소유·칸 소유가 군세 세력과 다르고 `2CC630` 적대, 정의 `+0x2C` ∉ {1,3,4})을 고르되 시설 반경 5칸에 적대 부대가 하나라도 있으면 탈락하고, **적합 시설을 찾아도 바깥 지역 순회는 계속해 뒤 지역의 적합 시설이 선택을 덮어쓴다**(내구·거리·공격력 비교 없음, 시설 번호 0·범위 밖 칸을 만나면 선택이 있는 상태에서는 그 지역 칸 루프 중단). 쓰기: 군세 `+0x14=4`, `+0x16=시설 번호`, 구성 부대마다 `2ECEA0(부대,6)`·`2ECF00(부대,11,시설 번호)`(`+0x140==0`일 때만), 경유점·`26E260`·내구 직접 감소 없음 [Codex 판독 2026-11-25·미검증]. 이전 서술: `185710`(길찾기)·`2ECEA0`(행동 쓰기)을 부른다. functions.md 3.5·3.6절의 쓰기 지점(`6F5F0` -> 종류 4)과 일치 | 코드(호출 목록) / 가설(경로 선정 식 미판독) |
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
| CSpyHomeOfficerSetNode | `3EBC0` | 0/18/0/0 | 인수 `[0]` 첩보 **대상 세력 T**, `[1]` 무장 P, `[2]` 슬롯(1부터). 조기 1: T 자체의 슬롯 값이 이미 T 번호·P 번호(코드는 F가 아니라 T의 슬롯을 읽음). 일반: 슬롯 < 3, 0 < T 번호 < 52, 1 ≤ P 번호 ≤ 6000, 군단 명령서 ≥ B440, F·T·P 유효. 쓰기: P의 기존 첩보 슬롯 해제(`22B1E0`), P가 도시 모병/훈련 담당이면 **현재 소재 거점**의 `+0xCA/+0xCC`=0, 지역 담당 전부 해제(`29DE10(P,0,0)`, 방침 유지), 슬롯에 T 번호(0..51)·P 번호(0..6000) 기록, 명령서 `−B21C`. 이미 같은 배치여도 T 기준 조기 비교를 통과하지 못하면 비용을 낼 수 있다 [Codex 판독 2026-11-25·미검증] | 코드 |
| CListRemoveForceNode | `84BC0` | 0/18/0/0 | 목록에서 세력 제거(실행 `84BC0` 공용) (같은 값 모든 항목 제거, 항상 1) [Sonnet 판독 2026-11-25·미검증] | 문서 참조/쓰임 |
| CCallScriptNode | `5D760` | 3/12/0/0 | `0000/param_s.bin` 수식표(`C11E0`이 읽음)의 n번 수식 계산. 판단표 밖 스크립트가 아니라 수식 호출(ai/formulas.md·ai/data_locations.md; 2026-11-25 4차) | 코드 |
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
| CGetTargetForcePrisonerListNode | `801D0` | 0/6/0/0 | A 관련 포로 후보를 목록 `[2]`의 **꼬리**에 추가(정렬·상한·중복 검사 없음, 목록 없으면 생성, 비어도 1). 후보 = 신분 `+0xE6`==6, 소속 거점(`+0xE2`)의 소유 세력 == B, `22E870`==A 또는 `+0x165`==A, 소재 종류가 5 도시·6 관문·0x1B 부대(종류 10 이동 형식 제외). 무장 목록 iterator의 vtable 슬롯 미확정(추정 `335540`) [Codex 판독 2026-11-25·미검증] | 코드 |
| CCommandExecutionMerchantNode | `2E410` | 0/6/0/0 | 군량 매매(상인). 인수 `[1]` **정수 직접값**(0/비0), `[2]` 금 과부족, `[3]` 군량 과부족, `[4]` 후보 무장 목록. **노드 `[1]`==0이 실제 명령 방향 1(매입), 비0이 방향 0(매각)** — 리터럴과 방향이 반대다. 게이트 `70FF80`(도시 번호<52, 군단 명령서 ≥ `B44C`, 도시 `+0xC9` bit0=1·bit2=0, 거래 가능, 가능 무장 있음). 후보는 목록 순서대로 가능 무장(`6DA1B0`)만 채택해 지력+정치 실효 능력 합 `A(p)`를 누적하며 거래량 `26A450`/`26A6A0` 상한(10명 상한, 같은 거래량이면 마지막 1명 제거)을 채우고 `1F2370`으로 실행: 무장 `+0x15E|=1`, 공적 `16A4E0(p, A/S×량×…)`, 금·군량 이동(방향 0: 금 `+량×10/r`·군량 `−량`, 방향 1: 금 `−(b+(량−1)×10)/b`·군량 `+량`), 명령서 `−B44C`, 도시 `+0xC9 |= 4`. 실행이 실패해도 노드는 1. 일부 나눗셈에 0 보호 없음. 난수 없음 [Codex 판독 2026-11-25·미검증] | 코드 |
| CGetExchangeConditionsNode | `7E930` | 0/6/0/0 | **포로 교환 조건이 아니라 자원 가치 변환기**: `[0]` 직접값 0이면 `x>0 ? B3B4×x/10 : 0`, 1이면 `x>0 ? x×10/B3B4 : 0`을 `[2]`에(B3B4=50이면 ×5, ÷5) [Codex 판독 2026-11-25·미검증] | 코드 |
| CRecruitOfficerRemoveNode | `3E6B0` | 0/6/0/0 | 인수 `[0]` 거점만 읽음(판단표의 둘째 인수는 미사용). 거점 `+0xCA`==0이면 1, 거점 군단 명령서 < `DAT_141A4B434`이면 2, 아니면 `1F34F0({거점, ID 0})`을 불러 반환을 무시하고 1. `1F34F0`: 명령서 `−B434`(0..200)를 치르고 **0번 무장**을 기준으로 거점 `+0xCA/+0xCC`가 그 무장이면 0, 첩보 담당·지역 담당 해제, 마지막 `+0xCA=0` — 기존 담당 무장을 넘겨 해제하는 함수가 아니다 [Codex 판독 2026-11-25·미검증] | 코드 |
| CRecruitOfficerSetNode | `3E750` | 0/6/0/0 | 인수 `[0]` 거점, `[1]` 무장. `거점 +0xCA == 무장 +0x10`이면 1(비용·유효 검사 없음), 아니면 **무장 소속 군단** 명령서 < `DAT_141A4B434`이면 2, 둘 다 유효하면 `1F34F0({거점, 무장})`(반환 0이면 2; 명령서는 **거점의 군단**에서 차감, 노드 사전 검사 군단과 다를 수 있음): 새 무장이 거점 `+0xCA/+0xCC`에 있으면 먼저 0, 첩보 슬롯(`279890`)·지역 담당(`29DE10(무장,1)`) 해제, `+0xCA = clamp(ID,0,6000)`. 모병 담당 배치이며 등용(Employ)이 아니다 [Codex 판독 2026-11-25·미검증] | 코드 |
| CTrainingOfficerSetNode | `3EF50` | 0/6/0/0 | `3E750`과 같은 구조이되 사전 검사 군단이 **거점 군단**(명령서 < `DAT_141A4B440`이면 2)이고 `201A80({거점, 무장})`으로 `+0xCC = clamp(ID,0,6000)`. 무장 능력·훈련 효율 평가는 노드에 없다 [Codex 판독 2026-11-25·미검증] | 코드 |
| CSceneryInvestSetNode | `3E890` | 0/3/0/0 | 명승 투자 시작: 판단 군단 무효 2. 명승 `+0x5F` bit0, `+0x64`==1, `+0x6C`가 1..5, `+0x66`==0, `+0x68`<1, 소유 세력·지역·도시 유효, 도시 군단 번호 == 판단 군단, 비용 C=`22C5F0` ≤ 도시 금이고 군단 명령서 ≠ 0이어야 한다. 통과 후 `+0x64=2`, 기간 d=`22C810`, 오늘 t, `+0x66`·`+0x68` 기록, 도시 금 `−C`(0..상한), 명령서 `−1`. `+0x66` 저장은 디컴파일이 `d≥1이면 0, d<1이면 (s16)(t+d)`로 읽혀 의도(`max(0,d)`)와 달라 원작 재현 미확정(디컴파일 아티팩트일 수 있음), `+0x68 = max(0,t+d)`. 비용 `22C5F0`·기간 `22C810` 식은 functions.md 기록과 일치 [Codex 판독 2026-11-25·미검증] | 코드 |
| CGetCanServePersonListNode | `7C300` | 0/3/0/0 | **군단 판단표 3회**. 등용 **대상** 후보 목록 `[1]`을 만든다: 전역 무장 연결목록 순서로 `1F0A30(P, 군단)`: `233BE0`이 아니고, 신분 ≠ 1, 소속 군단 번호가 46..51이 아니며, `234AB0==0`·`+0x15E` bit 0x4000 없음, 그리고 소속 세력이 군단 세력에 적대(신분 1..4) / 신분 5(재야)면 현재 칸 지역 소유가 우리 세력 / 신분 6(포로)면 `+0xE4` 거점의 소유가 우리 세력인 무장을 추가. 마지막으로 **같은 세력이 이미 내린 등용 명령**(명령 관리자 목록, 종류 2, 첫 대상이 무장)의 대상을 `21A350`으로 목록에서 전부 제거. 정렬 없음 [Codex 판독 2026-11-25·미검증] | 코드 |
| CCommandExecutionEmployNode | `2D720` | 0/3/0/0 | **군단 판단표 3회**(세력 아님). 인수 `[0]` 실행 무장 E, `[1]` 등용 대상 T, 둘 다 유효해야 하고 `1EECC0`({T,E,mode 0})을 불러 **결과와 무관하게 1**. 등록 `1F71B0`: E `+0x15E |= 1`, 소재를 이동 형식으로, 군사 조언 `2F5AA0`, 도착일 `232F70`/`2331F0`, 출발 거점 군단 명령서 `−6D5A50()`(0..200)을 쓰며 판정은 `279DE0(T,E,&roll)`(인수 순서 T,E)이다. 난수: `2F5AA0`의 `3FDAF0(100,10,E,T,0,0)` 1회(군사 유효 시) + `279DE0`의 `3FDAF0(100,1,E,T,0,0)` 1회(조기 종료 아니면). 지연 실행 `1DBD80`·소속 변경 `273100`의 vtable 연결은 추정 [Codex 판독 2026-11-25·미검증] | 코드 |
| CCommandExecutionHireNode | `2DAB0` | 0/3/0/0 | 인수 `[0]` 거점, `[1]` 템플릿 무장 목록. 군단 명령서 `−DAT_141A4BC0C`가 음수이거나 인원 문턱(`uint64(N + (200−R) − C) ≤ 200−Q` 꼴, signed로 바꾸면 안 됨)·금(`보유 − N×DAT_141A4BC00` < 0)에 걸리면 2. 목록을 연결 순서로 `331310`: 무장 ID 4201..4400(0x1069..0x1130) 중 **최초 빈 슬롯**을 골라 템플릿을 복제(`31DEE0`)·소속 편입(`29FB50`: 신분 4, 충성 `26A270`, `+0xE7=0x49`)·템플릿 `227D30`으로 초기화. 중간 실패 시 앞서 만든 무장은 되돌리지 않고 명령서·금 차감만 생략. 목록 비어도 명령서 차감. 난수 직접 호출 없음(가상 `+0x40` 2회 내부 미확정) [Codex 판독 2026-11-25·미검증] | 코드 |
| CListAddPersonUniqueNode | `82720` | 0/6/0/0 | 목록에 무장 추가(중복 제외) (꼬리 추가·중복이면 추가 없이 1) [Sonnet 판독 2026-11-25·미검증] | 이름 |
| CDomesticPriorityDevelopmentSelectNode | `7B0B0` | 0/6/0/0 | 인수 `[0]` 지역, `[1]` 결과 키(선택 항목 1 상업·2 농업·3 병영 추정, 0 = 선택 없음), `[2..4]` 즉치 가중치(판단표 25·50·75). 군단(`B7170`; 무효면 지역 거점의 군단)의 `B2AF0`: ① 군단 `+0x1A`가 3이고 지역 `+0x3C`≠1000이면 1, 2이고 `+0x3E`≠1000이면 2, 4이고 `+0x40`≠1000이면 3을 우선 선택하며 그 값이 지역 현재 방침 `+0x72`와 같으면 0으로 바꾸고 끝낸다(담당관 검사 없음). ② 아니면 군주 무장 `+0x170/+0x172/+0x174`(a1..a3), 개발값 `+0x3C/+0x3E/+0x40`을 4문턱(`13A9DDC`, 기존 기록 {100,300,600,1000})으로 단계 L1..L3(1..5)로 바꿔 `Si = Li×(ai+100)×wi/100`(개발값 ≥ 1000이면 50000)의 **최솟값** 항목을 고르고(전부 50000이면 0, 동점은 1→2→3), 선택이 `+0x72`와 같으면 담당관(`+0x36`)이 유효할 때 0, 무효이면 같은 항목을 다시 낸다. 난수·목록 없음 [Codex 판독 2026-11-25·미검증] | 코드 |
| CDomesticOfficerSetNode | `36E80` | 0/6/0/0 | 인수 `[0]` 지역, `[1]` 무장, `[2]` 개발 방침(정수 키, 값 0이면 변경 건너뛰고 1). 이미 같은 담당·방침이면 1. 무장 소속 군단 명령서 `+0x14` < `DAT_141A4B428`이면 2. 그 뒤 `25330`으로 지역·무장·방침 병렬 목록 명령을 만들어 `1EE630`을 실행(결과와 무관하게 1): 무장의 기존 담당 지역(`+0x1D0`)을 해제 항목으로 먼저 넣고 새 지역을 추가한다. 쓰기 3단계: (A) 대상 무장의 거점 모병·훈련 담당(`+0xCA/+0xCC`)과 첩보 슬롯을 0으로, 같은 무장의 다른 지역 담당(`2ABF60(무장,2)==0`일 때 첫 지역) 해제, (B) 명령 대상 지역 전부 담당 0·방침 0, (C) 목록 순서대로 새 담당(0..6000)·방침(0..3) 기록. 명령서 `+0x14 = clamp(기존 − k×B428, 0, 200)`(k = 바뀐 지역 수, 노드 사전 검사 군단과 다를 수 있음). 난수 없음 [Codex 판독 2026-11-25·미검증] | 코드 |
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
| CSetBehaviortreeRestartFlagNode | `85EC0` | 0/0/3/0 | 판단표 재시작 표식(군세 `+0x38`, structs 3.12) | 문서 참조/쓰임 |
| CGoodwillSuccessConditionNode | `80730` | 0/2/0/0 | 친선 제안 자원 검사: `9F180`이 요구 가치 `324F20`(우호도·혐오·관계 감면·정치 보정·개성을 포함하는 고정 절삭 식, 상세 rules_diplomacy.md 3.7절)과 제공 가능 가치를 비교하고 `보유 − 양 > 보존량`일 때 `[3]`에 금·군량 양 또는 명품. 수락 난수 없음 [Codex 판독 2026-11-25·미검증] | 코드 |
| CCommandExecutionGoodwillNode | `53930` | 0/2/0/0 | 제안 종류 4(친선) 제출: k=0/1이면 `보유 − 양 > rg/rf`(입력 정수 그대로, `80730`과 달리 보유량으로 치환하지 않음)일 때만, 아니면 2. 제출 실패해도 1. 우호도 증가는 도착 후 [Codex 판독 2026-11-25·미검증] | 코드 |
| CGetHiddenPoisonDataNode | `3C1F0` | 0/2/0/0 | 계략(HiddenPoison, 이름 직역 「숨은 독」) 실행 자료 조회 — 실행 무장 후보는 `6DD230` 공유(ai/conditions.md 조건 80) | 문서 참조/쓰임 |
| CCCommandExecutionHiddenPoisonNode | `54110` | 0/2/0/0 | **매복·지독(계략 14)** 등록: 인수 F(유효성만)·무장 A·지역 Z, A 군단 명령서 ≥ `B718`이면 군정 30% 상한으로 `1FA5C0`, 등록 실패도 1. 효과(치안·개발 감소)는 후일 `1FC530`. 상세 rules_diplomacy.md 5.5절 [Codex 판독 2026-11-25·미검증] | 코드 |
| CGetEstrangeDataNode | `3A0C0` | 0/2/0/0 | 이간 실행 자료 조회(`6DD230` 공유) | 문서 참조/쓰임 |
| CCCommandExecutionEstrangeNode | `533F0` | 0/2/0/0 | **이간 = 계략 12** 등록(종류 10 아님): A 군단 명령서 ≥ `B720`, 군정 70% 상한. 효과(목표 충성 하위 8비트 감소)는 후일 `1FF7B0`. rules_diplomacy.md 5.5절 [Codex 판독 2026-11-25·미검증] | 코드 |
| CGetPlacationDataNode | `3DB90` | 0/2/0/0 | 계략(Placation, 이름 직역 「회유」) 실행 자료 조회(`6DD230` 공유) | 문서 참조/쓰임 |
| CCCommandExecutionPlacationNode | `545D0` | 0/2/0/0 | **회유 = 계략 13** 등록: A 군단 명령서 ≥ `B72C`, 군정 50% 상한. 성공률 `1E1A60`(14용 `1E1370`과 구분), 효과(칸 소유 변경)는 후일 `1FD930`. rules_diplomacy.md 5.5절 [Codex 판독 2026-11-25·미검증] | 코드 |
| CCommandExecutionRumorNode | `2F080` | 0/2/0/0 | 유언(소문) 계략 실행(`6DD230` 공유) | 문서 참조/쓰임 |
| CGetUnattendedhomeDataNode | `3E400` | 0/2/0/0 | 계략(UnattendedHome, 이름 직역 「빈집」) 실행 자료 조회(`6DD230` 공유) | 문서 참조/쓰임 |
| CCommandExecutionUnattendedHomeNode | `54F50` | 0/2/0/0 | **구호탄랑 = 계략 11** 등록: 도시(`C+0x4E<52`)를 `22C1F0`로 정규화한 거점을 대상으로, A 군단 명령서 ≥ `B734`, 군정 80% 상한. 등록은 결과 > 1만 저장. 효과는 후일 `2000F0`. rules_diplomacy.md 5.5절 [Codex 판독 2026-11-25·미검증] | 코드 |
| CGetFireStrategySuccessFireStrategyNode | `7EAC0` | 0/0/0/2 | 화계 성공 확률(부대 판단표; ai/roles.md 7-5) | 문서 참조/쓰임 |
| CCommandExecutionFireStrategyNode | `1F2A0` | 0/0/0/2 | 화계 실행(ai/roles.md 7-5) | 문서 참조/쓰임 |
| CCommandExecutionExpansionNode | `53790` | 1/0/0/0 | 세력 정책 패널 추가 칸: 예산 `22EC90`만큼 반복하며 종류 0..4 중 목표−현재 부족분이 최대인 종류(동점 작은 번호)의 `세력+0x70+0x1E×i`를 `min(7,old+1)`로 쓴다. 비용·난수 없음, 예산→레벨 매핑 미확정 [Codex 판독 2026-11-25·미검증] | 코드 |
| CCommandExecutionPostAutoNode | `54710` | 1/0/0/0 | 관직 자동 배치: 세력 소속 무장 중 `233BE0==0`·신분 ≠ 1·6·`234AB0==0`·`+0x15E` bit14 없음 등을 모아 모두 기본 관직(0x49) 예정으로 만들고, 계급(세력 `+0x47`)이 허용하는 관직(`world+0x784F8..` 순, 번호 ≠ 0x49)마다 보정 4항(`1EF620`)이 가리키는 목록(총합/무관/문관: **기본 u8 능력** 합 + AI 보정 `T((+0x166×C9C8+1)/10)`, 내림차순, 동점 무장 번호 오름차순, 안정)에서 첫 후보를 배정한다. 이미 그 관직을 가진 사람이 있으면 건너뜀. 적용 `1F2B10`은 무장 포인터 오름차순, 충성 변화 `d`는 하위 8비트만 반영(명령서·금 차감 없음). 읽기 실패만 2, 그 밖 항상 1. 난수 없음 [Codex 판독 2026-11-25·미검증] | 코드 |
| CCommandExecutionTradeNode | `54CE0` | 0/3/0/0 | 교역 출발 등록: 본거지 금·군량·병사가 요구량을 **모두 엄격히 초과**할 때만 `1EBC60`(행상 행동 `CCmdActionCaravan`) 호출, 발행 실패도 노드 1. 출발 거점 군단 명령서 `−목록 수×B7A8`, 본거지 자원 차감(0..상한 포화), 무장 소재 이동·`+0x15E|=1`. 난수(날짜 해시) 2회: 조언 `2F5AA0`의 `R(100,10,…)`, `vt+0x130` 뒤 `R(100,10,현재일수,첫 무장 번호,?,?)`로 행동 `+0x81`(r ≤ `B84C`→2, ≤ `B858`→3, ≤ `B864`→4, ≤ `B870`→5, 그 밖 0). 도착 후 처리는 별도 [Codex 판독 2026-11-25·미검증] | 코드 |
| CCommandExecutionPrizeNode | `2EEA0` | 0/3/0/0 | 포상: 지급 거점 `22EDF0(군단)`, 예산 B = min([1], 거점 금)에서 목록 순서대로 `B −= 100`을 먼저 하고 B > 0일 때만 대상에 포함(딱 100이면 0명, 200이면 1명). 실행 `1F3C90`: 유효 무장마다 충성 `min(100, 충성 + min(9, (75−상성)/B558 + 3 + r))`(`r = 3FDAF0(2,1,군주,대상,0,0)`, 충성 > 100이면 100으로 내려갈 수 있음), `+0x15E|=2`, 금 `−100×n`(무효 대상도 n에 포함), 군단 명령서 `−B458` **한 번**. 노드는 실행 성공과 무관하게 1 [Codex 판독 2026-11-25·미검증] | 코드 |
| CCommandExecutionCreditGiveNode | `2D2A0` | 0/3/0/0 | 공적 부여: 게이트 `u64(B8B8×n) ≤ 금`(n = 원래 목록 수, 무효·중복 포함)·`B8D0 ≤ 군단 명령서`(n 곱 아님). 유효 무장만 임시 ID 목록(중복 허용)에 넣고 실행 `1ED620`: 무장마다 `+0x1BE`(s16 공적)에 `B8C4`를 가산(상·하한 포화), `0407E0==1`이고 새 공적 ≥ 기준이면 위계 `+0x1BC=2`, `+0x15E|=0x8000`. 금 `−m×B8B8`(m = 유효 수), 명령서 `−B8D0` 한 번. 난수 없음 [Codex 판독 2026-11-25·미검증] | 코드 |
| CCommandExecutionCreditRankUpNode | `2D440` | 0/3/0/0 | 공적 승급: 게이트 `u64(B894×n) ≤ 금`·`B8A0×n ≤ 명령서`(n = 원래 목록 수). 승급 단계 `040830` = 위계표에서 `+0x2C ≤ 공적`인 최고 단계와 `현재+1`의 최솟값(한 번에 1단계), 보상 니블은 지력·정치와 통솔·무력 합 비교로 high/low 증가(동점 low). 실행은 무장 **번호 오름차순**, 유효 대상 하나라도 `1F0950` 재검사에 실패하면 그 자리에서 0 반환(앞서 쓴 것은 되돌리지 않음), 금·명령서(`B894×m`, `B8A0×m`, m = 고유 유효 수)는 끝에서만 차감. 난수 없음 [Codex 판독 2026-11-25·미검증] | 코드 |
| CDistributeSpyPointNode | `550B0` | 1/0/0/0 | 군단에 첩보 포인트(군단 군정 `+0x24`) 배분(structs 3.10) | 문서 참조/쓰임 |
| CCommandExecutionLearnNode | `54330` | 1/0/0/0 | 전법 습득 실행(세력 판단표; 대상 거름은 조건 78 「전법습득가능」) | 문서 참조/쓰임 |
| CVariableGetFindItemIndexNode | `89FB0` | 0/1/0/0 | 인수 [0] 목록 종류, [1] 찾을 항목 키(종류 0xE는 정수), [2] 목록 변수 키, [3] 결과 키. 연결 목록(머리표 `1427D4140[ID×8]`)을 **앞에서부터** 돌며 8바이트 포인터가 같은 **첫** 항목의 0 기준 순번을 [3]에 쓴다(정수 목록 0xE는 4바이트 비교). 찾지 못함·항목 무효(`331780`)·읽기 실패는 2. 목록 순서가 추가 순서와 같은지 미확인 [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CGetNearCapitalNode | `1FE50` | 0/0/0/1 | 「가까운 수도」가 아니라 **이번 이동 경로 위 지역 중심 칸 보충**: `9CC90(부대, 2)`를 항상 부르고(반환 무시) 결과는 항상 1. 경유점을 `CDE60`이 시뮬레이션한 경로 위 칸 반경 2의 「소유가 다르고 거점 없는 지역 중심 칸」으로 최대 5개 다시 쓴다(상세 functions.md 3.6절 `9CC90`) [Sonnet 판독 2026-11-25·미검증] | 코드 |
| CResolutionFakeNewsNode | `20100` | 0/0/0/1 | 위보 해소(ai/roles.md 7-5 `CF150`) | 문서 참조/쓰임 |
| CGetFakeNewsSuccessProbabilityNode | `7E9E0` | 0/0/0/1 | 위보 성공 확률(ai/roles.md 7-5) | 문서 참조/쓰임 |
| CGetSpecifiedRangeTrapListNode | `80090` | 0/0/0/1 | 범위 안 함정 목록(ai/roles.md 7-5) | 문서 참조/쓰임 |
| CCommandExecutionFakeNewsNode | `1F1D0` | 0/0/0/1 | 위보 실행(ai/roles.md 7-5) | 문서 참조/쓰임 |
| CCommandExecutionDoctrinePanelAutoNode | `52FC0` | 세력 2 | **주의(교리) 판 자동 채택, 반복 노드** — 명령 1회가 아니라 후보를 정렬해 군주 군단 명령서(`+0x14`)가 닳거나 후보가 끝날 때까지 여러 항목을 채택한다(`2EF700(군주군단, 항목, 0)`). 인수 `+0x38`≠0이면 먼저 주의 판 환불·초기화(`337380`·`236F10`; 항목 1 무료 채택), 0이면 현재 상태에서 이어 채택(세력 트리 N167 `(1)` = 월 1·7월 1일, N169 `(0)` = 그 밖의 달 1일). 읽기: 군주 군단 = `230270(세력)`, 명령서 < `DAT_141A4B6B4`(항목 1개 비용)이면 1로 끝. 후보 = 항목 2..79를 id 오름차순으로 `2C6590(군주군단, id, 0)==0`(채택 가능)인 것. 정렬 `50450` = 안정 삽입 정렬, 비교자 `50FB0` 우선순위: ① 제한 플래그(`+0x46`)≠0·칸1(`+0x3D`)≠0·칸1==군주 주의번호인 항목이 앞 ② `52480` 점수 내림차순(칸1·칸2 비용 합 + 군주 주의와 같은 칸 가산 `A6A8` + 세력 무장 최다 다른 주의 `22B360`와 같은 칸 가산 `A69C`) ③ 선호 항목 직접 일치 가산 합 내림 ④ 선호 항목 인접 효과코드 일치 가산 합 내림 ⑤ 항목 id 오름차순(완전 전순서). 선호 항목 `+0x88`/`+0x90`은 노드에 남아 다음 실행에 쓰인다(상태 있음). 끝에 채택 비트가 백업과 다르면 `229A70`이 `군주군단+0x14 = clamp(명령서 − 새 채택 비용, 0, 200)` 확정. 난수 없음. `+0x50`/`+0x54`(항목 종류 키 2개)의 출처 미확인 [Sonnet 판독 2026-11-25·미검증] | 코드 / 가설(`+0x50`·`+0x54` 출처, 루프 내 `6DE100` 3번째 인수) |
| CCommandExecutionGovernmentAutoNode | `53B80` | 세력 1 | **시정(관직) 5줄 + 군사 자동 배치**(내정 명령이 아님). 인수 `+0x38` = 대상 세력. `263520`(12.8KB, 고르기 순서 rules_domestic §8.1a)이 시정 5줄(행 0..4 × 열 0..6)의 새 배치안과 새 군사 후보를 만들고, 비용 `51FF0` = (군사 변경이면 1) + 행마다 현재 배치에 없는 무장 수의 합. 군주 군단 명령서(`+0x14`)가 0이거나 비용보다 작으면 **행 0부터 현재 배치로 되돌려** 비용이 명령서 이하가 될 때까지 줄이고(군사 변경 비용은 되돌리지 않음), 끝까지 줄여도 모자라면 결과 2(적용 없음). 적용 = 행마다 `2EFA70`, 군사는 `2F1780` 또는 해임 `2EB110`, 명령서 `+0x14 = clamp(명령서 − 비용, 0, 200)`. 군사 선택: 능력 2(지력, `231770(무장,2,0xFFE)`) ≥ `DAT_141A4B570`인 세력 무장 중 삽입 정렬 `24F570` — 능력 2 내림(엄격) → 현재 군사 가산 점수(100) 내림 → 입사년(`+0x166`) 오름 → 무장 번호 오름, 맨 앞이 새 군사. 난수 없음 [Sonnet 판독 2026-11-25·미검증] | 코드(노드·정렬·`263520` 골격, Gemini g15 + 지휘 세션 대조 2026-11-25) / 가설(행 이름 뜻, 상수 값) |
| CForceCommandMoveNode | `55310` | 군단 3 | 군단 거점 사이 무장 이동 명령(종류 1, `1F2630`)을 최대 3건 등록(골격). 인수: 객체 `+0x38` 거점 목록 L0, 정수 `+0x44`/`+0x48`/`+0x4C` = L0 소속·L0 밖·관문류(종류 `+0x4E−0x34 < 10`) 거점 가중치, `+0x50` 키 ≠ 0이면 대상 군단 교체. 거점 원소 {점수 = `231DB0`, 하한, 가중치, L0 소속 플래그}를 안정 병합 정렬 3연속(마지막이 최우선): 점수 내림 → 소속 플래그 0 먼저 → (점수 − eff) 내림, 동점은 앞 순서 유지. 원소 수 < 2이면 2. 루프(원소 수/2회, 이동 3회에서 중단): 맨 앞 A(점수−하한 ≥ 1)와 짝 B로 A의 무장(`6DA4D0`)을 `1F2630`으로 이동, 성공마다 군단 `+0x14 = clamp(명령서 − DAT_141A4B4D0, 0, 200)`. 난수 없음. [Sonnet 판독 2026-11-25·미검증 → 작성자 디컴파일 대조(`decomp_cache.py get 55310`): 평균 보정식 `(Σ무장 수 − Σ목표 인원)/(도시 수+1)`, 정렬 3회, 이동 가능 인원 식(`max(목표, 하한)` 선택), 최대 3건(`2 < 발행 수`), 명령서 소모, 2차 경로 `+0xE7 != 'I'`] **채움(이동 인원·후보 필터·보조 갈래)**: 거점 원소 = {거점 `+0x10`, 무장 수(`231DB0`) `+0x18`, 하한 `+0x1C`(도시는 도시 내 항목 수(`22BA10`, 추정)+2, 관문은 1+2), 목표 인원 `+0x20`, L0 소속 플래그 `+0x24`}. 목표 인원은 거점이 L0이면 `+0x44`, 아니면 `+0x48`, 관문류면 `+0x4C`이다(위 「가중치」는 이 목표 인원이다). 이동 중인 무장(vcall `+0x98 == 1`)은 출발 거점 무장 수에서 1을 빼고 도착 거점에 1을 더해 센다. 도시마다 목표 인원에 `max(0, (무장 수 총합 − 목표 인원 총합) / (도시 수+1))`(정수 나눗셈)을 더한다(관문 제외). 정렬 3연속 뒤 루프는 원소 수/2회, 매회 목록의 **마지막(부족이 가장 큰 곳)** 을 도착, **첫 원소**를 출발로 한다. 도착의 부족량(목표−현재) < 1이거나 반복 수가 한도를 넘으면 끝, 도착 거점 세력이 플레이어 쪽(`235150`)이면 출발 후보를 vcall `+0x78` 값이 도착과 같은 쪽 먼저로 재배치한다. **이동 가능 인원**: 출발이 L0 소속이고 도착의 현재 무장이 0명이면 `max(1, 무장 수 − max(목표, 하한))`, 도착이 비어 있지 않으면 `무장 수 − max(목표, 하한)`(하한 클램프 없음), L0 소속이 아니면 `무장 수 − 목표`; 출발 무장 수 < 2 또는 이동 가능 인원 < 1이면 실패 카운터만 올린다. **무장 선택**: 출발 거점의 무장 목록(`6DA4D0`)을 앞에서부터 보며, 컴퓨터 쪽 무장이 군단장도 거점 대표도 아니면(플레이어 쪽이거나 군단장·대표이면 군단 `+0x11`이 거점 대표 `+0x11`과 같을 때만) 후보 검증에 올리고, 관계 목록에 `233BE0 == 0`·`234AB0(,0) == 0`·`+0x15E` bit14 = 0인 다른 무장이 없으면 순회 전체를 중단하며, `22EFD0 ≠ 0`이고 `22BAB0(무장,1)`이 무효(부대 없음)면 선택 목록 꼬리에 넣는다. 선택 수는 「부족량 잔여」와 「이동 가능 인원」 두 한도에 모두 걸려 중단한다(실효 상한은 두 값 중 작은 쪽 쯤, 코드 두 비교를 합친 해석). 선택이 있으면 `1F2630(목록,0)`(새 객체 `0x78`바이트를 `world+0x871E0` 쪽 관리자에 등록, 도착 거점이 선택 무장의 소속 `+0xE4`와 다를 때만 발행)을 부르고, 발행마다 군단 `+0x14` 소모 뒤 발행 3건에서 멈춘다. **이동 0건이면 2차 경로**: 목록이 2개 이상일 때 복사본에서 원소 수/2회, 마지막을 도착으로 하여 출발 거점 대표의 `+0x14 == 0`이면 끝내고, 출발 무장 중 `+0xE7 != 'I'`(0x49, 관직 값)인 무장을 `+0xE7 == 'I'`인 무장 수만큼 골라 같은 검증 뒤 `1F2630`으로 발행한다. 소모량 `DAT_141A4B4D0`=1(rules_people.md). 명령서 이름은 이미 확정된 `+0x14` 쪽을 따른다(g31의 「행동 포인트일 가설」은 쓰지 않음) | 코드(인수·정렬·이동 인원 식·`1F2630` 경로) / 가설(하한 뜻, 2차 경로의 `+0xE7` 뜻, 선택 상한 해석) |
| CRepairNeigoborObjectNode | `200A0` | 0/0/0/1 | 이웃 건물 보수(부대 판단표) | 이름 |

## 정정 기록

| 옛 해석 | 정정본 | 근거 |
|---|---|---|
| `53270`: 거점 `+0x14`가 임계값 이상일 때만 실행 | 실행 무장의 **군단** `+0x14`(명령서)가 `DAT_141A4B740` 이상일 때 | [Sonnet 판독 2026-11-25·미검증] s3 |
| `52FC0`(functions.md 577): 주의 채택 명령 1회 실행, 옛 RVA `52350` | 후보를 정렬해 명령서가 닳을 때까지 여러 항목 연속 채택하는 반복 노드. 옛 RVA `52350`은 현 빌드에서 `522B0` 안쪽(함수 시작점 아님) | [Sonnet 판독 2026-11-25·미검증] s3 |
| `53B80`: 내정 자동 명령 | 시정 5줄 + 군사 자동 배치(명령서로 비용 지불, 모자라면 되돌림) | [Sonnet 판독 2026-11-25·미검증] s3 |
| `29A90`: 정렬 헬퍼 7개 모두 정렬, 방향 미해결 | ①~④ 오름·⑤ 내림, 모두 안정 삽입(마지막이 최우선); ⑥⑦은 조건 분할 이동(군단장·군주가 대장인 부대를 앞으로, 만족 원소는 역순, 원래 머리 원소는 미검사로 그 뒤) | ①·⑥⑦ 확정(코드, 지휘 세션 대조 2026-11-25); ②~⑤ [Sonnet 판독 2026-11-25·미검증] s3 |
| `3A200` 인수 `[6]`: 수치(0이면 A 갈래 허용) | 그 값은 B 갈래 경로 방향 플래그도 겸한다(0: 기점→지역, 그 밖: 지역→기점) | [Sonnet 판독 2026-11-25·미검증] s3 |
| `1FE50`: 가까운 본거 조회 | 이번 이동 경로 위 지역 중심 칸을 경유점에 보충(`9CC90`) | [Sonnet 판독 2026-11-25·미검증] s4 |
| `2D720`·`7C300`: 세력 BT 3회(functions.md) | 군단 판단표 3회(사용 횟수 열이 군단) | [Codex 판독 2026-11-25·미검증] |
| `3E750`(CRecruitOfficerSetNode): 등용 담당관 설정 | 거점 `+0xCA` 모병 담당관 배치(Remove `3E6B0`도 같은 필드, 0번 무장 기준 해제) | [Codex 판독 2026-11-25·미검증] |
| `3E6B0`·`3EEB0`: 판단표 둘째 인수(현재 모병/훈련 담당관)를 노드가 소비 | 코드는 첫 인수(거점)만 읽는다 | [Codex 판독 2026-11-25·미검증] |
| `3EAA0`: 사전 검사와 차감이 같은 상수 | 사전 검사 `DAT_141A4B440`, 실제 차감 `DAT_141A4B21C`(다른 상수) | [Codex 판독 2026-11-25·미검증] |
| `BFBC0` 종류 0·1: 둘 다 「무장」 → 소속 거점(`230350`·`22EDF0`) | **0 = 세력 객체**(`+0x10` u16 = 군주 무장 번호) → 군주 소속 거점 칸, **1 = 군단 객체**(`+0x12` u16 = 군단장 무장 번호) → 군단장 소속 거점 칸. 두 함수는 같은 구조이나 읽는 필드가 다르다 | [Sonnet 판독 2026-11-25·미대조] g30 → 작성자 디컴파일 대조(`BFBC0`·`230350`·`22EDF0` 본문, structs.md 세력·군단 절) |
| `7B7B0`: 표 접근식 `표+번호×8`이 정의 크기 `0x48`과 맞지 않음(미확인) | 충돌 아님: `world+0x73860`은 포인터 배열, 가리키는 지형 정의 객체가 0x48바이트(structs.md 「지형 객체 표」와 같은 뜻) | [Sonnet 판독 2026-11-25·미대조] g30 → 작성자 디컴파일 대조(`233310`) |
