---
type: Join Relationship
title: 매출차감 Payment Header → 매출차감 Payment Item
description: TI_GRPF060와 TI_GRPF061는 PYDOC 로 이어지지만 양쪽 모두 중복이라 직접 조인하면 안 된다 (N:M).
tags: ['join:index-inferred', 'card:n-m', 'conf:medium']
from: /schemas/APPADAMSUSER/tables/TI_GRPF060.md
to: /schemas/APPADAMSUSER/tables/TI_GRPF061.md
from_columns: [PYDOC]
to_columns: [PYDOC]
cardinality: N:M
usable: false
join_condition: TI_GRPF060.PYDOC = TI_GRPF061.PYDOC
join_type_hint: null
join_filter: null
cartesian_risk: m2m
parent_unique: duplicate
match_ratio: 1.0
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

<!-- AUTO:BEGIN warning -->
**직접 조인 금지**: 양쪽 키가 모두 중복 (일치 100.0%) → 직접 조인하면 행이 곱해진다
<!-- AUTO:END warning -->

# 조인 조건
<!-- AUTO:BEGIN condition -->
```sql
TI_GRPF060.PYDOC = TI_GRPF061.PYDOC
```
<!-- AUTO:END condition -->

# 근거
<!-- AUTO:BEGIN evidence -->
- 근거: 유니크 키와 컬럼 이름·타입 일치 (procedure:add_info)
- 부모 키가 유일하지 않다
- 자식 키가 있는 행 101950건(표본 7.189331%) 중 100.0% 가 부모에 존재
- 판정: 양쪽 키가 모두 중복 (일치 100.0%) → 직접 조인하면 행이 곱해진다
<!-- AUTO:END evidence -->

# T2S 사용 주의
(사람이 보완: 예) 부모 테이블은 `DEL_YN = 'N'` 조건과 함께 쓴다)
