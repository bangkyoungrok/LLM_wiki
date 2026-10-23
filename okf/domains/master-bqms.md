---
type: Business Domain
title: BQMS 기준정보
description: BQMS 기준정보. IP, 사용자, 사이트, 카테고리, 공통코드 마스터.
tags: ["domain:master-bqms"]
system: BQMS
domain_name: 기준정보
status: draft
sources:
- id: add-info
  resource: /references/domain-sources.md
  title: add_info/domain 이식
---

# BQMS / 기준정보

## 프로세스

(없음)

## 테이블과 조회 기준

<IP 정보>
# 사내외 IP대역, 입찰/견적 제출IP 정보 테이블 관리
* IP 마스터 : TI_BQMS801
* 사내IP대역 : TN_BQMS099_COMPANY_IP
* 사설IP대역 : TN_BQMS098_PRIVATE_IP

<사용자 정보>
# 사용자 ID/PW, 접속IP, 접속 사이트, 권한 등을 관리
* ID/PW : TI_BQMS802
* 업체 사용차 : TI_BQMS001_URV_FULL
* BQMS 사내외 사용자 : TI_BQMS002_INFA_USER
* 업체 접속이력 : TI_BQMS003_SYS_USE_MST_HISTORY
* 사내사용자 권한 : TI_BQMS007_USER_ROLE

<사이트>
# BQMS의 사이트 정보 및 사용자별 접속 가능 사이트 정보 관리
* BQMS 사이트 정보 : TI_BQMS010_INFA_SITE
* 사내 사용자 접속 사이트 : TI_BQMS016_USER_SITE

<카테고리>
# BQMS 시스템 카테고리, 아이템 항목 정보
* BQMS 시스템 카테고리 : TI_BQMS015_CATEGORY
* BQMS 카테고리별 아이템 : TI_BQMS044_INFA_ITEM

## 테이블 목록

| 테이블 | 유형 (table_type) | 설명 (table_rule) |
|---|---|---|
| TI_BQMS001_URV_FULL (접근 범위 밖) |  | 접속화면 메뉴, 접속일시, 접속 사용자 IP 등 등록한 테이블 |
| [TI_BQMS002_INFA_USER](/schemas/APPADAMSUSER/tables/TI_BQMS002_INFA_USER.md) | 인터페이스 | 사내외 사이트 코드, 사용자ID,업체 코드등 업체 사용자 정보 테이블 |
| [TI_BQMS003_SYS_USE_MST_FULL](/schemas/APPADAMSUSER/tables/TI_BQMS003_SYS_USE_MST_FULL.md) | 마스터 | 사내외 사이트 코드, 사용자ID,업체 코드등 업체 사용자 정보 테이블 |
| [TI_BQMS003_SYS_USE_MST_HISTORY](/schemas/APPADAMSUSER/tables/TI_BQMS003_SYS_USE_MST_HISTORY.md) | 마스터 | 사내외 사이트 코드, 사용자ID,업체 코드등 업체 사용자 정보 히스토리 테이블 |
| [TI_BQMS006_COMMCODE](/schemas/APPADAMSUSER/tables/TI_BQMS006_COMMCODE.md) |  | 도시정보, 계약형태, 사이트, 벤더 정보 등 BQMS에서 사용하는 코드를 등록한 마스터 테이블 |
| [TI_BQMS007_USER_ROLE](/schemas/APPADAMSUSER/tables/TI_BQMS007_USER_ROLE.md) |  | 사내 사용자 권한,, ROLE 정보 테이블 |
| [TI_BQMS010_INFA_SITE](/schemas/APPADAMSUSER/tables/TI_BQMS010_INFA_SITE.md) |  | BQMS 사이트 정보. DS, SDC, 자회사 구분 코드 정보 테이블 |
| [TI_BQMS015_CATEGORY](/schemas/APPADAMSUSER/tables/TI_BQMS015_CATEGORY.md) |  | BQMS 카테고리 테이블 |
| [TI_BQMS016_USER_SITE](/schemas/APPADAMSUSER/tables/TI_BQMS016_USER_SITE.md) |  | 사용자별 접속 가능 사이트 정보 등록 테이블 |
| [TI_BQMS044_INFA_ITEM](/schemas/APPADAMSUSER/tables/TI_BQMS044_INFA_ITEM.md) |  | BQMS 아이템 항목 관리 테이블 |
| [TI_BQMS801](/schemas/APPADAMSUSER/tables/TI_BQMS801.md) |  | 사내외 IP대역, 입찰/견적 제출IP 정보를 모아놓은 IP정보 테이블 |
| [TI_BQMS802](/schemas/APPADAMSUSER/tables/TI_BQMS802.md) |  | BQMS 사용자 마스터 히스토리 테이블에서 ID/PW 정보 구성 테이블 |
| [TM_BQMS035_PREDICT_NOTICE](/schemas/APPADAMSUSER/tables/TM_BQMS035_PREDICT_NOTICE.md) |  | 목표가 정보 등록 테이블. 신규 목표가 등록 정보는 없음 |
| [TM_BQMS036_CTR_CHANGE_APPROVAL](/schemas/APPADAMSUSER/tables/TM_BQMS036_CTR_CHANGE_APPROVAL.md) |  | 매월 수동 입수하는 결재 변경 내역 테이블 |
| [TM_BQMS038_GWANLIJUJAE](/schemas/APPADAMSUSER/tables/TM_BQMS038_GWANLIJUJAE.md) |  |  |
| [TM_BQMS039_SVC_CTR_LEVEL_YN](/schemas/APPADAMSUSER/tables/TM_BQMS039_SVC_CTR_LEVEL_YN.md) |  | 입찰 견적 번호, 계약 번호, 법무검토 여부 매핑된 테이블 |
| [TM_BQMS040_ACTIVITY_OWNER](/schemas/APPADAMSUSER/tables/TM_BQMS040_ACTIVITY_OWNER.md) |  | 입찰 견적 번호와 구매의롸 요청자 정보 매핑된 테이블 |
| [TN_BQMS098_PRIVATE_IP](/schemas/APPADAMSUSER/tables/TN_BQMS098_PRIVATE_IP.md) |  | 수동 입수하는 사설 IP 대역 리스트 |
| [TN_BQMS099_COMPANY_IP](/schemas/APPADAMSUSER/tables/TN_BQMS099_COMPANY_IP.md) |  | 수동 입수하는 사내 IP 대역 리스트 |
