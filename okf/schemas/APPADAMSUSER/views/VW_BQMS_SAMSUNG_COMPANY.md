---
type: Oracle View
title: BQMS 업체코드(관계사)
description: 'BQMS 업체코드(관계사). 참조: TI_BQMS024_INFA_VENDOR.'
resource: oracle://PRD/APPADAMSUSER/VW_BQMS_SAMSUNG_COMPANY
tags: ['kind:view', 'owner:appadamsuser', 'class:view', 'access:select-full', 'domain:vendor']
owner: APPADAMSUSER
table_name: VW_BQMS_SAMSUNG_COMPANY
query_name: APPADAMSUSER.VW_BQMS_SAMSUNG_COMPANY
table_class: view
status: draft
stale_after: 2027-01-11T13:53:08+09:00
sources:
- id: dict
  resource: /references/dictionary-sources.md
  title: 딕셔너리 추출 스냅샷
generated:
  by: process:okf-dict-builder/0.1
  at: 2026-10-13T13:53:08+09:00
table_type: 마스터
business_area: BQMS
business_detail: 벤더정보
---

# 개요
(사람이 보완: 이 뷰가 무엇을 조인해서 보여 주는지)

# Schema
<!-- AUTO:BEGIN schema -->
| # | 컬럼 | 한글명 | 타입 | NULL | 키 | 코드/참조 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | EPR_CODE | 업체코드 | VARCHAR2(16) | Y |  |  |  |
| 2 | ERPEPR_CODE | ERP업체코드 | VARCHAR2(15) | Y |  |  |  |
| 3 | EPR_NAME | 로컬업체명 | VARCHAR2(500) | Y |  |  |  |
<!-- AUTO:END schema -->

# Definition
<!-- AUTO:BEGIN definition -->
```sql
SELECT EPR_CODE, ERPEPR_CODE, EPR_NAME
     FROM (SELECT EPR_CODE,
                  ERPEPR_CODE,
                  EPR_NAME,
                  ROW_NUMBER ()
                     OVER (PARTITION BY EPR_CODE ORDER BY FNL_UPDATE_DT DESC)
                     AS RN
             FROM TI_BQMS024_INFA_VENDOR
            WHERE 1 = 1 AND SUBSTR (ERPEPR_CODE, 5, 1) = '-')
    WHERE 1 = 1 AND RN = 1
   UNION
   /*GERP업체코드에 - 없으나 관계사*/
   SELECT 'EPRERP0000FA1UPE', 'FA1UPE', 'CHEIL ITALIA SRL' FROM DUAL
   UNION
   SELECT 'EPRERP0000FA12YM',
          'FA12YM',
          'CHEIL MEA FZ-LLC (MERKEZ？ DUBA？) TU？STANBUL ？UBES？'
     FROM DUAL
   UNION
   SELECT 'EPRERP0000FZXIFF', 'FZXIFF', 'CHEIL BENELUX BV' FROM DUAL
   UNION
   SELECT 'EPR829444528181', 'T505/09', 'Samsung SDS India Pvt Ltd' FROM DUAL
   UNION
   SELECT DISTINCT EPR_CODE, ERPEPR_CODE, EPR_NAME
     FROM TI_BQMS024_INFA_VENDOR
    WHERE 1 = 1 AND EPR_NAME = 'Cheil India Pvt Ltd'
   UNION
   SELECT 'EPRERP000000DD04', 'DD04', '삼성에스디에스(주)' FROM DUAL
   UNION
   SELECT 'EPRERP0000FA1UPE', 'FA1UPE', 'CHEIL ITALIA SRL' FROM DUAL
   UNION
   SELECT 'EPRERP0000FA141J', 'FA141J', 'CHEIL MEXICO, S.A. DE C.V.'
     FROM DUAL
   UNION
   SELECT 'EPR1416484636224', 'FA491M', 'CHEIL SPA' FROM DUAL
   UNION
   SELECT 'EPRERP0000FZWM92',
          'FZWM92',
          'CHEIL SINGAPORE PTE LTD T/A CHEILAUSTRALIA'
     FROM DUAL
   UNION
   SELECT 'EPRERP0000FZXJWF',
          'FZXJWF',
          'CHEIL GERMANY GmbH Sp. z.o.o.Oddzial w Polsce'
     FROM DUAL
   UNION
   SELECT 'EPRERP0000FZWM92', 'FZWM92', 'CHEIL SINGAPORE PTE LTD' FROM DUAL
   UNION
   SELECT 'EPRERP000Y4B1/01',
          'Y4B1/01',
          'Cheil Germany GmbHorganizacni slozka'
     FROM DUAL
   UNION
   SELECT 'EPR678544790527', 'FA5BDA', 'CHEIL PERU S.A.C.' FROM DUAL
   UNION
   SELECT 'EPR1951715035115', 'Y5B0/21', 'Cheil India Pvt Ltd' FROM DUAL
   UNION
   SELECT 'EPRERP0000FZXIFF', 'FZXIFF', 'CHEIL BENELUX BV' FROM DUAL
   UNION
   SELECT 'EPRERP000Y5B2/01',
          'Y5B2/01',
          'Cheil Singapore Pte Ltd TaiwanBranch'
     FROM DUAL
   UNION
   SELECT 'EPRERP0000FZXRK8', 'FZXRK8', 'Cheil Germany GmbH' FROM DUAL
   UNION
   SELECT 'EPR619077439486', 'FA60SL', 'Cheil Singapore Pte Ltd T/A Cheil Australia' FROM DUAL
   UNION
   SELECT 'EPRERP000Y1B0/02', 'Y1B0/02','Cheil Japan' FROM DUAL
```
<!-- AUTO:END definition -->

# 참조 객체
<!-- AUTO:BEGIN deps -->
- [TI_BQMS024_INFA_VENDOR](/schemas/APPADAMSUSER/tables/TI_BQMS024_INFA_VENDOR.md)
<!-- AUTO:END deps -->

# T2S 힌트
(사람이 보완하거나 P7 에서 규칙 문서를 링크한다)

<!-- ES-REFLECT:BEGIN (add_info/es_index_generated.csv + DB grain 실측 2026-10-15) -->
### 그레인 (DB 실측 2026-10-15, 전체 스캔)
- **업무 키 (유일성 확인)**: `EPR_CODE`, `EPR_NAME` — greedy 탐색(500K 표본) + 전체 스캔 dup 0
<!-- ES-REFLECT:END -->
