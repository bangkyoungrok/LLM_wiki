---
type: Reference
title: 태그 사전
description: 번들에서 쓰는 태그 네임스페이스와 허용 값.
tags: [reference]
generated:
  by: process:okf-dict-builder/0.1
  at: 2026-10-13T13:53:08+09:00
---

# 개요
태그 허용 어휘다. validate_okf.py 가 이 어휘로 태그를 검사한다.

# 태그 사전
<!-- AUTO:BEGIN vocab -->
| 네임스페이스 | 허용 값 | 설명 |
|---|---|---|
| kind | `table`, `view`, `mview` | 객체 유형 (ALL_OBJECTS) |
| owner | `appadamsuser`, `setadamsuser` | 소유 스키마 (소문자, 밑줄은 하이픈) |
| class | `master`, `code`, `transaction`, `detail`, `history`, `mapping`, `summary`, `interface`, `view`, `unknown` | 테이블 분류 (table_class 필드와 동일) |
| size | `xs`, `s`, `m`, `l`, `xl`, `unknown` | NUM_ROWS 구간. xs<1만, s<100만, m<1천만, l<1억, xl>=1억, 통계 없으면 unknown |
| part | `partitioned` | 파티션 테이블 |
| access | `select-full`, `select-partial` | AIAGT 권한: 전체 컬럼 / 일부 컬럼만 SELECT |
| has | `pk`, `unique-key`, `soft-delete`, `validity-period`, `amount`, `pii`, `code-column`, `lob` | 컬럼 기반 기능 유무 |
| quality | `no-pk`, `no-comment`, `no-column-comment`, `stale-stats`, `invalid-object` | 품질 경고 (검토 큐 입력) |
| domain | `bid-qt`, `fin-master`, `fin-org`, `hr`, `master-bqms`, `mkt-exp`, `mro`, `om-master`, `om-vendor`, `sales`, `vendor` | 업무 도메인 (config 의 domain_map 에 매핑된 경우만) |
| join | `fk-declared`, `view-derived`, `index-inferred`, `name-inferred`, `comment-inferred`, `manual` | 조인 근거 (조인 concept) |
| card | `1-1`, `n-1`, `n-m` | 카디널리티 자식→부모 (조인 concept) |
| conf | `high`, `medium`, `low` | 조인 신뢰도 (조인 concept) |

- 형식은 `네임스페이스:값` (소문자, 하이픈). 문서당 최대 12개.
- 새 값이 필요하면 config 의 `tags.vocab_extra` 에 먼저 추가한다.
- 관리 네임스페이스(kind, owner, class, size, part, access, has, quality, domain)의 태그만 생성기가 다시 계산한다. 그 밖의 태그는 보존한다.
<!-- AUTO:END vocab -->
