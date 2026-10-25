# 통계 도구 사용법과 탐색 관점

관점은 통계 결과를 보는 기준이며, 도구 결과의 기법 코드나 규칙 점검 종류에 대응한다. 판정 기준은 도구 안에 고정되어 있으므로 이 문서의 조건은 결과를 읽을 때 쓴다. 변형 조각에 맞는 도구는 6절 표를 따른다.

> 출처: 통계 데이터 추출 에이전트 A(agent-a-project-v6)의 `stat-extraction/references/stat-views.md`. 1~3절은 원본 그대로이고, 4절 조회문 예시와 5절(이 DB 에서의 쓰임)을 OKF 감사시스템 DB 에 맞게 바꾸고 더했다. 데이터 확인(5단계)의 기간 인자에는 **분석 기간**만 넣는다.

## 1. 요청 항목과 도구 인자

| 요청 항목 | 도구와 인자 | 나오는 관점 |
|---|---|---|
| 지표(금액, 수량, 단가, 비율 컬럼) | `stat_screen`: table_name, metric_column(지표), date_column(기준 날짜), date_from, date_to | 같은 대상의 평소, 월별 평소, 추세, 첫 자리 분포, 첫 두 자리 분포 |
| 비교 단위(집단 컬럼) | 위 인자에 group_column | 동료 대비 집중, 동료 대비 수준, 동료 대비 빈도, 업무 시간 외 입력 |
| 조건(값의 크기를 좌우하는 구분 컬럼, 최대 2개) | 위 인자에 peer_columns(쉼표로 구분) | 같은 조건 안 |
| 비율(분자 컬럼과 분모 컬럼) | metric_column 에 분자, denominator_column 에 분모 | 같은 대상의 평소(행 비율), 월별 평소, 추세. group_column 을 넣으면 동료 대비 비율, 동료 대비 수준 |
| 간격(두 날짜 사이 일수) | date_column 에 시작 날짜, metric_column 에 끝 날짜 | 간격, 월별 평소, 추세. group_column 을 넣으면 동료 대비 수준 |
| 중복 | `find_duplicates`: table_name, key_columns(1~4개), date_column, date_from, date_to, amount_column(선택) | 중복 |
| 결번 | `find_number_gaps`: table_name, number_column(숫자형 번호), date_column, date_from, date_to, group_column(번호 체계, 선택) | 결번, 중복, 번호 순서 역전 |
| 대조 | `match_tables`: table_name(기준), match_table(대상), join_columns(「기준컬럼=대상컬럼」 1~2쌍), date_column(기준), date_from, date_to, amount_columns(「기준금액=대상금액」, 선택) | 짝 없음, 금액 불일치 |
| 기준 금액 이상 건수 등 도구가 내지 않는 집계 | 통계 도구 없음 | variation-worker 가 sql_run 으로 계산한다 |

- 기한 날짜와 실제 날짜(예: 납기 요청일과 출고일)의 간격은 기한 날짜를 date_column, 실제 날짜를 metric_column 에 넣는다. 양수가 기한 초과 일수다.
- 조건 컬럼과 비율 분모는 요청자가 지정했을 때만 넣는다.
- 업무 시간 외 입력은 테이블의 기준 날짜로 부른 호출의 결과만 쓰고, 기한 날짜를 date_column 에 넣은 간격 호출의 결과는 쓰지 않는다.
- 대상에만 있는 행을 보려면 table_name 과 match_table, 연결 키 쌍의 순서를 바꿔 한 번 더 부른다.
- 호출 단위: `stat_screen` 은 지표 하나와 비교 단위 하나의 조합마다 1회, `find_duplicates` 와 `find_number_gaps` 는 요청마다 1회, `match_tables` 는 대조 방향마다 1회다. 기간이 24개월을 넘으면 24개월 이하로 나누어 기간마다 부른다.

## 2. 관점별 기법 코드와 판정 조건

| 관점 | 기법 코드, 종류 | 판정 대상 | 판정 조건 |
|---|---|---|---|
| 같은 대상의 평소 | B1_RECORD, B2_RECORD(조건 칸 없음) | 집단 안 개별 값 | 집단마다 0 이 아닌 값 30건 이상 |
| 같은 조건 안 | B1_RECORD, B2_RECORD(조건 칸 있음) | 조건 칸 안 개별 값 | 칸마다 30건 이상 |
| 간격 | B1_RECORD, B2_RECORD(간격 모드) | 두 날짜 사이 일수 | 집단마다 30건 이상 |
| 동료 대비 집중 | B1_GROUP, B2_GROUP | 집단 합계 | 값 모드, 30건 이상 집단 3개 이상 |
| 동료 대비 수준 | B1_LEVEL, B2_LEVEL | 집단 중앙값 | 30건 이상 집단 3개 이상 |
| 동료 대비 빈도 | B1_RATE, B2_RATE | 집단의 0 이 아닌 행 비율 | 지표의 0 비율 50% 이상, 30건 이상 집단 3개 이상 |
| 동료 대비 비율 | B1_RATIO, B2_RATIO | 집단의 분자 합 ÷ 분모 합 | 비율 모드, 30건 이상 집단 3개 이상 |
| 월별 평소 | B3_MONTH | 월 건수와 월 값 | 자료가 있는 월 7개 이상 |
| 추세 | B5_TREND | 월 건수와 월 값 | 자료가 있는 월 7개 이상, 연속 6개 월 모두 증가 또는 감소 |
| 첫 자리 분포 | B4_BENFORD | 10 이상 값의 첫째 자리 | 값 모드, 10 이상 값 500건 이상, 최댓값이 최솟값의 100배 초과 |
| 첫 두 자리 분포 | B4_BENFORD2 | 10 이상 값의 첫 두 자리 | 첫 자리 분포와 같다 |
| 업무 시간 외 입력 | B1_OFFHOUR, B2_OFFHOUR | 집단의 주말, 야간(22시~6시) 입력 비중 | group_column 있음, 30건 이상 집단 3개 이상 |
| 중복 | find_duplicates 완전 중복, 유사 중복. find_number_gaps 번호 중복 | key 값이 같은 행, 같은 번호 | 같은 날(완전), 7일 이내(유사), 같은 번호 2건 이상 |
| 결번 | find_number_gaps 결번 | 번호 구간 | 앞 번호와 차이가 1보다 큰 곳 |
| 번호 순서 역전 | find_number_gaps 번호 날짜 역전 | 번호 순 이웃 행 | 번호는 커졌는데 날짜가 이른 쌍 |
| 짝 없음 | match_tables 짝 없음 | 기준 행 | 대상에 같은 연결 키 없음 |
| 금액 불일치 | match_tables 금액 불일치 | 기준 행 | 금액 차이 0.01 초과 |

- 범위 밖 판정은 modified z(\|M\| > 3.5, MAD 가 0 이면 3×IQR)와 최소 폭(중앙값의 20%, 간격 1일, 발생률과 업무 시간 외 비중 0.02)을 도구가 적용한 결과다.

## 3. 판정하지 않는 조건

판정하지 않은 항목에는 아래 사유를 결과 그대로 적는다.

| 사유 | 결과에서 확인하는 곳 |
|---|---|
| 분석 가능 조건 제외(30건 미만, 빈 값 비율 20% 초과, 지표 고유값 5개 미만) | validity.items 의 verdict 「제외」, groups.excluded_reasons, cells.excluded_reasons |
| 집단 비교 불가(집단 3개 미만) | validity.items 의 차원 고유값, warnings |
| 월별 평소, 추세 불가(월 7개 미만) | validity.items 의 「추세 적용」, warnings |
| 첫 자리 분포 불가 | validity.items 의 「Benford 적용」 |
| 업무 시간 외 입력 불가 | validity.items 의 「업무 시간 외 적용」, warnings |
| 간격 모드, 비율 모드에서 하지 않는 판정 | note |

## 4. 조회문 방식의 인자

조회문 방식은 1절의 table_name 자리에 analysis_select(분석 대상 조회문)를 넣고, 컬럼 인자(metric_column, key_columns, number_column 등)에는 조회문의 alias 를 넣는 호출이다. 한 호출에는 table_name 과 analysis_select 중 하나만 넣으며, 호출 단위와 나오는 관점은 1절과 같다.

- match_tables: 기준 쪽은 table_name 또는 analysis_select, 대상 쪽은 match_table 또는 match_select 를 쪽마다 따로 고르고, join_columns 와 amount_columns 에는 양쪽의 alias 나 컬럼명을 넣는다. 대상 쪽에는 기간 조건이 붙지 않는다.
- 테이블명은 OKF 테이블 문서의 `query_name`(`OWNER.TABLE`)으로 쓴다. 통계 도구 스키마(`db_schema`)의 `describe_table` 결과로 확인했으면 `scope.schema` 를 접두어로 붙여도 같다.

| 분석 단위 | 조회문 | 인자 |
|---|---|---|
| 견적 제출 1건(문자열 시각 → DATE 변환) | `SELECT t.REQ_NO, t.REQ_SEQ, t.ITEM_ID, t.EPR_CODE, t.LOCAL_CURR AS CURR, TO_DATE(t.제출HQ DEFAULT NULL ON CONVERSION ERROR, 'YYYYMMDDHH24MISS') AS SUBMIT_DT, t.LOCAL_AMT AS AMT FROM APPADAMSUSER.TI_BQMS005_INFA_QT t WHERE t.제출HQ >= '20250916000000' AND t.제출HQ < '20260916000000'` | stat_screen: metric_column=AMT, date_column=SUBMIT_DT, group_column=EPR_CODE, peer_columns=CURR |
| 거래(거래 하나당 한 행, 금액은 거래 줄 합) | `SELECT h.TXN_NO, TO_DATE(h.TXN_DT DEFAULT NULL ON CONVERSION ERROR, 'YYYYMMDD') AS TXN_DATE, h.EMP_CD, h.PARTNER_CD, (SELECT SUM(l.QTY * l.UNIT_PRICE) FROM <OWNER>.TXN_LINE l WHERE l.TXN_NO = h.TXN_NO) AS AMT FROM <OWNER>.TXN_HDR h` | stat_screen: metric_column=AMT, date_column=TXN_DATE, group_column=EMP_CD |
| 거래 줄(줄 하나당 한 행, 거래일은 헤더에서 결합) | `SELECT l.TXN_NO, l.ITEM_CD, l.QTY, TO_DATE(h.TXN_DT DEFAULT NULL ON CONVERSION ERROR, 'YYYYMMDD') AS TXN_DATE, h.PARTNER_CD FROM <OWNER>.TXN_LINE l JOIN <OWNER>.TXN_HDR h ON h.TXN_NO = l.TXN_NO` | find_duplicates: key_columns=PARTNER_CD,ITEM_CD,QTY, date_column=TXN_DATE |

- 첫 행은 OKF 테이블 문서를 바탕으로 쓴 예다(실제 컬럼은 그 테이블의 문서로 확인한다). 통화가 섞인 금액이라 통화를 조건 칸(peer_columns)으로 나눴다. 둘째·셋째 행의 TXN_* 는 형태를 보이는 가상의 이름이며, 실제로는 OKF 테이블 문서의 이름으로 바꾼다.
- 기준 날짜가 없는 테이블은 table_name 으로 넘기지 않고, 두 번째 예시처럼 날짜가 있는 테이블을 결합해 기준 날짜를 산출한다.

## 5. 이 DB 에서의 쓰임 (OKF 감사시스템 DB)

- **방식 고르기**: 기준 날짜가 `DATE`/`TIMESTAMP` 이고 테이블이 통계 도구 `db_schema`(권장 `APPADAMSUSER`)에 있으면 `table_name` 방식(OWNER 없이 이름만)을 쓸 수 있다. 이 DB 는 날짜 대부분이 `VARCHAR2` 문자열이므로 보통 조회문 방식(`analysis_select`)을 쓴다. `SETADAMSUSER` 테이블도 조회문 방식으로만 부른다.
- **날짜 변환**: 문자열 날짜는 조회문에서 DATE 로 바꾼 alias 를 date_column 에 넣는다. 형식은 테이블 문서의 타입과 T2S 힌트로 정한다.
  - `VARCHAR2(8)` YYYYMMDD → `TO_DATE(t.<컬럼> DEFAULT NULL ON CONVERSION ERROR, 'YYYYMMDD') AS BASE_DT`
  - `VARCHAR2(14)` YYYYMMDDHH24MISS → `TO_DATE(t.<컬럼> DEFAULT NULL ON CONVERSION ERROR, 'YYYYMMDDHH24MISS') AS BASE_DT` (업무 시간 외 입력 관점은 시각이 있는 이 형식에서만 의미가 있다)
  - `VARCHAR2(6)` YYYYMM → `TO_DATE(t.<컬럼> || '01' DEFAULT NULL ON CONVERSION ERROR, 'YYYYMMDD') AS BASE_DT` (일 단위 관점은 쓰지 않는다)
  - 플레이스홀더(`'00000000'`)와 형식이 틀린 값은 NULL 이 되어 기간 밖으로 빠진다. 그 건수가 많으면 해석 주의에 적는다.
- **기간 조건 함께 넣기**: 도구의 기간 조건은 변환한 alias 에 걸리므로 원래 컬럼의 인덱스를 쓰지 못한다. `size:m` 이상 테이블은 조회문에 원래 문자열 컬럼의 범위 조건(`WHERE t.<컬럼> >= '<분석 시작>' AND t.<컬럼> < '<분석 끝>'`)을 date_from, date_to 와 같은 기간으로 함께 넣는다.
- **숫자 변환**: `VARCHAR2` 금액·수량은 `TO_NUMBER(t.<컬럼> DEFAULT NULL ON CONVERSION ERROR) AS AMT` 로 바꾼다. 단가 컬럼은 금액 지표로 쓰지 않는다.
- **통화**: 통화 컬럼이 있는 금액은 통화를 peer_columns(조건 칸)로 나누거나, KRW·USD 환산 금액 컬럼을 지표로 쓴다.
- **데이터 정리 조건**: soft-delete 플래그, 유효기간, `wiki/normal-patterns.md` 1절의 데이터 특성 제외를 조회문 WHERE 에 넣는다. 넣은 조건은 근거에 적는다.
- **물리명**: 조회문의 테이블·컬럼 이름은 OKF 테이블 문서의 `# Schema` 에서 복사한다. 공백·특수문자가 있는 컬럼은 큰따옴표로 감싸되 산출 alias 는 큰따옴표 없는 영문으로 붙인다.
- **PII**: 비고 `PII` 컬럼은 산출 컬럼에 넣지 않는다(key_columns 로 꼭 써야 하면 그 관점은 판정하지 않은 항목에 「PII 컬럼」으로 적는다).
- **분석 단위와 그레인**: 조회문 한 행이 분석 단위 하나가 되게 테이블 문서의 업무 키(그레인 블록)를 기준으로 쓴다. `near_key` 테이블은 중복 행이 있으므로 중복 점검 결과를 해석할 때 그 사실을 적는다.

## 6. 탐색 관점 7개와 수단

이 에이전트에서 통계 도구는 variation-worker 가 변형 조각의 경계(평소 범위, 동료 대비 집중 등)를 정하거나 변형 조건이 데이터에서 신호를 내는지 볼 때 2회 이하로 쓴다. 관점마다 어떤 도구·결과를 보는지는 아래 표를 따른다. 모든 계산은 분석 기간만 쓴다. 결과를 데이터 이상징후 패턴에 붙이는 대응은 `wiki/patterns/index.md` 2절이다.

| 관점 | 확인 내용 | 통계 도구 | 조각으로 쓰는 점검 조건(분류 파일) | 데이터 이상징후 패턴 |
|---|---|---|---|---|
| 분포 | 금액, 건수의 편중 | `stat_screen` + group_column → 같은 대상의 평소, 동료 대비 집중, 첫 자리·첫 두 자리 분포 | — | P-106, P-109, P-129, P-130 |
| 반복 | 같은 행위의 반복 | `find_duplicates`(완전·유사 중복), `stat_screen` 동료 대비 빈도 | — | P-117, P-119, P-122 |
| 시간 | 급증, 급감, 기간 말 집중, 업무 시간 외 | `stat_screen` → 월별 평소, 추세, 업무 시간 외 입력(14자리 시각 컬럼일 때) | 월말 3일 비중(P-129), 기간 역전(P-112), 선후 순서(P-111) | P-111, P-112, P-113, P-114, P-127, P-128, P-129 |
| 관계 | 특정 대상 쌍의 집중, 역할 겹침 | — | 역할 중복(P-120), 교차 엔티티 일치(P-121) | P-120, P-121, P-130 |
| 일관성 | 같은 행·연결된 두 테이블의 불일치 | `match_tables` → 금액 불일치 | 필드간 불일치(P-101), 논리적 관계 위반(P-103) | P-101, P-102, P-103 |
| 누락 | 값이나 상대 건의 누락 | `match_tables` → 짝 없음, `find_number_gaps` → 결번 | 빈 값 비율(P-123), 역조건(P-126) | P-104, P-115, P-123, P-124, P-126 |
| 비교 | 동종 집단 대비 차이 | `stat_screen` + group_column(+ peer_columns) → 동료 대비 수준, 같은 조건 안, 비율(denominator_column), 간격(날짜 둘) | — | P-107, P-113, P-114, P-129 |

- 차원이나 점검 컬럼에 PII 컬럼을 쓰지 않는다. `size:l`·`size:xl` 테이블은 법인·사이트 같은 조건을 더해 범위를 좁힌다(`sql-query` 작성 규칙의 큰 테이블).
