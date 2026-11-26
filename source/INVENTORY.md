# 딕셔너리 추출 인벤토리

- 스냅샷: `20261114_162924`  (추출 시각 2026-11-14T16:29:24+09:00)
- DB 별칭: PRD, 접속 계정: AIAGT, Oracle 버전: 19.30.0.0.0
- 대상 OWNER: APPADAMSUSER, SETADAMSUSER

| CSV | 원천 뷰 | 필수 | 행 수 | 상태 | 소요(s) | 비고 |
|---|---|---|---|---|---|---|
| objects.csv | ALL_OBJECTS + ALL_USERS | Y | 397 | ok | 0.2 |  |
| tables.csv | ALL_TABLES | Y | 346 | ok | 0.3 |  |
| tab_comments.csv | ALL_TAB_COMMENTS | Y | 397 | ok | 0.2 |  |
| columns.csv | ALL_TAB_COLUMNS | Y | 15254 | ok | 0.9 | 변형 3 사용 |
| col_comments.csv | ALL_COL_COMMENTS | Y | 15208 | ok | 0.3 |  |
| constraints.csv | ALL_CONSTRAINTS | Y | 42 | ok | 0.2 |  |
| cons_columns.csv | ALL_CONS_COLUMNS | Y | 124 | ok | 0.7 |  |
| tab_privs.csv | ALL_TAB_PRIVS | Y | 405 | ok | 0.6 |  |
| col_privs.csv | ALL_COL_PRIVS | Y | 0 | ok | 0.3 |  |
| indexes.csv | ALL_INDEXES | Y | 123 | ok | 0.2 |  |
| ind_columns.csv | ALL_IND_COLUMNS | Y | 278 | ok | 0.1 |  |
| views.csv | ALL_VIEWS |  | 51 | ok | 0.1 |  |
| synonyms.csv | ALL_SYNONYMS |  | 1121 | ok | 0.2 |  |
| col_stats.csv | ALL_TAB_COL_STATISTICS |  | 12176 | ok | 0.7 |  |
| dependencies.csv | ALL_DEPENDENCIES |  | 123 | ok | 0.1 |  |
| part_keys.csv | ALL_PART_KEY_COLUMNS |  | 2 | ok | 0.0 |  |
| mviews.csv | ALL_MVIEWS |  | 0 | ok | 0.2 |  |
| session_roles.csv | SESSION_ROLES |  | 3 | ok | 0.0 |  |
| session_privs.csv | SESSION_PRIVS |  | 12 | ok | 0.0 |  |

제외한 뷰: ALL_SOURCE(프로시저 본문), 시스템·권한 관리 뷰, 세그먼트, 히스토그램, AUD$ 계열 (이번 범위 밖).