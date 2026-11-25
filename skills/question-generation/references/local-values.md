# 이 환경의 값

이 환경에서만 쓰는 이름과 예시다. 다른 Wiki 파일은 이 파일의 값을 가져다 쓴다.

## schema 경로

| 스키마 | 내용 | 경로 |
|---|---|---|
| `ADAMSUSER` | 업무 데이터 + 감사 메타(시나리오·결과·공통코드). 단일 OWNER | `okf/schemas/ADAMSUSER/index.md`, `okf/schemas/ADAMSUSER/tables/<TABLE>.md` |

- 질문의 거래 테이블은 `ADAMSUSER` 의 `## transaction` 분류에서 찾는다.

## 패턴 번호

| 종류 | 번호 | 목록 |
|---|---|---|
| 부정 패턴 | P-001 ~ P-032 | `okf/wiki/patterns/fraud/index.md` |
| 이상징후 패턴 | P-101 ~ P-141 | `okf/wiki/patterns/anomaly/index.md` |

## 실제 사례 (`okf/real-cases`)

- 이 번들 `okf/real-cases/` 의 파일(`index.md`, `patterns.md`, `fraud.md`, `deficiencies.md`, `expedient-practices.md`)은 **현재 비어 있다**.
- 그래서 `risk_theme.real_cases` 는 원칙적으로 `[]` 로 남기고, 근거는 부정/이상징후 패턴, 테이블 구조, `okf/wiki/risk-interpretation.md` 의 감사 위험 행, `okf/glossary/biz-rules/` 의 업무 배경으로 대신 한다.
- 나중에 실제 사례가 채워지면 그 때만 CS-xxx 를 `real_cases` 에 넣고 근거로 쓴다. 지어내지 않는다.

## 사고 유형

drilldown 이 쓰는 7개 유형이다. 대분류는 부정, 부실, 편법(편법 비용 보전·비정도 영업)이다.

| 번호 | 유형 | 대분류 | 분류 기준 | 주요 수법·발생 방식 |
|---|---|---|---|---|
| ① | 횡령/사적 유용 | 부정 | 회사 자금·제품·혜택을 개인이 직접 취득하거나 사적으로 사용 | 지급계좌 변경, 허위 경비 청구, 개인 비용 대납, 제품 무단 반출·매각, 보상·사은품 부당 수령 |
| ② | 업체 유착/특혜 | 부정 | 거래상 지위를 이용해 특정 업체에 이익을 주거나 대가를 수수 | 과다 지급 후 리베이트 수수, 금품·차량 수수, 본인·가족 업체에 발주, 입찰정보 유출, 특혜 계약 |
| ③ | 프로세스 악용 | 부정 | 특정 대상·목적으로 제한된 구매·공급 조건을 악용 | 임직원 할인제품 재판매, 대리구매·계정 공유, 학생 신분 도용, 허위 B2B 고객 등록, B2C 전매·역외 유출 |
| ④ | 검증부실/과다지급 | 부실 | 실적·증빙·단가·수량의 진위나 정확성 문제로 비용이 부당 지급 | 허위 판매실적, 중복 증빙, 공급량 초과 청구, 미실시 행사·허위 인력 비용 청구, 단가·지급기준 오적용 |
| ⑤ | 사외펀드/예산전용 | 편법 | 거래업체 등에 회사 자금을 별도 적립하고 임의로 사용 | 허위 행사비 적립, 견적 부풀리기, 잔여 예산 선지급, 가격 차액 적립, 타 행사 전용·사적 사용 |
| ⑥ | 편법지원/과소충당 | 편법 | 영업목표 달성이나 거래선 보상을 위해 거래·비용·회계처리를 왜곡 | 구두보상 약속, 허위 명목의 가격·재고 보전, 허위 출고·매출, 비용 이월, 충당 누락·과소계상 |
| ⑦ | 정책/시스템 통제 미흡 | 부실 | 승인·정책·시스템 검증 또는 후속 조치의 우회·누락으로 손실이나 위험 발생 | 가격 적용일 변경, 발주 승인 우회, 예산 목적 외 사용, 할인 대상 검증 누락, 배송·환불 오류, 과지급금 미회수, 무상수리 제외 누락 |

### 부정 패턴별 기본 유형

| 부정 패턴 | 기본 유형 | 비고 |
|---|---|---|
| P-001 인센티브 조작 | ④ | 허위 실적·공급량 초과 청구 |
| P-002 사외펀드(Slush Fund) 조성 | ⑤ | |
| P-003 가짜 벤더 / 유령회사 | ② | |
| P-004 영수증/송장 위조 및 중복 청구 | ④ | 중복 증빙 |
| P-005 제품 유출 및 무단 재판매 | ③ | 자산 직접 취득이면 ① |
| P-006 지급 채널 가로채기 | ① | |
| P-008 시스템 제어 우회 | ⑦ | |
| P-009 예산 편법 사용 및 크로스 차징 | ⑤ | 목적 외 사용이면 ⑦ |
| P-010 과실 기반 부정 | ④ | 확인 누락 |
| P-011 계정 및 자격증명 공유 | ③ | |
| P-014 입찰 및 가격 조작 | ② | |
| P-016 물류 재고 및 배송 조작 | ⑥ | 허위 출고 |
| P-018 재무 및 인사 부정 | ① | |
| P-026 채널 스투핑 | ⑥ | |
| P-027 허위 출고 | ⑥ | |
| P-028 매출 Inflation | ⑥ | |
| P-029 Accrual 조작 | ⑥ | |
| P-030 고객 환불 부정 | ① | 회사 손실 전가면 ⑥ |
| P-032 경비 현금 부정 | ① | |

## 출력 예시

### top-down

```json
{
  "schema_version": "1.0",
  "question": "2025-11-01부터 2026-10-31까지 영업마케팅 매출(청구) 영역에서, 기간 말 며칠에 청구 금액이 비정상적으로 몰린 거래를 찾을 수 있는 부정 위험 시나리오를 만들어줘. 청구 시점 분포와 청구 유형을 함께 보고, 정상적인 계절성·프로모션 청구는 제외해줘.",
  "mode": "top-down",
  "scope": {
    "domain_name": "영업마케팅 매출",
    "domain_slug": "sales",
    "business_area": "영업마케팅",
    "business_process": "SO > DO > GI > 빌링/Invoice > 수금",
    "period": { "start": "2025-11-01", "end": "2026-10-31", "basis": "직전 달 말일까지 12개월" }
  },
  "risk_theme": {
    "summary": "기간 말 며칠에 몰린 대량 청구 — 매출 부풀리기·채널 스투핑 의심",
    "pattern_ids": ["P-026", "P-028"],
    "pattern_names": ["채널 스투핑", "매출 Inflation"],
    "real_cases": []
  },
  "intent": "청구 시점이 기간 말에 비정상적으로 몰린 매출 거래를 찾는다",
  "expected_finding": "매월 말 며칠에 청구 금액·건수가 평소보다 크게 몰려 청구 시점 분포가 비정상인 매출 청구",
  "grounding": {
    "primary_table": "ADAMSUSER.TI_GRPB022",
    "table_type": "인터페이스",
    "row_basis": "청구문서(BILNUM) + 라인(BILITM)",
    "date_column": "BILDATE",
    "amount_column": "BILAMT",
    "supporting_tables": [],
    "key_terms": [
      { "term": "매출 청구", "column": "TI_GRPB022.BILNUM / BILDATE / BILAMT" },
      { "term": "청구 수량", "column": "TI_GRPB022.BILQTY" },
      { "term": "법인", "column": "TI_GRPB022.CMCD" },
      { "term": "청구 유형", "column": "TI_GRPB022.BILTYPE" }
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
  "rationale": "부정 패턴 2개(P-026 채널 스투핑, P-028 매출 Inflation — okf/wiki/patterns/fraud/index.md 4절 sales 조합)가 같은 매출 청구 흐름에 걸리고, ADAMSUSER.TI_GRPB022(class:transaction, has:amount, row_count 18,315,855, size:l)의 BILDATE·BILAMT·BILQTY·BILTYPE 이 문서로 확인된다. 이 번들 okf/real-cases 가 비어 있어 실제 사고(CS) 근거는 미확인. okf/wiki/normal-patterns.md 의 「기간 말 매출의 다음 기간 초 반품」 을 정상 업무 제외 단서로 쓴다. 승인 시나리오 목록이 비어 신규(최종 중복 판정은 배치가 담당). size:l 이라 BILDATE/SPMON 조건 필수."
}
```

### bottom-up

```json
{
  "schema_version": "1.0",
  "question": "2025-11-01부터 2026-10-31까지 영업마케팅 마케팅비(EO(행사계획) → PR(지급요청) 정산)에서, 행사 계획 종료일보다 지급이 앞서 기표되었거나 행사 시작일 전에 지급이 기표된 건, 그리고 같은 인보이스 번호가 여러 지급요청에 연결된 건을 함께 찾아줘.",
  "mode": "bottom-up",
  "scope": {
    "domain_name": "영업마케팅 마케팅비",
    "domain_slug": "mkt-exp",
    "business_area": "영업마케팅",
    "business_process": "EO(행사계획) → PR(지급요청) → 정산",
    "period": { "start": "2025-11-01", "end": "2026-10-31", "basis": "직전 달 말일까지 12개월" }
  },
  "risk_theme": {
    "summary": "행사 계획 기간과 지급 시점의 순서 위반(종료 전·시작 전 지급), 같은 인보이스 번호의 반복 연결",
    "pattern_ids": ["P-111", "P-113", "P-119"],
    "pattern_names": ["선후 순서 위반", "비정상 단축", "증빙 중복"],
    "real_cases": []
  },
  "intent": "마케팅비 지급요청 건의 시간 순서(행사 계획 기간과 지급 기표 시점)와 증빙 연결이 서로 맞지 않는 거래를 찾는다",
  "expected_finding": "행사 계획 종료일보다 앞선 시점에 지급이 기표되었거나, 행사 시작일보다 앞서 지급된 정산 건, 같은 인보이스 번호가 여러 지급요청에 매핑된 건",
  "grounding": {
    "primary_table": "ADAMSUSER.TI_GRPF039",
    "table_type": "인터페이스",
    "row_basis": "EO(EONUM) + PR(PRNUM) 결합 (1행 = EO·PR 결합 1건)",
    "date_column": "BUDAT",
    "amount_column": "LTOTAMT",
    "supporting_tables": [],
    "key_terms": [
      { "term": "지급요청(PR) 전기일", "column": "TI_GRPF039.BUDAT" },
      { "term": "행사 계획 종료일", "column": "TI_GRPF039.PLENDT" },
      { "term": "행사 계획 시작일", "column": "TI_GRPF039.PLSTDT" },
      { "term": "정산금액(PR 총액)", "column": "TI_GRPF039.LTOTAMT" },
      { "term": "인보이스 번호", "column": "TI_GRPF039.IVNO" }
    ]
  },
  "bottom_up": {
    "starting_tables": ["ADAMSUSER.TI_GRPF039"],
    "related_tables": [],
    "expansion_path": "TI_GRPF039(BUDAT vs PLSTDT/PLENDT, IVNO) — 단일 테이블 내 시간·증빙 신호 2종",
    "table_scope": "단일",
    "rationale": "EO·PR 결합 원본 테이블에서 지급 기표 시점(BUDAT)과 행사 계획 기간(PLSTDT/PLENDT)의 순서, 인보이스 번호(IVNO)의 연결 구조를 출발점 삼아 실적 없는 지급·허위 프로모션 의심 건으로 확장"
  },
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
  "rationale": "okf/wiki/risk-interpretation.md 2절 「행사 종료 전 지급, 1일짜리 프로모션, 예산 승인 전 행사가 잦음 → 실적 없는 지급·허위 프로모션(부정 의심; P-111·P-113)」 행과 「같은 증빙(인보이스) 번호로 여러 번 지급 → 중복 지급(P-119)」 행이 같은 EO→PR 정산 흐름에 연결되고, ADAMSUSER.TI_GRPF039(class:transaction, has:amount, row_count 5,677,587)의 BUDAT·PLENDT·PLSTDT·LTOTAMT·IVNO 가 문서로 확인된다. 참고: mkt-exp 도메인 핵심 테이블 TI_GRPF_EO_REPORT 는 이 번들 밖이라 번들 내 EO·PR 결합 원본인 TI_GRPF039 로 대입. 이 번들 okf/real-cases 가 비어 있어 실제 사고 근거는 미확인. 배치는 LWAERS 통화가 섞여 있어 단순 합계 금지(통화별 집계·환산 필요), SPMON 또는 BUDAT/PLSTDT 조건 필수(5.68M행)를 확인해야 한다. 근거: okf/schemas/ADAMSUSER/tables/TI_GRPF039.md, okf/domains/mkt-exp.md, okf/wiki/patterns/anomaly/index.md, okf/wiki/risk-interpretation.md, okf/glossary/index.md."
}
```

### drilldown

예시 상황: 기준 시나리오 「셀아웃 인센티브 과다지급」(top-down, 1단계 거래선/SKU 기준 누적 셀인 < 셀아웃 인센티브 지급수량)이 검증을 통과했다. 원본 질의와 결과는 예시 값이다.

첫 드릴다운(이전 드릴다운 없음, 초과가 같은 모델의 대표 SKU 와 일부 거래선에 몰림 → 정산 단위·거래선 기준 문제부터 걸러 냄):

```json
{
  "mode": "drilldown",
  "proceed": true,
  "accident_type": "④ 검증부실/과다지급",
  "pattern_ids": [],
  "perspective": "정산 단위·거래선 기준 보정 후 초과",
  "question": "2025-11-01부터 2026-10-31까지 영업마케팅 매출차감의 셀아웃 인센티브 정산 영역에서, 거래선이 공급받은 수량보다 많은 판매실적으로 인센티브를 청구해 과다 지급된 것으로 의심되는 거래를 찾을 수 있는 부정 위험 시나리오를 만들어줘.\n위 질의에 더해, 아래 관점으로 결과를 더 좁고 깊게 봐 줘.\n- 정산 단위·거래선 기준 보정 후 초과: 같은 모델의 다른 SKU 셀인과, 매핑에는 없지만 같은 지급처·사업자등록번호를 가진 주문처의 셀인까지 더해도 셀아웃이 셀인을 넘는 건만 남겨 줘. 거래선 인수·합병이나 코드 통폐합으로 갈린 셀인은 합산해 주고, 모델로 묶거나 매핑을 보정해 해소되는 건은 제외해 줘.",
  "reason": ""
}
```

두 번째 드릴다운(직전 보고서 A-1 출발점에 「정산 단위·거래선 기준 보정 후 초과」 관점 줄이 있음 → 그 줄을 그대로 두고 이번 관점을 더함):

```json
{
  "mode": "drilldown",
  "proceed": true,
  "accident_type": "④ 검증부실/과다지급",
  "pattern_ids": [],
  "perspective": "판매가능수량 최초 초과 지급 문서",
  "question": "2025-11-01부터 2026-10-31까지 영업마케팅 매출차감의 셀아웃 인센티브 정산 영역에서, 거래선이 공급받은 수량보다 많은 판매실적으로 인센티브를 청구해 과다 지급된 것으로 의심되는 거래를 찾을 수 있는 부정 위험 시나리오를 만들어줘.\n위 질의에 더해, 아래 관점으로 결과를 더 좁고 깊게 봐 줘.\n- 정산 단위·거래선 기준 보정 후 초과: 같은 모델의 다른 SKU 셀인과, 매핑에는 없지만 같은 지급처·사업자등록번호를 가진 주문처의 셀인까지 더해도 셀아웃이 셀인을 넘는 건만 남겨 줘. 거래선 인수·합병이나 코드 통폐합으로 갈린 셀인은 합산해 주고, 모델로 묶거나 매핑을 보정해 해소되는 건은 제외해 줘.\n- 판매가능수량 최초 초과 지급 문서: 남은 거래선·SKU 마다 컨디션 판매기간 종료일 기준으로 누적 셀인과 누적 셀아웃 지급수량을 비교해, 처음 초과가 생긴 지급 문서와 그 뒤에도 계속 지급된 문서만 남기고 문서별 초과 금액을 보여 줘. 판매기간 종료일과 셀인 사이가 통상 리드타임 안인 건은 제외해 줘.",
  "reason": ""
}
```

세 번째 드릴다운에서 멈출 때:

```json
{
  "mode": "drilldown",
  "proceed": false,
  "accident_type": "④ 검증부실/과다지급",
  "pattern_ids": [],
  "perspective": "",
  "question": "",
  "reason": "결과가 회입 대상 지급 문서 단위로 특정되어 감사인이 한 건씩 바로 볼 수 있으므로 더 좁히지 않는다."
}
```