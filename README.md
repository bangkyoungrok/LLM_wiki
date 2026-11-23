# 감사 질문 생성 Agent Wiki

시나리오 생성 에이전트에 넣을 감사 질문 1건, 또는 드릴다운 질문 1건을 만드는 에이전트의 Wiki 다. 지침(`AGENTS.md`), 기술(`skills/`), sub-agent 정의(`sub-agents/`), 이 에이전트가 쓰는 OKF 문서 일부(`okf/`)를 담는다.

## 모드

| 모드 | 하는 일 | 따르는 파일 |
|---|---|---|
| `top-down` | 부정 패턴·실제 사고에서 질문을 만든다 | `skills/question-generation/SKILL.md` |
| `bottom-up` | 테이블 구조에서 질문을 만든다 | `skills/question-generation/SKILL.md` |
| `variant` | 기존 시나리오 1건을 바꿔 질문을 만든다 | `skills/question-generation/references/variant.md` |
| `drilldown` | 검증을 통과한 시나리오를 더 좁힐지 정하고 드릴다운 질문을 만든다 | `skills/question-generation/SKILL.md` 「drilldown」 절 |

## 구성

```
AGENTS.md                                  지침
skills/question-generation/                질문 만들기 skill
sub-agents/question-scout/                 top-down 후보 모으기
sub-agents/question-table-scout/           bottom-up 후보 모으기
sub-agents/question-grounder/              고른 후보 확인
okf/wiki/scenario/summary.md               variant 에서 기존 시나리오를 고르는 목록
okf/wiki/patterns/index.md                 패턴 목차
okf/wiki/patterns/perspective/             드릴다운 패턴(DP-001~DP-022)
```

이 브랜치의 `okf/` 에는 위 파일만 있다. 나머지 OKF 문서(`okf/wiki/scenario/<ID>.md` 등)는 실행 환경에 있는 것을 쓴다.

## 고칠 때

- 파일 경로는 맨 위 폴더부터 쓴다. 예: `skills/question-generation/SKILL.md`, `okf/wiki/normal-patterns.md`
- 상한은 `AGENTS.md` 「상한」 표에만 쓴다.
- 출력 JSON 은 시나리오 생성 에이전트(`DX/okf` 브랜치)의 입력이다. 키를 바꾸면 그쪽도 함께 확인한다.