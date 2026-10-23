---
type: Code Column
title: TI_BQMS004_INFA_BD 코드값 (실측)
description: '입찰집계 코드 컬럼 실측값. PROGRESS_STATUS(BD_PROGRESS), NOT_SELECT_REASON_YN, 선정여부/비최저가.'
tags: ['kind:code-column', 'owner:appadamsuser']
table: /schemas/APPADAMSUSER/tables/TI_BQMS004_INFA_BD.md
sources:
- id: llm-wiki
  resource: /references/llm-wiki-import.md
  title: llm wiki 실측 이식 (2026-10-07 DB 조회)
status: draft
---

# PROGRESS_STATUS (진행상태)

코드값 저장. 의미는 `SETADAMSUSER.TC_CF_COMM_CODE` (`CODE_ID='BD_PROGRESS'`, 삭제 플래그 `DELETE_YN='0'`=미삭제)의 KO_LABEL. 2026-10-07 DB 조회 확인한 값 22종:

| 값 | 의미 (KO_LABEL) |
|---|---|
| BIDS001 | 낙찰 |
| BDDO001 | 입찰진행중 |
| BDDO002 | 입찰마감 |
| BDDO003 | 입찰 취소 |
| BDDO004 | 입찰 취소 기안 |
| BDDR001 | 유찰 |
| BDDR004 | 폐찰완결 |
| BDDR005 | Activity 취소 |
| NEGO001 | 견적협의중 |
| EVA1011 | 평가진행 |
| EVA3031 | 평가결과 저장 |
| EVA3032 | 평가결과 기안 |
| EVA3033 | 평가결과 반려 |
| EVA3034 | 평가결과 완결 |
| NOTI001 | 공고 저장 |
| NOTI002 | 공고 기안 |
| NOTI003 | 공고 반려 |
| NOTI007 | 공고변경 |
| PRES001 | 설명회 저장 |
| IRPA001 | 과제품의중 |
| CNPR001 | 공사의뢰취소 |
| QNA0001 | 질의응답 저장 |

- 국문명 조인 필요 시: `TI_BQMS006_COMMCODE` (`COMM_CODE_TYPE_CODE='BD_PROGRESS'`) 또는 공통코드 테이블.

# NOT_SELECT_REASON_YN (최저가 미선정 여부)

| 값 | 의미 |
|---|---|
| Y | 최저가 미선정 (사유는 `NOT_SELECT_REASON_DESC` 자유 텍스트) |
| N | 최저가 미선정 아님 |

- 2026-10-07 실측 (2026년 입찰): Y 2,851행(고유 REQ_NO 476건) / N 294,094행.
- 사유는 요청자 자유 텍스트(한/영/아랍어 등)로 일부 건은 플래그와 불일치 (YN='Y'인데 사유에 "선정업체가 최저가" 기술). 감사 활용 시 사유 본문 교차 확인 필요.

# 선정여부 / 비최저가 (선정·최저가 플래그)

2026-10-07 실측 (2026년 입찰 데이터):

| 컬럼 | 값 | 의미 |
|---|---|---|
| `선정여부` | 'Y' | 해당 행 업체가 선정됨 |
| `선정여부` | NULL | 미선정 (**'N' 값 없음**) |
| `비최저가` | 'Y' | 비최저가 플래그 (선정된 비최저가 업체 행에 설정됨) |
| `비최저가` | NULL | 미설정 (**'N' 값 없음 — "최저가" 의미로 쓰면 안 됨**) |

- **"최저가가 아닌 업체가 선정"된 행** = `NOT_SELECT_REASON_YN='Y' AND 비최저가='Y' AND 선정여부='Y'` (2026: 696행 / 469건)
- 품목 최저가(`MIN(제출단가)`)에 플레이스홀더 가격(1, 0.01, 2 등)이 섞여 있어 가격 프리미엄 계산 시 `MIN(제출단가) >= 100` 필터 권장. 최저가 업체 측 입력 오류("wrong amount", "shifted one digit" 등)가 사유 본문에 자주 언급됨.
