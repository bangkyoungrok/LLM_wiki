---
type: Oracle Table
title: 입찰집계_본사(SET)
description: '입찰집계_본사(SET). 키: SITE_CODE, REQ_NO, REQ_SEQ, ITEM_ID, EPR_CODE.'
resource: oracle://PRD/APPADAMSUSER/TI_BQMS004_INFA_BD
tags: ['kind:table', 'owner:appadamsuser', 'class:transaction', 'size:m', 'access:select-full', 'has:pk', 'has:amount', 'has:pii', 'domain:bid-qt']
owner: APPADAMSUSER
table_name: TI_BQMS004_INFA_BD
query_name: APPADAMSUSER.TI_BQMS004_INFA_BD
table_class: transaction
primary_key: [SITE_CODE, REQ_NO, REQ_SEQ, ITEM_ID, EPR_CODE]
row_count: 1856264
last_analyzed: 2026-10-07
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
business_detail: 입찰
---

# 개요
(사람이 보완: 업무 의미, 생성 시점, 주의 사항)

# Schema
<!-- AUTO:BEGIN schema -->
| # | 컬럼 | 한글명 | 타입 | NULL | 키 | 코드/참조 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | SITE_CODE | 사이트코드 | VARCHAR2(10) | N | PK(1) |  |  |
| 2 | YMD | 입찰공고일_한국시각 | VARCHAR2(24) | Y |  |  |  |
| 3 | REQ_NO | 입찰코드 | VARCHAR2(35) | N | PK(2) |  |  |
| 4 | REQ_SEQ | 입찰차수 | NUMBER(3) | N | PK(3) |  |  |
| 5 | CTR_CHANGE_SEQ | 계약변경차수 | NUMBER(3) | N |  |  |  |
| 6 | REQ_NAME | 입찰명 | VARCHAR2(500) | Y |  |  |  |
| 7 | PROGRESS_STATUS | 진행상태 | VARCHAR2(20) | Y |  |  |  |
| 8 | BID상태 | BID상태 | VARCHAR2(2000) | Y |  |  |  |
| 9 | CTR_TYPE | 계약구분코드 | VARCHAR2(10) | Y |  |  |  |
| 10 | CATEGORY_NAME_1 | 카테고리명1 | VARCHAR2(4000) | Y |  |  |  |
| 11 | CATEGORY_NAME_2 | 카테고리명2 | VARCHAR2(4000) | Y |  |  |  |
| 12 | CATEGORY_NAME_3 | 카테고리명3 | VARCHAR2(4000) | Y |  |  |  |
| 13 | CATEGORY_NAME_4 | 카테고리명4 | VARCHAR2(4000) | Y |  |  |  |
| 14 | ITEM_ID | ITEM_ID | VARCHAR2(35) | N | PK(4) |  |  |
| 15 | ITEM_NAME | 품목명 | VARCHAR2(500) | Y |  |  |  |
| 16 | CIS_CODE | CIS코드 | VARCHAR2(11) | Y |  |  |  |
| 17 | 요청업체수 | 요청업체수 | NUMBER | Y |  |  |  |
| 18 | 제출업체수 | 제출업체수 | NUMBER | Y |  |  |  |
| 19 | 선정업체수 | 선정업체수 | NUMBER | Y |  |  |  |
| 20 | 선정여부 | 선정여부 | VARCHAR2(1) | Y |  |  |  |
| 21 | EPR_CODE | 업체EPR코드 | VARCHAR2(16) | N | PK(5) |  |  |
| 22 | EPRNAME | 업체명 | VARCHAR2(500) | Y |  |  |  |
| 23 | 참여순차 | 참여순차 | VARCHAR2(40) | Y |  |  |  |
| 24 | 비최저가 | 비최저가 | VARCHAR2(1) | Y |  |  |  |
| 25 | NOT_SELECT_REASON_YN | 최저가 미선정 여부 | VARCHAR2(1) | Y |  |  |  |
| 26 | NOT_SELECT_REASON_DESC | 최저가 미선정 사유 | VARCHAR2(2000) | Y |  |  |  |
| 27 | 요청HQ | 화면 내에서 입찰계획 쪽에 입찰서 제출시작시각 으로 함 - 즉, 업체에 입찰이 오픈된 시각 | VARCHAR2(16) | Y |  |  |  |
| 28 | 요청LOCAL | (LOCAL) 요청일시 | VARCHAR2(16) | Y |  |  |  |
| 29 | 요청EMAIL | 요청EMAIL | VARCHAR2(2000) | Y |  |  | PII |
| 30 | 마감HQ | 마감시각_한국시각 | VARCHAR2(16) | Y |  |  |  |
| 31 | 마감LOCAL | 마감시각_(LOCAL)마감일시 | VARCHAR2(16) | Y |  |  |  |
| 32 | 제출HQ | 제출시각_한국시각 | VARCHAR2(16) | Y |  |  |  |
| 33 | 제출LOCAL | 제출시각_(LOCAL)제출일시 | VARCHAR2(16) | Y |  |  |  |
| 34 | 제출IP | 제출IP | VARCHAR2(100) | Y |  |  |  |
| 35 | 제출ID | 제출ID | VARCHAR2(35) | Y |  |  |  |
| 36 | 예상수량 | 예상수량 | NUMBER | Y |  |  |  |
| 37 | 예상단가 | 예상단가 | NUMBER(22,5) | Y |  |  |  |
| 38 | TARGET_AMOUNT | LOCAL예상가 - LOCAL의 개념 : 사내 담당자가 지정한 값 | NUMBER(30,5) | Y |  |  |  |
| 39 | TARGET_AMOUNT_CURR | LOCAL예상가 CURRENCY - LOCAL의 개념 : 사내 담당자가 지정한 값 | CHAR(3) | Y |  |  |  |
| 40 | TARGET_AMT_KRW | 예상가KRW | NUMBER(30,5) | Y |  |  |  |
| 41 | TARGET_AMT_CURR | 예상가KRW CURRENCY - KRW | CHAR(3) | Y |  |  |  |
| 42 | 제출단가 | 제출단가 | NUMBER(22,5) | Y |  |  |  |
| 43 | 제출단가CURRENCY | 제출단가 CURRENCY | CHAR(3) | Y |  |  |  |
| 44 | LOCAL_AMOUNT | LOCAL제출금액 | NUMBER(30,5) | Y |  |  |  |
| 45 | LOCAL_AMOUNT_CURR | LOCAL제출금액 CURRENCY | CHAR(3) | Y |  |  |  |
| 46 | SUBMIT_AMT_KRW | 제출금액KRW_SUBMIT당시환율 | NUMBER(22,4) | Y |  |  |  |
| 47 | MINKRW | 최저가_최저 제출가는 제출한 건 이면서 0 제외 계산 | NUMBER(30,4) | Y |  |  |  |
| 48 | 평가유형 | 평가유형 | VARCHAR2(4000) | Y |  |  |  |
| 49 | VALUT_ROLE_YN | 평가자대행입력여부 | VARCHAR2(1) | Y |  |  |  |
| 50 | 최종RANK | 최종RANK | NUMBER | Y |  |  |  |
| 51 | 금액점수 | 금액점수 | NUMBER | Y |  |  |  |
| 52 | 기술점수 | 기술점수 | NUMBER | Y |  |  |  |
| 53 | 최종점수 | 최종점수 | NUMBER | Y |  |  |  |
| 54 | NOT_SELECT_VALUT_REASON_YN | 최고평가 미선정 여부 | VARCHAR2(1) | Y |  |  |  |
| 55 | NOT_SELECT_VALUT_REASON_DESC | 최고평가 미선정 사유 | VARCHAR2(2000) | Y |  |  |  |
| 56 | 입찰담당ID | 입찰담당ID | VARCHAR2(50) | Y |  |  |  |
| 57 | 입찰담당 | 입찰담당 | VARCHAR2(50) | Y |  |  |  |
| 58 | PR_NO | PR번호 | VARCHAR2(35) | Y |  |  |  |
| 59 | PR_USER_ID | PR담당자ID | VARCHAR2(35) | Y |  |  |  |
| 60 | CTR_NO | 계약No | VARCHAR2(35) | Y |  |  |  |
| 61 | FAILINBID_CONTENTS | 유찰사유 | VARCHAR2(2000) | Y |  |  |  |
| 62 | LOAD_DATE | BQMS적재일시 | VARCHAR2(14) | Y |  |  |  |
| 63 | LOAD_DT | 적재일시 | DATE | Y |  |  |  |
| 64 | DIV_COCD | A1 CE/IM(본사) ,B1 한국총괄, B2 중국총괄, B3 삼성전자로지텍, B4 삼성전자판매, B5 삼성전자서비스 ,B6 삼성메디슨, CO: 공통, ZZ: 미분류 | CHAR(2) | Y |  |  |  |
| 65 | CTR_FRM | 계약형태. 20200710추가. COMM_CODE_TYPE_CODE = BD_CLT_FRM | VARCHAR2(10) | Y |  |  |  |
| 66 | SUBMIT_PROXY_IP | SUBMIT_PROXY_IP | VARCHAR2(15) | Y |  |  |  |
<!-- AUTO:END schema -->

# Joins
<!-- AUTO:BEGIN joins -->
(확정된 조인 없음. 조인 관계는 P4 에서 확정한다. 컬럼 표의 '조인후보' 참고)
<!-- AUTO:END joins -->

# T2S 힌트
- `PROGRESS_STATUS`(진행상태) 코드값 22종과 국문명 조인: [코드값 문서](/codes/TI_BQMS004_INFA_BD.md). 국문명 조인 시 `TI_BQMS006_COMMCODE` (`COMM_CODE_TYPE_CODE='BD_PROGRESS'`).
- **비최저가·선정 미선정 행**: `NOT_SELECT_REASON_YN='Y' AND 비최저가='Y' AND 선정여부='Y'`. `선정여부`/`비최저가`는 'N'이 아니라 **NULL로 미설정**됨.
- `MIN(제출단가)`에 플레이스홀더 가격(1, 0.01, 2 등) 포함 — 프리미엄 계산 시 `MIN(제출단가) >= 100` 필터 권장.
- 사이트→법인 매핑 조인 후보: `SITE_CODE = TI_BQMS900.SITE_CD` (N:1, TI_BQMS900.SITE_CD 고유 312행). 조인 문서 미작성 — 사용 전 확인 필요.
- `CTR_FRM` 코드는 `COMM_CODE_TYPE_CODE = BD_CLT_FRM`.

> 출처: /references/llm-wiki-import.md (2026-10-07 DB 조회)

<!-- ES-REFLECT:BEGIN (add_info/es_index_generated.csv + DB grain 실측 2026-10-15) -->
### 그레인 (DB 실측 2026-10-15)
- 1행 단위: 사이트·입찰번호·입찰차수·품목·업체 단위 입찰 참여 및 평가 실적 1건
- **업무 키 (유일성 확인)**: `SITE_CODE`, `REQ_NO`, `REQ_SEQ`, `ITEM_ID`, `EPR_CODE` — ROWNUM<=500K 표본 distinct=전체 (유일)
<!-- ES-REFLECT:END -->
