---
type: Code Column
title: TI_BQMS005_INFA_QT 코드값 (실측)
description: '견적집계 QT상태 — 한글 라벨 자체 저장 (코드 아님).'
tags: ['kind:code-column', 'owner:appadamsuser']
table: /schemas/APPADAMSUSER/tables/TI_BQMS005_INFA_QT.md
sources:
- id: llm-wiki
  resource: /references/llm-wiki-import.md
  title: llm wiki 실측 이식 (2026-10-07 DB 조회)
status: draft
---

# QT상태 (견적 상태)

입찰(`TI_BQMS004_INFA_BD.PROGRESS_STATUS`)과 달리 **한글 라벨 자체**가 저장됨 (코드 아님, 2026-10-07 DB 조회 확인). 코드 테이블 조인 불필요.

2026년 데이터에서 관찰된 값:

| 값 | 비고 |
|---|---|
| 견적요청 |  |
| 요청저장 |  |
| 결과저장 |  |
| 선정결재중 |  |
| 선정완료 |  |
| 선정마감 |  |
| NULL |  |
