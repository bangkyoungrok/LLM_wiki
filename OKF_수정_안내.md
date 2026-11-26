# OKF 수정 안내 (시나리오 생성 다이어트 후속)

- 대상: 시나리오 생성 쪽 `okf/`
- 기준: 11/25 받은 okf-dx.zip 안의 okf. 지금 실제 okf 와 다를 수 있으니 행 번호보다 문장으로 찾아 고친다.
- 배경: okf 밖 파일(AGENTS, skill, sub-agent)에서 아래 문서들을 더 이상 읽지 않게 바꿨다. okf 에서는 그 문서들을 지우고, 지운 문서를 가리키던 줄을 정리한다.
  - 이상징후 패턴
  - 위험 해석
  - 선별 기준
  - 업무 규칙 역방향
  - 패턴 조합 점검

---

## 1. 지울 파일·폴더 (4가지)

| 경로 | 파일 수 | 지우는 이유 |
|---|---|---|
| `okf/wiki/patterns/anomaly/` | index 포함 42개 | Bottom-up 이 데이터를 보기 전에 패턴 목록부터 보면 그 목록만 찾게 됨. 데이터에서 출발하도록 끊음 |
| `okf/wiki/risk-interpretation.md` | 1개 | 패턴 번호별로 해석 행을 고르는 문서라 해석까지 패턴에 묶임 |
| `okf/wiki/criteria/` | 3개 (index, top-down, bottom-up) | 예전 점수 기준. 이미 어떤 skill 도 읽지 않음 |
| `okf/glossary/biz-rules/tables/` | 4개 (index, 테이블별 3개) | 업무 규칙 역방향(테이블 기준, 등급 A·B) 절차를 없앰. 도메인 기준 정방향(`okf/glossary/biz-rules/<도메인>/`)은 남김 |

---

## 2. 고칠 파일 (5개)

### 2-1. `okf/wiki/index.md`

이 파일은 이제 skill 이 직접 읽지 않는다. 도메인은 `okf/domains/index.md` 에서 정한다. 지운 문서로 가는 링크만 정리한다.

**① 「모드별로 읽는 것」 표의 Top-down 줄 (15행)**: 「해석·선별」 칸에서 위험 해석, 선별 기준 링크를 지운다.

```
| Top-down (`topdown-scenario-generation`) | [부정 패턴 목록](okf/wiki/patterns/fraud/index.md)(P-001 ~ P-032, 고의) → 패턴 page `okf/wiki/patterns/fraud/P-0xx.md` | [정상 업무 패턴](okf/wiki/normal-patterns.md) | [이전 시나리오](okf/wiki/examples/index.md) |
```

**② 같은 표의 Bottom-up 줄 (16행)**: 「패턴」 칸의 이상징후 패턴 목록을 지우고, 「해석·선별」 칸에서 위험 해석, 선별 기준 링크를 지운다.

```
| Bottom-up (`bottomup-scenario-generation`) | 없음 (데이터에서 출발) | [정상 업무 패턴](okf/wiki/normal-patterns.md) | 통계 도구는 sub-agent `bottomup-anomaly-explorer` |
```

**③ 18행 패턴 설명**: 두 종류에서 한 종류로 바꾼다.

```
- 패턴은 **부정 패턴**(고의, Top-down 이 참고) 한 종류다. Bottom-up 은 패턴 없이 데이터에서 출발한다. 안내는 [패턴 허브](okf/wiki/patterns/index.md).
```

**④ 「지도」 표 32행**: 「선별 기준 색인」 행을 통째로 지운다.

```
| [선별 기준 색인](okf/wiki/criteria/index.md) | 모드별 시나리오 후보·가설 점수 기준 |
```

**⑤ 「지도」 표 34행**: 「그레인 실측」 행 중간에 빈 줄이 30줄쯤 끼어 표가 깨져 있다. 빈 줄을 지워 한 줄로 잇는다.

```
| [그레인 실측](okf/references/grain-samples.md) | 1행 단위와 업무 키(분석 단위, key_columns), near_key(중복 적재) |
```

---

### 2-2. `okf/wiki/patterns/index.md` (패턴 허브)

**① 10행 첫 문장**

- AS-IS: 감사 패턴은 두 종류이며 모드마다 한 종류만 쓴다. 자기 모드의 목록으로 바로 간다.
- TO-BE:

```
감사 패턴은 부정 패턴 한 종류이며 Top-down 에서 참고한다. Bottom-up 은 패턴 없이 데이터에서 출발한다.
```

**② 15행**: 표의 「데이터 이상징후 패턴 (P-101 ~ P-141)」 행을 통째로 지운다.

**③ 17행**

- AS-IS: 조합 유형 이름(같은 행, 집단→행, 흐름→행, 단일)은 두 종류가 같다. SQL 로 잇는 법은 `skills/sql-query` 5절.
- TO-BE:

```
- 조합 유형 이름은 같은 행, 집단→행, 흐름→행, 단일이다. SQL 로 잇는 법은 `skills/sql-query` 5절.
```

**④ 18행**: 「패턴 파일의 『이 기법을 쓰는 부정 패턴』 줄과 … 다른 모드의 패턴을 시나리오에 붙이지 않는다.」 줄을 통째로 지운다.

---

### 2-3. `okf/wiki/patterns/fraud/index.md` (부정 패턴 목록)

okf 밖에서 「조합 점검」 절차와 선별 점수를 없앴다. 그래서 그 둘을 가리키는 문장과 「2~3개」, 「최대 3개」 같은 숫자를 정리한다.

**① 1절 쓰는 순서 (20~21행)**

- AS-IS 2: 대입과 조합(2단계, topdown-hypothesizer): 넘겨받은 테이블에 패턴을 대입하고, 4절 규칙과 5절 조합 단서로 2~3개씩 묶어 가설 1개를 만든다.
- AS-IS 3: 시험(3단계, main-agent): 조합 점검 질의 1회로 조합이 실행되고 해당 건이 있는지 본다.
- TO-BE:

```
2. 대입과 조합(2단계, topdown-hypothesizer): 넘겨받은 테이블에 패턴을 대입하고, 같은 대상에 함께 걸 수 있는 패턴들이 있으면 4절 규칙과 5절 조합 단서를 참고해 묶어 가설 1개를 만든다.
3. 시험(3단계, main-agent): 시나리오 SQL 의 건수 확인으로 조합이 실행되고 해당 건이 있는지 본다.
```

**② 25행**: 「데이터 이상징후 패턴(P-101 ~ P-141)은 Bottom-up 이 쓰며 …」 문장 가운데 앞 문장만 지운다.

- TO-BE:

```
- 패턴 page 의 「탐지 기법(SQL 형태)」 줄은 원본의 기법 분류와 SQL 골격만 옮긴 것이다.
```

**③ 29행 (2절 첫 문단 끝)**: 「넣을 수 없으면 위험 연결 점수를 1점으로 둔다(`okf/wiki/criteria/top-down.md`).」 문장을 지운다.

**④ 119행 (4절 첫 문장)**

- AS-IS: 조합은 … 함께 걸 수 있는 부정 패턴 2~3개다. 조합 하나가 시나리오 후보 하나가 된다. 유형 이름은 Bottom-up 의 데이터 이상징후 패턴 조합과 같다.
- TO-BE:

```
조합은 **같은 점검 대상**(같은 거래 행, 같은 행위자, 또는 업무 흐름으로 이어지는 거래)에 함께 걸 수 있는 부정 패턴들이다. 조합 하나가 시나리오 후보 하나가 된다.
```

**⑤ 130행**

- AS-IS: 조합의 패턴은 최대 3개다. 5절 조합 단서에 없는 조합도 위 규칙을 지키면 만들 수 있다.
- TO-BE:

```
- 5절 조합 단서에 없는 조합도 위 규칙을 지키면 만들 수 있다.
```

**⑥ 131~132행 「성립 확인」**: 두 줄에 걸친 문장이다.

- TO-BE:

```
- 성립 확인: 시나리오 SQL 의 건수 확인(`HIT_CNT`)이 0 보다 커야 한다. 0 이면 조건의 값·연결을 다시 보고, 가설의 뜻이 유지되는 범위에서 고친다.
```

**⑦ 133행 「단일 패턴 후보」**

- AS-IS: … 「단일」로 예비 시나리오에 둘 수 있다. 선별 기준의 위험 연결은 1점이다(`okf/wiki/criteria/top-down.md`).
- TO-BE:

```
- 단일 패턴 후보: 묶을 상대가 없는 패턴은 「단일」로 예비 시나리오에 둘 수 있다.
```

---

### 2-4. `okf/real-cases/index.md`

실제 사고 사례는 남긴다. 다만 Bottom-up 규칙이 이상징후 패턴 역인덱스를 가리키고 있어서 고친다.

**15행 「이용 규칙」 2번**

- AS-IS: **Bottom-up**: 가설을 세울 때 [patterns.md](patterns.md) 「데이터 이상징후 패턴 (P-101 ~ P-141)」 절의 역인덱스로 가설에 쓴 이상징후 패턴의 실제 사례를 확인한다. 동일 취약점에서 실제 사고가 난 신호는 가설 우선도가 높다.
- TO-BE:

```
2. **Bottom-up**: 찾은 이상치와 비슷한 신호가 남은 실제 사례가 있는지 사례 파일(fraud, expedient-practices, deficiencies)에서 확인한다. 같은 신호로 실제 사고가 난 적이 있으면 그 이상치를 먼저 쓴다.
```

---

### 2-5. `okf/real-cases/patterns.md` (패턴별 역인덱스)

**369행부터 끝까지**: 「## 데이터 이상징후 패턴 (P-101 ~ P-141)」 절을 통째로 지운다. 부정 패턴(P-001~P-032) 절은 그대로 둔다.

사례 파일(`fraud.md`, `expedient-practices.md`, `deficiencies.md`) 안의 P-1xx 표기는 사례의 태그일 뿐이라 그대로 둬도 된다. 일관성을 맞추려면 「관련 패턴」 칸에서 P-1xx 만 빼면 된다(선택).

---

## 3. 그대로 둘 것

| 파일 | 이유 |
|---|---|
| `okf/log.md` 13행 (risk-interpretation 언급) | 변경 이력이라 고치지 않는다 |
| `okf/glossary/biz-rules/index.md` | `tables/` 를 가리키는 줄이 없다 |
| `okf/glossary/biz-rules/GPPM/abnormal-inventory-management-rules.md` 212행 | 영문 원문의 단어 "criteria" 일 뿐, 폴더 링크가 아니다 |
| `okf/wiki/normal-patterns.md` | sql-query 의 「데이터 특성」 SQL 조건과 이상치 탐색의 제외 조건으로 계속 쓴다 |
| `okf/wiki/patterns/fraud/P-0xx.md` | Top-down 가설 생성에서 계속 참고한다. ACFE·COSO 줄도 문서에는 남겨 둔다(가설 출력에서만 뺐다) |
| `okf/real-cases/` 사례 파일 | Top-down 가설 생성과 Bottom-up 해석에서 계속 쓴다 |

---

## 4. 다 고친 뒤 확인

okf 폴더에서 아래 단어로 찾아 남은 곳이 없으면 된다. 3절 「그대로 둘 것」은 빼고 본다.

```
patterns/anomaly
risk-interpretation
wiki/criteria
biz-rules/tables
조합 점검
P-101 ~ P-141
```
