---
type: Oracle Table
title: 쿼리툴 plan테이블
description: 쿼리툴 plan테이블.
resource: oracle://PRD/SETADAMSUSER/PLAN_TABLE
tags: ['kind:table', 'owner:setadamsuser', 'class:transaction', 'size:xs', 'access:select-full', 'has:amount', 'has:lob', 'quality:no-pk', 'quality:no-column-comment']
owner: SETADAMSUSER
table_name: PLAN_TABLE
query_name: SETADAMSUSER.PLAN_TABLE
table_class: transaction
row_count: 116
last_analyzed: 2026-06-10
status: draft
stale_after: 2027-01-11T13:53:08+09:00
sources:
- id: dict
  resource: /references/dictionary-sources.md
  title: 딕셔너리 추출 스냅샷
generated:
  by: process:okf-dict-builder/0.1
  at: 2026-10-13T13:53:08+09:00
---

# 개요
(사람이 보완: 업무 의미, 생성 시점, 주의 사항)

# Schema
<!-- AUTO:BEGIN schema -->
| # | 컬럼 | 한글명 | 타입 | NULL | 키 | 코드/참조 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | STATEMENT_ID |  | VARCHAR2(30) | Y |  |  |  |
| 2 | PLAN_ID |  | NUMBER | Y |  |  |  |
| 3 | TIMESTAMP |  | DATE | Y |  |  |  |
| 4 | REMARKS |  | VARCHAR2(4000) | Y |  |  |  |
| 5 | OPERATION |  | VARCHAR2(30) | Y |  |  |  |
| 6 | OPTIONS |  | VARCHAR2(255) | Y |  |  |  |
| 7 | OBJECT_NODE |  | VARCHAR2(128) | Y |  |  |  |
| 8 | OBJECT_OWNER |  | VARCHAR2(128) | Y |  |  |  |
| 9 | OBJECT_NAME |  | VARCHAR2(128) | Y |  |  |  |
| 10 | OBJECT_ALIAS |  | VARCHAR2(65) | Y |  |  |  |
| 11 | OBJECT_INSTANCE |  | NUMBER | Y |  |  |  |
| 12 | OBJECT_TYPE |  | VARCHAR2(30) | Y |  |  |  |
| 13 | OPTIMIZER |  | VARCHAR2(255) | Y |  |  |  |
| 14 | SEARCH_COLUMNS |  | NUMBER | Y |  |  |  |
| 15 | ID |  | NUMBER | Y |  |  |  |
| 16 | PARENT_ID |  | NUMBER | Y |  |  |  |
| 17 | DEPTH |  | NUMBER | Y |  |  |  |
| 18 | POSITION |  | NUMBER | Y |  |  |  |
| 19 | COST |  | NUMBER | Y |  |  |  |
| 20 | CARDINALITY |  | NUMBER | Y |  |  |  |
| 21 | BYTES |  | NUMBER | Y |  |  |  |
| 22 | OTHER_TAG |  | VARCHAR2(255) | Y |  |  |  |
| 23 | PARTITION_START |  | VARCHAR2(255) | Y |  |  |  |
| 24 | PARTITION_STOP |  | VARCHAR2(255) | Y |  |  |  |
| 25 | PARTITION_ID |  | NUMBER | Y |  |  |  |
| 26 | OTHER |  | LONG | Y |  |  |  |
| 27 | DISTRIBUTION |  | VARCHAR2(30) | Y |  |  |  |
| 28 | CPU_COST |  | NUMBER | Y |  |  |  |
| 29 | IO_COST |  | NUMBER | Y |  |  |  |
| 30 | TEMP_SPACE |  | NUMBER | Y |  |  |  |
| 31 | ACCESS_PREDICATES |  | VARCHAR2(4000) | Y |  |  |  |
| 32 | FILTER_PREDICATES |  | VARCHAR2(4000) | Y |  |  |  |
| 33 | PROJECTION |  | VARCHAR2(4000) | Y |  |  |  |
| 34 | TIME |  | NUMBER | Y |  |  |  |
| 35 | QBLOCK_NAME |  | VARCHAR2(128) | Y |  |  |  |
| 36 | OTHER_XML |  | CLOB | Y |  |  |  |
<!-- AUTO:END schema -->

# Joins
<!-- AUTO:BEGIN joins -->
(확정된 조인 없음. 조인 관계는 P4 에서 확정한다. 컬럼 표의 '조인후보' 참고)
<!-- AUTO:END joins -->

# T2S 힌트
(사람이 보완하거나 P7 에서 규칙 문서를 링크한다)
### 그레인 (DB 실측 2026-10-16, 키 비유일 — 전체 스캔)
- 키 후보 `ID` — 어떤 식별 컬럼을 추가해도 dup 불변 (전체 스캔 dup 38).
  완전 복제행(이력·스냅샷) 또는 자연스러운 1:N 관계. 집계/JOIN 시 DISTINCT 또는 최신값(RN=1) 처리 필요.
