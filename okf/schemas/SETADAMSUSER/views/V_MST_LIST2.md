---
type: Oracle View
title: 마스터 기본정보(전체)
description: '마스터 기본정보(전체). 참조: TC_CF_COMM_CODE, TN_AD_MASTER_BASE, TN_CF_USER.'
resource: oracle://PRD/SETADAMSUSER/V_MST_LIST2
tags: ['kind:view', 'owner:setadamsuser', 'class:view', 'access:select-full', 'has:soft-delete', 'has:code-column', 'has:lob']
owner: SETADAMSUSER
table_name: V_MST_LIST2
query_name: SETADAMSUSER.V_MST_LIST2
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
| 2 | MASTER_SEQ | 마스터순번 | NUMBER(4,1) | Y |  |  |  |
| 3 | SEQ | 마스터화면정렬순서 | NUMBER | Y |  |  |  |
| 4 | BUSINESS_TYPE | 업무구분 코드-GCM004 (M1 재무 M2 구매 M3 제조 M4 영업마케팅 M5 물류 M6 개발 M7 서비스 M8 인사총무 M9 보안 M10 BQMS | VARCHAR2(10) | N |  |  |  |
| 5 | BUSINESS_TYPE_NM | 업무구분 명 | VARCHAR2(500) | Y |  |  |  |
| 6 | MASTER_ID | 마스터ID | VARCHAR2(20) | N |  |  |  |
| 7 | MASTER_VER | 마스터버전 | NUMBER(10,1) | N |  |  |  |
| 8 | MASTER_NM | 마스터명 | VARCHAR2(200) | N |  |  |  |
| 9 | MASTER_TYPE | 마스터 유형코드-GCM010 (10:원본, 20:결합, 30:임시, 50:점검용) | CHAR(2) | N |  | 코드후보 |  |
| 10 | MASTER_TYPE_NM | 마스터 유형명 | VARCHAR2(500) | Y |  |  |  |
| 11 | MASTER_OUTLINE | 마스터 개요 | VARCHAR2(500) | Y |  |  |  |
| 12 | TARGET_TABLE_ID | TargetTable ID | VARCHAR2(50) | N |  |  |  |
| 13 | TARGET_TABLE_NM | TargetTable 명 | VARCHAR2(200) | N |  |  |  |
| 14 | PROPOSER_ID | 제안자ID | VARCHAR2(30) | N |  |  |  |
| 15 | PROPOSER_NM | 제안자명 | VARCHAR2(50) | N |  |  |  |
| 16 | CHARGE_PERSON_ID | 담당자ID | VARCHAR2(30) | N |  |  |  |
| 17 | CHARGE_PERSON_NM | 담당자명 | VARCHAR2(50) | N |  |  |  |
| 18 | ADMIN_ID | 운영자ID | VARCHAR2(30) | N |  |  |  |
| 19 | ADMIN_NM | 운영자명 | VARCHAR2(50) | N |  |  |  |
| 20 | IF_SYSTEM_NM | 대상시스템명 | VARCHAR2(200) | Y |  |  |  |
| 21 | IF_SYSTEM_MODULE_NM | 대상시스템 모듈명 | VARCHAR2(50) | Y |  |  |  |
| 22 | IF_SYSTEM_CHARGE_PERSON_ID | 대상시스템 담당자ID | VARCHAR2(30) | Y |  |  |  |
| 23 | IF_SYSTEM_CHARGE_PERSON_NM | 대상시스템 담당자명 | VARCHAR2(50) | Y |  |  |  |
| 24 | IF_SYSTEM_ADMIN_ID | 대상시스템 운영자ID | VARCHAR2(30) | Y |  |  |  |
| 25 | IF_SYSTEM_ADMIN_NM | 대상시스템 운영자명 | VARCHAR2(50) | Y |  |  |  |
| 26 | INTERFACE_TYPE | I/F방식 코드-INT010 (10:EAI, 20:ETL, 30:JDBC, 40:웹서비스, 50:파일업로드) | CHAR(2) | Y |  | 코드후보 |  |
| 27 | INTERFACE_TYPE_NM | I/F방식 코드명 | VARCHAR2(500) | Y |  |  |  |
| 28 | PERIOD_TYPE | I/F주기-GCS031 (10:일,20:주,30:월,40:분기,50:년,60:반기,70:임의) | CHAR(2) | Y |  | 코드후보 |  |
| 29 | PERIOD_TYPE_NM | I/F주기 | VARCHAR2(500) | Y |  |  |  |
| 30 | DEFAULT_BASE | Default 조회기간 구분: GCS031 그룹코드 활용 (데이터 양에 따른 설정) | CHAR(2) | Y |  |  |  |
| 31 | DEFAULT_SEARCH | 조회기간 숫자값: 구분에 대한 숫자값 | VARCHAR2(5) | Y |  |  |  |
| 32 | GRID_DISPLAY_YN | 화면OPEN시 GRID 자동 표시 여부YN | CHAR(1) | N |  |  |  |
| 33 | DEFAULT_SEARCH_PERIOD | 마스터 기본조회기간 설정(기본:3개월) | NUMBER | Y |  |  |  |
| 34 | DIV_COCD | 대상범위-A1 CE/IM(본사) ,B1 한국총괄, B2 중국총괄, B3 삼성전자로지텍, B4 삼성전자판매, B5 삼성전자서비스 ,B6 삼성메디슨, CO: 공통, ZZ: 미분류 | VARCHAR2(100) | Y |  |  |  |
| 35 | DIV_CONM | 대상범위 | VARCHAR2(4000) | Y |  |  |  |
| 36 | PRESERVE_PERIOD | 보존주기 | VARCHAR2(10) | Y |  |  |  |
| 37 | PRESERVE_PERIOD_NM | 보존주기명 | VARCHAR2(500) | Y |  |  |  |
| 38 | USE_YN | 사용여부YN | CHAR(1) | Y |  |  |  |
| 39 | DELETE_YN | 삭제여부YN | CHAR(1) | Y |  |  |  |
| 40 | FINAL_YN | 최종버전여부(Y/N) | CHAR(1) | Y |  |  |  |
| 41 | STATUS_TYPE | 상태 코드-GCV010(10:작성중, 20:개발요청, 30:개발중, 40:요청반려, 50:개발완료, 60:보완요청, 70:등록요청, 80:등록완료, 90:폐기요청, 91:폐기완료) | CHAR(2) | Y |  | 코드후보 |  |
| 42 | STATUS_TYPE_NM | 상태명 | VARCHAR2(500) | Y |  |  |  |
| 43 | REGISTER_NM | 최초등록자 | VARCHAR2(600) | Y |  |  |  |
| 44 | REGISTER_DT | 최초등록일시 | DATE | Y |  |  |  |
| 45 | MODIFIER_NM | 최종변경자 | VARCHAR2(600) | Y |  |  |  |
| 46 | MODIFIER_DT | 최종변경일시 | DATE | Y |  |  |  |
| 47 | BUSINESS_LOGIC | 추출로직 | VARCHAR2(4000) | Y |  |  |  |
| 48 | BUSINESS_SQL | 참조SQL | CLOB | Y |  |  |  |
<!-- AUTO:END schema -->

# Definition
<!-- AUTO:BEGIN definition -->
```sql
select /* 마스터 기본정보(전체) */
         a.ord
        --,dense_rank() over (order by a.ord, a.business_type, a.master_id, to_number(a.master_ver)) as seq
        ,a.master_seq
        ,dense_rank() over (order by a.ord, a.business_type, a.master_seq, (case when instr(a.div_cocd,'A1') > 0 then 'A1' else a.DIV_COCD end), a.master_id, to_number(a.master_ver)) as seq
        ,a.business_type,a.business_type_nm,a.master_id,a.master_ver,a.master_nm
        ,a.master_type,a.master_type_nm
        ,a.master_outline,a.target_table_id,a.target_table_nm,a.proposer_id,a.proposer_nm,a.charge_person_id,a.charge_person_nm,a.admin_id,a.admin_nm
        ,a.if_system_nm,a.if_system_module_nm,a.if_system_charge_person_id,a.if_system_charge_person_nm,a.if_system_admin_id,a.if_system_admin_nm
        ,a.interface_type,a.interface_type_nm,a.period_type,a.period_type_nm,a.default_base,a.default_search,a.grid_display_yn,a.default_search_period
        ,a.div_cocd,a.div_conm,a.preserve_period,a.preserve_period_nm
        ,a.use_yn,a.delete_yn,a.final_yn,a.status_type,a.status_type_nm,a.register_nm,a.register_dt,a.modifier_nm,a.modifier_dt,a.business_logic,a.business_sql
from (
    select
       (select ord from TC_CF_COMM_CODE where COMM_CODE_TYPE_CODE ='GCM004' and CODE = a.business_type and delete_yn='0' ) as  ord
       , a.business_type
       , (select ko_label from TC_CF_COMM_CODE where COMM_CODE_TYPE_CODE = 'GCM004' and CODE = a.business_type and delete_yn='0')  as business_type_nm
       , a.master_id,a.master_ver,a.master_nm
       , a.master_type
       , (select ko_label from TC_CF_COMM_CODE where COMM_CODE_TYPE_CODE = 'GCM010' and CODE = a.master_type and delete_yn='0')  as master_type_nm
       , a.master_outline,a.target_table_id,a.target_table_nm
       , a.proposer_id,a.proposer_nm,a.charge_person_id,a.charge_person_nm
       , a.admin_id,a.admin_nm
       , a.if_system_nm,decode(a.if_system_module_nm,'N/A','',a.if_system_module_nm) as if_system_module_nm, a.if_system_charge_person_id,a.if_system_charge_person_nm,a.if_system_admin_id,a.if_system_admin_nm
       , a.interface_type
        , (select ko_label from TC_CF_COMM_CODE where COMM_CODE_TYPE_CODE = 'INT010' and CODE = a.interface_type and delete_yn='0')  as interface_type_nm
       , a.period_type
       , (select ko_label from TC_CF_COMM_CODE where COMM_CODE_TYPE_CODE = 'GCS031' and CODE = a.period_type and delete_yn='0')  as period_type_nm
       , a.default_base,a.default_search
       , a.grid_display_yn,a.default_search_period
   , a.div_cocd
   , replace(replace(replace(replace(replace(replace(replace(replace(replace(a.div_cocd, 'A1','본사'),'B1','한총'),'B2','중총'),'B3','로직텍'),'B4','판매'),'B5','서비스'),'B6','메디슨'),'CO','공통'),'ZZ','미분류') as div_conm
       , a.preserve_period
       , (select ko_label from TC_CF_COMM_CODE where COMM_CODE_TYPE_CODE = 'GCS034' and CODE = a.preserve_period and delete_yn='0')  as preserve_period_nm
       , a.use_yn,a.delete_yn
       , (case when a.master_ver = (select max(master_ver) from TN_AD_MASTER_BASE where master_id = a.master_id and use_yn='Y' and status_type ='80' ) then 'Y' else 'N' end) as final_yn  -- 최종버전여부
       , a.status_type
       , (select ko_label from TC_CF_COMM_CODE where COMM_CODE_TYPE_CODE = 'GCV010' and CODE = a.status_type and delete_yn='0')  as status_type_nm
       , nvl((select user_name from TN_CF_USER where user_id = a.register_id), a.register_id) as register_nm
       , a.register_dt
       , nvl((select user_name from TN_CF_USER where user_id = a.modifier_id),a.modifier_id) as modifier_nm
       , a.modifier_dt
       , a.business_logic,a.business_sql
       , a.master_seq
from TN_AD_MASTER_BASE a
where 1=1
--and a.use_yn='Y'
--and a.status_type ='80' -- 등록완료
--and a.master_ver = (select max(master_ver) from TN_AD_MASTER_BASE where master_id = a.master_id)
) a
--order by a.ord, a.business_type, a.master_id, to_number(a.master_ver)
```
<!-- AUTO:END definition -->

# 참조 객체
<!-- AUTO:BEGIN deps -->
- [TC_CF_COMM_CODE](/schemas/SETADAMSUSER/tables/TC_CF_COMM_CODE.md)
- [TN_AD_MASTER_BASE](/schemas/SETADAMSUSER/tables/TN_AD_MASTER_BASE.md)
- SETADAMSUSER.TN_CF_USER (번들 밖)
<!-- AUTO:END deps -->

# T2S 힌트
(사람이 보완하거나 P7 에서 규칙 문서를 링크한다)

<!-- ES-REFLECT:BEGIN (add_info/es_index_generated.csv + DB grain 실측 2026-10-15) -->
### 그레인 (DB 실측 2026-10-15)
- 1행 단위: 마스터 ID(MASTER_ID) 및 버전(MASTER_VER) 단위 마스터 정의 1건
- **업무 키 (유일성 확인)**: `MASTER_ID`, `MASTER_VER` — ROWNUM<=500K 표본 distinct=전체 (유일)
<!-- ES-REFLECT:END -->
