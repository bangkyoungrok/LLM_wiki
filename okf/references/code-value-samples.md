---
title: "코드·플래그 컬럼 실제값 샘플 (DB 실측)"
type: Reference
description: "_YN/_GB/_ST/_FL 컬럼 실제값 샘플 (AIAGT 표본). 0/1 vs Y/N 인코딩 판별용."
source: "work/code_value_samples.csv"
extracted_at: "20261015"
---

# 코드·플래그 컬럼 실제값 샘플 (DB 실측)

테이블의 `_YN`/`_GB`/`_ST`/`_FL` 컬럼 **실제 데이터값** 샘플이다 (AIAGT, `ROWNUM<=50000` 표본, 컬럼당 TOP15).
출처: `work/code_value_samples.csv` (열: table, column, value, rowcount, note, extracted_at).

대상 컬럼 452개 (테이블 155개). 값 패턴 분포:

| 패턴 | 컬럼 수 |
|---|---:|
| `0/1` | 1 |
| `0/1+NULL` | 1 |
| `Y/N` | 171 |
| `Y/N+NULL` | 81 |
| NULL-only | 30 |
| multi(10) | 1 |
| multi(12) | 1 |
| multi(15) | 13 |
| multi(2) | 49 |
| multi(3) | 17 |
| multi(4) | 9 |
| multi(5) | 4 |
| multi(6) | 5 |
| multi(7) | 1 |
| multi(8) | 1 |
| multi(9) | 2 |
| single | 65 |
| **합계** | **452** |

## `0/1` 인 컬럼 (쿼리 시 `='N'`/`='Y'` 쓰면 안 됨)

대부분의 `_YN`은 `Y/N`인데, 아래는 실제값이 **`0`/`1`**인 컬럼이다. 조건은 `='0'`/`='1'`로:

| 테이블 | 컬럼 | 값 |
|---|---|---|
| SETADAMSUSER.TC_CF_COMM_CODE_TYPE | DELETE_YN | `0`, `1` |
| SETADAMSUSER.TC_CF_COMM_CODE | DELETE_YN | `0`, `1`, `NULL` |

나머지 355개 컬럼은 `Y/N`(+NULL) 또는 `multi`(한글·숫자 코드 등). 개별값은 `work/code_value_samples.csv`에서 확인한다.

> 추출 방식: `SELECT col, COUNT(*) FROM (SELECT col FROM <table> WHERE ROWNUM<=50000) GROUP BY col ORDER BY 2 DESC FETCH FIRST 15 ROWS ONLY`. `size:xl` 테이블은 표본이라 값이 더 있을 수 있음.
