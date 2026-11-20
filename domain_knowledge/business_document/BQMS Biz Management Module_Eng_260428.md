---
title: BQMS(Biz. Management) Manual / Biz Management Module
source_file: BQMS Biz Management Module_Eng_260428.pdf
source_version: 260428
effective_from: null
effective_to: null
doc_type: mixed
tags: [BQMS, Bidding, Quotation, Contract, Work Order, Inspection, Settlement, Posting]
description: BQMS Biz Management Module의 입찰·견적, 계약, 발주, 검수, 정산 및 기장(Posting)까지의 업무 절차, 판단 기준 및 시스템 연동 규칙을 정의한 문서
use_when: BQMS 입찰/견적 기준 문의, WO 생성 및 수정 권한 확인, 검수/정산/경비청구서 처리 절차 문의, Legal System 연동 및 계약 데이터 변경 절차 문의, Posting Process 오류 처리 문의
created_at: 2026-11-10
---

# BQMS(Biz. Management) Manual / Biz Management Module

## 1. 핵심 요약
- BQMS는 벤더 선택, PO/검사, 정산까지의 비즈니스 프로세스를 관리하며, 벤더 유착 방지와 부패 예방이 목적임.
- Bidding은 2개 이상 업체 대상 종합 평가, Quotation은 1개 이상 업체 대상 가격 중심 최저가 선정으로 구분됨.
- Work Order(WO)는 계약 완료 후 발주 요청 생성 문서이며, Inspection(검수)은 정산 전 필수 단계임.
- 정산(Settlement)은 'Confirm' 후 조건부 경비 청구서 생성 및 'Posting Process'로 이어지며, N-ERP 기장까지 연계됨.
- 시스템 간 연동(VERS, Legal System, N-ERP 등)에 따라 WO 생성이나 데이터 수정 권한에 제약을 가짐.

## 2. 주요 개념 및 정의
- **BQMS**: Bidding & Quotation Management System. 벤더 선택, PO/검사 허용 시스템 [p.1, p.68]
- **Bidding**: 2개 이상 업체, 기술 포함 종합 평가 방식 [p.1]
- **Quotation(RFQ)**: 1개 이상 업체, 가격 중심 최저가 선정 방식 [p.1]
- **Unit Price Contract**: 변동비 성격, 추정량×단가로 정산, 계약 금액 초과 발주 가능 [p.1]
- **Lump-sum Contract**: 고정비 성격, 총액 초과 정산/발주 불가 [p.1]
- **Work Order(WO/PO)**: 계약 완료 후 생성되는 발주 요청 문서 [p.1]
- **Inspection(검수)**: 정산 전 필수 단계, 결함 시 거절 가능 [p.1]
- **Settlement(정산)**: 벤더 인보이스 또는 구매 요청자가 직접 생성하여 진행하는 절차 [p.1]
- **Expense Report(경비 청구서)**: 정산 'Confirm' 시 'Expense Report Necessity' 체크에 따라 생성 [p.1]
- **Contract base**: 정산 시 Final Amount를 직접 입력하는 방식 [p.64]
- **GR Base**: 정산 시 Final Amount를 수정할 수 없는 방식 [p.64]
- **PR/QT/BD/CO/PO**: 각각 벤더 선정 요청, 견적서, 입찰서, 선정 결과(계약), 작업 주문서 문서 번호 [p.66]

## 3. 핵심 지식
### 3.1 규정 및 판단 기준
- **담당자 분리 원칙**: Requester와 Manager, Procurement Mgmt 담당자와 Created by 작성자는 동일인 불가 [p.1]
- **견적 제출 기간**: 최소 48시간 설정 필수, 단축 불가. Close 후 연장/봉인 시 마감 취소 불가 [p.1]
- **평가 기준**: 평가자 최소 2명 필수. VAT 제외 단가 입력. Evaluator는 견적서 열람 불가 [p.1]
- **벤더 선정**: 입찰/견적 시 벤더 2개 이상 복수 선택 필수. Target Amount Cost 순서는 Previous → Budget → Market → Est. 순으로 적용 [p.1]
- **Legal System I/F**: 상태가 'Y'인 경우, 법무 계약 번호 연동 없이는 WO 생성 불가 [p.1]
- **WO 수정 범위**: 승인 후에도 Subject, Issue Date, Inspector, Item Qty만 수정 가능 [p.1]
- **검사 제한**: 승인/거절 시 Comment 50자 이내. 정산 완료 시 거절(재검수) 불가 [p.1]
- **정산 거절**: 'Reject' 시 사유 입력 필수. 'Confirm' 시 경비 청구서 필요성 선택 및 사유 입력 필수 [p.1]
- **기장(Posting) 제약**: N-ERP 시스템 내에서는 Posting Process 정보 수정 불가. 오류 없으면 자동 제출 및 회계 부서 승인 처리 [p.65]
- **계약 데이터 변경**: 완료된 계약 기간 변경 및 Legal system I/F 상태값 변경('Y'→'N') 시 승인(Approve) 필요 [p.67]

### 3.2 업무 절차
1. **요청~계약**: Request → Reception → Bidding/Quotation 등록 → 평가 → 결과 확인(CO## 생성) → Contract Mgmt [p.1]
2. **Work Order(WO) 생성**:
   - 경로: BQMS > Biz. Mgmt > Contract/Work Order > Work Order > Create [p.1]
   - 계약 검색 → PO 정보/첨부파일/항목(최대 100개) 선택 → 'Request' [p.1]
3. **검사(Inspection) 수행**:
   - Vendor Portal: Delivery Confirmation Request → PO 선택 → Create [p.1]
   - BQMS: Inspection Process → 검색 → Delivery Information 확인 → Subject 선택 → Approve/Rejected [p.1]
4. **정산(Settlement) 및 기장(Posting)**:
   - Invoice Confirm: 대상 탐색 → 벤더 선택 → 인보이스 선택 → 'Confirm' [p.64]
   - Expense Report: 필요 시 작성 및 제출 [p.64]
   - Posting Process: 대상 선택 → Edit(정보 입력/저장) → Submit → 최종 Submit [p.65]

### 3.3 개념·데이터 간 관계
- **프로세스 흐름**: Request → Bidding/Quotation → Contract → WO → Inspection → Goods Receipt → Settlement → Posting [p.1]
- **검사-정산 의존성**: 검수 승인/거절 후 Goods Receipt 'Received' 상태가 형성되며, 이는 정산의 선행 필수 조건임 [p.1]
- **정산-경비청구-기장**: 'Confirm' 처리 후 'Expense Report Necessity'에 따라 경비 청구서가 생성되며, 이후 'Posting Process'로 이어짐 [p.1, p.64]
- **시스템 연동**:
  - VERS: 벤더/카테고리 검색 [p.1]
  - Legal System(CLM, CCLMS 등): WO 생성 전제 조건 [p.1, p.67]
  - N-ERP/My-Pumui: 기장(Posting) 처리 시스템 [p.1, p.65]
  - 연동 사이트: CIS, G-SRM, GPMS, ECMS 2.0, Global EHS, DS 등 [p.68]

## 4. 적용 상황
- BQMS에서 Bidding과 Quotation의 적용 차이 및 평가 기준 문의 시
- Work Order 생성 시 Legal System 연동 상태에 따른 권한 확인
- 정산 완료 후 검수 거절(재검수)이 불가능한 이유 문의 시
- Posting Process 진행 중 N-ERP에서 수정이 불가한 이유 문의 시
- 계약 종료 후 계약 기간이나 Legal System 연동 상태 변경 요청 시

## 5. 예외 및 주의사항
- **발주 제한**: Lump-sum 계약은 총액 초과 발주/정산 불가. Unit Price 계약은 단가 기반 계약 금액 초과 발주 가능 [p.1]
- **조기 종결 금지**: Submission Period 내 조기 종결 및 벤더 선정 금지 [p.1]
- **비최저가 선정**: 'Non-cheapest selection'으로 선정 시 Item Code 기록 필수 [p.1]
- **Legal Status 변경 주의**: 'Y'에서 'N'으로 변경 시 법적 시스템에 계약 내용이 반영되지 않으므로, 법적 시스템에서 별도로 수정해야 함 [p.67]
- **검색 불가 상황**: VERS 미등록, 카테고리 미매핑, Portal 미가입/비활성화 시 검색 불가 [p.1]
- **첨부파일 제한**: WO 첨부파일 최대 999개, 총 용량 200.0 MB 이내 [p.1]

## 6. 확인 필요 사항
- **Bidding/RFQ No 표기**: 'BD25087454' vs 'B025087454', RFQ No 세 가지 상이 사례 존재 [p.1]
- **Evaluator 이름 표기**: 'MYOUNGHOON PARK' vs 'MIYOUNGHOON PARK' [p.1]
- **기술 평가 점수**: 팝업 '-4' vs 표 데이터 '0' [p.1]
- **파일 용량 표기**: '200.0 MB(A)' 중 'A'의 의미 불명 [p.1]
- **Vendor After Bidding Registration**: 정확한 정의 및 전 단계 절차 불명확 [p.1]
- **Subject 표기 불일치**: p.54 이미지 "일질 Test" vs 테이블 "입찰 Test" [p.1]
- **Date Created 상이**: p.54(11/25/2025) vs p.55(3/31/2026, 4/22/2026) [p.1]
- **Delivery Information**: p.58 테이블 구조 손상/빈칸으로 실질 내용 부재 [p.1]
- **검사 승인 순서**: p.58에서 '선택'이 '확인'보다 먼저 목록에 나와 있어 순서적 의미 불명확 [p.1]
- **Request Number 불일치**: p.60 목록 'IE25007026' vs 상세 'IE25Q07026' [p.1]
- **GR Status 정의**: 'Confirmed' 상태 정의 및 'Received'와의 전환 조건 미명시 [p.1]
- **날짜 논리 오류**: p.62 인보이스 발행일(11/26/2025)이 확인일(10/28/2025)보다 미래인 경우 존재 [p.1]
- **Invoice Vendor 불일치**: p.64 Invoice Information의 'Samsung Medison Co.,Ltd(TRT2)'와 선택 단계의 'Stephens Machine Inc.' 간 컨텍스트 불일치 [p.64]
- **Invoice No 중복**: p.64 Invoice Information 표에서 'Invoice No.' 행이 두 번 반복됨 [p.64]
- **Document Flow 데이터**: p.66 GR25186342 행의 Subject 및 Period 값이 비어있거나 '~'로 표기 [p.66]

## 7. 출처
- 원문: BQMS Biz Management Module_Eng_260428.pdf
- 버전: 260428
- 주요 참조 위치: p.1-63 (핵심 프로세스/규정), p.64-66 (정산/기장/문서 흐름), p.67-69 (데이터 변경/연동 정보)