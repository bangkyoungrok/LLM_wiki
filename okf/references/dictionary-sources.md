---
type: Reference
title: 딕셔너리 추출 스냅샷
description: AIAGT 로 추출한 오라클 딕셔너리 뷰 스냅샷 20261013_135308 의 내역.
resource: oracle://PRD
tags: [reference]
generated:
  by: process:okf-dict-builder/0.1
  at: 2026-10-13T13:53:08+09:00
---

# 개요
번들의 모든 Oracle Table/View 문서가 근거로 삼는 딕셔너리 추출 스냅샷이다.

# 추출 내역
<!-- AUTO:BEGIN sources -->
- 스냅샷 ID: `20261013_135308`
- 추출 시각: 2026-10-13T13:53:08+09:00
- DB 별칭: PRD / 접속 계정: AIAGT / Oracle 버전: 19.27.0.0.0
- 대상 OWNER: APPADAMSUSER, SETADAMSUSER

| CSV | 원천 뷰 | 행 수 | 상태 | 비고 |
|---|---|---|---|---|
| objects.csv | ALL_OBJECTS + ALL_USERS | 367 | ok |  |
| tables.csv | ALL_TABLES | 329 | ok |  |
| tab_comments.csv | ALL_TAB_COMMENTS | 367 | ok |  |
| columns.csv | ALL_TAB_COLUMNS | 13622 | ok | 변형 3 사용 |
| col_comments.csv | ALL_COL_COMMENTS | 13579 | ok |  |
| constraints.csv | ALL_CONSTRAINTS | 46 | ok |  |
| cons_columns.csv | ALL_CONS_COLUMNS | 133 | ok |  |
| tab_privs.csv | ALL_TAB_PRIVS | 375 | ok |  |
| col_privs.csv | ALL_COL_PRIVS | 0 | ok |  |
| indexes.csv | ALL_INDEXES | 118 | ok |  |
| ind_columns.csv | ALL_IND_COLUMNS | 276 | ok |  |
| views.csv | ALL_VIEWS | 38 | ok |  |
| synonyms.csv | ALL_SYNONYMS | 1099 | ok |  |
| col_stats.csv | ALL_TAB_COL_STATISTICS | 11107 | ok |  |
| dependencies.csv | ALL_DEPENDENCIES | 88 | ok |  |
| part_keys.csv | ALL_PART_KEY_COLUMNS | 1 | ok |  |
| mviews.csv | ALL_MVIEWS | 0 | ok |  |
| session_roles.csv | SESSION_ROLES | 3 | ok |  |
| session_privs.csv | SESSION_PRIVS | 12 | ok |  |
<!-- AUTO:END sources -->
