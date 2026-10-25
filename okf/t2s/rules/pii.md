---
type: Query Guideline
title: PII·민감 컬럼
description: "has:pii 태그 또는 비고 PII 컬럼은 SELECT 목록에 넣지 않는다. 필요 시 COUNT/집계만."
tags: ['t2s:rule']
status: draft
---

# 규칙

- frontmatter에 **`has:pii`** 태그가 있거나 `# Schema` 표 비고에 **PII**로 표시된 컬럼(주소, 전화번호, 이메일, 계좌번호, 주민등록번호, IP, 이메일 등)은 **SELECT 목록에 넣지 않는다**.
- PII가 조건에 꼭 필요하면(예: 특정 이메일로 검색) WHERE에만 쓰고 SELECT에는 포함하지 않는다.
- 집계·존재 확인이 목적이면 `COUNT(*)`, `COUNT(DISTINCT col)`으로만 사용.
- 결과 값은 채팅으로 바로 전달되므로, 행 데이터에 민감 값이 섞이는 SELECT를 만들지 않는다.

# 예외

- 감사 시나리오에서 IP(제출IP)가 분석 대상인 경우: IP 자체는 `has:pii` 비고가 없는 컬럼인지 문서에서 확인한 뒤 사용. 비고 PII로 표시되어 있으면 제외하고 집계 수준으로 대체.
