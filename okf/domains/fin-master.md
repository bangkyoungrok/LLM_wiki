---
type: Business Domain
title: 재무 기준정보(마스터)
description: 재무 기준정보(마스터). 코드마스터(TI_GRPF910), 총계정원장(TI_GRPF902), 환율(TI_MT_EXCHRATE), 공통코드(TC_CF_COMM_CODE).
tags: ["domain:fin-master"]
system: 재무
domain_name: 기준정보(마스터)
status: draft
sources:
- id: add-info
  resource: /references/domain-sources.md
  title: add_info/domain 이식
---

# 재무 / 기준정보(마스터)

## 프로세스

**총계정원장(G/L Account, General Ledger)**은 N-ERP 시스템의 재무회계(FI) 및 영업/물류(SD/MM) 모듈에서 자산, 부채, 자본, 수익, 비용의 증감을 기록하고 계산하는 가장 기본적인 단위입니다.
총계정원장에 대한 주요 내용은 다음과 같습니다.
1. 정의 및 역할

기록의 근간: 모든 회계 거래는 총계정원장을 통해 기록되며, 이는 재무상태표(Balance Sheet)와 손익계산서(Profit and Loss Statement)를 작성하는 근간이 됩니다.
회계 처리: 모든 거래는 차변(Dr)과 대변(Cr)으로 구분되어 기록됩니다.
모듈 간 연계: 매출이나 매입과 같은 영업/물류 활동(SD/MM)의 결과가 최종적으로 총계정원장에 회계 전표로 전기됩니다.

2. 주요 관리 및 조회 기능

계정 마스터 관리:
GCoA(Global Chart of Account, 계정과목표): 삼성전자의 표준 계정과목 일람표로, 모든 회계 처리의 체계적인 분류 기준이 됩니다.
계정 생성 및 업로드: ZLFIZGL00002(Upload G/L Account) 등의 프로그램을 통해 신규 계정을 생성하거나 지역 회계과목표(Local CoA)를 업로드할 수 있습니다.
계정 조회 및 상태 확인:
Fiori App(Display G/L Account Master Data) 또는 **FS00(Display G/L Account Master Data)**를 통해 계정의 세부 마스터 정보를 조회할 수 있습니다.
**ZRFIZGL00001(Display G/L Account Status)**를 통해 계정의 상태를 일괄적으로 조회할 수 있습니다.
변경 내역 관리: ZFRFIZGL0001(Display GL Account) 등을 사용하여 등록된 계정의 변경 이력(Change History)을 조회할 수 있습니다.

N-ERP의 환율 관리 프로세스는 국가별 통화 및 환율을 관리하기 위해 통화 마스터를 등록하고, 외부 시스템으로부터 환율을 인터페이스(I/F) 받거나 담당자가 수작업으로 등록하는 과정을 포함합니다.
주요 사용 및 등록 기준은 다음과 같습니다.
1. 환율 사용 및 등록 기준
환율은 법적 제약 여부와 데이터 소스에 따라 다음과 같이 구분하여 사용합니다.

법적 제약이 있는 경우: 각국 중앙은행에서 고시하는 환율을 사용합니다.
특정 통화(RUB, BRL, HUF, PLN, EUR): Bloomberg 인터페이스(I/F) 환율을 사용합니다.
그 외 국가: 각국 중앙은행 고시 환율을 RPA로 자동 업로드하거나, 법인 담당자가 수작업으로 입력합니다.
법적 제약이 없는 경우: 하나은행 환율 기준의 Conversion(변환) 환율을 사용합니다.
하나은행 I/F: KRW(원화)의 경우 매일 오전 09:30경에 자동 I/F되며, 하나은행 최초고시환율(매매기준율 = M타입)을 사용합니다.
환율 변환: KRW 이외의 통화 환율은 KRW 환율을 사용하여 Conversion(변환)하여 생성합니다.
원자재 관련: 하나은행 신규 환율(전월 평균) 수신 시, 원자재 PO 발주 시 Vendor와 협의된 환율을 적용해야 합니다.

## 테이블과 조회 기준

<코드마스터> : TI_GRPF910
# 컬럼 코드에 대한 코드명 및 부가정보 조회
# 데이터에서 사용하는 코드/코드명은 주로 TI_GRPF910 테이블을 사용
# GRPCD(그룹코드),CD(코드),CDNM(코드명),ECD1~ECD7(코드에 대한 부가정보)
# 일부 조직/마스터 정보도 코드정보에 포함되어 있으나, 원본 테이블을 주로 참조
     (예 : 법인코드가 TI_GRPF910, TC_CF_COMM_CODE에도 있지만 TI_GPRF900을 메인으로 사용)
* 코드마스터 : TI_GRPF910
* 그룹코드마스터(코드그룹정보) : TI_GRPF910_GRP
* 웹시스템용 코드마스터 : TC_CF_COMM_CODE
* 웹시스템용 그룹 코드마스터 : TC_CF_COMM_CODE_TYPE

<총계정원장> : TI_GRPF902
# 비용/수익/자산 등에 대한 계정정보
# 예: 광고비,광고선전비,마케팅비용,판촉비,프로모션비용,지급수수료 등
* 총계정원장(계정코드당 1줄로 표현) : TI_GRPF902
* 총계정원장(SKAT) ERP원본(언어별 계정코드/계정명) : TI_GRPF902_ALL

<환율> : TI_MT_EXCHRATE
# 기준일, 통화, KRW환율, USD환율, (from 매매기준율)
# 표현단위는 일반적인 표시용 환율이 아닌 실계산용 환율임
# ERP에서는 법인/용도별 별도환율를 기준으로 하나, 시스템에서는 편의상 한개로 사용함
    (I/F 환율계산 금액이 시스템에서 계산한 금액과 차이가 있을 수 있음)
* ERP 환율 I/F 테이블 : TI_GRPF912
* ERP 통화 환산키(ERP에서 DB로 직접 데이터를 받을 경우 환산필요) : TI_GRPF912_CONV
* 환율정보 : TI_MT_EXCHRATE
* 월평균환율정보 : TI_MT_EXCHRATE_YM
* 주평균환율정보 : TI_MT_EXCHRATE_YW

## 테이블 목록

| 테이블 | 유형 (table_type) | 설명 (table_rule) |
|---|---|---|
| [TC_CF_COMM_CODE](/schemas/SETADAMSUSER/tables/TC_CF_COMM_CODE.md) | 기준정보 |  |
| [TC_CF_COMM_CODE_TYPE](/schemas/SETADAMSUSER/tables/TC_CF_COMM_CODE_TYPE.md) | 기준정보 |  |
| [TI_GRPF902](/schemas/APPADAMSUSER/tables/TI_GRPF902.md) |  | 계정코드 |
| [TI_GRPF902_ALL](/schemas/APPADAMSUSER/tables/TI_GRPF902_ALL.md) |  |  |
| [TI_GRPF903](/schemas/APPADAMSUSER/tables/TI_GRPF903.md) |  |  |
| [TI_GRPF910](/schemas/APPADAMSUSER/tables/TI_GRPF910.md) |  | => 조회 방법(코드, 그룹코드 입력)     (select  cdnm from ti_grpf910 where grpcd='그룹코드' and cd ='코드') as "코드명"     (select  ecd1 from ti_grpf910 where grpcd='그룹코드' and cd ='코드') as "부가정보1" |
| [TI_GRPF910_GRP](/schemas/APPADAMSUSER/tables/TI_GRPF910_GRP.md) |  |  |
| [TI_GRPF912](/schemas/APPADAMSUSER/tables/TI_GRPF912.md) |  | ERP 환율(매매기준율) I/F 테이블 |
| [TI_GRPF912_CONV](/schemas/APPADAMSUSER/tables/TI_GRPF912_CONV.md) |  |  |
| [TI_GRPF918](/schemas/APPADAMSUSER/tables/TI_GRPF918.md) |  |  |
| [TI_GRPF919](/schemas/APPADAMSUSER/tables/TI_GRPF919.md) |  |  |
| [TI_GRPF920](/schemas/APPADAMSUSER/tables/TI_GRPF920.md) |  |  |
| [TI_MT_EXCHRATE](/schemas/APPADAMSUSER/tables/TI_MT_EXCHRATE.md) |  | => 조회 방법(통화,기준일자 입력) , (select kr_amt from TI_MT_EXCHRATE where std_dt = '기준일자' and curr_cd = '기준통화' ) as "기준일자환율"  , (SELECT round(F.KR_AMT * '기준금액',0) FROM TI_MT_EXCHRATE F WHERE F.STD_DT = '기준일자' AND F.CURR_CD = '기준통화' ) AS  "KRW금액" , (SELECT round(F.US_AMT * '기준금액',2) FROM TI_MT_EXCHRATE F WHERE F.STD_DT = '기준일자' AND F.CURR_CD = '기준통화' ) AS "USD금액" , (SELECT round(F.KR_AMT / G.KR_AMT * '기준금액',2)   FROM TI_MT_EXCHRATE F, TI_MT_EXCHRATE G   WHERE F.STD_DT = '기준일자' AND G.STD_DT = '기준일자' AND F.CURR_CD = '기준통화' AND G.CURR_CD = '변환대상통화' ) AS 변환금액 (이종통화 계산시) |
| [TI_MT_EXCHRATE_YM](/schemas/APPADAMSUSER/tables/TI_MT_EXCHRATE_YM.md) |  | 월단위 평균환율 계산(Avg 함수사용) |
| [TI_MT_EXCHRATE_YW](/schemas/APPADAMSUSER/tables/TI_MT_EXCHRATE_YW.md) |  | 월단위 평균환율 계산(Avg 함수사용) |
