---
type: Join Relationship
title: 거래선이름(히스토리) → 거래선정보
description: TI_GRPB811.CMCD,ENTP_CD → TI_GRPB810.CMCD,ENTP_CD (N:1, 신뢰도 medium, 고아 7.1%).
tags: ['join:index-inferred', 'card:n-1', 'conf:medium']
from: /schemas/APPADAMSUSER/tables/TI_GRPB811.md
to: /schemas/APPADAMSUSER/tables/TI_GRPB810.md
from_columns: [CMCD, ENTP_CD]
to_columns: [CMCD, ENTP_CD]
cardinality: N:1
usable: true
join_condition: TI_GRPB811.CMCD = TI_GRPB810.CMCD AND TI_GRPB811.ENTP_CD = TI_GRPB810.ENTP_CD
join_type_hint: LEFT
join_filter: null
cartesian_risk: none
parent_unique: constraint
match_ratio: 0.9292
fanout:
  avg: 1.4
  p99: 6
  max: 343
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
TI_GRPB811.CMCD = TI_GRPB810.CMCD AND TI_GRPB811.ENTP_CD = TI_GRPB810.ENTP_CD
```
<!-- AUTO:END condition -->

# 근거
<!-- AUTO:BEGIN evidence -->
- 근거: 유니크 키와 컬럼 이름·타입 일치 (name:pk-composite)
- 선언된 PK/UK/유니크 인덱스로 부모 키가 유일하다
- 자식 키가 있는 행 100900건(표본 3.469189%) 중 92.9% 가 부모에 존재
- 고아 7.1% → LEFT JOIN 권장
- 부모 1건당 자식: 평균 1.4, 최대 343 (exact)
<!-- AUTO:END evidence -->

# T2S 사용 주의
(사람이 보완: 예) 부모 테이블은 `DEL_YN = 'N'` 조건과 함께 쓴다)
