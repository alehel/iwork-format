"""Check the differences the experiments' Evidence tables state against the sample documents.

Usage: python3 -I fixtures/evidence.py [NNNN ...]      check, and write fixtures/EVIDENCE.json
       python3 -I fixtures/evidence.py --check NNNN ... check only
       python3 -I fixtures/evidence.py --diff A B      list what differs between two documents, to write a table from

An experiment's `## Evidence` section is a table with the columns File, Compared with, Difference and
Shows. A document is named as it is in samples/, without the experiment's own number: `underline.pages`,
`0008/middle.pages`. In the Difference column each piece of `code` is a statement this script checks:

  `2021 11.11 = 1`            some record of type 2021 holds 1 at field path 11.11
  `2021 11.11 ≠ 1`            none does
  `2001 3 ~ "tre"`            some record holds bytes containing these there
  `2052#1732770 4: "a" → "b"` that record (or, without #ID, some record of the type) held "a" and holds "b":
                              fewer hold the first value than in the document compared with, and more the second.
                              `absent` as the first value checks the second alone, and the other way round
  `2001 5.1: ×1 → ×3`         how many times the field occurs in all records of the type (or in that record)
  `6002#7 3: changed`         it holds other values than in the document compared with, or in another order
  `records 212: 0 → 1`        how many records of a type each document holds
  `header 2001#5 5: 7 → 9`    as for a record's fields, but in its part of the record header (field 2 there)
  `part .iwpv2: absent → present`   a file in the package; `*` stands for any characters
  `part X: changed`, `part X: same`, `part X ~ "text"`   its bytes, or an .iwa part's decoded ones
  `order Index/Document.iwa: changed`   the records of a part come in another order, or in another part
  `same records`              every record has the same ID, type and bytes
  `same parts`                every file in the package has the same bytes, once decoded
  `same bytes`                the two files are identical
  `unreadable`                the file can't be read as records

Any other code in that column is an error. Values are numbers (with a point for a float or double, compared
to half of the last decimal given), "text" with JSON escapes, x"hex", `absent` or `present`. Where a File cell
holds a pattern, `c-*.pages` (`*` within a folder, `**` across them), the row is about every document it matches;
a pattern in Compared with stands for the document with the same name parts. An experiment without documents of its own says so instead of, or before,
a table: the section starts with "No documents of its own".

A cell that starts with "Only" also states that nothing else differs: no other field of any record or
its header, no record more or less or in another order, and no other file but the previews. A Keynote document that was made
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
import zlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("build", os.path.join(ROOT, "fixtures", "build.py"))
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)
w = build.writer
EXT = (".pages", ".key", ".numbers")
OUT = os.path.join(ROOT, "fixtures", "EVIDENCE.json")
COLUMNS = ["File", "Compared with", "Difference", "Shows"]
NUMBER = r"-?\d+(?:\.\d+)?"
TEXT = r'"(?:[^"\\]|\\.)*"'
VALUE = rf'(?:{TEXT}|x"[0-9a-f ]*"|{NUMBER}|absent|present)'
FIELD = re.compile(rf"^(header )?(\d+)(?:#(\d+))? (\d+(?:\.\d+)*)(?: (=|≠|~) ({VALUE})|: ({VALUE}) → ({VALUE})|: ×(\d+) → ×(\d+)|: (changed))$")
RECORDS = re.compile(r"^records (\d+): (\d+) → (\d+)$")
PART = re.compile(rf"^part (\S.*?)(?:: (absent|present) → (absent|present)|: (changed|same)| ~ ({TEXT}))$")
ORDER = re.compile(r"^order (\S+): changed$")
ORIGINAL_ONLY = re.compile(r"\boriginal only\b")


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
            password = build.password(rel) or build.password(re.sub(r"^samples/(?=\d{4}/)", "samples/theme/", rel))
            with open(path, "rb") as f:
                self.sha = hashlib.sha256(f.read()).hexdigest()
            parts = list(build.decrypted_parts(path, password) if password else file_parts(path))
        self.parts = {n: d for n, d in parts if not n.endswith("/")}
        self.read(rel)

    def read(self, rel):
        self.records, self.headers, self.order, self.error = {}, {}, {}, None  # records: (ID, payload number) -> (type, payload)
        for name, data in self.parts.items():
            if not name.endswith(".iwa"):
                continue
            try:
                found = w.records(data)
            except Exception as why:
                self.error = f"{name}: {why!r}"
                continue
            for header, payloads in found:
                infos = [w.parse_message(v) for f, _, v in header if f == 2]
                for n, (info, payload) in enumerate(zip(infos, payloads)):
                    kind = next(w.read_varint(v, 0)[0] for f, _, v in info if f == 1)
                    key = (w.record_id(header), n)
                    self.records[key] = (kind, payload)
                    self.headers[key] = (kind, w.serialize_message([x for x in info if x[0] != 3]))  # 3 is the length
                    self.order.setdefault(name, []).append(key)
        if not self.records and not self.error:
            self.error = "no records"

    def values(self, kind, object_id, path, header=False):
        """Every (wire type, raw value) at a field path, one list per record of the type."""
        found = []
        for (rid, _), (k, payload) in (self.headers if header else self.records).items():
            if k == kind and object_id in (None, rid):
                found.append(at(payload, path))
        return found


def file_parts(path):
    """A ZIP document's files, .iwa parts decoded; what can't be decoded as it is stored."""
    with zipfile.ZipFile(path) as z:
        for info in z.infolist():
            name = build.fix_name(info)
            try:
                data = z.read(info)
            except zipfile.BadZipFile:  # a UTF-8 name that one of its two headers doesn't mark as UTF-8 (container.md)
                with open(path, "rb") as f:
                    f.seek(info.header_offset + 26)
                    skip = struct.unpack("<HH", f.read(4))
                    f.seek(sum(skip), 1)
                    data = f.read(info.compress_size)
                data = zlib.decompress(data, -15) if info.compress_type == zipfile.ZIP_DEFLATED else data
            if name.endswith(".iwa"):
                try:
                    data = w.iwa_decode(data)
                except Exception:
                    pass
            yield name, data


def at(payload, path):
    try:
        fields = [(t, v) for f, t, v in w.parse_message(payload) if f == path[0]]
    except Exception:
        return []
    if len(path) == 1:
        return fields
    return [x for t, v in fields if t == 2 for x in at(v, path[1:])]


def raw_bytes(literal):
    return bytes.fromhex(literal[2:-1]) if literal.startswith("x") else json.loads(literal).encode("utf-8")


def matches(item, literal):
    wire, raw = item
    if literal == "present":
        return True
    if literal[0] in '"x':
        return wire == 2 and raw == raw_bytes(literal)
    if "." in literal:
        if wire not in (1, 5):
            return False
        close = 0.5 * 10 ** -len(literal.split(".")[1]) * 1.0001
        return abs(struct.unpack("<d" if wire == 1 else "<f", raw)[0] - float(literal)) <= close
    if wire != 0:
        return False
    n = w.read_varint(raw, 0)[0]
    return int(literal) in (n, n - (1 << 64))


def holding(doc, kind, object_id, path, literal, header=False):
    """How many records of the type (or whether that record) hold a value at the path."""
    lists = doc.values(kind, object_id, path, header)
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
        if any(not 0 < f <= 20000 or (t in (1, 5) and len(v) != (8 if t == 1 else 4)) for f, t, v in fa + fb):
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
    """Every difference: ("field" or "header", type, ID, path), ("record", type, ID, +1 or -1), ("order", part) or
    ("part", name)."""
    out = []
    for key in sorted(set(base.records) | set(doc.records)):
        a, b = base.records.get(key), doc.records.get(key)
        if a is None or b is None or a[0] != b[0]:
            out.append(("record", (b or a)[0], key[0], 1 if a is None else -1 if b is None else 0))
            continue
        if a != b:
            out += [("field", a[0], key[0], p) for p in leaf_paths(a[1], b[1])]
        if base.headers[key] != doc.headers[key]:
            out += [("header", a[0], key[0], p) for p in leaf_paths(base.headers[key][1], doc.headers[key][1])]
    for name in sorted(set(base.order) & set(doc.order)):
        x, y = base.order[name], doc.order[name]
        if [k for k in x if k in doc.records] != [k for k in y if k in base.records]:
            out.append(("order", name))
    for name in sorted(set(base.parts) | set(doc.parts)):
        if is_preview(name) or (name in base.order and name in doc.order):
            continue
        if base.parts.get(name) != doc.parts.get(name):
            out.append(("part", name))
    return out


def count(doc, m):
    """How many times the field of a FIELD statement occurs."""
    return sum(map(len, doc.values(int(m[2]), int(m[3]) if m[3] else None, [int(p) for p in m[4].split(".")], bool(m[1]))))


def check(statement, base, doc):
    """Why a statement doesn't hold, or None when it does."""
    if statement == "unreadable":
        return None if doc.error else "it can be read"
    if statement == "same bytes":
        return None if base.sha == doc.sha else "the files differ"
    if statement == "same parts":
        return None if base.parts == doc.parts else "these differ: " + ", ".join(
            n for n in sorted(set(base.parts) | set(doc.parts)) if base.parts.get(n) != doc.parts.get(n))[:200]
    m = PART.match(statement)
    if m:
        found = [{n: v for n, v in d.parts.items() if fnmatch.fnmatch(n, m[1])} if d else {} for d in (base, doc)]
        if m[5]:
            return None if any(raw_bytes(m[5]) in v for v in found[1].values()) else "it doesn't hold that"
        if m[4]:
            if not found[0] and not found[1]:
                return "there is no such file"
            return None if (found[0] == found[1]) == (m[4] == "same") else f"it is {'the same' if m[4] == 'changed' else 'changed'}"
        have = ["present" if f else "absent" for f in found]
        return None if have == [m[2], m[3]] else f"it is {have[0]}, then {have[1]}"
    if doc.error:
        return f"the document can't be read: {doc.error}"
    if statement == "same records":
        return None if base.records == doc.records else "the records differ"
    m = ORDER.match(statement)
    if m:
        return None if ("order", m[1]) in differences(base, doc) else "the records are in the same order"
    m = RECORDS.match(statement)
    if m:
        have = [sum(k == int(m[1]) for k, _ in d.records.values()) for d in (base, doc)]
        return None if have == [int(m[2]), int(m[3])] else f"there are {have[0]} and {have[1]}"
    m = FIELD.match(statement)
    if not m:
        raise SystemExit(f"{doc.rel}: not a statement this script can check: `{statement}`")
    header, kind, oid, path = bool(m[1]), int(m[2]), int(m[3]) if m[3] else None, [int(p) for p in m[4].split(".")]
    if m[5] == "~":
        want = raw_bytes(m[6])
        return None if any(t == 2 and want in v for x in doc.values(kind, oid, path, header) for t, v in x) else "no record holds that"
    if m[5]:
        n = holding(doc, kind, oid, path, m[6], header)
        if not doc.values(kind, oid, path, header):
            return "there is no such record"
        return None if bool(n) == (m[5] == "=") else f"{n} records hold it"
    if base is None:
        raise SystemExit(f"{doc.rel}: `{statement}` needs a document to compare with")
    if base.error:
        return f"the document compared with can't be read: {base.error}"
    if m[11]:
        have = [[x for v in d.values(kind, oid, path, header) for x in v] for d in (base, doc)]
        have = have if oid is not None else [sorted(x) for x in have]  # in one record the order counts too
        return None if have[0] != have[1] else "it holds the same values"
    if m[9]:
        have = [count(d, m) for d in (base, doc)]
        return None if have == [int(m[9]), int(m[10])] else f"it occurs {have[0]} and {have[1]} times"
    old, new = ([holding(d, kind, oid, path, v, header) for d in (base, doc)] for v in (m[7], m[8]))
    problems = []
    if m[7] != "absent" and not old[0] > old[1]:
        problems.append(f"{old[0]} then {old[1]} hold {m[7]}")
    if m[8] != "absent" and not new[0] < new[1]:
        problems.append(f"{new[0]} then {new[1]} hold {m[8]}")
    if oid is not None:
        if m[7] == "absent" and not old[0] and base.values(kind, oid, path, header):
            problems.append("the record held a value already")
        if m[8] == "absent" and not new[1]:
            problems.append("the record still holds a value")
    return "; ".join(problems) or None


def uncovered(statements, base, doc):
    """The differences that no statement of an "Only" row names."""
    fields, parts, counted, orders = [], [], set(), set()
    for s in statements:
        if FIELD.match(s):
            m = FIELD.match(s)
            fields.append(("header" if m[1] else "field", int(m[2]), int(m[3]) if m[3] else None, tuple(int(p) for p in m[4].split("."))))
        elif PART.match(s):
            parts.append(PART.match(s)[1])
        elif RECORDS.match(s):
            counted.add(int(RECORDS.match(s)[1]))
        elif ORDER.match(s):
            orders.add(ORDER.match(s)[1])
    left = []
    for d in differences(base, doc):
        if d[0] == "part" and any(fnmatch.fnmatch(d[1], p) for p in parts):
            continue
        if d[0] == "order" and d[1] in orders:
            continue
        if d[0] == "record" and d[1] in counted:
            continue
        if d[0] in ("field", "header") and any(h == d[0] and k == d[1] and i in (None, d[2]) and d[3][:len(p)] == p for h, k, i, p in fields):
            continue
        left.append(d)
    return left


def show(d):
    if d[0] in ("field", "header"):
        return f"{'header ' if d[0] == 'header' else ''}{d[1]}#{d[2]} {'.'.join(map(str, d[3]))}"
    if d[0] in ("part", "order"):
        return f"{d[0]} {d[1]}"
    return f"{ {1: 'one more', -1: 'one less', 0: 'another type of'}[d[3]]} record {d[1]}#{d[2]}"


NONE = "No documents of its own"


def evidence_rows(md):
    """The Evidence table's rows, empty when the section says there are no documents, or None without a section."""
    section = re.search(r"^## Evidence\s*$(.*?)(?=^## |\Z)", md, re.M | re.S)
    if not section:
        return None
    rows = [[c.strip() for c in line.strip().strip("|").split("|")]
            for line in section[1].splitlines() if line.startswith("|")]
    if not rows and section[1].strip().startswith(NONE):
        return []
    if len(rows) < 3 or rows[0] != COLUMNS or any(len(r) != 4 for r in rows):
        raise SystemExit(f"the Evidence table needs the columns {' | '.join(COLUMNS)}, and no | in a cell")
    return rows[2:]


def sample(cell, number):
    """The path in samples/ a File or Compared with cell names, or None for a cell that names none."""
    m = re.match(r"^`([^`]+)`", cell)
    if not m:
        return None
    name = m[1] if re.match(r"^(?:\d{4}|\*|theme|release|resave)/", m[1]) else f"{number}/{m[1]}"
    return "samples/" + name


_ALL = []


def all_documents():
    """Every document's path, samples/ first."""
    if not _ALL:
        for d, subdirs, files in os.walk(os.path.join(ROOT, "samples"), followlinks=True):
            folders = [s for s in subdirs if s.endswith(EXT)]
            subdirs[:] = sorted(s for s in subdirs if not s.endswith(EXT))
            _ALL.extend("samples/" + os.path.relpath(os.path.join(d, f), os.path.join(ROOT, "samples")) for f in sorted(files + folders) if f.endswith(EXT))
    return _ALL


def expand(rel, base_rel):
    """The (document, document compared with) pairs a row is about."""
    if "*" not in rel:
        return [(rel, base_rel)]
    shape = re.compile("^" + "".join({"**": "(.*?)", "*": "([^/]*?)"}.get(x) or re.escape(x) for x in re.split(r"(\*\*?)", rel)) + "$")
    pairs = []
    for path in all_documents():
        m = shape.match(path)
        if m:
            base = base_rel
            for part in m.groups() if base_rel and "*" in base_rel else ():
                base = re.sub(r"\*\*?", lambda _: part, base, count=1)
            pairs.append((path, base))
    if not pairs:
        raise SystemExit(f"{rel}: no document matches")
    return pairs


def remake(rel):
    """The test-theme version of a Keynote sample, if there is one."""
    new = re.sub(r"^samples/(?=\d{4}/)", "samples/theme/", rel)
    return new if rel.endswith(".key") and new != rel and os.path.exists(os.path.join(ROOT, new)) else None


def own_documents(number):
    """The experiment's documents; a test-theme version counts only where there is no original."""
    own = [p for p in all_documents() if p.startswith(f"samples/{number}/")]
    return own + [p for p in all_documents() if p.startswith(f"samples/theme/{number}/") and p.replace("theme/", "", 1) not in own]


def check_experiment(number, md, load):
    """The experiment's checked rows for EVIDENCE.json, and what doesn't hold."""
    out, problems, named = [], [], set()
    for file_cell, base_cell, difference, shows in evidence_rows(md):
        rel, base_rel = sample(file_cell, number), sample(base_cell, number)
        if not rel:
            raise SystemExit(f"{number}: the File column names no file: {file_cell}")
        statements = re.findall(r"`([^`]+)`", difference)
        only = bool(re.match(r"^Only\b", difference))
        if base_rel is None and (only or any(re.match(r"^(same|records|order) |^part .*: ", s) for s in statements)):
            raise SystemExit(f"{number}: {rel}: nothing to compare with")
        pairs = expand(rel, base_rel)
        named.update(p for p, _ in pairs)
        row = {"file": rel, "compared": base_rel, "difference": difference, "documents": []}
        if not statements and not only:  # nothing to check: only that the documents are there
            for p in [x for pair in pairs for x in pair if x]:
                if not os.path.exists(os.path.join(ROOT, p)):
                    raise SystemExit(f"{number}: {p} doesn't exist")
            if "*" in rel:
                row["matches"] = len(pairs)
                out.append(row)
                continue
        for r, b in list(pairs):
            if remake(r) and not ORIGINAL_ONLY.search(difference):
                pairs.append((remake(r), b and (remake(b) or b)))
        for r, b in pairs:
            for p in (r, b):
                if p and not os.path.exists(os.path.join(ROOT, p)):
                    raise SystemExit(f"{number}: {p} doesn't exist")
            doc, base = load(r), load(b) if b else None
            for s in statements:
                why = check(s, base, doc)
                if why:
                    problems.append(f"{number}: {r}: `{s}`: {why}")
            if only:
                left = uncovered(statements, base, doc)
                if left or doc.error or base.error:
                    problems.append(f"{number}: {r}: also differs: " + (doc.error or base.error or "; ".join(map(show, left[:8])) + (f" and {len(left) - 8} more" if len(left) > 8 else "")))
            if len(pairs) > 80:  # a release's whole set: how many, not which
                row["matches"] = len(pairs)
                continue
            row["documents"].append({"path": r, "sha256": doc.sha, **({"compared": b, "compared_sha256": base.sha} if base else {})})
        out.append(row)
    problems += [f"{number}: the table doesn't name {p}" for p in own_documents(number) if p not in named]
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

    only_check = argv[:1] == ["--check"]
    argv = argv[only_check:]
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
        cache.clear()
        try:
            if evidence_rows(md) is None:
                raise SystemExit("there is no Evidence section")
            results[number], found = check_experiment(number, md, load)
        except SystemExit as why:
            results.pop(number, None)
            problems.append(f"{number}: {str(why).removeprefix(number + ': ')}")
            continue
        problems += found
        n = sum(len(re.findall(r"`[^`]+`", r["difference"])) for r in results[number])
        statements += n
        print(f"{number}: {len(results[number])} documents, {n} statements" + (f", {len(found)} problems" if found else ""))
    for p in problems:
        print(p, file=sys.stderr)
    if problems:
        sys.exit(f"{len(problems)} problems; fixtures/EVIDENCE.json not written")
    if only_check:
        print(f"{statements} statements hold")
        return
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(dict(sorted(results.items())), f, indent=1, ensure_ascii=False)
        f.write("\n")
    print(f"{statements} statements hold; wrote fixtures/EVIDENCE.json")


if __name__ == "__main__":
    main(sys.argv[1:])
