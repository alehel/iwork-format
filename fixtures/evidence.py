"""Check the differences the experiments' Evidence tables state against the sample documents.

Usage: python3 -I fixtures/evidence.py [NNNN ...]      check, and write fixtures/EVIDENCE.json
       python3 -I fixtures/evidence.py --diff A B      list what differs between two documents, to write a table from

An experiment's `## Evidence` section is a table with the columns File, Compared with, Difference and
Shows. A document is named as it is in samples/, without the experiment's own number: `underline.pages`,
`0008/middle.pages`. In the Difference column each piece of `code` is a statement this script checks:

  `2021 11.11 = 1`            some record of type 2021 holds 1 at field path 11.11
  `2052#1732770 4: "a" → "b"` that record (or, without #ID, some record of the type) held "a" and holds "b":
                              fewer hold the first value than in the document compared with, and more the second.
                              `absent` as the first value checks the second alone, and the other way round
  `records 212: 0 → 1`        how many records of a type each document holds
  `part .iwpv2: absent → present`   a file in the package; `*` stands for any characters
  `same records`              every record has the same ID, type and bytes
  `same bytes`                the two files are identical

Any other code in that column is an error.

A cell that starts with "Only" also states that nothing else differs: no other field of any record, no
record more or less, and no other file but the previews. Values are numbers (with a point for a float or
double, compared to within 0.01), "text" with JSON escapes, or `absent`. A Keynote document that was made
again with the test theme is checked in both versions, since the remake is the one published; a cell that
says "original only" states something the remake doesn't show, and is checked in the original alone.

Nothing is written unless every statement holds. Encrypted documents are read with their test passwords
(fixtures/build.py), which needs target/release/iwork-probe. The site's builder compares the tables with
EVIDENCE.json, so a table can't change without this being run. Only the standard library is used.
"""
import collections
import fnmatch
import hashlib
import importlib.util
import json
import os
import re
import struct
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("build", os.path.join(ROOT, "fixtures", "build.py"))
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)
w = build.writer
OUT = os.path.join(ROOT, "fixtures", "EVIDENCE.json")
COLUMNS = ["File", "Compared with", "Difference", "Shows"]
NUMBER = r"-?\d+(?:\.\d+)?"
VALUE = rf'(?:"(?:[^"\\]|\\.)*"|{NUMBER}|absent)'
FIELD = re.compile(rf"^(\d+)(?:#(\d+))? (\d+(?:\.\d+)*)(?: = ({VALUE})|: ({VALUE}) → ({VALUE}))$")
RECORDS = re.compile(r"^records (\d+): (\d+) → (\d+)$")
ORIGINAL_ONLY = re.compile(r"\boriginal only\b")
PART = re.compile(r"^part (\S.*): (absent|present) → (absent|present)$")


class Document:
    """A sample's package files and records, by path in samples/."""

    def __init__(self, rel):
        self.rel = rel
        path = os.path.join(ROOT, rel)
        if os.path.isdir(path):
            parts = list(build.folder_parts(path))
            h = hashlib.sha256()
            for name in build.folder_files(path):
                with open(os.path.join(path, name), "rb") as f:
                    h.update(name.encode() + b"\0" + f.read())
            self.sha = h.hexdigest()
            parts.append(("Index.zip", b""))  # read into its parts above; here only to say that it's there
        else:
            password = build.password(rel)
            with open(path, "rb") as f:
                self.sha = hashlib.sha256(f.read()).hexdigest()
            parts = list(build.decrypted_parts(path, password) if password else build.plain_parts(path))
        self.parts = {n: d for n, d in parts if not n.endswith("/")}
        self.records = {}  # (ID, payload number) -> (type, payload)
        for name, data in self.parts.items():
            if not name.endswith(".iwa"):
                continue
            for header, payloads in w.records(data):
                infos = [w.parse_message(v) for f, _, v in header if f == 2]
                for n, (info, payload) in enumerate(zip(infos, payloads)):
                    kind = next(w.read_varint(v, 0)[0] for f, _, v in info if f == 1)
                    self.records[(w.record_id(header), n)] = (kind, payload)
        if not self.records:
            raise SystemExit(f"{rel}: no records could be read")

    def values(self, kind, object_id, path):
        """Every (wire type, raw value) at a field path, one list per record of the type."""
        found = []
        for (rid, _), (k, payload) in self.records.items():
            if k == kind and object_id in (None, rid):
                found.append(at(payload, path))
        return found


def at(payload, path):
    try:
        fields = [(t, v) for f, t, v in w.parse_message(payload) if f == path[0]]
    except Exception:
        return []
    if len(path) == 1:
        return fields
    return [x for t, v in fields if t == 2 for x in at(v, path[1:])]


def matches(item, literal):
    wire, raw = item
    if literal.startswith('"'):
        return wire == 2 and raw == json.loads(literal).encode("utf-8")
    if "." in literal:
        if wire not in (1, 5):
            return False
        return abs(struct.unpack("<d" if wire == 1 else "<f", raw)[0] - float(literal)) <= 0.01
    if wire != 0:
        return False
    n = w.read_varint(raw, 0)[0]
    return int(literal) in (n, n - (1 << 64))


def holding(doc, kind, object_id, path, literal):
    """How many records of the type (or whether that record) hold a value at the path."""
    lists = doc.values(kind, object_id, path)
    if literal == "absent":
        return sum(not x for x in lists)
    return sum(any(matches(i, literal) for i in x) for x in lists)


def is_preview(name):
    return os.path.basename(name).startswith("preview")


def leaf_paths(a, b, path=()):
    """The field paths where two payloads differ, as deep as both parse as messages."""
    if a == b:
        return []
    try:
        fa, fb = w.parse_message(a), w.parse_message(b)
        # Plain text can pass for a message, read past its end: only what encodes to the same bytes is one.
        if any(not 0 < f <= 3000 or (t in (1, 5) and len(v) != (8 if t == 1 else 4)) for f, t, v in fa + fb):
            raise ValueError
        if w.serialize_message(fa) != bytes(a) or w.serialize_message(fb) != bytes(b):
            raise ValueError
    except Exception:
        return [path]
    groups = [collections.defaultdict(list), collections.defaultdict(list)]
    for group, fields in zip(groups, (fa, fb)):
        for f, t, v in fields:
            group[f].append((t, v))
    out = []
    for f in sorted(set(groups[0]) | set(groups[1])):
        x, y = groups[0][f], groups[1][f]
        if x == y:
            continue
        if len(x) != len(y):
            out.append(path + (f,))
            continue
        for (t, v), (u, z) in zip(x, y):
            if (t, v) != (u, z):
                out += leaf_paths(v, z, path + (f,)) if t == u == 2 and v and z else [path + (f,)]
    return out or [path]  # the same fields in another order


def differences(base, doc):
    """Every difference: ("field", type, ID, path), ("record", type, ID, +1 or -1) or ("part", name)."""
    out = []
    for key in sorted(set(base.records) | set(doc.records)):
        a, b = base.records.get(key), doc.records.get(key)
        if a == b:
            continue
        if a is None or b is None or a[0] != b[0]:
            out.append(("record", (b or a)[0], key[0], 1 if a is None else -1))
        else:
            out += [("field", a[0], key[0], p) for p in leaf_paths(a[1], b[1])]
    for name in sorted(set(base.parts) | set(doc.parts)):
        if name.endswith(".iwa") or is_preview(name):
            continue
        if base.parts.get(name) != doc.parts.get(name):
            out.append(("part", name))
    return out


def check(statement, base, doc):
    """Why a statement doesn't hold, or None when it does."""
    if statement == "same records":
        return None if base.records == doc.records else "the records differ"
    if statement == "same bytes":
        return None if base.sha == doc.sha else "the files differ"
    m = RECORDS.match(statement)
    if m:
        have = [sum(k == int(m[1]) for k, _ in d.records.values()) for d in (base, doc)]
        return None if have == [int(m[2]), int(m[3])] else f"there are {have[0]} and {have[1]}"
    m = PART.match(statement)
    if m:
        have = ["present" if any(fnmatch.fnmatch(n, m[1]) for n in d.parts) else "absent" for d in (base, doc)]
        return None if have == [m[2], m[3]] else f"it is {have[0]}, then {have[1]}"
    m = FIELD.match(statement)
    if not m:
        raise SystemExit(f"{doc.rel}: not a statement this script can check: `{statement}`")
    kind, oid, path = int(m[1]), int(m[2]) if m[2] else None, [int(p) for p in m[3].split(".")]
    if m[4]:
        return None if holding(doc, kind, oid, path, m[4]) else "no record holds it"
    if base is None:
        raise SystemExit(f"{doc.rel}: `{statement}` needs a document to compare with")
    old, new = ([holding(d, kind, oid, path, v) for d in (base, doc)] for v in (m[5], m[6]))
    problems = []
    if m[5] != "absent" and not old[0] > old[1]:
        problems.append(f"{old[0]} then {old[1]} hold {m[5]}")
    if m[6] != "absent" and not new[0] < new[1]:
        problems.append(f"{new[0]} then {new[1]} hold {m[6]}")
    if oid is not None:
        if m[5] == "absent" and not old[0]:
            problems.append("the record held a value already")
        if m[6] == "absent" and not new[1]:
            problems.append("the record still holds a value")
    return "; ".join(problems) or None


def uncovered(statements, base, doc):
    """The differences that no statement of an "Only" row names."""
    fields, parts, counted = [], [], set()
    for s in statements:
        if FIELD.match(s):
            m = FIELD.match(s)
            fields.append((int(m[1]), int(m[2]) if m[2] else None, tuple(int(p) for p in m[3].split("."))))
        elif PART.match(s):
            parts.append(PART.match(s)[1])
        elif RECORDS.match(s):
            counted.add(int(RECORDS.match(s)[1]))
    left = []
    for d in differences(base, doc):
        if d[0] == "part" and any(fnmatch.fnmatch(d[1], p) for p in parts):
            continue
        if d[0] == "record" and d[1] in counted:
            continue
        if d[0] == "field" and any(k == d[1] and i in (None, d[2]) and d[3][:len(p)] == p for k, i, p in fields):
            continue
        left.append(d)
    return left


def show(d):
    if d[0] == "field":
        return f"{d[1]}#{d[2]} {'.'.join(map(str, d[3]))}"
    return f"part {d[1]}" if d[0] == "part" else f"{'one more' if d[3] > 0 else 'one less'} record {d[1]}#{d[2]}"


def evidence_rows(md):
    """The Evidence table's rows, or None when the experiment has none."""
    section = re.search(r"^## Evidence\s*$(.*?)(?=^## |\Z)", md, re.M | re.S)
    if not section:
        return None
    rows = [[c.strip() for c in line.strip().strip("|").split("|")]
            for line in section[1].splitlines() if line.startswith("|")]
    if len(rows) < 3 or rows[0] != COLUMNS or any(len(r) != 4 for r in rows):
        raise SystemExit(f"the Evidence table needs the columns {' | '.join(COLUMNS)}")
    return rows[2:]


def sample(cell, number):
    """The path in samples/ a File or Compared with cell names, or None for a cell that names none."""
    m = re.match(r"^`([^`]+)`", cell)
    if not m:
        return None
    name = m[1] if re.match(r"^(?:\d{4}|theme|release|resave)/", m[1]) else f"{number}/{m[1]}"
    return "samples/" + name


def remake(rel):
    """The test-theme version of a Keynote sample, if there is one."""
    new = re.sub(r"^samples/(?=\d{4}/)", "samples/theme/", rel)
    return new if rel.endswith(".key") and new != rel and os.path.exists(os.path.join(ROOT, new)) else None


def check_experiment(number, md, load):
    """The experiment's checked rows for EVIDENCE.json, and what doesn't hold."""
    out, problems = [], []
    for file_cell, base_cell, difference, shows in evidence_rows(md):
        rel, base_rel = sample(file_cell, number), sample(base_cell, number)
        if not rel:
            raise SystemExit(f"{number}: the File column names no file: {file_cell}")
        statements = re.findall(r"`([^`]+)`", difference)
        only = bool(re.match(r"^Only\b", difference))
        if base_rel is None and (only or any(s.startswith(("same ", "records ", "part ")) for s in statements)):
            raise SystemExit(f"{number}: {rel}: nothing to compare with")
        pairs = [(rel, base_rel)]
        if remake(rel) and not ORIGINAL_ONLY.search(difference):
            pairs.append((remake(rel), base_rel and (remake(base_rel) or base_rel)))
        row = {"file": rel, "compared": base_rel, "difference": difference, "documents": []}
        for r, b in pairs:
            doc, base = load(r), load(b) if b else None
            for s in statements:
                why = check(s, base, doc)
                if why:
                    problems.append(f"{number}: {r}: `{s}`: {why}")
            if only:
                left = uncovered(statements, base, doc)
                if left:
                    problems.append(f"{number}: {r}: also differs: " + "; ".join(map(show, left[:8])) + (f" and {len(left) - 8} more" if len(left) > 8 else ""))
            row["documents"].append({"path": r, "sha256": doc.sha, **({"compared": b, "compared_sha256": base.sha} if base else {})})
        out.append(row)
    return out, problems


def main(argv):
    if argv[:1] == ["--diff"]:
        for d in differences(Document(argv[1]), Document(argv[2])):
            print(show(d))
        return
    cache = {}

    def load(rel):
        if rel not in cache:
            cache[rel] = Document(rel)
        return cache[rel]

    results, problems, statements = {}, [], 0
    if argv and os.path.exists(OUT):
        with open(OUT, encoding="utf-8") as f:
            results = json.load(f)
    for name in sorted(os.listdir(os.path.join(ROOT, "experiments"))):
        number = name[:4]
        if not re.match(r"^\d{4}-.*\.md$", name) or (argv and number not in argv):
            continue
        with open(os.path.join(ROOT, "experiments", name), encoding="utf-8") as f:
            md = f.read()
        if evidence_rows(md) is None:
            results.pop(number, None)
            continue
        cache.clear()
        results[number], found = check_experiment(number, md, load)
        problems += found
        n = sum(len(re.findall(r"`[^`]+`", r["difference"])) for r in results[number])
        statements += n
        print(f"{number}: {len(results[number])} documents, {n} statements" + (f", {len(found)} problems" if found else ""))
    for p in problems:
        print(p, file=sys.stderr)
    if problems:
        sys.exit(f"{len(problems)} problems; fixtures/EVIDENCE.json not written")
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(dict(sorted(results.items())), f, indent=1, ensure_ascii=False)
        f.write("\n")
    print(f"{statements} statements hold; wrote fixtures/EVIDENCE.json")


if __name__ == "__main__":
    main(sys.argv[1:])
