---
type: Join Relationship
title: 매출차감-정산내역+집계+시나리오체크(결합마스터)(최종) → 매출차감-컨디션 금액 및 체크(Report용)
description: TI_GRPB_DE_REPORT.CONDITION_NO → TI_GRPB_DE_CONDITION_AMT.CONDITION_NO (N:1, 신뢰도 medium, 고아 0.0%).
tags: ['join:index-inferred', 'card:n-1', 'conf:medium']
from: /schemas/APPADAMSUSER/tables/TI_GRPB_DE_REPORT.md
to: /schemas/APPADAMSUSER/tables/TI_GRPB_DE_CONDITION_AMT.md
from_columns: [CONDITION_NO]
to_columns: [CONDITION_NO]
cardinality: N:1
usable: true
join_condition: TI_GRPB_DE_REPORT.CONDITION_NO = TI_GRPB_DE_CONDITION_AMT.CONDITION_NO
join_type_hint: LEFT
join_filter: null
cartesian_risk: none
parent_unique: constraint
match_ratio: 1.0
fanout:
  avg: 1.33
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
TI_GRPB_DE_REPORT.CONDITION_NO = TI_GRPB_DE_CONDITION_AMT.CONDITION_NO
```
<!-- AUTO:END condition -->

# 근거
<!-- AUTO:BEGIN evidence -->
- 근거: 유니크 키와 컬럼 이름·타입 일치 (name:pk)
- 선언된 PK/UK/유니크 인덱스로 부모 키가 유일하다
- 자식 키가 있는 행 100105건(표본 0.833362%) 중 100.0% 가 부모에 존재
- 고아 0.0% → LEFT JOIN 권장
- 부모 1건당 자식: 평균 1.33, 최대 - (stats-est)
<!-- AUTO:END evidence -->

# T2S 사용 주의
(사람이 보완: 예) 부모 테이블은 `DEL_YN = 'N'` 조건과 함께 쓴다)
