---
type: Oracle Table
title: 견적집계_본사(SET)
description: '견적집계_본사(SET). 키: SITE_CODE, REQ_NO, REQ_SEQ, ITEM_ID, EPR_CODE.'
resource: oracle://PRD/APPADAMSUSER/TI_BQMS005_INFA_QT
tags: ['kind:table', 'owner:appadamsuser', 'class:transaction', 'size:m', 'access:select-full', 'has:pk', 'has:amount', 'has:pii', 'domain:bid-qt']
owner: APPADAMSUSER
table_name: TI_BQMS005_INFA_QT
query_name: APPADAMSUSER.TI_BQMS005_INFA_QT
table_class: transaction
primary_key: [SITE_CODE, REQ_NO, REQ_SEQ, ITEM_ID, EPR_CODE]
row_count: 4413011
last_analyzed: 2026-10-09
status: draft
stale_after: 2027-01-11T13:53:08+09:00
sources:
- id: dict
  resource: /references/dictionary-sources.md
  title: 딕셔너리 추출 스냅샷
generated:
  by: process:okf-dict-builder/0.1
  at: 2026-10-13T13:53:08+09:00
table_type: 인터페이스
business_area: BQMS
business_detail: 견적
---

# 개요
(사람이 보완: 업무 의미, 생성 시점, 주의 사항)

# Schema
<!-- AUTO:BEGIN schema -->
| # | 컬럼 | 한글명 | 타입 | NULL | 키 | 코드/참조 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | SITE_CODE | 사이트코드 | VARCHAR2(10) | N | PK(1) |  |  |
| 2 | YMD | 견적요청일_한국시각 | VARCHAR2(24) | Y |  |  |  |
| 3 | REQ_NO | 견적코드 | VARCHAR2(35) | N | PK(2) |  |  |
| 4 | REQ_SEQ | 견적차수 | NUMBER(3) | N | PK(3) |  |  |
| 5 | REQ_NAME | 견적명 | VARCHAR2(500) | Y |  |  |  |
| 6 | 최종차수 | 최종차수여부 | VARCHAR2(1) | Y |  |  |  |
| 7 | REQ_TYPE | 견적구분 | VARCHAR2(12) | Y |  |  |  |
| 8 | 계약구분 | 계약구분 | VARCHAR2(12) | Y |  |  |  |
| 9 | CTR_TYPE | 계약구분코드 | VARCHAR2(10) | Y |  |  |  |
| 10 | CATEGORY_NAME_1 | 카테고리명1 | VARCHAR2(4000) | Y |  |  |  |
| 11 | CATEGORY_NAME_2 | 카테고리명2 | VARCHAR2(4000) | Y |  |  |  |
| 12 | CATEGORY_NAME_3 | 카테고리명3 | VARCHAR2(4000) | Y |  |  |  |
| 13 | CATEGORY_NAME_4 | 카테고리명4 | VARCHAR2(4000) | Y |  |  |  |
| 14 | QT상태 | QT상태 | VARCHAR2(500) | Y |  |  |  |
| 15 | 견적담당ID | 견적담당ID | VARCHAR2(35) | Y |  |  |  |
| 16 | 견적담당 | 견적담당 | VARCHAR2(200) | Y |  |  |  |
| 17 | ITEM_ID | ITEM_ID | VARCHAR2(35) | N | PK(4) |  |  |
| 18 | ITEM_NAME | 품목명 | VARCHAR2(500) | Y |  |  |  |
| 19 | CIS_CODE | CIS코드 (2019.11 추가) | VARCHAR2(11) | Y |  |  |  |
| 20 | EPR_CODE | 업체EPR코드 | VARCHAR2(16) | N | PK(5) |  |  |
| 21 | EPRNAME | 업체명 | VARCHAR2(500) | Y |  |  |  |
| 22 | LOCAL_AMT | LOCAL총액 | NUMBER(30,8) | Y |  |  |  |
| 23 | LOCAL_CURR | LOCAL통화 ( 2019.11 추가요청 - 제출단가 CURRENCY은 기존 LOCAL_CURR 컬럼이 해당 의미의 컬럼임) | VARCHAR2(11) | Y |  |  |  |
| 24 | SUBMIT_AMT_KRW | 제출금액KRW_SUBMIT당시환율 | NUMBER(30,8) | Y |  |  |  |
| 25 | SUBMIT_AMT_KRW2 | 제출금액KRW_SYSDATE기준 | NUMBER(30,8) | Y |  |  |  |
| 26 | MINKRW | 최저가_0이상 이면서 상태 제출건만 계산 | NUMBER(30,8) | Y |  |  |  |
| 27 | MINKRW_ALL_SEQ | 최저가_0이상 이면서 상태 제출건만 계산, 전체차수 대상 | NUMBER(30,8) | Y |  |  |  |
| 28 | MINKRW_ALL_SEQ2 | 최저가_0이상 이면서 상태 제출건만 계산, 전체차수 대상. BQMS연계DB생성일자환율 | NUMBER(30,8) | Y |  |  |  |
| 29 | TARGET_AMOUNT | 예상가 | NUMBER(30,8) | Y |  |  |  |
| 30 | TARGET_AMOUNT_CURR | 예상가통화 | CHAR(3) | Y |  |  |  |
| 31 | 예상수량 | 예상수량 | NUMBER | Y |  |  |  |
| 32 | 예상단가 | 예상단가(재/변경계약의 경우에는 이전 예상단가) | NUMBER(30,8) | Y |  |  |  |
| 33 | 예상금액 | 예상금액 (2019.11 추가 - LOCAL예상가) | NUMBER(30,8) | Y |  |  |  |
| 34 | 예상통화 | 예상통화 (2019.11 추가 - LOCAL예상가 CURRENCY) | VARCHAR2(11) | Y |  |  |  |
| 35 | 제출단가 | 제출단가 | NUMBER(30,8) | Y |  |  |  |
| 36 | 요청업체수 | 요청업체수 | NUMBER | Y |  |  |  |
| 37 | 제출업체수 | 제출업체수 | NUMBER | Y |  |  |  |
| 38 | 선정업체수 | 선정업체수 | NUMBER | Y |  |  |  |
| 39 | 선정여부 | 선정여부 | VARCHAR2(1) | Y |  |  |  |
| 40 | 최종선정 | 최종선정 | VARCHAR2(1) | Y |  |  |  |
| 41 | 참여순차 | 참여순차 | VARCHAR2(40) | Y |  |  |  |
| 42 | 비최저가 | 비최저가 | VARCHAR2(1) | Y |  |  |  |
| 43 | 비최저가ALL_SEQ | 비최저가ALL_SEQ | VARCHAR2(1) | Y |  |  |  |
| 44 | 비최저가ALL_SEQ2 | 비최저가ALL_SEQ2 | VARCHAR2(1) | Y |  |  |  |
| 45 | 요청HQ | 요청시각_한국시각 | VARCHAR2(14) | Y |  |  |  |
| 46 | LOCAL 요청일시 | 요청시각_현지시각 (2019.11 추가) | VARCHAR2(14) | Y |  |  |  |
| 47 | 요청EMAIL | 요청EMAIL | VARCHAR2(2500) | Y |  |  | PII |
| 48 | 마감HQ | 마감시각_한국시각 | VARCHAR2(14) | Y |  |  |  |
| 49 | LOCAL 마감일시 | 마감시각_현지시각 (2019.11 추가) | VARCHAR2(14) | Y |  |  |  |
| 50 | 제출HQ | 제출시각_한국시각 | VARCHAR2(14) | Y |  |  |  |
| 51 | LOCAL 제출일시 | 제출시각_현지시각 (2019.11 추가) | VARCHAR2(14) | Y |  |  |  |
| 52 | 제출 | 제출여부 | VARCHAR2(6) | Y |  |  |  |
| 53 | 제출IP | 제출IP | VARCHAR2(100) | Y |  |  |  |
| 54 | 제출ID | 제출ID | VARCHAR2(35) | Y |  |  |  |
| 55 | SOLE_VENDOR | SOLE_VENDOR 여부 (2019.11 추가) | VARCHAR2(2) | Y |  |  |  |
| 56 | SOLE_VENDOR_CODE | SOLE_VENDOR사유코드 | VARCHAR2(20) | Y |  |  |  |
| 57 | SOLE_VENDOR_REMARK | SOLE_VENDOR사유 텍스트 (2019.11 추가) | VARCHAR2(2000) | Y |  |  |  |
| 58 | PR_NO | PR번호 | VARCHAR2(35) | Y |  |  |  |
| 59 | PR_USER_ID | PR담당자ID | VARCHAR2(35) | Y |  |  |  |
| 60 | CTR_NO | 계약No | VARCHAR2(35) | Y |  |  |  |
| 61 | LOAD_DATE | BQMS적재일시 | VARCHAR2(14) | Y |  |  |  |
| 62 | LOAD_DT | 적재일시 | DATE | Y |  |  |  |
| 63 | DIV_COCD | DIV_COCD | CHAR(2) | Y |  |  |  |
| 64 | CTR_FRM | 계약형태. 20200710추가. COMM_CODE_TYPE_CODE = BD_CLT_FRM. 글로벌마케팅은 프로세스상 null임 | VARCHAR2(10) | Y |  |  |  |
| 65 | SUBMIT_PROXY_IP | SUBMIT_PROXY_IP | VARCHAR2(15) | Y |  |  |  |
<!-- AUTO:END schema -->

# Joins
<!-- AUTO:BEGIN joins -->
- [TI_BQMS005_INFA_QT_2](/schemas/APPADAMSUSER/tables/TI_BQMS005_INFA_QT_2.md) ← EPR_CODE, ITEM_ID, REQ_NO, REQ_SEQ, SITE_CODE (1:1, medium, LEFT 권장) — [상세](/joins/APPADAMSUSER/TI_BQMS005_INFA_QT_2__TI_BQMS005_INFA_QT__EPR_CODE_AND_ITEM_ID_AND_REQ_NO_AND_REQ_SEQ_AND_SITE_CODE.md)
- [TI_BQMS840](/schemas/APPADAMSUSER/tables/TI_BQMS840.md) ← SITE_CD, REQ_NO, REQ_SEQ, ITEM_ID, EPR_CD (N:1, medium, LEFT 권장) — [상세](/joins/APPADAMSUSER/TI_BQMS840__TI_BQMS005_INFA_QT__SITE_CODE_AND_REQ_NO_AND_REQ_SEQ_AND_ITEM_ID_AND_EPR_CODE.md)
<!-- AUTO:END joins -->

# T2S 힌트
- `QT상태`는 **한글 라벨 자체 저장** (코드 아님, 코드 테이블 조인 불필요). 관찰값: 견적요청/요청저장/결과저장/선정결재중/선정완료/선정마감/NULL — [코드값 문서](/codes/TI_BQMS005_INFA_QT.md).
- 사이트→법인 매핑 조인 후보: `SITE_CODE = TI_BQMS900.SITE_CD` (N:1, TI_BQMS900.SITE_CD 고유 312행). 조인 문서 미작성 — 사용 전 확인 필요.
- `CTR_FRM` 코드는 `COMM_CODE_TYPE_CODE = BD_CLT_FRM` (글로벌마케팅은 프로세스상 NULL).

> 출처: /references/llm-wiki-import.md (2026-10-07 DB 조회)

<!-- ES-REFLECT:BEGIN (add_info/es_index_generated.csv + DB grain 실측 2026-10-15) -->
### 그레인 (DB 실측 2026-10-15)
- 1행 단위: 사이트(SITE)·견적번호(REQ_NO)·차수(REQ_SEQ)·품목(ITEM_ID)·업체(EPR_CODE) 단위 견적 제출 실적 1건
- **업무 키 (유일성 확인)**: `SITE_CODE`, `REQ_NO`, `REQ_SEQ`, `ITEM_ID`, `EPR_CODE` — ROWNUM<=500K 표본 distinct=전체 (유일)
<!-- ES-REFLECT:END -->
