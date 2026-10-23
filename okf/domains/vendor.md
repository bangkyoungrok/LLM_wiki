---
type: Business Domain
title: BQMS 업체정보
description: BQMS 업체정보. BQMS 벤더마스터+구매 벤더마스터 결합 마스터(TI_BQMS800) 중심.
tags: ["domain:vendor"]
system: BQMS
domain_name: 업체정보
status: draft
sources:
- id: add-info
  resource: /references/domain-sources.md
  title: add_info/domain 이식
---

# BQMS / 업체정보

## 프로세스

(없음)

## 테이블과 조회 기준

<업체(vendor) 결합 마스터>
#업체(vendor) 결합 마스터는 BQMS 벤더 마스터 + 구매 벤더 마스터로 구성되며 구매 벤더 마스터에 있으나 BQMS 벤더 마스터에 없는 업체 정보를 추가하여 업체 마스터 구성함.
* 업체(vendor) 결합 마스터 : TI_BQMS800
* BQMS 벤더 마스터 : TI_BQMS024_INFA_VENDOR
* 구매 벤터 마스터 : TI_GRPI002


<업체(vendor) 관련 마스터>
* BQMS 벤더 마스터 : TI_BQMS024_INFA_VENDOR
* 카테고리별 업체 정보 : TI_BQMS014_CATEGORY_VENDOR
* 단독 공급업체(Sole vendor) 정보 : TI_BQMS042_INFA_SOLE_VENDOR

## 테이블 목록

| 테이블 | 유형 (table_type) | 설명 (table_rule) |
|---|---|---|
| [TI_BQMS014_CATEGORY_VENDOR](/schemas/APPADAMSUSER/tables/TI_BQMS014_CATEGORY_VENDOR.md) |  | 카테고리별 벤더 등록/관리 정보 |
| [TI_BQMS024_INFA_VENDOR](/schemas/APPADAMSUSER/tables/TI_BQMS024_INFA_VENDOR.md) |  | VERS 시스템에 등록된 벤더 마스터 |
| [TI_BQMS024_INFA_VENDOR_2](/schemas/APPADAMSUSER/tables/TI_BQMS024_INFA_VENDOR_2.md) |  | TI_BQMS024_INFA_VENDOR 테이블 연계를 위한 I/F전용 테이블 |
| [TI_BQMS030_INFA_VENDOR_APPR](/schemas/APPADAMSUSER/tables/TI_BQMS030_INFA_VENDOR_APPR.md) |  | DS 전용 테이블 |
| [TI_BQMS042_INFA_SOLE_VENDOR](/schemas/APPADAMSUSER/tables/TI_BQMS042_INFA_SOLE_VENDOR.md) |  | ERP 업체코드-BQMS의 SOLE VENDOR로 등록된 업체 리스트 |
| [TI_BQMS800](/schemas/APPADAMSUSER/tables/TI_BQMS800.md) |  |  |
| [TM_BQMS_VENDOR_BZNS_NO](/schemas/APPADAMSUSER/tables/TM_BQMS_VENDOR_BZNS_NO.md) |  |  |
| [VW_BQMS_SAMSUNG_COMPANY](/schemas/APPADAMSUSER/views/VW_BQMS_SAMSUNG_COMPANY.md) | 마스터 |  |
