---
type: index
id: patterns
status: 자동 생성(드릴다운 행은 수동 추가)
source: patterns_73_2.json, 드릴다운 패턴(okf/wiki/patterns/perspective/index.md)
updated_at: 2026-11-21
---
# 패턴 허브

감사 패턴은 세 종류이며 모드마다 한 종류만 쓴다. 자기 모드의 목록으로 바로 간다.

| 종류 | 뜻 | 쓰는 모드 | 목록 | 상세 |
|---|---|---|---|---|
| 부정 패턴 (P-001 ~ P-032, 32건) | 고의로 규정·통제를 어기고 숨긴 행위(ACFE 부정 유형) | Top-down | [부정 패턴 목록](okf/wiki/patterns/fraud/index.md): 고의성 신호(2절), 목록(3절), 조합 규칙(4절), 조합 단서(5절) | 패턴 page `okf/wiki/patterns/fraud/P-0xx.md` |
| 데이터 이상징후 패턴 (P-101 ~ P-141) | 데이터에 남는 이상 신호. 실수·누락·고의 모두 원인일 수 있음 | Bottom-up | [데이터 이상징후 패턴 목록](okf/wiki/patterns/anomaly/index.md): 모드별 쓰임(1절), 대응표(2절), 목록(3절), 조합 규칙(4절) | 패턴 파일 `okf/wiki/patterns/anomaly/P-1xx.md` 41개 |
| 드릴다운 패턴 (DP-001 ~ DP-023, 23건) | 검증을 통과한 시나리오의 결과를 한 단계 더 좁고 깊게 보는 감사 관점 | Drilldown | [드릴다운 패턴 목록](okf/wiki/patterns/perspective/index.md): 쓰임(1절), 사고 유형(2절), 유형 판단(3절), 목록(4절), 묶기 규칙(5절), 대상 범위(6절), 멈춤(7절) | 패턴 파일 `okf/wiki/patterns/perspective/DP-0xx.md` 23개 |

- 조합 유형 이름(같은 행, 집단→행, 흐름→행, 단일)은 부정 패턴과 데이터 이상징후 패턴이 같다. SQL 로 잇는 법은 `skills/scenario-probe/references/writing.md` 3절.
- 패턴 파일의 「이 기법을 쓰는 부정 패턴」 줄과 부정 패턴 page 의 「탐지 기법」 줄은 두 종류를 잇는 참고 정보다. 다른 모드의 패턴을 시나리오에 붙이지 않는다.
- 드릴다운 패턴은 시나리오를 처음 만들 때(Top-down·Bottom-up·variant) 쓰지 않는다. 드릴다운 패턴 파일의 「관련 패턴」 줄은 참고 정보다.
