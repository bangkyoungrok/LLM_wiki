---
type: Join Relationship
title: '마케팅 비용 처리 내역 : 19년~ → MBO(마케팅 예산 조직)(엑셀)'
description: TI_GRPF039.MBOCD → TI_GRPF913.MBOCD (N:1, 신뢰도 medium, 고아 0.9%).
tags: ['join:index-inferred', 'card:n-1', 'conf:medium']
from: /schemas/APPADAMSUSER/tables/TI_GRPF039.md
to: /schemas/APPADAMSUSER/tables/TI_GRPF913.md
from_columns: [MBOCD]
to_columns: [MBOCD]
cardinality: N:1
usable: true
join_condition: TI_GRPF039.MBOCD = TI_GRPF913.MBOCD
join_type_hint: LEFT
join_filter: null
cartesian_risk: fanout
parent_unique: constraint
match_ratio: 0.9914
fanout:
  avg: 2416.77
  p99: 9094
  max: 20145
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
TI_GRPF039.MBOCD = TI_GRPF913.MBOCD
```
<!-- AUTO:END condition -->

# 근거
<!-- AUTO:BEGIN evidence -->
- 근거: 유니크 키와 컬럼 이름·타입 일치 (name:pk)
- 선언된 PK/UK/유니크 인덱스로 부모 키가 유일하다
- 자식 키가 있는 행 282762건(전수) 중 99.1% 가 부모에 존재
- 고아 0.9% → LEFT JOIN 권장
- 부모 1건당 자식: 평균 2416.77, 최대 20145 (exact)
<!-- AUTO:END evidence -->

# T2S 사용 주의
(사람이 보완: 예) 부모 테이블은 `DEL_YN = 'N'` 조건과 함께 쓴다)
