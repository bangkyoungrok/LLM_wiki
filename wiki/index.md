---
type: index
id: index
status: 자동 생성
updated_at: 2026-10-22
---
# 시나리오 변형 wiki

시나리오 변형 agent 가 가장 먼저 읽는 진입 색인이다. agent 는 원본 시나리오를 감사 골격으로 나누고, OKF 번들(`okf/`)로 변형 대상(테이블·도메인·조건)을 찾아 변형 시나리오를 설계하고, 데이터로 확인한 뒤 이 wiki 로 해석하고 점수를 매긴다. 새 위험을 고르거나 데이터에서 새 이상을 찾지 않는다.

## 원본 찾기

| 입력 | 보는 곳 |
|---|---|
| 기존 시나리오 목록의 이름 | [기존 시나리오 목록](okf/references/scenarios.md)(있을 때): 시나리오 이름, 프로시저, 감사 포인트, 참조 테이블. SQL 전문은 없다 |
| 같은 시나리오의 검증 SQL | `okf/t2s/examples/` 폴더의 예제 문서(있을 때). 같은 감사 포인트의 예제가 있으면 그 SQL 을 원본으로 쓴다 |
| JSON·자연어 | 입력 자체. 테이블·컬럼은 OKF 테이블 문서로 확인 |

## 해석 자료

| 경로 | 쓰는 때 |
|---|---|
| [데이터 이상징후 패턴 목록](wiki/patterns/index.md) | 원본·변형 조각에 패턴 붙이기(2·3절), 조합 규칙(4절) |
| `wiki/patterns/anomaly/*.md` | 데이터 이상징후 패턴 41건(기법 분류별 8개 파일): 점검 질의 열 조건, OKF 에서 찾는 곳, 자주 묶이는 패턴 |
| [위험 해석](wiki/risk-interpretation.md) | 원본·변형 → 감사 위험, 경영진 주장, 위험 구분(부정 의심·오류 의심) |
| [정상 업무 패턴](wiki/normal-patterns.md) | 정상 업무(2절)와 데이터 특성(1절). 반박·재분류의 근거와 제외 조건 |
| [감사 가치 점수](wiki/criteria.md) | 원본과 변형의 점수(위험 연결, 영향 규모, 탐지 가능성, 원본과의 차이) |
| [변형 유형](skills/scenario-variation/references/variation-types.md) | 감사 골격, 변형 유형 5종, 유형 고르기, 후보 기록 형식 |
| [통계 도구 사용법](skills/scenario-variation/references/stat-views.md), [도구 결과 읽기](skills/scenario-variation/references/result-reading.md) | 변형 조각에 통계 경계가 필요할 때 |

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
