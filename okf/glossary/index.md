# glossary

업무 용어와 컬럼·테이블 매핑. 질의 시 INDEX와 함께 가장 먼저 참고한다.

## 용어 매핑

| 용어(동의어) | 의미 | 매핑 (query_name.컬럼) | 비고 |
|---|---|---|---|
| SEUK (SEUK 법인) | 법인 SEUK, 법인코드 C430 | `CMCD`='C430' (예: APPADAMSUSER.TI_GRPB_DE_PAYMENT_REPORT) | 법인**명**이 SEUK(CMNM), 법인**코드**는 C430(CMCD). 마스터: [TI_GRPF900_MST](/schemas/APPADAMSUSER/tables/TI_GRPF900_MST.md) (CMCD/CMNM). 2026-10-05 DB 조회 확인 |

> 출처: /references/llm-wiki-import.md (llm wiki glossary 이식)
