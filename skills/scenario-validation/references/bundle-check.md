# 데이터 사전 대조

`scenario_sql` 이 쓰는 객체·컬럼·조인·코드값이 데이터 사전 문서(`okf/schemas/**`, `okf/joins/**`)에 근거가 있는지 확인하고 `bundle_check` 를 채운다. SQL 은 고치지 않는다.

## 1. SELECT 전용 점검

- 단일 `SELECT` 또는 `WITH ... SELECT` 문이어야 한다.
- 다음 중 하나라도 있으면 `select_violation: true`, **실행하지 않는다**: DML(`INSERT`/`UPDATE`/`DELETE`/`MERGE`), DDL(`CREATE`/`ALTER`/`DROP`/`TRUNCATE`), PL/SQL 블록(`BEGIN`/`DECLARE`), `DBMS_*` 호출, `FOR UPDATE`, 다문장(문장 중간 세미콜론).
- 끝의 세미콜론 1개는 위반이 아니다 (실행할 때만 뗀다).

## 2. 객체명 점검 → `invalid_query_names`

- FROM/JOIN 의 각 객체를 데이터 사전 문서 frontmatter 의 `query_name`(`OWNER.OBJECT`)과 대조한다. 문서 위치: `okf/schemas/<OWNER>/tables/<OBJ>.md` 또는 `okf/schemas/<OWNER>/views/<OBJ>.md`.
- 다음은 `invalid_query_names` 에 SQL 에 적힌 그대로 넣는다: 데이터 사전 문서가 없는 객체, 시노님, OWNER 없이 쓴 이름, `query_name` 과 OWNER 가 다른 이름.
- CTE 이름(`WITH x AS`)과 인라인 뷰 별칭은 객체가 아니므로 제외한다.
- 하나라도 있으면 **실행하지 않는다**.

## 3. 컬럼 점검 → `missing_columns`

- 객체별로 SQL 에서 쓴 컬럼(SELECT, WHERE, JOIN, GROUP BY, ORDER BY, 분석함수 PARTITION/ORDER)이 그 문서의 `# Schema` 표에 있는지 확인한다.
- 없으면 `"OWNER.OBJECT.COLUMN"` 형식으로 넣는다.
- 인라인 뷰·CTE 안에서 새로 만든 별칭 컬럼(예: `SELECTION_CNT`)은 제외한다.
- `invalid_query_names` 에 들어간 객체의 컬럼은 확인할 수 없으므로 넣지 않는다 (객체명 위반으로 이미 기록됨).
- 컬럼 누락은 실행을 막지 않는다. 실행하면 `ORA-00904` 가 나고, 그 오류가 근거가 된다.

## 4. 조인 점검 → `unsafe_joins`

조인 조건이 있는 테이블 쌍마다 아래 순서로 문서를 찾는다.

1. `okf/joins/index.md` — 직접 조인 금지 쌍과 중복 주의 쌍 목록 확인
2. `okf/joins/graph.md` — 쌍의 연결 경로 확인
3. 개별 조인 문서 — `usable`, `cartesian_risk`, `join_type_hint`, `fanout` 기록

| 결과 | 기록 |
|---|---|
| `usable: false` | `unsafe_joins` 에 `"<A.col> = <B.col> (usable:false)"` |
| `cartesian_risk: m2m` | `unsafe_joins` 에 `"<A.col> = <B.col> (m2m)"` |
| index.md 의 직접 조인 금지 쌍 | `unsafe_joins` 에 `"<A> - <B> (직접 조인 금지)"` |
| index.md 의 중복 주의 쌍인데 조인 문서의 패턴(한쪽 또는 양쪽을 먼저 GROUP BY)을 따르지 않음 | `unsafe_joins` 에 `"<A> - <B> (중복 주의)"` |
| 조인 문서 없음 | `unsafe_joins` 에 넣지 않고 출력에 "조인 문서 없음(2단계 쿼리 또는 추측 조인)"으로 기록. 심판 D5 가 판정 |
| 문서 있고 안전 | 출력에 `usable`·`cartesian_risk`·`join_type_hint`·`fanout` 값 기록 |

## 5. 코드값 의미 확인

- CODE 성격 컬럼에 리터럴이 있으면(예: `PROGRESS_STATUS = '<코드>'`) 컬럼 코멘트와 `okf/codes/` 코드 문서를 먼저 본다. 거기에 풀이가 있으면 조회하지 않는다.
- 풀이가 없으면 공통코드를 조회한다. 코드는 코드셋 안에서만 고유하므로 코드셋(`COMM_CODE_TYPE_CODE`)을 함께 건다(컬럼명은 `okf/schemas/ADAMSUSER/tables/TI_BQMS006_COMMCODE.md` 의 `# Schema` 표 기준):

```sql
SELECT COMM_CODE_TYPE_CODE, CODE, KO_LABEL, DESCRIPTION
FROM   ADAMSUSER.TI_BQMS006_COMMCODE
WHERE  COMM_CODE_TYPE_CODE = '<코드셋>' AND CODE = '<리터럴>'
```

- 리터럴이 코드 목록에 없으면 출력에 "미등록 코드값"으로 기록 (심판 D2 근거).

## 6. 삭제 플래그 규약

삭제 플래그 값(`Y/N`, `0/1`)은 테이블마다 다르다. `scenario_sql` 이 `DELETE_YN = 'N'` 같은 리터럴을 쓰면 그 테이블 문서 `# Schema` 의 비고로 규약을 확인한다. 어긋나면 출력에 기록 (심판 D3·L3 근거).

## 7. PII 점검 → `pil_columns`

- SELECT 목록에 데이터 사전 문서에서 `has:pii` 태그가 붙은 컬럼이 있으면 `"OWNER.OBJECT.COLUMN"` 형식으로 넣는다.
- PII 조회는 실행을 막지 않는다. 다만 출력의 표본·evidence 에서는 값을 `"***"` 로 마스킹한다.
- 키 이름은 입출력 명세서 표기 `pil_columns` 를 따른다 (`skills/scenario-validation/references/output-spec.md` 의 주의 참고).

## 8. 실행 여부 결정

| 조건 | 실행 |
|---|---|
| `select_violation: true` | 하지 않음 → `row_count: null` (미실행) |
| `invalid_query_names` 1개 이상 | 하지 않음 → `row_count: null` (미실행) |
| 그 외 (컬럼 누락·불안전 조인·PII 포함) | 실행 |

실행하지 않아도 4단계(심판)까지 진행한다.

## 9. bundle_check 작성

```json
{
  "missing_columns": [],
  "unsafe_joins": [],
  "pil_columns": [],
  "invalid_query_names": [],
  "select_violation": false
}
```

- 해당 사항이 없으면 빈 배열 `[]`. 빈 문자열 `""` 을 원소로 넣지 않는다.
- 다섯 키는 항상 모두 쓴다. 입력 파싱 실패로 대조하지 못했으면 `bundle_check: null`.