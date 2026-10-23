---
type: Query Example
title: 입찰평가 1위 업체 미선정
description: "평가 1위 업체가 미선정된 입찰 건 추출 (시나리오 SSA1712009)."
tags: ['example', 'domain:bid-qt']
question: "입찰평가 1위 업체가 미선정된 건을 보여줘"
status: stable
executed: "2026-10-15 sql_ro.py (PRD, 2025년 기준) 정상 추출"
verified:
- by: human
  at: 2026-10-15T16:03:27+09:00
uses:
- /schemas/APPADAMSUSER/tables/TI_BQMS840.md
- /schemas/APPADAMSUSER/tables/TI_BQMS011_BD_EVL.md
---

# 질문

"입찰평가 1위 업체가 미선정된 건을 보여줘"

# 사용 테이블

- [TI_BQMS840](/schemas/APPADAMSUSER/tables/TI_BQMS840.md) — `EVL_ORD`(최종Rank), `EVL_TOT_PT`(최종점수), `SEL_YN`
- (대안) [TI_BQMS011_BD_EVL](/schemas/APPADAMSUSER/tables/TI_BQMS011_BD_EVL.md) — 평가자별 평가 상세

# SQL

```sql
SELECT DISTINCT
       a.SITE_CD, a.REQ_NO, a.REQ_SEQ,
       a.EPR_CD, a.ENTP_NM,
       a.EVL_ORD, a.EVL_TOT_PT, a.SEL_YN, a.STD_DT
  FROM APPADAMSUSER.TI_BQMS840 a
 WHERE a.GB = '입찰'
   AND a.FSTATUS = '낙찰'
   AND a.STD_DT BETWEEN :p_from AND :p_to
   AND a.EVL_ORD = 1                      -- 평가 1위
   AND NVL(a.SEL_YN, ' ') <> 'Y'          -- 그런데 미선정
   AND EXISTS (SELECT 1
                 FROM APPADAMSUSER.TI_BQMS840 s
                WHERE s.SITE_CD = a.SITE_CD
                  AND s.REQ_NO  = a.REQ_NO
                  AND s.REQ_SEQ = a.REQ_SEQ
                  AND s.SEL_YN = 'Y')     -- 실제로 다른 업체가 낙찰된 건만
 ORDER BY a.STD_DT DESC
 FETCH FIRST 20 ROWS ONLY;
```

# 근거

- 원본 시나리오: `SETADAMSUSER.SP_BQ_SSA1712009` — "입찰평가 1위업체 미선정(BQMS)".
- 840의 `EVL_ORD`(최종Rank)=1이 평가 1위. item 단위이므로 1건의 REQ/SEQ 안에서 여러 item 1위가 나올 수 있어 `DISTINCT`.
- 원본은 TI_BQMS011_BD_EVL(평가자별)로 집계하지만, 840에 최종점수·순위가 이미 들어 있어 840 단일 테이블로 단순화.

# 결과 (2026-10-15, 2025년 기준, 20행)

평가 1위 업체가 미선정된 입찰 건 정상 추출 (예: AK01/BD25099717에 1위 업체 다수 미선정).

# 가정

- 기간 = 2025년 1/1~12/31.
- `EVL_ORD`가 item 기준이라 1건의 1위가 여러 행으로 나타남.

# 확인 필요

- 원본의 평가자별 재집계(TI_BQMS011_BD_EVL)와 840의 `EVL_ORD`가 항상 일치하는지.
