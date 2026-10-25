# variation — 시나리오 변형(Scenario Variation)

기존 감사 시나리오(이름, 다른 agent 가 낸 JSON, 자연어 설명)를 감사 골격으로 나누고, 테이블 이전·도메인 이전·조건 강화·조건 확장·대칭 변형 가운데 요청에 맞는 변형 시나리오를 설계한다. 변형을 데이터로 확인·반박·재분류·보류로 판정하고, 확인된 변형의 건수를 UNION ALL 질의로 `sql_submit` 1회에 집계해 원본과 비교하는 보고서로 낸다.

| 경로 | 내용 |
|---|---|
| `AGENTS.md` | 규약, 변형 범위(감사 포인트 유지, 바꾸는 축 1~2개), 보고서 요지 |
| `skills/scenario-variation/` | 절차(원본 분해 → 변형 설계 → 데이터 확인 → 표본 → 제출 → 보고서), 변형 유형, 질의, 통계 도구, 답변 형식 |
| `skills/sql-query/` | 테이블 선택, 그라운딩, 조인, 작성 규칙, 시험 실행 판정 |
| `sub-agents/` | variation-worker(변형 후보 1건 확인), term-grounding(후보별 확인) |
| `wiki/` | 이상징후 패턴(조각 해석용), 위험 해석, 정상 업무, 선별 기준 |
| `okf/` | OKF 번들 (`main` 브랜치 OKF.md) |

- 출력: 시나리오 1건마다 11절 분석 보고서(부록 A-1 사용 테이블, A-2 탐지 SQL, A-3 원본 SQL) + `## 만들지 못한 시나리오` + `## 부록: 시나리오 JSON`. 확인된 변형이 없으면 JSON 부록을 쓰지 않는다.
- 상한: main `sql_run` 10회, 테이블 문서 10개, `sql_submit` 1회(+1). variation-worker 후보당 `sql_run` 5회·통계 도구 2회, 동시 5개.
- 등록 전에 `AGENTS.md` 6절 접속 URL 의 `<PASSWORD>` 를 실제 값으로 바꾼다.
