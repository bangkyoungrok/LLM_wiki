---
type: Join Relationship
title: 견적집계_INFA_QT_2 (2020년 10월 18일 이후 INFA_QT 적재 테이블)에서 연계하는 테이블_본사(SET) → 견적집계_본사(SET)
description: TI_BQMS005_INFA_QT_2.EPR_CODE,ITEM_ID,REQ_NO,REQ_SEQ,SITE_CODE → TI_BQMS005_INFA_QT.EPR_CODE,ITEM_ID,REQ_NO,REQ_SEQ,SITE_CODE (1:1, 신뢰도 medium).
tags: ['join:index-inferred', 'card:1-1', 'conf:medium']
from: /schemas/APPADAMSUSER/tables/TI_BQMS005_INFA_QT_2.md
to: /schemas/APPADAMSUSER/tables/TI_BQMS005_INFA_QT.md
from_columns: [EPR_CODE, ITEM_ID, REQ_NO, REQ_SEQ, SITE_CODE]
to_columns: [EPR_CODE, ITEM_ID, REQ_NO, REQ_SEQ, SITE_CODE]
cardinality: '1:1'
usable: true
join_condition: TI_BQMS005_INFA_QT_2.EPR_CODE = TI_BQMS005_INFA_QT.EPR_CODE AND TI_BQMS005_INFA_QT_2.ITEM_ID = TI_BQMS005_INFA_QT.ITEM_ID AND TI_BQMS005_INFA_QT_2.REQ_NO = TI_BQMS005_INFA_QT.REQ_NO AND TI_BQMS005_INFA_QT_2.REQ_SEQ = TI_BQMS005_INFA_QT.REQ_SEQ AND TI_BQMS005_INFA_QT_2.SITE_CODE = TI_BQMS005_INFA_QT.SITE_CODE
join_type_hint: LEFT
join_filter: null
cartesian_risk: none
parent_unique: constraint
match_ratio: 1.0
fanout:
  avg: 1.0
  p99: 1
  max: 1
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
TI_BQMS005_INFA_QT_2.EPR_CODE = TI_BQMS005_INFA_QT.EPR_CODE AND TI_BQMS005_INFA_QT_2.ITEM_ID = TI_BQMS005_INFA_QT.ITEM_ID AND TI_BQMS005_INFA_QT_2.REQ_NO = TI_BQMS005_INFA_QT.REQ_NO AND TI_BQMS005_INFA_QT_2.REQ_SEQ = TI_BQMS005_INFA_QT.REQ_SEQ AND TI_BQMS005_INFA_QT_2.SITE_CODE = TI_BQMS005_INFA_QT.SITE_CODE
```
<!-- AUTO:END condition -->

# 근거
<!-- AUTO:BEGIN evidence -->
- 근거: 유니크 키와 컬럼 이름·타입 일치 (name:pk-composite)
- 선언된 PK/UK/유니크 인덱스로 부모 키가 유일하다
- 자식 키가 있는 행 99541건(표본 2.28169%) 중 100.0% 가 부모에 존재
- 부모 1건당 자식: 평균 1.0, 최대 1 (exact)
<!-- AUTO:END evidence -->

# T2S 사용 주의
(사람이 보완: 예) 부모 테이블은 `DEL_YN = 'N'` 조건과 함께 쓴다)
