---
type: Oracle View
title: 마스터 요약정보
description: '마스터 요약정보. 참조: V_MST_LIST.'
resource: oracle://PRD/SETADAMSUSER/V_MST_LIST3
tags: ['kind:view', 'owner:setadamsuser', 'class:view', 'access:select-full', 'has:soft-delete']
owner: SETADAMSUSER
table_name: V_MST_LIST3
query_name: SETADAMSUSER.V_MST_LIST3
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
table_type: 기준정보
business_area: 시스템
business_detail: 시나리오
---

# 개요
(사람이 보완: 이 뷰가 무엇을 조인해서 보여 주는지)

# Schema
<!-- AUTO:BEGIN schema -->
| # | 컬럼 | 한글명 | 타입 | NULL | 키 | 코드/참조 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | ORD | 마스터업무구분순서 | NUMBER | Y |  |  |  |
| 2 | SEQ | 마스터화면정렬순서 | NUMBER | Y |  |  |  |
| 3 | BUSINESS_TYPE_NM | 업무구분 명 | VARCHAR2(500) | Y |  |  |  |
| 4 | MASTER_ID | 마스터ID | VARCHAR2(20) | N |  |  |  |
| 5 | MASTER_VER | 마스터버전 | NUMBER(10,1) | N |  |  |  |
| 6 | MASTER_NM | 마스터명 | VARCHAR2(200) | N |  |  |  |
| 7 | MASTER_TYPE_NM | 마스터 유형명 | VARCHAR2(500) | Y |  |  |  |
| 8 | MASTER_OUTLINE | 마스터 개요 | VARCHAR2(500) | Y |  |  |  |
| 9 | TARGET_TABLE_ID | TargetTable ID | VARCHAR2(50) | N |  |  |  |
| 10 | TARGET_TABLE_NM | TargetTable 명 | VARCHAR2(200) | N |  |  |  |
| 11 | CHARGE_PERSON_NM | 담당자명 | VARCHAR2(50) | N |  |  |  |
| 12 | ADMIN_NM | 운영자명 | VARCHAR2(50) | N |  |  |  |
| 13 | IF_SYSTEM_NM | 대상시스템명 | VARCHAR2(200) | Y |  |  |  |
| 14 | IF_SYSTEM_MODULE_NM | 대상시스템 모듈명 | VARCHAR2(50) | Y |  |  |  |
| 15 | INTERFACE_TYPE_NM | I/F방식 코드명 | VARCHAR2(500) | Y |  |  |  |
| 16 | PERIOD_TYPE_NM | I/F주기 | VARCHAR2(500) | Y |  |  |  |
| 17 | DIV_COCD | 조회범위- CE/IM(본사) ,B1 한국총괄, B2 중국총괄, B3 삼성전자로지텍, B4 삼성전자판매, B5 삼성전자서비스 ,B6 삼성메디슨, CO: 공통, ZZ: 미분류 | VARCHAR2(100) | Y |  |  |  |
| 18 | PRESERVE_PERIOD_NM | 보존주기명 | VARCHAR2(500) | Y |  |  |  |
| 19 | USE_YN | 사용여부YN | CHAR(1) | Y |  |  |  |
| 20 | DELETE_YN | 삭제여부YN | CHAR(1) | Y |  |  |  |
| 21 | FINAL_YN | 최종버전여부(Y/N) | CHAR(1) | Y |  |  |  |
| 22 | STATUS_TYPE_NM | 상태명 | VARCHAR2(500) | Y |  |  |  |
| 23 | BUSINESS_LOGIC | 추출로직 | VARCHAR2(4000) | Y |  |  |  |
<!-- AUTO:END schema -->

# Definition
<!-- AUTO:BEGIN definition -->
```sql
select
a.ORD
,a.SEQ
--,a.BUSINESS_TYPE
,a.BUSINESS_TYPE_NM
,a.MASTER_ID
,a.MASTER_VER
,a.MASTER_NM
--,a.MASTER_TYPE
,a.MASTER_TYPE_NM
,a.MASTER_OUTLINE
,a.TARGET_TABLE_ID
,a.TARGET_TABLE_NM
--,a.PROPOSER_ID
--,a.PROPOSER_NM
--,a.CHARGE_PERSON_ID
,a.CHARGE_PERSON_NM
--,a.ADMIN_ID
,a.ADMIN_NM
,a.IF_SYSTEM_NM
,a.IF_SYSTEM_MODULE_NM
--,a.IF_SYSTEM_CHARGE_PERSON_ID
--,a.IF_SYSTEM_CHARGE_PERSON_NM
--,a.IF_SYSTEM_ADMIN_ID
--,a.IF_SYSTEM_ADMIN_NM
--,a.INTERFACE_TYPE
,a.INTERFACE_TYPE_NM
--,a.PERIOD_TYPE
,a.PERIOD_TYPE_NM
--,a.DEFAULT_BASE
--,a.DEFAULT_SEARCH
--,a.GRID_DISPLAY_YN
--,a.DEFAULT_SEARCH_PERIOD
,a.DIV_COCD
--,a.PRESERVE_PERIOD
,a.PRESERVE_PERIOD_NM
,a.USE_YN
,a.DELETE_YN
,a.FINAL_YN
--,a.STATUS_TYPE
,a.STATUS_TYPE_NM
--,a.REGISTER_ID
--,a.REGISTER_DT
--,a.MODIFIER_ID
--,a.MODIFIER_DT
,a.BUSINESS_LOGIC
--,a.BUSINESS_SQL
from V_MST_LIST a
where 1=1
--and a.FINAL_YN ='Y' -- 최종
```
<!-- AUTO:END definition -->

# 참조 객체
<!-- AUTO:BEGIN deps -->
- [V_MST_LIST](/schemas/SETADAMSUSER/views/V_MST_LIST.md)
<!-- AUTO:END deps -->

# T2S 힌트
(사람이 보완하거나 P7 에서 규칙 문서를 링크한다)

<!-- ES-REFLECT:BEGIN (add_info/es_index_generated.csv + DB grain 실측 2026-10-15) -->
### 그레인 (DB 실측 2026-10-15, 전체 스캔)
- 1행 단위: 마스터 ID 및 버전 단위 마스터 메타데이터 1건
- **업무 키 (유일성 확인)**: `MASTER_ID`, `TARGET_TABLE_ID`, `SEQ` — greedy 탐색(500K 표본) + 전체 스캔 dup 0
<!-- ES-REFLECT:END -->
