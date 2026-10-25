---
type: Join Relationship
title: 시나리오 컬럼정보 → 시나리오 단계별 추출로직
description: TN_AD_SCENARIO_COLUMN.SCENARIO_ID,SCENARIO_STEP,SCENARIO_VER → TN_AD_SCENARIO_LOGIC.SCENARIO_ID,SCENARIO_STEP,SCENARIO_VER (N:1, 신뢰도 medium, 고아 2.4%).
tags: ['join:index-inferred', 'card:n-1', 'conf:medium']
from: /schemas/SETADAMSUSER/tables/TN_AD_SCENARIO_COLUMN.md
to: /schemas/SETADAMSUSER/tables/TN_AD_SCENARIO_LOGIC.md
from_columns: [SCENARIO_ID, SCENARIO_STEP, SCENARIO_VER]
to_columns: [SCENARIO_ID, SCENARIO_STEP, SCENARIO_VER]
cardinality: N:1
usable: true
join_condition: TN_AD_SCENARIO_COLUMN.SCENARIO_ID = TN_AD_SCENARIO_LOGIC.SCENARIO_ID AND TN_AD_SCENARIO_COLUMN.SCENARIO_STEP = TN_AD_SCENARIO_LOGIC.SCENARIO_STEP AND TN_AD_SCENARIO_COLUMN.SCENARIO_VER = TN_AD_SCENARIO_LOGIC.SCENARIO_VER
join_type_hint: LEFT
join_filter: null
cartesian_risk: none
parent_unique: constraint
match_ratio: 0.9765
fanout:
  avg: 62.78
  p99: 158
  max: 158
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
TN_AD_SCENARIO_COLUMN.SCENARIO_ID = TN_AD_SCENARIO_LOGIC.SCENARIO_ID AND TN_AD_SCENARIO_COLUMN.SCENARIO_STEP = TN_AD_SCENARIO_LOGIC.SCENARIO_STEP AND TN_AD_SCENARIO_COLUMN.SCENARIO_VER = TN_AD_SCENARIO_LOGIC.SCENARIO_VER
```
<!-- AUTO:END condition -->

# 근거
<!-- AUTO:BEGIN evidence -->
- 근거: 유니크 키와 컬럼 이름·타입 일치 (name:pk-composite)
- 선언된 PK/UK/유니크 인덱스로 부모 키가 유일하다
- 자식 키가 있는 행 42630건(전수) 중 97.6% 가 부모에 존재
- 고아 2.4% → LEFT JOIN 권장
- 부모 1건당 자식: 평균 62.78, 최대 158 (exact)
<!-- AUTO:END evidence -->

# T2S 사용 주의
(사람이 보완: 예) 부모 테이블은 `DEL_YN = 'N'` 조건과 함께 쓴다)
