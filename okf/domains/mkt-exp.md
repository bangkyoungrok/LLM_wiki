---
type: Business Domain
title: 영업마케팅 마케팅비
description: 영업마케팅 마케팅비. 계획>캠페인>PP>EO>PR>충당>정산. 핵심 TI_GRPF_EO_REPORT, 조회 기준 PRCRDT·EO/PR상태·MBO.
tags: ["domain:mkt-exp"]
system: 영업마케팅
domain_name: 마케팅비
status: draft
sources:
- id: add-info
  resource: /references/domain-sources.md
  title: add_info/domain 이식
---

# 영업마케팅 / 마케팅비

## 프로세스

마케팅비 프로세스는 크게 마케팅 계획(경영계획/실행계획), 마케팅 집행(캠페인/품의), **마케팅 결과(지급/충당)**의 단계로 구분됩니다.

주요 단계별 상세 비즈니스 프로세스는 다음과 같습니다.

1. 마케팅 계획 수립

경영계획: 차년도 마케팅 활동을 위한 비용 계획을 수립하고 예산을 확정하는 단계입니다. 확정된 데이터는 차년도 Campaign 생성의 기초가 됩니다.
실행계획: 미래 3개월 또는 그 이상의 기간에 대한 비용 계획을 수립합니다. 또한, 결산 전 당월 마케팅 비용을 예측하는 속보 프로세스가 포함됩니다.
예산 관리: 사업부 및 GMC의 예산을 지역(지점, 마케팅 법인)에 캠페인 형태로 배분하여 관리합니다.

2. 마케팅 집행 및 관리

Campaign (캠페인): 연간 마케팅 활동을 위해 예산을 편성하고 계획을 확정하는 단위입니다. 경영계획을 바탕으로 생성하거나 필요 시 Ad-hoc 캠페인을 추가로 생성할 수 있습니다.
Plan Proposal (PP, 기본 품의): 마케팅 활동 집행을 위한 최초 단계로, 캠페인을 참조하여 예산 범위 내에서 일정, TIM Activity, 월별 비용 등을 입력합니다. 입력된 정보는 BQMS를 통한 업체 선정 및 계약의 근거가 됩니다.
Execution Order (EO, 실행 품의): 수립된 계획(PP)에 대해 실제 활동을 실행하기 위한 단계입니다. BQMS를 통해 업체가 선정되고 구매오더(PO)가 생성되면 EO가 자동 생성되기도 합니다.

3. 마케팅 결과 처리 및 결산

Payment Request (PR, 지급 요청): 마케팅 활동을 수행한 업체로부터 Invoice를 받은 후, 비용 및 세금 기표와 선급비용 처리를 수행하는 단계입니다.
충당 (Accrual): 활동은 완료되었으나 아직 Invoice를 받지 못한 경우, 객관적 증빙(행사완료 보고서 등)을 바탕으로 미지급 비용을 결산에 미리 반영하는 절차입니다.
대행사 선지급 (Reconciliation): 매체비 등에 대해 대행사에게 증빙 없이 선지급이 필요한 경우, BQMS의 Reconciliation 프로세스를 통해 선지급 후 사후 정산을 진행할 수 있으며, 관련 정보는 N-ERP의 EO와 PR에 인터페이스되어 관리됩니다.

마케팅비 프로세스에서 Accrual은 예산 할당이 아닌 충당을 의미합니다.
**Accrual(충당)**의 정의와 상세 내용은 다음과 같습니다.
1. 정의 및 목적

마케팅 활동은 완료되었으나, 업체로부터 아직 Invoice(송장)를 받지 못해 비용 처리가 지연될 경우에 수행합니다.
발생주의 회계 원칙에 따라, 객관적인 증빙(행사완료 보고서, 진행 보고서, 영수증 등)을 기반으로 미지급 비용을 결산에 미리 반영하는 절차입니다.

2. 주요 프로세스 및 특징

결산 단계: 결산 프로세스 중 비용 마감 단계에서 진행되며, 진행 중인 Execution Order(EO)와 Payment Request(PR)가 완료된 후 수행합니다.
데이터 산출 로직: 당월 충당 대상 금액은 **'전월 EO 잔액 + 당월 EO 금액 – 당월 PR 금액'**으로 계산됩니다.
전표 처리: 전월 충당 금액을 Negative(역기표) 처리한 후 당월 충당을 진행하며, Negative 충당 전표는 전월 충당 전표를 Reverse하는 형태로 생성되어 두 전표는 Clearing(청산) 대상이 됩니다.
제어: 추가적인 마케팅 문서가 생성되지 않도록 EO와 PR을 Block(차단)하여 비용 마감을 진행합니다.

마케팅비 프로세스에서 Reconciliation(사후 정산)은 BQMS와 N-ERP 시스템의 연계를 통해 진행되며, 구체적인 방법은 다음과 같습니다.
1. 선지급 프로세스 (BQMS 연계)
매체비 등 증빙 없이 대행사에게 선지급이 필요한 경우, BQMS Process에서 Reconciliation을 선택하여 선지급을 먼저 진행한 후 사후 정산을 수행합니다.

BQMS에서 벤더 선택, 발주, 납기 확인, 청구서 수령 등의 사전 절차를 거칩니다.
이 Reconciliation 정보는 N-ERP의 EO(실행 품의) 및 **PR(지급 요청)**로 인터페이스되어 관리됩니다.
EO�� Header 내 Additional Data Tab에서 Reconciliation 상태와 금액을 조회할 수 있습니다.
PR의 Header 내 BQMS Tab에서 Reconciliation 상태와 금액을 확인할 수 있습니다. (아래 이미지 1 참조)

2. 정산 현황 모니터링 및 관리
선지급한 금액과 실제 수행된 Activity 금액을 비교하여 적절하게 후정산이 이루어지는지 아래 프로그램을 통해 관리합니다.
ZRMK400110(Reconciliation Monitoring Report)
Reconciliation 대상인 EO에 대해 업체에 선지급한 금액과 실제 수행한 Activity 금액을 확인하고 관리할 수 있습니다.
Reconciled AMT 항목에서 회입(환입) 대상 금액을 확인합니다.
선지급한 비용 중 환급받아야 하는 경우에는 AMT to be Refunded 항목을 통해 확인합니다.

## 테이블과 조회 기준

프로세스 : 계획수립 > 캠페인 > PP > EO > PR > 충당 > 정산

마케팅비 핵심 테이블 : TI_GRPF_EO_REPORT
# 데이터 구조 : EO정보 + PR정보(아이템 단위)
# 별도 요청이 없으면 주로 정산(PR)내역 조회
# 기준 조건
    . 기간 : PR기표일(BUDAT) 대신 주로 PR생성일(PRCRDT) 기준으로 조회함
    . 상태 : EO상태(AF : Closed, AC : Completed) & PR상태(AC : Completed, AG : Reversed)
    . 조직 : 마케팅 예산조직(MBO)
* I/F테이블 : TI_GRPF039
* 정산(아이템레벨) : TI_GRPF_EO_REPORT
* 충당(아이템레벨) : TI_GRPF_EO_ACC

<집계>
* 정산(EO기준) : TI_GRPF860
* 정산(EO기준 합계) : TI_GRPF861
* 거래선(벤더)별 집계(법인/월별)(from TI_GRPF039) : TI_GRPB_DE_MKT_VENDOR_YM
* 거래선(벤더)별 집계(법인/월별)(from ERP) : TI_GRPF033
# ERP에서 집계되어 온 내역 보다는 기준 테이블로 집계한 내역을 사용함

<특화용도>
* BQMS에서 NO REASON 유형으로 나간 EO정보 : TI_GRPF_EO_NO_REASON
* BQMS NO REASON 코드 마스터 : TI_GRPF_EO_NO_REASON_MASTER
* 마케팅비 벤더 리스트 : TI_GRPB_DE_MKT_VENDER

## 테이블 목록

| 테이블 | 유형 (table_type) | 설명 (table_rule) |
|---|---|---|
| [TI_GRPB_DE_MKT_VENDER](/schemas/APPADAMSUSER/tables/TI_GRPB_DE_MKT_VENDER.md) |  | 마케팅비 벤더 리스트  => 단순히 마케팅비가 누적으로 한번이라도 나간 벤더코드 리스트  => 벤더마스터에서 별도로 마케팅 벤더라고 유형을 지정하지 않음  => 일부 시나리에서 해당조건 체크하기 위함 |
| [TI_GRPB_DE_MKT_VENDOR_YM](/schemas/APPADAMSUSER/tables/TI_GRPB_DE_MKT_VENDOR_YM.md) |  | 마케팅비 벤더별 월별/법인별 정산(PR)금액 집계내역 (일부 시나리에서 해당조건 체크하기 위함) |
| [TI_GRPF009](/schemas/APPADAMSUSER/tables/TI_GRPF009.md) |  | 마케팅비 정산 지연된 내역(from ERP) |
| [TI_GRPF033](/schemas/APPADAMSUSER/tables/TI_GRPF033.md) |  | 마케팅비 법인/거래선별 월별 집계내역(from ERP) |
| [TI_GRPF039](/schemas/APPADAMSUSER/tables/TI_GRPF039.md) |  | ERP 마케팅비 I/F 테이블(from ERP) |
| [TI_GRPF860](/schemas/APPADAMSUSER/tables/TI_GRPF860.md) |  | 마케팅비 정산 헤더(PR) 기준 요약내역 => EO정보(EO번호+아이템) + 정산정보(PR 번호+아이템) |
| [TI_GRPF861](/schemas/APPADAMSUSER/tables/TI_GRPF861.md) |  | 마케팅비 EO기준 합계금액 집계(from TI_GRPF860 테이블 참조) => EO정보(EO번호+아이템) + 금액집계정보 |
| [TI_GRPF_EO_ACC](/schemas/APPADAMSUSER/tables/TI_GRPF_EO_ACC.md) |  | 마케팅비 충당 아이템 기준 상세내역 => EO정보(EO번호+아이템) + 충당정보(충당번호 +아이템) |
| [TI_GRPF_EO_INFO](/schemas/APPADAMSUSER/tables/TI_GRPF_EO_INFO.md) |  | ERP 마케팅비 리포트(TI_GRPF_EO_INFO_REPORT)에서 EO번호 기준 최초금액 표시 |
| [TI_GRPF_EO_INFO_REPORT](/schemas/APPADAMSUSER/tables/TI_GRPF_EO_INFO_REPORT.md) |  | ERP 마케팅비 리포트(from ERP) |
| [TI_GRPF_EO_NO_REASON](/schemas/APPADAMSUSER/tables/TI_GRPF_EO_NO_REASON.md) |  | BQMS에서 NO REASON 유형으로 나간 EO정보(일부 시나리오에서 해당조건 체크하기 위함) |
| [TI_GRPF_EO_NO_REASON_MASTER](/schemas/APPADAMSUSER/tables/TI_GRPF_EO_NO_REASON_MASTER.md) |  | BQMS NO REASON 코드 마스터 |
| [TI_GRPF_EO_REPORT](/schemas/APPADAMSUSER/tables/TI_GRPF_EO_REPORT.md) |  | 마케팅비 정산 아이템 기준 상세내역(충당 헤더 정보 포함) => EO정보(EO번호+아이템) + 정산정보(PR 번호+아이템) |
