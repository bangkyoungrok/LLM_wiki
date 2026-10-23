---
type: Join Relationship
title: '판가 Condition(헤더+아이템)(15년~23년)(결합) → 판가 Header 정보 : 15년~24년6월'
description: TI_GRPB_PRICE_CONDITION.DOC_NO → TI_GRPB_PRICE_HEADER.DOC_NO (N:1, 신뢰도 medium).
tags: ['join:index-inferred', 'card:n-1', 'conf:medium']
from: /schemas/APPADAMSUSER/tables/TI_GRPB_PRICE_CONDITION.md
to: /schemas/APPADAMSUSER/tables/TI_GRPB_PRICE_HEADER.md
from_columns: [DOC_NO]
to_columns: [DOC_NO]
cardinality: N:1
usable: true
join_condition: TI_GRPB_PRICE_CONDITION.DOC_NO = TI_GRPB_PRICE_HEADER.DOC_NO
join_type_hint: LEFT
join_filter: null
cartesian_risk: fanout
parent_unique: constraint
match_ratio: 1.0
fanout:
  avg: 112.81
  p99: 2701
  max: 12991
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
TI_GRPB_PRICE_CONDITION.DOC_NO = TI_GRPB_PRICE_HEADER.DOC_NO
```
<!-- AUTO:END condition -->

# 근거
<!-- AUTO:BEGIN evidence -->
- 근거: 유니크 키와 컬럼 이름·타입 일치 (name:pk)
- 선언된 PK/UK/유니크 인덱스로 부모 키가 유일하다
- 자식 키가 있는 행 100857건(표본 1.107487%) 중 100.0% 가 부모에 존재
- 부모 1건당 자식: 평균 112.81, 최대 12991 (exact)
<!-- AUTO:END evidence -->

# T2S 사용 주의
(사람이 보완: 예) 부모 테이블은 `DEL_YN = 'N'` 조건과 함께 쓴다)
