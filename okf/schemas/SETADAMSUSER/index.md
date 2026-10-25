# SETADAMSUSER

테이블·뷰 63건 (분류별).

## master (10)
- [TI_CMMT003](/schemas/SETADAMSUSER/tables/TI_CMMT003.md) — DB테이블 컬럼레이아웃.
- [TI_CMMT004](/schemas/SETADAMSUSER/tables/TI_CMMT004.md) — DB테이블 마스터I/F 추출컬럼 기준정보.
- [TI_CMMT005](/schemas/SETADAMSUSER/tables/TI_CMMT005.md) — DB테이블 EXPORT대상.
- [TN_AD_MASTER_BASE](/schemas/SETADAMSUSER/tables/TN_AD_MASTER_BASE.md) — 마스터DB 기본정보. 키: MASTER_ID, MASTER_VER.
- [TN_AD_MASTER_COLUMN](/schemas/SETADAMSUSER/tables/TN_AD_MASTER_COLUMN.md) — 마스터DB 컬럼정보. 키: MASTER_ID, MASTER_VER, COLUMN_ID.
- [TN_AD_MASTER_SQL](/schemas/SETADAMSUSER/tables/TN_AD_MASTER_SQL.md) — 마스터DB SQL조회 관리.
- [TN_AD_SCENARIO_BASE](/schemas/SETADAMSUSER/tables/TN_AD_SCENARIO_BASE.md) — 시나리오 기본정보.
- [TN_AD_SCENARIO_COLUMN](/schemas/SETADAMSUSER/tables/TN_AD_SCENARIO_COLUMN.md) — 시나리오 컬럼정보. 키: SCENARIO_ID, SCENARIO_VER, SCENARIO_STEP, COLUMN_ID.
- [TN_AD_SCENARIO_LOGIC](/schemas/SETADAMSUSER/tables/TN_AD_SCENARIO_LOGIC.md) — 시나리오 단계별 추출로직. 키: SCENARIO_ID, SCENARIO_VER, SCENARIO_STEP.
- [TS_AD_SCN_KEY](/schemas/SETADAMSUSER/tables/TS_AD_SCN_KEY.md) — 시나리오KEY기준사고대상. 키: SCENARIO_ID, SCENARIO_VER, SCENARIO_STEP, EXT_YM, KEY_NM, COM_NM.

## code (2)
- [TC_CF_COMM_CODE](/schemas/SETADAMSUSER/tables/TC_CF_COMM_CODE.md) — SDP (표준플랫폼)-공통코드. 키: CODE_ID.
- [TC_CF_COMM_CODE_TYPE](/schemas/SETADAMSUSER/tables/TC_CF_COMM_CODE_TYPE.md) — SDP (표준플랫폼)-공통코드유형. 키: COMM_CODE_TYPE_CODE.

## transaction (4)
- [PLAN_TABLE](/schemas/SETADAMSUSER/tables/PLAN_TABLE.md) — 쿼리툴 plan테이블.
- [TI_CMMT050](/schemas/SETADAMSUSER/tables/TI_CMMT050.md) — 첨부파일정보.
- [TS_AD_DB_BID_SUCCESS](/schemas/SETADAMSUSER/tables/TS_AD_DB_BID_SUCCESS.md) — 업체 대시보드 낙찰성공률 상세.
- [TS_AD_SCN_RESULT](/schemas/SETADAMSUSER/tables/TS_AD_SCN_RESULT.md) — 시나리오 실행결과 통합저장. 키: SCENARIO_ID, RUN_SEQ, DATA_SEQ.

## history (1)
- [TI_CMMT002](/schemas/SETADAMSUSER/tables/TI_CMMT002.md) — DB테이블/인덱스 리스트(날짜별)(ALL).

## mapping (1)
- [TN_AD_MASTER_SCENARIO](/schemas/SETADAMSUSER/tables/TN_AD_MASTER_SCENARIO.md) — 마스터vs시나리오. 키: MASTER_ID, SCENARIO_ID.

## summary (8)
- [TI_CMMT001](/schemas/SETADAMSUSER/tables/TI_CMMT001.md) — DB테이블 스페이스 사용현황(날짜별).
- [TS_AD_DB_SAL_DETAIL](/schemas/SETADAMSUSER/tables/TS_AD_DB_SAL_DETAIL.md) — 업체 대시보드 판매현황 SUMMARY.
- [TS_AD_SCN_BCNT](/schemas/SETADAMSUSER/tables/TS_AD_SCN_BCNT.md) — 시나리오 월별 집계결과(+법인).
- [TS_AD_SCN_CNT](/schemas/SETADAMSUSER/tables/TS_AD_SCN_CNT.md) — 시나리오 월별 집계결과. 키: SCENARIO_ID, SCENARIO_VER, SCENARIO_STEP, STD_GB, STD_YM.
- [TS_AD_SCN_KCNT](/schemas/SETADAMSUSER/tables/TS_AD_SCN_KCNT.md) — 시나리오 월별 추출결과(KEY).
- [TS_AD_SCN_RST](/schemas/SETADAMSUSER/tables/TS_AD_SCN_RST.md) — 시나리오 월별 추출내역(인물/업체).
- [TS_AD_SCORE_ENT_RESULT](/schemas/SETADAMSUSER/tables/TS_AD_SCORE_ENT_RESULT.md) — 주요군 현황용 업체점수.
- [TS_AD_SCORE_USER_RESULT](/schemas/SETADAMSUSER/tables/TS_AD_SCORE_USER_RESULT.md) — 주요군 현황용 인물점수.

## view (37)
- [V_MST_COLUMN](/schemas/SETADAMSUSER/views/V_MST_COLUMN.md) — 마스터 컬럼정보. 참조: TN_AD_MASTER_COLUMN.
- [V_MST_IF_CNT](/schemas/SETADAMSUSER/views/V_MST_IF_CNT.md) — 마스터 IF 결과(ETL+데이타기준). 참조: TH_AD_MASTER_RUN, TI_CMMT008, V_MST_LIST.
- [V_MST_LIST](/schemas/SETADAMSUSER/views/V_MST_LIST.md) — 마스터 기본정보(전체). 참조: TC_CF_COMM_CODE, TN_AD_MASTER_BASE, TN_CF_USER.
- [V_MST_LIST2](/schemas/SETADAMSUSER/views/V_MST_LIST2.md) — 마스터 기본정보(전체). 참조: TC_CF_COMM_CODE, TN_AD_MASTER_BASE, TN_CF_USER.
- [V_MST_LIST3](/schemas/SETADAMSUSER/views/V_MST_LIST3.md) — 마스터 요약정보. 참조: V_MST_LIST.
- [V_MST_LIST4](/schemas/SETADAMSUSER/views/V_MST_LIST4.md) — 마스터 요약정보(한글헤더). 참조: V_MST_LIST.
- [V_MST_LIST5](/schemas/SETADAMSUSER/views/V_MST_LIST5.md) — 마스터 연관 시나리오 정보. 참조: TN_AD_MASTER_SCENARIO, V_MST_LIST, V_SCN_LIST.
- [V_MST_LIST6](/schemas/SETADAMSUSER/views/V_MST_LIST6.md) — 마스터 연관 시나리오 정보(한글헤더). 참조: TN_AD_MASTER_SCENARIO, V_MST_LIST, V_SCN_LIST.
- [V_MST_SQL](/schemas/SETADAMSUSER/views/V_MST_SQL.md) — 마스터DB SQL 조회. 참조: TC_CF_COMM_CODE, TN_AD_MASTER_SQL.
- [V_MST_SQL_LIST](/schemas/SETADAMSUSER/views/V_MST_SQL_LIST.md) — 마스터DB SQL 추출컬럼 기준정보. 참조: V_MST_SQL.
- [V_SCN_COL](/schemas/SETADAMSUSER/views/V_SCN_COL.md) — 시나리오 컬럼헤더ID/명. 참조: TN_AD_SCENARIO_COLUMN, V_SCN_LIST.
- [V_SCN_COLID](/schemas/SETADAMSUSER/views/V_SCN_COLID.md) — 시나리오 컬럼헤더ID. 참조: TN_AD_SCENARIO_COLUMN, V_SCN_LIST.
- [V_SCN_COLNM](/schemas/SETADAMSUSER/views/V_SCN_COLNM.md) — 시나리오 컬럼헤더명. 참조: TN_AD_SCENARIO_COLUMN, V_SCN_LIST.
- [V_SCN_INFO](/schemas/SETADAMSUSER/views/V_SCN_INFO.md) — 시나리오 추출컬럼 기준정보(최종단계). 참조: TN_AD_SCENARIO_COLUMN, TN_AD_SCENARIO_LOGIC, V_SCN_LIST2.
- [V_SCN_INFO_PROC](/schemas/SETADAMSUSER/views/V_SCN_INFO_PROC.md) — 시나리오 프로시져 정보. 참조: V_SCN_LIST2.
- [V_SCN_INFO_SQL](/schemas/SETADAMSUSER/views/V_SCN_INFO_SQL.md) — 시나리오 추출컬럼 기준정보(최종단계+SQL). 참조: TN_AD_SCENARIO_COLUMN, TN_AD_SCENARIO_LOGIC, V_SCN_LIST2.
- [V_SCN_INFO_STEP](/schemas/SETADAMSUSER/views/V_SCN_INFO_STEP.md) — 시나리오 추출컬럼 기준정보(단계별). 참조: TN_AD_SCENARIO_COLUMN, TN_AD_SCENARIO_LOGIC, V_SCN_LIST2.
- [V_SCN_LIST](/schemas/SETADAMSUSER/views/V_SCN_LIST.md) — 시나리오 기본정보(등록완료-모든버전). 참조: TC_CF_COMM_CODE, TN_AD_SCENARIO_BASE, TN_AD_SCENARIO_LOGIC.
- [V_SCN_LIST0](/schemas/SETADAMSUSER/views/V_SCN_LIST0.md) — 시나리오 기본정보(전체-최종버전). 참조: TC_CF_COMM_CODE, TN_AD_SCENARIO_BASE, TN_AD_SCENARIO_LOGIC.
- [V_SCN_LIST1](/schemas/SETADAMSUSER/views/V_SCN_LIST1.md) — 시나리오 기본정보(사용중-모든버전). 참조: TC_CF_COMM_CODE, TN_AD_SCENARIO_BASE, TN_AD_SCENARIO_LOGIC.
- [V_SCN_LIST2](/schemas/SETADAMSUSER/views/V_SCN_LIST2.md) — 시나리오 상세정보(전체+단계정보컬럼추가). 참조: TC_CF_COMM_CODE, TN_AD_SCENARIO_BASE, TN_AD_SCENARIO_LOGIC.
- [V_SCN_LIST3](/schemas/SETADAMSUSER/views/V_SCN_LIST3.md) — 시나리오 요약정보(전체). 참조: V_SCN_LIST2.
- [V_SCN_LIST4](/schemas/SETADAMSUSER/views/V_SCN_LIST4.md) — 시나리오 요약정보(한글헤더). 참조: V_SCN_LIST2.
- [V_SCN_LIST5](/schemas/SETADAMSUSER/views/V_SCN_LIST5.md) — 시나리오 연관 마스터 정보. 참조: TN_AD_MASTER_SCENARIO, V_MST_LIST, V_SCN_LIST2.
- [V_SCN_LIST6](/schemas/SETADAMSUSER/views/V_SCN_LIST6.md) — 시나리오 연관 마스터 정보(한글헤더). 참조: TN_AD_MASTER_SCENARIO, V_MST_LIST, V_SCN_LIST2.
- [V_SCN_REPORT](/schemas/SETADAMSUSER/views/V_SCN_REPORT.md) — 시나리오 년간 추출현황(등록완료 기준). 참조: TN_AD_SCENARIO_LOGIC, TS_AD_SCN_CNT, V_SCN_LIST.
- [V_SCN_REPORT10](/schemas/SETADAMSUSER/views/V_SCN_REPORT10.md) — 시나리오 법인별 추출 집계 현황. 참조: TN_AD_SCENARIO_LOGIC, TS_AD_SCN_BCNT, V_SCN_LIST.
- [V_SCN_REPORT2](/schemas/SETADAMSUSER/views/V_SCN_REPORT2.md) — 시나리오 년간(단계별) 추출현황. 참조: V_SCN_REPORT.
- [V_SCN_REPORT3](/schemas/SETADAMSUSER/views/V_SCN_REPORT3.md) — 시나리오 최종 추출현황. 참조: TS_AD_SCN_CNT, V_SCN_INFO, V_SCN_LIST.
- [V_SCN_REPORT4](/schemas/SETADAMSUSER/views/V_SCN_REPORT4.md) — 시나리오 최종 추출현황(년도별). 참조: TS_AD_SCN_CNT, V_SCN_INFO, V_SCN_LIST.
- [V_SCN_REPORT5](/schemas/SETADAMSUSER/views/V_SCN_REPORT5.md) — 시나리오 최종 점검년월. 참조: TS_AD_SCN_CNT.
- [V_SCN_REPORT6](/schemas/SETADAMSUSER/views/V_SCN_REPORT6.md) — 시나리오 년간 추출현황(법인별). 참조: TN_AD_SCENARIO_LOGIC, TS_AD_SCN_BCNT, V_SCN_LIST.
- [V_SCN_REPORT7](/schemas/SETADAMSUSER/views/V_SCN_REPORT7.md) — 시나리오 년간(단계별) 추출현황(법인별). 참조: V_SCN_REPORT6.
- [V_SCN_REPORT8](/schemas/SETADAMSUSER/views/V_SCN_REPORT8.md) — 시나리오 조건별 추출현황. 참조: TS_AD_SCN_CNT, V_SCN_LIST.
- [V_SCN_REPORT9](/schemas/SETADAMSUSER/views/V_SCN_REPORT9.md) — 시나리오 조건별 추출현황(법인별). 참조: TS_AD_SCN_BCNT, V_SCN_LIST.
- [V_SCN_SQL](/schemas/SETADAMSUSER/views/V_SCN_SQL.md) — 시나리오 추출조회SQL. 참조: TN_AD_SCENARIO_COLUMN, TN_AD_SCENARIO_LOGIC, V_SCN_LIST.
- [V_TI_CMMT050](/schemas/SETADAMSUSER/views/V_TI_CMMT050.md) — 첨부파일정보. 참조: TI_CMMT050.
