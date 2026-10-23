---
type: Reference
title: 도메인 지식 출처 (add_info 이식)
description: "domains/ 문서의 원본(add_info/domain)과 이식 일시, 교정 사항."
tags: ['kind:reference']
status: draft
---

# 이식 내역 (2026-10-15)

- 원본: `add_info/domain/domain.json`(시스템·도메인별 프로세스·테이블 규칙), `add_info/domain/domain_table.json`(도메인→테이블 멤버십, 146건)
- 대상: `domains/<slug>.md` 11건, `domains/index.md`, `config/okf_build.yaml`의 `tags.domain_map`
- `domain` 태그는 사람이 직접 붙이지 않는다. config의 `domain_map`을 다음 재생성(`build_okf.py`) 시 테이블 문서에 자동 부여된다.

## 교정·제외 사항

- `TI_BQMS001_URV_FULL`: 번들(AIAGT 접근 범위)에 없음 — domains 문서에서 링크하지 않음.
- `TI_GPRF900`(domain_rule 본문): 오타. 실제 테이블은 `TI_GRPF900`.
- `domain_desc_rule`의 "(아래 이미지 n 참조)": 원본의 다이어그램 참조 문구로 이미지는 번들에 없음. 프로세스 설명 자체만 유효.
- 영업마케팅/업체정보, 영업마케팅/기준정보(마스터) 중 `domain_rule`이 비어 있는 도메인은 domain_table.json의 멤버십만 문서화.
- 도메인 slug는 소문자 ASCII (생성기 `slug()`가 한글 제거): bid-qt, mro, vendor, master-bqms, mkt-exp, sales, om-vendor, hr, fin-org, fin-master, om-master
- 테이블이 여러 도메인에 속할 수 있으나(예: TI_BQMS800 = 업체정보 + 입찰/견적) 태그는 1개. `TI_BQMS800` 계열은 vendor(벤더 마스터)로 배정. 다중 소속은 각 domains 문서의 테이블 목록에 둘 다 기록되어 있다.

## add_info/procedure (이식됨 → /references/scenarios.md)

감사 시나리오 추출 스크립트 38건(.prc/.sql)의 시나리오·감사포인트·참조테이블을 `/references/scenarios.md`로 이식. `t2s/examples/` 의 근거 원천. SQL 전문은 복제하지 않음. 공사 시나리오(90/91, SHR)는 참조 테이블이 접근 범위 밖이라 T2S 대상 아님.
