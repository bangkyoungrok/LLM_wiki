---
type: Oracle Table
title: SDP (표준플랫폼)-공통코드유형
description: 'SDP (표준플랫폼)-공통코드유형. 키: COMM_CODE_TYPE_CODE.'
resource: oracle://PRD/SETADAMSUSER/TC_CF_COMM_CODE_TYPE
tags: ['kind:table', 'owner:setadamsuser', 'class:code', 'size:xs', 'access:select-full', 'has:pk', 'has:soft-delete', 'domain:fin-master']
owner: SETADAMSUSER
table_name: TC_CF_COMM_CODE_TYPE
query_name: SETADAMSUSER.TC_CF_COMM_CODE_TYPE
table_class: code
primary_key: [COMM_CODE_TYPE_CODE]
row_count: 117
last_analyzed: 2026-06-12
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
| 1 | COMM_CODE_TYPE_CODE | 공통코드유형코드 | VARCHAR2(20) | N | PK |  |  |
| 2 | COMM_CODE_TYPE_NAME | 공통코드유형명 | VARCHAR2(1000) | Y |  |  |  |
| 3 | DESCRIPTION | 설명 | VARCHAR2(2000) | Y |  |  |  |
| 4 | FIRST_REG_DATETIME | 최초등록일시 | DATE | Y |  |  |  |
| 5 | FIRST_REGR_ID | 최초등록자ID | VARCHAR2(100) | Y |  |  |  |
| 6 | LAST_MOD_DATETIME | 최종수정일시 | DATE | Y |  |  |  |
| 7 | LAST_MODR_ID | 최종수정자ID | VARCHAR2(100) | Y |  |  |  |
| 8 | KO_LABEL | 공통코드명(한글) | VARCHAR2(500) | Y |  |  |  |
| 9 | EN_LABEL | 공통코드명(영문) | VARCHAR2(500) | Y |  |  |  |
| 10 | LABEL | 공통코드명(기타) | VARCHAR2(500) | Y |  |  |  |
| 11 | DELETE_YN | 삭제여부(미삭제:0,삭제:1) | VARCHAR2(1) | Y |  |  |  |
| 12 | FROM_DATE | 시작일자 | VARCHAR2(8) | Y |  |  |  |
| 13 | THRU_DATE | 종료일자 | VARCHAR2(8) | Y |  |  |  |
<!-- AUTO:END schema -->

# Joins
<!-- AUTO:BEGIN joins -->
(확정된 조인 없음. 조인 관계는 P4 에서 확정한다. 컬럼 표의 '조인후보' 참고)
<!-- AUTO:END joins -->

# T2S 힌트
(사람이 보완하거나 P7 에서 규칙 문서를 링크한다)

<!-- ES-REFLECT:BEGIN (add_info/es_index_generated.csv + DB grain 실측 2026-10-15) -->
### 그레인 (DB 실측 2026-10-15)
- 1행 단위: 공통코드 유형 1건
- **업무 키 (유일성 확인)**: `COMM_CODE_TYPE_CODE` — ROWNUM<=500K 표본 distinct=전체 (유일)
<!-- ES-REFLECT:END -->
