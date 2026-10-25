# 감사 질의 작성과 건수 점검 (시나리오 변형)

원본·변형 시나리오의 예외 질의, 모집단 질의, 시나리오 SQL 을 쓰고 `sql_run` 으로 점검하는 규칙이다. 테이블·컬럼·조인·코드값을 OKF 로 확정하는 법과 Oracle 작성 규칙은 skill `sql-query` 를 따르고, 이 문서는 감사 질의에만 붙는 규칙을 적는다.

> 이 문서의 ```sql 블록은 질의를 만드는 틀이다. `sql_run`·통계 도구에 넣는 질의이며, 사용자에게 내는 보고서 본문에는 어떤 SQL 도 쓰지 않는다(시나리오 SQL 은 `sql_submit` 입력, 보고서 부록 A-2(원본은 A-3), 답변 끝 `## 부록: 시나리오 JSON` 에만 들어간다).

| 단계 | 기간 리터럴 | 질의 |
|---|---|---|
| 원본 확보(2단계, main agent) | 분석 기간 | 원본 예외 질의·모집단 질의(복원 포함), 건수 점검(3절) |
| 데이터 확인(5단계, variation-worker) | 분석 기간 | 변형 검증 질의(6절), 변형 예외 질의, 모집단 질의, 비교 지표 질의, 건수 점검(3절) |
| 표본 점검(6단계, main agent) | 분석 기간 | 표본 질의(4절) |
| 시나리오 SQL(7단계에서 확정) | 분석 기간 | variation-worker 의 변형 예외 질의 그대로 |

모든 단계가 같은 분석 기간(`AGENTS.md` 5절) 리터럴을 쓴다. 원본 SQL 에 다른 기간 리터럴이 있으면 분석 기간으로 바꿔 실행한다(원본의 기간이 곧 분석 기간이 되었으면 그대로). 집단 조건 서브쿼리(6절)의 기간 리터럴도 바깥 질의와 같다. variation-worker 의 변형 예외 질의가 그대로 시나리오 SQL 이 된다.

## 1. 두 SQL

| SQL | 무엇을 돌려주나 | 쓰는 곳 |
|---|---|---|
| 예외 질의 = 시나리오 SQL | 이상을 만든 조건에 맞는 점검 대상 행. **행 하나가 점검 대상 1건**이다 | 건수 점검, 표본 점검, `sql_submit` 의 UNION ALL, 부록 JSON 의 `scenario_sql` |
| 모집단 질의 | 같은 FROM, JOIN, 공통 조건(기간, 정상 업무 제외, soft-delete)에서 예외 조건만 뺀 행 | 건수 점검, 비교 기준. 제출하거나 답변에 쓰지 않는다 |
| 비교 지표 질의 | 이상을 나타내는 지표와 비교 기준을 **한 행, 두 열**(`TARGET_VAL` 대상 값, `BASE_VAL` 비교 기준 값)로 내는 집계(예: 대상 집단의 비율과 전체 비율) | 데이터 확인의 수치, 보고서의 「이상을 뒷받침하는 근거」 |

## 2. 예외 질의(시나리오 SQL) 작성 규칙

- SELECT 로 시작하는 한 문장이다. CTE 가 꼭 필요하면 WITH 로 시작해도 되지만, 3절의 점검 질의(괄호로 감싼 형태)가 실행되는지 확인한다.
- **한 줄로 쓴다.** 줄바꿈 대신 공백 하나를 쓴다. 주석(`--`, `/* */`), 세미콜론, `FETCH FIRST`, 바인드 변수(`:p_from`)를 넣지 않는다. 문자열 리터럴 안에도 `--` 를 쓰지 않는다.
- 행 단위: 점검 대상의 업무 키(key_columns, 예: 견적번호·차수·업체)마다 한 행이 되게 쓴다. 상세 테이블과 조인해 행이 늘면 `SELECT DISTINCT` 나 `GROUP BY` 로 키 단위로 줄인다. 업무 키는 테이블 문서의 `primary_key` 와 그레인 블록에서 정한다.
- SELECT 목록: key_columns, 기준 날짜, 금액(있으면), 예외 판단에 쓴 값만 넣는다. `SELECT *`, PII 컬럼은 넣지 않는다. 컬럼 alias 는 영문 대문자와 밑줄로 짓는다(서로 겹치지 않게).
- 기간: 기준 날짜 컬럼에 리터럴로 `>= '<시작>' AND < '<종료>'` 를 건다. 리터럴 형식은 컬럼 형식에 맞춘다(`VARCHAR2(8)` → `'20251001'`, `VARCHAR2(6)` → `'202510'`, `VARCHAR2(14)` → `'20251001000000'`, `DATE` → `DATE '2025-10-01'`). `size:l`·`size:xl`·`size:unknown` 테이블은 기간 조건이 반드시 있어야 한다.
- 정상 업무 제외: `wiki/normal-patterns.md` 의 SQL 조건 가운데 대상 테이블에 해당하는 것과, variation-worker 의 반례 조회에서 정상으로 확인된 조건을 넣는다. soft-delete 플래그, 유효기간, 플레이스홀더(`'00000000'`, 금액 1/10,000) 제외도 넣는다. 넣지 못한 제외는 「데이터 해석 가정」에 적는다.
- 예외 조건은 조건 단위로 쓴다. 이상이 특정 업체·거래선·사원에 몰렸어도 그 값을 리터럴로 넣지 않고, 그 대상을 드러낸 조건(비율, 반복 횟수, 경계 초과)으로 쓴다. 고정 금액 기준이 필요하면 기준 테이블(예: `TI_GRPB_COMPANY_AUDIT_AMT`)이나 통계 도구 경계로 정하고, 숫자를 지어내지 않는다.
- 예외 조건은 변형 후보의 대응표(`variation-types.md` 4절)에 적은 조각을 6절 유형대로 이은 것이다. 대응표에 없는 조건을 더하지 않는다(정상 업무 제외와 데이터 정리 조건은 공통 조건이다).
- 통계 도구의 경계 값(`boundaries` 의 low, high)을 조건으로 쓸 때는 결과 값을 그대로 리터럴로 쓰고 새로 계산하지 않는다. 경계 값을 리터럴로 쓴 조건은 「데이터 해석 가정」에 「분석 기간 경계 값 사용」으로 적는다.
- 조인은 `sql-query` 「조인」 절대로 쓰고, 문서 없는 조인은 실측 검증 SQL 을 먼저 `sql_run` 으로 실행한다.
- 큰따옴표는 공백·특수문자가 있는 컬럼 이름에만 쓴다(`"LOCAL 요청일시"`). 문자열 값은 작은따옴표로 감싼다.
- `ORDER BY` 는 넣어도 되지만 건수에는 영향이 없다. 넣으면 기준 날짜와 키 순으로 둔다.

## 3. 건수 점검 질의

예외 질의(시나리오 SQL)와 모집단 질의를 각각 괄호 속에 그대로 넣어 한 번에 점검한다. key_columns 가 둘 이상이면 `||'|'||` 로 잇는다. 금액 컬럼이 없으면 `HIT_AMT` 를 빼고, 문자형 금액이면 `TO_NUMBER(… DEFAULT NULL ON CONVERSION ERROR)` 로 바꾼다.

```sql
SELECT p.POP_CNT, p.POP_KEY_CNT, h.HIT_CNT, h.KEY_CNT, h.HIT_AMT FROM (SELECT COUNT(*) AS POP_CNT, COUNT(DISTINCT <키1> || '|' || <키2>) AS POP_KEY_CNT FROM (<모집단 질의>)) p CROSS JOIN (SELECT COUNT(*) AS HIT_CNT, COUNT(DISTINCT <키1> || '|' || <키2>) AS KEY_CNT, SUM(<금액>) AS HIT_AMT FROM (<시나리오 SQL>)) h
```

- 판정은 `AGENTS.md` 7절 표를 따른다. 위에서부터 맞는 첫 행을 따른다.
- 원본 시나리오는 main agent 가 2단계에서 1회, 변형 시나리오는 variation-worker 가 5단계에서 1회 이 점검을 한다. main agent 는 변형의 점검을 다시 실행하지 않고 worker 가 돌려준 값을 쓴다.
- 이 점검의 `HIT_AMT` 는 선별 기준의 영향 규모(`wiki/criteria.md`, 후보 가운데 예외 금액 상위 3위)에 그대로 쓴다.
- 건수 점검과 6단계 표본 점검을 통과한 시나리오 SQL(variation-worker 의 예외 질의)의 글자가 그대로 제출과 부록 JSON 에 들어간다. 고쳤으면 고친 글자로 건수 점검을 다시 한다.

## 4. 표본 질의 (6단계, 후보당 sql_run 1회)

variation-worker 가 「충분」·「충분(소수)」으로 돌려준 예외 질의(분석 기간)에서 5행을 본다. PII 컬럼을 빼고 키, 기준 날짜, 판단 값만 본다.

```sql
SELECT <키1>, <키2>, <기준 날짜>, <판단 값> FROM (<시나리오 SQL>) FETCH FIRST 5 ROWS ONLY
```

- 예외 조건이 의도대로 걸렸는지와, 표본 행이 `wiki/normal-patterns.md` 의 정상 업무 패턴에 해당하지 않는지를 본다(scenario-variation 판정 표).
- 시나리오 SQL 의 기간 리터럴과 조건은 바꾸지 않는다. 표본 행의 값은 답변에 옮기지 않는다.

## 5. 수정

| 결과 | 처리 |
|---|---|
| ORA 오류 | skill `sql-query` 의 판정 표대로 고친다 |
| 시간 초과 | 기간 조건이 인덱스를 쓰도록 컬럼에 함수를 씌우지 않았는지, 불필요한 조인이 있는지 확인해 줄인다. 1회만 다시 점검한다 |
| 모집단 0건 | 날짜 리터럴 형식, 코드값 vs 한글 라벨, 플래그 값(Y/N vs 0/1), 조인 방향(INNER → LEFT)을 차례로 확인한다. 조건을 하나씩 뺀 모집단 COUNT 로 원인 조건을 찾는다 |
| 행 늘어남(HIT_CNT > KEY_CNT) | 조인 문서의 `cardinality`·`fanout` 을 보고 DISTINCT·GROUP BY·EXISTS 로 키 단위로 줄인다 |
| 예외 = 모집단 | 예외 조건의 리터럴과 값 형식을 값 확인 SQL 로 확인한다 |

수정은 질의 1건당 2회까지다. 같은 SQL 은 다시 실행하지 않는다. 고쳐도 안 되면 그 질의는 실패로 두고 넘어간다.

## 6. 변형 조각 잇기와 변형 검증 질의

변형 예외 질의는 원본 조각 가운데 유지한 것과 바꾸거나 더한 조각을 유형대로 이은 것이다(`variation-types.md` 2절). 조각 유형은 데이터 이상징후 패턴 조합과 같다(`wiki/patterns/index.md` 4절).

| 유형 | 예외 조건 |
|---|---|
| 같은 행 | `<조각 A> AND <조각 B>` |
| 집단→행 | `<행 조각> AND t.<차원> IN (SELECT s.<차원> FROM <query_name> s WHERE s.<기준 날짜> >= '<시작>' AND s.<기준 날짜> < '<종료>' GROUP BY s.<차원> HAVING COUNT(*) >= 30 AND <집단 조각>)` |
| 흐름→행 | `NOT EXISTS (SELECT 1 FROM <상대 query_name> m WHERE <조인 조건>) AND <행 조각>` (대칭 변형은 기준 테이블과 상대 테이블을 바꾼다) |

- 조건 조각은 원본 SQL 의 조각, 분류 파일(`wiki/patterns/anomaly/*.md`)의 「점검 질의 열 조건」, 통계 도구가 돌려준 경계(`boundaries` 의 low, high)를 그대로 쓴다. 새 숫자를 지어내지 않는다.
- 집단 조각은 `HAVING` 에 쓰는 집계 조건이다(예: P-130 → `SUM(s.<금액>) > <경계 값>`, P-129 → `AVG(CASE WHEN <조건> THEN 1 ELSE 0 END) > <비교 기준 값>`). 특정 차원 값을 리터럴로 넣지 않는다.
- 서브쿼리의 기간 리터럴은 바깥 질의와 같게 쓴다.

**변형 검증 질의** (variation-worker 의 질의 ①, `sql_run` 1회): 비교 지표, 변형 재현 건수, 조각별 기여, 반례를 한 문장으로 본다. 분석 기간 리터럴을 쓴다. 키가 둘 이상이면 `||'|'||` 로 잇는다.

```sql
SELECT c.TARGET_VAL, c.BASE_VAL, k.POP_KEY_CNT, k.HIT_KEY_CNT, k.A_CNT, k.B_CNT, k.NORMAL_CNT FROM (<비교 지표 질의>) c CROSS JOIN (SELECT COUNT(DISTINCT <키>) AS POP_KEY_CNT, COUNT(DISTINCT CASE WHEN <조각 A> AND <조각 B> THEN <키> END) AS HIT_KEY_CNT, COUNT(DISTINCT CASE WHEN <조각 A> THEN <키> END) AS A_CNT, COUNT(DISTINCT CASE WHEN <조각 B> THEN <키> END) AS B_CNT, COUNT(DISTINCT CASE WHEN <조각 A> AND <조각 B> AND <정상 조건> THEN <키> END) AS NORMAL_CNT FROM <변형 모집단 질의의 FROM·JOIN> WHERE <변형 모집단 질의의 공통 조건, 정상 제외는 빼고>) k
```

- 조각이 하나면 `A_CNT` 와 `HIT_KEY_CNT` 가 같고 `B_CNT` 를 뺀다. 세 개면 `C_CNT` 를 더한다. 집단 조각은 `t.<차원> IN (…)` 꼴로 CASE 안에 넣는다.
- `NORMAL_CNT` 는 변형 건 가운데 `wiki/normal-patterns.md` 의 정상 조건(반례)에 해당하는 건수다. 정상 조건이 없으면 이 열을 빼고 반환에 「반례 조건 없음」을 적는다.
- 판단(위에서부터 맞는 첫 행):

| 결과 | 처리 |
|---|---|
| 실행 오류 | `sql-query` 판정 표로 1회 고친다. 그래도 오류면 보류(이유: 실행 오류 <오류 문구>) |
| `HIT_KEY_CNT` 가 0 | 더한 조각(원본에 없던 것)이 있으면 그 조각을 빼고 질의 ①을 1회만 다시 실행한다(경로 「조각 수정」). 뺄 조각이 없거나 그래도 0 이면 반박(이유: 분석 기간에 해당 건 없음) |
| `TARGET_VAL` 과 `BASE_VAL` 의 차이가 없거나 설계와 반대 방향 | 반박(이유: 비교 기준과 차이 없음) |
| `HIT_KEY_CNT - NORMAL_CNT` 가 0 | 정상 조건이 `wiki/normal-patterns.md` 2절(업무 패턴)이면 반박(이유: 정상 업무 <조건> 으로 설명됨), 1절(데이터 특성)이면 재분류(이유: 데이터 적재·표기 특성 <조건> 으로 설명됨) |
| `HIT_KEY_CNT - NORMAL_CNT` 가 1 ~ 29 | 충분(소수). 정상 조건은 예외 질의에 제외 조건(`AND NOT (<정상 조건>)`)으로 넣는다 |
| 그 밖 | 충분. 정상 조건은 예외 질의에 제외 조건으로 넣는다 |
