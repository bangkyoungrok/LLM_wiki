---
type: Code Column
title: TI_GRPF830.CRCR_KDCD (실측)
description: "신용카드사용내역 카드구분. COMMENT(A:개인,B:법인)와 실데이터(한글) 불일치."
tags: ['kind:code-column', 'owner:appadamsuser']
table: /schemas/APPADAMSUSER/tables/TI_GRPF830.md
sources:
- id: llm-wiki
  resource: /references/llm-wiki-import.md
  title: llm wiki 실측 이식 (2026-10-05 DEV 실측)
status: draft
---

# CRCR_KDCD (카드구분)

| 값 | 의미 |
|---|---|
| 개인 | 개인카드 (실측 2026-10-05, DEV: 2,496,793행) |
| 법인 | 법인카드 (실측 2026-10-05, DEV: 1,002,744행) |

- **DB 컬럼 COMMENT는 "A:개인, B:법인"이라고 되어 있으나 실데이터는 한글 '개인'/'법인' 값** ('A'/'B' 값 0건). WHERE 조건은 실데이터 값으로 작성할 것.
