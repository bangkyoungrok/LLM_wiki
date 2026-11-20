---
title: Sales Trade Spend $106 / TIM overview $106.10
source_file: GSTD_S106.10_ENG.docx
source_version: B.4
effective_from: null
effective_to: null
doc_type: mixed
tags: [TIM, Trade Spend, Marketing Spend, KPI, CORES, RRP, Sell-out, GSTD]
description: TIM(Trade Investment Management)의 개념, Trade Spend 및 Marketing Spend 분류 체계, 관리 프로세스(CORES/SMIT), 그리고 핵심 성과 지표(KPI) 산식과 기준을 정의한 표준 문서.
use_when: TIM 관련 비용(Trade/Marketing Spend) 분류 코드 조회, TIM KPI(효율성, 성취도 등) 계산 및 해석, 프로모션 계획 및 실행 프로세스 점검, RRP 기반 매출(Net Sales) 구조 이해
created_at: 2026-11-09
---

# Sales Trade Spend $106 / TIM overview $106.10

## 1. 핵심 요약
TIM(Total Investment to Market)은 Trade Spend(세일즈 공제, 마케팅 공동 광고)과 Marketing Spend(ATL, BTL)를 포함하여 RRP에서 Net Sales까지의 투자 활동을 관리하는 체계이다. TIM 활동은 총 42개로, 세일즈 공제(34개), 마케팅 스피드(25개) 중 17개 공통 활동을 중복 제거하여 산정한다. 수익 구조는 RRP에서 딜러 할인으로 Gross Sales, 다시 Trade Spend 차감으로 Net Sales가 도출된다.
관리 도구로는 CORES(프로모션 ROI 관리)와 SMIT(마케팅 투자 배분 최적화)를 활용하며, 2013년부터 Activity 없는 Direct Posting은 제한된다. 성과 관리(KPI)는 Trade/Mktg Spend Rate, Sell-out Ratio, Price Protection Rate, Sell-out Achievement Rate 등 연간 목표 대비 효율성을 측정하는 데 초점을 맞춘다.

## 2. 주요 개념 및 정의
- **TIM (Total Investment to Market)**: Trade spend + Marketing spend. 유통업자/대리점을 통한 소비자 판매 및 마케팅 총 투자 [p.1]
- **Trade Spend**: 매출 공제(Sales Deduction)와 마케팅 공동 광고(Marketing Co-Op)의 합. Gross Sales에서 차감하여 Net Sales를 도출 [p.1]
- **RRP (Recommended Resale Price)**: 권장 재판매 가격 [p.3]
- **CORES**: Sales deduction management system. 프로모션의 범위·타이밍 의사결정 지원 및 ROI 시뮬레이션·계획·실행·분석 시스템 [p.6]
- **SMIT (Samsung Marketing Investment Tool)**: 소비자 인사이트와 데이터 기반으로 마케팅 투자 배분을 최적화하는 도구 (CDJ Research, Marketing ROI Modeling, Optimization 기반) [p.6]
- **TIM Efficiency Rate**: `(Gross Sales^n / Gross Sales^{n-1}) / (TIM^n / TIM^{n-1})`. 전년 대비 매출 성장률과 지출 성장률의 비 [p.8]

## 3. 핵심 지식

### 3.1 규정 및 판단 기준
- **TIM 활동 분류 코드**:
  - 총 활동 수: 42개 (34 + 25 - 17 중복) [p.2]
  - Trade Spend Activity Code: 34개 (Sell-in 13, Sell-out 20, Price Protection 1) [p.2]
  - Marketing Spend Activity Code: 본문 20개로 명시, 상세 분류는 총 25개(ATL 11 + BTL 14)로 구성 [p.2, p.3]
- **Direct Posting 제한**: Activity 없이 직접 Posting하는 것은 2013년부터 제한됨 [p.7]
- **예외 계정**: `Ad Exp - Other (54176900)` 및 `Sales Promo Exp - Other (54196901)` 만 예외적으로 사용 가능 [p.7]
- **KPI 산식**:
  - Trade Spend Rate: `Trade spend / RRP Amount` [p.8]
  - Mktg Spend Rate: `Mktg. spend / Net sales` [p.8]
  - Sell-Out Ratio: `Sell-Out activity amount / Trade Spend amount` [p.8]
  - Price Protection Rate: `Price protection amount / Gross Sales amount` [p.8]
  - Sales Deduction Ratio: `(S/Deduction + Mktg Coop) amount / Trade Spend amount` [p.8]
  - Sell-out Achievement Rate: `Actual sell-out AMT / Target sell-out AMT` (AMT = Qty X Gross price, Gross price는 최근 1개월 인보이스 평균가) [p.8]

### 3.2 업무 절차
1. **Promotion Plan (계획)**: 명확한 목적 및 행동 항목 수립 → Baseline sales 추정 및 ROI 분석 → 리테일러 협상 [p.6]
2. **Execute and Monitor (실행 및 모니터링)**: 계획에 따른 실행 및 진행 상황 모니터링 [p.6]
3. **Evaluate (평가)**: 실제 ROI 분석 및 학습 사항 정리하여 향후 계획 반영 [p.6]
4. **RRP 관리**: GBMs가 월별 RRP 가이드라인 제공, GFK 데이터 활용, 승인 리드 타임 단축 목표 [p.3]
5. **TIM Management**: Activity별 연차/월별 계획 프로세스 강화, 총 예산 기반에서 제품/Activity별 예산으로 전환 [p.7]

### 3.3 개념·데이터 간 관계
- **수익 구조**: `RRP - Dealer Discount = Gross Sales` → `Gross Sales - Trade Spend = Net Sales` [p.1]
- **시스템 연동**: CORES는 GSCM(Sell-out FCST, Actual) 및 GERP(Price, Cost, RRP) 데이터와 연동 [p.6]
- **BI Report**: TIM spending을 P&L account 또는 TIM Activity별로 조회, Plan/Target/Actual 비교 제공 [p.4-5]
- **SMIT 기반**: CDJ Research(CE Category Touch point 구매 영향) 및 McKinsey 전문성 기반 Marketing ROI Modeling 활용 [p.6]

## 4. 적용 상황
- TIM 관련 비용 항목이 Trade Spend인지 Marketing Spend인지 분류할 때
- 프로모션 기획 단계에서 ROI 추정 및 예산 배분 기준을 수립할 때
- 월/연말 정산 시 Trade Spend Rate, Sell-out Achievement Rate 등 KPI 달성 여부를 계산할 때
- Direct Posting이 불가한 경우 예외 계정(54176900, 54196901) 적용 가능 여부를 판단할 때

## 5. 예외 및 주의사항
- **공통 활동 중복 제거**: 세일즈 공제와 마케팅 스피드에 공통으로 존재하는 17개 활동은 총 활동 수(42개) 계산 시 중복으로 처리되지 않도록 주의 [p.2]
- **Gross Price 산정**: Sell-out Achievement Rate 계산 시 Gross price는 '최근 1개월간 인보이스 평균 가격'을 기준으로 해야 함 [p.8]
- **Direct Posting 금지**: 예외 계정이 아닌 일반 계정으로 Activity 없이 Direct Posting하는 것은 불가함 [p.7]
- **보안**: 문서 전체가 'Confidential' 마킹됨 [p.1-8]

## 6. 확인 필요 사항
- **Marketing Spend 코드 수 불일치**: 본문에서는 Marketing Spend Activity Code를 20개로 명시하였으나, 상세 분류는 ATL(11)+BTL(14)로 총 25개로 나열되어 있음. 실제 적용 코드 수 확인 필요 [p.2, p.3]
- **Sell-out Investment 항목 수**: 표상 Sell-out Investment를 20개로 기재했으나, 세부 채널(4개) 하위 항목 포함 시 20개가 되는지 정합성 확인 필요 [p.2]
- **표 구조 모호함**: p.4-7 상단 테이블의 열 이름(Sales, $106 등)이 불명확하거나 레이아웃 오류일 수 있음 [p.4-7]

## 7. 출처
- 원문: GSTD_S106.10_ENG.docx
- 버전: B.4
- 주요 참조 위치: p.1(개념/구조), p.2-3(분류/코드), p.6(프로세스/시스템), p.8(KPI 산식)