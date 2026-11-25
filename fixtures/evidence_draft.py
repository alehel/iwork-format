"""Draft an experiment's Evidence table: for each of its documents, what it is best compared with and what differs.

Usage: python3 -I fixtures/evidence_draft.py NNNN [...]

Prints, for each document, the closest document among those the experiment mentions and its own earlier ones.
Where few fields differ (a document written from another), the Difference is complete: an "Only" list whose
every statement fixtures/evidence.py confirms. Otherwise (two documents an app saved) it prints candidates:
the values that occur more often in one than in the other, without what differs between any two saves, to
choose from. What each document shows is for the experiment to say. Only the standard library is used.
"""
import collections
import importlib.util
import json
import os
import re
import struct
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("evidence", os.path.join(ROOT, "fixtures", "evidence.py"))
e = importlib.util.module_from_spec(spec)
spec.loader.exec_module(e)
w = e.w
FEW = 14
CANDIDATES = 45
# Two saves of the same content: what differs between them is noise.
SAME_CONTENT = [("0001/empty-a.pages", "0001/empty-b.pages"), ("0024/empty-a.numbers", "0024/empty-b.numbers"),
                ("theme/0024/empty-a.key", "theme/0024/empty-b.key"), ("0024/empty-a.key", "0024/empty-b.key"),
                ("0002/hello.pages", "0012/underline.pages")]
NOISY_TYPES = {11006, 11011, 4000, 4001, 4003, 4004, 4008, 4009, 10012, 10011}
_DOCS = {}


def load(rel):
    if rel not in _DOCS:
        _DOCS[rel] = e.Document(rel)
    return _DOCS[rel]


def literal(wire, raw):
    if wire == 0:
        n = w.read_varint(raw, 0)[0]
        return str(n if n < 1 << 63 else n - (1 << 64))
    if wire in (1, 5):
        v = struct.unpack("<d" if wire == 1 else "<f", raw)[0]
        s = f"{v:.4f}".rstrip("0")
        s = s + "0" if s.endswith(".") else s
        return s if abs(v) < 1e9 and (abs(v) >= 0.001 or v == 0) else None
    try:
        s = raw.decode("utf-8")
        if all(c.isprintable() or c in "\n\t\u2028\u0005\ufffc" for c in s) and len(raw) <= 70 and "`" not in s and "|" not in s:
            return json.dumps(s, ensure_ascii=False).replace("\ufffc", "\\ufffc").replace("\u2028", "\\u2028").replace("\u00ad", "\\u00ad").replace("\u00a0", "\\u00a0").replace("\u200b", "\\u200b")
    except UnicodeDecodeError:
        pass
    return f'x"{raw.hex()}"' if len(raw) <= 12 else None


def is_message(raw):
    try:
        f = w.parse_message(raw)
        return bool(f) and all(0 < n <= 20000 and not (t in (1, 5) and len(v) != (8 if t == 1 else 4)) for n, t, v in f) and w.serialize_message(f) == bytes(raw)
    except Exception:
        return False


def is_text(raw):
    try:
        s = bytes(raw).decode("utf-8")
    except UnicodeDecodeError:
        return False
    return all(c.isprintable() or c in "\n\t\u2028\u0005\ufffc" for c in s)


def leaves(payload, path=()):
    for f, t, v in w.parse_message(payload):
        p = path + (f,)
        if t == 2 and v and is_message(v) and not (is_text(v) and len(v) > 1):
            yield from leaves(v, p)
        else:
            yield p, t, bytes(v)


def facts(doc):
    ids = {i for i, _ in doc.records}
    out = collections.Counter()
    for (_, _), (kind, payload) in doc.records.items():
        if kind in NOISY_TYPES:
            continue
        for path, t, v in leaves(payload):
            if t == 0 and w.read_varint(v, 0)[0] in ids and w.read_varint(v, 0)[0] > 2000:
                continue
            lit = literal(t, v)
            out[(kind, path, lit if lit is not None else "(long)")] += 1
    return out


_NOISE = set()


def noise():
    if not _NOISE:
        for a, b in SAME_CONTENT[:4]:
            a, b = facts(load("samples/" + a)), facts(load("samples/" + b))
            _NOISE.update((k, p) for k, p, _ in (a - b) + (b - a))
    return _NOISE


def one_statement(d, base, doc):
    """A statement for one difference, with values where they can be written."""
    if d[0] == "part":
        have = ["present" if d[1] in x.parts else "absent" for x in (base, doc)]
        return f"part {d[1]}: {have[0]} → {have[1]}" if have[0] != have[1] else f"part {d[1]}: changed"
    if d[0] == "order":
        return f"order {d[1]}: changed"
    if d[0] == "record":
        have = [sum(k == d[1] for k, _ in x.records.values()) for x in (base, doc)]
        return f"records {d[1]}: {have[0]} → {have[1]}"
    head = ("header " if d[0] == "header" else "") + f"{d[1]}#{d[2]} " + ".".join(map(str, d[3]))
    x, y = ([i for v in z.values(d[1], d[2], list(d[3]), d[0] == "header") for i in v] for z in (base, doc))
    if len(x) <= 1 and len(y) <= 1 and (x or y):
        lits = [literal(*v[0]) if v else "absent" for v in (x, y)]
        if None not in lits and lits[0] != lits[1]:
            s = f"{head}: {lits[0]} → {lits[1]}"
            if e.check(s, base, doc) is None:
                return s
    if len(x) != len(y):
        return f"{head}: ×{len(x)} → ×{len(y)}"
    return f"{head}: changed"


def candidates(base, doc):
    a, b = facts(base), facts(doc)
    out = []
    more, less = b - a, a - b
    for (k, p, v), n in sorted(more.items(), key=lambda x: (a.get(x[0], 0), x[0][0], x[0][1])):
        if (k, p) in noise() or v == "(long)":
            continue
        old = [o for kk, pp, o in less if (kk, pp) == (k, p) and o != "(long)"]
        path = ".".join(map(str, p))
        s = f"{k} {path}: {old[0] if len(old) == 1 else 'absent'} → {v}"
        if len(out) > 150:  # thousands of values differ, as with a large table; checking each takes minutes
            break
        if e.check(s, base, doc) is None:
            out.append((a.get((k, p, v), 0) > 0, len(old) > 1, s))
    seen = {(k, p) for k, p, _ in more}
    for (k, p, v), n in sorted(less.items()):
        if (k, p) in noise() or (k, p) in seen or v == "(long)":
            continue
        s = f"{k} {'.'.join(map(str, p))}: {v} → absent"
        if len(out) > 220:
            break
        if e.check(s, base, doc) is None:
            out.append((True, True, s))
    types = [collections.Counter(k for k, _ in x.records.values()) for x in (base, doc)]
    records = [f"records {k}: {types[0][k]} → {types[1][k]}" for k in sorted(set(types[0]) | set(types[1])) if types[0][k] != types[1][k] and k not in (4003, 4004, 4008, 4009)]
    parts = []
    for n in sorted(set(base.parts) ^ set(doc.parts)):
        if not n.endswith(".iwa"):
            parts.append(f"part {n}: " + ("absent → present" if n in doc.parts else "present → absent"))
    return records[:20], parts[:10], [s for _, _, s in sorted(out, key=lambda x: x[:2])]


def mentioned(md, number):
    found = []
    for m in re.finditer(r"(?:samples/)?((?:theme/)?\d{4}/(?:[\wåæøÅÆØ.-]+/)*[\wåæøÅÆØ. -]+?\.(?:pages|key|numbers))", md):
        found.append("samples/" + m[1])
    for m in re.finditer(r"\[(\d{4})\]\([^)]*\)[^|\n]{0,80}?`([\w.-]+\.(?:pages|key|numbers))`", md):
        found += [f"samples/{m[1]}/{m[2]}", f"samples/theme/{m[1]}/{m[2]}"]
    for m in re.finditer(r"`([\w.-]+\.(?:pages|key|numbers))`[^|\n]{0,40}?\[(\d{4})\]", md):
        found += [f"samples/{m[2]}/{m[1]}", f"samples/theme/{m[2]}/{m[1]}"]
    for m in re.finditer(r"\[(\d{4})\]\(", md):  # the documents of experiments it cites, when they have few
        own = [p for p in e.own_documents(m[1])]
        found += own if len(own) <= 6 else []
    out = []
    for p in found:
        if p not in out and os.path.exists(os.path.join(ROOT, p)) and f"/{number}/" not in p:
            out.append(p)
    return out[:14]


def distance(a, b):
    if a.error or b.error:
        return 10 ** 6 - (sum(a.parts.get(n) == v for n, v in b.parts.items()))
    n = sum(a.records.get(k) != v for k, v in b.records.items()) + sum(k not in b.records for k in a.records)
    return n + sum(1 for k in set(a.headers) & set(b.headers) if a.headers[k] != b.headers[k]) \
        + sum(a.parts.get(n) != v for n, v in b.parts.items() if not n.endswith(".iwa") and not e.is_preview(n))


def draft(number):
    name = next(f for f in os.listdir(os.path.join(ROOT, "experiments")) if f.startswith(number + "-") and f.endswith(".md"))
    with open(os.path.join(ROOT, "experiments", name), encoding="utf-8") as f:
        md = f.read()
    own = e.own_documents(number)
    ext = {p.rsplit(".", 1)[1] for p in own}
    outside = [p for p in mentioned(md, number) if p.rsplit(".", 1)[1] in ext]
    print(f"### {number} {md.splitlines()[0].split(': ', 1)[-1]}: {len(own)} documents")
    if not own:
        print("No documents of its own. Mentions:", ", ".join(p[8:] for p in mentioned(md, number)))
        return
    if len(own) > 30:
        print("(many documents)", ", ".join(p[8:] for p in own))
    pool, todo = list(outside), list(own)
    first = [p for p in todo if re.match(r"(original|plain|empty|control|base|before|none)", os.path.basename(p))]
    row = re.search(r"^\| (?:Baseline|Input) \|(.*)\|$", md, re.M)
    baseline = [p for p in (mentioned(row[1], number) if row else []) if p in pool]
    while todo:
        best = None
        for p in todo:
            for q in pool:
                if q.rsplit(".", 1)[1] != p.rsplit(".", 1)[1]:
                    continue
                d = 0 if load(p).sha == load(q).sha else 1 + distance(load(q), load(p))
                if best is None or d < best[0]:
                    best = (d, p, q)
        if best is None or (best[0] > 40 and first and first[0] in todo):
            p = first[0] if first and first[0] in todo else todo[0]
            best = best if best and best[1] == p else next(((1 + distance(load(q), load(p)), p, q) for q in pool if q.rsplit(".", 1)[1] == p.rsplit(".", 1)[1]), (0, p, None))
        _, p, q = best
        if q and best[0] > 40:  # two documents an app saved: the experiment's own baseline says more than the closest
            same = [b for b in baseline if b.rsplit(".", 1)[1] == p.rsplit(".", 1)[1]]
            q = same[0] if same and not re.match(rf"samples/(theme/)?{number}/", q) else q
        todo.remove(p)
        pool.append(p)
        doc = load(p)
        short = p[len(f"samples/{number}/"):] if p.startswith(f"samples/{number}/") else p[8:]
        if q is None:
            print(f"- `{short}`: nothing to compare with" + (f"; UNREADABLE {doc.error}" if doc.error else ""))
            continue
        base = load(q)
        qs = q[len(f"samples/{number}/"):] if q.startswith(f"samples/{number}/") else q[8:]
        rem = f"; REMADE as {e.remake(p)[8:]}" if e.remake(p) else ""
        if base.sha == doc.sha:
            print(f"- `{short}` | `{qs}` | `same bytes`{rem}")
            continue
        if doc.error or base.error:
            print(f"- `{short}` | `{qs}` | UNREADABLE {doc.error or base.error}{rem}; parts differing: " + ", ".join(n for n in sorted(set(base.parts) | set(doc.parts)) if base.parts.get(n) != doc.parts.get(n))[:300])
            continue
        diffs = e.differences(base, doc)
        if not diffs:
            print(f"- `{short}` | `{qs}` | Only nothing: `same records`" + (", `same parts`" if base.parts == doc.parts else "") + rem)
        elif len(diffs) <= FEW or len({(d[0], d[1]) for d in diffs}) <= 2 and len(diffs) <= 60:
            statements = []
            for d in diffs:
                s = one_statement(d, base, doc)
                if s not in statements:
                    statements.append(s)
            print(f"- `{short}` | `{qs}` | Only " + ", ".join(f"`{s}`" for s in statements[:FEW + 4]) + (" …" if len(statements) > FEW + 4 else "") + rem)
            bad = [(s, e.check(s, base, doc)) for s in statements if e.check(s, base, doc)]
            if bad:
                print("    DON'T HOLD:", bad[:4])
        else:
            records, parts, cand = candidates(base, doc)
            print(f"- `{short}` | `{qs}` | candidates ({len(diffs)} differences){rem}")
            if records or parts:
                print("    " + ", ".join(f"`{s}`" for s in records + parts))
            print("    " + ", ".join(f"`{s}`" for s in cand[:CANDIDATES]) + (f" … {len(cand) - CANDIDATES} more" if len(cand) > CANDIDATES else ""))


if __name__ == "__main__":
    for n in sys.argv[1:]:
        _DOCS.clear()
        draft(n)
