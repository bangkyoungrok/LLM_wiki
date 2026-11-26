# 딕셔너리 추출 인벤토리

- 스냅샷: `20261025_141001`  (추출 시각 2026-10-25T14:10:01+09:00)
- DB 별칭: PRD, 접속 계정: AIAGT, Oracle 버전: 19.27.0.0.0
- 대상 OWNER: APPADAMSUSER, SETADAMSUSER

| CSV | 원천 뷰 | 필수 | 행 수 | 상태 | 소요(s) | 비고 |
|---|---|---|---|---|---|---|
| objects.csv | ALL_OBJECTS + ALL_USERS | Y | 374 | ok | 0.5 |  |
| tables.csv | ALL_TABLES | Y | 336 | ok | 0.4 |  |
| tab_comments.csv | ALL_TAB_COMMENTS | Y | 374 | ok | 0.1 |  |
| columns.csv | ALL_TAB_COLUMNS | Y | 14097 | ok | 0.8 | 변형 3 사용 |
| col_comments.csv | ALL_COL_COMMENTS | Y | 14051 | ok | 0.2 |  |
| constraints.csv | ALL_CONSTRAINTS | Y | 42 | ok | 0.2 |  |
| cons_columns.csv | ALL_CONS_COLUMNS | Y | 124 | ok | 0.6 |  |
| tab_privs.csv | ALL_TAB_PRIVS | Y | 382 | ok | 0.5 |  |
| col_privs.csv | ALL_COL_PRIVS | Y | 0 | ok | 0.2 |  |
| indexes.csv | ALL_INDEXES | Y | 118 | ok | 0.2 |  |
| ind_columns.csv | ALL_IND_COLUMNS | Y | 267 | ok | 0.1 |  |
| views.csv | ALL_VIEWS |  | 38 | ok | 0.1 |  |
| synonyms.csv | ALL_SYNONYMS |  | 1104 | ok | 0.2 |  |
| col_stats.csv | ALL_TAB_COL_STATISTICS |  | 11599 | ok | 0.7 |  |
| dependencies.csv | ALL_DEPENDENCIES |  | 88 | ok | 0.1 |  |
| part_keys.csv | ALL_PART_KEY_COLUMNS |  | 2 | ok | 0.1 |  |
| mviews.csv | ALL_MVIEWS |  | 0 | ok | 0.2 |  |
| session_roles.csv | SESSION_ROLES |  | 3 | ok | 0.0 |  |
| session_privs.csv | SESSION_PRIVS |  | 12 | ok | 0.0 |  |

제외한 뷰: ALL_SOURCE(프로시저 본문), 시스템·권한 관리 뷰, 세그먼트, 히스토그램, AUD$ 계열 (이번 범위 밖).