---
type: Join Relationship
title: 마케팅 비용(최초 계획 금액포함) → MBO(마케팅 예산 조직)(엑셀)
description: TI_GRPF_EO_INFO.MBO_CODE → TI_GRPF913.MBOCD (N:1, 신뢰도 medium, 고아 0.2%).
tags: ['join:comment-inferred', 'card:n-1', 'conf:medium']
from: /schemas/APPADAMSUSER/tables/TI_GRPF_EO_INFO.md
to: /schemas/APPADAMSUSER/tables/TI_GRPF913.md
from_columns: [MBO_CODE]
to_columns: [MBOCD]
cardinality: N:1
usable: true
join_condition: TI_GRPF_EO_INFO.MBO_CODE = TI_GRPF913.MBOCD
join_type_hint: LEFT
join_filter: null
cartesian_risk: fanout
parent_unique: constraint
match_ratio: 0.9984
fanout:
  avg: 31008.91
  p99: 329050
  max: 577109
  basis: exact
evidence: comment_match
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
TI_GRPF_EO_INFO.MBO_CODE = TI_GRPF913.MBOCD
```
<!-- AUTO:END condition -->

# 근거
<!-- AUTO:BEGIN evidence -->
- 근거: 컬럼 설명(한글명) 일치 (comment)
- 선언된 PK/UK/유니크 인덱스로 부모 키가 유일하다
- 자식 키가 있는 행 99974건(표본 2.028226%) 중 99.8% 가 부모에 존재
- 고아 0.2% → LEFT JOIN 권장
- 부모 1건당 자식: 평균 31008.91, 최대 577109 (exact)
<!-- AUTO:END evidence -->

# T2S 사용 주의
(사람이 보완: 예) 부모 테이블은 `DEL_YN = 'N'` 조건과 함께 쓴다)
