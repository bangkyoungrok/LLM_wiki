---
type: index
id: index
status: 자동 생성
updated_at: 2026-10-21
---
# 데이터 이상징후 탐색 wiki (Bottom-up)

Bottom-up agent 가 가장 먼저 읽는 진입 색인이다. 이 wiki 는 시나리오를 먼저 정하는 재료가 아니라 탐색과 해석 자료다. agent 는 OKF 번들(`okf/`)로 질의를 쓰고, 통계 도구와 이상징후 점검 질의로 데이터에서 이상 신호를 먼저 찾고, 신호를 데이터 이상징후 패턴에 대응시켜 가설을 세우고, 이 wiki 로 해석하고 고른다.

## 해석 자료

| 경로 | 쓰는 때 |
|---|---|
| [데이터 이상징후 패턴 목록](wiki/patterns/index.md) | 탐지 결과 → 패턴 대응(1절), 패턴 목록(2절), 조합 규칙(3절) |
| `wiki/patterns/anomaly/*.md` | 41개 패턴의 정의 전체와 Bottom-up 에서 쓰는 법(점검 질의 열 조건, OKF 에서 찾는 곳, 자주 묶이는 패턴). 기법 분류별 8개 파일 |
| [위험 해석](wiki/risk-interpretation.md) | 가설 → 감사 위험, 경영진 주장, 위험 구분(부정 의심·오류 의심) |
| [정상 업무 패턴](wiki/normal-patterns.md) | 정상 업무(2절)와 데이터 특성(1절). 반박·재분류의 근거와 제외 조건 |
| [선별 기준](wiki/criteria.md) | 확인된 가설의 순위 |
| [통계 도구 사용법과 탐색 관점](skills/data-investigation/references/stat-views.md) | 관점별 도구(6절), 인자와 판정 조건 |
| [도구 결과 읽기](skills/data-investigation/references/result-reading.md) | 통계 도구 결과 → 이상 목록 |

부정 패턴(P-001 ~ P-032)은 Top-down agent 가 쓰며 이 wiki 에는 없다.

## 지도 (OKF 번들)

| 경로 | 쓰는 때 |
|---|---|
| [도메인 목록](okf/domains/index.md) | 범위를 도메인에 대응시킬 때. 도메인 page 에 프로세스와 핵심 테이블 |
| [APPADAMSUSER 목차](okf/schemas/APPADAMSUSER/index.md) | 업무 데이터. `## transaction` 분류가 탐색 대상 거래 테이블 |
| [SETADAMSUSER 목차](okf/schemas/SETADAMSUSER/index.md) | 감사 메타(시나리오·결과·점수·공통코드) |
| [용어집](okf/glossary/index.md) | 업무 표현 ↔ 컬럼 |
| [조인 목차](okf/joins/index.md) | 허브 테이블, 직접 조인 금지 목록 |
| [코드](okf/codes/index.md), [코드값 샘플](okf/references/code-value-samples.md) | 코드값·플래그 값(Y/N vs 0/1) |
| [날짜 규칙](okf/t2s/rules/date-handling.md), [soft-delete·유효기간](okf/t2s/rules/soft-delete-validity.md), [PII](okf/t2s/rules/pii.md), [결과 해석](okf/t2s/rules/result-interpretation.md) | 날짜, soft-delete, PII, 0행·VPD 해석. 실행·행 제한·이름·조인 규칙은 `sql-query` skill |
| [그레인 실측](okf/references/grain-samples.md) | 1행 단위와 업무 키(분석 단위, key_columns), near_key(중복 적재) |

도메인 대응(요청 표현 → OKF 도메인): 매출·판매·빌링·출고·반품 → `sales` / 마케팅비·프로모션·판촉·인센티브·EO → `mkt-exp` / 입찰·견적·발주·계약·입고 → `bid-qt` / MRO → `mro` / 업체·벤더 → `vendor`, `om-vendor` / 인사·임직원 → `hr` / 재무·회사코드·환율 → `fin-org`, `fin-master` / 사용자·IP·사이트 → `master-bqms`

거래 테이블 고르기: 도메인 page 의 핵심 테이블 가운데 테이블 문서 frontmatter 의 `table_class: transaction`(태그 `class:transaction`)이고 `has:amount` 가 있는 테이블을 먼저 고른다. 기준 날짜 컬럼과 형식은 테이블 문서의 `# Schema`·`# T2S 힌트`로 정한다.
