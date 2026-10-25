---
name: sql-query
description: 질문에 필요한 테이블, 컬럼, 값, 조인을 OKF 번들(okf/ 아래 목차, 테이블 문서, 조인 문서, 코드 문서, t2s 규칙)로 확정하고(그라운딩), Oracle SELECT 를 작성해 sql_run 으로 확인한 뒤 sql_submit 으로 1회 제출하는 절차다. 건수, 합계, 목록, 추이, 비율, 최댓값과 최솟값, 존재 여부를 묻는 데이터형 질문에서 쓴다. 범위는 감사시스템 Oracle 19c 의 APPADAMSUSER(업무 데이터)와 SETADAMSUSER(감사 메타) 테이블·뷰다.
---

# sql-query

질문의 표현을 테이블·컬럼·값·조인에 연결하고(그라운딩), SQL 을 작성해 데이터베이스를 조회하는 절차다. 테이블과 컬럼 이름은 OKF 테이블 문서에서 복사만 하고, 확정하지 못한 표현은 모호 후보나 미연결 표현으로 남긴다. 결과 점검과 답변은 `AGENTS.md` 8~9절을 따른다. OKF 문서 링크(`/schemas/...`)는 앞에 `okf` 를 붙여 읽는다.

## 절차

0. 테이블 선택: 아래 「테이블 선택」 절대로 쓸 테이블을 고른다. `AGENTS.md` 10절 위임 기준에 해당하면 「테이블 선택」 3의 후보 확인을 `term-grounding` 에 맡기고, 돌려받은 후보별 확인 표로 직접 고른 뒤 3단계로 간다.
1. 테이블·컬럼 확정(schema linking): 「테이블 선택」에서 고른 테이블의 문서(`okf/schemas/<OWNER>/tables/<TABLE>.md`, 뷰는 `views/`. 이미 읽었으면 다시 읽지 않는다)에서 질문의 대상, 지표, 기간, 조건, 구분을 가리키는 표현마다 `# Schema` 의 컬럼명과 한글명에서 컬럼을 찾고(질문의 표현이 그대로 없으면 같은 뜻의 컬럼을 넓게 찾는다), 아래 「테이블 문서 읽는 법」으로 처리한다. 비슷한 질문이 `okf/t2s/examples/` 나 `okf/references/scenarios.md` 에 있으면 그 사용 테이블과 조건을 견본으로 삼는다.
2. 조인 확정: 여러 테이블이면 테이블 문서의 `# Joins` 절에서 조인 문서를 열어 조건을 정하고, 문서가 없으면 아래 「조인」 절의 2단계 검증을 `sql_run` 으로 한다.
3. 값 확인(value linking): 질문에 나온 값(코드, 번호, 이름, 상태)이 어느 컬럼 값인지, 코드인지 한글 라벨인지 테이블 문서(`# T2S 힌트`, 코드/참조 열)와 `okf/codes/` 문서, `okf/references/code-value-samples.md` 로 정해지지 않으면 `sql_run` 으로 조회해 확인한다(아래 값 확인 SQL 예시).
4. 작성: 작성 규칙에 따라 질문에 답하는 SQL 한 개를 쓴다.
5. 실행: `sql_run` 의 `url` 에 `AGENTS.md` 6절의 접속 URL 을, `sql` 에 SQL 을 넣어 실행한다. 상세 행 조회는 맨 바깥에 `FETCH FIRST 20 ROWS ONLY` 를 붙인다(사용자가 20 이하의 상위 N건을 요청했으면 N). 결과가 1~수십 행인 집계에는 붙이지 않는다.
6. 결과 판정: 실행 결과로 판정 표의 처리를 고른다. 표는 위에서부터 맞는 첫 행을 따른다.
7. 답 형태 확인: 열이 질문이 요구한 값과 맞는지, 건수는 COUNT 인지, 중복 행이 없는지(그레인과 DISTINCT), 최댓값과 최솟값에서 같은 값의 행이 더 있는지(동점), 통화별로 나뉘었는지 확인하고 `AGENTS.md` 8절 결과 점검을 한다. 어긋나면 SQL 을 고친다.
8. 제출(반드시 마지막에 1회): 7단계까지 마쳤으면 `sql_submit` 을 부른다. 7단계까지 확인한 SQL 은 제출 전에 다시 점검하지 않는다(제출 오류는 아래대로 1회 고쳐 다시 낼 수 있다). 질문에 답하는 SQL 을 5단계의 `FETCH FIRST 20 ROWS ONLY` 없이 `sql_submit` 의 `final_sql_query` 로 넣어 1회 제출한다. 사용자가 요청한 상위 N건 제한만 남긴다(「작성 규칙」의 행 수). 상세 행 목록이면 답변에 `total_rows_count` 로 전체 건수를 밝힌다. 시험 실행이 0행이어도 조건이 타당하면 제출한다. 제출 결과에 오류가 있으면 오류가 가리키는 곳을 고쳐 1회 더 제출하고, 그래도 실패하면 오류 문구로 답한다.

- 구조형 질문(컬럼, 조인)은 해당 테이블 문서와 조인 문서만 읽고 답하며 SQL 도구를 부르지 않는다.

## 테이블 선택

쓸 테이블은 문서만 보고 아래 순서로 고른다. 우선순위는 `okf/t2s/rules/table-selection.md` 를 읽고 따르며, 이 절은 그 규칙을 적용하는 방법이다. 고르는 일은 main agent 가 한다. subagent 는 넘겨받은 테이블이나 후보를 쓰고 이 절차로 다시 고르지 않는다.

1. 후보 모으기
   - 업무에 맞는 도메인 page(`okf/domains/<도메인>.md`, 목록은 `okf/domains/index.md`)를 고른다. 두 업무에 걸치면 2개까지 본다.
   - 그 page 의 「## 테이블 목록」 표(`| 테이블 | 유형 (table_type) | 설명 (table_rule) |`)에서 아래를 모두 후보로 적는다. 하나만 고르지 않는다.
     - 설명이 질문의 대상·지표·조건과 맞는 테이블
     - 유형이 「종합리포트」·「리포트」인 테이블 전부. 여러 테이블을 합친 결합 테이블이라 설명이 출처 위주로 적혀 있어도 넣는다
   - 도메인 page 로 찾지 못한 표현이 있으면 그 표현만 OWNER 목차(`okf/schemas/<OWNER>/index.md`)에서 후보를 더한다.
   - 「시나리오」 유형과 테이블 문서 링크가 없는 테이블(예: 「(접근 범위 밖)」 표시)은 뺀다.
   - 도메인 page 의 「## 테이블과 조회 기준」 글 목록, 「## 관련 업무 지식」(`okf/glossary/biz-*.md`)과 그 「관련 테이블」, 용어집은 후보를 모으는 데 쓰지 않는다. 업무 뜻이 헷갈릴 때만 읽는다.
2. 순서 정하기: `table-selection.md` 의 유형 순서로 후보를 늘어놓는다. 유형은 표의 「유형 (table_type)」 칸(빈칸은 유형 없음)에서, OWNER 목차에서 더한 후보는 테이블 문서 frontmatter 의 `table_type` 에서 읽는다.
3. 고르기(앞 순서부터)
   - 앞선 후보부터 테이블 문서를 열어(한 응답에 2~3개씩), 필요한 개념(대상, 지표, 조건, 구분, 기간)마다 그것을 담는 컬럼이 `# Schema` 에 있는지 본다. 한글명이 질문 표현과 글자로 같지 않아도 같은 뜻이면 담는 것으로 본다.
   - 모든 개념을 담는 첫 후보를 쓴다.
   - 앞선 후보를 건너뛸 수 있는 이유는 「담지 못하는 개념이 있다」 하나다(`table-selection.md` 가 따로 정한 예외는 따른다). 아래는 건너뛸 이유가 아니다: 테이블이 질문보다 넓은 범위(다른 업무 단계)까지 담고 있다, 다음 후보가 더 딱 맞아 보인다, 다음 후보의 컬럼 한글명이 질문 표현과 더 같다, 다음 후보에서 먼저 값 확인을 해 봤다.
   - 모든 개념을 담는 후보가 없으면 가장 많이 담는 앞선 후보를 기준으로 하고, 모자란 개념만 다음 후보에서 조인으로 가져온다(「조인」 절).
   - 테이블 문서는 한 작업에서 10개까지 연다. 그 안에서 앞선 후보부터 확인한다. 목록에 링크가 있어도 문서 파일이 없으면(읽기 실패) 그 후보는 「문서 없음」으로 적고 건너뛴다(폴더 목록으로 미리 확인하지 않는다).
   - 후보가 3개 이상이거나 값을 확인할 코드값이 2개 이상이면(`AGENTS.md` 10절) 이 확인을 `term-grounding` 에 맡긴다. 위임 prompt 에 2의 순서대로 후보 목록(query_name, 유형, 문서 경로)을 넣고, 돌려받은 「후보별 확인 표」를 이 3의 기준으로 직접 읽어 고른다. 고르는 일은 맡기지 않는다.
4. 값 확인은 고른 뒤에: 질문에 나온 값(이름, 코드, 번호)은 고른 테이블에서 확인한다(절차 3단계). 고른 테이블에서 그 값이 0건이고 다음 후보에는 있으면 다음 후보로 바꾸고, 그 사실을 기록에 적는다.
5. 기록: 고른 결과를 `테이블 선택: 후보 <A>(<유형>), <B>(<유형>), … / 채택 <X>(<유형>) / 건너뛴 이유: <건너뛴 후보마다 담지 못한 개념 또는 값 0건>` 한 줄로 남긴다. 답변 「근거」에 적는다(`AGENTS.md` 9절).

## 그라운딩 판정

| 상황 | 처리 |
|---|---|
| 후보 1개 | 그 테이블·컬럼으로 확정한다 |
| 후보가 여럿이지만 업무 의미가 같음 | 「테이블 선택」 절대로 하나를 고르고, 고른 해석을 답변에 밝힌다 |
| 업무 의미가 다른 후보가 2개 이상 남음 | 후보와 구분 기준을 모호 후보로 남긴다. main agent 는 가장 일반적인 해석으로 SQL 을 쓰고, `sql_submit` 을 마친 뒤 답변에서 다른 해석이 맞는지 묻는다 |
| 질문의 표현이 문서에 그대로 없음 | 용어집과 후보 테이블의 `# Schema` 한글명을 넓게 보고 같은 뜻의 컬럼으로 확정한다. 답변에 질문의 표현과 실제로 쓴 컬럼을 밝힌다 |
| 목차에는 있으나 테이블 문서 파일이 없음 | 그 테이블은 쓰지 않는다. 다른 후보가 없으면 미연결 표현으로 남기고 「테이블 문서 없음」을 적는다 |
| 후보 없음 | 같은 뜻의 컬럼도, 값 확인으로도 찾지 못하면 미연결 표현으로 남기고 확인한 경로를 밝힌다. main agent 는 찾은 조건만으로 SQL 을 써서 `sql_submit` 을 마치고, 답변에서 그 조건을 빼고 조회했다는 것을 밝히고 다시 묻는다 |

## 테이블 문서 읽는 법

| 위치 | 확인할 것 |
|---|---|
| frontmatter `query_name` | FROM 에 쓰는 이름(`OWNER.OBJECT`). 이것만 쓴다 |
| frontmatter `primary_key` / `unique_key` | 1행을 식별하는 키. 여러 컬럼이면 모두 함께 써야 유일하다 |
| frontmatter `tags` | `size:`(xs<1만, s<100만, m<1천만, l<1억, xl≥1억, unknown), `has:pii`, `has:soft-delete`, `has:validity-period`, `has:amount`, `class:`, `domain:`, `access:select-partial` |
| frontmatter `table_type`, `business_area`, `business_detail` | 테이블 선택 우선순위와 업무 영역 |
| frontmatter `row_count`, `last_analyzed` | 통계 기준 행 수(근사값) |
| `# Schema` 표 | **컬럼 존재 여부의 유일한 근거.** 컬럼(원본 이름), 한글명, 타입(문자형 날짜·금액 여부), NULL, 키(`PK(n)`, `UK`, `IDX`), 코드/참조(코드 후보·조인 후보), 비고(`PII`, `접근불가`) |
| `# Joins` 절 | 이 테이블에 걸린 조인 문서 링크와 방향(`→` 자식→부모, `←` 부모→자식), 카디널리티, 신뢰도, LEFT/INNER 권장 |
| `# T2S 힌트` 절 | 사람·실측이 보탠 업무 지식(코드 vs 한글 라벨, 날짜 형식, 조인 후보, 플레이스홀더 값) |
| 그레인 블록(`### 그레인 (DB 실측 …)`) | 1행 단위와 업무 키. `near_key` 는 업무 키가 있으나 중복 데이터가 있다는 뜻이다. 「제외」 표기 테이블(TR_ 시나리오 추출, HYBR)은 조회 대상이 아니다 |

| 표기 | 처리 |
|---|---|
| 비고 `PII` | SELECT 목록에 넣지 않는다. 사용자가 값을 직접 지정한 경우의 WHERE 조건이나 COUNT 로만 쓴다 |
| 비고 `접근불가` | 쿼리에 쓰지 않는다 |
| 컬럼명에 공백·특수문자(예: `LOCAL 요청일시`) | 큰따옴표로 감싸 문서 철자 그대로 쓴다(`"LOCAL 요청일시"`). 한글만으로 된 이름(`선정여부`)은 따옴표 없이 그대로 쓴다 |
| "(사람이 보완: …)" 빈 개요 | 아직 비어 있을 뿐 오류가 아니다. Schema 와 T2S 힌트로 판단한다 |
| "추정", "~로 보임", "확인 필요", "?" | 그대로 SQL 설계의 근거로 쓰지 않는다. 컬럼명, 한글명, 타입으로 판단하거나 `sql_run` 으로 값을 조회해 확인한다. "쓰지 말라"는 방향의 경고는 따른다 |
| 적재·메타 컬럼(`LOAD_*`, `RGNT_ID`, `RGTN_DT`, `MDPR_ID`, `MODF_DT`, `BDP_UPDATE_*`, `SDW_LD_DT`) | 업무 기간 조건으로 쓰지 않는다 |
| 이름이 `_H`, `_HISTORY`, `_RAW`, `_2` 로 끝나는 사본·이력 테이블 | 기본 테이블을 쓰고, 이력이 필요할 때만 쓴다 |

## 조인

근거 없는 조인은 하지 않는다. 근거는 번들 문서와 `sql_run` 실측으로 입증하며, 아래 3단계를 순서대로 따른다. 조인 규칙은 이 절이 기준이다.

1. 문서 있는 조인(우선): `okf/joins/index.md`(허브 테이블, 직접 조인 금지 쌍)를 확인하고, 테이블 문서 `# Joins` 절의 조인 문서를 열어 frontmatter 를 따른다.
   - `usable: true` → `join_condition` 을 그대로 쓰고 `join_type_hint`(LEFT/INNER)를 따른다.
   - `usable: conditional` → `join_filter` 를 반드시 함께 쓴다.
   - `usable: false`, `cartesian_risk: m2m` → 조인하지 않는다(3단계의 2단계 쿼리로 바꾼다).
   - `fanout` 이 크면(부모 1건당 자식 수백 이상) 상세 행을 조인하지 않고 필요한 단위로 먼저 집계한 뒤 조인한다.
2. 문서 없는 조인(근거와 실측이 있을 때만): 아래 세 가지가 모두 성립해야 쓴다.
   - ① 컬럼 근거: 조인 키가 양쪽 `# Schema` 에 실제로 있고 이름·타입이 같다(대개 `*_CD`, `*_NO`, `*_ID`).
   - ② 부모 유일성: 부모 쪽 키가 `# Schema` 키 열의 `PK`·`UK` 표기나 T2S 힌트의 실측으로 유일하다.
   - ③ 실측: 아래 검증 SQL 을 이번 조건 범위에서 `sql_run` 으로 실행해 고아율(자식 키가 부모에 없는 비율)이 낮은지 본다(높으면 INNER/LEFT 방향을 다시 본다). 문서에 PK·UK 표기가 없으면 부모 중복 SQL 도 실행해 0행인지 본다. 검증 SQL 에는 PII 가 아닌 키 컬럼만 쓴다. 시간 초과면 검증하지 못한 것으로 보고 3단계로 간다.
   - T2S 힌트에 「조인 후보 — 조인 문서 미작성」처럼 적힌 관계는 ①②가 이미 충족된 것이므로 ③의 고아율 검증 1건만 통과하면 쓴다.
   - 세 가지가 성립하면 N:1(자식→부모) 조인은 행이 늘지 않으므로 한 SQL 에 조인해도 된다. 근거에 `추측 조인(번들 문서 없음): <A>.<key> = <B>.<key>, 근거=<컬럼 일치+부모 PK/실측>, 고아율=<n>%` 를 적는다. 조인 문서는 만들지 않는다.
3. 조인 불가: ①②를 문서로 입증하지 못하거나, 양쪽이 모두 상세 테이블이라 M:N 이 의심되거나, 검증 SQL 이 시간 초과이거나, `usable: false`·`cartesian_risk: m2m`·직접 조인 금지 쌍이면 조인하지 않는다. 대신 2단계 쿼리(첫 쿼리로 연결 키를 뽑아 두 번째 쿼리의 `IN (...)` 조건으로)를 쓴다. `IN` 목록이 수백 건을 넘으면 조건을 좁힌다.

- 복합 키는 모든 컬럼을 조인 조건에 넣는다(일부 키만으로 조인하지 않는다).
- 허브 테이블(`TI_GRPF913`, `TI_GRPF911` 등)을 지나는 다단계 조인은 한 번에 2단계까지만 연결하고 단계마다 fanout 을 확인한다.
- 조인한 뒤에도 PII, 행 수, 큰 테이블, soft-delete 규칙은 그대로 적용된다.

조인 실측 검증 SQL(문서 없는 조인일 때만):

```sql
SELECT COUNT(*) AS n, COUNT(p.<KEY>) AS matched
FROM (SELECT <KEY> FROM <CHILD query_name> WHERE <질문 조건> FETCH FIRST 10000 ROWS ONLY) c
LEFT JOIN <PARENT query_name> p ON p.<KEY> = c.<KEY>
```

```sql
SELECT <KEY>, COUNT(*) AS cnt FROM <PARENT query_name> WHERE <조건>
GROUP BY <KEY> HAVING COUNT(*) > 1 FETCH FIRST 5 ROWS ONLY
```

## 값 확인 SQL 예시

테이블 문서를 먼저 읽고, 문서로 정해지지 않는 것(값이 들어 있는 컬럼, 코드값 목록, 코드인지 한글 라벨인지, 값의 형식)은 `sql_run` 으로 조회해 확인한다. 아래는 자주 쓰는 형태이며 필요에 맞게 바꿔 쓴다. 목록을 보는 조회에는 `FETCH FIRST n ROWS ONLY` 를 붙인다. `<…>` 자리는 꺾쇠괄호까지 바꾼다. `size:l`·`size:xl` 테이블은 기간 같은 조건을 함께 넣는다.

값 일치(코드, 번호): 후보 컬럼이 여럿이면 한 번에 확인한다. 1 이 나온 컬럼이 그 값의 컬럼이다.

```sql
SELECT MAX(CASE WHEN <후보 컬럼1> = '<값>' THEN 1 ELSE 0 END) AS <후보 컬럼1>,
       MAX(CASE WHEN <후보 컬럼2> = '<값>' THEN 1 ELSE 0 END) AS <후보 컬럼2>
FROM <query_name>
WHERE <후보 컬럼1> = '<값>' OR <후보 컬럼2> = '<값>'
```

부분 일치(이름): 값 일치로 찾지 못한 이름 표현에만 쓴다. PII 컬럼에는 쓰지 않는다.

```sql
SELECT DISTINCT <후보 컬럼> FROM <query_name>
WHERE UPPER(<후보 컬럼>) LIKE UPPER('%<값>%')
ORDER BY <후보 컬럼>
FETCH FIRST 10 ROWS ONLY
```

코드값 목록(코드 컬럼의 실제 값, 코드인지 라벨인지):

```sql
SELECT <코드 컬럼>, COUNT(*) AS cnt FROM <query_name>
WHERE <기간 조건>
GROUP BY <코드 컬럼> ORDER BY cnt DESC
FETCH FIRST 20 ROWS ONLY
```

공통코드 해석: 컬럼 코멘트나 T2S 힌트에 적힌 코드 유형으로 `SETADAMSUSER.TC_CF_COMM_CODE` 를 조회한다. 이 테이블의 삭제 플래그 `DELETE_YN` 실제값은 `'0'`(정상)/`'1'`(삭제)이다. 컬럼은 `okf/schemas/SETADAMSUSER/tables/TC_CF_COMM_CODE.md` 의 Schema 에서 확인한다.

날짜 형식(형식이 문서에 없을 때):

```sql
SELECT MIN(LENGTH(<날짜 컬럼>)) AS min_len, MAX(LENGTH(<날짜 컬럼>)) AS max_len, MIN(<날짜 컬럼>) AS min_val, MAX(<날짜 컬럼>) AS max_val
FROM (SELECT <날짜 컬럼> FROM <query_name> WHERE <날짜 컬럼> IS NOT NULL FETCH FIRST 1000 ROWS ONLY)
```

- 값 일치가 0행(또는 모두 0)이면 다른 후보 컬럼을 확인하고, 이름 표현이면 부분 일치를 1회 실행한다. 그래도 없으면 미연결 표현으로 남긴다. 값이 없다는 것만으로 데이터가 없다고 답하지 않는다.
- 부분 일치 결과가 여러 개면 확정하지 않고 모호 후보로 남긴다.

## 작성 규칙

SQL 실행과 검증은 `sql_run`(시험 실행)과 `sql_submit`(제출)으로만 하며, 실행 방법·행 제한·이름·조인에 관한 규칙은 이 skill 이 기준이다. OKF 문서(예제, 근거 문서)에 나오는 `scripts/sql_ro.py`, 종료 코드, `--max-rows`, 바인드 변수(`:p_from`) 같은 표기는 번들을 만든 환경의 것이므로 따르지 않는다. 날짜, soft-delete·유효기간, PII, 결과 해석은 아래 요지로 정해지지 않을 때만 `okf/t2s/rules/` 의 해당 문서(`date-handling.md`, `soft-delete-validity.md`, `pii.md`, `result-interpretation.md`)를 읽는다. 테이블 선택 규칙(`table-selection.md`)은 「테이블 선택」 절에서 항상 읽는다.

- 조회 전용: Oracle SQL 을 SELECT 또는 WITH … SELECT 로 시작하는 한 문장만, 세미콜론 없이 쓴다. INSERT·UPDATE·DELETE·MERGE·TRUNCATE, CREATE·ALTER·DROP·COMMENT ON, GRANT·REVOKE, PL/SQL 블록(DECLARE·BEGIN)·CALL, `DBMS_*`·`UTL_*` 호출, EXPLAIN PLAN, FOR UPDATE 는 쓰지 않는다. 집계(COUNT, SUM, GROUP BY)는 조회이므로 쓴다. 사용자가 데이터 수정·생성을 요구하면 SQL 을 만들지 않고 조회 전용이라 할 수 없다고 답한다.
- 이름: FROM·JOIN 이름은 테이블·뷰 문서 frontmatter 의 `query_name`(`OWNER.OBJECT`, 예: `APPADAMSUSER.TI_BQMS810`)만 쓴다. OWNER 를 빼거나 시노님·뷰 이름을 추측하지 않는다. 컬럼은 `# Schema` 표의 원본 이름 그대로 쓰고(한글 컬럼명 `선정여부` 도 그대로), 표에 없는 컬럼은 없는 것으로 본다. 공백·특수문자가 있는 컬럼만 큰따옴표로 감싼다. 테이블 별칭은 `AS` 없이(`FROM APPADAMSUSER.TI_BQMS810 a`), 컬럼 별칭에만 `AS` 를 쓴다. `SELECT *` 는 쓰지 않는다.
- `LIMIT` 대신 `FETCH FIRST n ROWS ONLY` 를 쓴다. 문자열 값은 작은따옴표로 감싸고, 빈 문자열 조건은 `IS NULL` 로 쓴다(Oracle 에서 `''` 는 NULL).
- 바인드 변수(`:p_from`, `:p_ym`)는 `sql_run`, `sql_submit` 에서 값을 받을 수 없으므로 쓰지 않고, 기간·코드·업체 같은 입력값은 리터럴로 넣는다. `okf/t2s/examples/` 의 예제 SQL 은 견본으로만 쓰고, 그 안의 `:p_from` 같은 자리와 세미콜론, `BETWEEN` 날짜 범위는 이 규칙대로 바꾼다.
- 집계는 `GROUP BY` 를 쓰고, SELECT 의 비집계 컬럼을 모두 GROUP BY 에 넣는다. 집계식과 계산식에는 사용자가 이해할 수 있는 alias 를 붙인다.
- CTE 와 서브쿼리를 쓸 수 있지만 기반 데이터가 어떤 실제 테이블에서 오는지 분명해야 한다. 여러 지표가 필요해도 하나의 SQL 에 담는다(`sql_submit` 은 1회).
- **질문에 답하는 SQL 에는 모두 ORDER BY 를 넣는다(값 확인과 데이터 확인용 조회는 예외).** 정렬 기준은 질문에 명시된 것, 없으면 날짜 → 금액 → 시간 순이며, 결과에 없는 컬럼은 건너뛴다.
- 질문에 기여하지 않는 테이블은 넣지 않는다.

이 데이터베이스의 필수 규칙:

- 문자열 날짜(`okf/t2s/rules/date-handling.md`): 날짜 컬럼 대부분이 `VARCHAR2` 다. Schema 의 타입과 T2S 힌트의 형식대로 문자열로 비교하고, 범위는 `>= AND <` 로 쓴다.
  - `VARCHAR2(8)` = 'YYYYMMDD' → `STD_DT >= '20250101' AND STD_DT < '20260101'`
  - `VARCHAR2(14)` = 'YYYYMMDDHH24MISS' → WHERE 조건은 `'20250101000000'` 형식의 문자열 범위로 비교한다(컬럼에 `SUBSTR` 을 씌우지 않는다). 일자·월 단위로 묶을 때만 SELECT·GROUP BY 에서 `SUBSTR(컬럼, 1, 8)` 을 쓴다
  - `VARCHAR2(6)` = 'YYYYMM' → `STD_YM >= '202501' AND STD_YM < '202601'`
  - `DATE` 타입만 `DATE '2025-01-01'` 이나 `TO_DATE` 로 비교한다. 날짜 컬럼에 함수를 씌우는 것은 일수 계산처럼 꼭 필요할 때만 한다(`TO_DATE(컬럼 DEFAULT NULL ON CONVERSION ERROR, 'YYYYMMDD')`).
- 상대 기간: "최근", "요즘" 은 최근 3개월, "작년" 은 직전 연도 1/1~12/31 로 해석하고 가정에 밝힌다. 사용자가 기간을 명시하면 그 기간을 쓴다. 현재 날짜는 `SYSDATE` 기준이다(`TO_CHAR(ADD_MONTHS(SYSDATE, -3), 'YYYYMMDD')`).
- 큰 테이블: `size:l`, `size:xl`, `size:unknown`(통계 없음) 테이블은 기간·법인·사이트·사업부 같은 조건이 없으면 전수 조회를 만들지 않는다. 질문에 기간이 없으면 최근 1년을 기본으로 넣고 가정에 밝힌다. 조건에는 파티션·인덱스 열(대개 기간, 법인 코드)을 넣는다. `size:xl` 은 조건 없는 `COUNT(*)` 도 하지 않는다. 시간 초과는 「판정」 표대로 처리한다.
- 행 수: `sql_run` 의 상세 행 조회는 기본 20행(`FETCH FIRST 20 ROWS ONLY`)이고, 결과가 1~수십 행인 집계에는 행 제한을 걸지 않는다. `sql_submit` 에는 20행 제한을 붙이지 않고 사용자가 요청한 상위 N건 제한만 남긴다. 전체 행을 보여 달라는 요청("전체", "모든", "N행")이 명시적일 때만 답변에 전체를 다루며, 그때도 큰 테이블은 조건을 함께 넣는다. `size:xs`·`size:s` 마스터의 전수 목록이 수천 행이면 일부만 보여 주고 가정에 밝힌다.
- soft-delete·유효기간·플레이스홀더(`okf/t2s/rules/soft-delete-validity.md`): `has:soft-delete` 면 삭제 플래그 필터를, `has:validity-period` 면 유효기간 조건(질문에 시점이 없으면 현재 유효)을 넣는다. `'00000000'` 같은 날짜, 금액 1/10,000 같은 플레이스홀더는 기간·비율 계산 전에 뺀다. 플래그가 `Y/N` 인지 `0/1` 인지는 `okf/references/code-value-samples.md` 로 확인한다.
- PII(`okf/t2s/rules/pii.md`): 비고 `PII` 컬럼은 SELECT 목록에 넣지 않는다.
- 문자형 금액·수량: 타입이 `VARCHAR2` 인 금액·수량은 `TO_NUMBER(컬럼 DEFAULT NULL ON CONVERSION ERROR)` 로 바꿔 집계한다.
- 통화: 통화 컬럼(`CURR`, `CURRENCY`, `CURR_CD`, `LOCAL_CURR` 등)이 있는 금액은 통화별로 GROUP BY 하거나 KRW·USD 환산 금액 컬럼으로 집계한다. 서로 다른 통화를 그대로 합산하지 않는다. 환율 테이블 조인은 직접 조인 금지 쌍(`TI_MT_EXCHRATE_YM/YW ⇄ TI_MT_EXCHRATE`)을 피한다.
- 단가: 한글명에 '단가' 가 들어간 컬럼은 합계 금액이 아니다. 금액이 필요하면 단가 × 수량으로 계산한다.
- 코드값 vs 라벨(`okf/t2s/rules/result-interpretation.md`): 같은 상태라도 코드(`BDDO001`)로 저장된 컬럼과 한글 라벨(`선정완료`)로 저장된 컬럼이 있다. `okf/codes/` 와 T2S 힌트로 확인한다.

Oracle 문법 참고:

| 용도 | 문법 |
|---|---|
| 개월 더하기 | `ADD_MONTHS(d, n)` |
| 일 더하기 | `d + n` |
| 날짜 → 문자열 | `TO_CHAR(d, 'YYYYMMDD')` |
| 문자열 → 날짜(형식 오류는 NULL) | `TO_DATE(s DEFAULT NULL ON CONVERSION ERROR, 'YYYYMMDD')` |
| 문자열 연결 | `a \|\| b` |
| 행 수 제한 | `FETCH FIRST n ROWS ONLY` |
| 월의 마지막 날 | `LAST_DAY(d)` |
| 중앙값 | `MEDIAN(x)`, `PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY x)` |
| 직전 행 값 | `LAG(x) OVER (PARTITION BY … ORDER BY …)` |

작성 후 실행 전 점검:

```text
Concept        Covered By
지표           TI_BQMS005_INFA_QT.LOCAL_AMT (LOCAL총액, 통화 LOCAL_CURR 별 집계)
기간           TI_BQMS005_INFA_QT.제출HQ (VARCHAR2(14) YYYYMMDDHH24MISS, 제출시각_한국시각)
구분           TI_BQMS005_INFA_QT.REQ_TYPE (견적구분, 값은 sql_run 으로 확인)
```

- 질문의 지표, 기간, 구분, 조건이 모두 실제 컬럼에 연결되었는가. 누락이 있으면 실행하지 않고 고친다.
- 모든 컬럼이 해당 테이블 문서의 `# Schema` 에 있고, 같은 이름의 컬럼을 다른 테이블에서 가져오지 않았는가.
- 모든 JOIN 에 조인 조건이 있고, 조인 근거(문서 또는 실측)가 있으며, 조인으로 SUM·COUNT 가 부풀지 않는가.
- 문자열 날짜, 큰 테이블 조건, soft-delete·유효기간·플레이스홀더, 문자형 금액, 통화, PII 규칙을 반영했는가.

## 판정

| 결과 | 처리 |
|---|---|
| 오류 ORA-00904(잘못된 식별자) | 컬럼명과 alias 를 테이블 문서 Schema 와 문자 단위로 대조해 고친다. 공백·특수문자가 있는 컬럼은 큰따옴표로 감쌌는지 확인한다 |
| 오류 ORA-00942(테이블 없음) | `query_name` 의 OWNER 와 테이블명 표기를 테이블 문서와 대조해 고친다 |
| 오류 ORA-01031(권한 없음) | `access:select-partial` 테이블의 `접근불가` 컬럼을 썼는지 확인하고 뺀다 |
| 오류 ORA-01722(숫자 변환), ORA-01841·ORA-01843·ORA-01861(날짜 형식) | 문자형 수치는 `TO_NUMBER(… DEFAULT NULL ON CONVERSION ERROR)`, 문자열 날짜는 문서의 형식대로 문자열로 비교한다 |
| 그 밖의 문법 오류(ORA-00907, ORA-00933, ORA-00936, ORA-00979 등) | 괄호 짝, 콤마, 문자열 따옴표, 키워드 띄어쓰기, GROUP BY 누락을 고친다 |
| 시간 초과, ORA-01013 | 같은 SQL 을 반복하지 않는다. 질문 의미를 바꾸지 않는 범위에서 기간이나 법인·사이트 조건을 좁히고 불필요한 조인과 중간 집계를 뺀다. 그래도 실패하면 `SAMPLE` 표본이나 COUNT 집계로 한 번만 바꾼다 |
| 0행 | 데이터 없음으로 단정하지 않는다. ① 조건 오타·값 형식(문자열 날짜 형식, 코드값 vs 한글 라벨) ② soft-delete 플래그 방향(`Y/N` vs `0/1`), 유효기간 조건 ③ VPD·권한 ④ 실제로 데이터가 없는 경우 순서로 확인한다. 고칠 근거가 없으면 0행을 정상 결과로 보고 제출한다 |
| 결과가 `FETCH FIRST` 제한에 걸림 | 받은 행은 일부다. 건수와 합계는 COUNT 와 SUM 으로 구하고, 목록은 제출 결과의 `total_rows_count` 로 전체 건수를 밝힌다 |
| 행 수가 통계(`row_count`) 대비 비정상적으로 적음, 값이 `********` | VPD·마스킹 가능성을 「확인 필요」에 적는다 |
| 정상 결과 | 7단계로 간다 |
| 도구 실패(결과 없이 실패) | `sql_run` 이 결과 없이 실패했다(연결 실패 등). 1회만 다시 부르고, 다시 실패하면 더 고치지 않고 그때까지 가장 나은 SQL 로 `sql_submit` 을 부른다 |

## 상한

- SQL 호출: main agent 의 `sql_run` 은 질문 1건당 10회까지다. `sql_submit` 은 1회이며, 제출 결과가 오류일 때만 고쳐서 1회 더 제출한다. subagent(term-grounding)의 `sql_run` 은 이 횟수에 들어가지 않는다(subagent 정의의 상한을 따른다). 10회를 다 쓰면 더 고치지 않고 그때까지 가장 나은 SQL 로 `sql_submit` 을 부른다.
- 대부분은 `sql_run` 1~2회와 `sql_submit` 1회로 끝내는 것을 목표로 한다.
- 테이블 문서: main agent 가 직접 읽는 테이블 문서는 질문 1건당 10개까지다. 핵심 컬럼이나 조인 키를 찾지 못했을 때만 더 읽는다.
- 재실행: 같은 SQL 은 다시 실행하지 않는다. 같은 오류 유형이 2회 연속이면 다른 테이블 조합이나 다른 구조(CTE, 서브쿼리, 2단계 쿼리)로 바꾼다. 재시도할 때 유효했던 테이블과 조건은 유지한다.
- 상한 도달: 그때까지 가장 나은 SQL 로 `sql_submit` 을 1회 하고, 「확인하지 못함」과 확인한 문서, 오류나 빈 결과 사실로 답한다.

## 금지

- 답 값을 SQL 에 직접 넣거나 질문의 조건을 빼서 결과를 만들지 않는다. 조건을 뺀 SQL 은 0행의 원인을 찾을 때와, 문서와 값 확인으로 찾지 못한 조건을 빼고 제출할 때만 쓴다.
- OKF 번들에 없는 테이블, 컬럼, 조인, 코드값을 만들어 쓰지 않는다.
