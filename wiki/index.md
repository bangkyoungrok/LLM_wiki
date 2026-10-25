---
type: index
id: index
status: 자동 생성
updated_at: 2026-10-21
---
# 감사 시나리오 wiki (Top-down)

Top-down agent 가 가장 먼저 읽는 진입 색인이다. agent 는 부정 패턴을 고르고, OKF 번들(`okf/`)의 스키마에 대입하고, 같은 점검 대상에 함께 걸 수 있는 부정 패턴을 묶어 시나리오 SQL 을 쓰고, `sql_run` 으로 실행 가능성과 건수를 확인한 뒤, 통과한 시나리오를 정해진 형식으로 낸다. 데이터 이상을 찾는 탐색 집계는 하지 않는다(Bottom-up 의 일).

## 위험 패턴

- [패턴 목록](wiki/patterns/index.md): 부정 32건(P-001 ~ P-032, 고의). 고의성 신호, 패턴별 OKF 후보 도메인과 SQL 대입 가능 여부, 조합 규칙(같은 행, 집단→행, 흐름→행), 조합 단서
- 부정 패턴 page: `wiki/patterns/fraud/P-0xx.md`
- 데이터 이상징후 패턴(P-101 ~ P-141)은 Bottom-up agent 가 쓰며 이 wiki 에는 없다

## 스키마 (OKF 번들)

| 경로 | 쓰는 때 |
|---|---|
| [도메인 목록](okf/domains/index.md) | 요청 범위(매출, 마케팅비, 입찰·견적 등)를 도메인에 대응시킬 때. 도메인 page 에 프로세스와 핵심 테이블 |
| [APPADAMSUSER 목차](okf/schemas/APPADAMSUSER/index.md) | 업무 데이터 후보 테이블 고르기 |
| [SETADAMSUSER 목차](okf/schemas/SETADAMSUSER/index.md) | 감사 메타(시나리오·결과·점수·공통코드) |
| [용어집](okf/glossary/index.md) | 업무 표현 ↔ 컬럼 |
| [조인 목차](okf/joins/index.md) | 허브 테이블, 직접 조인 금지 목록 |
| [코드](okf/codes/index.md), [코드값 샘플](okf/references/code-value-samples.md) | 코드값·플래그 값 |
| [날짜 규칙](okf/t2s/rules/date-handling.md), [soft-delete·유효기간](okf/t2s/rules/soft-delete-validity.md), [PII](okf/t2s/rules/pii.md), [결과 해석](okf/t2s/rules/result-interpretation.md) | 날짜, soft-delete, PII, 0행·VPD 해석. 실행·행 제한·이름·조인 규칙은 `sql-query` skill |
| [그레인 실측](okf/references/grain-samples.md) | 테이블 1행 단위와 업무 키(시나리오 key_columns) |

도메인 대응(요청 표현 → OKF 도메인): 매출·판매·빌링·출고·반품 → `sales` / 마케팅비·프로모션·판촉·인센티브·EO → `mkt-exp` / 입찰·견적·발주·계약·입고 → `bid-qt` / MRO → `mro` / 업체·벤더 → `vendor`, `om-vendor` / 인사·임직원 → `hr` / 재무·회사코드·환율 → `fin-org`, `fin-master` / 사용자·IP·사이트 → `master-bqms`

## 형식과 참고

- [이전 시나리오](wiki/examples/index.md): 기존 시나리오(중복 회피, 대입 단서), 승인된 질문-SQL 예제(SQL 문체 견본)
- [외부 참고 자료](wiki/external/index.md): ACFE 부정 유형, COSO 통제 코드
- [정상 업무 패턴](wiki/normal-patterns.md): 정상 업무 제외 조건
- [선별 기준](wiki/criteria.md): 후보 점수
