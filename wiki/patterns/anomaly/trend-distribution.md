---
type: pattern-group
id: anomaly-trend-distribution
status: 자동 생성
source: patterns_73_2.json (데이터 이상징후 패턴 P-06 추세·분포, P-127 ~ P-131)
updated_at: 2026-10-22
---
# 데이터 이상징후 패턴: 추세·분포 (P-127 ~ P-131)

시간에 따른 흐름이나 집단 사이 분포가 평소와 다른 신호이다. 원본 패턴 정의(설명, 수법, 탐지 방법, COSO, 원본 질의 골격)와 Bottom-up 에서 쓰는 법(수준, 탐지 수단, 점검 질의 열 조건, OKF 에서 찾는 곳, 자주 묶이는 패턴)을 패턴마다 함께 적었다. 조합 규칙은 `wiki/patterns/index.md` 4절이다.

## P-127 지속 방향성 변화

- 설명: 시간 경과에 따라 값이 지속적으로 증가하거나 감소하는 패턴. 예를 들어 월별 매출이 연속적으로 증가하거나, 반품률이 지속적으로 상승할 때 탐지
- 기법 분류: P-06 추세·분포
- ACFE: N/A (기술적 탐지 패턴)
- COSO: CA-03-04 실적을행 비교
- SQL 대입: 가능
- 원본 질의 골격:
  - SQL: `WHERE col > LAG(col) > LAG(col,2)`
  - SPARQL(참고, 이 환경에는 KG 가 없다): `?s a dpsc:MonthlySales . ?s dpsp:month ?m . ?s dpsp:amount ?a . ?s2 a dpsc:MonthlySales . ?s2 dpsp:month ?m2 . ?s2 dpsp:amount ?a2 . FILTER(?m > ?m2 && ?a > ?a2)`
- 수법: 연속적 증가 추세 / 연속적 감소 추세 / 방향성 전환 감지
- 탐지 방법: 시계열 방향성 분석 / LAG 함수를 통한 전월 비교 / 추세 전환 시 경고
- 쓰는 법:
  - 수준: 집단
  - 탐지 수단: `stat_screen` 추세(B5_TREND)
  - 찾는 곳(OKF): 월별 집계에 `LAG` 를 써서 3개월 이상 연속 증가·감소한 집단.
  - 자주 묶이는 패턴: P-128 급증/급감, P-130 집중도 이상

## P-128 급증/급감

- 설명: 전 기간 대비 값의 변화율이 임계값을 초과하는 경우. 예를 들어 전월 대비 매출이 50% 이상 급증하거나, 비용이 50% 이상 급감할 때 탐지
- 기법 분류: P-06 추세·분포
- ACFE: N/A (기술적 탐지 패턴)
- COSO: CA-03-02 검증·조정, CA-03-04 실적을행 비교
- SQL 대입: 가능
- 원본 질의 골격:
  - SQL: `WHERE ABS(col-LAG(col))/LAG(col) > 0.5`  (참고용. 실제 범위 밖 판정은 통계 도구 기준, `stat-views.md` 2절)
  - SPARQL(참고, 이 환경에는 KG 가 없다): `?s a dpsc:MonthlySales . ?s dpsp:amount ?a . ?s2 a dpsc:MonthlySales . ?s2 dpsp:amount ?a2 . FILTER(ABS(?a-?a2)/?a2 > 0.5)`
- 수법: 매출 급증 / 비용 급감 / 건수 급변
- 탐지 방법: 기간별 변화율 계산 / 변화율 임계값 기반 경고 / 급변 원인 분석 및 검증
- 쓰는 법:
  - 수준: 집단
  - 탐지 수단: `stat_screen` 월별 평소(B3_MONTH)
  - 찾는 곳(OKF): 전월 대비 변화율. 월 문자열은 `SUBSTR(날짜, 1, 6)`.
  - 자주 묶이는 패턴: P-127 지속 방향성 변화, P-129 분포 편차

## P-129 분포 편차

- 설명: 그룹별 분포가 정상 범위를 벗어나는 경우. 예를 들어 특정 대리인의 거래 건수가 평균을 크게 벗어나거나, 부서별 비용 분포가 불균형할 때 탐지
- 기법 분류: P-06 추세·분포
- ACFE: N/A (기술적 탐지 패턴)
- COSO: CA-03-04 실적을행 비교
- SQL 대입: 가능
- 원본 질의 골격:
  - SQL: `GROUP BY grp HAVING COUNT > threshold`
  - SPARQL(참고, 이 환경에는 KG 가 없다): `?s a dpsc:Transaction . ?s dpsp:handler ?h . { SELECT ?h (COUNT(?h) AS ?c) WHERE { ?t dpsp:handler ?h } GROUP BY ?h HAVING (?c > 10) }`
- 수법: 특정 그룹 편중 / 분포 불균형 / 예상 분포 대비 편차
- 탐지 방법: 그룹별 분포 분석 / 정상 분포 범위 정의 / 편차 발생 그룹 플래그
- 쓰는 법:
  - 수준: 집단
  - 탐지 수단: `stat_screen` 동료 대비 수준·빈도(B1_LEVEL, B2_LEVEL, B1_RATE, B2_RATE), 업무 시간 외 입력(B1_OFFHOUR, B2_OFFHOUR), 첫 자리·첫 두 자리 분포(B4_BENFORD, B4_BENFORD2), 이상징후 점검 질의 열 `R_P129`(월말 3일 비중)
  - 점검 질의 열 조건: `CASE WHEN TO_DATE(<기준 날짜> DEFAULT NULL ON CONVERSION ERROR, 'YYYYMMDD') > LAST_DAY(TO_DATE(<기준 날짜> DEFAULT NULL ON CONVERSION ERROR, 'YYYYMMDD')) - 3 THEN 1 ELSE 0 END` (월말 3일 비중)
  - 찾는 곳(OKF): 집단별 건수·금액이 전체 분포에서 벗어난 집단.
  - 자주 묶이는 패턴: 대부분의 행 수준 패턴

## P-130 집중도 이상

- 설명: 값이 특정 엔티티에 과도하게 집중된 경우. 예를 들어 인센티브의 대부분이 특정 고객에게 집중되거나, 거래 금액이 특정 벤더에 편중될 때 탐지
- 기법 분류: P-06 추세·분포
- ACFE: N/A (기술적 탐지 패턴)
- COSO: CA-03-04 실적을행 비교
- SQL 대입: 가능
- 원본 질의 골격:
  - SQL: `WHERE GINI(col) > 0.5`  (참고용. 실제 범위 밖 판정은 통계 도구 기준, `stat-views.md` 2절)
  - SPARQL(참고, 이 환경에는 KG 가 없다): `?s a dpsc:Incentive . ?s dpsp:amount ?a . ?s dpsp:customer ?c . { SELECT ?c (SUM(?a) AS ?total) WHERE { ?i dpsp:customer ?c ; dpsp:amount ?a } GROUP BY ?c }`
- 수법: 금액 집중도 이상 / 건수 집중도 이상 / 고객/벤더별 편중
- 탐지 방법: 지니 계수 기반 집중도 분석 / 상위 N% 엔티티 점유율 계산 / 집중도 임계값 초과 시 경고
- 쓰는 법:
  - 수준: 집단
  - 탐지 수단: `stat_screen` 동료 대비 집중(B1_GROUP, B2_GROUP), (선택) 차원 쌍 집중 집계
  - 찾는 곳(OKF): 업체·거래선 점유율 집중(기존 시나리오 「단수견적 몰아주기」 SP_BQ_SSA1802012 와 겹치지 않게).
  - 자주 묶이는 패턴: P-122 완전 중복, P-106 통계적 임계 초과, P-102 테이블간 조인 불일치

## P-131 역추세

- 설명: 일반적으로 정적 상관관계를 가져야 하는 두 변수가 역의 상관관계를 보이는 경우. 예를 들어 마케팅 지출이 증가하는데 매출이 감소하거나, 재고 증가 대비 판매가 감소할 때 탐지
- 기법 분류: P-06 추세·분포
- ACFE: N/A (기술적 탐지 패턴)
- COSO: CA-03-04 실적을행 비교
- SQL 대입: 가능
- 원본 질의 골격:
  - SQL: `WHERE CORR(col_a, col_b) < -0.5`
  - SPARQL(참고, 이 환경에는 KG 가 없다): `?s a dpsc:MonthlyData . ?s dpsp:marketingSpend ?m . ?s dpsp:sales ?s . { SELECT CORR(?m, ?s) AS ?r WHERE { ?d dpsp:marketingSpend ?m ; dpsp:sales ?s } } FILTER(?r < -0.5)`
- 수법: 마케팅-매출 역상관 / 재고-판매 역상관 / 비용-수익 역상관
- 탐지 방법: 변수 간 상관관계 계산 / 정상 상관관계 범위 정의 / 역추세 발생 시 원인 분석
- 쓰는 법:
  - 수준: 집단
  - 탐지 수단: 기본 탐색에서는 보지 않는다. 남은 `sql_run` 이 있을 때만 두 지표의 월별 `CORR` 1회
  - 찾는 곳(OKF): 같은 단위로 집계한 두 지표의 `CORR` 이 음수인 집단.
  - 자주 묶이는 패턴: P-127 지속 방향성 변화
