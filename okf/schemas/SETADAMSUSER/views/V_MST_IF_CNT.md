---
type: Oracle View
title: 마스터 IF 결과(ETL+데이타기준)
description: '마스터 IF 결과(ETL+데이타기준). 참조: TH_AD_MASTER_RUN, TI_CMMT008, V_MST_LIST.'
resource: oracle://PRD/SETADAMSUSER/V_MST_IF_CNT
tags: ['kind:view', 'owner:setadamsuser', 'class:view', 'access:select-full', 'has:validity-period', 'has:code-column']
owner: SETADAMSUSER
table_name: V_MST_IF_CNT
query_name: SETADAMSUSER.V_MST_IF_CNT
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
| 1 | BUSINESS_TYPE | 업무구분 코드-GCM004 (M1 재무 M2 구매 M3 제조 M4 영업마케팅 M5 물류 M6 개발 M7 서비스 M8 인사총무 M9 보안 M10 BQMS | VARCHAR2(10) | N |  |  |  |
| 2 | BUSINESS_TYPE_NM | 업무구분 명 | VARCHAR2(500) | Y |  |  |  |
| 3 | MASTER_TYPE | 마스터 유형코드-GCM010 (10:원본, 20:결합, 30:임시, 50:점검용) | CHAR(2) | N |  | 코드후보 |  |
| 4 | MASTER_TYPE_NM | 마스터 유형명 | VARCHAR2(500) | Y |  |  |  |
| 5 | MASTER_ID | 마스터ID | VARCHAR2(20) | N |  |  |  |
| 6 | MASTER_VER | 마스터버전 | NUMBER(10,1) | N |  |  |  |
| 7 | MASTER_NM | 마스터명 | VARCHAR2(200) | N |  |  |  |
| 8 | TARGET_TABLE_ID | TargetTable ID | VARCHAR2(50) | N |  |  |  |
| 9 | START_DT | 시작일 | DATE | Y |  |  |  |
| 10 | END_DT | 종료일 | DATE | Y |  |  |  |
| 11 | STD_DT | 기준일 | VARCHAR2(8) | Y |  |  |  |
| 12 | CNT | 건수 | NUMBER | Y |  |  |  |
| 13 | IF_COUNT | IF건수 | NUMBER | Y |  |  |  |
| 14 | STD_GB | 기준일구분 | VARCHAR2(20) | Y |  |  |  |
| 15 | IF_DT | IF일자 | VARCHAR2(8) | Y |  |  |  |
| 16 | IF_CNT | IF건수 | NUMBER | Y |  |  |  |
<!-- AUTO:END schema -->

# Definition
<!-- AUTO:BEGIN definition -->
```sql
with tmp_run  -- 마스터 RUN 집계 (ETL + JAVA)
as (
select a.master_id, a.master_ver, a.start_dt, a.end_dt, a.std_dt, a.cnt, a.if_count_sum as if_count--, a.if_count, a.no, a.no_d, a.no_m
from (
select a.master_id, a.master_ver
        , a.start_dt, a.end_dt
        , to_char(a.start_dt,'yyyymmdd') as std_dt
        , a.if_count
        , row_number() over (partition by a.master_id, a.master_ver, to_char(a.start_dt,'yyyy-mm-dd') order by a.start_dt desc ) as no_d  -- 마스터별 일별건수 체크용
            , row_number() over (partition by a.master_id, a.master_ver order by a.start_dt desc ) as no_m   -- 마스터별 건수 체크용
        , count(*) over (partition by a.master_id, a.master_ver, to_char(a.start_dt,'yyyy-mm-dd')) as cnt  -- IF 수행횟수
        , sum(a.if_count) over (partition by a.master_id, a.master_ver, to_char(a.start_dt,'yyyy-mm-dd')) as if_count_sum  -- IF 건수 합계
        , a.no
from (
select a.*
        , row_number() over (partition by a.master_id, a.master_ver, a.run_seq, a.start_dt, a.if_count order by a.start_dt desc ) as no  -- 중복 I/F 건수 제거
from th_ad_master_run a
where 1=1
--and to_char(a.start_dt,'yyyy-mm-dd') >= '2020-11-14'
--and master_id || run_seq in  (select master_id || max (run_seq) from th_ad_master_run group by master_id)
--and regexp_like (div_cocd, 'a1|b1|b2|b3|b4|b5|b6|zz|zz|co')
and a.use_yn = 'Y'
and a.delete_yn = 'N'
   ) a
   where no =1  -- 중복 I/F 건수 제거
) a
where 1=1
--and no_d =1 -- 마스터별 일별건수
and no_m =1 -- 마스터별 건수
order by master_id, master_ver, start_dt
)
, tmp_cm  -- I/F 집계 (프로시져 데이타기준)
as (
select a.*
from (
select a.*
         , row_number() over (partition by a.owner, a.table_id order by a.ym desc, decode(a.std_gb,'입력월',1,'대상월',2)) as no
from TI_CMMT008 a
where 1=1
and a.owner ='SETADAMSUSER'
) a
where 1=1
and no =1
)

select a.business_type, a.business_type_nm, a.master_type, a.master_type_nm, a.master_id, a.master_ver, a.master_nm, a.target_table_id
       , b.start_dt, b.end_dt, b.std_dt, b.cnt, b.if_count
       , c.std_gb, c.if_dt, c.cnt as if_cnt
from v_mst_list a, tmp_run b, tmp_cm c
where 1=1
and a.final_yn='Y'
and a.master_id = b.master_id(+)
and a.master_ver = b.master_ver(+)

and a.target_table_id = c.table_id(+)

--order by a.ord, a.business_type, a.master_id, to_number(a.master_ver);
```
<!-- AUTO:END definition -->

# 참조 객체
<!-- AUTO:BEGIN deps -->
- SETADAMSUSER.TH_AD_MASTER_RUN (번들 밖)
- SETADAMSUSER.TI_CMMT008 (번들 밖)
- [V_MST_LIST](/schemas/SETADAMSUSER/views/V_MST_LIST.md)
<!-- AUTO:END deps -->

# T2S 힌트
(사람이 보완하거나 P7 에서 규칙 문서를 링크한다)

<!-- ES-REFLECT:BEGIN (add_info/es_index_generated.csv + DB grain 실측 2026-10-15) -->
### 그레인 (DB 실측 2026-10-15)
- 1행 단위: 비즈니스 유형·마스터 유형·마스터 ID·버전·기준일 단위 IF 건수 집계 1건
- **업무 키 (유일성 확인)**: `MASTER_ID`, `TARGET_TABLE_ID` — ROWNUM<=500K 표본 distinct=전체 (유일)
<!-- ES-REFLECT:END -->
