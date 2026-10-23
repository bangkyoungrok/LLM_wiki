---
type: index
id: patterns
status: 자동 생성
source: patterns_73_2.json (P-101 ~ P-141)
updated_at: 2026-10-21
---
# 데이터 이상징후 패턴 목록 (Bottom-up)

**데이터 이상징후 패턴**(P-101 ~ P-141)은 데이터에 남는 이상 신호의 유형이다. 값이 서로 맞지 않거나, 평소 범위를 넘거나, 순서가 뒤바뀌거나, 같은 기록이 반복되거나, 있어야 할 값이 비어 있는 모습 같은 것이다. 실수, 입력 누락, 관리 소홀로 생길 수도 있고 고의로 생길 수도 있다. 어느 쪽인지는 패턴이 아니라 감사 위험 해석(`wiki/risk-interpretation.md`)과 데이터 확인으로 판단한다.

Bottom-up 은 패턴을 먼저 고르지 않는다. 데이터를 먼저 집계하고, 나온 이상을 이 목록의 패턴에 대응시킨 뒤, 같은 대상에서 함께 나온 패턴을 묶어 가설(시나리오 후보)을 만든다. 부정 패턴(P-001 ~ P-032)은 Top-down agent 가 쓰며 이 wiki 에는 없다.

41개 패턴의 정의 전체(설명, 기법 분류, ACFE, COSO, 이 기법을 쓰는 부정 패턴, 원본 질의 골격, 수법, 탐지 방법)와 Bottom-up 에서 쓰는 법(수준, 탐지 수단, 점검 질의 열 조건, OKF 에서 찾는 곳, 자주 묶이는 패턴)은 기법 분류별 파일 8개(`wiki/patterns/anomaly/*.md`)에 있다. 4단계에서 가설에 쓰는 패턴이 든 분류 파일만 읽는다.

## 1. 탐지 결과 → 데이터 이상징후 패턴 (4단계 대응표)

탐색 결과의 관점·종류·점검 질의 열을 아래 표로 패턴에 대응시킨다. 한 이상이 두 패턴에 대응하면 둘 다 붙인다.

| 탐지 수단 | 결과 (관점, 종류) | 데이터 이상징후 패턴 |
|---|---|---|
| `stat_screen` | 같은 대상의 평소, 같은 조건 안 (B1_RECORD, B2_RECORD, 값 모드) | P-106 통계적 임계 초과. 방향이 상한 초과면 P-109 극단값 탐지도 함께 |
| `stat_screen` | 비율 모드의 개별 값 (B1_RECORD, B2_RECORD, 비율 모드), 동료 대비 비율 (B1_RATIO, B2_RATIO) | P-107 비율 임계 초과 |
| `stat_screen` | 간격 (B1_RECORD, B2_RECORD, 간격 모드) 하한 미만 | P-113 비정상 단축. 대상 값이 음수면 P-111 선후 순서 위반 |
| `stat_screen` | 간격 상한 초과 | P-114 비정상 지연 |
| `stat_screen` | 동료 대비 집중 (B1_GROUP, B2_GROUP) | P-130 집중도 이상 |
| `stat_screen` | 동료 대비 수준, 동료 대비 빈도 (B1_LEVEL, B2_LEVEL, B1_RATE, B2_RATE) | P-129 분포 편차 |
| `stat_screen` | 월별 평소 (B3_MONTH) | P-128 급증/급감 |
| `stat_screen` | 추세 (B5_TREND) | P-127 지속 방향성 변화 |
| `stat_screen` | 첫 자리·첫 두 자리 분포 (B4_BENFORD, B4_BENFORD2), 업무 시간 외 입력 (B1_OFFHOUR, B2_OFFHOUR) | P-129 분포 편차 |
| `find_duplicates` | 완전 중복, 유사 중복 | P-122 완전 중복. key_columns 에 증빙·인보이스 번호가 있으면 P-119 증빙 중복, 업무 키만이면 P-117 식별자 중복 |
| `find_number_gaps` | 결번 / 번호 중복 / 번호 날짜 역전 | P-115 순서 위반 / P-117 식별자 중복 / P-111 선후 순서 위반 |
| `match_tables` | 짝 없음 | P-104 참조 무결성 위반. 대상이 결재·검수·로그 기록이면 P-124 검증 로그 부재 |
| `match_tables` | 금액 불일치 | P-102 테이블간 조인 불일치 |
| 이상징후 점검 질의 (`skills/data-investigation/references/query-writing.md` 7절) | 열 `R_P1xx` 의 전체 비율이 0 보다 큼 | 그 열의 패턴 |
| 차원 쌍 집중 템플릿 (`query-writing.md` 7절, 선택) | top_share 상위 | P-130 집중도 이상 |

- **신호 판정**: 통계 도구가 범위 밖 후보를 냈거나, 규칙 점검에서 위반이 나왔거나, 점검 질의 열의 전체 비율(IS_TOTAL = 1 행)이 0 보다 클 때만 그 패턴에 신호가 있다. 「범위 밖 0건」, 「판정하지 않은 항목」, 전체 비율 0 인 패턴은 신호가 없으며 가설에 넣지 않는다.

## 2. 패턴 목록

41개 전체 목록이다. 수준: **행** = 한 행(업무 키)에서 판정, **집단** = 차원 값(업체, 담당자, 거래선, 월) 단위로 판정, **흐름** = 두 테이블 사이에서 판정, **쓰지 않음** = 이 환경에서 탐지할 수 없음.

| ID | 이름 | 수준 | 탐지 수단 | 분류 파일 |
|---|---|---|---|---|
| P-101 | 필드간 값 불일치 | 행 | 점검 질의 R_P101 | `wiki/patterns/anomaly/value-mismatch.md` |
| P-102 | 테이블간 조인 불일치 | 흐름 | match_tables 금액 불일치 | `wiki/patterns/anomaly/value-mismatch.md` |
| P-103 | 논리적 관계 위반 | 행 | 점검 질의 R_P103 | `wiki/patterns/anomaly/value-mismatch.md` |
| P-104 | 참조 무결성 위반 | 흐름 | match_tables 짝 없음(대상이 마스터·상위 건일 때) | `wiki/patterns/anomaly/value-mismatch.md` |
| P-105 | 절대 임계 초과 | 행 | 점검 질의 R_P105 | `wiki/patterns/anomaly/threshold.md` |
| P-106 | 통계적 임계 초과 | 행 | stat_screen 같은 대상의 평소, 같은 조건 안(B1_RECORD, B2_RECORD) | `wiki/patterns/anomaly/threshold.md` |
| P-107 | 비율 임계 초과 | 행·집단 | stat_screen 비율 모드(denominator_column), 동료 대비 비율(B1_RATIO, B2_RATIO) | `wiki/patterns/anomaly/threshold.md` |
| P-108 | 누적 임계 초과 | 집단 | 점검 질의 R_P108 | `wiki/patterns/anomaly/threshold.md` |
| P-109 | 극단값 탐지 | 행 | stat_screen B1_RECORD, B2_RECORD 의 상한 초과 쪽(P-106 과 함께 표시) | `wiki/patterns/anomaly/threshold.md` |
| P-110 | 범위 상한 초과 | 행 | 점검 질의 R_P110 | `wiki/patterns/anomaly/threshold.md` |
| P-111 | 선후 순서 위반 | 행 | 점검 질의 R_P111, stat_screen 간격 모드에서 대상 값이 음수인 하한 미만, find_number_gaps 번호 날짜 역전 | `wiki/patterns/anomaly/time-order.md` |
| P-112 | 기간 역전 | 행 | 점검 질의 R_P112 | `wiki/patterns/anomaly/time-order.md` |
| P-113 | 비정상 단축 | 행 | stat_screen 간격 모드(date_column=시작, metric_column=끝)의 하한 미만 | `wiki/patterns/anomaly/time-order.md` |
| P-114 | 비정상 지연 | 행 | stat_screen 간격 모드의 상한 초과 | `wiki/patterns/anomaly/time-order.md` |
| P-115 | 순서 위반 | 흐름·행 | find_number_gaps 결번(번호 순서의 빈 곳) | `wiki/patterns/anomaly/time-order.md` |
| P-116 | 동기화 역전 | 행 | 점검 질의 R_P116 | `wiki/patterns/anomaly/time-order.md` |
| P-117 | 식별자 중복 | 행 | find_duplicates(key_columns = 업무 키), find_number_gaps 번호 중복, 그레인 near_key | `wiki/patterns/anomaly/duplicate.md` |
| P-118 | 연락처 중복 | 행 | 점검 질의 R_P118 | `wiki/patterns/anomaly/duplicate.md` |
| P-119 | 증빙 중복 | 행 | find_duplicates(key_columns 에 증빙·인보이스 번호) | `wiki/patterns/anomaly/duplicate.md` |
| P-120 | 역할 중복 | 행 | 점검 질의 R_P120 | `wiki/patterns/anomaly/duplicate.md` |
| P-121 | 교차 엔티티 일치 | 행 | 점검 질의 R_P121 | `wiki/patterns/anomaly/duplicate.md` |
| P-122 | 완전 중복 | 행 | find_duplicates 완전 중복, 유사 중복 | `wiki/patterns/anomaly/duplicate.md` |
| P-123 | 필수 필드 NULL | 행 | 점검 질의 R_P123 | `wiki/patterns/anomaly/missing.md` |
| P-124 | 검증 로그 부재 | 흐름 | match_tables 짝 없음(대상이 결재·검수·로그 기록일 때) | `wiki/patterns/anomaly/missing.md` |
| P-125 | 증빙 파일 부재 | 쓰지 않음 | 없음(첨부 테이블이 AIAGT 접근 범위 밖) | `wiki/patterns/anomaly/missing.md` |
| P-126 | 역조건 존재 | 행 | 점검 질의 R_P126 | `wiki/patterns/anomaly/missing.md` |
| P-127 | 지속 방향성 변화 | 집단 | stat_screen 추세(B5_TREND) | `wiki/patterns/anomaly/trend-distribution.md` |
| P-128 | 급증/급감 | 집단 | stat_screen 월별 평소(B3_MONTH) | `wiki/patterns/anomaly/trend-distribution.md` |
| P-129 | 분포 편차 | 집단 | stat_screen 동료 대비 수준·빈도(B1_LEVEL, B2_LEVEL, B1_RATE, B2_RATE), 업무 시간 외 입력(B1_OFFHOUR, B2_OFFHOUR), 첫 자리·첫 두 자리 분포(B4_BENFORD, B4_BENFORD2), 점검 질의 R_P129(월말 3일 비중) | `wiki/patterns/anomaly/trend-distribution.md` |
| P-130 | 집중도 이상 | 집단 | stat_screen 동료 대비 집중(B1_GROUP, B2_GROUP), (선택) 차원 쌍 집중 템플릿 | `wiki/patterns/anomaly/trend-distribution.md` |
| P-131 | 역추세 | 집단 | 기본 탐색에서는 보지 않는다. 남은 sql_run 이 있을 때만 두 지표의 월별 CORR 1회 | `wiki/patterns/anomaly/trend-distribution.md` |
| P-132 | 형식 불일치 | 행 | 점검 질의 R_P132 | `wiki/patterns/anomaly/format-value.md` |
| P-133 | 논리 범위 위반 | 행 | 점검 질의 R_P133 | `wiki/patterns/anomaly/format-value.md` |
| P-134 | 변경값 무의미 | 행 | 점검 질의 R_P134 | `wiki/patterns/anomaly/format-value.md` |
| P-135 | 인코딩/특수문자 | 행 | 점검 질의 R_P135 | `wiki/patterns/anomaly/format-value.md` |
| P-136 | 이해관계 탐지 | 쓰지 않음 | 없음(관계 그래프 분석 필요, KG 없음) | `wiki/patterns/anomaly/relation-graph.md` |
| P-137 | 사외유용 경로 | 쓰지 않음 | 없음(관계 그래프 분석 필요, KG 없음) | `wiki/patterns/anomaly/relation-graph.md` |
| P-138 | 다단계 동일인 | 쓰지 않음 | 없음(관계 그래프 분석 필요, KG 없음) | `wiki/patterns/anomaly/relation-graph.md` |
| P-139 | 관계 네트워크 이상 | 쓰지 않음 | 없음(관계 그래프 분석 필요, KG 없음) | `wiki/patterns/anomaly/relation-graph.md` |
| P-140 | 온톨로지 타입 불일치 | 쓰지 않음 | 없음(관계 그래프 분석 필요, KG 없음) | `wiki/patterns/anomaly/relation-graph.md` |
| P-141 | 관계 경로 누락 | 쓰지 않음 | 없음(관계 그래프 분석 필요, KG 없음) | `wiki/patterns/anomaly/relation-graph.md` |

**쓰지 않는 패턴**: 수준이 「쓰지 않음」인 7개(P-125, P-136 ~ P-141)는 정의만 분류 파일에 남겨 두었다. 대응표에 나와도 가설에 넣지 않는다.

## 3. 조합 규칙

가설 하나는 **같은 점검 대상**(같은 테이블의 같은 행이나 같은 차원 값, 또는 조인 문서가 있는 두 테이블의 같은 건)에서 함께 신호가 나온 패턴 2~3개의 조합이다.

| 유형 | 성립하는 때 | 예외 조건(시나리오 SQL) 쓰는 법 | 예 |
|---|---|---|---|
| 같은 행 | 행 수준 패턴 둘 이상이 같은 업무 키 행에서 함께 나옴 | `<조건 A> AND <조건 B>` | P-113 비정상 단축 + P-106 통계적 임계 초과: 처리 기간이 비정상적으로 짧고 금액이 평소 범위를 넘은 견적 |
| 집단→행 | 집단 수준 패턴(P-127 ~ P-130, P-107 동료 대비 비율, P-108)이 나온 차원 값에서 행 수준 패턴의 비율도 전체보다 높음 | `<행 조건> AND <차원> IN (SELECT <차원> FROM <query_name> WHERE <같은 기간 조건> GROUP BY <차원> HAVING <집단 조건>)` | P-130 집중도 이상 + P-122 완전 중복: 지급이 몰린 거래선의 중복 지급 행 |
| 흐름→행 | 짝 없음·금액 불일치(P-104, P-124, P-102) 행에서 행 수준 패턴이 함께 나옴 | `NOT EXISTS (SELECT 1 FROM <상대 query_name> WHERE <조인 조건>) AND <행 조건>` 또는 조인 문서의 조인 조건 + `<행 조건>` | P-104 참조 무결성 위반 + P-123 필수 필드 NULL: 발주 짝이 없고 필수 값도 빈 입고 |

- 신호가 있는 패턴만 묶는다. 데이터에서 나오지 않은 패턴을 이름만 보고 붙이지 않는다.
- 같은 대상인지는 탐색 결과로 본다: 통계 도구 후보의 target(차원 값)과 점검 질의 결과 행의 DIM 이 같거나, 같은 테이블의 행 수준 신호끼리이거나, match_tables 결과의 기준 테이블과 같은 테이블이다. 행이 실제로 겹치는지는 hypothesis-worker 가 조합 질의(`query-writing.md` 6절)로 확인한다.
- 집단 조건의 경계(HAVING 값)는 통계 도구 결과의 경계 값이나 점검 질의의 전체 비율을 그대로 쓰고 새로 계산하지 않는다. 기간 조건은 바깥 질의와 같은 분석 기간 리터럴로 쓴다.
- 조합의 패턴은 최대 3개다. 같은 탐지 결과에서 함께 붙은 패턴(P-106 과 P-109, P-122 와 P-117)은 하나로 센다.
- 성립 조건: 분석 기간에 조합 조건을 함께 충족하는 키가 30건 이상이어야 한다. 30건 미만이면 hypothesis-worker 가 기여가 가장 작은 패턴을 빼고 줄인다. 줄여서 1개가 남으면 「단일」이다.
- 단일 패턴 가설: 다른 패턴과 겹치는 대상이 없는 이상은 「단일」로 둘 수 있다. 조합 가설이 요청 건수보다 적을 때만 가설 loop 에 넣고, 선별 기준의 위험 연결은 1점이다(`wiki/criteria.md`).
