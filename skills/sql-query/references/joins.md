# 조인

필요한 컬럼이 한 테이블에 있으면 조인하지 않는다(`okf/t2s/rules/join-rules.md`). 조인이 필요하면 아래 3단계를 순서대로 따른다. 이 프로젝트의 조인 기준은 이 문서다.

## 1단계: 문서 있는 조인 (우선)

`okf/joins/index.md`(허브 테이블, 직접 조인 금지 쌍)와 테이블 문서 `# Joins` 에서 고른 조인 문서들을 한 응답에서 읽고, 조인 문서 frontmatter 를 따른다.

| frontmatter | 처리 |
|---|---|
| `usable: true` | `join_condition` 그대로, `join_type_hint`(LEFT/INNER) 따름 |
| `usable: conditional` | `join_filter` 를 반드시 함께 |
| `usable: false` 또는 `cartesian_risk: m2m` | 조인하지 않는다 → 3단계 |
| `fanout` 큼(부모 1건당 자식 수백 이상) | 자식을 먼저 필요한 단위로 집계한 뒤 조인 |

## 2단계: 문서 없는 조인 (근거 + 실측)

세 가지가 모두 성립할 때만 쓴다.

1. 컬럼 근거: 조인 키가 양쪽 `# Schema` 에 있고 이름·타입이 같다(대개 `*_CD`, `*_NO`, `*_ID`).
2. 부모 유일성: 부모 키가 `PK`·`UK` 표기나 T2S 힌트 실측으로 유일하다.
3. 실측: 아래 검증 SQL 을 이번 조건 범위로 `execute_sql`. 고아율이 낮아야 한다. PK·UK 표기가 없으면 부모 중복 SQL 도 0행이어야 한다. 시간 초과면 검증 실패 → 3단계.

T2S 힌트에 「조인 후보 — 조인 문서 미작성」으로 적힌 관계는 1·2가 충족된 것이므로 3의 고아율 검증만 한다.

성립하면 N:1(자식→부모) 조인은 한 SQL 에 써도 된다. 근거에 적는다:
`추측 조인(번들 문서 없음): <A>.<key> = <B>.<key>, 근거=<컬럼 일치+부모 PK/실측>, 고아율=<n>%`

```sql
SELECT COUNT(*) AS n, COUNT(p.<KEY>) AS matched
FROM (SELECT <KEY> FROM <CHILD query_name> WHERE <질문 조건> FETCH FIRST 10000 ROWS ONLY) c
LEFT JOIN <PARENT query_name> p ON p.<KEY> = c.<KEY>
```

```sql
SELECT <KEY>, COUNT(*) AS cnt FROM <PARENT query_name> WHERE <조건>
GROUP BY <KEY> HAVING COUNT(*) > 1 FETCH FIRST 5 ROWS ONLY
```

## 3단계: 조인 불가 → 2단계 쿼리

1·2단계로 입증하지 못했거나, 양쪽이 상세 테이블이라 M:N 이 의심되거나, 금지 대상이면 조인하지 않는다. 첫 쿼리로 연결 키를 뽑아 두 번째 쿼리의 `IN (...)` 조건으로 쓴다. `IN` 목록이 수백 건을 넘으면 조건을 좁힌다.

## 공통

- 복합 키는 모든 컬럼을 조인 조건에 넣는다.
- 허브 테이블을 지나는 다단계 조인은 한 번에 2단계까지, 단계마다 fanout 확인.
- 조인 후에도 행 수·큰 테이블·soft-delete 규칙은 그대로.