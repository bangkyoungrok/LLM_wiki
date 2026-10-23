---
type: Reference
title: llm wiki 실측 지식 이식 출처
description: 'D:\workspace\llm\wiki (별도 작성)에서 이식한 실측 코드값·질의 노트의 출처와 실측 일시.'
tags: ['kind:reference']
status: draft
---

# 이식 내역 (2026-10-15)

별도로 작성된 `D:\workspace\llm\wiki` 번들에서 DB 실측 기반 지식만 okf로 이식했다. 원본의 스키마 구조 문서(테이블 컬럼, INDEX)는 이 번들의 `schemas/`가 정본이므로 이식하지 않았다.

| okf 문서 | 원본 위치 | 실측 일시 (원본 기재) |
|---|---|---|
| /codes/TI_BQMS004_INFA_BD.md | wiki codes.md | 2026-10-07 DB 조회 |
| /codes/TI_BQMS005_INFA_QT.md | wiki codes.md | 2026-10-07 DB 조회 |
| /codes/TI_GRPF830__CRCR_KDCD.md | wiki codes.md + TI_GRPF830 질의 노트 | 2026-10-05 DEV 실측 |
| /glossary/index.md (SEUK) | wiki glossary.md | 2026-10-05 DB 조회 |
| TI_GRPB_DE_PAYMENT_REPORT T2S 힌트 | wiki join-hints.md + 테이블 질의 노트 | 2026-10-05 DB 실측 |
| TI_BQMS004_INFA_BD T2S 힌트 | wiki join-hints.md | 2026-10-07 DB 조회 |
| TI_BQMS005_INFA_QT T2S 힌트 | wiki join-hints.md | 2026-10-07 DB 조회 |
| TI_GRPF830 / TI_GRPF005 / TI_GRPF003 / TI_GSCM009 T2S 힌트 | wiki 테이블 질의 노트 | 2026-10-05 DEV 실측 |

- 원본은 DEV 환경 실측임을 각 문서에 그대로 표기했다. PRD 실측으로 재확인 전까지는 참고 수준으로 쓰라.
- 원본에 있던 `AUDIT.*` 스키마 예제·용어는 존재하지 않는 스키마라 이식하지 않았고, 2026-10-15 원본에서 제거했다.
