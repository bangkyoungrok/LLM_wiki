---
type: Query Guideline
title: 날짜·문자열 처리
description: "대부분 날짜 컬럼은 VARCHAR2 문자열(YYYYMMDD/YYYYMM)이라 문자열 비교. DATE 타입만 TO_DATE."
tags: ['t2s:rule']
status: draft
---

# 규칙

- 컬럼 타입은 문서 `# Schema` 표에서 확인:
  - **VARCHAR2 날짜** (이 DB 대부분; `YYYYMMDD` 8자, `YYYYMM` 6자, `YYYYMMDDHH24MISS` 14자 등) → **문자열 비교**:
    `POSTING_DATE >= '20250701' AND POSTING_DATE < '20260101'`
  - **DATE** 타입 (소수, 예: `TI_BQMS004_INFA_BD.LOAD_DT`) → `TO_DATE('2025-07-01','YYYY-MM-DD')` 또는 `DATE '2025-07-01'`.
- 범위 조건은 `BETWEEN`보다 `>= AND <` 권장 (시각 포함 여지 제거).
- 날짜 컬럼에 함수(`TO_CHAR`, `TRUNC`)를 씌워 인덱스를 무효화하지 않는다.
- 문자열 검색은 대소문자 구분: `UPPER(col) LIKE UPPER(:kw)`.
- 문자열 연결은 `||`.
- 테이블 문서 T2S 힌트에 표기된 날짜 형식(예: TI_GRPB_DE_PAYMENT_REPORT의 YYYYMMDD)은 그 표기를 따른다.

# 예외

- 형식이 문서에 없는 날짜 컬럼은 소수 행 표본 조회로 실제 형식을 확인한 뒤 조건을 만든다 (가정에 명시).
