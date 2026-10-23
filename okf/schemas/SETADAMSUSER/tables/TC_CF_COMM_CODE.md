---
type: Oracle Table
title: SDP (표준플랫폼)-공통코드
description: 'SDP (표준플랫폼)-공통코드. 키: CODE_ID.'
resource: oracle://PRD/SETADAMSUSER/TC_CF_COMM_CODE
tags: ['kind:table', 'owner:setadamsuser', 'class:code', 'size:xs', 'access:select-full', 'has:unique-key', 'has:soft-delete', 'quality:no-pk', 'domain:fin-master']
owner: SETADAMSUSER
table_name: TC_CF_COMM_CODE
query_name: SETADAMSUSER.TC_CF_COMM_CODE
table_class: code
unique_key: [CODE_ID]
row_count: 3402
last_analyzed: 2026-09-16
status: draft
stale_after: 2027-01-11T13:53:08+09:00
sources:
- id: dict
  resource: /references/dictionary-sources.md
  title: 딕셔너리 추출 스냅샷
generated:
  by: process:okf-dict-builder/0.1
  at: 2026-10-13T13:53:08+09:00
table_type: 기준정보
business_area: 시스템/공통
business_detail: 공통코드
---

# 개요
(사람이 보완: 업무 의미, 생성 시점, 주의 사항)

# Schema
<!-- AUTO:BEGIN schema -->
| # | 컬럼 | 한글명 | 타입 | NULL | 키 | 코드/참조 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | CODE_ID | 코드ID | VARCHAR2(35) | Y | IDX |  |  |
| 2 | CODE | 코드 | VARCHAR2(20) | Y | IDX |  |  |
| 3 | UPPER_CODE_ID | 상위코드ID | VARCHAR2(35) | Y |  |  |  |
| 4 | DESCRIPTION | 설명 | VARCHAR2(2000) | Y |  |  |  |
| 5 | COMM_CODE_TYPE_CODE | 공통코드유형코드 | VARCHAR2(20) | Y | IDX |  |  |
| 6 | HIERARCHY_LEVEL | 계층레벨 | NUMBER(5) | Y |  |  |  |
| 7 | FIRST_REG_DATETIME | 최초등록일시 | DATE | Y |  |  |  |
| 8 | FIRST_REGR_ID | 최초등록자ID | VARCHAR2(35) | Y |  |  |  |
| 9 | LAST_MOD_DATETIME | 최종수정일시 | DATE | Y |  |  |  |
| 10 | LAST_MODR_ID | 최종수정자ID | VARCHAR2(35) | Y |  |  |  |
| 11 | ORD | 정렬순서 | NUMBER(5) | Y |  |  |  |
| 12 | KO_LABEL | 한글코드명 | VARCHAR2(500) | Y |  |  |  |
| 13 | EN_LABEL | 영문코드명 | VARCHAR2(500) | Y |  |  |  |
| 14 | LABEL | 기타코드명 | VARCHAR2(500) | Y |  |  |  |
| 15 | DELETE_YN | 삭제여부 | VARCHAR2(1) | Y |  |  |  |
| 16 | FROM_DATE | 시작일자 | VARCHAR2(8) | Y |  |  |  |
| 17 | THRU_DATE | 종료일자 | VARCHAR2(8) | Y |  |  |  |
| 18 | REF1 | 참조1 | VARCHAR2(200) | Y |  |  |  |
| 19 | REF2 | 참조2 | VARCHAR2(200) | Y |  |  |  |
| 20 | REF3 | 참조3 | VARCHAR2(200) | Y |  |  |  |
| 21 | REF4 | 참조4 | VARCHAR2(200) | Y |  |  |  |
| 22 | REF5 | 참조5 | VARCHAR2(200) | Y |  |  |  |
<!-- AUTO:END schema -->

# Joins
<!-- AUTO:BEGIN joins -->
(확정된 조인 없음. 조인 관계는 P4 에서 확정한다. 컬럼 표의 '조인후보' 참고)
<!-- AUTO:END joins -->

# T2S 힌트
(사람이 보완하거나 P7 에서 규칙 문서를 링크한다)

<!-- ES-REFLECT:BEGIN (add_info/es_index_generated.csv + DB grain 실측 2026-10-15) -->
### 그레인 (DB 실측 2026-10-15)
- 1행 단위: 공통코드 유형별 개별 코드값 1건
- **업무 키 (유일성 확인)**: `CODE_ID`, `UPPER_CODE_ID`, `FIRST_REGR_ID`, `LAST_MODR_ID` — ROWNUM<=500K 표본 distinct=전체 (유일)
<!-- ES-REFLECT:END -->
