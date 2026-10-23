---
type: Query Example
title: 견적 최저가 업체 미선정
description: "최저가 견적을 제출한 업체가 탈락한 건 추출 (시나리오 SSA1802017)."
tags: ['example', 'domain:bid-qt']
question: "지난해 견적에서 최저가를 제출한 업체가 미선정된 건을 보여줘"
status: stable
executed: "2026-10-15 sql_ro.py (PRD, 2025년 기준) 정상 추출"
verified:
- by: human
  at: 2026-10-15T16:03:27+09:00
uses:
- /schemas/APPADAMSUSER/tables/TI_BQMS840.md
---

# 질문

"지난해 견적에서 최저가를 제출한 업체가 미선정된 건을 보여줘"

# 사용 테이블

- [TI_BQMS840](/schemas/APPADAMSUSER/tables/TI_BQMS840.md) — 입찰/견적/발주/정산 결합 테이블

# SQL

```sql
SELECT DISTINCT
       a.SITE_CD, a.REQ_NO, a.REQ_SEQ,
       a.EPR_CD, a.ENTP_NM,
       a.TAMT, a.TMIN_AMT, a.STD_DT
  FROM APPADAMSUSER.TI_BQMS840 a
 WHERE a.GB = '견적'
   AND a.FSTATUS = '선정완료'
   AND a.STD_DT BETWEEN :p_from AND :p_to
   AND a.TAMT = a.TMIN_AMT                 -- 제출총액 = 최저가 (제출한 업체가 최저가)
   AND NVL(a.SEL_YN, ' ') <> 'Y'           -- 그런데 미선정
   AND EXISTS (SELECT 1
                 FROM APPADAMSUSER.TI_BQMS840 s
                WHERE s.SITE_CD = a.SITE_CD
                  AND s.REQ_NO  = a.REQ_NO
                  AND s.REQ_SEQ = a.REQ_SEQ
                  AND s.SEL_YN = 'Y')      -- 실제로 다른 업체가 선정된 건만
 ORDER BY a.STD_DT DESC
 FETCH FIRST 20 ROWS ONLY;
```

# 근거

- 원본 시나리오: `SETADAMSUSER.SP_BQ_SSA1802017` 1단계 — "최저가 견적을 제출한 업체가 탈락된 건".
- `TAMT`(제출총액, 업체기준) = `TMIN_AMT`(최저가, 업체기준) → 제출한 업체가 그 건의 최저가.
- 840이 item 단위라 업체가 중복 출력될 수 있어 `DISTINCT`, "선정된 업체가 있는 건"만 보기 위해 `EXISTS` 사용.

# 결과 (2026-10-15, 2025년 기준, 20행)

최저가 제출 업체가 미선정된 견적 건 정상 추출 (예: QT25186679 TAMT=TMIN_AMT=502272, 미선정, 해당 건에 선정 업체 존재).

# 가정

- 기간 = 2025년 1/1~12/31.
- 원본의 2단계(예상금액 대비 선정가 상승), 3단계(담당자-업체 반복)는 이 예제에 미반영 — 핵심 탐지(1단계)만.

# 확인 필요

- 원본 2·3단계 필터를 반영할지 (예상금액 비교, 담당자-업체 1년 2회 이상).
