# 감사 에이전트 Wiki

감사 에이전트가 읽는 지침(AGENTS), 기술(skills), sub-agent 정의, 도메인 정보(`domain_knowledge/`)를 담는다. OKF 문서(`okf/`)는 이 브랜치에 없고, 실행 환경에 있는 것을 쓴다.

## 두 가지 판

같은 skill·sub-agent 파일을 쓰고, 에이전트 파일만 다르다.

| 판 | 에이전트 파일 | 하는 일 |
|---|---|---|
| full | `AGENTS.md` | 감사 시나리오 생성(Top-down·Bottom-up), 시나리오 검증, 데이터 질문 답변 |
| t2s | `AGENTS-t2s.md` | 데이터 질문 답변만 (조회·집계·목록·구조) |

## 구성

| 경로 | full | t2s |
|---|:---:|:---:|
| `domain_knowledge/` | ✓ | ✓ |
| `skills/sql-query/` | ✓ | ✓ |
| `sub-agents/schema-linker/` | ✓ | ✓ |
| `sub-agents/term-grounding/` | ✓ | ✓ |
| `skills/topdown-scenario-generation/` | ✓ | |
| `skills/bottomup-scenario-generation/` | ✓ | |
| `skills/scenario-validation/` | ✓ | |
| `skills/audit-report/` | ✓ | |
| `sub-agents/topdown-hypothesizer/` | ✓ | |
| `sub-agents/bottomup-anomaly-explorer/` | ✓ | |

## 쓰는 법

- full: 이 브랜치 전체와 `AGENTS.md` 를 쓴다.
- t2s: 위 표에서 t2s 에 표시된 폴더와 `AGENTS-t2s.md` 만 가져간다. 실행 환경이 `AGENTS.md` 라는 이름만 읽으면 `AGENTS-t2s.md` 의 이름을 `AGENTS.md` 로 바꾼다.

## 고칠 때

- 두 판이 함께 쓰는 파일(`domain_knowledge/`, `skills/sql-query/`, `sub-agents/schema-linker/`, `sub-agents/term-grounding/`)은 한 번 고치면 두 판에 똑같이 적용된다.
- 판마다 다른 내용은 `AGENTS.md` 와 `AGENTS-t2s.md` 에만 쓴다.
- `skills/sql-query/SKILL.md` 의 시나리오 SQL 절은 full 에서만 쓴다. t2s 에서는 읽히지 않는다.
- 파일 경로는 맨 위 폴더부터 쓴다. 예: `skills/sql-query/SKILL.md`, `sub-agents/schema-linker/SKILL.md`, `okf/wiki/normal-patterns.md`