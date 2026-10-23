---
type: Join Relationship
title: 계약마스터_본사(SET)_히스토리 → 계약마스터_본사(SET)
description: TI_BQMS026_INFA_CTRT_H.CTR_CATEGORY_ID,CTR_DATE_END,CTR_DATE_START,CTR_NO,EPR_CODE,SITE_CODE → TI_BQMS026_INFA_CTRT.CTR_CATEGORY_ID,CTR_DATE_END,CTR_DATE_START,CTR_NO,EPR_CODE,SITE_CODE (N:1, 신뢰도 medium, 고아 0.0%).
tags: ['join:index-inferred', 'card:n-1', 'conf:medium']
from: /schemas/APPADAMSUSER/tables/TI_BQMS026_INFA_CTRT_H.md
to: /schemas/APPADAMSUSER/tables/TI_BQMS026_INFA_CTRT.md
from_columns: [CTR_CATEGORY_ID, CTR_DATE_END, CTR_DATE_START, CTR_NO, EPR_CODE, SITE_CODE]
to_columns: [CTR_CATEGORY_ID, CTR_DATE_END, CTR_DATE_START, CTR_NO, EPR_CODE, SITE_CODE]
cardinality: N:1
usable: true
join_condition: TI_BQMS026_INFA_CTRT_H.CTR_CATEGORY_ID = TI_BQMS026_INFA_CTRT.CTR_CATEGORY_ID AND TI_BQMS026_INFA_CTRT_H.CTR_DATE_END = TI_BQMS026_INFA_CTRT.CTR_DATE_END AND TI_BQMS026_INFA_CTRT_H.CTR_DATE_START = TI_BQMS026_INFA_CTRT.CTR_DATE_START AND TI_BQMS026_INFA_CTRT_H.CTR_NO = TI_BQMS026_INFA_CTRT.CTR_NO AND TI_BQMS026_INFA_CTRT_H.EPR_CODE = TI_BQMS026_INFA_CTRT.EPR_CODE AND TI_BQMS026_INFA_CTRT_H.SITE_CODE = TI_BQMS026_INFA_CTRT.SITE_CODE
join_type_hint: LEFT
join_filter: null
cartesian_risk: none
parent_unique: constraint
match_ratio: 0.9999
fanout:
  avg: 33.02
  basis: stats-est
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
TI_BQMS026_INFA_CTRT_H.CTR_CATEGORY_ID = TI_BQMS026_INFA_CTRT.CTR_CATEGORY_ID AND TI_BQMS026_INFA_CTRT_H.CTR_DATE_END = TI_BQMS026_INFA_CTRT.CTR_DATE_END AND TI_BQMS026_INFA_CTRT_H.CTR_DATE_START = TI_BQMS026_INFA_CTRT.CTR_DATE_START AND TI_BQMS026_INFA_CTRT_H.CTR_NO = TI_BQMS026_INFA_CTRT.CTR_NO AND TI_BQMS026_INFA_CTRT_H.EPR_CODE = TI_BQMS026_INFA_CTRT.EPR_CODE AND TI_BQMS026_INFA_CTRT_H.SITE_CODE = TI_BQMS026_INFA_CTRT.SITE_CODE
```
<!-- AUTO:END condition -->

# 근거
<!-- AUTO:BEGIN evidence -->
- 근거: 유니크 키와 컬럼 이름·타입 일치 (name:pk-composite)
- 선언된 PK/UK/유니크 인덱스로 부모 키가 유일하다
- 자식 키가 있는 행 102667건(표본 0.27343%) 중 100.0% 가 부모에 존재
- 고아 0.0% → LEFT JOIN 권장
- 부모 1건당 자식: 평균 33.02, 최대 - (stats-est)
<!-- AUTO:END evidence -->

# T2S 사용 주의
(사람이 보완: 예) 부모 테이블은 `DEL_YN = 'N'` 조건과 함께 쓴다)
