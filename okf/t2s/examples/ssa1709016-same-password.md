---
type: Query Example
title: 동일 패스워드 견적 제출
description: "동일 견적에 2개 이상 업체가 동일(비정상) 패스워드로 제출한 건 추출 (시나리오 SSA1709016)."
tags: ['example', 'domain:bid-qt']
question: "여러 업체가 같은 패스워드로 견적을 제출한 건을 보여줘"
status: stable
executed: "2026-10-15 sql_ro.py (PRD, 2025년 기준) 정상 추출"
verified:
- by: human
  at: 2026-10-15T16:03:27+09:00
uses:
- /schemas/APPADAMSUSER/tables/TI_BQMS840.md
---

# 질문

"여러 업체가 같은 패스워드로 견적을 제출한 건을 보여줘"

# 사용 테이블

- [TI_BQMS840](/schemas/APPADAMSUSER/tables/TI_BQMS840.md) — `PW`(제출패스워드), `EPR_CD`, `SEL_YN`

# SQL

```sql
SELECT
       a.SITE_CD, a.REQ_NO, a.REQ_SEQ,
       COUNT(DISTINCT a.EPR_CD)                                   AS VENDOR_CNT,  -- 동일 PW로 제출한 업체 수
       COUNT(DISTINCT CASE WHEN a.SEL_YN = 'Y' THEN a.EPR_CD END) AS SEL_CNT,     -- 그중 선정된 업체 수
       MAX(a.STD_DT)                                               AS MAX_DT
  FROM APPADAMSUSER.TI_BQMS840 a
 WHERE a.GB = '견적'
   AND a.FSTATUS = '선정완료'
   AND a.STD_DT BETWEEN :p_from AND :p_to
   AND a.PW IS NOT NULL
   AND a.PW <> 'C.Xx.C'          -- 원본의 데일리/초기화 비밀번호 제외
   AND a.PW NOT LIKE '%*%'       -- 마스킹된 PW 제외
 GROUP BY a.SITE_CD, a.REQ_NO, a.REQ_SEQ, a.PW
HAVING COUNT(DISTINCT a.EPR_CD) >= 2   -- 2개 이상 업체가 동일 PW
 ORDER BY MAX(a.STD_DT) DESC
 FETCH FIRST 20 ROWS ONLY;
```

# 근거

- 원본 시나리오: `SETADAMSUSER.SP_BQ_SSA1709016` 1단계 — "동일 견적에 2개 이상의 업체가 동일 PW로 견적제출한 건".
- **PW 값은 SELECT 목록에 두지 않는다** (민감 정보). 그룹 키로만 쓰고, 결과에는 업체 수·선정 수만 노출.
- 3단계(동일 PW 업체 중 한 업체 선정)는 `SEL_CNT >= 1`으로 2차 필터 가능.

# 결과 (2026-10-15, 2025년 기준, 20행)

동일 PW로 2~4개 업체가 제출한 건 정상 추출 (예: C550A/QT25145605 4개 업체 동일 PW, 4개 선정).

# 가정

- 기간 = 2025년 1/1~12/31.
- `PW` 마스킹 형태(별표)는 원본이 `C.Xx.C` 외치로 처리해 `%*%`로 추가 제외.
- 원본의 "이전 PW도 동일"(2단계), "유사 ID"(edit_distance)은 미반영 — 핵심 탐지(1단계)만.

# 확인 필요

- `PW`가 마스킹되어 있어 동일성 판정이 정확하지 않을 수 있음. 원본 TI_BQMS802(PW 히스토리) 기준 2단계 반영 여부.
