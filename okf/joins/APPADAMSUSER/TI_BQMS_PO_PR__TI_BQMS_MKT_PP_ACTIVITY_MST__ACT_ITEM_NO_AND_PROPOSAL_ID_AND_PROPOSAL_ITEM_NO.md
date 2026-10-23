---
type: Join Relationship
title: BQMS 의뢰정보 신규 IF 20260923 → NERP PP 정보 신규 IF 20260923
description: TI_BQMS_PO_PR.ACT_ITEM_NO,PROPOSAL_ID,PROPOSAL_ITEM_NO → TI_BQMS_MKT_PP_ACTIVITY_MST.ACT_ITEM_NO,PROPOSAL_ID,PROPOSAL_ITEM_NO (N:1, 신뢰도 medium, 고아 1.0%).
tags: ['join:index-inferred', 'card:n-1', 'conf:medium']
from: /schemas/APPADAMSUSER/tables/TI_BQMS_PO_PR.md
to: /schemas/APPADAMSUSER/tables/TI_BQMS_MKT_PP_ACTIVITY_MST.md
from_columns: [ACT_ITEM_NO, PROPOSAL_ID, PROPOSAL_ITEM_NO]
to_columns: [ACT_ITEM_NO, PROPOSAL_ID, PROPOSAL_ITEM_NO]
cardinality: N:1
usable: true
join_condition: TI_BQMS_PO_PR.ACT_ITEM_NO = TI_BQMS_MKT_PP_ACTIVITY_MST.ACT_ITEM_NO AND TI_BQMS_PO_PR.PROPOSAL_ID = TI_BQMS_MKT_PP_ACTIVITY_MST.PROPOSAL_ID AND TI_BQMS_PO_PR.PROPOSAL_ITEM_NO = TI_BQMS_MKT_PP_ACTIVITY_MST.PROPOSAL_ITEM_NO
join_type_hint: LEFT
join_filter: null
cartesian_risk: none
parent_unique: constraint
match_ratio: 0.9899
fanout:
  avg: 1.0
  p99: 1
  max: 2
  basis: exact
evidence: index_name_match
status: draft
stale_after: 2027-01-11T13:53:08+09:00
sources:
- id: verification
  resource: /references/join-verification.md
  title: 조인 실측 요약
generated:
  by: process:okf-join-builder/0.1
  at: 2026-10-13T13:53:08+09:00
---

# 조인 조건
<!-- AUTO:BEGIN condition -->
```sql
TI_BQMS_PO_PR.ACT_ITEM_NO = TI_BQMS_MKT_PP_ACTIVITY_MST.ACT_ITEM_NO AND TI_BQMS_PO_PR.PROPOSAL_ID = TI_BQMS_MKT_PP_ACTIVITY_MST.PROPOSAL_ID AND TI_BQMS_PO_PR.PROPOSAL_ITEM_NO = TI_BQMS_MKT_PP_ACTIVITY_MST.PROPOSAL_ITEM_NO
```
<!-- AUTO:END condition -->

# 근거
<!-- AUTO:BEGIN evidence -->
- 근거: 유니크 키와 컬럼 이름·타입 일치 (name:pk-composite)
- 선언된 PK/UK/유니크 인덱스로 부모 키가 유일하다
- 자식 키가 있는 행 45884건(전수) 중 99.0% 가 부모에 존재
- 고아 1.0% → LEFT JOIN 권장
- 부모 1건당 자식: 평균 1.0, 최대 2 (exact)
<!-- AUTO:END evidence -->

# T2S 사용 주의
(사람이 보완: 예) 부모 테이블은 `DEL_YN = 'N'` 조건과 함께 쓴다)
