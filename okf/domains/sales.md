---
type: Business Domain
title: 영업마케팅 매출
description: 영업마케팅 매출. SO>DO>GI>빌링/Invoice>수금. 핵심 TI_GRPB004B(빌링), 판가 TI_GRPB_PRICE_CONDITION.
tags: ["domain:sales"]
system: 영업마케팅
domain_name: 매출
status: draft
sources:
- id: add-info
  resource: /references/domain-sources.md
  title: add_info/domain 이식
---

# 영업마케팅 / 매출

## 프로세스

N-ERP의 주문 및 매출 프로세스는 크게 일반 주문, 예외 주문, 그리고 프로젝트(PJT) 판매로 구분됩니다.
1. 일반 주문 및 매출 프로세스 (SD 모듈)
일반적인 판매 프로세스는 고객의 주문부터 대금 청구까지 순차적인 단계를 거칩니다.

주문 생성 (Sales Order): 고객의 주문을 바탕으로 **Sales Order(S/O)**를 생성합니다. 이 단계에서는 고객 정보(Sold-To Party, Ship-To Party), 납기 일자, 주문 사유 등을 입력하며, 가용성 점검(ATP Check)과 신용 점검(Credit Check)을 통해 주문의 유효성을 검증합니다. (아래 이미지 1 참조), (아래 이미지 2 참조)
납품 및 출고 (Delivery & Goods Issue): 생성된 S/O를 기준으로 창고에 제품 출고를 지시하는 **Delivery Order(D/O)**를 생성합니다. 이후 실제로 제품이 창고에서 반출되어 재고가 감소하는 Goods Issue(G/I) 단계가 진행됩니다.
적송 대상: 창고 출시 시 1차 G/I가 발생하며, 배송 완료 후 배송업체의 e-POD 입력에 따라 2차 G/I가 진행됩니다. (아래 이미지 3 참조)
Intercompany(법인간 거래): 물류/생산법인의 G/I 이후에 매출 처리가 진행됩니다.
매출 청구 (Billing): 출고가 완료된 후 고객에게 대금을 청구하기 위해 Billing 문서를 생성합니다. 생성 시점에 FI 모듈로 매출 및 채권 데이터가 자동 전기됩니다.
YPO2(SolutionBilling): 청구 항목을 생성하고 수정(Customer/Material AAG, Tax Classification 등)할 수 있으며, [Save] 버튼을 통해 주문 구성 정보로 Billing을 생성합니다.

2. 예외 주문 및 매출 조정 프로세스
판가 변화나 수량 차이 등으로 인해 이미 완료된 매출을 수정해야 하는 경우 다음과 같은 프로세스를 사용합니다.

매출 조정 (Credit/Debit Memo): Billing 처리 이후 판가 변화나 수량 차이를 반영하기 위해 Credit Memo(대변 메모) 또는 Debit Memo(차변 메모) 조정 주문을 통해 매출을 조정합니다.
서비스 자재 반품: ASC 거래선으로부터 반품 요청이 접수되면 이를 승인하고 제품을 회수하여 Credit을 차감하는 프로세스를 진행합니다.

3. 프로젝트(PJT) 판매 프로세스
프로젝트 비즈니스는 일반 주문과 달리 계약과 실제 매출 인식 단계가 구분됩니다.

계약 기반 관리: **Contract(계약)**를 기반으로 계산서를 관리하며, 실제 매출 인식은 Solution order를 통해 진행합니다.
매출 인식: 계약에 따른 선급금, 중도금, 잔금에 대해 V.C Billing Plan을 등록하여 계약일에 Billing 처리 및 Invoice를 발행합니다. 프로젝트 종료 시점에 계산서 가계정과 매출 가계정을 소거합니다.

N-ERP의 매출(Billing) 프로세스는 크게 일반 매출, 진행도 매출, 그리고 매출 조정의 세 가지 유형으로 구분됩니다.

1. 매출 유형별 프로세스

일반 매출
거래선에 판매 주문(Sales Order)을 생성하고, 제품을 배송(Delivery)한 후 최종적으로 대금 지불을 요청하는 프로세스입니다.
거래선의 출고 내역을 기준으로 매출 채권을 발생시키거나 취소하는 대금 청구 과정을 포함합니다.
Intercompany(법인간 거래)의 경우, 물류/생산법인의 출고(G/I) 이후에 매출 처리가 진행됩니다.
진행도 매출 (프로젝트 Biz)
프로젝트 비즈니스는 계산서 금액과 실제 매출 금액이 일치하지 않는 특성이 있습니다.
따라서 계산서는 **Contract(계약)**를 기반으로 진행하며, 실제 매출 인식은 Solution order를 통해 진행합니다.
프로젝트 종료 시점에 계산서 가계정과 매출 가계정을 소거하는 과정을 거칩니다.
계약에 따른 선급금, 중도금, 잔금에 대해서는 V.C Billing Plan을 등록하여 계약일에 Billing 처리 및 Invoice를 발행합니다.
매출 조정
Billing 처리 완료 후, 판가 변화나 수량 차이 등으로 인해 매출 금액을 수정해야 할 때 사용하는 프로세스입니다.
CR/DR Adjust: 판가 변화나 수량 차이에 의한 조정입니다.
매출 차감: 가격 결정 이후 거래선과 합의하여 판매 확대 및 시장 대응을 위해 사후에 지불하는 비용(Rebate, Sales Allowance 등)을 처리합니다.
Re-Invoice: 법적으로 Billing 취소가 불가능한 법인에서 매출을 취소한 후 다시 인보이스를 발행하는 방식입니다.

2. 주요 청구(Billing) 처리 방식

VF01(Billing 건별 진행): 특정 판매 주문 또는 배송 주문 번호를 바탕으로 개별적으로 청구 문서를 생성합니다.
VF06(Billing 자동 진행): 일정 주기를 설정하여 백그라운드에서 Billing 문서를 자동으로 생성하는 배치(Batch) 작업 방식입니다.

판가 관리(Pricing Management) 프로세스는 제품의 기준 판가를 설정하고, 변경 사항을 시뮬레이션하여 검증한 후, 최종적으로 시스템에 반영하는 과정을 의미합니다.
주요 단계와 상세 내용은 다음과 같습니다.
1. 판가 설정 및 준비

기준 판가 설정: 오버헤더 및 원가를 참고하여 제품의 기준 판가를 설정합니다.
사전 정보 확인: 판가를 설정하기 전, **ZRSDB64660(RRP 변경 내용 확인)**을 통해 RRP(권장소비자가) 변경 내용을 확인하거나, **ZRSDB60000(Condition 및 Table별 설정 값 확인)**을 통해 기존에 설정된 판가 정보를 확인합니다.

2. 판가 품의 및 시뮬레이션
신규 판가를 등록할 때는 반드시 시뮬레이션 절차를 거쳐야 하며, 주문 생성 시 시뮬레이션 기준 판가와 비교하는 체크 로직이 운영됩니다.

판가 품의 수행: ZFLSDB82010(RRP, Dealer Margin 판가 설정) 프로그램을 통해 판가 품의를 진행합니다. 품의 화면은 기존 품의 조회, 신규 품의 생성, Item 상세 정보 입력의 3개 화면으로 구성됩니다.
시뮬레이션(Simulation): 판가 주요 정보나 Condition 입력 화면에서 Simulation 버튼을 클릭하여 수행합니다.
시뮬레이션을 통해 변경된 Invoice Price(송장 금액) 등을 확인합니다.
FIORI - Pricing Simulation을 통해 조회할 수 있으며, 시뮬레이션 결과로 Old/New Invoice, 장려금, CGS 등의 정보를 확인할 수 있습니다. (아래 이미지 1 참조)
시뮬레이션 결과 앞단의 버튼을 클릭하면 해당 Invoice Price에 대한 상세 내용을 팝업으로 확인할 수 있습니다.
판가 적용 확인: 시뮬레이션 결과를 바탕으로 **ZLSDB00120(판가 일괄 확인)**을 통해 판가가 적절히 적용되었는지 확인합니다.

3. 승인 및 시스템 반영 (Workflow)

최종 품의 생성: 시뮬레이션으로 변경된 Invoice Price를 확인한 후 최종 판가 품의 생성을 요청합니다.
결재 진행: 시뮬레이션 결과가 맞으면 변경된 판가 혹은 Condition에 대해 일괄 워크플로우(Work-Flow)를 진행합니다.
승인 제목, 담당자, 승인 유형(Approval/Consent/Notification) 등을 입력하여 승인 프로세스를 초기화합니다. (아래 이미지 2 참조)
Knox 메일 또는 Portal 내 결재 모듈 중 어느 시스템에서 결재를 진행할지 선택하여 제출합니다.
시스템 반영: 결재가 완료되면 변경된 판가가 시스템에 최종 반영됩니다.

## 테이블과 조회 기준

프로세스 : 주문(SO) > 납품(DO) > 출고(GI) > 청구 및 매출인식(빌링/Invoice) > 수금
빌링(판매주문) : TI_GRPB004B
# 데이터 구조 : 빌링 Item정보 + SO정보(Header) + DO기본정보
    (인덱스 : 빌링번호 + Item번호)
# 기준조건 : 빌링일자(BILL_DT)
# 주문정보를 별도로 I/F 받고 있지 않고, 빌링정보에 주문기본정보를 포함해서 받음
# 동의어 : 매출, 판매액, 빌링, 청구금액
# 빌링금액(Gross Value) = 공급가(원가+제조사마진)(Net Value) + VAT 로 되어있음
     (따라서 FOC 무상공급도 VAT금액이 포함되어 금액이 존재함)
# 내부실적기준에 사용되는 Net Value 계산을 위해서는 VAT액을 제외해야함. (VAT금액은 26년이후부터 별도컬럼에 I/F 받음)
# 반품빌링의 경우 원빌링정보가 별도로 있음
* 빌링마스터 테이블(빌링/아이템번호 키값) : TI_GRPB004B
* 빌링 I/F 테이블 : TI_GRPB004N
* 빌링매핑정보 : TI_GRPB004B_MAP
  . 법인, 빌링,SO,DO 번호/아이템,빌링일자,Material 컬럼만 구성, 각 항목별 인덱스 구성
  . SO/DO번호로 빌링을 조회할 때 사용, TI_GRPB004B 직접 조회시 속도느림

<집계>
* 빌링집계 (주요 항목기준 월별 빌링수량,금액 집계) : TI_GRPB004B_GRP
* 거래선 월별 거래실적(from TI_GRPF035) : TI_GRPB812
* 거래선 년도별 거래실적(from TI_GRPF035) : TI_GRPB813
* 거래선 거래규모(매출) (from ERP집계) : TI_GRPF035
* 거래선 판매내역(from ERP집계) : TI_GRPF041
# ERP에서 집계하여 I/F 받은 내역보다는 기준 테이블(TI_GRPB004B)로 집계한 내역을 사용함

<판가> : TI_GRPB_PRICE_CONDITION
# 판가 컨디션(Header + Item) 등록(결재) 내역
# 월/수시 Invoice 판매가격 설정, 신규 판가 등록시 시뮬레이션(Simulation) 기준 판가와 비교 체크 
프로세스 : RRP(권장소비자가)확인 > 기존판가정보(컨디션,테이블설정값 등) 확인 > 판가품의생성 > 판가시뮬레이션 > 결재 > 반영
# 판가 테이블은 수작업 I/F 로 데이터 업데이트 안되고 있음

* 판가 컨디션 헤더 정보 : TI_GRPB_PRICE_HEADER
* 판가 컨디션 아이템 정보 : TI_GRPB_PRICE_ITEM
* 판가 컨디션 헤더+아이템 정보(결합) : TI_GRPB_PRICE_CONDITION

## 테이블 목록

| 테이블 | 유형 (table_type) | 설명 (table_rule) |
|---|---|---|
| [TI_FMLY001](/schemas/APPADAMSUSER/tables/TI_FMLY001.md) |  | 전자 임직원 복지몰 판매내역 |
| [TI_GRPB001](/schemas/APPADAMSUSER/tables/TI_GRPB001.md) |  |  |
| [TI_GRPB002](/schemas/APPADAMSUSER/tables/TI_GRPB002.md) |  | Batch User제외하고 주문, DO, 빌링생성자가 각각 하나라도 동일한 내역 |
| [TI_GRPB003](/schemas/APPADAMSUSER/tables/TI_GRPB003.md) |  | 무상오더 출고내역  * FOC Order 데이터 추출 (YF01 - FOC Without Tax, YFT1 - FOC With Tax, YH01 - In-house Sales) |
| [TI_GRPB004B](/schemas/APPADAMSUSER/tables/TI_GRPB004B.md) |  | 빌링 아이템 기준 상세내역 => 빌링 Item정보 + SO정보(Header) + DO기본정보 |
| [TI_GRPB004B_GRP](/schemas/APPADAMSUSER/tables/TI_GRPB004B_GRP.md) |  | 빌링 법인/영업조직/BA/DIVISION/유통채널/거래선 월별 빌링수,금액(USD) 집계 |
| [TI_GRPB004B_MAP](/schemas/APPADAMSUSER/tables/TI_GRPB004B_MAP.md) |  | 법인/빌링번호/빌링아이템/빌링일자/Material/SO번호/SO아이템/DO번호/DO아이템 매핑 |
| [TI_GRPB004N](/schemas/APPADAMSUSER/tables/TI_GRPB004N.md) |  | ERP 빌링 I/F 테이블(from ERP) |
| [TI_GRPB010](/schemas/APPADAMSUSER/tables/TI_GRPB010.md) |  | 법인/영업조직/Material Group 별 매출 |
| TI_GRPB012 (접근 범위 밖) |  | B2B주문중에서 Serial No. 있는 것만 내부거래 제외, Distribution Channel이 B2B(11, 21) SO 배송지와 DO 배송지가 다른 건만(제거) B2B 판매제품의 S/N과 서비스로 접수된 S/N를 비교하여 일치되는 건을 추출 |
| [TI_GRPB013](/schemas/APPADAMSUSER/tables/TI_GRPB013.md) |  | 반품/출하 DO의 S/N 단위로 데이터를 추출 < 해외 판매법인의 경우 >  G/I  serial no. 관리  ZTLEZ59011-SERNR (SET 등) ZTLEZ59021-SERNR (HDD/OMS 등) ZTLEZ59031-SERNR (HHP등)  반품 serial no. 관리 ZTSDX61030-SERIALNO (반품 require ) ZTCSF00003-SERIALNO (반품 inspection )  < 한국총괄의 경우 >  인도(설치) 시 : ZTLEK50780-PRONO   반품 시 : ZTLEL50020-SERNO ( 착하불량만 관리, 나머지 인수거부등은 serial 관리 안 됨) 무선제품은 S/N 관리 안함. 정합성은 법인마다 다르며, 확인필요 |
| [TI_GRPB015](/schemas/APPADAMSUSER/tables/TI_GRPB015.md) |  | 주문타입(Order Type) : YS02(Bundle with FOC item) 빌링 추출 |
| [TI_GRPB017](/schemas/APPADAMSUSER/tables/TI_GRPB017.md) |  | 샘플 시스템에서 출고된 무상샘플中 회수여부가 "N"인 件 추출 |
| [TI_GRPB022](/schemas/APPADAMSUSER/tables/TI_GRPB022.md) |  | 최근 3개월간 해외판매법인내 빌링내역中 거래선별 2개 이상 Customer Group이 적용된 거래선의 최근 3개월간 모든 빌링내역 추출 ※ 주문 Type : Normal(YN01), 유통경로 : B2C(10, 20) |
| [TI_GRPB812](/schemas/APPADAMSUSER/tables/TI_GRPB812.md) |  | 거래선 년도별/월별 거래실적(거래선별 년도별 월을 가로로 표시) |
| [TI_GRPB813](/schemas/APPADAMSUSER/tables/TI_GRPB813.md) |  | 거래선 년도별 거래실적(거래선별 년도를 가로로 표시) |
| [TI_GRPB_PRICE_BILLING_AVG1](/schemas/APPADAMSUSER/tables/TI_GRPB_PRICE_BILLING_AVG1.md) |  | 과거 VAT제외한 금액으로 판가 계산하기 위해 수작업으로 받은 데이터로 집계한 자료(미사용) |
| [TI_GRPB_PRICE_BILLING_AVG2](/schemas/APPADAMSUSER/tables/TI_GRPB_PRICE_BILLING_AVG2.md) |  | 과거 VAT제외한 금액으로 판가 계산하기 위해 수작업으로 받은 데이터로 집계한 자료(미사용) |
| [TI_GRPB_PRICE_BILLING_REPORT](/schemas/APPADAMSUSER/tables/TI_GRPB_PRICE_BILLING_REPORT.md) |  | 과거 VAT제외한 금액으로 판가 계산하기 위해 수작업으로 받은 데이터로 집계한 자료(미사용) |
| [TI_GRPB_PRICE_CONDITION](/schemas/APPADAMSUSER/tables/TI_GRPB_PRICE_CONDITION.md) |  | 판가 컨디션 헤더(TI_GRPB_PRICE_HEADER) + 아이템(TI_GRPB_PRICE_ITEM) 테이블 조인 |
| [TI_GRPB_PRICE_HEADER](/schemas/APPADAMSUSER/tables/TI_GRPB_PRICE_HEADER.md) |  | 판가 컨디션 헤더 정보 |
| [TI_GRPB_PRICE_ITEM](/schemas/APPADAMSUSER/tables/TI_GRPB_PRICE_ITEM.md) |  | 판가 컨디션 아이템 정보 |
| [TI_GRPF015](/schemas/APPADAMSUSER/tables/TI_GRPF015.md) |  | 1. 거래선 Credit Limit 변경횟수가 年 10回 이상이고 한도가 20億원 이상인 거래선 (생성 기준으로, 결산월기준으로 환산, 거래선으로 유효한도 합산금액) 2. 결산월 기준 91日 이상의 악성 부실채권잔액이 있는 거래선 3. 결산월에 발생한 여신변경 건 |
| [TI_GRPF028](/schemas/APPADAMSUSER/tables/TI_GRPF028.md) |  | 1. 결산월에 생성된 건 2. 年間 특별한도 부여 총액이 5億원 이상이고 특별한도 부여횟수가 5回 이상인 件 (년간 총 발생건으로 합계, 유효여부 상관없이, Reverse 포함) |
| [TI_GRPF032](/schemas/APPADAMSUSER/tables/TI_GRPF032.md) |  | 법인별, 거래선별 결산월에 대한 Base Margin, Contract Margin, Special Margin, Additional Margin금액을 집계 |
| [TI_GRPF035](/schemas/APPADAMSUSER/tables/TI_GRPF035.md) |  | 거래선 월별 매출실적 |
| [TI_GRPF041](/schemas/APPADAMSUSER/tables/TI_GRPF041.md) |  | 거래선 월별/유통채널/DIVISON/주문타입별 판매수량,금액 |
| [TI_GRPF053](/schemas/APPADAMSUSER/tables/TI_GRPF053.md) |  | 수작업(manual)으로 AR(매출채권) 기표한 내역 |
| [TI_GRPI001](/schemas/APPADAMSUSER/tables/TI_GRPI001.md) |  |  |
