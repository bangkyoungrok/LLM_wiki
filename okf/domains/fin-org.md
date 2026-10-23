---
type: Business Domain
title: 재무 기준정보(조직)
description: 재무 기준정보(조직). ERP 회사코드(TI_GRPF900)를 축으로 BA/코스트센터/Plant/MBO/영업·구매조직.
tags: ["domain:fin-org"]
system: 재무
domain_name: 기준정보(조직)
status: draft
sources:
- id: add-info
  resource: /references/domain-sources.md
  title: add_info/domain 이식
---

# 재무 / 기준정보(조직)

## 프로세스

N-ERP에서 조직정보는 관리 목적과 모듈에 따라 다음과 같이 구분되어 관리됩니다.
1. 재무 및 자금 관리 조직 (FI 모듈)
법인을 전사, 지역, 법인 등으로 계층 구조화하여 관리하며, 주요 관리 항목은 다음과 같습니다.

법인 조직정보(Company Hierarchy) 관리: 업무 단위별로 법인을 계층 구조로 관리합니다.
Company Group 등록: **ZVCFIBMBUKDTL(Register Company Group)**을 통해 등록합니다.
Hierarchy Version 등록: **ZVMFIBMBUKHVR(Define Version)**을 통해 등록합니다.
Company Hierarchy 등록: **ZLFIBMM00100(Register Company Hierarchy)**을 통해 계층 구조를 등록합니다.
비용 배부 조직: 배부된 G-ERP IT 비용을 청구하기 위해 Cost Center 단위로 조직정보를 관리하는 프로그램(ZLFIGIT00131(Register Charge Organization))이 있습니다.

2. 판매 및 영업 조직 (SD 모듈)
판매 주문(Sales Order) 생성 시 정확한 조직 할당을 위해 다음과 같은 조직 정보를 입력해야 합니다.
Sales Organization (판매 조직): 법인 내 주문을 담당하는 조직입니다.
Distribution Channel (유통 경로): B2C 또는 B2B 기준에 따른 유통 경로 정보입니다.
Division (제품군/디비전): 제품의 품목 또는 제품군을 나타냅니다.
Sales Area (판매 영역): 위 세 가지 요소(Sales Organization + Distribution Channel + Division)의 조합으로 구성됩니다.

3. 기준정보 및 마스터 조직 (MD 모듈)
물류 및 재무 프로세스 운영을 위한 공통 기준정보를 관리합니다.
Plant (플랜트): 제품을 생산하거나 재고를 보관하는 물리적/논리적 단위(공장, 센터 등)입니다.
Vendor(벤더) 관련 조직: 물류 0005 벤더의 경우, CIS System에서 업체 정보를 입력하면 N-ERP로 자동 인터페이스됩니다. 이때 N-ERP 내에 해당 조직(T* 시작 4자리 코드)이 정상 존재하면 물류비 정산용 구매 조직 마스터가 자동으로 생성됩니다.

**코스트센터(Cost Center, 원가 중심점)**는 비용이 발생하는 부서나 위치를 나타내는 관리 단위로, N-ERP 시스템의 여러 모듈에서 비용의 책임 소재를 명확히 하고 예산을 관리하기 위해 핵심적으로 사용됩니다.

1. 주요 정의 및 역할
비용 귀속 및 책임: 비용 전표를 생성할 때 비용이 어느 부서에서 발생했는지 기록하는 기본 단위입니다. 이를 통해 부서별 비용 발생 현황을 파악하고 책임 소재를 명확히 할 수 있습니다.
예산 관리: 부서의 예산 관리 및 운영을 위해 부여된 코드입니다.
직무코드(Job category Code)와의 관계: 효율적인 예산 관리를 위해 부서코드를 세분화한 것으로, 일반적으로 부서코드 뒤에 붙는 알파벳 3자리로 구성됩니다. (예: N-ERP 그룹 C10S4749 IGA의 경우 'IGA'가 직무코드)

2. 모듈별 활용 및 관리
1) FI (재무회계) 모듈
비용 전표 전기: FI 비용 전표를 생성할 때 비용 귀속 원가 관리 영역을 지정하기 위해 반드시 코스트센터를 지정해야 합니다.
기본 원가센터(Default Cost Center) 관리: 특정 G/L 계정(예: 운송 서비스 비용 등)에 대해 결산 시 자동으로 비용이 귀속될 대표 코스트센터를 할당하여 관리할 수 있습니다. (ZOKB9N(Display Default Cost Center) 활용)
전도금 및 지점 관리: 해외 지점의 전도처(Cost Center) 정보 및 계좌 정보를 관리하며, 사원마스터 상의 코스트센터를 기준으로 정보를 출력하거나 관리합니다. (ZLFIGBR00010(Manage Master of Advanced to BR) 활용)
비용 귀속부서 세팅: 해당 월의 비용이 귀속될 코스트센터를 확인하고, 이름, 파트너명, ID 및 관련 재무 속성(세금, 은행 등)을 관리합니다. (ZLFIGIT00131(Register Charge Organization) 활용)

2) SD (판매관리) 모듈
비용 귀속 우선순위: FOC(무상) 주문의 경우, 기본적으로 정의된 Profit Center별 코스트센터로 처리되지만, 주문 생성 시점에 비용 발생 주체의 코스트센터를 직접 입력하면 해당 코스트센터가 우선하여 인식됩니다.

3) CM (결재관리) 모듈
결재자 지정: 결재 프로세스에서 코스트센터에 해당하는 인사 부서의 부서장 코스트센터 코드를 관리자(Manager of Cost Center) 정보로 활용할 수 있습니다.

## 테이블과 조회 기준

조직 및 기준정보 대부분은 ERP 시스템 정보/체계를 기반으로 함
<회사코드> : TI_GRPF900
# ERP법인정보인 TI_GRPF900 테이블을 주로 사용.
     그외 TI_GRPF900_DAT, TI_GRPF900_MST, TI_GRPF900_SCM, TI_GRPF901, TI_GRPF908 테이블은
     타시스템(DART,SCM)에서 가져오거나, 특별한 기준을 참조하기 위한 부가 정보임
# ERP 회사코드는 법인을 의미하는 코드임.
# 국가, (로컬)통화, 상위 개념인 본사/자회사를 구분, 권역(지역), 유형(판매/생산/연구소/서비스 외), DX/DS법인구분, 사용여부 포함
* 법인코드 마스터 (ERP회사코드 + 추가정보) : TI_GRPF900
* DART 공시정보 종속회사 현황 : TI_GRPF900_DAT
* 법인명 수작업 매핑 : TI_GRPF900_MST
* G-SCM 시스템 법인(사이트) 정보 : TI_GRPF900_SCM
* ERP법인코드 vs 인사시스템(GHR) 법인 매핑정보(과거 법인정보) : TI_GRPF901
* DS법인코드 : TI_GRPF908

#회사코드 하위에는 ERP 모듈별로 BA, PLANT, MBO, 영업조직, 구매조직 등 이 있음
     FI(재무) : Business Area(사업영역) : TI_GRPF906
     MK(마케팅) : 마케팅 예산조직(MBO) : TI_GRPF913
     CO(관리)  : Cost Center(원가센터) : TI_GRPF904
     MM(자재) : Plant(플랜트) : TI_GRPF911
                    Purchasing Organization(구매조직) : TI_GRPF917
     SD(영업) : Sales Organization(영업조직) : TI_GRPF916
                   Division(사업부/제품군) : TI_GRPF910 공통코드 테이블 grpcd ='div_cd'

<BA : 사업영역> : TI_GRPF906
# ERP FI(재무) 모듈 Business Area(사업영역), 사업부(인사조직 구분)와 비슷한 개념 단위임(본사에 한함)
      단, 사업부와 1:1 매핑은 되지 않고 대표 매칭이 일부 가능함.
# 본사의 경우 기능별로 상세히 구분되어 있고,
     해외법인의 경우 HQ/플랜트(생산/판매/연구소) or 거점별로 주로 3~5개로 구분됨
* BA별 대금지급(AP) 정보(금액, 발생/종료일) : TI_GRPF906_TERM
* 사업부 BA 매핑정보(본사) : TI_GRPF907
* 사업부 BA 매핑정보 헤더(본사) : TI_GRPF907_MAP

<코스트센터 : Cost Center> : TI_GRPF904
# ERP CO(관리) 모듈 비용집계 단위, 부서(인사조직)와 비슷한 개념이나, 용도별로도 생성할 수 있음.
# 부서별 코스트센터는 정의되어 있으나, 코스트센터별 부서 매핑정보는 없음 (매칭건 외 이름/코드체계로 추정 매칭)
# 동의어 : 코스트센터, 비용센터, 부서, 비용부서, Cost Center
* 코스트센터 마스터 : TI_GRPF904
* 코스트센터 vs KNOX부서 수작업 매핑정보 : TI_GRPF904_MAP
* 코스트센터 Text정보(코스트센터 마스터 테이블의 코드/코드명 간략 정보) : TI_GRPF905

## 테이블 목록

| 테이블 | 유형 (table_type) | 설명 (table_rule) |
|---|---|---|
| [TI_GRPF900](/schemas/APPADAMSUSER/tables/TI_GRPF900.md) |  | 법인코드 마스터 => 주요컬럼 : 법인코드,국가,회사코드,권역(총괄),유형(판매/생산/연구소/서비스 법인), DS법인구분, 사용여부 등 * 사용여부(USE_YN='Y') : 현재기준 미사용이더라도, 과거데이터 조회 필요가 있는 경우 Y * 현재기준 사용여부(CUR_YN='Y) :  * 법인명 변경   스페인,포르투칼(SESA=>SEIB), 오스트리아,스위스(SEAG=>SEAS) => 조회방법(법인코드 입력)    , (select coknm from ti_grpf900 where cmcd = '법인코드')  as "회사명"    , (select cmnm from ti_grpf900 where cmcd = '법인코드')  as "법인명"    , (select divnm from ti_grpf900 where cmcd = '법인코드') as "권역" |
| [TI_GRPF900_DAT](/schemas/APPADAMSUSER/tables/TI_GRPF900_DAT.md) |  |  |
| [TI_GRPF900_MST](/schemas/APPADAMSUSER/tables/TI_GRPF900_MST.md) |  |  |
| [TI_GRPF900_SCM](/schemas/APPADAMSUSER/tables/TI_GRPF900_SCM.md) |  | G-SCM 법인(사이트) 정보, G-SCM에서만 사용하는 V% 코드도 있음(법인이 없는 지점 포함) |
| [TI_GRPF901](/schemas/APPADAMSUSER/tables/TI_GRPF901.md) |  |  |
| [TI_GRPF904](/schemas/APPADAMSUSER/tables/TI_GRPF904.md) |  | => 조회 방법(코드,기준일자 입력)    (select category from ti_grpf904 where kostl = '코스트센터코드'    and end_dt  = ( select min(end_dt) from ti_grpf904 where kostl = '코스트센터코드' and end_dt >= '기준일자' ) and rownum=1)  as   "발생부서 카테고리" |
| [TI_GRPF904_MAP](/schemas/APPADAMSUSER/tables/TI_GRPF904_MAP.md) |  |   |
| [TI_GRPF905](/schemas/APPADAMSUSER/tables/TI_GRPF905.md) |  | 코스트센터 코드/코드명정보(유효기간별)  => 코스트센터명은 조직변경/관리변경에 따라 계속 이름이 변경될 수 잇음 => 동일 코스트센터에 대한 최종 유효기간 선택필요 |
| [TI_GRPF906](/schemas/APPADAMSUSER/tables/TI_GRPF906.md) |  | => 주요컬럼 : BA/BA명, 유효기간, 사용여부, DX/DS구분  => 조회방법(코드 입력)     , (select replace(ba_nm,'[Inactive]','') from ti_grpf906 where ba = 'BA코드') as "BA명" |
| [TI_GRPF906_TERM](/schemas/APPADAMSUSER/tables/TI_GRPF906_TERM.md) |  |  |
| [TI_GRPF907](/schemas/APPADAMSUSER/tables/TI_GRPF907.md) |  | 사업부 : 인사조직구분 vs BA : ERP재무 조직 구분 매핑 (C100 본사만 해당) => 둘 사이에 조인 관계 구성  => AP내역에서 사업부 BA를 가져옮      한 BA가 여러 개의 사업부로 연결될 수 있음(업무별 특성에 따라)      BA_YN ='Y' 으로 BA 한개에 대표 사업부 1개로 설정 후  => 사업부 : BA = 1 : N |
| [TI_GRPF907_MAP](/schemas/APPADAMSUSER/tables/TI_GRPF907_MAP.md) |  |  |
| [TI_GRPF908](/schemas/APPADAMSUSER/tables/TI_GRPF908.md) |  | DS 조직정보(from 회사코드,법인코드,BA,MBO,PLANT,영업조직,사이트코드 등) : DS에 해당되는 조직 전체 |
| [TI_GRPF911](/schemas/APPADAMSUSER/tables/TI_GRPF911.md) |  | => 조회방법(코드 입력)    , (select replace(NM,'[Inactive]','') from TI_GRPF911 where PLANT = 'PLANT코드') as "플랜트명" |
| [TI_GRPF913](/schemas/APPADAMSUSER/tables/TI_GRPF913.md) |  | 마케팅 예산조직(주로 마케팅비에서만 사용) |
| [TI_GRPF914](/schemas/APPADAMSUSER/tables/TI_GRPF914.md) |  | BQMS 사이트코드(조직) |
| [TI_GRPF916](/schemas/APPADAMSUSER/tables/TI_GRPF916.md) |  | 영업조직 |
| [TI_GRPF917](/schemas/APPADAMSUSER/tables/TI_GRPF917.md) |  | 구매조직 |
