---
type: Join Relationship
title: 부서정보(GHR+LDAP) 히스토리 → 부서정보(GHR+LDAP)
description: TI_GRPF806H.COCD,IF_GB,INNR_DPCD → TI_GRPF806.COCD,IF_GB,INNR_DPCD (N:1, 신뢰도 medium, 고아 2.8%).
tags: ['join:index-inferred', 'card:n-1', 'conf:medium']
from: /schemas/APPADAMSUSER/tables/TI_GRPF806H.md
to: /schemas/APPADAMSUSER/tables/TI_GRPF806.md
from_columns: [COCD, IF_GB, INNR_DPCD]
to_columns: [COCD, IF_GB, INNR_DPCD]
cardinality: N:1
usable: true
join_condition: TI_GRPF806H.COCD = TI_GRPF806.COCD AND TI_GRPF806H.IF_GB = TI_GRPF806.IF_GB AND TI_GRPF806H.INNR_DPCD = TI_GRPF806.INNR_DPCD
join_type_hint: LEFT
join_filter: null
cartesian_risk: none
parent_unique: constraint
match_ratio: 0.972
fanout:
  avg: 18.2
  p99: 20
  max: 20
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
TI_GRPF806H.COCD = TI_GRPF806.COCD AND TI_GRPF806H.IF_GB = TI_GRPF806.IF_GB AND TI_GRPF806H.INNR_DPCD = TI_GRPF806.INNR_DPCD
```
<!-- AUTO:END condition -->

# 근거
<!-- AUTO:BEGIN evidence -->
- 근거: 유니크 키와 컬럼 이름·타입 일치 (name:pk-composite)
- 선언된 PK/UK/유니크 인덱스로 부모 키가 유일하다
- 자식 키가 있는 행 100089건(표본 5.420947%) 중 97.2% 가 부모에 존재
- 고아 2.8% → LEFT JOIN 권장
- 부모 1건당 자식: 평균 18.2, 최대 20 (exact)
<!-- AUTO:END evidence -->

# T2S 사용 주의
(사람이 보완: 예) 부모 테이블은 `DEL_YN = 'N'` 조건과 함께 쓴다)
