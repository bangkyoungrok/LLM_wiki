# 이 환경의 값

이 환경에서만 쓰는 이름과 예시다. 다른 Wiki 파일은 이 파일의 값을 가져다 쓴다.

## schema 경로

| 스키마 | 내용 | 경로 |
|---|---|---|
| `APPADAMSUSER` | 업무 데이터 | `okf/schemas/APPADAMSUSER/index.md`, `okf/schemas/APPADAMSUSER/tables/<TABLE>.md` |
| `SETADAMSUSER` | 감사 메타 | `okf/schemas/SETADAMSUSER/index.md` |

질문의 거래 테이블은 `APPADAMSUSER` 에서 찾는다.

## 패턴 번호

| 종류 | 번호 | 목록 |
|---|---|---|
| 부정 패턴 | P-001 ~ P-032 | `okf/wiki/patterns/fraud/index.md` |
| 이상징후 패턴 | P-101 ~ P-141 | `okf/wiki/patterns/anomaly/index.md` |
| 드릴다운 패턴 | DP-001 ~ DP-023 | `okf/wiki/patterns/perspective/index.md` |

## 사고 유형

drilldown 이 쓰는 7개 유형이다. 분류 기준과 유형별로 먼저 보는 패턴은 `okf/wiki/patterns/perspective/index.md` 2절에 있다.

| 번호 | 유형 |
|---|---|
| ① | 횡령/사적 유용 |
| ② | 업체 유착/특혜 |
| ③ | 프로세스 악용 |
| ④ | 검증부실/과다지급 |
| ⑤ | 사외펀드/예산전용 |
| ⑥ | 편법지원/과소충당 |
| ⑦ | 정책/시스템 통제 미흡 |

## 출력 예시

### top-down

```json
{
  "schema_version": "1.0",
  "question": "2025-11-01부터 2026-10-31까지 영업마케팅 매출(출고→빌링→반품·정정) 영역에서, 출고 기록 없이 빌링이 생성되었거나 기간 말 빌링이 다음 기간 초 반품·정정으로 되돌아간 거래를 찾을 수 있는 부정 위험 시나리오를 만들어줘. 출고·청구·반품 흐름이 서로 맞지 않는 경우를 함께 보고, 정상적인 서비스 품목 청구나 사유가 기록된 반품은 제외해줘.",
  "mode": "top-down",
  "scope": {
    "domain_name": "영업마케팅 매출",
    "domain_slug": "sales",
    "business_area": "영업마케팅",
    "business_process": "SO > DO > GI > 빌링/Invoice > 수금",
    "period": { "start": "2025-11-01", "end": "2026-10-31", "basis": "직전 달 말일까지 12개월" }
  },
  "risk_theme": {
    "summary": "출고(GI) 기록 없이 청구(빌링)되었거나, 기간 말 빌링이 다음 기간 초 반품·정정으로 되돌아간 매출 조작 의심 거래",
    "pattern_ids": ["P-027", "P-028"],
    "pattern_names": ["허위 출고", "매출 Inflation"],
    "real_cases": ["CS-034", "CS-043"]
  },
  "intent": "출고·청구·반품 흐름이 서로 맞지 않는 거래를 찾는다",
  "expected_finding": "출고(D/O) 기록 없이 빌링이 생성되었거나, 기간 말 빌링이 원빌링 정보로 확인되는 반품·정정으로 되돌아간 거래",
  "grounding": {
    "primary_table": "APPADAMSUSER.TI_GRPB004B",
    "table_type": "리포트",
    "row_basis": "빌링번호(BILL_NO) + 빌링아이템(BILL_ITEM)",
    "date_column": "BILL_DT",
    "amount_column": "TAMT",
    "supporting_tables": ["APPADAMSUSER.TI_GRPB010"],
    "key_terms": [
      { "term": "빌링(청구·매출)", "column": "TI_GRPB004B.BILL_NO / BILL_DT / TAMT" },
      { "term": "출고(GI)", "column": "TI_GRPB004B.DO_NO / DO_DT (D/O 문서 대리 지표)" },
      { "term": "반품·정정", "column": "TI_GRPB004B.ORG_SO / ORG_BILL_DT (원빌링번호·원빌링일자)" }
    ]
  },
  "data_evidence": null,
  "variant": null,
  "duplicate_check": {
    "checked_against": "okf/wiki/examples/index.md",
    "similar_scenarios": [],
    "result": "신규"
  },
  "score": {
    "total": 10,
    "criteria": { "risk_link": 2, "data_feasibility": 2, "scope_clarity": 2, "detectability": 2, "novelty": 2 }
  },
  "rationale": "실제 사고(CS-034 허위 출고·실적 조작, CS-043 허위매출 계리)와 부정 패턴 2개(P-027·P-028)가 같은 출고→빌링→반품 흐름에 걸리고, 거래 테이블·기준 날짜·금액 컬럼이 문서로 확인된다. okf/wiki/examples/index.md 승인 목록은 비어 있어 신규(최종 중복 판정은 배치가 담당)."
}
```

### bottom-up

```json
{
  "schema_version": "1.0",
  "question": "2025-11-01부터 2026-10-31까지 영업마케팅 마케팅비(행사주문(EO) → 지급요청(PR) 정산)에서, 행사가 끝나기 전에 지급이 기표되었거나 행사 시작 전에 지급이 기표된 정산 건, 그리고 실제 정산 금액이 최초 계획 금액보다 큰 건, 그리고 같은 증빙 번호로 여러 지급요청에 연결된 건을 함께 찾아줘.",
  "mode": "bottom-up",
  "scope": {
    "domain_name": "영업마케팅 마케팅비",
    "domain_slug": "mkt-exp",
    "business_area": "영업마케팅",
    "business_process": "EO(행사주문) → PR(지급요청) → 정산",
    "period": { "start": "2025-11-01", "end": "2026-10-31", "basis": "직전 달 말일까지 12개월" }
  },
  "risk_theme": {
    "summary": "행사 종료 전 또는 시작 전에 지급된 마케팅비 정산, 최초 계획 금액을 크게 초과한 정산, 같은 증빙 번호의 반복 연결",
    "pattern_ids": ["P-111", "P-113", "P-129"],
    "pattern_names": ["선후 순서 위반", "비정상 단축", "분포 편차"],
    "real_cases": []
  },
  "intent": "마케팅비 정산 건의 시간 순서(행사 기간과 지급 시점)와 계획 대비 정산 금액, 증빙 연결이 서로 맞지 않는 거래를 찾는다",
  "expected_finding": "행사 종료일보다 앞선 시점에 지급이 기표되었거나, 행사 시작보다 앞서 지급된 정산 건, 최초 계획 금액 대비 크게 초과된 정산 건, 같은 인보이스 번호가 여러 지급요청에 매핑된 건",
  "grounding": {
    "primary_table": "APPADAMSUSER.TI_GRPF_EO_REPORT",
    "table_type": "리포트",
    "row_basis": "PRNUM + EONUM + PAYITEMNO + EOACTNO (문서 그레인, dup 269로 비유일 — 데이터 품질 문제 기록)",
    "date_column": "PRCRDT",
    "amount_column": "LTOTAMT",
    "supporting_tables": [],
    "key_terms": [
      { "term": "지급요청(PR) 생성일", "column": "TI_GRPF_EO_REPORT.PRCRDT" },
      { "term": "행사 종료일", "column": "TI_GRPF_EO_REPORT.PLENDT" },
      { "term": "행사 시작일", "column": "TI_GRPF_EO_REPORT.PLSTDT" },
      { "term": "정산금액", "column": "TI_GRPF_EO_REPORT.LTOTAMT" },
      { "term": "EO최초계획금액", "column": "TI_GRPF_EO_REPORT.EO_INIT_AMT" },
      { "term": "증빙(인보이스) 번호", "column": "TI_GRPF_EO_REPORT.IVNO" }
    ]
  },
  "bottom_up": {
    "starting_tables": ["APPADAMSUSER.TI_GRPF_EO_REPORT"],
    "related_tables": [],
    "expansion_path": "TI_GRPF_EO_REPORT(PRCRDT vs PLSTDT/PLENDT, LTOTAMT vs EO_INIT_AMT, IVNO) — 단일 테이블 내 시간·금액·증빙 신호 3종",
    "table_scope": "단일",
    "rationale": "EO/PR 정산 결합 리포트에서 지급 시점과 행사 기간의 순서, 최초 계획 대비 정산 금액, 증빙 번호의 연결 구조를 출발점 삼아 실적 없는 지급·허위 프로모션 의심 건으로 확장"
  },
  "variant": null,
  "duplicate_check": {
    "checked_against": "okf/wiki/examples/index.md",
    "similar_scenarios": [],
    "result": "신규"
  },
  "score": {
    "total": 8,
    "criteria": { "risk_link": 1, "data_feasibility": 1, "scope_clarity": 2, "detectability": 2, "novelty": 2 }
  },
  "rationale": "risk-interpretation 2절의 「행사 종료 전 지급, 1일짜리 프로모션, 예산 승인 전 행사가 잦음 → 실적 없는 지급·허위 프로모션(부정 의심)」 행과 P-111·P-113·P-129가 같은 EO→PR 정산 흐름에 연결되고, 거래 테이블·기준 날짜(PRCRDT)·금액(LTOTAMT)이 문서로 확인된다. risk-interpretation 행의 패턴 3개 중 2개만 포함해 위험 연결 1점, 그레인 dup 269(비유일)로 실현성 1점을 감점했다. 근거 문서: okf/schemas/APPADAMSUSER/tables/TI_GRPF_EO_REPORT.md, okf/domains/mkt-exp.md, okf/wiki/patterns/anomaly/index.md, okf/wiki/risk-interpretation.md, okf/wiki/examples/index.md, okf/glossary/index.md."
}
```

### drilldown

예시 상황: 기준 시나리오 「셀아웃 인센티브 과다지급」(top-down, 1단계 거래선/SKU 기준 누적 셀인 < 셀아웃 인센티브 지급수량)이 검증을 통과했다. 원본 질의와 결과는 예시 값이다.

첫 드릴다운(이전 드릴다운 없음, 초과가 같은 모델의 대표 SKU 와 일부 거래선에 몰림 → 진위 판별 먼저):

```json
{
  "proceed": true,
  "accident_type": "④ 검증부실/과다지급",
  "pattern_ids": [
    "DP-002",
    "DP-004"
  ],
  "perspective": "정산 단위·거래선 기준 보정 후 초과",
  "question": "2025-11-01부터 2026-10-31까지 영업마케팅 매출차감의 셀아웃 인센티브 정산 영역에서, 거래선이 공급받은 수량보다 많은 판매실적으로 인센티브를 청구해 과다 지급된 것으로 의심되는 거래를 찾을 수 있는 부정 위험 시나리오를 만들어줘.\n위 질의에 더해, 아래 관점으로 결과를 더 좁고 깊게 봐 줘.\n- 정산 단위·거래선 기준 보정 후 초과: 같은 모델의 다른 SKU 셀인과, 매핑에는 없지만 같은 지급처·사업자등록번호를 가진 주문처의 셀인까지 더해도 셀아웃이 셀인을 넘는 건만 남겨 줘. 거래선 인수·합병이나 코드 통폐합으로 갈린 셀인은 합산해 주고, 모델로 묶거나 매핑을 보정해 해소되는 건은 제외해 줘.",
  "reason": ""
}
```

두 번째 드릴다운(보고서에 「## 정산 단위·거래선 기준 보정 후 초과 관점으로 더 확인」 절이 있음 → 그 줄을 그대로 두고 이번 관점을 더함):

```json
{
  "proceed": true,
  "accident_type": "④ 검증부실/과다지급",
  "pattern_ids": [
    "DP-008"
  ],
  "perspective": "판매가능수량 최초 초과 지급 문서",
  "question": "2025-11-01부터 2026-10-31까지 영업마케팅 매출차감의 셀아웃 인센티브 정산 영역에서, 거래선이 공급받은 수량보다 많은 판매실적으로 인센티브를 청구해 과다 지급된 것으로 의심되는 거래를 찾을 수 있는 부정 위험 시나리오를 만들어줘.\n위 질의에 더해, 아래 관점으로 결과를 더 좁고 깊게 봐 줘.\n- 정산 단위·거래선 기준 보정 후 초과: 같은 모델의 다른 SKU 셀인과, 매핑에는 없지만 같은 지급처·사업자등록번호를 가진 주문처의 셀인까지 더해도 셀아웃이 셀인을 넘는 건만 남겨 줘. 거래선 인수·합병이나 코드 통폐합으로 갈린 셀인은 합산해 주고, 모델로 묶거나 매핑을 보정해 해소되는 건은 제외해 줘.\n- 판매가능수량 최초 초과 지급 문서: 남은 거래선·SKU 마다 컨디션 판매기간 종료일 기준으로 누적 셀인과 누적 셀아웃 지급수량을 비교해, 처음 초과가 생긴 지급 문서와 그 뒤에도 계속 지급된 문서만 남기고 문서별 초과 금액을 보여 줘. 판매기간 종료일과 셀인 사이가 통상 리드타임 안인 건은 제외해 줘.",
  "reason": ""
}
```

세 번째 드릴다운에서 멈출 때:

```json
{
  "proceed": false,
  "accident_type": "④ 검증부실/과다지급",
  "pattern_ids": [],
  "perspective": "",
  "question": "",
  "reason": "결과가 회입 대상 지급 문서 단위로 특정되어 감사인이 한 건씩 바로 볼 수 있으므로 더 좁히지 않는다."
}
```
