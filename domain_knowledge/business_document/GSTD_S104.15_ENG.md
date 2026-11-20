---
title: Sell-out Forecasting
doc_id: DOC00005133
source_file: GSTD_S104.15_ENG.docx
doc_no: $104.15
source_version: A.19
effective_from: null
effective_to: null
doc_type: process
tags: [Sell-out Forecast, Sell-in Guide, WOS, AI Forecast, SKU, Account, PM, KAM]
description: 자회사 및 본사의 Sell-out 예측(Sell-out FCST) 수립, AI 예측 활용, 그리고 이를 기반으로 한 Sell-in 가이드(Sell-in Guide) 생성 및 WOS(재고주회) 관리 프로세스를 정의한다.
use_when: Sell-out 예측 입력 주체 및 주기 확인, Sell-in 가이드 생성 로직 이해, WOS 최적화 기준 확인, PM/KAM 간 컨센서스 절차 확인, 채널 구조 변경 시 대응 절차 확인
created_at: 2026-11-12
---

# Sell-out Forecasting

## 1. 핵심 요약
- 자회사는 AI 예측(AI sellout guide)을 참고하여 SKU/Account 수준에서 Sell-out 예측을 수립하며, 수정 시 'under bar'로 업데이트 증거를 남긴다. [p.1]
- 단기(W1~W12) Sell-out 예측은 자회사의 PM/KAM이, 중장기(W13~W24)는 본사 RPM이 입력한다. [p.1]
- 시스템은 Sell-out 예측과 최적 목표 WOS를 기반으로 최적 Sell-in 예측(Sell-in Guide)을 제안하며, 목표 WOS는 GBM 가이드에 따라 설정된다. [p.2]
- Sell-out 예측은 매주 목요일 업데이트, Sell-in 예측은 매주 금요일 Sell-in 가이드 기반으로 반영되는 비즈니스 리듬을 유지한다. [p.2]
- 최종 Sell-out FCST 수량은 자회사 유형에 따라 KAM(CE) 또는 PM(MX)이 결정한다. [p.4]

## 2. 주요 개념 및 정의
- **Sell-out Forecast**: 자회사가 AI 예측을 참고하여 SKU/Account 수준에서 수립하는 예측. [p.1]
- **Sell-in Guide**: Sell-out FCST와 최적 목표 WOS를 계산하여 시스템이 제안하는 최적 Sell-in FCST. [p.2]
- **Target WOS**: 고객의 주문 빈도, 과거 판매, 배송 리드타임을 고려하여 판매 손실을 최소화하기 위해 GBM 가이드에 따라 설정되는 목표 재고주회. [p.2]
- **Under bar**: 사용자가 Sell-out 예측을 업데이트했음을 나타내는 시각적 증거. [p.1]

## 3. 핵심 지식
### 3.1 규정 및 판단 기준
- **입력 수준**: 제품 수준은 SKU, 판매자 계층 수준은 Account 기준. (자회사 상황에 따라 Y2015에서 AP2, AP1, Regional 수준으로 조정 가능) [p.1]
- **WOS 초과 시**: 미래 WOS가 최적 수준을 초과할 경우, SOP(Sales Order Plan)를 이에 맞게 조정한다. [p.2]
- **HHP(High-Value Product) 기준**: Sell-in 스캐닝 프로세스를 통해 Account 수준 Sell-out을 관리하며, 입력 수준은 DP의 AP2 입력 수준과 동기화되어야 한다. [p.2]
- **기타 제품 기준**: EDI 또는 MCS 커버리지 및 데이터 처리 리드타임을 확인하며, 입력 수준은 Account 수준으로 설정 가능. [p.2]

### 3.2 업무 절차
1. **Step 1: Channel structure and sales hierarchy re-structuring**
   - 담당: PM/KAM/HQ GOC
   - 시점: 필요 시 (When required)
   - 내용: 채널 구조 및 판매 계층 변경 시 채널과 판매 계층을 동기화한다. [p.3]
2. **Step 2: AI forecast management**
   - 담당: HQ SCM group AI solution part
   - 시점: 필요 시 (When required)
   - 내용: 본사가 AI 예측을 유지 및 제공해야 한다. [p.4]
3. **Step 3: Sell-out FCST management**
   - 담당: PM / KAM
   - 시점: 매주 (Weekly)
   - 내용: KAM과 PM 간 Sell-out 예측 컨센서스를 형성한다.
     - CE: 최종 Sell-out FCST 수량은 KAM이 결정.
     - MX: 최종 Sell-out FCST 수량은 PM이 결정. [p.4]
4. **Step 4: Sell-in Guide (Sell-out based RTF)**
   - 담당: GOC
   - 시점: 매주 (Weekly)
   - 내용: Sell-out FCST → Target WOS → Sell-in Guide → RTF 순서로 처리. [p.4]

### 3.3 개념·데이터 간 관계
- Sell-out FCST와 Target WOS는 Sell-in Guide 생성의 입력값으로 작용한다. [p.4]
- AI auto copy master setting에 따라 AI 예측은 AI auto copy 설정을 통해 사용되어야 한다. [p.2]

## 4. 적용 상황
- 자회사별 Sell-out 예측 입력 주체(PM/KAM/RPM) 및 주기(주 단위)를 확인해야 할 때.
- Sell-in 가이드가 어떻게 생성되는지(WOS 기반)를 설명해야 할 때.
- HHP와 일반 제품의 Sell-out 데이터 관리 및 입력 수준 차이를 적용해야 할 때.
- 채널 구조 변경 시 필요한 동기화 작업을 수행해야 할 때.

## 5. 예외 및 주의사항
- **입력 수준 조정**: 자회사 특정 상황에 따라 판매자 계층 입력 수준을 Y2015에서 조정할 수 있음(예: AP2, AP1, Regional). [p.1]
- **최종 결정 주체 차이**: CE와 MX 자회사에서 최종 Sell-out FCST 수량을 결정하는 주체가 다르므로(KAM vs PM) 혼동 주의. [p.4]
- **AI 예측 활용**: AI auto copy 설정에 따라 AI 예측을 반드시 AI auto copy master setting을 통해 사용해야 함. [p.2]
- **HHP 특수성**: HHP의 경우 Account 수준 Sell-out 관리를 위해 Sell-in 스캐닝 프로세스를 확인해야 하며, 입력 수준이 AP2와 동기화되어야 함. [p.2]

## 6. 확인 필요 사항
- **Y2015**: 원문에서 "Y2015"라는 용어가 사용되었으나, 연도인지 시스템 코드인지 명확한 정의가 원문에 없음. [p.1]
- **CE/MX**: 자회사 유형으로 언급되었으나, CE와 MX의 정확한 정의나 범위가 원문에 명시되지 않음. [p.4]
- **SOP**: "SOP volume" 및 "SOP will be adjusted"로 언급되었으나, SOP의 정확한 정의(Standard Operating Procedure 또는 Sales Order Plan 등)가 원문에 없음. [p.2]
- **RTF**: Step 4 제목에 "Sell-out based RTF"로 언급되었으나, RTF의 정의가 원문에 없음. [p.4]

## 7. 출처
- 원문: GSTD_S104.15_ENG.docx
- 버전: A.19
- 주요 참조 위치: I. Definition, III. Policy, IV. Check point, V. Procedure