# t2s — T2S(OKF) 프로젝트

자연어 질문을 감사시스템 Oracle 19c 의 SELECT 로 바꿔 답한다. 도메인 page 「## 테이블 목록」에서 후보를 모아 `okf/t2s/rules/table-selection.md` 순서로 테이블을 고르고, `sql_run` 으로 확인한 뒤 `sql_submit` 을 1회 부른다.

| 경로 | 내용 |
|---|---|
| `AGENTS.md` | 규약: 범위, 금지, 도구·상한, 경로, DB, 답변 형식, 위임 |
| `skills/sql-query/` | 테이블 선택, 그라운딩, 조인, 작성 규칙, 판정, 제출 |
| `sub-agents/term-grounding/` | 후보 테이블별 컬럼·값 확인(고르지 않음) |
| `okf/` | OKF 번들 (`main` 브랜치 OKF.md) |

- 상한: main `sql_run` 10회, 테이블 문서 10개, `sql_submit` 1회(오류 시 1회 재제출). term-grounding `sql_run` 6회.
- 등록 전에 `AGENTS.md` 6절 접속 URL 의 `<PASSWORD>` 를 실제 값으로 바꾼다.
