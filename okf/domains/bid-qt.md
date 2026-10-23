---
type: Business Domain
title: BQMS 입찰/견적
description: BQMS 입찰/견적. PR>입찰/견적>선정>발주(PO)>계약(CTR)>입고(GR)>정산(IV) 프로세스. 결합테이블 TI_BQMS810/820/830/840 중심.
tags: ["domain:bid-qt"]
system: BQMS
domain_name: 입찰/견적
status: draft
sources:
- id: add-info
  resource: /references/domain-sources.md
  title: add_info/domain 이식
---

# BQMS / 입찰/견적

## 프로세스

<BQMS 입찰/견적 프로세스>
# 구매요쳥(PR) > 입찰(BD)/견적(QT) > 선정 > 발주(PO) > 계약(CTR) > 입고(GR) > 정산(IV)

## 테이블과 조회 기준

<입찰 및 견적 결합테이블>
# 입찰/견적 집계 RAW 데이터를 바탕으로 구매요청 정보, 결재 정보, 업체 정보, IP정보, ID/PW정보, 구매의뢰 요청자 정보, 구매의뢰일, 법인별 관리주재원 정보를 추가하여 입찰 및 견적정보 결합테이블 생성
* 입찰 및 견적정보 결합테이블 : TI_BQMS810

* 입찰 집계(본사) 테이블 : TI_BQMS004_INFA_BD
* 견적 집계(본사) 테이블 : TI_BQMS005_INFA_QT
* 수작업 BQMS 견적집계 테이블 : TI_BQMS033_INFA_QT_MASTER_RAW
* 견적 결재선 집계 테이블 : TI_BQMS012_APPROVAL_QT
* 입찰 결재선 집계 테이블 : TI_BQMS013_APPROVAL_BD
* 견적정보 차수별 요청업체 테이블 : TI_BQMS045_INFA_QT_UI
* 업체(Vendor) 정보 : TI_BQMS800
* BQMS IP 정보 테이블 : TI_BQMS801
* BQMS ID/PW 정보 테이블 : TI_BQMS802
* BQMS 공통코드 마스터 테이블 : TI_BQMS006_COMMCODE
* 법인별 관리주재원 정보 테이블 : TM_BQMS038_GWANLIJUJAE
* 구매의뢰 요청자 테이블 : TM_BQMS040_ACTIVITY_OWNER
* 구매의뢰일 정보 테이블 : TM_BQMS041_PR_REQ_DATE

<계약내역 결합테이블>
# 입찰/견적 결합정보 데이터를 기반으로 업체(Vendor) 정보, 법무검토 여부 계약 정보, 계약 마스터 정보를 이용하여 계약내역 결합테이블 생성
* 계약내역 결합테이블 : TI_BQMS820

* 계약 마스터(본사) 테이블 : TI_BQMS026_INFA_CTRT
* 업체(Vendor) 정보 : TI_BQMS800
* 입찰 및 견적정보 결합테이블 : TI_BQMS810
* 카테고리 마스터 테이블 : TI_BQMS015_CATEGORY
* 법무검토 진행정보 테이블 : TM_BQMS039_SVC_CTR_LEVEL_YN

<발주 및 정산내역 결합테이블>
# 입찰 및 견적정보 결합테이블 데이터를 바탕으로 발주 정보, 정산 정보를 추가하여 발주 및 정산내역 결합테이블 생성
* 발주 및 정산내역 결합테이블 : TI_BQMS830

* 입찰 및 견적정보 결합테이블 : TI_BQMS810
* 발주 집계(본사) 테이블 : TI_BQMS008_INFA_PO
* 업체(Vendor) 정보 테이블 : TI_BQMS800
* BQMS 공통코드 마스터 테이블 : TI_BQMS006_COMMCODE


<입찰/견적/발주/정산 결함테이블>
# TI_BQMS810, TI_BQMS820, TI_BQMS830 테이블에서 구매요청(PR), 입찰(BD)/견적(QT), 선정, 평가, 발주(PO), 계약(CTR), 정산(IV) 데이터를 모두 발췌하여 최종 테이블로 생성.
* 입찰/견적/발주/정산 테이블 : TI_BQMS840

* 입찰 및 견적 결합테이블 : TI_BQMS810
* 계약내역 결합테이블 : TI_BQMS820
* 발주 및 정산내역 결합테이블 : TI_BQMS830

## 테이블 목록

| 테이블 | 유형 (table_type) | 설명 (table_rule) |
|---|---|---|
| [TI_BQMS004_INFA_BD](/schemas/APPADAMSUSER/tables/TI_BQMS004_INFA_BD.md) | 인터페이스 | 견적 건에 대한 카테고리, 아이템, 진행상태, 업체정보, 금액, 시간, IP, 구매요청번호(PR_NO), 계약번호(CTR_NO) 등을 포함. |
| [TI_BQMS005_INFA_QT](/schemas/APPADAMSUSER/tables/TI_BQMS005_INFA_QT.md) | 인터페이스 | 입찰 건에 대한 카테고리, 아이템, 진행상태, 업체정보, 금액, 시간, IP, 구매요청번호(PR_NO), 계약번호(CTR_NO) 등을 포함. |
| [TI_BQMS005_INFA_QT_2](/schemas/APPADAMSUSER/tables/TI_BQMS005_INFA_QT_2.md) |  | TI_BQMS005_INFA_QT 테이블 연계를 위한 I/F전용 테이블 |
| [TI_BQMS008_INFA_PO](/schemas/APPADAMSUSER/tables/TI_BQMS008_INFA_PO.md) |  | 사이트별 EO, PO, 발주총액, PO생성일자, PO생성자, 계약번호, 업체 정보를 포함하는 테이블 |
| [TI_BQMS011_BD_EVL](/schemas/APPADAMSUSER/tables/TI_BQMS011_BD_EVL.md) |  | 입찰견적 건별 업체별 평가 정보 테이블, |
| [TI_BQMS012_APPROVAL_QT](/schemas/APPADAMSUSER/tables/TI_BQMS012_APPROVAL_QT.md) |  | 견적건 결재ID, 진행 상태, 상신자, 결재자 정보 |
| [TI_BQMS013_APPROVAL_BD](/schemas/APPADAMSUSER/tables/TI_BQMS013_APPROVAL_BD.md) |  | 입찰건 결재ID, 진행 상태, 상신자, 결재자 정보 |
| [TI_BQMS017_LOG_BD_SUBMIT](/schemas/APPADAMSUSER/tables/TI_BQMS017_LOG_BD_SUBMIT.md) |  | 입찰 제출 접속메뉴, 사용자ID, 사용날짜, URL, IP 정보 테이블 |
| [TI_BQMS018_LOG_BD_RETRV](/schemas/APPADAMSUSER/tables/TI_BQMS018_LOG_BD_RETRV.md) |  | 입찰 조회 접속메뉴, 사용자ID, 사용날짜, URL, IP 정보 테이블 |
| [TI_BQMS019_LOG_QT_SUBMIT](/schemas/APPADAMSUSER/tables/TI_BQMS019_LOG_QT_SUBMIT.md) |  | 견적 제출 접속메뉴, 사용자ID, 사용날짜, URL, IP 정보 테이블 |
| [TI_BQMS020_LOG_QT_RETRV](/schemas/APPADAMSUSER/tables/TI_BQMS020_LOG_QT_RETRV.md) |  | 견적 조회 접속메뉴, 사용자ID, 사용날짜, URL, IP 정보 테이블 |
| [TI_BQMS021_LOG_EVL_SUBMIT](/schemas/APPADAMSUSER/tables/TI_BQMS021_LOG_EVL_SUBMIT.md) |  | 평가 제출 접속메뉴, 사용자ID, 사용날짜, URL, IP 정보 테이블 |
| [TI_BQMS022_LOG_EVL_RETRV](/schemas/APPADAMSUSER/tables/TI_BQMS022_LOG_EVL_RETRV.md) |  | 평가 조회 접속메뉴, 사용자ID, 사용날짜, URL, IP 정보 테이블 |
| [TI_BQMS026_INFA_CTRT](/schemas/APPADAMSUSER/tables/TI_BQMS026_INFA_CTRT.md) |  | 계약번호, 계약금액, 계약기간, 업체코드, 계약유형, 견적입찰 번호 포함하는 테이블 |
| [TI_BQMS026_INFA_CTRT_H](/schemas/APPADAMSUSER/tables/TI_BQMS026_INFA_CTRT_H.md) |  | 계약번호, 계약금액, 계약기간, 업체코드, 계약유형, 견적입찰 번호 포함하는 아카이빙 테이블 |
| [TI_BQMS031_BD_EVL_DTL](/schemas/APPADAMSUSER/tables/TI_BQMS031_BD_EVL_DTL.md) |  | 입찰견적 건별 업체별 평가 정보에 평가자별 점수 및 평가 사유 등 정보가 추가된 테이블 |
| [TI_BQMS032_INFA_QT_RESULT](/schemas/APPADAMSUSER/tables/TI_BQMS032_INFA_QT_RESULT.md) |  | 입찰번호별 업체 선정사유 TEXT 정보 포함 테이블 |
| [TI_BQMS033_INFA_QT_MASTER_RAW](/schemas/APPADAMSUSER/tables/TI_BQMS033_INFA_QT_MASTER_RAW.md) |  | 견적건 별 카테고리, 업체정보, 업체 제출정보 테이블. 견적 집계보다 제한적 데이터 보유한 비정기 연계 테이블 |
| [TI_BQMS034_INFA_BD_MASTER_RAW](/schemas/APPADAMSUSER/tables/TI_BQMS034_INFA_BD_MASTER_RAW.md) |  | 입찰건 별 카테고리, 업체정보, 업체 제출정보 테이블. 입찰 집계보다 제한적 데이터 보유한  비정기 연계 테이블 |
| [TI_BQMS045_INFA_QT_UI](/schemas/APPADAMSUSER/tables/TI_BQMS045_INFA_QT_UI.md) |  | 차수별 견적 업체 제출 정보로 견적 집계보다 제한적 데이터 보유 |
| [TI_BQMS045_INFA_QT_UI_BASE](/schemas/APPADAMSUSER/tables/TI_BQMS045_INFA_QT_UI_BASE.md) |  | 차수별 견적 업체 제출 정보로 견적 집계보다 제한적 데이터 보유 |
| [TI_BQMS810](/schemas/APPADAMSUSER/tables/TI_BQMS810.md) |  | 입찰집계, 견적집계 RAW 데이터를 바탕으로 구매요청 정보, 결재 정보, 업체 정보, 입찰 Item항목 정보, 평가 정보 등을 추가하여 생성한 입찰 및 견적정보 결합테이블 |
| [TI_BQMS820](/schemas/APPADAMSUSER/tables/TI_BQMS820.md) |  | TI_BQMS810 테이블 정보에서 입찰/견적, 업체 정보를 뽑고 계약 정보를 추가한 계약내역 결합테이블 |
| [TI_BQMS830](/schemas/APPADAMSUSER/tables/TI_BQMS830.md) |  | TI_BQMS820 테이블 정보에 발주 정보, 정산 정보를 추가한 발주 및 정산내역 결합테이블 |
| [TI_BQMS840](/schemas/APPADAMSUSER/tables/TI_BQMS840.md) |  | TI_BQMS810, TI_BQMS820, TI_BQMS830 테이블에서 구매요청(PR), 입찰(BD)/견적(QT), 선정, 평가, 발주(PO), 계약(CTR), 정산(IV) 데이터를 모두 발췌하여 그상힌 최종 결합테이블 |
| [TI_BQMSMB001](/schemas/APPADAMSUSER/tables/TI_BQMSMB001.md) |  |  |
| [TI_BQMSMB002](/schemas/APPADAMSUSER/tables/TI_BQMSMB002.md) |  |  |
| [TM_BQMS041_PR_REQ_DATE](/schemas/APPADAMSUSER/tables/TM_BQMS041_PR_REQ_DATE.md) |  | 입철견적번호에 구매요청번호(PR_NO)매핑한 테이블 |


## 관련 업무 지식

- [입찰·견적의 요청, 차수와 업체 제출](/glossary/biz-procurement-request-submission.md) — 입찰·견적은 물품이나 용역을 사기 위해 여러 업체의 제안을 받는 절차다. 요청 하나가 여러 차수로 진행되면 차수마다 입찰 건이 생기며, 업체 제출건은 업체가 품목별로 제시한 가격 제안을 뜻한다.
- [평가 항목, 평가자 기록과 선정 결과](/glossary/biz-procurement-evaluation-selection.md) — 입찰·견적 평가는 업체가 평가 항목별로 받은 점수와 평가자의 사유·의견을 담는다. 선정 결과에는 최저가 또는 최고 평가 업체를 고르지 않은 경우의 사유도 기록한다.
- [요청 결재와 계약 변경 결재](/glossary/biz-procurement-approvals.md) — 결재선은 요청의 상신부터 완결까지 누가 어떤 순서로 결재했는지를 담는다. 계약 변경 이력은 변경 시점의 조건을 차수별로 구분해, 언제 무엇이 달라졌는지 보여 준다.
- [구매계약의 항목과 변경 이력](/glossary/biz-procurement-contract-details.md) — 계약항목은 계약 안의 개별 항목으로, 한 계약에 여러 항목이 있을 수 있고 항목마다 금액과 카테고리가 다를 수 있다. 계약 변경 이력은 변경 시점의 조건을 차수별로 담는다.
