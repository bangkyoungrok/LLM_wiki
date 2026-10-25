---
type: Join Relationship
title: 선적 출고 실행 Confirm 이력 관리(PO Confirmation)[pop] → PLANT(엑셀)
description: TI_GSCM003.PLANT → TI_GRPF911.PLANT (N:1, 신뢰도 medium, 고아 0.5%).
tags: ['join:index-inferred', 'card:n-1', 'conf:medium']
from: /schemas/APPADAMSUSER/tables/TI_GSCM003.md
to: /schemas/APPADAMSUSER/tables/TI_GRPF911.md
from_columns: [PLANT]
to_columns: [PLANT]
cardinality: N:1
usable: true
join_condition: TI_GSCM003.PLANT = TI_GRPF911.PLANT
join_type_hint: LEFT
join_filter: null
cartesian_risk: fanout
parent_unique: constraint
match_ratio: 0.9952
fanout:
  avg: 16320.31
  p99: 110878
  max: 278974
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
TI_GSCM003.PLANT = TI_GRPF911.PLANT
```
<!-- AUTO:END condition -->

# 근거
<!-- AUTO:BEGIN evidence -->
- 근거: 유니크 키와 컬럼 이름·타입 일치 (name:pk)
- 선언된 PK/UK/유니크 인덱스로 부모 키가 유일하다
- 자식 키가 있는 행 100251건(표본 3.000073%) 중 99.5% 가 부모에 존재
- 고아 0.5% → LEFT JOIN 권장
- 부모 1건당 자식: 평균 16320.31, 최대 278974 (exact)
<!-- AUTO:END evidence -->

# T2S 사용 주의
(사람이 보완: 예) 부모 테이블은 `DEL_YN = 'N'` 조건과 함께 쓴다)
