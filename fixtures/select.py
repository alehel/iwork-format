"""Choose which documents of the release sets and the resaved samples are worth publishing.

Usage: python3 -I fixtures/select.py

Writes fixtures/SELECTED.txt (committed), which fixtures/build.py reads. A set is cut down to documents
that together hold every field path the whole set holds: the (app, record type, field, nested field ...)
sequences in its records, down to five levels, found by parsing every length-delimited value that parses
as a message. The choice is greedy: the document adding most paths first, the smaller and then the first
by name on a tie. The sections of SELECTED.txt are:
  - release/R for each older release R: enough of its set (experiments 0475, 0477) for its field paths,
    and every encrypted document, whose paths can't be read;
  - resaved: of the samples the newest release changed when it saved them again (0476), enough for the
    field paths of those;
  - starter: of the newest release's set and the samples it saved again, enough for every field path of
    both and, for the set, every small number (below 400) a field holds, such as function numbers.
Field paths say which structures occur, not every value or combination, so this decides what to publish
of sets that can be made again from their recipes; the experiments' own samples are always published.
Only the standard library is used.
"""
import glob
import importlib.util
import multiprocessing
import os
import subprocess
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("build", os.path.join(ROOT, "fixtures", "build.py"))
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)
w = build.writer
NEWEST, OLDER = build.NEWEST, ("14.5", "13.1")
DEPTH, SMALL = 4, 400


def walk(data, prefix, out, depth):
    try:
        fields = w.parse_message(data)
    except Exception:
        return
    if any(not 0 < f <= 3000 for f, _, _ in fields):
        return
    for f, wire, value in fields:
        path = prefix + (f,)
        out.add(path)
        if wire == 0:
            n = w.read_varint(value, 0)[0]
            if n < SMALL:
                out.add(path + ("=", n))
        elif wire == 2 and depth < DEPTH and value:
            value = bytes(value)
            if not (len(value) > 2 and all(32 <= c < 127 for c in value)):  # plain text isn't a message
                walk(value, path, out, depth + 1)


def paths(rel):
    """The field paths of a document, or None when it can't be read (encrypted, or a folder package)."""
    app, out = rel.rsplit(".", 1)[1], set()
    try:
        with zipfile.ZipFile(rel) as z:
            for name in z.namelist():
                if not name.endswith(".iwa"):
                    continue
                for header, payloads in w.records(w.iwa_decode(z.read(name))):
                    for info, payload in zip([v for f, _, v in header if f == 2], payloads):
                        kind = next(w.read_varint(v, 0)[0] for f, _, v in w.parse_message(info) if f == 1)
                        walk(bytes(payload), (app, kind), out, 0)
    except Exception:
        return None
    return frozenset(out)


def survey(rel):
    why = build.problem(rel, rel)
    return rel, None if why else paths(rel), why


def cover(found, values, have=()):
    """The documents, chosen greedily, that hold every path of all of them beyond those in HAVE."""
    sets = {r: {p for p in s if values or "=" not in p} - set(have) for r, s in found.items() if s}
    chosen = []
    while True:
        best = min(sets, key=lambda r: (-len(sets[r]), os.path.getsize(r), r), default=None)
        if best is None or not sets[best]:
            return chosen
        chosen.append(best)
        got = sets.pop(best)
        for r in sets:
            sets[r] -= got


def documents(top):
    return sorted(p for p in glob.glob(f"{top}/**/*.*", recursive=True) if p.endswith((".pages", ".numbers", ".key")))


def changed():
    """The samples the newest release changed when it saved them again, as 0476 compares them."""
    out = subprocess.run([sys.executable, "-I", "recipes/0476-resave.py", NEWEST, "--compare"],
                         capture_output=True, text=True, check=True).stdout
    return {f"samples/resave/{NEWEST}/" + line[8:].split(": ", 1)[0] for line in out.splitlines() if line.startswith("DIFFERS ")}


def main():
    os.chdir(ROOT)
    sets = {f"release/{r}": documents(f"samples/release/{r}") for r in (NEWEST,) + OLDER}
    sets["resave"] = documents(f"samples/resave/{NEWEST}")
    with multiprocessing.get_context("fork").Pool() as pool:
        found = {k: [x for x in pool.map(survey, docs, chunksize=8) if not x[2]] for k, docs in sets.items()}
    readable = {k: {r: s for r, s, _ in v if s} for k, v in found.items()}
    lines = ["# Written by fixtures/select.py: the documents of the larger sets that are published, as paths in samples/."]
    sections = {}
    for r in OLDER:
        sections[f"release/{r}"] = sorted(cover(readable[f"release/{r}"], False) + [p for p, s, _ in found[f"release/{r}"] if not s])
    diff = changed()
    sections["resaved"] = sorted(cover({p: s for p, s in readable["resave"].items() if p in diff}, False))
    new = readable[f"release/{NEWEST}"]
    first = cover(new, True)
    have = set().union(*new.values())
    sections["starter"] = sorted(first + cover(readable["resave"], False, have))
    for name, docs in sections.items():
        lines += ["", f"[{name}]"] + [d.removeprefix("samples/") for d in docs]
        print(f"{name}: {len(docs)} documents, {sum(os.path.getsize(d) for d in docs) / 1e6:.1f} MB")
    with open(os.path.join("fixtures", "SELECTED.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
