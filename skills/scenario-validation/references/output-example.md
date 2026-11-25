# 출력 예시

아래 입력 1건에 이 스킬을 적용한 출력 예시다. `DEMO.DEMO_BID`(입찰), `DEMO.DEMO_VENDOR`(업체)는 설명을 위한 가상 테이블이고, 데이터 사전 문서가 있다고 가정했다. 수치도 가상이다.

## 입력

- scenario_name: `동일 견적가와 업체 반복 선정이 겹친 입찰`
- scenario_sql: `SELECT BID_ID, BID_DT, VENDOR_ID, SAME_PRICE_CNT FROM (SELECT BID_ID, BID_DT, VENDOR_ID, SAME_PRICE_CNT, COUNT(*) OVER (PARTITION BY VENDOR_ID) AS SELECTION_CNT FROM DEMO.DEMO_BID WHERE BID_DT >= DATE '2025-11-01' AND BID_DT < DATE '2026-11-01' AND VENDOR_ID IS NOT NULL AND SAME_PRICE_CNT >= 2) WHERE SELECTION_CNT >= 3`

## 출력 (아래 구분선 사이가 에이전트가 내보내는 Markdown 전문)

---

# 유효성 검증 결과: 동일 견적가와 업체 반복 선정이 겹친 입찰

| 판정 | 행 수 | 남은 행 | 중복 | 검증일 |
|---|---|---|---|---|
| PASS | 214행 | 61행 | 없음 | 2026-11-25 |

## 1. 입력 확인

- scenario_name: 동일 견적가와 업체 반복 선정이 겹친 입찰
- 형식 점검: 이상 없음 (한 줄, 세미콜론·FETCH FIRST·바인드 변수·주석 없음)

## 2. 데이터 사전 대조

| 점검 | 결과 | 근거 |
|---|---|---|
| SELECT 전용 | 통과 | 단일 SELECT, 인라인 뷰 1개 |
| 객체명 | 통과 | `DEMO.DEMO_BID` 가 `query_name` 과 일치 |
| 컬럼 | 통과 | `BID_ID`, `BID_DT`, `VENDOR_ID`, `SAME_PRICE_CNT` 모두 `# Schema` 표에 있음 |
| 조인 | 해당 없음 | 단일 테이블 |
| 코드값 | 해당 없음 | 코드 리터럴 없음 |
| 삭제 플래그 | 해당 없음 | 삭제 플래그 컬럼 없음 |
| PII | 해당 없음 | `has:pii` 컬럼 없음 |

## 3. SQL 실행 결과

- 실행: 성공
- 행 수: 214행 (10행이 돌아와 `COUNT(*)` 로 감싸 셈)
- 오류: 없음

| BID_ID(입찰번호) | BID_DT(입찰일) | VENDOR_ID(선정업체) | SAME_PRICE_CNT(동일견적가업체수) |
|---|---|---|---|
| B2501103 | 2025-11-04 | V0182 | 3 |
| B2501177 | 2025-11-19 | V0182 | 2 |
| B2512020 | 2025-12-08 | V0415 | 4 |

## 4. 소명 확인

### 4.1 소명 경로별 확인

| 경로 | 확인한 것 | 소명된 행 수 | 결과 | 근거 |
|---|---|---|---|---|
| 조회 착시 | `BID_ID(입찰번호)` 별 행 수 | - | 해당 없음 | 입찰 1건 = 1행(중복 0) |
| 적재·데이터 품질 | `REGISTER_ID(등록자)`·`REGISTER_DT(등록일시)` 분포 | - | 해당 없음 | 등록자 37명, 등록 시각 고르게 퍼짐 |
| 같은 테이블의 다른 컬럼 | 걸린 행과 안 걸린 행의 `BID_TYPE(입찰유형)` 분포 | 131행 | 일부 소명 | 걸린 행의 61%가 단가계약(안 걸린 행 12%). 단가계약은 고정 단가라 견적가가 같은 것이 정상 |
| 같은 테이블의 다른 행 | 같은 품목의 `REBID_YN(재공고여부)` 행 | 8행 | 일부 소명 | 유찰 뒤 재공고로 같은 업체가 다시 선정됨 |
| 코드값 뜻 | `BID_TYPE(입찰유형)` 코멘트와 공통코드 | - | 해당 없음 | 공통코드에서 'F' 가 단가계약이라는 뜻을 확인했고, 이 행들은 단가계약 소명에 이미 들어 있음 |
| 연결된 테이블 | `# Joins` 와 조인 문서 | - | 해당 없음 | 승인·결재 기록과 이어진 테이블 없음 |
| 대상의 속성 | `DEMO.DEMO_VENDOR` 의 `SOLE_SUPPLIER_YN(단독공급업체여부)` | 17행 | 일부 소명 | 단독 공급 업체라 반복 선정이 정상 |
| 기간 경계 | 짝 기록이 필요한 조건인지 | - | 해당 없음 | 짝 기록을 보는 조건이 아님 |
| 단위·환산 | 견적 통화 | - | 해당 없음 | 모두 원화 |
| 정상 업무 | `okf/wiki/normal-patterns.md` | - | 해당 없음 | 정상 업무 문서의 「단가계약은 고정 단가」는 단가계약 입찰 소명과 같은 행이라 따로 세지 않음 |
| 업무 규칙·운영 지식 | 구매 도메인 규칙 문서의 긴급 구매 예외 | 0행 | 해당 없음 | 긴급 구매 표시가 있는 행 없음 |

### 4.2 소명 조건

| 소명 조건(업무 말) | SQL 조건 | 소명된 행 수 |
|---|---|---|
| 단가계약 입찰 | `BID_TYPE = 'F'` | 131 |
| 유찰 뒤 재공고 입찰 | `REBID_YN = 'Y'` | 8 |
| 단독 공급 업체 선정 | `EXISTS (SELECT 1 FROM DEMO.DEMO_VENDOR v WHERE v.VENDOR_ID = s.VENDOR_ID AND v.SOLE_SUPPLIER_YN = 'Y')` | 17 |

### 4.3 남은 행

- 남은 행: 61행
- 세는 SQL: `SELECT COUNT(*) AS REMAINING FROM (<원본 SQL>) s WHERE NOT EXISTS (SELECT 1 FROM DEMO.DEMO_BID b WHERE b.BID_ID = s.BID_ID AND (b.BID_TYPE = 'F' OR b.REBID_YN = 'Y')) AND NOT EXISTS (SELECT 1 FROM DEMO.DEMO_VENDOR v WHERE v.VENDOR_ID = s.VENDOR_ID AND v.SOLE_SUPPLIER_YN = 'Y')`

| BID_ID(입찰번호) | BID_DT(입찰일) | VENDOR_ID(선정업체) | SAME_PRICE_CNT(동일견적가업체수) |
|---|---|---|---|
| B2512020 | 2025-12-08 | V0415 | 4 |
| B2603311 | 2026-03-27 | V0415 | 3 |

## 5. 중복 판별

| 후보 | 위험 상황 | 대상 | 조건 구조 | 판정 |
|---|---|---|---|---|
| SSA2405003(들러리 견적 업체 반복 참여) | same(경쟁 견적의 형식화) | different(참여 업체 vs 선정 업체) | different(참여 횟수 vs 동일 견적가 + 선정 횟수) | different |

- 판정: 중복 아님

## 6. 감사인이 확인할 소명 자료

- 남은 61행의 견적 요청서와 업체 선정 품의서(같은 견적가가 나온 경위, 선정 사유)

## 7. 확인 필요

- 없음

## 판정

| 키 | 값 |
|---|---|
| scenario_name | 동일 견적가와 업체 반복 선정이 겹친 입찰 |
| verdict | PASS |
| row_count | 214 |
| remaining_rows | 61 |
| explained_conditions | 단가계약 입찰 131행 · 유찰 뒤 재공고 입찰 8행 · 단독 공급 업체 선정 17행 |
| reason | 동일 견적가 입찰에서 같은 업체가 3번 이상 선정된 214건 중 153건 소명, 61건 소명 안 됨(소명 경로 모두 확인). 기존 시나리오와 2축 이상 일치 없음. |
| evidence | 214행 중 단가계약 131행, 재공고 8행, 단독 공급 업체 17행이 소명됨(겹침 제외 153행). 남은 61행은 일반 경쟁 입찰이다. |
| duplicate_of | 없음 |
| bundle_check | 객체 위반 없음 / 컬럼 누락 없음 / 조인 위험 없음 / PII 없음 / SELECT 전용 통과 |

## 검증 요약

- **판정: PASS** — 데이터로는 소명되지 않는 61건이 남아 감사 시나리오로 쓸 수 있다.
- 214건 중 153건은 단가계약(`BID_TYPE(입찰유형)`), 재공고, 단독 공급 업체로 소명됐다.
- 남은 61건은 일반 경쟁 입찰인데 견적가가 같고 같은 업체가 반복 선정됐다.
- 감사인은 남은 건의 견적 요청서와 선정 품의서를 확인한다.

## verdict JSON

```json
{
  "verdicts": [
    {
      "scenario_name": "동일 견적가와 업체 반복 선정이 겹친 입찰",
      "verdict": "PASS",
      "row_count": 214,
      "remaining_rows": 61,
      "explained_conditions": [
        {"condition": "단가계약 입찰", "rows": 131},
        {"condition": "유찰 뒤 재공고 입찰", "rows": 8},
        {"condition": "단독 공급 업체 선정", "rows": 17}
      ],
      "reason": "동일 견적가 입찰에서 같은 업체가 3번 이상 선정된 214건 중 153건 소명, 61건 소명 안 됨(소명 경로 모두 확인). 기존 시나리오와 2축 이상 일치 없음."
    }
  ]
}
```

---

## 다른 판정일 때 달라지는 부분 (요약)

- `EXPLAINED`: 걸린 행이 모두 소명된 경로에서 멈추고, 그 뒤 경로는 「소명 확인」 표에 「보지 않음(모두 소명됨)」으로 적는다. `remaining_rows` 는 0, 「중복 판별」은 미수행(모두 소명)이다.
- `INVALID`(데이터 사전에 없는 객체): 「SQL 실행 결과」가 `미실행(<사유>)`, 「소명 확인」·「중복 판별」은 미수행이다. `row_count`·`remaining_rows` 는 null, `explained_conditions` 는 `[]` 다.
- `PASS`(상한에 닿아 보지 못한 경로가 있음): 「소명 확인」 표에 그 경로를 「보지 못함」으로 적고, `reason` 괄호를 `소명 경로 2개는 확인하지 못함` 으로 쓴다. 「확인 필요」에는 예를 들어 `질의 횟수 한도에 닿아, 같은 입찰이 분석 기간 바로 앞뒤 달에 다시 공고됐는지와 견적 금액의 통화가 섞였는지는 확인하지 못했다.` 처럼 쓴다.