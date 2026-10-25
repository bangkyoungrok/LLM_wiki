---
type: Oracle Table
title: DB테이블 스페이스 사용현황(날짜별)
description: DB테이블 스페이스 사용현황(날짜별).
resource: oracle://PRD/SETADAMSUSER/TI_CMMT001
tags: ['kind:table', 'owner:setadamsuser', 'class:summary', 'size:xs', 'access:select-full', 'quality:no-pk']
owner: SETADAMSUSER
table_name: TI_CMMT001
query_name: SETADAMSUSER.TI_CMMT001
table_class: summary
row_count: 3900
last_analyzed: 2026-08-04
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
| 1 | REG_NO | 등록순번 | NUMBER | N |  |  |  |
| 2 | STD_DT | 기준일자 | VARCHAR2(8) | N |  |  |  |
| 3 | DB_USER | DB유저 | VARCHAR2(30) | N |  |  |  |
| 4 | TABLESPACE_NAME | 테이블스페이스명 | VARCHAR2(30) | N |  |  |  |
| 5 | TOTAL_GB | 전체용량(GB) | NUMBER | Y |  |  |  |
| 6 | USE_GB | 사용량(GB) | NUMBER | Y |  |  |  |
| 7 | FREE_GB | 잔여량(GB) | NUMBER | Y |  |  |  |
| 8 | USE_RATIO | 사용율(%) | NUMBER | Y |  |  |  |
| 9 | CNTS | 비고 | VARCHAR2(100) | Y |  |  |  |
| 10 | REGISTER_ID | 등록자ID | VARCHAR2(30) | Y |  |  |  |
| 11 | REGISTER_DT | 등록일시 | DATE | Y |  |  |  |
| 12 | MODIFIER_ID | 수정자ID | VARCHAR2(30) | Y |  |  |  |
| 13 | MODIFIER_DT | 수정일시 | DATE | Y |  |  |  |
<!-- AUTO:END schema -->

# Joins
<!-- AUTO:BEGIN joins -->
(확정된 조인 없음. 조인 관계는 P4 에서 확정한다. 컬럼 표의 '조인후보' 참고)
<!-- AUTO:END joins -->

# T2S 힌트
(사람이 보완하거나 P7 에서 규칙 문서를 링크한다)

<!-- ES-REFLECT:BEGIN (add_info/es_index_generated.csv + DB grain 실측 2026-10-15) -->
### 그레인 (DB 실측 2026-10-15)
- 1행 단위: 날짜(STD_DT)·DB유저(DB_USER)·테이블스페이스(TABLESPACE_NAME) 단위 용량 사용 실적 1건
- **업무 키 (유일성 확인)**: `STD_DT`, `DB_USER`, `TABLESPACE_NAME` — ROWNUM<=500K 표본 distinct=전체 (유일)
<!-- ES-REFLECT:END -->
