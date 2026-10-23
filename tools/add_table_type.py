# -*- coding: utf-8 -*-
"""
OKF 도메인 page 의 「## 테이블 목록」 표에 「유형 (table_type)」 칸을 넣는다.

- 유형 값은 각 테이블·뷰 문서(okf/schemas/<OWNER>/tables|views/<이름>.md) frontmatter 의
  `table_type` 을 그대로 쓴다. 문서가 없거나 table_type 이 없으면 빈칸으로 둔다.
- 표 머리는 `| 테이블 | 유형 (table_type) | 설명 (table_rule) |` 가 된다(테이블 칸 바로 뒤에 넣는다).
- 이미 유형 칸이 있으면 칸을 더 만들지 않고 값만 다시 채운다(여러 번 실행해도 같다).
- 「## 테이블 목록」 표 밖의 내용, 줄바꿈 방식(CRLF/LF), BOM 은 바꾸지 않는다.

사용법 (okf 폴더가 있는 곳에서):
    python add_table_type.py okf            # 실제로 고친다
    python add_table_type.py okf --dry-run  # 고치지 않고 결과만 본다
"""
import argparse
import re
import sys
from pathlib import Path

SECTION_RE = re.compile(r"^##\s+테이블\s*목록\s*$")
NEXT_SECTION_RE = re.compile(r"^#{1,2}\s")
LINK_RE = re.compile(r"\]\(([^)\s]+)\)")
NAME_RE = re.compile(r"\[([^\]]+)\]")
NEW_HEADER = "유형 (table_type)"


def read_text(path):
    data = path.read_bytes()
    bom = data.startswith(b"\xef\xbb\xbf")
    if bom:
        data = data[3:]
    # 깨진 바이트가 있어도 그대로 보존한다(surrogateescape)
    text = data.decode("utf-8", errors="surrogateescape")
    return text, bom


def write_text(path, text, bom):
    data = text.encode("utf-8", errors="surrogateescape")
    if bom:
        data = b"\xef\xbb\xbf" + data
    path.write_bytes(data)


def frontmatter_value(text, key):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for line in lines[1:]:
        if line.strip() == "---":
            break
        m = re.match(r"^" + re.escape(key) + r"\s*:\s*(.*)$", line)
        if m:
            v = m.group(1).split(" #")[0].strip().strip("'\"").strip()
            return v or None
    return None


def build_type_map(okf):
    by_path, by_name = {}, {}
    for doc in sorted((okf / "schemas").glob("*/*/*.md")):
        if doc.parent.name not in ("tables", "views"):
            continue
        text, _ = read_text(doc)
        ttype = frontmatter_value(text, "table_type") or ""
        rel = "/" + doc.relative_to(okf).as_posix()
        by_path[rel.lower()] = ttype
        owner = doc.parent.parent.name.upper()
        name = doc.stem.upper()
        by_name[name] = ttype if name not in by_name else by_name[name]
        by_name[f"{owner}.{name}"] = ttype
        qn = frontmatter_value(text, "query_name")
        if qn:
            by_name[qn.upper()] = ttype
    return by_path, by_name


def pipe_positions(line):
    """이스케이프(\\|)되지 않고 인라인 코드(`) 밖에 있는 | 위치."""
    pos, in_code, i = [], False, 0
    while i < len(line):
        c = line[i]
        if c == "\\":
            i += 2
            continue
        if c == "`":
            in_code = not in_code
        elif c == "|" and not in_code:
            pos.append(i)
        i += 1
    return pos


def lookup(first_cell, by_path, by_name):
    m = LINK_RE.search(first_cell)
    if m:
        target = m.group(1).split("#")[0]
        if not target.startswith("/"):
            target = "/" + target.lstrip("./")
        if target.startswith("/okf/"):
            target = target[4:]
        if target.lower() in by_path:
            return by_path[target.lower()], True
    m = NAME_RE.search(first_cell)
    name = (m.group(1) if m else first_cell).strip().strip("`").strip().upper()
    if name in by_name:
        return by_name[name], True
    return "", False


def process_domain(path, by_path, by_name, dry_run):
    text, bom = read_text(path)
    lines = text.splitlines(keepends=True)
    stats = {"rows": 0, "typed": 0, "blank": [], "nodoc": [], "status": "목록 없음"}

    start = next((i for i, l in enumerate(lines) if SECTION_RE.match(l.rstrip("\r\n"))), None)
    if start is None:
        return stats
    end = next((i for i in range(start + 1, len(lines)) if NEXT_SECTION_RE.match(lines[i])), len(lines))
    table_idx = [i for i in range(start + 1, end) if lines[i].lstrip().startswith("|")]
    if len(table_idx) < 2:
        stats["status"] = "표 없음"
        return stats

    header_i, sep_i, row_is = table_idx[0], table_idx[1], table_idx[2:]

    def body(i):
        raw = lines[i]
        stripped = raw.rstrip("\r\n")
        return stripped, raw[len(stripped):]

    hdr, hdr_nl = body(header_i)
    hp = pipe_positions(hdr)
    cells = [hdr[hp[k] + 1:hp[k + 1]].strip() for k in range(len(hp) - 1)]
    existing = next((k for k, c in enumerate(cells) if c.startswith("유형")), None)

    new_lines = list(lines)
    if existing is None:
        # 첫 칸(테이블) 뒤, 두 번째 | 자리에 새 칸을 넣는다
        def insert(line, value):
            p = pipe_positions(line)
            if len(p) < 2:
                return line
            return line[:p[1]] + "| " + value + " " + line[p[1]:]

        new_lines[header_i] = insert(hdr, NEW_HEADER) + hdr_nl
        sep, sep_nl = body(sep_i)
        p = pipe_positions(sep)
        new_lines[sep_i] = (sep[:p[1]] + "|---" + sep[p[1]:] if len(p) >= 2 else sep) + sep_nl
        col = None
        stats["status"] = "칸 추가"
    else:
        insert = None
        col = existing
        stats["status"] = "값 다시 채움"

    for i in row_is:
        row, nl = body(i)
        p = pipe_positions(row)
        if len(p) < 2:
            continue
        first = row[p[0] + 1:p[1]]
        ttype, found = lookup(first, by_path, by_name)
        name = (NAME_RE.search(first).group(1) if NAME_RE.search(first) else first.strip())
        stats["rows"] += 1
        if not found:
            stats["nodoc"].append(name)
        elif not ttype:
            stats["blank"].append(name)
        else:
            stats["typed"] += 1
        if col is None:
            new_lines[i] = insert(row, ttype) + nl
        elif len(p) > col + 1:
            new_lines[i] = row[:p[col] + 1] + " " + ttype + " " + row[p[col + 1]:] + nl

    new_text = "".join(new_lines)
    if new_text == text:
        stats["status"] += "(변경 없음)"
    elif not dry_run:
        write_text(path, new_text, bom)
    return stats


def main():
    ap = argparse.ArgumentParser(description="도메인 page 「## 테이블 목록」에 유형 (table_type) 칸 넣기")
    ap.add_argument("okf", nargs="?", default="okf", help="okf 폴더 경로 (기본: okf)")
    ap.add_argument("--dry-run", action="store_true", help="파일을 고치지 않고 결과만 출력")
    args = ap.parse_args()

    okf = Path(args.okf)
    if not (okf / "domains").is_dir() or not (okf / "schemas").is_dir():
        sys.exit(f"[오류] {okf} 아래에 domains/ 와 schemas/ 가 없습니다. okf 폴더 경로를 확인하세요.")

    by_path, by_name = build_type_map(okf)
    print(f"테이블·뷰 문서 {len(by_path)}건 읽음 (table_type 있는 문서 {sum(1 for v in by_path.values() if v)}건)")
    print("모드:", "확인만(--dry-run)" if args.dry_run else "파일 수정")
    print()

    total = {"rows": 0, "typed": 0}
    for path in sorted((okf / "domains").glob("*.md")):
        if path.name == "index.md":
            continue
        try:
            s = process_domain(path, by_path, by_name, args.dry_run)
        except Exception as e:  # 한 파일이 실패해도 나머지는 처리한다
            print(f"- {path.name}: [실패] {e}")
            continue
        total["rows"] += s["rows"]
        total["typed"] += s["typed"]
        print(f"- {path.name}: {s['status']} / 행 {s['rows']}, 유형 채움 {s['typed']}")
        if s["blank"]:
            print(f"    table_type 없음(빈칸): {', '.join(s['blank'])}")
        if s["nodoc"]:
            print(f"    테이블 문서 없음(빈칸): {', '.join(s['nodoc'])}")
    print()
    print(f"합계: 행 {total['rows']}, 유형 채움 {total['typed']}, 빈칸 {total['rows'] - total['typed']}")


if __name__ == "__main__":
    main()
