---
type: Query Example
title: 셀아웃 실적 정산 Level 임의변경
description: "동일 거래선+품목이 정산 Level 0/2와 1/3/4를 섞어 사용한 건 추출 (시나리오 SSA2004001, 1단계)."
tags: ['example', 'domain:mkt-exp']
question: "셀아웃 정산 Level을 낮게(0/2) 쓰고 높게(1/3/4)도 쓴 거래선이 있어?"
status: stable
executed: "2026-10-15 sql_ro.py (PRD) 정상 추출"
verified:
- by: human
  at: 2026-10-15T16:03:27+09:00
uses:
- /schemas/APPADAMSUSER/tables/TI_GRPB_DE_SELLOUT.md
---

# 질문

"셀아웃 정산 Level을 낮게(0/2) 쓰고 높게(1/3/4)도 쓴 거래선이 있어?"

# 사용 테이블

- [TI_GRPB_DE_SELLOUT](/schemas/APPADAMSUSER/tables/TI_GRPB_DE_SELLOUT.md) — `SETTLEMENT_LEVEL`, `CUSTOMER`, `MATERIAL_GROUP`, `CONDITION_DOC_NO`

# SQL

```sql
SELECT
       c.CUSTOMER, c.CUSTOMER_NAME, c.MATERIAL_GROUP,
       COUNT(DISTINCT CASE WHEN c.SETTLEMENT_LEVEL IN ('0','2') THEN c.CONDITION_DOC_NO END) AS LOW_LV_DOC,
       COUNT(DISTINCT CASE WHEN c.SETTLEMENT_LEVEL IN ('1','3','4') THEN c.CONDITION_DOC_NO END) AS HIGH_LV_DOC,
       MIN(c.POSTING_DATE) AS MIN_PDT, MAX(c.POSTING_DATE) AS MAX_PDT
  FROM APPADAMSUSER.TI_GRPB_DE_SELLOUT c
 WHERE c.CUSTOMER IS NOT NULL
   AND c.POSTING_DATE BETWEEN :p_from AND :p_to
 GROUP BY c.CUSTOMER, c.CUSTOMER_NAME, c.MATERIAL_GROUP
HAVING COUNT(DISTINCT CASE WHEN c.SETTLEMENT_LEVEL IN ('0','2') THEN c.CONDITION_DOC_NO END) >= 1
    AND COUNT(DISTINCT CASE WHEN c.SETTLEMENT_LEVEL IN ('1','3','4') THEN c.CONDITION_DOC_NO END) >= 1
 ORDER BY MAX(c.POSTING_DATE) DESC
 FETCH FIRST 20 ROWS ONLY;
```

# 근거

- 원본 시나리오: `SETADAMSUSER.SP_SA_SSA2004001` — "셀아웃 실적 검증조건을 수량 검증하지 않는 정산 Level 0, 2로 임의 변경하여 실적을 조작". 1단계 = "정산 Level 0 또는 2로 정산한 것 중 동일 거래선+품목으로 Level 1,3,4로 정산한 이력이 있는 건".
- `SETTLEMENT_LEVEL` 실측 값: 0/1/2/3/4 (2026-10-15: 0=278,682 1=1,434,928 2=298,187 3=3,829 4=716,983).
- `MATERIAL_GROUP`을 품목 구분 키로 사용 (원본 1.4단계에서 Division→Material_Group으로 변경).

# 결과 (2026-10-15, 20행)

Level 0/2와 1/3/4를 병행한 거래선 정상 추출 (예: DERYA KLIMA ABG0A LOW 17 / HIGH 62건).

# 가정

- 기간 필터는 `POSTING_DATE`로 (미지정 시 전체 기간).
- Level 0/2 = "수량 검증 안 함"(낮은 검증), 1/3/4 = 검증 수반으로 해석.

# 확인 필요

- 원본 2단계 "충당금액과 지급금액 일치" 필터는 [TI_GRPB_DE_PAYMENT_REPORT](/schemas/APPADAMSUSER/tables/TI_GRPB_DE_PAYMENT_REPORT.md) 조인이 필요 — 미반영.
