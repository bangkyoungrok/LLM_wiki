---
type: Business Domain
title: BQMS MRO
description: BQMS MRO. MRO몰, MRO카테고리, MRO 미연계(공급사) 데이터.
tags: ["domain:mro"]
system: BQMS
domain_name: MRO
status: draft
sources:
- id: add-info
  resource: /references/domain-sources.md
  title: add_info/domain 이식
---

# BQMS / MRO

## 프로세스

# MRO는 MRO몰 데이터, MRO카테고리 데이터, MRO 미연계 수동 입수 데이터로 구분되며,
MRO미연계 데이터에는 구매대행사 정보 뿐만 아니라 실제 공급 업체 정보가 포함되어있음.

## 테이블과 조회 기준

* MRO몰 테이블 : TI_BQMS009_MROMALL_IF
* MRO구매 내역 테이블 : TI_BQMS009_MRO_PR_PO_GR
* MRO공급사(미연계) 테이블 : TI_BQMS078_MRO_PO_SUPPLIER
* MRO 아이템 단가 테이블 : TI_BQMS023_MRO_VE_UNIT

## 테이블 목록

| 테이블 | 유형 (table_type) | 설명 (table_rule) |
|---|---|---|
| [TI_BQMS009_MROMALL_IF](/schemas/APPADAMSUSER/tables/TI_BQMS009_MROMALL_IF.md) |  | MRO몰에 구매 내역에 대한 PR/PO/GR 테이블 |
| [TI_BQMS009_MRO_PR_PO_GR](/schemas/APPADAMSUSER/tables/TI_BQMS009_MRO_PR_PO_GR.md) |  | MRO몰+MRO카테고리 전체 구매내역에 대한 PR/PO/GR 테이블 |
| [TI_BQMS009_MRO_PR_PO_GR_IF](/schemas/APPADAMSUSER/tables/TI_BQMS009_MRO_PR_PO_GR_IF.md) |  | TI_BQMS009_MRO_PR_PO_GR 테이블 연계를 위한 I/F전용 테이블 |
| [TI_BQMS023_MRO_VE_UNIT](/schemas/APPADAMSUSER/tables/TI_BQMS023_MRO_VE_UNIT.md) |  | 사이트, 벤더 별로 등록한 아이템 단가 정보 누적 데이터 테이블 |
| [TI_BQMS077_MRO_PE_DATA](/schemas/APPADAMSUSER/tables/TI_BQMS077_MRO_PE_DATA.md) |  | MRO 구매 지급내역 테이블 |
| [TI_BQMS078_MRO_PO_SUPPLIER](/schemas/APPADAMSUSER/tables/TI_BQMS078_MRO_PO_SUPPLIER.md) |  | MRO 미연계 데이터로 대행사 정보 외에 실제 공급사 정보를 포함하는 테이블 |
