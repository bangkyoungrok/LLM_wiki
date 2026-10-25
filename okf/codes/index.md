# codes

코드성 컬럼과 공통코드. 공통코드 정본은 `SETADAMSUSER.TC_CF_COMM_CODE` (`CODE_ID`+삭제 플래그).

> **삭제 플래그값 주의 (DB 실측 2026-10-15)**: `TC_CF_COMM_CODE.DELETE_YN`과 `TC_CF_COMM_CODE_TYPE.DELETE_YN`은 실제값이 **`0`(정상)/`1`(삭제)** — `'N'/'Y'` 아님.
> `_YN`/`_GB` 컬럼은 표마다 `Y/N`인 것과 `0/1`인 것이 공존한다 (대부분 `Y/N`, `0/1`은 일부). 쿼리 작성 전 해당 컬럼 실제값은 `/references/code-value-samples.md`(`work/code_value_samples.csv`)로 확인.

## 코드 컬럼 문서 (DB 실측)

- [TI_BQMS004_INFA_BD](/codes/TI_BQMS004_INFA_BD.md) — PROGRESS_STATUS(BD_PROGRESS 22종), NOT_SELECT_REASON_YN, 선정여부/비최저가(NULL 처리)
- [TI_BQMS005_INFA_QT](/codes/TI_BQMS005_INFA_QT.md) — QT상태 (한글 라벨 저장, 코드 아님)
- [TI_GRPF830__CRCR_KDCD](/codes/TI_GRPF830__CRCR_KDCD.md) — 카드구분 (COMMENT와 실데이터 불일치)

> 출처: /references/llm-wiki-import.md (llm wiki 실측 이식, DEV 실측 기준)
