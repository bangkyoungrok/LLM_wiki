# bottom_up — 데이터 이상징후 분석(Bottom-up)

통계 도구(stat_screen, find_duplicates, find_number_gaps, match_tables)와 점검 질의로 이상 신호를 찾고, 데이터 이상징후 패턴(P-101 ~ P-141) 조합으로 가설을 세워 데이터로 확인·반박·재분류·보류를 판정한다. 확인된 가설을 시나리오로 만들어 UNION ALL 질의로 `sql_submit` 1회에 집계해 보고서로 낸다.

| 경로 | 내용 |
|---|---|
| `AGENTS.md` | 규약, 건수 점검, 보고서 틀 |
| `skills/data-investigation/` | 절차(대상 → 탐색 → 가설 → 조사 → 표본 → 제출 → 보고서), 통계 도구, 질의, 결과 읽기, 답변 형식 |
| `skills/sql-query/` | 테이블 선택, 그라운딩, 조인, 작성 규칙, 시험 실행 판정 |
| `sub-agents/` | stat-screener, hypothesis-worker, term-grounding |
| `wiki/` | 이상징후 패턴, 위험 해석, 정상 업무, 선별 기준 |
| `okf/` | OKF 번들 (`main` 브랜치 OKF.md) |

- 출력: 확인된 시나리오 1건마다 11절 분석 보고서(부록 A-1 사용 테이블, A-2 탐지 SQL) + `## 만들지 못한 시나리오` + `## 부수 발견` + `## 부록: 시나리오 JSON`. 확인된 시나리오가 없으면 JSON 부록을 쓰지 않는다.
- 상한: main `sql_run` 10회, 테이블 문서 10개, `sql_submit` 1회(+1). stat-screener 동시 4개, hypothesis-worker 가설당 `sql_run` 5회·통계 도구 2회, 동시 5개.
- 등록 전에 `AGENTS.md` 6절 접속 URL 의 `<PASSWORD>` 를 실제 값으로 바꾼다.
