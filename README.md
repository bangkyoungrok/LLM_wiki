# LLM_wiki

감사 에이전트용 LLM Wiki 저장소다. 에이전트가 읽는 지침(AGENTS), 기술(skills), sub-agent 정의를 조직별 브랜치에 나눠 둔다. 이 `main` 브랜치에는 소개 글만 둔다.

## 브랜치

| 브랜치 | 내용 |
|---|---|
| `DX/okf` | DX 부문 OKF 기준 Wiki |
| `DS/okf` | DS 부문 OKF 기준 Wiki |

두 브랜치는 같은 구조와 같은 규칙으로 쓰였다. 다른 것은 OKF 차이에서 오는 부분(스키마, 용어집·보조 자료 설명, 코드마스터, 기존 시나리오 뷰 등)뿐이다.

## 각 브랜치의 구성

```
AGENTS.md          full 판 지침 (시나리오 생성·검증·데이터 질문)
AGENTS-t2s.md      t2s 판 지침 (데이터 질문만)
README.md          브랜치 안내
skills/            기술
sub-agents/        sub-agent 정의
```

자세한 사용법은 각 브랜치의 `README.md` 에 있다.