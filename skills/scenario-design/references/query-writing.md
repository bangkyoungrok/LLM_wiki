# 시나리오 SQL 작성과 건수 점검

시나리오 SQL 과 모집단 SQL 을 쓰고 `sql_run` 으로 점검하는 규칙이다. 테이블·컬럼·조인·코드값을 OKF 로 확정하는 법과 Oracle 작성 규칙은 skill `sql-query` 를 따르고, 이 문서는 시나리오에만 붙는 규칙을 적는다.

> 이 문서의 ```sql 블록은 질의를 만드는 틀이다. `sql_run` 에 넣는 질의이며, 사용자에게 내는 답변에는 어떤 SQL 도 코드 블록으로 쓰지 않는다(시나리오 SQL 은 답변 끝 `## 부록: 시나리오 JSON` 의 JSON 블록 안에만 들어간다, `answer-format.md` 3·5절).

scenario-worker 의 `sql_run` 은 후보 1건당 5회다: 확인 질의(6절, 필요할 때만) 1회, 조합 점검 질의(3절) 1회, 표본 1회, 수정·조합 축소 합쳐 2회. 여러 방향을 보는 일은 문서로 하고, 데이터로 확인할 것은 한 문장에 묶는다.

## 1. 두 SQL

| SQL | 무엇을 돌려주나 | 쓰는 곳 |
|---|---|---|
| 시나리오 SQL | 부정 패턴 조합의 예외 조건(조건 조각들을 5절 유형대로 이은 것)에 맞는 점검 대상 행. **행 하나가 점검 대상 1건**이다 | 조합 점검, `sql_submit` 의 UNION ALL, 부록 JSON 의 `scenario_sql` |
| 모집단 SQL | 같은 FROM, JOIN, 공통 조건(기간, 정상 업무 제외, soft-delete)에서 예외 조건만 뺀 행. 주 패턴의 모집단이다 | 조합 점검에만 쓴다. 제출하거나 답변에 쓰지 않는다 |

## 2. 시나리오 SQL 작성 규칙

- SELECT 로 시작하는 한 문장이다. CTE 가 꼭 필요하면 WITH 로 시작해도 되지만, 3절의 점검 질의(괄호로 감싼 형태)가 실행되는지 확인한다.
- **한 줄로 쓴다.** 줄바꿈 대신 공백 하나를 쓴다. 주석(`--`, `/* */`), 세미콜론, `FETCH FIRST`, 바인드 변수(`:p_from`)를 넣지 않는다.
- 행 단위: 점검 대상의 업무 키(key_columns, 예: 견적번호·차수·업체)마다 한 행이 되게 쓴다. 상세 테이블과 조인해 행이 늘면 `SELECT DISTINCT` 나 `GROUP BY` 로 키 단위로 줄인다. 업무 키는 테이블 문서의 `primary_key` 와 그레인 블록에서 정한다.
- SELECT 목록: key_columns, 기준 날짜, 금액(있으면), 예외 판단에 쓴 값만 넣는다. `SELECT *`, PII 컬럼은 넣지 않는다. 컬럼 alias 는 영문 대문자와 밑줄로 짓는다(서로 겹치지 않게).
- 기간: 기준 날짜 컬럼에 리터럴로 `>= '<시작>' AND < '<종료>'` 를 건다. 리터럴 형식은 컬럼 형식에 맞춘다(`VARCHAR2(8)` → `'20251001'`, `VARCHAR2(6)` → `'202510'`, `VARCHAR2(14)` → `'20251001000000'`, `DATE` → `DATE '2025-10-01'`). `size:l`·`size:xl`·`size:unknown` 테이블은 기간 조건이 반드시 있어야 한다.
- 정상 업무 제외: 패턴 page 의 정상 업무 제외와 `wiki/normal-patterns.md` 의 SQL 조건 가운데 대상 테이블에 해당하는 것을 넣는다. soft-delete 플래그, 유효기간, 플레이스홀더(`'00000000'`, 금액 1/10,000) 제외도 넣는다. 넣지 못한 제외는 「데이터 해석 가정」에 적는다.
- 예외 조건은 조건 단위로 쓴다. 특정 업체·거래선·사원·문서번호 리터럴을 넣지 않는다. 고정 금액 기준이 필요하면 기준 테이블(예: `TI_GRPB_COMPANY_AUDIT_AMT`)이나 같은 데이터의 분포(분석 함수)로 정하고, 숫자를 지어내지 않는다.
- 예외 조건은 부정 패턴 조합의 조건 조각을 5절 유형대로 이은 것이다. 조합에 없는 조건을 예외 조건에 더하지 않는다(정상 업무 제외와 데이터 정리 조건은 공통 조건이다).
- 고의성 신호(`wiki/patterns/index.md` 2절)를 표현할 수 있으면 해당 패턴의 조각에 넣는다. 조합 자체가 신호(같은 행위자 반복, 사후 변경)가 되면 그렇게 적는다.
- 조인은 `sql-query` 「조인」 절대로 쓰고, 문서 없는 조인은 실측 검증 SQL 을 먼저 `sql_run` 으로 실행한다.
- 큰따옴표는 공백·특수문자가 있는 컬럼 이름에만 쓴다(`"LOCAL 요청일시"`). 문자열 값은 작은따옴표로 감싼다.
- `ORDER BY` 는 넣어도 되지만 건수에는 영향이 없다. 넣으면 기준 날짜와 키 순으로 둔다.

## 3. 조합 점검 질의 (`sql_run` 1회)

시나리오 SQL 과 모집단 SQL 의 건수, 행 늘어남, 그리고 조합의 패턴별 건수를 한 문장으로 본다. 패턴별 건수는 모집단 안에서 그 패턴의 조각만 충족하는 키 수다. key_columns 가 둘 이상이면 `||'|'||` 로 잇는다.

```sql
SELECT p.POP_CNT, p.A_CNT, p.B_CNT, h.HIT_CNT, h.KEY_CNT FROM (SELECT COUNT(*) AS POP_CNT, COUNT(DISTINCT CASE WHEN <조각 A> THEN <키> END) AS A_CNT, COUNT(DISTINCT CASE WHEN <조각 B> THEN <키> END) AS B_CNT FROM <모집단 SQL 의 FROM·JOIN> WHERE <모집단 SQL 의 공통 조건>) p CROSS JOIN (SELECT COUNT(*) AS HIT_CNT, COUNT(DISTINCT <키1> || '|' || <키2>) AS KEY_CNT FROM (<시나리오 SQL>)) h
```

- 패턴이 3개면 `C_CNT` 를 더한다. 단일 후보는 `A_CNT`, `B_CNT` 를 빼고 `POP_CNT` 와 `h` 만 본다.
- 집단→행·흐름→행의 조각(`IN (…)`, `EXISTS (…)`)도 CASE 안에 그대로 넣는다.
- 판정은 `AGENTS.md` 8절 표를 따른다. 위에서부터 맞는 첫 행을 따른다.
- `HIT_CNT` 가 0 이면 4절 「조합 축소」로 간다.
- 통과하면 표본을 1회 본다. PII 컬럼을 빼고 키와 판단 값만 본다. 예외 조건이 의도대로 걸렸는지만 확인하고 값은 반환에 옮기지 않는다.

```sql
SELECT <키1>, <키2>, <판단 값> FROM (<시나리오 SQL>) FETCH FIRST 5 ROWS ONLY
```

- 시험 실행에서 고친 시나리오 SQL 은 고친 글자 그대로 다시 점검한다. 점검을 통과한 글자가 제출과 부록 JSON 에 들어간다.

## 4. 수정

| 결과 | 처리 |
|---|---|
| ORA 오류 | skill `sql-query` 의 판정 표대로 고친다 |
| 시간 초과 | 기간 조건이 인덱스를 쓰도록 컬럼에 함수를 씌우지 않았는지, 불필요한 조인이 있는지 확인해 줄인다. 1회만 다시 점검한다 |
| 모집단 0건 | 날짜 리터럴 형식, 코드값 vs 한글 라벨, 플래그 값(Y/N vs 0/1), 조인 방향(INNER → LEFT)을 차례로 확인한다. 조건을 하나씩 뺀 모집단 COUNT 로 원인 조건을 찾는다 |
| 행 늘어남(HIT_CNT > KEY_CNT) | 조인 문서의 `cardinality`·`fanout` 을 보고 DISTINCT·GROUP BY·EXISTS 로 키 단위로 줄인다 |
| 예외 = 모집단 | 예외 조건의 리터럴과 값 형식을 확인한다(값 확인이 필요하면 6절 확인 질의 1회) |
| 조합 축소(`HIT_CNT` 0) | 패턴별 건수(`A_CNT`, `B_CNT`)를 본다. 주 패턴의 건수가 0 보다 크면 다른 조각을 빼고 주 패턴만 남긴 「단일」로 조합 점검 질의를 1회 다시 실행한다. 주 패턴의 건수가 0 이고 다른 패턴만 0 보다 크면 그 패턴을 주 패턴으로 한 단일로 바꾼다(모집단도 그 패턴의 것으로 바꾼다). 모두 0 이면 실패(사유: 기간 안 해당 건 0건) |

수정과 조합 축소는 합쳐 후보 1건당 2회까지다. 같은 SQL 은 다시 실행하지 않는다.

## 5. 부정 패턴 조합 조건

시나리오 후보는 부정 패턴 2~3개의 조합이다(`wiki/patterns/index.md` 4절). 패턴마다 **조건 조각**(그 패턴의 예외 조건을 OKF 컬럼으로 쓴 SQL 조건) 하나를 정하고, 유형에 따라 잇는다. 주 패턴의 모집단이 시나리오의 모집단이다.

| 유형 | 예외 조건 |
|---|---|
| 같은 행 | `<조각 A> AND <조각 B>` |
| 집단→행 | `<행 조각> AND t.<행위자> IN (SELECT s.<행위자> FROM <query_name> s WHERE s.<기준 날짜> >= '<시작>' AND s.<기준 날짜> < '<종료>' AND <행위자 조각>)` (행위자 조각이 집계 조건이면 `GROUP BY s.<행위자> HAVING <조건>`) |
| 흐름→행 | `<조각 A> AND EXISTS (SELECT 1 FROM <다음 단계 query_name> n WHERE <조인 조건> AND <조각 B>)` (짝이 없어야 하는 조건이면 `NOT EXISTS`) |

- 조건 조각은 패턴 page 의 대입 예시, 탐지 기법(SQL 형태), 탐지 방법을 OKF 컬럼으로 쓴 것이다. 코드값은 테이블 문서·`okf/codes/` 의 값만 쓰고, 고정 금액이 필요하면 기준 테이블(예: `TI_GRPB_COMPANY_AUDIT_AMT`)이나 같은 데이터의 분포(분석 함수)로 정한다. 숫자를 지어내지 않는다.
- 서브쿼리의 기간 리터럴은 바깥 질의와 같게 쓴다. 흐름→행에서 다음 단계 거래가 기간 밖으로 넘어갈 수 있으면(예: 기간 말 청구의 다음 기간 반품) 다음 단계 쪽 기간을 「시작일 ~ 종료일 + 업무상 기간(예: 30일)」으로 쓰고 데이터 해석 가정에 적는다.
- 특정 업체·거래선·사원 값을 리터럴로 넣지 않는다.

## 6. 확인 질의 (필요할 때만, `sql_run` 1회)

위임 prompt 의 「확인된 사실」에 없는 값(코드값, 플래그 값, 날짜 형식, 문서 없는 조인의 고아율)이 시나리오 SQL 에 꼭 필요할 때만 쓴다. 확인할 항목을 한 문장에 열로 묶어 한 번에 본다.

```sql
SELECT a.FLAG_Y, a.FLAG_0, b.MIN_LEN, b.MAX_LEN, c.N, c.MATCHED FROM (SELECT SUM(CASE WHEN <플래그> = 'Y' THEN 1 ELSE 0 END) AS FLAG_Y, SUM(CASE WHEN <플래그> = '0' THEN 1 ELSE 0 END) AS FLAG_0 FROM <query_name> WHERE <기간>) a CROSS JOIN (SELECT MIN(LENGTH(<날짜 컬럼>)) AS MIN_LEN, MAX(LENGTH(<날짜 컬럼>)) AS MAX_LEN FROM (SELECT <날짜 컬럼> FROM <query_name> WHERE <날짜 컬럼> IS NOT NULL FETCH FIRST 1000 ROWS ONLY)) b CROSS JOIN (SELECT COUNT(*) AS N, COUNT(p.<키>) AS MATCHED FROM (SELECT <키> FROM <자식 query_name> WHERE <기간> FETCH FIRST 10000 ROWS ONLY) c LEFT JOIN <부모 query_name> p ON p.<키> = c.<키>) c
```

- 필요한 열만 남긴다. 코드값 목록처럼 여러 행이 필요한 확인은 이 질의에 넣지 않고, 테이블 문서와 `okf/references/code-value-samples.md` 로 정하거나 「데이터 해석 가정」에 적는다.
- 확인 질의를 따로 여러 번 실행하지 않는다.
