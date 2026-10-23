---
type: Join Relationship
title: 입찰및견적+발주및정산정보 → 견적집계_본사(SET)
description: TI_BQMS840.SITE_CD,REQ_NO,REQ_SEQ,ITEM_ID,EPR_CD → TI_BQMS005_INFA_QT.SITE_CODE,REQ_NO,REQ_SEQ,ITEM_ID,EPR_CODE (N:1, 신뢰도 medium, 고아 49.9%).
tags: ['join:index-inferred', 'card:n-1', 'conf:medium']
from: /schemas/APPADAMSUSER/tables/TI_BQMS840.md
to: /schemas/APPADAMSUSER/tables/TI_BQMS005_INFA_QT.md
from_columns: [SITE_CD, REQ_NO, REQ_SEQ, ITEM_ID, EPR_CD]
to_columns: [SITE_CODE, REQ_NO, REQ_SEQ, ITEM_ID, EPR_CODE]
cardinality: N:1
usable: true
join_condition: TI_BQMS840.SITE_CD = TI_BQMS005_INFA_QT.SITE_CODE AND TI_BQMS840.REQ_NO = TI_BQMS005_INFA_QT.REQ_NO AND TI_BQMS840.REQ_SEQ = TI_BQMS005_INFA_QT.REQ_SEQ AND TI_BQMS840.ITEM_ID = TI_BQMS005_INFA_QT.ITEM_ID AND TI_BQMS840.EPR_CD = TI_BQMS005_INFA_QT.EPR_CODE
join_type_hint: LEFT
join_filter: null
cartesian_risk: none
parent_unique: constraint
match_ratio: 0.5006
fanout:
  avg: 1.0
  p99: 1
  max: 8
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
TI_BQMS840.SITE_CD = TI_BQMS005_INFA_QT.SITE_CODE AND TI_BQMS840.REQ_NO = TI_BQMS005_INFA_QT.REQ_NO AND TI_BQMS840.REQ_SEQ = TI_BQMS005_INFA_QT.REQ_SEQ AND TI_BQMS840.ITEM_ID = TI_BQMS005_INFA_QT.ITEM_ID AND TI_BQMS840.EPR_CD = TI_BQMS005_INFA_QT.EPR_CODE
```
<!-- AUTO:END condition -->

# 근거
<!-- AUTO:BEGIN evidence -->
- 근거: 유니크 키와 컬럼 이름·타입 일치 (procedure:add_info)
- 선언된 PK/UK/유니크 인덱스로 부모 키가 유일하다
- 자식 키가 있는 행 100191건(표본 1.140111%) 중 50.1% 가 부모에 존재
- 고아 49.9% → LEFT JOIN 권장
- 부모 1건당 자식: 평균 1.0, 최대 8 (exact)
<!-- AUTO:END evidence -->

# T2S 사용 주의
(사람이 보완: 예) 부모 테이블은 `DEL_YN = 'N'` 조건과 함께 쓴다)
