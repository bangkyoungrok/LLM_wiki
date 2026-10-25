# 도구 결과 읽기

> 이 에이전트에서는 variation-worker 가 통계 도구를 직접 부르고, 그 결과를 이 기준으로 읽는다.

도구 결과 읽기는 통계 도구 4종이 돌려준 JSON 의 필드를 이상 목록의 칸으로 옮기는 기준이다(출처: 통계 데이터 추출 에이전트 A 의 result-reading.md. 내용은 원본과 같고 TABLE_NOT_FOUND 처리만 OKF 에 맞췄다). variation-worker 는 이 기준으로 도구 결과를 이상 목록(대상, 관점, 방향, 하한·상한, 대상 값, 건수, 금액, 평소 값)으로 정리한다. 수치는 결과 값을 그대로 옮기고 다시 계산하지 않는다. 칸을 비우지 않고, 결과에 없는 값은 「결과에 없음」, 그 관점에 없는 칸은 「해당 없음」으로 적는다.


> 이 프로젝트에서 이 문서의 「통계 표」, 「답변 칸」, 「분석 조건」은 탐색 결과를 정리한 이상 목록의 칸을 뜻한다. 사용자에게 내는 보고서의 형식은 `AGENTS.md` 10절이며, 통계 표를 그대로 보고서에 내지 않는다. 이상 목록의 수치는 변형별 상세(이상을 뒷받침하는 근거)에 쉬운 말로 옮긴다.
>
> 「근거」 칸(도구 이름과 인자, 조회문 원문, SQL 원문)은 이상 목록과 위임 prompt 에만 쓰는 내부 자료다. 보고서에는 옮기지 않으며, 보고서에는 SQL 을 쓰지 않는다(`answer-format.md` 6절).
>
> 이상 목록의 행마다 `wiki/patterns/index.md` 1절 표로 데이터 이상징후 패턴 ID 를 붙인다(scenario-variation 4단계). 관점·기법 코드·규칙 점검 종류가 그 표의 「결과」 칸이다.

## 1. stat_screen 결과 필드

| 결과 필드 | 답변 위치 |
|---|---|
| scope.table_name 또는 조회문 원문(analysis_source 가 select), metric_column, date_column, group_column, peer_columns, denominator_column, date_from, date_to | 분석 조건 |
| scope.metric_mode | 분석 조건의 지표 모드. value 는 값, interval_days 는 간격(단위 일), ratio 는 비율(지표 ÷ 분모) |
| scope.rows_in_period | 분석 조건의 기간 안 행 수 |
| scope.basis | log 이면 해석 주의에 「경계는 ln 기준으로 구해 원래 단위로 적었다」를 적는다 |
| validity.items 의 verdict 「제외」, groups.excluded_reasons, cells.excluded_reasons | 판정하지 않은 항목. 집단과 칸은 사유별 수와 이름 몇 개만 적는다 |
| validity.items 의 verdict 「주의」 | 분석 조건 아래 한 줄 |
| candidates | 통계 표, 예외 조건, 점검 대상 사례 |
| marks | 표 아래 「표시 N건(후보 아님)」. N 은 marks 의 건수다 |
| message, warnings, note | 생략된 판정은 판정하지 않은 항목에, 그 밖의 안내는 해석 주의에 적는다 |
| sql | 옮기지 않는다 |

- status 가 ok 인데 candidates 가 비고 message 에 제외 사유가 있으면 그 지표는 분석 가능 조건에서 제외된 것이다.
- reduced 가 true 이면 message 의 전체 후보 수를 요약에 함께 적는다.
- warnings 가 peer_columns 없이 다시 호출하라고 하면 같은 인자에서 peer_columns 만 비워 1회 더 부른다.

## 2. 후보를 통계 표로 옮기는 기준

통계 표는 범위 밖 대상마다 한 행이며, 후보 하나에 기법 코드가 여럿이면 기법마다 한 행으로 적는다. 대상 값은 observed, 방향은 direction 이고, 그 밖의 칸은 아래 표를 따른다. 표의 boundaries 는 candidates[].boundaries.<기법 코드> 다.

| 기법 코드 | 대상 | 하한, 상한 | 건수 | 금액 | 평소 값 |
|---|---|---|---|---|---|
| B1_RECORD, B2_RECORD | target(「컬럼=값」), cell | boundaries.low, high | out_cnt | out_amt | boundaries.median |
| B1_GROUP, B2_GROUP, B1_LEVEL, B2_LEVEL, B1_RATIO, B2_RATIO | target, cell | boundaries.low, high | out_cnt(집단 건수) | out_amt | boundaries.median |
| B1_RATE, B2_RATE, B1_OFFHOUR, B2_OFFHOUR | target | boundaries.low, high | out_cnt | 해당 없음 | boundaries.median |
| B3_MONTH | target(월) | 기준 측정값(measures 에 amt, avg_days, ratio 가 있으면 그 값, 없으면 cnt)의 _low, _high(예: amt_low, amt_high) | out_cnt(그 달 건수) | out_amt | 해당 없음 |
| B5_TREND | target(구간 「YYYY-MM~YYYY-MM」) | 해당 없음 | 「months개월」 | 해당 없음 | 구간 첫 월 값 |
| B4_BENFORD | 지표 컬럼, boundaries.digits_top 의 d(기대보다 많이 나온 첫째 자리)와 observed(관측 비율) | 상한 boundaries.out_threshold. 대상 값은 boundaries.digit_mad | 해당 없음 | 해당 없음 | 해당 없음 |
| B4_BENFORD2 | target(두 자리 값) | 해당 없음. 대상 값은 boundaries.n | out_cnt(기대 대비 초과 건수) | 해당 없음 | boundaries.expected_n |

- 방향: direction 이 high 면 「상한 초과」, low 면 「하한 미만」, increase 면 「증가」, decrease 면 「감소」이며 그 밖의 값은 그대로 적는다. 개별 값 후보의 out_high_cnt 와 out_low_cnt 가 모두 0 보다 크면 두 방향의 건수를 병기한다(예: 상한 초과 12건, 하한 미만 3건).
- 예외 조건: 표 아래에 범위 밖 대상마다 「예외 조건: <지표> <비교 기호> <경계 값>(<단위>)」 한 줄을 적는다(예: 「예외 조건: DC_AMT/AMT > 0.0156(비율)」). 상한 초과는 > 상한, 하한 미만은 < 하한이다. 경계 값은 결과 값 그대로 쓰고 새로 계산하지 않는다. 추세와 규칙 점검은 stat-views.md 2절의 판정 조건을 적는다.
- 점검 대상 사례: 개별 값 후보의 sample_rows 를 「점검 대상 사례」 표로 대상마다 최대 5행 옮긴다. 열은 식별 열, 지표 값, 날짜다.
- 같은 후보에 개별 값 기법이 함께 있으면 out_cnt, out_amt 는 개별 값 기법의 값이므로 다른 기법 행의 건수와 금액은 「해당 없음」이다.
- 간격 모드: 단위는 일이고 금액은 「해당 없음」이다.
- 비율 모드: 대상 값은 비율이고 금액은 분자 합계다. 분자가 금액이 아니면 금액은 「해당 없음」이다.
- 역할이 단가, 비율인 지표: 동료 대비 집중(B1_GROUP, B2_GROUP) 후보는 판정하지 않은 항목에 「합계가 의미 없는 지표」로 적고, 다른 행의 금액도 「해당 없음」이다.
- 범위 밖 0건: 판정 조건(stat-views.md 2절)을 충족했고 생략 안내가 없는데 그 관점의 후보가 없으면 「범위 밖 0건」 한 행으로 적는다.

## 3. 규칙 점검 도구 결과

규칙 점검 결과는 관점마다 통계 표 한 행이며, 평소 값과 하한, 상한, 방향은 「해당 없음」이다. 값은 summary 에서 옮긴다.

| 도구와 종류 | 관점 | 대상 | 대상 값 | 건수 | 금액 |
|---|---|---|---|---|---|
| find_duplicates | 중복 | key_columns | 「완전 exact_groups묶음, 유사 near_groups묶음」 | dup_rows | 해당 없음 |
| find_number_gaps 결번 | 결번 | number_column | gap_cnt 구간 | missing_cnt | 해당 없음 |
| find_number_gaps 번호 중복 | 중복 | number_column | dup_numbers | dup_rows | 해당 없음 |
| find_number_gaps 번호 날짜 역전 | 번호 순서 역전 | number_column | inversion_ratio | order_inversions | 해당 없음 |
| match_tables 짝 없음 | 짝 없음 | join_columns | 해당 없음 | unmatched_rows | unmatched_amount |
| match_tables 금액 불일치 | 금액 불일치 | join_columns | 해당 없음 | mismatch_rows | mismatch_abs_diff_sum |

- 위반이 0건인 종류는 「범위 밖 0건」 한 행으로 적는다.
- findings 상위 5건을 2절과 같이 점검 대상 사례 표로 옮긴다(중복은 keys, row_cnt, amount_sum, first_date, last_date, 결번과 역전은 group, number_from, number_to, missing_cnt 또는 days_back, 대조는 keys, base_date, base_amount, match_amount, diff).
- summary 의 null_key_rows, null_rows, non_integer_rows 는 판정하지 않은 항목에 적는다. match_tables 의 dup_key_rows 가 0 보다 크면 금액 불일치가 실제보다 많을 수 있다고 해석 주의에 적는다.

## 4. 오류 결과

| error_code | 처리 |
|---|---|
| INVALID_NAME, INVALID_DATE, PERIOD_TOO_LONG | hint 대로 인자를 고쳐 1회 다시 부른다. 기간이 24개월을 넘으면 나누어 부른다 |
| TABLE_NOT_FOUND | main agent 는 OKF 테이블 문서로 `query_name` 을 확인해 조회문 방식(테이블이 통계 도구 스키마 밖이면 반드시)으로 1회 다시 부른다. variation-worker 도 같은 방식으로 1회 다시 부른다 |
| COLUMN_NOT_FOUND, COLUMN_TYPE_MISMATCH | hint 의 컬럼 목록에서 describe_table 결과로 의미가 확인되는 물리명을 골라 1회 다시 부른다. 조회문 방식이면 목록은 산출 컬럼이므로 alias 를 고르거나 빠진 컬럼을 조회문에 더한다 |
| ARG_CONFLICT | table_name 과 analysis_select(대상 쪽은 match_table 과 match_select) 중 하나만 넣어 1회 다시 부른다 |
| SELECT_INVALID | hint 가 지목한 규칙 위반을 고쳐 1회 다시 부른다 |
| SELECT_FAILED | hint 의 DB 오류와 산출 컬럼 목록을 보고 조회문의 테이블명, 컬럼명, 형식을 describe_table 결과에 맞게 고쳐 1회 다시 부른다 |
| CONFIG_INVALID, QUERY_FAILED, INTERNAL_ERROR | 다시 부르지 않는다. 판정하지 않은 항목에 「도구 관리자 확인 필요」로 적는다 |

조회문을 고칠 때 그레인과 지표 정의는 바꾸지 않고, 고친 조회문을 근거에 적는다. 다시 부른 호출도 실패하면 판정하지 않은 항목에 오류 코드와 함께 적는다.

## 5. 해석 주의

- 범위 밖 값: 이상으로 확정한 것이 아니라 표시만 한 것이며 지우거나 고치지 않았다.
- 범위 밖 금액: 범위 밖 값이나 규칙 위반 행의 금액 합계이며 손실액이나 노출액이 아니다.
- 표시: 통계 경계 밖이지만 최소 폭 안인 값이며 후보가 아니다.
- 판정하지 않은 항목: 이상이 없다는 뜻이 아니라 판정하지 못한 대상이다. 「범위 밖 0건」과 다르다.
- 첫 두 자리 분포: 기대보다 많이 나온 두 자리 값이며, 대상 값은 실제 건수, 평소 값은 기대 건수다. 10 이상 값이 5,000건 미만이면 warnings 안내를 함께 적는다.
