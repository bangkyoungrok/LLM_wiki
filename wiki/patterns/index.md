---
type: index
id: patterns
status: 자동 생성
source: patterns_73_2.json (부정 32건)
updated_at: 2026-10-21
---
# 부정 패턴 목록 (32) — Top-down

Top-down agent 가 신규 시나리오를 만들 때 OKF 스키마에 대입하는 부정 패턴 목록이다. 패턴 page(`wiki/patterns/fraud/P-0xx.md`)마다 설명, 수법, 탐지 방법, ACFE·COSO 근거, 탐지 기법(SQL 형태), 원본 질의 골격, OKF 대입 힌트, 조합 단서가 있다.

## 1. Top-down 에서의 쓰임

**부정**(P-001 ~ P-032)은 고의로 규정·통제를 어기고 숨긴 행위다(ACFE 부정 유형). Top-down 은 데이터를 탐색하지 않고, 부정 패턴을 OKF 스키마에 대입하고 같은 점검 대상에 함께 걸 수 있는 부정 패턴 2~3개를 묶어 시나리오 후보를 만든다.

1. 선택(scenario-design 2단계): 범위 도메인에 맞고 「SQL 대입」이 「가능」인 패턴을 고른다.
2. 대입과 조합(3단계, 문서만): 패턴마다 필요한 테이블을 OKF 에서 찾고, 4절 규칙과 5절 조합 단서로 2~3개씩 묶는다.
3. 시험(4~5단계, scenario-worker): 조합 점검 질의 1회로 조합이 실행되고 해당 건이 있는지 본다.
4. 답변: 시나리오마다 「부정 패턴 조합」 줄에 묶은 패턴을 적는다(`AGENTS.md` 9절).

- 오탐이 사람 지목으로 이어지므로 정상 업무 제외를 반드시 넣고, 2절의 고의성 신호를 예외 조건에 넣는다. 조합은 그 자체로 고의성 신호(같은 행위자 반복, 사후 변경 등)를 강하게 만든다.
- 부실 패턴(P-101 ~ P-141, 과실·데이터 오류)은 Bottom-up agent 가 데이터 탐색 결과를 해석할 때 쓰며 이 프로젝트에는 없다. 패턴 page 의 「탐지 기법(SQL 형태)」 줄은 원본의 기법 분류와 SQL 골격만 옮긴 것이다.
- 원본 `sql_core` 가 「불가능(그래프 관계 분석 필요)」인 패턴(P-007, P-024)은 이 환경(KG 없음)에서 대입하지 않는다.
- 원본 P-002, P-004, P-005, P-006 의 `sql_core` 에는 SQL 이 아닌 SPARQL 이 들어 있다. SQL 골격으로 쓰지 않는다.

## 2. 부정 시나리오의 고의성 신호

부정 패턴을 대입할 때는 아래 가운데 OKF 컬럼으로 표현할 수 있는 신호를 하나 이상 예외 조건에 넣고, 넣은 신호를 「데이터 해석 가정」에 적는다. 넣을 수 없으면 위험 연결 점수를 1점으로 둔다(`wiki/criteria.md`).

| 신호 | 예외 조건의 예 |
|---|---|
| 같은 행위자 반복 | 같은 담당자·업체·거래선 조합이 기간 안에 2회 이상 |
| 통제 회피 | 승인 기준 바로 아래 금액·할인율, 결재 없이 처리, 수의·단수 견적 |
| 시점 조작 | 기간 말 며칠 집중, 마감 뒤 변경·취소, 승인 전 실행 |
| 사후 변경 | 선정·계약 뒤 단가·금액·조건 변경, 기준일·마감시각 변경 |
| 은폐 흔적 | 사유 없는 취소·정정, Dummy 코드, 증빙 번호 재사용 |

## 3. 부정 패턴 (P-001 ~ P-032)

| ID | 이름 | ACFE | 탐지 기법(원본 분류) | OKF 후보 도메인 | SQL 대입 | 비고 |
|---|---|---|---|---|---|---|
| [P-001](wiki/patterns/fraud/P-001.md) | 인센티브 조작 | Revenue Recognition Fraud, Rebate… | 값 불일치, 임계 초과, 추세·분포 | mkt-exp, sales | 가능 | 대입 예시 |
| [P-002](wiki/patterns/fraud/P-002.md) | 사외펀드(Slush Fund) 조성 | Cash Disbursements Fraud (Slush Fu… | 임계 초과, 중복·동일인, 추세·분포 | mkt-exp | 가능 | |
| [P-003](wiki/patterns/fraud/P-003.md) | 가짜 벤더 / 유령회사 | Vendor Overbilling (Fake Vendor, S… | 값 불일치, 중복·동일인, 관계 그래프 | vendor, om-vendor, bid-qt | 가능 | 대입 예시 |
| [P-004](wiki/patterns/fraud/P-004.md) | 영수증/송장 위조 및 중복 청구 | Expense Reimbursement Fraud (Forge… | 중복·동일인, 형식·값 이상 | mkt-exp, fin-master | 가능 | |
| [P-005](wiki/patterns/fraud/P-005.md) | 제품 유출 및 무단 재판매 | Inventory Theft (Employee Discount… | 중복·동일인, 관계 그래프 | sales | 가능 | |
| [P-006](wiki/patterns/fraud/P-006.md) | 지급 채널 가로채기 | Wire Transfer Fraud (Payment Diver… | 값 불일치, 누락·부재 | vendor, om-vendor | 가능 | |
| [P-007](wiki/patterns/fraud/P-007.md) | 이해관계 충돌 / 자기거래 | Conflict of Interest (Self-Dealing… | 관계 그래프 | hr, vendor | 불가(그래프) | |
| [P-008](wiki/patterns/fraud/P-008.md) | 시스템 제어 우회 | Cash Disbursements Fraud (Return P… | 값 불일치, 시간·순서, 누락·부재 | bid-qt, sales | 가능 | 대입 예시 |
| [P-009](wiki/patterns/fraud/P-009.md) | 예산 편법 사용 및 크로스 차징 | Expense Reimbursement Fraud (Budge… | 임계 초과, 누락·부재 | mkt-exp | 가능 | |
| [P-010](wiki/patterns/fraud/P-010.md) | 과실 기반 부정 | Negligence (Failure to Verify, Ove… | 누락·부재 | mkt-exp | 가능 | |
| [P-011](wiki/patterns/fraud/P-011.md) | 계정 및 자격증명 공유 | Digital Asset Misuse (Account Shar… | 중복·동일인, 형식·값 이상 | bid-qt, master-bqms | 가능 | 대입 예시 |
| [P-012](wiki/patterns/fraud/P-012.md) | 보증 및 서비스 시스템 남용 | Customer Refund Fraud (Warranty Ab… | 임계 초과, 누락·부재 | 없음 | 도메인 없음 | |
| [P-013](wiki/patterns/fraud/P-013.md) | 생산 데이터 조작 | Revenue Recognition Fraud (Fake Pr… | 값 불일치, 임계 초과, 추세·분포 | 없음 | 도메인 없음 | |
| [P-014](wiki/patterns/fraud/P-014.md) | 입찰 및 가격 조작 | Vendor Overbilling (Bid Rigging, P… | 값 불일치, 임계 초과 | bid-qt, mro | 가능 | |
| [P-015](wiki/patterns/fraud/P-015.md) | 개발 IP 및 자원 유출 | Intellectual Property Theft (R&D I… | 중복·동일인, 형식·값 이상 | 없음 | 도메인 없음 | |
| [P-016](wiki/patterns/fraud/P-016.md) | 물류 재고 및 배송 조작 | Inventory Fraud (Fake Shipping, In… | 값 불일치, 시간·순서, 추세·분포 | sales, bid-qt | 가능 | |
| [P-017](wiki/patterns/fraud/P-017.md) | 서비스 보증 및 부품 남용 | Customer Refund Fraud (Warranty Pa… | 임계 초과, 누락·부재 | 없음 | 도메인 없음 | |
| [P-018](wiki/patterns/fraud/P-018.md) | 재무 및 인사 부정 | Expense Reimbursement Fraud, Vendo… | 값 불일치, 중복·동일인, 임계 초과, 누락·부재 | hr, fin-master | 가능 | |
| [P-019](wiki/patterns/fraud/P-019.md) | 현금 가로채기(Skimming) | Skimming (1-1) | 절대 임계 초과 | sales | 가능 | |
| [P-020](wiki/patterns/fraud/P-020.md) | 급여 부정 | Payroll Fraud (1-1), Ghost Promote… | 테이블간 조인 불일치 | hr | 가능 | |
| [P-021](wiki/patterns/fraud/P-021.md) | 재고 기록 조작 | Inventory Fraud (1-2) | 통계적 임계 초과 | sales | 가능 | |
| [P-022](wiki/patterns/fraud/P-022.md) | 부품 대체 | Counterfeit Parts (1-2) | 필드간 값 불일치 | 없음 | 도메인 없음 | |
| [P-023](wiki/patterns/fraud/P-023.md) | 자산 처분 부정 | Asset Disposal Fraud (1-4) | 절대 임계 초과 | fin-master | 가능 | |
| [P-024](wiki/patterns/fraud/P-024.md) | 미공개 이해관계 충돌 | Undisclosed Conflicts (2) | 이해관계 탐지 | hr, vendor | 불가(그래프) | |
| [P-025](wiki/patterns/fraud/P-025.md) | 협박/강요 | Extortion (2) | 절대 임계 초과 | 없음 | 도메인 없음 | |
| [P-026](wiki/patterns/fraud/P-026.md) | 채널 스투핑 | Revenue Recognition Fraud (3) | 누적 임계 초과 | sales | 가능 | 대입 예시 |
| [P-027](wiki/patterns/fraud/P-027.md) | 허위 출고 | Revenue Recognition Fraud (3) | 테이블간 조인 불일치 | sales, bid-qt | 가능 | 대입 예시 |
| [P-028](wiki/patterns/fraud/P-028.md) | 매출 Inflation | Revenue Recognition Fraud (3) | 절대 임계 초과 | sales | 가능 | 대입 예시 |
| [P-029](wiki/patterns/fraud/P-029.md) | Accrual 조작 | Period End Manipulation (3) | 비율 임계 초과 | mkt-exp, fin-master | 가능 | |
| [P-030](wiki/patterns/fraud/P-030.md) | 고객 환불 부정 | Customer Refund Fraud (1-1) | 기간 역전 | sales | 가능 | 대입 예시 |
| [P-031](wiki/patterns/fraud/P-031.md) | 수표/송금 위조 | Check Tampering (1-1) | 필수 필드 NULL | fin-master | 가능 | |
| [P-032](wiki/patterns/fraud/P-032.md) | 경비 현금 부정 | Petty Cash Fraud (1-1) | 절대 임계 초과 | fin-master, hr | 가능 | |

- 「SQL 대입」 칸: 가능 = OKF 에 대입할 후보 도메인이 있음, 도메인 없음 = OKF 도메인 11종에 해당 업무가 없어 목차에서 테이블을 찾지 못하면 만들지 않은 후보, 불가(그래프) = 이 환경에서 대입하지 않음. 「도메인 없음」·「불가(그래프)」 패턴은 조합에 넣지 않는다.
- 「비고」의 대입 예시 = 감사 wiki 기본안의 모집단·예외·정상 업무 제외 예시가 page 에 있음. 「탐지 기법」은 원본 Anomaly_Patterns 의 기법 분류이며, 패턴 page 의 「탐지 기법(SQL 형태)」 줄에 SQL 골격이 있다.

## 4. 조합 규칙

조합은 **같은 점검 대상**(같은 거래 행, 같은 행위자, 또는 업무 흐름으로 이어지는 거래)에 함께 걸 수 있는 부정 패턴 2~3개다. 조합 하나가 시나리오 후보 하나가 된다. 유형 이름은 Bottom-up 의 부실 패턴 조합과 같다.

| 유형 | 성립하는 때 | 예외 조건(시나리오 SQL) 쓰는 법 | 예 |
|---|---|---|---|
| 같은 행 | 두 패턴의 예외 조건을 같은 테이블의 같은 업무 키 행에 함께 걸 수 있음 | `<조각 A> AND <조각 B>` | P-014 입찰 조작(최저가 미선정) + P-011 자격증명 공유(같은 제출 IP) |
| 집단→행 | 한 패턴의 신호가 행위자(업체, 거래선, 담당자) 단위로 정의되고, 그 행위자의 거래에 다른 패턴의 조건을 걸 수 있음 | `<행 조각> AND t.<행위자> IN (SELECT s.<행위자> FROM <query_name> s WHERE <같은 기간 조건> AND <행위자 조각>)` 또는 `GROUP BY … HAVING` 꼴 | P-003 가짜 벤더(새로 등록된 업체) + P-014 입찰 조작(단수 견적 선정) |
| 흐름→행 | 앞 패턴의 거래가 업무 흐름의 다음 단계(조인 문서로 이어지는 테이블)에서 뒤 패턴의 거래로 이어짐 | `<조각 A> AND EXISTS (SELECT 1 FROM <다음 단계 query_name> n WHERE <조인 조건> AND <조각 B>)` (짝이 없어야 하는 조건이면 `NOT EXISTS`) | P-027 허위 출고(출고 없는 청구) + P-030 고객 환불 부정(그 청구의 정정·반품) |

- 조합의 패턴은 모두 「SQL 대입」이 「가능」이고, 후보 도메인이 서로 겹치거나 조인 문서로 이어지는 도메인이어야 한다.
- 조각마다 근거 테이블·컬럼이 OKF 테이블 문서에 있어야 한다. 흐름→행의 조인은 조인 문서(`usable: true`·`conditional`)나 `sql-query` 「조인」 절 2단계 실측을 통과한 것만 쓴다.
- 조합의 패턴은 최대 3개다. 5절 조합 단서에 없는 조합도 위 규칙을 지키면 만들 수 있다.
- 성립 확인: scenario-worker 의 조합 점검 질의에서 조합 조건을 함께 충족하는 건(`HIT_CNT`)이 0 보다 커야 한다. 0 이면 worker 가 조합을 줄인다(주 패턴만 남김). 줄여서 1개가 남으면 「단일」이다.
- 단일 패턴 후보: 묶을 상대가 없는 패턴은 「단일」로 둘 수 있다. 조합 후보가 요청 건수보다 적을 때만 선별에 넣고, 선별 기준의 위험 연결은 1점이다(`wiki/criteria.md`).
- 기존 시나리오(`okf/references/scenarios.md`)와 감사 포인트가 같은 조합은 만들지 않는다. 조합의 한 패턴이 기존 시나리오와 같아도, 다른 패턴이 탐지 조건을 바꾸면 만들 수 있다(데이터 해석 가정에 기존 시나리오 이름을 적는다).

## 5. 조합 단서 (자동 생성)

업무 흐름과 수법이 이어져 함께 묶기 쉬운 쌍이다. 대입할 테이블·컬럼·조인이 OKF 에 있는지는 패턴마다 확인한다. 패턴 page 의 「조합 단서」 절에도 같은 내용이 있다.

| 조합 | 유형 | 도메인 | 함께 보는 점검 대상 |
|---|---|---|---|
| [P-027](wiki/patterns/fraud/P-027.md) 허위 출고 + [P-030](wiki/patterns/fraud/P-030.md) 고객 환불 부정 | 흐름→행 | sales | 출고 없이 잡은 청구를 뒤에 정정·반품으로 되돌린 거래 |
| [P-026](wiki/patterns/fraud/P-026.md) 채널 스투핑 + [P-030](wiki/patterns/fraud/P-030.md) 고객 환불 부정 | 흐름→행 | sales | 기간 말에 몰아 낸 출고·청구가 다음 기간 초 반품·정정된 거래 |
| [P-026](wiki/patterns/fraud/P-026.md) 채널 스투핑 + [P-028](wiki/patterns/fraud/P-028.md) 매출 Inflation | 같은 행 | sales | 기간 말 며칠에 몰린 대량 청구가 마감 뒤 취소된 실적 |
| [P-027](wiki/patterns/fraud/P-027.md) 허위 출고 + [P-016](wiki/patterns/fraud/P-016.md) 물류 재고 및 배송 조작 | 흐름→행 | sales, bid-qt | 출고·입고 기록이 서로 맞지 않는 청구·배송 건 |
| [P-001](wiki/patterns/fraud/P-001.md) 인센티브 조작 + [P-026](wiki/patterns/fraud/P-026.md) 채널 스투핑 | 집단→행 | mkt-exp, sales | 셀인을 부풀린 거래선에 지급된 셀아웃 인센티브 |
| [P-001](wiki/patterns/fraud/P-001.md) 인센티브 조작 + [P-004](wiki/patterns/fraud/P-004.md) 영수증/송장 위조 및 중복 청구 | 같은 행 | mkt-exp | 같은 프로모션 인센티브가 같은 증빙으로 다시 청구된 건 |
| [P-002](wiki/patterns/fraud/P-002.md) 사외펀드(Slush Fund) 조성 + [P-009](wiki/patterns/fraud/P-009.md) 예산 편법 사용 및 크로스 차징 | 같은 행 | mkt-exp | 행사 비용이 행사와 다른 예산 조직(MBO)으로 처리된 건 |
| [P-002](wiki/patterns/fraud/P-002.md) 사외펀드(Slush Fund) 조성 + [P-010](wiki/patterns/fraud/P-010.md) 과실 기반 부정 | 같은 행 | mkt-exp | 행사 결과 확인·예산 승인 없이 지급된 행사 비용 |
| [P-009](wiki/patterns/fraud/P-009.md) 예산 편법 사용 및 크로스 차징 + [P-029](wiki/patterns/fraud/P-029.md) Accrual 조작 | 같은 행 | mkt-exp, fin-master | 기간 말 남은 예산을 충당·이월로 돌린 지급 |
| [P-003](wiki/patterns/fraud/P-003.md) 가짜 벤더 / 유령회사 + [P-014](wiki/patterns/fraud/P-014.md) 입찰 및 가격 조작 | 집단→행 | vendor, bid-qt | 새로 등록된 업체가 단수·수의 견적으로 선정된 건 |
| [P-003](wiki/patterns/fraud/P-003.md) 가짜 벤더 / 유령회사 + [P-006](wiki/patterns/fraud/P-006.md) 지급 채널 가로채기 | 집단→행 | vendor, om-vendor | 새로 등록된 업체의 지급 정보가 곧 바뀐 건(변경 이력 테이블이 있을 때) |
| [P-014](wiki/patterns/fraud/P-014.md) 입찰 및 가격 조작 + [P-011](wiki/patterns/fraud/P-011.md) 계정 및 자격증명 공유 | 같은 행 | bid-qt | 최저가·평가 1위가 아닌 업체가 선정됐고, 그 견적에 다른 업체와 같은 제출 정보(IP 등)가 있는 건 |
| [P-014](wiki/patterns/fraud/P-014.md) 입찰 및 가격 조작 + [P-008](wiki/patterns/fraud/P-008.md) 시스템 제어 우회 | 흐름→행 | bid-qt | 선정 뒤 계약 단가·조건이 바뀐 건 |
| [P-018](wiki/patterns/fraud/P-018.md) 재무 및 인사 부정 + [P-032](wiki/patterns/fraud/P-032.md) 경비 현금 부정 | 같은 행 | fin-master, hr | 같은 임직원의 경비 청구가 기준을 넘고 반복된 건 |
