---
name: sql-query
description: 감사시스템 Oracle 에서 SQL 을 쓰고 실행하는 기술. execute_sql 과 submit_sql 을 언제 어떻게 쓰는지, 테이블 문서 읽는 법, SQL 작성 규칙, 데이터 질문에 답하는 순서, 시나리오 SQL 의 형식과 건수 확인을 담는다. 건수·합계·목록·구조 같은 데이터 질문에 쓰고, Top-down·Bottom-up·Variant 의 시나리오 탐색도 이 skill 의 시나리오 SQL 쓰는 법을 따른다.
---

# sql-query

SQL 을 쓰고 실행하는 방법은 이 skill 한 곳에 있다. 다른 skill 과 sub-agent 는 SQL 도구의 동작을 따로 정하지 않고 여기를 따른다.

## 1. SQL 도구 두 개

| 도구 | 하는 일 | 돌려주는 것 | 쓰는 곳 |
|---|---|---|---|
| `execute_sql(sql_query)` | SQL 을 그대로 실행한다. 실행 시간은 180초까지 | 결과 행 **최대 10행**, 실패하면 오류 메시지. agent 만 보고 사용자 화면에는 남지 않는다 | 값 확인, 조인 실측, 시험 실행, 건수 세기 |
| `submit_sql(final_sql_query)` | 최종 SQL 을 제출해 사용자 화면에 결과 표로 보여 준다 | `grid_data`(결과 행), `total_rows_count`(전체 행 수) | 데이터 질문의 마지막 답에서만 1회(오류면 1회 더) |

- `execute_sql` 은 10행까지만 돌려준다. 건수·합계·금액은 `COUNT`·`SUM` 질의로 직접 센다.
- 행 수 제한, 시간 제한, 제출 결과의 전체 건수 세기는 도구가 한다. SQL 에 안전장치로 `FETCH FIRST` 를 붙이지 않는다. 사용자가 상위 N 개를 요청했을 때만 쓴다.
- 서로 결과에 기대지 않는 `execute_sql` 은 한 응답에서 함께 부른다. 같은 SQL 은 다시 실행하지 않는다.
- `SELECT`·`WITH … SELECT` 만 쓴다. INSERT·UPDATE·DELETE·MERGE·TRUNCATE, DDL, GRANT·REVOKE, PL/SQL·CALL, `DBMS_*`·`UTL_*`, EXPLAIN PLAN, `FOR UPDATE` 는 쓰지 않는다.

## 2. 테이블 문서 읽는 법

테이블 문서는 `okf/schemas/<OWNER>/tables/<테이블>.md`(뷰는 `okf/schemas/<OWNER>/views/<뷰>.md`)다. 경로는 처음부터 `okf/` 로 쓴다. 파일 이름을 추측하지 않고 `okf/schemas/<OWNER>/index.md` 목차로 찾는다.

| 위치 | 확인할 것 |
|---|---|
| frontmatter `query_name` | FROM 에 쓰는 이름. 이것만 쓴다 |
| `primary_key`, `unique_key` | 1행을 가리키는 키. 여러 컬럼이면 모두 함께 |
| `tags` | `size:`(xs<1만, s<100만, m<1천만, l<1억, xl≥1억, unknown), `has:soft-delete`, `has:validity-period`, `has:amount`, `has:pii` |
| `# Schema` | 컬럼이 있는지의 유일한 근거. 이름, 한글명, 타입(문자형 날짜·금액), 키, 코드/참조, 비고(`접근불가`) |
| `# Joins` | 조인 문서 링크, 방향(`→` 자식→부모), 카디널리티, LEFT/INNER 권장 |
| `# T2S 힌트` | 코드 vs 한글 라벨, 날짜 형식, 조인 후보, 임시값 |
| 그레인 | 1행 단위와 업무 키. `near_key` 는 중복 데이터가 있다는 뜻. 「제외」 표기 테이블은 쓰지 않는다 |

- `status: draft` 문서도 근거로 쓴다. "추정", "확인 필요" 표기는 그대로 믿지 않고 컬럼명·타입이나 조회로 확인한다.
- `접근불가` 컬럼은 쓰지 않는다. 적재·메타 컬럼(`LOAD_*`, `RGNT_ID`, `RGTN_DT`, `MDPR_ID`, `MODF_DT`, `BDP_UPDATE_*`, `SDW_LD_DT`)은 업무 기간 조건으로 쓰지 않는다.
- 공백·특수문자가 있는 컬럼명은 큰따옴표로 문서 철자 그대로 쓴다.
- 목차에만 있고 문서 파일이 없는 테이블은 쓰지 않는다.

## 3. SQL 작성 규칙 (Oracle 19c)

- FROM·JOIN 은 `query_name` 만, 컬럼은 `# Schema` 원본 이름만 쓴다. `SELECT *` 는 쓰지 않는다.
- 입력값(기간·코드·업체)은 리터럴로 넣는다. 바인드 변수는 쓰지 않는다. 문자열은 작은따옴표, 빈 문자열 조건은 `IS NULL`.
- 테이블 별칭은 `AS` 없이, 컬럼 별칭에만 `AS`. 비집계 SELECT 컬럼은 모두 GROUP BY 에.
- 데이터 질문에 답하는 SQL 에는 ORDER BY 를 넣는다(질문 기준, 없으면 날짜 → 금액).

| 주제 | 규칙 |
|---|---|
| 문자열 날짜 | 대부분 `VARCHAR2`. 범위는 `>= AND <` 문자열 비교. `VARCHAR2(8)` → `'20250101'`, `VARCHAR2(6)` → `'202501'`, `VARCHAR2(14)` → `'20250101000000'`. WHERE 의 컬럼에 `SUBSTR` 를 씌우지 않는다. `DATE` 타입만 `DATE '2025-01-01'`. 일수 계산이 꼭 필요할 때만 `TO_DATE(c DEFAULT NULL ON CONVERSION ERROR, 'YYYYMMDD')` |
| 상대 기간 | "최근" = 최근 3개월, "작년" = 직전 연도 1/1~12/31. 가정에 밝힌다 |
| 큰 테이블 | `size:l`·`xl`·`unknown` 은 기간·법인 조건 없이 조회하지 않는다. 기간이 없으면 최근 1년. `xl` 은 조건 없는 `COUNT(*)` 도 하지 않는다 |
| 삭제 표시·유효기간 | `has:soft-delete` → 삭제 플래그 조건, `has:validity-period` → 유효기간 조건. `Y/N` 인지 `0/1` 인지는 그 테이블 문서 `# Schema` 비고에서 확인 |
| 임시값 | `'00000000'` 날짜, 금액 1/10,000 등은 기간·비율 계산 전에 뺀다 |
| 문자형 금액 | `TO_NUMBER(c DEFAULT NULL ON CONVERSION ERROR)` 로 바꿔 집계 |
| 통화 | 통화 컬럼이 있으면 통화별로 나누거나 KRW·USD 환산 컬럼을 쓴다. 다른 통화를 그대로 합하지 않는다 |
| 단가 | 한글명에 '단가' 가 있으면 합계 금액이 아니다. 금액 = 단가 × 수량 |
| 코드 vs 라벨 | 같은 상태가 코드인 컬럼과 라벨인 컬럼이 있다. `okf/codes/` 와 T2S 힌트로 확인 |
| 필수 열 | 시나리오 SQL 과 행 단위 목록 조회는 맨 앞에 법인코드, 법인명(테이블에 없으면 법인 기준 테이블을 LEFT JOIN, `okf/t2s/rules/naming.md`), 문제 금액 순으로 둔다. 건수·합계 같은 집계에는 적용하지 않는다 |

자주 쓰는 Oracle 문법: `ADD_MONTHS(d, n)`, `TO_CHAR(d, 'YYYYMMDD')`, `LAST_DAY(d)`, `MEDIAN(x)`, `LAG/LEAD(x) OVER (PARTITION BY … ORDER BY …)`, 문자열 연결 `a || b`.

상황에 따라 더 읽는 문서:

| 상황 | 문서 |
|---|---|
| 데이터 질문에서 테이블을 고를 때 | `skills/sql-query/references/table-selection.md` |
| 두 테이블 이상을 이을 때 | `skills/sql-query/references/joins.md` |
| 질문에 나온 코드·이름이 어느 컬럼 값인지 확인할 때 | `skills/sql-query/references/value-linking.md` |
| 오류, 0행, 시간 초과, 이상한 결과가 나왔을 때 | `skills/sql-query/references/result-handling.md` |
| 고른 테이블의 컬럼·코드값 뜻을 확인할 것이 여럿일 때(테이블 3개 이상, 또는 확인할 코드값 2개 이상) | `term-grounding` 에 맡긴다 |

## 4. 데이터 질문에 답하기

1. **도메인 정보**(필요할 때만): 질문의 용어나 업무 배경을 OKF 문서만으로 알 수 없으면 `domain_knowledge/index.md` 에서 관련 문서를 골라 읽는다.
2. **테이블 찾기**: `okf/domains/index.md` 에서 도메인 page 1~2개를 읽고 「테이블 목록」에서 `skills/sql-query/references/table-selection.md` 대로 고른다. 후보가 3개 이상이거나, 조인이 필요하거나, 확인할 값이 2개 이상이거나, 도메인 page 로 못 찾은 표현이 있으면 `schema-linker` 에 맡긴다.
3. **SQL 쓰고 확인**: 위 작성 규칙대로 쓰고 `execute_sql` 로 실행해 본다.
4. **제출·답변**: `submit_sql` 로 1회 제출하고 `skills/sql-query/references/answer-format.md` 대로 답한다. 0행이어도 조건이 타당하면 제출한다.

어떤 테이블이 있는지, 컬럼·조인 구조가 어떤지처럼 문서만으로 답할 수 있는 질문은 SQL 도구를 부르지 않는다.

## 5. 시나리오 SQL (Top-down·Bottom-up·Variant 시나리오 탐색)

시나리오 SQL 은 보고서 「시나리오 JSON」과 다음 단계 프로그램이 글자 그대로 쓴다.

**형식**

- Oracle `SELECT` 한 줄. `WITH`, 주석, 세미콜론, `FETCH FIRST`, 바인드 변수를 쓰지 않는다. 중간 집계는 `FROM` 안 하위 질의로 쓴다.
- 조건에 걸리는 거래 한 건이 한 행이 되게 쓴다. 맨 앞 세 열은 필수 열이다.
- 기간은 분석 기간을 기준 날짜 형식에 맞춘 리터럴로 쓴다.
- 특정 거래처·사원 값을 조건에 넣지 않는다. 특정 대상에 몰린 것을 보려면 대상별 값을 계산하는 하위 질의를 쓴다.
- `okf/wiki/normal-patterns.md` 「데이터 특성」 표의 SQL 조건(임시값, 삭제 표시, 유효기간 등)을 넣어 실제 거래가 아닌 행을 뺀다.

**드릴다운**: 직전 SQL 을 글자 그대로 `FROM` 안 하위 질의로 두고 바깥에 조건을 더한다. 직전 SQL 안은 고치지 않는다. 새 테이블은 직전 결과의 키로 붙이되 행이 늘지 않게 한다(먼저 집계하거나 `EXISTS`). 맨 앞 세 열은 그대로 둔다. `HIT_CNT` 가 직전 보고서의 결과 수보다 크면 SQL 을 고친다.

**조합 점검**(Top-down 에서 부정 패턴을 2개 이상 묶었을 때): 시나리오 SQL 을 다듬기 전에, 묶은 패턴의 조건을 모두 함께 만족하는 건수(`HIT_CNT`)를 아래 「건수 확인」 질의로 1회 센다.

- 0 보다 크면 그 조합으로 진행한다.
- 0 이면 가설에 가장 적게 기여하는 패턴(가설의 핵심 수법과 가장 덜 관련된 보조 패턴)의 조건을 하나 빼고 다시 센다. 0 보다 커질 때까지 이렇게 하나씩 뺀다.
- 하나만 남으면 「단일」 패턴 시나리오로 진행한다. 뺀 패턴은 보고서 부록 「A-1. 참고한 근거」의 출발점에 빼낸 사유와 함께 적는다.

**건수 확인**: 시나리오 SQL 을 감싸 센다.

```sql
SELECT COUNT(*) AS HIT_CNT, COUNT(DISTINCT <거래 키>) AS KEY_CNT, SUM(<문제 금액>) AS HIT_AMT, COUNT(DISTINCT <대상>) AS HIT_ACTOR_CNT FROM (<시나리오 SQL>)
```

- 0건: 조건이 너무 좁거나 잘못된 것이다. 조건을 고쳐 다시 한다.
- 너무 많음: 감사팀이 하나씩 확인하기 어려울 만큼 많거나 업무 전반의 방식으로 보이면 조건을 좁힌다. 많은지는 테이블 규모와 요청을 보고 판단한다.
- `HIT_CNT` 가 `KEY_CNT` 보다 크면 조인 때문에 행이 늘어난 것이다. SQL 을 고친다.

**걸린 건 살펴보기**: 시나리오 SQL 결과를 대상(법인·거래처·담당자)별 상위 건수·금액과 월별 건수로 집계하고, 금액 큰 행 몇 개를 본다.

- 특정 대상이나 시기에 몰려 있으면 감사 가치가 높다. 전체에 고르게 퍼져 있으면 조건을 좁힌다.
- SQL 오류(조인으로 행이 늘어남, 같은 거래가 중복으로 잡힘, 임시값이 섞임)가 보이면 고친다.
- 문제가 없으면 시나리오로 확정한다. 확정은 후보를 걸러 낸 것이며, 걸린 거래가 부정이거나 정상 업무가 아니라는 것을 확인한 것은 아니다.

확정한 시나리오의 `HIT_CNT` 가 보고서의 결과 수다.

## 항상 지킬 것

- 문서에 없는 테이블·컬럼·코드값을 만들지 않는다.
- 결과를 맞추려고 조건을 빼거나 답 값을 SQL 에 넣지 않는다.
- `usable: false`, `m2m`, 직접 조인 금지 쌍은 조인하지 않는다.
- 같은 오류가 2번 연속이면 구조(CTE, 서브쿼리, 두 번에 나눈 조회)를 바꾼다.