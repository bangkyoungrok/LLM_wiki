---
title: "테이블 그레인(업무 키) DB 실측"
type: Reference
description: "테이블별 그레인(행 유일성) DB 실측 요약. 후보 키 검증·greedy 탐색·2차 전체 스캔·4차 I/F 컬럼 제외 탐색·사람 키 검증."
source: "work/grain_final.csv, work/grain_search_results.csv, work/grain_search2_results.csv, work/grain_search3_results.csv, work/grain_search4_results.csv, work/grain_human_keys_check.csv, work/grain_manual_review.md"
extracted_at: "20261016"
---

# 테이블 그레인(업무 키) DB 실측

테이블 360개에 대해 **1행을 유일하게 식별하는 컬럼 집합(그레인)**을 AIAGT에서 실측 검증했다.
각 테이블의 그레인 판정은 문서 `# T2S 힌트` 영역의 `### 그레인 (DB 실측 ...)` 블록에 반영되어 있다.

## 방법 (4단계)

1. **후보 키 검증**: 후보 키(ES 물리PK > ES 1행단위 토큰매핑 > okf PK > 휴리스틱)로 `ROWNUM<=500K` 표본에서 `COUNT(*)` vs `GROUP BY` distinct 비교. okf PK 46개 별도 검증.
2. **적재 메타 분리**: 유일화에 `LOAD_DT`/`LOAD_DTTM`(적재 메타)이 필요했던 12개는 `loadmeta`(중복 적재 의심, 데이터 관리 재검토 대상)로 분류.
3. **greedy 키 탐색** (비유일·미확인 226개 대상): ① 1회 쿼리로 전 컬럼 distinct/notnull 통계로 선택도 랭킹(PII 제외) → ② 최선단 컬럼부터 1개씩 추가하며 GROUP BY dup_groups 추적(최대 6컬럼, 어느 컬럼을 추가해도 dup이 안 줄면 중단) → ③ 기존 키 실패 시 최상위 단일 컬럼부터 폴백 재탐색 → ④ 발견 키는 **전체 스캔**(무제한 GROUP BY HAVING)으로 dup 0 재검증.
4. **2차 전체 스캔 재탐색** (1차 비유일·loadmeta 141개 대상, 2026-10-16): 1차에 파악된 주요 컬럼(`start_key`)을 출발점으로, **전체 스캔 기준**(ROWNUM 제한 없는 무제한 GROUP BY HAVING)으로 컬럼을 하나씩 늘려 dup 0 달성 시도. 컬럼 상한 16, 연속 비개선 6개면 중단, **적재 메타(LOAD_*)는 업무 키 후보에서 제외**(user 정책). 근접(dup≤20) 그룹은 3차로 16열까지 추가 탐색.
5. **4차 I/F 컬럼 제외 탐색 + 사람 키 검증** (APPADAMSUSER partial/flat 95개 대상, 2026-10-16): ②에서 파악된 최선 컬럼에서 **I/F·적재 컬럼(`RGNT_ID, RGTN_DT, MDPR_ID, MODF_DT, LOAD_*, CE_GUID, BDP_UPDATE_*, SDW_LD_DT`)을 제외**하고 dup 재측정 후 일반 컬럼으로 확장(16열). NULL 함정 점검(모든 키 컬럼 NOT NULL 조건 dup). 사람(`work/grain_manual_review.md`)이 직접 쿼리로 확인한 **업무 키 15건**은 전체 스캔으로 dup 실측해 반영.

산출물: `work/grain_inventory.csv`(후보 키), `work/grain_verification.csv`(1차), `work/grain_secondpass.csv`(2차), `work/grain_okfpk_check.csv`(okf PK), `work/grain_search_results.csv`(1차), `work/grain_search2_results.csv`(2차), `work/grain_search3_results.csv`(3차 근접), `work/grain_human_keys_check.csv`(사람 키 실측), `work/grain_search4_results.csv`(4차 I/F 제외), `work/grain_final.csv`(최종 판정), `work/grain_manual_review.md`(사람 키 탐색 워크 문서).

## 판정 분포 (360개)

| 판정 | 개수 | 의미 |
|---|---:|---|
| unique | 248 | 유일 (전체 스캔 dup 0) — 자동 탐색(1~4차) + **사람 직접 쿼리 확인** 누적 |
| **near_key** | **44** | **업무 키는 확인(사람)했으나 전체 스캔 dup>0 — 데이터 품질(중복 적재·NULL·포맷 불일치)로 비유일. 데이터 정비 후 unique 전환 기대.** |
| unique_with_time | 2 | 유일 (업무 기간 컬럼 필요 — 월별 스냅샷) |
| unique_okfpk | 1 | 유일 (okf 물리 PK 확인) |
| **loadmeta** | **10** | **업무 키만으론 비유일 — 적재 메타(LOAD_DT/LOAD_DTTM)까지 넣어야 유일. 중복 적재 흔적, 데이터 관리 재검토 요청 대상** |
| non_unique | 52 | 비유일. **TR_(시나리오 추출) 8 + HYBR(하이퍼스) 13은 사용자 지시로 제외**(T2S 조회 대상 미사용), SETADAMSUSER 19 별도 미진행, APPADAMSUSER 비고만 10(사용 지시) + 미처리 2(`work/grain_manual_review.md`) |
| empty_or_null | 3 | 빈 테이블 (COUNT(*)=0) |
| unverified | 0 | 검증 불가 (CLOB 컬럼 포함 뷰 등) |

> **사람 직접 쿼리 확인** (2026-10-16, `work/grain_manual_review.md`): 자동 탐색(1~4차)으로 유일 키 못 찾은 테이블을 사람이 `GROUP BY HAVING COUNT(1)>1`으로 직접 검증. 1차 문서 56건 + 2차 문서 56건 처리 — **unique 33**(dup 0 확인) + **near_key 35**(업무 키 확인·데이터 품질로 dup>0) + **비고(사용 지시) 26** + **TR_/HYBR 제외 21**.

## greedy 탐색 성과

- **1차 greedy 탐색**: 비유일·미확인 **226개** 중 **82개 신규 유일 키 발견** (전체 스캔 dup 0 확인).
- **2차 전체 스캔 재탐색** (2026-10-16): 1차 비유일·loadmeta **141개** 대상으로 전체 스캔(무제한) 기준 재탐색 → **10개 추가 유일 키 발견** (업무 키, LOAD 제외), **2개 loadmeta 신규 확인** (LOAD 넣어야 유일), **129개 비유일 확정**(1:N·복제행). unique 213 → **223**.
- **2차에서 새로 유일 확인된 업무 키 10개**: TI_GRPB811(`ENTP_CD,STRT_DT,IF_GB,ENTP_NM,CMCD,IF_DT`), TI_GRPB_CUSTOMER_GROUP(`CUSTOMER_CODE,CUSTOMER_NAME,CUSTOMER_GROUP,COMPANY`), TI_GRPB_DE_CONDITION_TCOST(10컬럼), TI_GRPB_DE_DEALSHEET(`CONDITION_NO,SEQNO,SEND_DATE,RECEIVER`), TI_GRPB_MD_MODEL(9컬럼), TI_GRPF801(`COCD,EMID,EPID,SGID`), TI_HYBR007(10컬럼), TI_CMMT050(`CMCD,FILE_ID,RGNT_ID,MDPR_ID,KEY2,SEQ`), V_SCN_LIST2(`DSEQ`), V_TI_CMMT050(`KEY1,FILE_ID,KEY2,SEQ`).
- **4차 I/F 컬럼 제외 탐색** (2026-10-16, APPADAMSUSER 95개): I/F·적재 컬럼(`RGNT_ID,RGTN_DT,MDPR_ID,MODF_DT,LOAD_*,CE_GUID,BDP_UPDATE_*,SDW_LD_DT`)을 키 후보에서 제외하고 재탐색 → **TI_GMCS001, TI_GRPF029 dup 0 확인**(unique 승격). **9개는 NOT NULL 조건 시 dup 0** (NULL 행이 dup을 만들어 냄 — near_key).
- **사람 확인 키 15건** (`work/grain_manual_review.md` 직접 쿼리, 2026-10-16): 전체 스캔 dup 실측 후 **5건 unique 승격**(TI_GRPF830, TI_GRPB_MD_MODEL_CM, TI_GRPB_MD_PRICE_VALUATION, TI_GRPB_MD_SALES_MODEL, 그 외 dup 0) / **10건 near_key**(업무 키는 확실하나 데이터 품질로 dup>0 — TI_GRPF_EO_INFO dup 149만, TN_AD_ENTP dup 200만 등).
- **2차 신규 loadmeta 2개**: TI_BQMS006_COMMCODE(`COMM_CODE_TYPE_CODE,CODE,KO_LABEL,DESCRIPTION` + LOAD_DT), TI_BQMS032_INFA_QT_RESULT(`SITE_CODE,REQ_NO,REQ_SEQ` + LOAD_DT/LOAD_DATE) — 500K 표본에선 잡히지 않았던 중복 적재가 전체 스캔에서 확인.
- **표본(500K)에서 유일했으나 전체 스캔에서 비유일 14개** — 표본 검증의 한계 확인, `work/grain_search_results.csv` `status=FULL_SCAN_NON_UNIQUE` 참조.
- **loadmeta 12개 중 4개는 업무 키로 유일 확인되어 해제** (TI_GRPF009, TI_GRPF030, TI_GRPI010, TI_GSCM001 — 등록일/통계일 등 업무 컬럼 포함). 나머지 8개는 2차 전체 스캔에서도 업무 키 비유일 확인 — 데이터 관리 이슈 유지.

## 업무 기간 컬럼이 필요한 유일한 키 (월별 스냅샷, 2개)

| 테이블 | 키 |
|---|---|
| TS_AD_SCORE_ENT_RESULT | ENT_ID,REGISTER_ID,MODIFIER_ID,SCORE_YYYYMM |
| V_SCN_REPORT5 | SCENARIO_ID,STD_YM |

## 적재 메타(LOAD_DT/LOAD_DTTM) 포함 시에만 유일한 키 — 데이터 관리 이슈 (10개)

| 테이블 | 업무 키 후보 (비유일) | 비고 |
|---|---|---|
| TI_BQMS002_INFA_USER | USER_ID | 1차 |
| TI_BQMS006_COMMCODE | COMM_CODE_TYPE_CODE,CODE,KO_LABEL,DESCRIPTION | 2차 신규 (dup 37) |
| TI_BQMS032_INFA_QT_RESULT | SITE_CODE,REQ_NO,REQ_SEQ | 2차 신규 (dup 2331) |
| TI_GRPF060 | PYDOC | 1차 |
| TI_GRPF063 | CODOC,HLVER | 1차 |
| TI_GRPF064 | CODOC,CITEM,ACAMT_L,TCAMT_U,TPROCO | 1차 |
| TI_GRPF067 | CODOC,TFAMT,TFQTY | 1차 |
| TI_GSCM002 | ITEM | 1차 |
| TI_GSCM009 | SITEID,ITEM,CATEGORY | 1차 |
| TI_GSCM011 | COMPANY,SITEID | 1차 |

## near_key — 업무 키 확인·데이터 품질로 비유일 (44개)

사람이 직접 쿼리로 확인한 업무 키(1차 15 + 2차 43) + 4차 탐색에서 NOT NULL 조건 시 dup 0인 키(9). **업무적으로는 이 컬럼이 키이나 실제 행에 중복·NULL·포맷 불일치**가 있어 전체 스캔 dup>0. 데이터 정비 후 unique 전환 기대. okf 문서에 사람 비고(사용 방식: PARTITION BY 최신값, OR JOIN 조건, 중복제거 필요 등) 포함.

| 유형 | 개수 | 대표 |
|---|---:|---|
| 사람 확인 키 (dup>0) | 35 | TI_GRPF_EO_INFO(`ORDER_ID,ORDER_ITEM_NO,PROPOSAL_ID,DOC_STATUS` dup 149만 — CREATE_DATE 포맷), TN_AD_ENTP(`ENTP_CD` dup 200만 — 최근 날짜 사용), TI_BQMS810(`CMCD,SITE_CD,STD_DT,REQ_NO,ITEM_ID,EPR_CD` LAST_YN='Y' 기준), TI_BQMS045_INFA_QT_UI(SELECT_YES 중복 적재) |
| NOT NULL 시 dup 0 (NULL 함정) | 9 | TI_BQMS017/018/019/021_LOG_*(`REQ_NO`), TI_GRPB_DE_SELLOUT, TI_HYBR009, TI_HYBR032, TI_KDPT002 |

## 빈 테이블 (COUNT(*)=0, 3개)

`TI_GRPB_DE_CONDITION_AMT`, `TI_GRPB_DE_CONDITION_ITEM`, `TI_GRPB_DE_CONDITION_TCMS` — 그레인 없음. 조회 시 0행.

## 주요 발견

- **okf 물리 PK 46개 중 45개 유일성 확인** (1건 `TI_GRPB_DE_CONDITION_AMT`은 빈 테이블).
- ES `1행 단위` 서술 신뢰 가능 — 스키마 매핑 후보 대부분 유일 확인 (예: TI_GRPB_DE_PAYMENT `PAYMENT_NO,ITEM_NO,CONDITION_NO`).
- **non_unique 52개** — 남은 비유일. 구성: **TR_(시나리오 추출) 8 + HYBR(하이퍼스) 13은 사용자 지시로 제외**(T2S 조회 대상 미사용, okf 그레인 블록 "제외" 표기), **SETADAMSUSER 19는 별도 미진행**(사용자 지시), **APPADAMSUSER 12**(비고로 사용 지시 10 + `work/grain_manual_review.md` 미처리 2: TI_BQMS020_LOG_QT_RETRV, TI_BQMSMB002).
- **사람 직접 확인으로 정리 완료** (2026-10-16): non_unique였던 APPADAMSUSER 테이블 중 사람이 `GROUP BY HAVING COUNT(1)>1`으로 직접 검증 → **unique 33**(dup 0) + **near_key 35**(업무 키 확인, dup>0·데이터 품질) + **비고(사용 지시) 26** + **제외 21**. 키 오타 교정: `DICISION`→`DIVISION`(TI_GRPB004B_GRP), TRNO→TR_NO, ESTORE_HYBIRS_ID→ESTORE_HYBRIS_ID.

## 주의

- **unique는 전체 스캔 기준** (1차·2차 greedy로 발견한 키는 무제한 GROUP BY HAVING dup 0 확인). 단 1차 표본 검증 키(ES/휴리스틱/okf) 중 전체 스캔 재검증은 TI_BQMS005_INFA_QT_2(사람 지시)·loadmeta 4건·2차 10건에 한함 — 표본(500K) 범위만 확인된 키는 있음을 인지할 것.
- ROWNUM<=500K 표본은 실행 순서 기반이라 시간별 균일표본 아님. 2차 전체 스캔으로 14개(표본유일→전체비유일)·2개(신규 loadmeta) 교정됨.
- **2차 전체 스캔은 컬럼 상한 16** — 16열을 넘어선 그레인은 탐색으로 못 찾음 (partial로 분류). PII·적재 메타(LOAD_*)는 후보에서 제외.
- 그레인 판정은 **조회(SELECT)의 집계·JOIN 정확도**를 위한 참고지식이지, 물리 PK 정의가 아니다.
