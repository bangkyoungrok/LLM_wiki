# top_down — 감사 시나리오 설계(Top-down)

wiki 의 부정 패턴(P-001 ~ P-032) 2~3개 조합을 OKF 스키마에 대입해 신규 감사 시나리오 SQL 을 만들고, 통과한 시나리오의 건수를 UNION ALL 질의로 `sql_submit` 1회에 집계해 보고서로 낸다.

| 경로 | 내용 |
|---|---|
| `AGENTS.md` | 규약, 통과 기준, 보고서 틀 |
| `skills/scenario-design/` | Process(패턴 선택 → 대입 → 조합 → 선별 → 시험 → 제출 → 답변), 질의 작성, 답변 형식 |
| `skills/sql-query/` | 테이블 선택, 그라운딩, 조인, 작성 규칙, 시험 실행 판정 |
| `sub-agents/` | scenario-worker(후보 1건 대입·시험), term-grounding(후보별 확인) |
| `wiki/` | 부정 패턴, 선별 기준, 정상 업무, 기존 시나리오, ACFE·COSO |
| `okf/` | OKF 번들 (`main` 브랜치 OKF.md) |

- 출력: 유효 시나리오 1건마다 11절 분석 보고서(부록 A-1 사용 테이블, A-2 탐지 SQL) + `## 만들지 못한 시나리오` + `## 부록: 시나리오 JSON`(시나리오마다 `{"scenario_name":"…","scenario_sql":"…"}`). 유효 시나리오가 없으면 JSON 부록을 쓰지 않는다.
- 상한: main `sql_run` 10회, 테이블 문서 10개, `sql_submit` 1회(+1). scenario-worker 후보당 `sql_run` 5회, 동시 5개.
- 등록 전에 `AGENTS.md` 6절 접속 URL 의 `<PASSWORD>` 를 실제 값으로 바꾼다.
