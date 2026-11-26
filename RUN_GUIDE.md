# OKF 번들 생성 스크립트 실행 가이드 (P0~P3)

기준 문서: [OKF_WORK_GUIDE.md](OKF_WORK_GUIDE.md) · 대상 독자: 스크립트를 DB가 접속되는 환경에서 실행하는 사람

## 업무 지식 보완본 사용·재생성 주의

현재 `okf/`에는 glossary·도메인 안내·테이블 설명의 업무 지식 보완이 포함돼 있다. 별도 biz 폴더를 실행 입력으로 추가하지 않는다. 질의 시 활용은 [audit-work 스킬](skills/audit-work/SKILL.md) §6을 따른다.

아래 생성 명령이 보완 자료를 자동으로 다시 만드는 것은 아니다. 재생성 전후 diff로 추가 glossary와 목차·도메인 링크, 테이블 AUTO 밖 설명이 보존됐는지 확인한다.

## 1. 준비

### 1.1 요구 사항
- Python 3.9 이상, 패키지 `oracledb`(추출 때만), `PyYAML`
  ```bash
  pip install -r scripts/requirements.txt
  ```
  폐쇄망이면 외부망에서 `pip download -r scripts/requirements.txt -d wheels` 후 반입해 `pip install --no-index --find-links wheels -r scripts/requirements.txt`.
- DB 12.1 미만이면 thick 모드가 필요하다 (`.env`의 `ORACLE_CLIENT_LIB_DIR`).

### 1.2 `.env` 설정
```bash
cp .env.example .env      # 이미 .env 가 있으면 값만 채운다
```
| 변수 | 필수 | 설명 |
|---|---|---|
| `AIAGT_DSN` | 필수 | 접속 문자열 (`host:1521/service` 또는 tnsnames 별칭) |
| `AIAGT_USER` | | 비우면 `config/okf_build.yaml`의 `db.expected_user`(AIAGT) |
| `AIAGT_PASSWORD` | | **비워 두면 실행 시 입력 프롬프트** (권장) |
| `ORACLE_CLIENT_LIB_DIR` | | thick 모드일 때만 |

- `.env`는 프로젝트 루트에 둔다. 다른 경로면 `--env-file <경로>`.
- 이미 설정된 OS 환경변수가 `.env`보다 우선한다.
- `.env`는 공유·커밋하지 않는다 (`.gitignore`에 포함).
- 접속 정보 외의 설정은 `.env`가 아니라 [config/okf_build.yaml](config/okf_build.yaml)에 둔다.

### 1.3 `config/okf_build.yaml` 확인 (실행 전)
| 항목 | 할 일 |
|---|---|
| `db.alias` | `resource` URI에 들어갈 DB 식별자를 정한다 (기본 `PRD`) |
| `scope.target_owners` | 대상 OWNER 목록. 비우면 AIAGT가 접근 가능한 전체(기본 스키마 제외) |
| `scope.query_name_mode` | AIAGT가 시노님으로 조회하면 `synonym` |
| `tags.domain_map` | 도메인 매핑이 정해졌으면 입력. 비워 두면 `domain:*` 태그는 달리지 않는다 |

## 2. 실행 순서

모든 명령은 프로젝트 루트(`check/`)에서 실행한다. `--snapshot`을 생략하면 가장 최근 스냅샷을 쓴다.

| # | 단계 | 명령 | DB | 산출물 |
|---|---|---|---|---|
| 0 | (선택) 자체 점검 | `python scripts/selftest.py` | 아니오 | 콘솔 (모든 점검 통과 확인) |
| 1 | **P1 추출** | `python scripts/extract_dictionary.py` | **예 (AIAGT)** | `source/dictionary/<일시>/*.csv`, `snapshot.json`, `INVENTORY.md` |
| 2 | **P0 접근 범위** | `python scripts/build_scope.py` | 아니오 | `work/scope_objects.csv`, `excluded_objects.csv`, `privilege_warnings.csv` |
| 3 | **P2 골격** | `python scripts/build_okf.py --skeleton-only` | 아니오 | `okf/` (index, log, references) |
| 4 | **P2 분류 초안** | `python scripts/classify_tables.py` | 아니오 | `work/table_classification.csv`, `review_queue.csv` |
| 5 | **사람 검토** | `work/table_classification.csv`의 `final_class` 입력 | - | 분류 확정 |
| 6 | **P3 문서 생성** | `python scripts/build_okf.py` | 아니오 | `okf/schemas/**`, `work/join_candidates.csv` |
| 7 | 검증 | `python scripts/validate_okf.py --check-regen` | 아니오 | 콘솔, `work/broken_links.csv` |
| 8~13 | **P4 조인 그래프** | 아래 6장 | 일부 | `okf/joins/**` |

> P0 범위 확정은 개념상 추출 직후에 하는 단계라 2번에 둔다. 번호 순서대로 실행하면 된다.

### 2.1 단계별 방법과 확인할 것

**1) 추출** — DSN과 비밀번호가 준비되면 실행한다.
```bash
python scripts/extract_dictionary.py                     # 전체
python scripts/extract_dictionary.py --only objects,tables   # 일부만 다시 추출
python scripts/extract_dictionary.py --print-sql         # DB 접속 없이 SQL만 출력 (SQL 도구에서 직접 확인할 때)
```
- 접속 직후 `SELECT USER`가 AIAGT가 아니면 중단한다. SELECT/WITH 이외 문장은 실행하지 않는다.
- 콘솔에 CSV별 상태·행 수가 나온다. **필수 뷰가 실패하면 중단**(종료 코드 2)하고, 선택 뷰는 건너뛴다. 사유는 `INVENTORY.md`와 `work/run.log`에 남는다.
- 실행할 때마다 새 스냅샷 폴더가 생긴다. 기존 스냅샷은 수정하지 않는다.

**2) 접근 범위**
```bash
python scripts/build_scope.py
```
- `대상 N건 / 제외 M건 / 권한 경고 K건`을 확인한다.
- `privilege_warnings.csv`에서 **`HIGH`(INSERT/UPDATE/DELETE 등)가 있으면 AIAGT 권한 설계 문제**이므로 담당자에게 보고한다. `CHECK`는 SELECT 권한을 딕셔너리에서 찾지 못한 객체다.
- 제외 규칙을 바꾸려면 config의 `scope.exclude_*`를 고치고 다시 실행한다. 특정 객체를 되살리려면 `scope.include_override: ["ERP.TB_X"]`.

**3) 골격**
```bash
python scripts/build_okf.py --skeleton-only
```
- `okf/index.md`, `log.md`, `references/*`(추출 내역, 접근 범위, 태그 사전)와 후속 단계 폴더의 `index.md`가 만들어진다.

**4) 분류 초안**
```bash
python scripts/classify_tables.py
```
- 분류 현황과 `unknown` 건수가 출력된다. 검토 큐(`review_queue.csv`)에는 unknown, PK 없음, 코멘트 없음, 통계 오래됨, 권한 불명이 쌓인다.

**5) 사람 검토 (필수)**
- `work/table_classification.csv`를 열어 `auto_class`가 틀렸거나 `unknown`인 행의 **`final_class`** 를 채운다.
  - 허용 값: `master, code, transaction, detail, history, mapping, summary, interface, view, unknown`
  - 번들에서 빼려면 `exclude`
- `final_class`가 비어 있으면 `auto_class`를 그대로 쓴다. 입력한 값은 `classify_tables.py`를 다시 실행해도 보존된다.
- 자동 분류가 많이 틀리면 `config`의 `classification.name_rules`(정규식)를 조정한 뒤 `classify_tables.py`를 다시 실행하는 편이 빠르다.
- **`unknown`이 남아 있으면 6번이 멈춘다.** 건너뛰려면 `--allow-unknown`.

**6) P3 문서 생성**
```bash
python scripts/build_okf.py
```
- `생성 / 갱신 / 변경없음 / 범위 밖이 된 문서` 건수가 출력된다.
- 태그가 12개를 넘어 일부가 빠진 문서는 경고로 표시된다.
- `okf/schemas/<OWNER>/tables|views/*.md`, OWNER별 `index.md`, `okf/log.md`가 갱신된다.

**7) 검증**
```bash
python scripts/validate_okf.py --check-regen
```
- 종료 코드 0이면 오류 없음, 1이면 오류가 목록으로 출력된다. (OKF 적합성, 스냅샷 대조, 접근 범위, 태그 사전, 컬럼 수 대조)
- `--check-regen`은 같은 입력으로 다시 생성한 결과와 현재 번들을 비교한다. 사람이 문서를 고쳤다면 차이가 나는 것이 정상이다.
- 깨진 링크는 오류가 아니라 TODO로 `work/broken_links.csv`에 모인다.

## 3. 다시 실행할 때

| 상황 | 방법 |
|---|---|
| DB가 바뀌어 최신 정보가 필요하다 | 1)부터 다시 실행 → 새 스냅샷. 2)·4)·6)·7) 재실행 |
| config(제외 규칙, 태그 패턴 등)만 바꿨다 | 2)부터 재실행 (스냅샷 재추출 불필요) |
| 같은 스냅샷으로 다시 생성했다 | 결과가 바이트 단위로 같다. 변경이 없으면 `log.md`에도 기록되지 않는다 |
| 사람이 문서 본문을 고쳤다 | AUTO 마커(`<!-- AUTO:BEGIN ... -->`) 안쪽만 갱신되고 나머지는 보존된다 |
| `status: stable` 또는 `verified`가 있는 문서 | AUTO 영역만 갱신. 관리 필드(행 수 등)까지 갱신하려면 `build_okf.py --force` |
| DB에서 접근 범위 밖이 된 객체 | 문서는 삭제하지 않고 `work/orphan_docs.csv`에 목록만 남긴다 |
| 특정 스냅샷으로 되돌려 생성 | `--snapshot <폴더명 또는 경로>` |

### 3.1 자주 쓰는 옵션
| 옵션 | 해당 스크립트 | 설명 |
|---|---|---|
| `--snapshot` | scope, classify, build, validate | 스냅샷 지정 (기본 `latest`) |
| `--work`, `--out`/`--okf` | 공통 | 작업/번들 폴더 경로 (기본 `work/`, `okf/`) |
| `--config` | 공통 | 설정 파일 (기본 `config/okf_build.yaml`) |
| `--skeleton-only` | build_okf | 골격만 생성 |
| `--allow-unknown` | build_okf | unknown 분류가 있어도 진행 |
| `--force` | build_okf | stable/verified 문서도 관리 필드 갱신 |
| `--print-sql`, `--only` | extract | SQL 출력만 / 일부 추출 |
| `--env-file` | extract | `.env` 경로 지정 |

## 4. 폴더 구조 (실행 후)
```
check/
├── .env                      # 접속 정보 (공유 금지)
├── config/okf_build.yaml
├── scripts/
├── source/dictionary/<일시>/ # 추출 스냅샷 (수정 금지) + source/INVENTORY.md
├── work/                     # 중간 산출물, run.log (SQL·소요시간 기록, 비밀번호 없음)
└── okf/                      # ★ OKF 번들
```

## 5. 문제 해결

| 증상 | 원인과 조치 |
|---|---|
| `AIAGT_DSN 이 필요하다` | `.env`에 `AIAGT_DSN`을 입력했는지, 프로젝트 루트에서 실행했는지 확인 |
| `접속 계정이 X 이다. AIAGT 가 아니므로 중단` | `.env`의 `AIAGT_USER` 또는 config `db.expected_user` 확인 |
| `DPY-3010` 등 버전 미지원 | DB 12.1 미만 → Oracle Instant Client 설치 후 `ORACLE_CLIENT_LIB_DIR` 지정 |
| `[필수 실패] ...` | 해당 뷰 조회 권한/문법 문제. `work/run.log`의 오류 문구 확인. `--print-sql`로 SQL을 직접 실행해 본다 |
| `ORA-00904` 변형 사용 안내 | 정상. 하위 버전용 쿼리로 자동 대체되었다는 뜻 (`INVENTORY.md` 비고에 표시) |
| `classify`/`build`에서 `scope_objects.csv 가 없다` | 2) `build_scope.py`를 먼저 실행 |
| `분류가 unknown 인 객체 N건...` | 5) 사람 검토에서 `final_class` 입력 |
| `분류표에 없는 객체 N건` | 범위가 바뀐 뒤 분류표가 오래됨 → `classify_tables.py` 재실행 |
| `...AUTO:xxx 마커가 없어 문서 끝에 추가함` | 사람이 마커를 지운 문서. 필요하면 정리 |
| 한글이 깨져 보임 (Windows 콘솔) | 파일은 UTF-8로 저장된다. 콘솔 인코딩 문제이므로 `set PYTHONIOENCODING=utf-8` |

## 6. P4 조인 그래프 (J1~J6)

선행: 위 1~7번(P0~P3)이 끝나 `okf/schemas/**`가 있어야 한다. 기준 문서는 [JOIN_DISCOVERY_GUIDE.md](JOIN_DISCOVERY_GUIDE.md). DB를 쓰는 것은 `join_verify.py`뿐이다.

| # | 단계 | 명령 | DB | 산출물 |
|---|---|---|---|---|
| 8 | **J1·J2 후보 수집** | `python scripts/join_collect.py` | 아니오 | `work/join/candidates.csv`, `candidates_excluded.csv` |
| 9 | (선택) 후보 점검 | `candidates.csv`의 `decision`(accept/reject/fix), `manual_edges.csv` 추가 | - | |
| 10 | **J3 실측 검증** | `python scripts/join_verify.py --dry-run` → `--limit 20` → 전체 | **예 (AIAGT)** | `work/join/verification.csv`, `run.log` |
| 11 | **J4~J6 판정·반영** | `python scripts/join_build.py` | 아니오 | `okf/joins/**`, `okf/joins/graph.md`, `work/join/edges.csv`, `join_graph.json`, `REPORT.md` |
| 12 | 사람 검토 | `work/join/review_queue.csv` → `candidates.csv`의 `decision` 입력 후 11번 재실행 | - | |
| 13 | 검증 | `python scripts/validate_okf.py --check-regen` | 아니오 | |

### 6.1 단계별 방법
**8) 후보 수집**: 선언 FK, 뷰 정의의 조인 조건, 유니크 키와 이름 일치(복합키 포함), 컬럼 한글명 일치, 사람 지정(`work/join/manual_edges.csv`: `child_table, child_cols, parent_table, parent_cols, note`, 테이블은 `OWNER.TABLE`, 컬럼 여러 개는 `|`)에서 후보를 만든다. **날짜 컬럼**(DATE/TIMESTAMP, `*_DT`/`*_YMD` 등)과 범용 컬럼, 코드끼리의 조인은 제외된다. `join:` 설정(점수, 제외 패턴, 임계값)은 `config/okf_build.yaml`.

**10) 실측 검증**: 후보별로 부모 키 유일성 → 자식→부모 포함도(`EXISTS`) → 팬아웃 → (작은 테이블만) 조인 건수를 SELECT로 확인한다.
```bash
python scripts/join_verify.py --dry-run             # 실행할 SQL 출력만 (DB 접속 없음)
python scripts/join_verify.py --limit 20            # 점수 높은 20건으로 먼저 시험
python scripts/join_verify.py                       # 전체. 중단(Ctrl+C)해도 done 건은 저장, 다시 실행하면 이어서
python scripts/join_verify.py --only J1a2b3c4d      # 특정 후보
python scripts/join_verify.py --revalidate          # 이미 done 인 것도 다시
python scripts/join_verify.py --priority-min 20     # 기본 min_score(30) 아래 후보까지
```
- 큰 테이블은 크기 등급(`size:` 태그)에 따라 표본·통계만 쓰고 쿼리마다 타임아웃(`join.verify.timeout_sec`)이 걸린다. 시간 초과 시 더 가벼운 방식으로 한 번만 재시도하고, 그래도 안 되면 `skipped`로 남긴다.
- 저장되는 것은 건수·비율뿐이다 (키 값은 저장하지 않는다. 짧은 최빈값만 더미 키 탐지용으로 기록).
- `EXPLAIN PLAN`은 쓰지 않는다 (PLAN_TABLE 쓰기가 필요해서 SELECT 전용 원칙과 맞지 않는다).

**11) 판정과 반영**: 결과에 따라 확정(N:1, 1:1), 조건부, 직접 조인 금지(N:M), 기각, 검토대기로 나눈다. 조인 concept(`okf/joins/<OWNER>/…md`)와 그래프를 만들고, 마지막에 테이블 문서의 Schema `조인:` 표기와 `# Joins` 영역을 갱신한다 (`--no-refresh`로 생략 가능).
- 사람이 `decision: accept`한 건은 수치는 그대로 남기고 최소 `medium` 신뢰도로 올린다. 부모가 유효기간 이력이라 키가 중복인 경우 `note`에 `filter: <조건>`을 적고 accept하면 조건부 조인이 된다.
- `joins/graph.md`의 인접 목록이 T2S가 읽는 본체다. 보고서(`work/join/REPORT.md`)에서 고립 테이블, 허브, 경로 테스트(거래/상세 → 마스터/코드 도달 여부)를 확인한다.

### 6.2 에이전트(opencode)가 SELECT를 실행할 때
LLM이 직접 조인을 탐색할 때는 [join-discovery 스킬](skills/join-discovery/SKILL.md)을 따른다. 읽기 전용 래퍼 `scripts/sql_ro.py`를 쓰며, **실행 인자·종료코드·응대 절차는 [sql_run 스킬](skills/sql_run/SKILL.md)의 "실행(sql_ro.py)"절을 따른다.**
- 결과 값은 에이전트에게 그대로 전달된다. 래퍼는 컬럼 내용을 걸러 주지 않으므로, 감사/운영 컬럼(`has:audit`)을 업무 이벤트로 오용하지 않도록 join-discovery 스킬의 절대 규칙으로 통제한다.

### 6.3 P4 문제 해결
| 증상 | 조치 |
|---|---|
| `work/join/candidates.csv 가 없다` | `join_collect.py` 먼저 실행 |
| 후보가 너무 적다 / 고립 테이블이 많다 | `REPORT.md`의 고립 목록 확인. 이름이 다른 키는 컬럼 한글명이 같아야 후보가 된다. 안 잡히는 관계는 `manual_edges.csv`로 추가 |
| 후보가 너무 많다 | `candidates_excluded.csv`로 제외 사유 확인, `join.min_score` 상향, `generic_column_patterns` 보강 |
| `verify_skipped: timeout@C` | 큰 테이블. `join.verify.timeout_sec`를 늘리거나 `sample_target_rows`를 줄인다 |
| `parent_keyed_by_validity_period` 검토 항목 | 부모가 기간 이력. `note`에 `filter: 조건` 입력 후 `decision: accept` |
| validate: `usable: true 인데 parent_unique 가...` | 문서를 손으로 고쳤거나 오래된 결과. `join_build.py` 재실행 |
| validate: `join_graph.json 엣지 ≠ 조인 문서` | `join_build.py` 재실행 |

## 7. 이번 범위 밖 (다음 단계)
코드값(P5), 용어집(P6), T2S 규칙·예제(P7)는 아직 스크립트가 없다. 조인 활용 규칙(`t2s/rules/join-usage.md`: 팬 트랩, 차즘 트랩)은 P7에서 작성한다.