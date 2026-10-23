---
type: Join Relationship
title: 시나리오 단계별 추출로직 → 시나리오 기본정보
description: TN_AD_SCENARIO_LOGIC.SCENARIO_ID,SCENARIO_VER → TN_AD_SCENARIO_BASE.SCENARIO_ID,SCENARIO_VER (N:1, 신뢰도 high, 고아 0.9%).
tags: ['join:view-derived', 'card:n-1', 'conf:high']
from: /schemas/SETADAMSUSER/tables/TN_AD_SCENARIO_LOGIC.md
to: /schemas/SETADAMSUSER/tables/TN_AD_SCENARIO_BASE.md
from_columns: [SCENARIO_ID, SCENARIO_VER]
to_columns: [SCENARIO_ID, SCENARIO_VER]
cardinality: N:1
usable: true
join_condition: TN_AD_SCENARIO_LOGIC.SCENARIO_ID = TN_AD_SCENARIO_BASE.SCENARIO_ID AND TN_AD_SCENARIO_LOGIC.SCENARIO_VER = TN_AD_SCENARIO_BASE.SCENARIO_VER
join_type_hint: LEFT
join_filter: null
cartesian_risk: none
parent_unique: data
match_ratio: 0.991
fanout:
  avg: 2.29
  p99: 4
  max: 5
  basis: exact
evidence: view_definition
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
TN_AD_SCENARIO_LOGIC.SCENARIO_ID = TN_AD_SCENARIO_BASE.SCENARIO_ID AND TN_AD_SCENARIO_LOGIC.SCENARIO_VER = TN_AD_SCENARIO_BASE.SCENARIO_VER
```
<!-- AUTO:END condition -->

# 근거
<!-- AUTO:BEGIN evidence -->
- 근거: 뷰 정의의 조인 조건 (view:SETADAMSUSER.V_SCN_LIST2)
- 데이터 검사에서 부모 키 중복 0건
- 자식 키가 있는 행 668건(전수) 중 99.1% 가 부모에 존재
- 고아 0.9% → LEFT JOIN 권장
- 부모 1건당 자식: 평균 2.29, 최대 5 (exact)
<!-- AUTO:END evidence -->

# T2S 사용 주의
(사람이 보완: 예) 부모 테이블은 `DEL_YN = 'N'` 조건과 함께 쓴다)
