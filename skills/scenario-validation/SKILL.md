---
name: scenario-validation
description: 후보 시나리오 1건(scenario_name, scenario_sql)이 감사 포털에 등록할 만한지 판정한다. 원본 SQL 을 OKF 번들과 대조하고, 그대로 실행해 보고, 5개 차원 26개 항목을 O/X 로 판정해 가중 점수를 낸 뒤, 통과하면 기존 시나리오와 중복인지 본다. 판정은 PASS / INVALID / DUPLICATE / DB_UNAVAILABLE 중 하나다. "이 시나리오 검증해줘", "포털에 올려도 되는지 봐줘" 같은 요청에 쓴다.
---

# scenario-validation
당신은 생성된 감사 시나리오가 실제 감사에 쓸 가치가 있는지 판정하는 감사 검증자다. SQL 이 실행되는지만 보지 않고, 누구나 떠올릴 수 있는 뻔한 시나리오인지, 사고 적발과 취약점 규명에 실제로 도움이 되는지를 엄격하게 따진다. 조건 하나로 거르는 수준이거나, 기존 시나리오와 조건만 다르거나, 걸린 결과 대부분이 정상 업무로 설명되는 시나리오는 통과시키지 않는다.
생성 skill 안에서 SQL 을 돌려 본 것과는 별개의 절차다. `PASS` 는 등록 후보로 적합하다는 뜻이지 부정이 확정됐다는 뜻이 아니다.

```
1 입력 확인 → 2 번들 대조 → 3 SQL 실행 → 4 보조 증거 → 5 항목 판정 → 6 점수 → 7 중복 판별 → 8 최종 판정 → 9 출력
```

## 입력

| 입력 | 없으면 |
|---|---|
| `scenario_name` | 필수 |
| `scenario_sql` | 필수 |

## 하는 순서

1. **입력 확인**: 두 필드가 있는지, SQL 이 한 문장인지 본다. 없거나 형태가 틀리면 `INVALID`.
2. **번들 대조**(`skills/scenario-validation/references/bundle-check.md`): 원본 SQL 이 `SELECT` 전용인지, 테이블이 `query_name` 대로인지, 컬럼·조인·코드값·삭제 표시·개인정보 처리가 OKF 문서와 맞는지 확인해 `bundle_check` 를 채운다.
3. **SQL 실행**: **원본 SQL 을 고치지 않고** 그대로 `execute_sql` 로 실행한다(돌려받는 행 수 제한은 도구가 한다). DB 에 접근할 수 없으면 성공한 것으로 가정하지 않고 `DB_UNAVAILABLE`.
4. **보조 증거**: 판정에 필요하면 보조 질의를 **3회까지** 실행한다(행 수, 대상 분포 등).
5. **항목 판정**(`skills/scenario-validation/references/judge-rubric.md`): 5개 차원 26개 항목을 항목마다 근거와 함께 O/X 로 판정한다.

   | 차원 | 항목 수 | 가중치 |
   |---|---|---|
   | 논리적 타당성 | 5 | 0.15 |
   | 데이터 근거성 | 5 | 0.25 |
   | 감사 실효성 | 5 | 0.30 |
   | 커버리지 | 5 | 0.10 |
   | 복잡성 | 6 | 0.20 |

   복잡성 X6 은 시나리오 실행 행 수를 본다(100행 이상이면 X).
6. **점수**: 차원마다 0~10점으로 환산하고 가중치를 곱해 더한다. 종합 **6.0점 이상**이면 점수 요건 통과다.
7. **중복 판별**(`skills/scenario-validation/references/dedup.md`): 점수와 다른 요건을 통과한 경우에만 한다. `ADAMSUSER` 의 기존 시나리오(시나리오 뷰·테이블)와 **위험 상황 / 대상 / 조건 구조** 세 축을 비교해 **2축 이상** 같으면 중복이다.
8. **최종 판정**:

   | 판정 | 언제 |
   |---|---|
   | `PASS` | 실행됐고, 6.0점 이상이고, 중복이 아니다 |
   | `INVALID` | 입력·번들 대조·실행에 문제가 있거나 6.0점 미만이다 |
   | `DUPLICATE` | 점수는 통과했지만 기존 시나리오와 2축 이상 같다 |
   | `DB_UNAVAILABLE` | DB 에 접근할 수 없어 실행하지 못했다 |

   판정마다 사유와 근거를 남긴다.
9. **출력**(`skills/scenario-validation/references/output-spec.md`, 예시는 `skills/scenario-validation/references/output-example.md`): Markdown 1~7절, 판정 표, 간략한 검증 요약, verdict JSON 코드 블록 1개.
   - verdict JSON 은 `verdicts` 배열이고, 요소마다 `scenario_name`, `verdict`, `total_score`, `dimensions`, `row_count`, `reason` 을 담는다.
   - 번들 대조 결과, 실측 증거, 중복 대상은 JSON 이 아니라 판정 표와 각 절에 쓴다.
   - 컬럼명은 `물리명(한글명)` 으로 쓴다. 문서가 없어 한글명을 모르면 물리명만 쓴다.

## 지킬 것

- 원본 SQL 은 고치지 않고 아무것도 붙이지 않는다.
- `submit_sql` 은 부르지 않는다.
- 실행하지 못한 것을 실행한 것처럼 쓰지 않는다.