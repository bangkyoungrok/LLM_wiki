# 값 확인 (value linking)

문서를 먼저 본다: 테이블 문서 `# T2S 힌트`·코드/참조 열 → `okf/codes/` 코드 문서 → `okf/references/code-value-samples.md` → 용어집(`okf/glossary/index.md`, 예: SEUK = `CMCD`='C430'). 문서로 정해지지 않을 때만 `execute_sql` 으로 확인한다. 여러 후보는 **한 문장에 묶어** 한 번에 확인한다. `size:l`·`size:xl` 테이블에는 기간 조건을 함께 넣는다. `<…>` 는 꺾쇠까지 바꾼다.

## 값 일치 (코드·번호) — 1 이 나온 컬럼이 그 값의 컬럼

```sql
SELECT MAX(CASE WHEN <컬럼1> = '<값>' THEN 1 ELSE 0 END) AS <컬럼1>,
       MAX(CASE WHEN <컬럼2> = '<값>' THEN 1 ELSE 0 END) AS <컬럼2>
FROM <query_name>
WHERE <컬럼1> = '<값>' OR <컬럼2> = '<값>'
```

## 여러 후보 테이블에 같은 값이 있는지

```sql
SELECT '<후보1>' AS TBL, CASE WHEN EXISTS (SELECT 1 FROM <후보1> WHERE <컬럼> = '<값>') THEN 1 ELSE 0 END AS HIT FROM DUAL
UNION ALL
SELECT '<후보2>', CASE WHEN EXISTS (SELECT 1 FROM <후보2> WHERE <컬럼> = '<값>') THEN 1 ELSE 0 END FROM DUAL
```

## 부분 일치 (이름) — 값 일치로 못 찾은 이름만

```sql
SELECT DISTINCT <컬럼> FROM <query_name>
WHERE UPPER(<컬럼>) LIKE UPPER('%<값>%')
ORDER BY <컬럼> FETCH FIRST 10 ROWS ONLY
```

## 코드값 목록 (코드인지 한글 라벨인지)

```sql
SELECT <코드 컬럼>, COUNT(*) AS cnt FROM <query_name>
WHERE <기간 조건>
GROUP BY <코드 컬럼> ORDER BY cnt DESC FETCH FIRST 20 ROWS ONLY
```

## 날짜 형식 (문서에 없을 때)

```sql
SELECT MIN(LENGTH(<날짜>)) AS min_len, MAX(LENGTH(<날짜>)) AS max_len, MIN(<날짜>) AS min_val, MAX(<날짜>) AS max_val
FROM (SELECT <날짜> FROM <query_name> WHERE <날짜> IS NOT NULL FETCH FIRST 1000 ROWS ONLY)
```

## 결과 처리

| 결과 | 처리 |
|---|---|
| 1 이 나온 컬럼 하나 | 그 컬럼으로 확정 |
| 1 이 나온 컬럼 둘 이상 / 부분 일치 결과 여러 개 | 확정하지 않고 모호 후보로 |
| 0행 또는 모두 0 | 다른 후보 컬럼 확인 → 이름이면 부분 일치 1회, 코드면 코드값 목록 1회. 그래도 없으면 「미연결」. 값이 없다는 것만으로 데이터가 없다고 답하지 않는다 |
| ORA-00904/00942 | 이름을 문서와 대조해 고쳐 1회 재실행 |
| 그 밖의 오류·시간 초과 | 재실행하지 않고 「미연결」 + 오류 문구 |