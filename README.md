# LLM_wiki

감사시스템 Oracle 19c(조회 계정 `AIAGT`)를 조회하는 agent studio 프로젝트 3종을 브랜치별로 관리한다. 세 프로젝트 모두 OKF 번들(`okf/`)을 테이블·컬럼·조인의 근거로 쓴다. OKF 설명은 [OKF.md](OKF.md) 에 따로 있다.

## 브랜치

| 브랜치 | 프로젝트 | 하는 일 | 최종 출력 |
|---|---|---|---|
| `main` | 공통 | 이 README, OKF 설명, 도구 스크립트 | — |
| `t2s` | T2S | 자연어 질문을 Oracle SELECT 로 바꿔 `sql_run` 으로 확인하고 `sql_submit` 1회 | 답변 + 근거 |
| `top_down` | 감사 시나리오 설계 | 부정 패턴(P-001 ~ P-032) 조합을 OKF 스키마에 대입해 신규 시나리오 SQL 을 만든다 | 보고서 + 부록 시나리오 JSON |
| `bottom_up` | 데이터 이상징후 분석 | 통계 도구·점검 질의로 이상 신호를 찾고, 이상징후 패턴(P-101 ~ P-141) 가설을 데이터로 판정한다 | 보고서 + 부록 시나리오 JSON |

`t2s`, `top_down`, `bottom_up` 은 서로 이력이 따로인 브랜치이며, 브랜치 루트가 곧 프로젝트 루트다. 각 브랜치 설명은 그 브랜치의 `.github/README.md` 에 있다.

## 프로젝트 구조

```
AGENTS.md      규약 (system prompt 로 읽힘)
skills/        sql-query (+ scenario-design 또는 data-investigation)
sub-agents/    term-grounding (+ scenario-worker 또는 stat-screener, hypothesis-worker)
wiki/          패턴·기준 문서 (top_down, bottom_up 만)
okf/           OKF 번들
```

## 쓰는 법

1. 프로젝트 브랜치를 받아 루트 폴더를 zip 으로 묶어 agent studio 에 등록한다. `.github/` 폴더는 빼도 된다.
2. `AGENTS.md` 6절 접속 URL 의 `<PASSWORD>` 를 실제 비밀번호(URL 인코딩, 예: `!` → `%21`)로 바꾼다. 저장소에는 비밀번호를 올리지 않는다.
3. OKF 를 새로 받으면 [OKF.md](OKF.md) 의 업데이트 절차를 따른다.

## 도구

- `tools/add_table_type.py`: 도메인 page 「## 테이블 목록」에 「유형 (table_type)」 칸을 넣는다. 사용법은 OKF.md.
