---
type: Query Guideline
title: soft-delete·유효기간·플레이스홀더
description: "has:soft-delete 테이블은 삭제 플래그 필터, has:validity-period는 기간 조건. 플레이스홀더 날짜값('00000000') 주의."
tags: ['t2s:rule']
status: draft
---

# 규칙

- frontmatter에 **`has:soft-delete`** 태그가 있으면 삭제 플래그 컬럼(문서 `# Schema` 표에서 확인, 예: `DEL_YN`, `USE_YN`) 필터를 조건에 포함한다. 플래그 값(Y/N 중 어느 쪽이 활성인지)은 문서 비고·T2S 힌트 또는 코드 문서로 확인.
- **`has:validity-period`** 태그가 있으면 유효기간 컬럼(시작/종료) 조건이 누락되면 **행이 증폭**된다. 질문이 특정 시점을 묻지 않으면 현재 유효 조건으로 한정하고 가정에 명시.
- **플레이스홀더 날짜**: `CONDITION_TO='00000000'` 같은 값은 "종료일 미정의"다. 기간 이탈·만료 분석 시 제외 필요 (예: TI_GRPB_DE_PAYMENT_REPORT T2S 힌트).
- 플레이스홀더 금액도 동일: 계약금액 1.0/10,000 (TI_GRPF005)처럼 비율 계산 전 필터 필요.

# 예외

- 삭제 플래그를 걸면 결과가 0행이 되는 경우: 플래그 값 해석이 반대일 수 있음. 둘 다 시도하고 어느 쪽이 정상 데이터인지 표본으로 확인 후 가정에 기록.
