# 중복 판별

종합 6.0 이상인 시나리오 1건이 **기존 시나리오와 의미 기준으로 겹치는지** 판별한다. 6.0 미만이면 실행하지 않는다.

- 기존 시나리오의 **정본은 DB**(`ADAMSUSER` 시나리오 뷰·테이블)다. 데이터 사전 md 는 참고 인덱스일 뿐이다.
- 시나리오명 텍스트가 닮았는지가 아니라 **무엇이 잘못되는지(위험 상황), 무엇을 단위로(대상), 어떻게 탐지하는지(조건 구조)** 가 같은지 본다.
- 유사 판정권은 메인 절차에 있다. 이 문서는 비교 대상을 모으고 3축으로 비교하는 방법이다.

입력: 채점 통과한 `scenario_name`, `scenario_sql`, 데이터 사전 대조 결과(사용 테이블·조인·코드값).

## 1. 기존 시나리오 목록 조회

```sql
SELECT SCENARIO_ID, SCENARIO_NM, SCENARIO_VER, BUSINESS_TYPE, RISK_TYPE, SCENARIO_OUTLINE
FROM   ADAMSUSER.VI_AD_SCENARIO_BASE_AI
WHERE  DELETE_YN = 'N'
ORDER  BY SCENARIO_ID, SCENARIO_VER
```

- `VI_AD_SCENARIO_BASE_AI` 는 시나리오(SCENARIO_ID)+버전(SCENARIO_VER)당 1행이다. 후보의 최종 버전은 여기서 받은 `SCENARIO_VER` 를 쓴다.
- `execute_sql` 은 10행까지만 돌려준다. 10행이 돌아오면 `COUNT(*)` 로 전체 건수를 보고, 2절의 업무 영역 조건(`BUSINESS_TYPE`, `RISK_TYPE`, `SCENARIO_OUTLINE`)을 WHERE 에 더해 나눠 조회한다.
- 컬럼명은 `okf/schemas/ADAMSUSER/views/VI_AD_SCENARIO_BASE_AI.md` 의 `# Schema` 표에 있는 것만 쓴다. 표에 없는 컬럼이 있으면 빼고 조회한다.

## 2. 1차 스크리닝 (의미 판단 전)

전체 목록에서 비교 후보를 고른다.

- 새 시나리오가 참조하는 테이블의 업무 영역과, 기존 시나리오의 `BUSINESS_TYPE`·`RISK_TYPE`·`SCENARIO_OUTLINE` 이 가리키는 업무 영역이 겹치는 것을 고른다.
- 기존 시나리오 목록(`ADAMSUSER.VI_AD_SCENARIO_BASE_AI`)에서 참조 테이블·업무 영역이 겹치는 시나리오를 먼저 확인한다.
- 후보가 0건이면 "기존 시나리오와 겹치지 않음"으로 판정하고 5절로 간다.
- 후보가 많으면 업무 영역과 참조 테이블이 모두 겹치는 것부터 정렬해 상위 후보를 비교한다. 비교하지 않고 남긴 후보 수를 기록한다.

## 3. 후보 정의 수집 (후보당 2회 이하)

### 3-1. 단계별 개요·대상 테이블·이상 기준

```sql
SELECT SCENARIO_STEP, SCENARIO_STEP_NM, STEP_DESCRIPTION, TARGET_TABLE_NM
FROM   ADAMSUSER.VI_AD_SCENARIO_LOGIC_AI
WHERE  SCENARIO_ID = '<후보 SCENARIO_ID>' AND SCENARIO_VER = <후보 SCENARIO_VER> AND DELETE_YN = 'N'
ORDER  BY SCENARIO_STEP
```

- `STEP_SQL_BATCH`(작업 SQL, CLOB)는 SELECT 하지 않는다. 로직 요약은 `SCENARIO_STEP_NM` + `STEP_DESCRIPTION` 으로 충분하다.
- `STEP_DESCRIPTION` 이 `VI_AD_SCENARIO_LOGIC_AI` 문서의 `# Schema` 표에 없으면 빼고 조회한다.

### 3-2. 추출 컬럼과 대상(인물/업체/법인)

```sql
SELECT SCENARIO_RESULT_TYPE
FROM   ADAMSUSER.VI_AD_SCENARIO_BASE_AI
WHERE  SCENARIO_ID = '<후보 SCENARIO_ID>' AND SCENARIO_VER = <후보 SCENARIO_VER>
```

- 컬럼명은 `okf/schemas/ADAMSUSER/views/VI_AD_SCENARIO_BASE_AI.md` 의 `# Schema` 표에 있는 것만 쓴다.
- `SCENARIO_RESULT_TYPE`(GCS030: 인물/업체/인물+업체)이 그 시나리오의 대상이다.

## 4. 3축 의미 비교 (후보 1건당)

| 축 | 새 시나리오에서 보는 것 | 기존 시나리오에서 보는 것 |
|---|---|---|
| 위험 상황 (risk) | 이름 + SQL 의 WHERE/집계 조건이 가리키는 "무엇이 잘못되는가" | `SCENARIO_NM` + `SCENARIO_OUTLINE` + 단계명·설명 + 추출 컬럼이 가리키는 상황 |
| 대상 (target) | FROM/조인 대상 테이블, 집계 단위(업체? 인물? 거래선? 건?) | `SCENARIO_RESULT_TYPE`(인물/업체), `TARGET_TABLE_NM` |
| 조건 구조 (condition) | 어떤 비교·집계·임계값·패턴으로 탐지하는가 | 단계 구성, `STEP_DESCRIPTION`·`CHECK_ITEM` 이 가리키는 조건 |

축마다 `same` / `different` / `unknown` 중 하나로 기록하고 근거를 한 줄 쓴다.

### 판정

- **duplicate**: 3축 중 2축 이상이 `same`.
- **different**: `same` 이 1축 이하이고, 판정에 필요한 정보가 있다. 위험 상황이 같아도 대상이나 조건 구조가 명확히 다르면 비유사다. 예: 같은 "특정 시점 거래 몰림"이라도 업체 단위 vs 인물 단위, 또는 임계값 구조가 다르면 different.
- **insufficient**: 판단에 필요한 기존 시나리오 정보가 DB 에 없어(컬럼 공백, 로직 미등록) `unknown` 축 때문에 2축 이상 `same` 여부를 정할 수 없다. 유사로도 비유사로도 처리하지 않고 "확인 필요"에 올린다.

## 5. 최종 판정

| 후보 비교 결과 | 결과 | 최종 verdict |
|---|---|---|
| duplicate 1건 이상 | 중복(예) | `DUPLICATE` |
| duplicate 0건, insufficient 1건 이상 | 중복(아니오) + 확인 필요 | `PASS` (reason 에 "정보 부족 후보 N건 확인 필요") |
| 모두 different, 또는 후보 0건 | 중복(아니오) | `PASS` |

`duplicate_of` 는 duplicate 후보 중 `same` 축이 가장 많은 1건(같으면 목록 순서가 앞선 것)으로 채운다. 나머지 duplicate 후보는 출력의 "중복 판별" 절에만 적는다.

```json
{"scenario_id": "SSA2405003", "scenario_nm": "들러리 견적 업체 반복 참여", "matched_axes": ["risk", "target"]}
```

## 금지

- 기존 시나리오 로직을 새 시나리오 SQL 에 "맞추어" 다시 쓰지 않는다.
- `VI_AD_SCENARIO_LOGIC_AI` 의 로직 본문(`STEP_SQL_BATCH`)을 실행용 SQL 로 바꾸거나 실행하지 않는다 (SELECT 조회만).
- 후보의 `SCENARIO_VER` 는 항상 `VI_AD_SCENARIO_BASE_AI` 에서 받은 최종 버전만 쓴다.

## 출력에 남길 것

- 후보 목록: `SCENARIO_ID`, `SCENARIO_NM`, `BUSINESS_TYPE`, 개요 요약
- 후보별 3축 비교표와 판정(duplicate / different / insufficient)
- 조회 SQL 별 행 수