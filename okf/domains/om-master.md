---
type: Business Domain
title: 영업마케팅 기준정보(마스터)
description: 영업마케팅 기준정보(마스터). TimeZone, FTZ, 관리주재원(CFO) 등 부가 마스터.
tags: ["domain:om-master"]
system: 영업마케팅
domain_name: 기준정보(마스터)
status: draft
sources:
- id: add-info
  resource: /references/domain-sources.md
  title: add_info/domain 이식
---

# 영업마케팅 / 기준정보(마스터)

## 프로세스

(없음)

## 테이블과 조회 기준

(없음)

## 테이블 목록

| 테이블 | 유형 (table_type) | 설명 (table_rule) |
|---|---|---|
| [TI_CORES_ACTIVITY](/schemas/APPADAMSUSER/tables/TI_CORES_ACTIVITY.md) |  | CORES 프로모션 ACTIVITY 기준정보 |
| [TI_GRPB_B2B_FTZ](/schemas/APPADAMSUSER/tables/TI_GRPB_B2B_FTZ.md) |  | 자유 무역지구(Free Trade Zone) 기준 정보 |
| [TI_GRPB_CFO](/schemas/APPADAMSUSER/tables/TI_GRPB_CFO.md) |  | 해외법인 관리주재원 정보 : 최신 정보 아니라 미사용되고 있으나 조회 조건에 반드시 필요할 경우 사용 |
| [TI_GRPB_COMPANY_AUDIT_AMT](/schemas/APPADAMSUSER/tables/TI_GRPB_COMPANY_AUDIT_AMT.md) |  |  |
| [TI_GRPB_TIME_ZONE](/schemas/APPADAMSUSER/tables/TI_GRPB_TIME_ZONE.md) |  | 글로벌 시간대(Time zone) 정보 |
