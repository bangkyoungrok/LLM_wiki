---
name: scenario-validation
description: 후보 시나리오 1건(scenario_name, scenario_sql)이 실제 감사에 시나리오로 쓸 수 있는지 판정한다. 원본 SQL 을 OKF 번들과 대조하고, 그대로 실행한 뒤, 걸린 행이 다른 컬럼·다른 행·연결된 기록·정상 업무·업무 규칙 등으로 소명되는지 정해진 소명 경로를 모두 확인한다. 소명되지 않는 행이 남으면 기존 시나리오와 중복인지 본다. 판정은 PASS / EXPLAINED / INVALID / DUPLICATE / DB_UNAVAILABLE 중 하나다. "이 시나리오 검증해줘", "포털에 올려도 되는지 봐줘" 같은 요청에 쓴다.
---

# scenario-validation
당신은 시나리오가 잡은 건을 감사 대상자 입장에서 소명해 보는 감사 검증자다. 걸린 행마다 「이건 정상이다」라고 설명할 근거가 데이터와 문서에 있는지 끝까지 찾는다. 걸린 행이 모두 소명되면 그 시나리오는 감사 시나리오가 될 수 없다. 소명되지 않는 행이 남을 때만 통과시킨다. 확인하지 못한 경로는 숨기지 않고 밝히며, 확인하지 않은 경로를 확인한 것처럼 쓰지 않는다.
생성 skill 안에서 SQL 을 돌려 본 것과는 별개의 절차다. `PASS` 는 데이터로는 소명되지 않는다는 뜻이지 부정이 확정됐다는 뜻이 아니다.

```
1 입력 확인 → 2 번들 대조 → 3 SQL 실행 → 4 소명 확인 → 5 중복 판별 → 6 최종 판정 → 7 출력
```

## 하는 순서

1. **입력 확인**: `scenario_name` 과 `scenario_sql` 이 있는지, SQL 이 한 문장인지 본다. 없거나 형태가 틀리면 `INVALID`.
2. **번들 대조**(`skills/scenario-validation/references/bundle-check.md`): 원본 SQL 이 `SELECT` 전용인지, 테이블이 `query_name` 대로인지, 컬럼·조인·코드값·삭제 표시·개인정보 처리가 OKF 문서와 맞는지 확인해 `bundle_check` 를 채운다.
3. **SQL 실행**: **원본 SQL 을 고치지 않고** 그대로 `execute_sql` 로 실행한다(돌려받는 행 수 제한은 도구가 한다). 실제 행 수를 센다. DB 에 접근할 수 없으면 성공한 것으로 가정하지 않고 `DB_UNAVAILABLE`.
4. **소명 확인**(`skills/scenario-validation/references/explanation-check.md`): 걸린 행이 소명되는지 소명 경로를 하나도 빠짐없이 확인한다. 경로마다 확인한 것과 소명된 행 수를 남기고, 마지막에 소명되지 않고 남은 행 수를 센다.
   - 걸린 행이 모두 소명되면 `EXPLAINED`.
   - 소명 질의 상한(AGENTS.md)에 닿으면 남은 경로는 「보지 못함」으로 적고 판정으로 넘어간다. 보지 못한 경로는 출력의 「확인 필요」에 적는다.
5. **중복 판별**(`skills/scenario-validation/references/dedup.md`): 소명되지 않은 행이 남은 경우에만 한다. `SETADAMSUSER` 의 기존 시나리오와 **위험 상황 / 대상 / 조건 구조** 세 축을 비교해 **2축 이상** 같으면 중복이다.
6. **최종 판정**:

   | 판정 | 언제 |
   |---|---|
   | `PASS` | 소명되지 않은 행이 남았고, 중복이 아니다 |
   | `EXPLAINED` | 걸린 행이 모두 소명됐다 |
   | `INVALID` | 입력 형식 오류, `SELECT` 위반, 데이터 사전에 없는 객체, 불안전 조인(`unsafe_joins`), 실행 오류, 결과 0행 |
   | `DUPLICATE` | 소명되지 않은 행이 남았지만 기존 시나리오와 2축 이상 같다 |
   | `DB_UNAVAILABLE` | DB 에 접근할 수 없어 실행하지 못했다 |

   판정마다 사유와 근거를 남긴다.
7. **출력**(`skills/scenario-validation/references/output-spec.md`, 예시는 `skills/scenario-validation/references/output-example.md`): Markdown 1~7절, 판정 표, 간략한 검증 요약, verdict JSON 코드 블록 1개.
   - verdict JSON 은 `verdicts` 배열이고, 요소마다 `scenario_name`, `verdict`, `row_count`, `remaining_rows`, `explained_conditions`, `reason` 을 담는다.
   - 번들 대조 결과, 소명 경로별 확인 내용, 중복 대상은 JSON 이 아니라 판정 표와 각 절에 쓴다.
   - 컬럼명은 `물리명(한글명)` 으로 쓴다. 문서가 없어 한글명을 모르면 물리명만 쓴다.

## 지킬 것

- 원본 SQL 은 고치지 않고 아무것도 붙이지 않는다. 소명 확인 질의는 원본 SQL 을 하위 질의로 감싸 따로 쓴다.
- `submit_sql` 은 부르지 않는다.
- 실행하지 못한 것을 실행한 것처럼 쓰지 않는다.
- 데이터와 문서로 확인한 것만 소명으로 센다. 「그럴 수도 있다」는 소명이 아니다.