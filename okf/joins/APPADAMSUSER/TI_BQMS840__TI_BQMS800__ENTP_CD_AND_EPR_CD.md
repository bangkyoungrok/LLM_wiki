---
type: Join Relationship
title: 입찰및견적+발주및정산정보 → 업체(VENDOR)정보
description: TI_BQMS840.ENTP_CD,EPR_CD → TI_BQMS800.ENTP_CD,EPR_CD (N:1, 신뢰도 medium).
tags: ['join:index-inferred', 'card:n-1', 'conf:medium']
from: /schemas/APPADAMSUSER/tables/TI_BQMS840.md
to: /schemas/APPADAMSUSER/tables/TI_BQMS800.md
from_columns: [ENTP_CD, EPR_CD]
to_columns: [ENTP_CD, EPR_CD]
cardinality: N:1
usable: true
join_condition: TI_BQMS840.ENTP_CD = TI_BQMS800.ENTP_CD AND TI_BQMS840.EPR_CD = TI_BQMS800.EPR_CD
join_type_hint: LEFT
join_filter: null
cartesian_risk: fanout
parent_unique: constraint
match_ratio: 1.0
fanout:
  avg: 236.95
  p99: 3463
  max: 151777
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
TI_BQMS840.ENTP_CD = TI_BQMS800.ENTP_CD AND TI_BQMS840.EPR_CD = TI_BQMS800.EPR_CD
```
<!-- AUTO:END condition -->

# 근거
<!-- AUTO:BEGIN evidence -->
- 근거: 유니크 키와 컬럼 이름·타입 일치 (name:pk-composite)
- 선언된 PK/UK/유니크 인덱스로 부모 키가 유일하다
- 자식 키가 있는 행 100385건(표본 1.140111%) 중 100.0% 가 부모에 존재
- 부모 1건당 자식: 평균 236.95, 최대 151777 (exact)
<!-- AUTO:END evidence -->

# T2S 사용 주의
(사람이 보완: 예) 부모 테이블은 `DEL_YN = 'N'` 조건과 함께 쓴다)
