---
type: Oracle Table
title: DB테이블/인덱스 리스트(날짜별)(ALL)
description: DB테이블/인덱스 리스트(날짜별)(ALL).
resource: oracle://PRD/SETADAMSUSER/TI_CMMT002
tags: ['kind:table', 'owner:setadamsuser', 'class:history', 'size:xs', 'access:select-full', 'has:soft-delete', 'quality:no-pk']
owner: SETADAMSUSER
table_name: TI_CMMT002
query_name: SETADAMSUSER.TI_CMMT002
table_class: history
row_count: 6584
last_analyzed: 2026-07-23
status: draft
stale_after: 2027-01-11T13:53:08+09:00
sources:
- id: dict
  resource: /references/dictionary-sources.md
  title: 딕셔너리 추출 스냅샷
generated:
  by: process:okf-dict-builder/0.1
  at: 2026-10-13T13:53:08+09:00
table_type: 기준정보
business_area: 시스템
business_detail: 시스템관리
---

# 개요
(사람이 보완: 업무 의미, 생성 시점, 주의 사항)

# Schema
<!-- AUTO:BEGIN schema -->
| # | 컬럼 | 한글명 | 타입 | NULL | 키 | 코드/참조 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | STD_DT | 기준일자 | VARCHAR2(8) | N | IDX |  |  |
| 2 | OWNER | DB유저명 | VARCHAR2(20) | N |  |  |  |
| 3 | TABLESPACE_NAME | 테이블스페이스명 | VARCHAR2(30) | Y |  |  |  |
| 4 | TABLE_ID | 테이블ID | VARCHAR2(200) | N | IDX |  |  |
| 5 | TABLE_TYPE | 테이블타입(테이블/테이블파티션/인덱스/인덱스파티션) | VARCHAR2(20) | Y |  |  |  |
| 6 | SEGMENT_ID | SEGMENT ID(테이블/인덱스ID) | VARCHAR2(200) | N |  |  |  |
| 7 | PARTITION_NAME | 파티션명 | VARCHAR2(200) | Y |  |  |  |
| 8 | TABLE_NM | 테이블명 | VARCHAR2(2000) | Y |  |  |  |
| 9 | GB1 | 구분 | VARCHAR2(100) | Y |  |  |  |
| 10 | GB2 | 분야 | VARCHAR2(100) | Y |  |  |  |
| 11 | GB3 | 담당자 | VARCHAR2(100) | Y |  |  |  |
| 12 | GB4 | 주기 | VARCHAR2(100) | Y |  |  |  |
| 13 | GB5 | 테이블내용 | VARCHAR2(2000) | Y |  |  |  |
| 14 | TABLE_SIZE | 테이블크기(MB) | NUMBER | Y |  |  |  |
| 15 | TABLE_SIZE_SUM | 테이블+인덱스 크기 합계(MB) | NUMBER | Y |  |  |  |
| 16 | PARTITION_YN | 파티션여부(O) | VARCHAR2(20) | Y |  |  |  |
| 17 | COMPRESS_YN | 압축여부(O) | VARCHAR2(20) | Y |  |  |  |
| 18 | COMPRESS_LEVEL | 압축방식 | VARCHAR2(100) | Y |  |  |  |
| 19 | CHARGE | 운영담당자 | VARCHAR2(100) | Y |  |  |  |
| 20 | USE_YN | 사용여부(운영,백업용) | VARCHAR2(20) | Y |  |  |  |
| 21 | EXPORT_YN | EXPORT백업대상여부 | VARCHAR2(20) | Y |  |  |  |
| 22 | SUMMARY_YN | 요약표시여부(Y) | VARCHAR2(20) | Y |  |  |  |
| 23 | CNTS | 비고 | VARCHAR2(4000) | Y |  |  |  |
| 24 | REGISTER_ID | 등록자ID | VARCHAR2(30) | Y |  |  |  |
| 25 | REGISTER_DT | 등록일시 | DATE | Y |  |  |  |
| 26 | MODIFIER_ID | 수정자ID | VARCHAR2(30) | Y |  |  |  |
| 27 | MODIFIER_DT | 수정일시 | DATE | Y |  |  |  |
<!-- AUTO:END schema -->

# Joins
<!-- AUTO:BEGIN joins -->
(확정된 조인 없음. 조인 관계는 P4 에서 확정한다. 컬럼 표의 '조인후보' 참고)
<!-- AUTO:END joins -->

# T2S 힌트
(사람이 보완하거나 P7 에서 규칙 문서를 링크한다)

<!-- ES-REFLECT:BEGIN (add_info/es_index_generated.csv + DB grain 실측 2026-10-15) -->### 그레인 (DB 실측 2026-10-16, 키 비유일 — 전체 스캔)
- 1행 단위: 기준일자(STD_DT) + 테이블/인덱스 식별자(TABLE_ID) 단위 1건
- 키 후보 `STD_DT, TABLE_ID, TABLE_SIZE_SUM, TABLE_SIZE, TABLE_NM, REGISTER_DT, PARTITION_NAME, TABLE_TYPE, COMPRESS_LEVEL, USE_YN` — 전체 스캔(무제한)에서도 비유일 (dup 238272 (1차 후보 dup 1355986 → 238272)).
  1:N 관계 또는 그레인이 16컬럼 초과. 집계/JOIN 시 추가 식별 컬럼 확인 필요.
<!-- ES-REFLECT:END -->
