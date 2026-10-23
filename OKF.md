# OKF 번들

OKF(Open Knowledge Format)는 SDS 측이 만들어 관리하는 DB 지식 번들이다. 테이블·뷰 문서, 조인 문서, 코드, 도메인, 용어, SQL 규칙이 마크다운으로 들어 있다. 각 프로젝트 브랜치의 `okf/` 가 이 번들이며, 에이전트는 문서 안의 링크(`/schemas/...`) 앞에 `okf` 를 붙여 읽는다.

## 구조

```
okf/
├── codes/          코드 컬럼 실측값
├── domains/        업무 도메인 page (「## 테이블 목록」에 유형 칸)
├── glossary/       업무 용어·업무 지식(biz-*.md)
├── joins/          조인 문서 (index.md, graph.md, OWNER별)
├── references/     근거 자료 (그레인, 코드값 샘플, 시나리오 등)
├── schemas/        OWNER별 목차와 테이블·뷰 문서 (APPADAMSUSER, SETADAMSUSER)
└── t2s/
    ├── examples/   승인된 질문-SQL 예제
    └── rules/      date-handling, pii, result-interpretation, soft-delete-validity, table-selection
```

## 이 저장소의 okf 상태

- 원본에서 에이전트가 쓰지 않는 파일 11개를 뺐다(아래 목록). 실행·행 수·이름·조인 규칙은 각 프로젝트의 `skills/sql-query` 에 들어 있다.
- 도메인 page 「## 테이블 목록」에 `tools/add_table_type.py` 로 「유형 (table_type)」 칸을 넣었다.
- 갖고 있는 사본이 일부라 빠진 파일이 있다. 빠진 폴더마다 `PLACEHOLDER.md` 에 빠진 파일 이름이 적혀 있다.

| 폴더 | 들어 있음 | 빠진 파일 |
|---|---|---|
| `schemas/APPADAMSUSER/tables/` | 5개 | 291개 |
| `schemas/SETADAMSUSER/tables/` | 5개 | 21개 |
| `schemas/SETADAMSUSER/views/` | 5개 | 32개 |
| `glossary/` | 2개 | biz-*.md 34개 정도 |
| `joins/APPADAMSUSER/` | 54개 | 몇 개 더 있을 수 있음 |

## 업데이트 절차 (OKF 를 새로 받을 때)

1. 원본 `okf-main/okf/` 의 내용 전부를 프로젝트의 `okf/` 에 복사한다(덮어쓰기). `okf-main` 루트의 다른 파일(README, scripts 등)은 쓰지 않는다.
2. 프로젝트 루트에서 11개를 지운다.

   ```powershell
   $files = @('index.md','log.md','references\access-scope.md','references\es-index-sources.md','references\table-type-sources.md','t2s\index.md','t2s\rules\big-table.md','t2s\rules\join-rules.md','t2s\rules\naming.md','t2s\rules\row-limit.md','t2s\rules\select-only.md')
   foreach ($f in $files) { Remove-Item -LiteralPath (Join-Path 'okf' $f) -ErrorAction SilentlyContinue }
   ```

3. `main` 브랜치의 `tools/add_table_type.py` 를 받아 프로젝트 루트에서 `python <경로>/add_table_type.py okf` 로 유형 칸을 채운다(`--dry-run` 으로 미리 볼 수 있다).
4. 남은 `PLACEHOLDER.md` 를 지운다.

지우는 11개는 OKF 가 바뀌어도 늘 같다(파일 추가·삭제 없이 내용만 바뀌는 전제). 에이전트 파일이 이 11개를 어떤 경로로도 가리키지 않는다.
