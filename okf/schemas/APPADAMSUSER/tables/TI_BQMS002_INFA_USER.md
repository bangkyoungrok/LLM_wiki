---
type: Oracle Table
title: BQMS 사내외 사용자마스타
description: BQMS 사내외 사용자마스타.
resource: oracle://PRD/APPADAMSUSER/TI_BQMS002_INFA_USER
tags: ['kind:table', 'owner:appadamsuser', 'class:master', 'size:unknown', 'access:select-full', 'quality:no-pk', 'quality:stale-stats', 'domain:master-bqms']
owner: APPADAMSUSER
table_name: TI_BQMS002_INFA_USER
query_name: APPADAMSUSER.TI_BQMS002_INFA_USER
table_class: master
status: draft
stale_after: 2027-01-11T13:53:08+09:00
sources:
- id: dict
  resource: /references/dictionary-sources.md
  title: 딕셔너리 추출 스냅샷
generated:
  by: process:okf-dict-builder/0.1
  at: 2026-10-13T13:53:08+09:00
table_type: 인터페이스
business_area: BQMS
business_detail: 사용자정보
---

# 개요
(사람이 보완: 업무 의미, 생성 시점, 주의 사항)

# Schema
<!-- AUTO:BEGIN schema -->
| # | 컬럼 | 한글명 | 타입 | NULL | 키 | 코드/참조 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | 사내외구분 | 사내외구분 | VARCHAR2(9) | Y |  |  |  |
| 2 | SITE_CODE | 사이트코드 | VARCHAR2(20) | Y |  |  |  |
| 3 | USER_ID | 사용자ID | VARCHAR2(100) | Y |  |  |  |
| 4 | ACTIVE_FLAG | 사용여부 | VARCHAR2(10) | Y |  |  |  |
| 5 | USER_NAME | 사용자명 | VARCHAR2(300) | Y |  |  |  |
| 6 | COMP_CODE | 업체코드 | VARCHAR2(100) | Y |  |  |  |
| 7 | COMP_NAME | 업체명 | VARCHAR2(200) | Y |  |  |  |
| 8 | EN_COMP_NAME | 영문업체명 | VARCHAR2(500) | Y |  |  |  |
| 9 | USER_REG_ID | 사용승인자ID | VARCHAR2(100) | Y |  |  |  |
| 10 | USER_REG_IP | 유저 등록IP | VARCHAR2(100) | Y |  |  |  |
| 11 | FIRST_REG_DATETIME | 사용승인일시 | DATE | Y |  |  |  |
| 12 | RECENT_LOGIN_IP | 최근 접속IP | VARCHAR2(50) | Y |  |  |  |
| 13 | LAST_LOGIN_IP | 최총 접속 IP | VARCHAR2(50) | Y |  |  |  |
| 14 | PASSWD_HK | 패스워드(암호화) | VARCHAR2(500) | Y |  |  |  |
| 15 | LOAD_DT | 적재일시 | DATE | Y |  |  |  |
| 16 | DIV_COCD | A1 CE/IM(본사) ,B1 한국총괄, B2 중국총괄, B3 삼성전자로지텍, B4 삼성전자판매, B5 삼성전자서비스 ,B6 삼성메디슨, CO: 공통, ZZ: 미분류 | CHAR(2) | Y |  |  |  |
| 17 | RECENT_LOGIN_PROXY_IP | RECENT_LOGIN_PROXY_IP | VARCHAR2(15) | Y |  |  |  |
| 18 | LAST_LOGIN_PROXY_IP | LAST_LOGIN_PROXY_IP | VARCHAR2(15) | Y |  |  |  |
<!-- AUTO:END schema -->

# Joins
<!-- AUTO:BEGIN joins -->
(확정된 조인 없음. 조인 관계는 P4 에서 확정한다. 컬럼 표의 '조인후보' 참고)
<!-- AUTO:END joins -->

# T2S 힌트
(사람이 보완하거나 P7 에서 규칙 문서를 링크한다)

<!-- ES-REFLECT:BEGIN (add_info/es_index_generated.csv + DB grain 실측 2026-10-15) -->### 그레인 (DB 실측 2026-10-16, 중복 적재 의심 — 데이터 관리 이슈)
- 1행 단위: 사이트(SITE_CODE)별 사용자(USER_ID) 계정 1건
- 업무 키 후보 `USER_ID` — 전체 스캔(무제한)으로도 비유일 (dup 382140).
- 적재 메타(LOAD_DT/LOAD_DTTM) 포함 시에만 유일 — **중복 적재(재적재) 흔적**, 데이터 관리 담당에 재검토 요청 필요.
### 유사 테이블 구분 (ES)
설명이 비슷한 테이블: TI_BQMS003_SYS_USE_MST_HISTORY. 이 테이블에만 있는 컬럼: 최근 접속 프록시 IP, 최종 접속 프록시 IP (18컬럼)

<!-- ES-REFLECT:END -->
