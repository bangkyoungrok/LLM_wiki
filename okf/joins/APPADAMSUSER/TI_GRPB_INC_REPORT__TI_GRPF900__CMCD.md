---
type: Join Relationship
title: 셀인셀아웃인센티브(점검결과 전체) → 회사코드(T001)(엑셀)
description: TI_GRPB_INC_REPORT.CMCD → TI_GRPF900.CMCD (N:1, 신뢰도 medium).
tags: ['join:index-inferred', 'card:n-1', 'conf:medium']
from: /schemas/APPADAMSUSER/tables/TI_GRPB_INC_REPORT.md
to: /schemas/APPADAMSUSER/tables/TI_GRPF900.md
from_columns: [CMCD]
to_columns: [CMCD]
cardinality: N:1
usable: true
join_condition: TI_GRPB_INC_REPORT.CMCD = TI_GRPF900.CMCD
join_type_hint: LEFT
join_filter: null
cartesian_risk: fanout
parent_unique: data
match_ratio: 1.0
fanout:
  avg: 2935.54
  p99: 28587
  max: 32237
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
TI_GRPB_INC_REPORT.CMCD = TI_GRPF900.CMCD
```
<!-- AUTO:END condition -->

# 근거
<!-- AUTO:BEGIN evidence -->
- 근거: 유니크 키와 컬럼 이름·타입 일치 (procedure:add_info)
- 데이터 검사에서 부모 키 중복 0건
- 자식 키가 있는 행 114486건(전수) 중 100.0% 가 부모에 존재
- 부모 1건당 자식: 평균 2935.54, 최대 32237 (exact)
<!-- AUTO:END evidence -->

# T2S 사용 주의
(사람이 보완: 예) 부모 테이블은 `DEL_YN = 'N'` 조건과 함께 쓴다)
