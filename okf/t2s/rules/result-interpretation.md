---
type: Query Guideline
title: 결과 해석 (VPD·마스킹·0행)
description: "VPD/마스킹 정책으로 결과가 예상보다 적을 수 있다. 0행·이상 결과의 해석 순서."
tags: ['t2s:rule']
status: draft
---

# 규칙

- **VPD(View Private Data)·마스킹**: AIAGT 계정에 보안 정책이 적용되어 같은 SQL이라도 로그인 사용자 기준으로 **예상보다 적은 행**이 반환되거나 값이 마스킹(`********`)될 수 있다. 행 수가 스키마 통계 대비 비정상적으로 적으면 이 가능성을 **확인 필요** 항목으로 명시한다.
- **0행 결과** 해석 순서:
  1. 조건 오타/값 형식 (문자열 날짜 형식, 코드값 vs 한글 라벨 — /codes/ 문서 확인)
  2. soft-delete 플래그 방향, 유효기간 조건
  3. VPD/권한 (access:select-partial이면 일부 컬럼만 조회 가능)
  4. 실제로 데이터가 없는 경우
- **코드값 vs 라벨 혼동**: 같은 컬럼이라도 코드(BDDO001) 저장인지 한글 라벨(입찰진행중) 저장인지 /codes/ 문서와 T2S 힌트로 반드시 확인 (예: TI_BQMS004.PROGRESS_STATUS=코드, TI_BQMS005.QT상태=한글).
- 플레이스홀더 값(금액 1/10,000, 날짜 '00000000')이 결과에 섞이면 필터를 추가해 재실행 (soft-delete-validity 규칙).
- DEV/PRD 차이: 번들 실측이 DEV 기준인 값은 /references/llm-wiki-import.md 확인 — PRD에서는 다를 수 있음을 가정에 명시.

# 예외

없음.
