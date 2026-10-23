---
type: Oracle Table
title: BQMS 사용자마스터 히스토리테이블
description: BQMS 사용자마스터 히스토리테이블.
resource: oracle://PRD/APPADAMSUSER/TI_BQMS003_SYS_USE_MST_HISTORY
tags: ['kind:table', 'owner:appadamsuser', 'class:history', 'size:m', 'access:select-full', 'quality:no-pk', 'domain:master-bqms']
owner: APPADAMSUSER
table_name: TI_BQMS003_SYS_USE_MST_HISTORY
query_name: APPADAMSUSER.TI_BQMS003_SYS_USE_MST_HISTORY
table_class: history
row_count: 3730000
last_analyzed: 2026-10-12
status: draft
stale_after: 2027-01-11T13:53:08+09:00
sources:
- id: dict
  resource: /references/dictionary-sources.md
  title: 딕셔너리 추출 스냅샷
generated:
  by: process:okf-dict-builder/0.1
  at: 2026-10-13T13:53:08+09:00
table_type: 마스터
business_area: BQMS
business_detail: 사용자정보
---

# 개요
(사람이 보완: 업무 의미, 생성 시점, 주의 사항)

# Schema
<!-- AUTO:BEGIN schema -->
| # | 컬럼 | 한글명 | 타입 | NULL | 키 | 코드/참조 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | 사내외구분 | 사내외구분 | VARCHAR2(20) | Y |  |  |  |
| 2 | SITE_CODE | 사이트코드 | VARCHAR2(20) | Y |  |  |  |
| 3 | USER_ID | 사용자ID | VARCHAR2(100) | Y |  |  |  |
| 4 | ACTIVE_FLAG | 사용여부 | VARCHAR2(10) | Y |  |  |  |
| 5 | USER_NAME | 사용자명 | VARCHAR2(300) | Y |  |  |  |
| 6 | COMP_CODE | 업체코드 | VARCHAR2(100) | Y |  |  |  |
| 7 | COMP_NAME | 업체명 | VARCHAR2(200) | Y |  |  |  |
| 8 | EN_COMP_NAME | 영문업체명 | VARCHAR2(500) | Y |  |  |  |
| 9 | USER_REG_ID | 유저 승인자ID | VARCHAR2(100) | Y |  |  |  |
| 10 | USER_REG_IP | BQMS측 LOG_VENDORUSER_REQ(업체사용자등록IP)의 USE_IP(사용IP)임. 즉 업체사용자가 사용자등록메뉴를 사용한IP임. 임직원의 승인IP가 아님) | VARCHAR2(30) | Y |  |  |  |
| 11 | FIRST_REG_DATETIME | 최초등록일시 | DATE | Y |  |  |  |
| 12 | RECENT_LOGIN_IP | 최근 접속IP | VARCHAR2(50) | Y |  |  |  |
| 13 | LAST_LOGIN_IP | 최총 접속 IP | VARCHAR2(50) | Y |  |  |  |
| 14 | PASSWD_HK | 패스워드(암호화) | VARCHAR2(500) | Y |  |  |  |
| 15 | RN | 데이터구성시 필요한 컬럼_의미없음 | NUMBER | Y |  |  |  |
| 16 | TOT_CNT | 데이터구성시 필요한 컬럼_의미없음 | NUMBER | Y |  |  |  |
| 17 | LAST_EXRC | 최종추출월 | CHAR(6) | Y |  |  |  |
| 18 | CREATE_DT | 적재일시_갱신및추가작업일시 | DATE | Y |  |  |  |
| 19 | DIV_COCD | A1 CE/IM(본사) ,B1 한국총괄, B2 중국총괄, B3 삼성전자로지텍, B4 삼성전자판매, B5 삼성전자서비스 ,B6 삼성메디슨, CO: 공통, ZZ: 미분류 | CHAR(2) | Y |  |  |  |
| 20 | UPD_DT | 업데이트일시 | DATE | Y |  |  |  |
<!-- AUTO:END schema -->

# Joins
<!-- AUTO:BEGIN joins -->
(확정된 조인 없음. 조인 관계는 P4 에서 확정한다. 컬럼 표의 '조인후보' 참고)
<!-- AUTO:END joins -->

# T2S 힌트
(사람이 보완하거나 P7 에서 규칙 문서를 링크한다)

<!-- ES-REFLECT:BEGIN (add_info/es_index_generated.csv + DB grain 실측 2026-10-15) -->
### 그레인 (DB 실측 2026-10-15, 전체 스캔)
- 1행 단위: 사이트·사용자ID·최종추출월(LAST_EXRC) 단위 사용자 마스터 스냅샷 1건
- **업무 키 (유일성 확인)**: `LAST_LOGIN_IP`, `CREATE_DT`, `USER_ID` — greedy 탐색(500K 표본) + 전체 스캔 dup 0
### 유사 테이블 구분 (ES)
설명이 비슷한 테이블: TI_BQMS002_INFA_USER. 이 테이블에만 있는 컬럼: 행 번호 (의미 없음), 총 개수 (의미 없음), 최종 추출 월 (20컬럼)

<!-- ES-REFLECT:END -->
