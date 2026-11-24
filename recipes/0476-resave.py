"""Experiment 0476: open every sample in the installed apps and save a copy, then compare the copies.

Usage: python3 -I recipes/0476-resave.py RELEASE [--compare | --pair OTHER] [--only NNNN,NNNN] [--skip NNNN,NNNN] [--apps APP,APP] [--limit N]

Opens each .pages, .numbers and .key directly under samples/NNNN/ (experiments 0001 to 0460) and
samples/theme/NNNN/, one at a time, with recipes/0372-in-app.sh, saves it with AppleScript's
`save d in` as samples/resave/RELEASE/<the same path>, and closes it unsaved. The app writes the
whole document out again from what it read, so the copy shows how the installed release writes
every feature in the sample, including those made by hand in the app. Left out: experiments 0179
and 0180, whose password prompt would hold the run up, and those whose files were written to make
an app fail (0379, 0394, 0396, 0424, 0434, 0451). A sample already copied is skipped, so a run can
be resumed. --apps (from experiment 0480 on) keeps to some of Pages, Numbers and Keynote. Prints OK or FAILED per document and a total. RELEASE only names the folder.

With --compare, compares each copy with its original using --compare of
recipes/0473-release-set.py, which knows what every document of RELEASE differs in. With --pair
OTHER, compares each copy with OTHER's copy of the same sample instead: what saving does in both
releases cancels out, so what is left, besides the differences known between the two releases,
is a difference between them.
Only the standard library is used.
"""
import glob
import importlib.util
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HELPER = os.path.join(ROOT, "recipes", "0372-in-app.sh")
SKIP = {"0179", "0180", "0379", "0394", "0396", "0424", "0434", "0451"}
APPS = {".pages": "Pages", ".numbers": "Numbers", ".key": "Keynote"}


def samples(only, skip=frozenset()):
    docs = []
    for top in ("samples", "samples/theme"):
        for d in sorted(glob.glob(os.path.join(ROOT, top, "[0-9][0-9][0-9][0-9]"))):
            exp = os.path.basename(d)
            if int(exp) > 460 or exp in SKIP or exp in skip or (only and exp not in only):
                continue
            for f in sorted(os.listdir(d)):
                if os.path.splitext(f)[1] in APPS:
                    docs.append(os.path.relpath(os.path.join(d, f), os.path.join(ROOT, "samples")))
    return docs


def pair(a, b):
    spec = importlib.util.spec_from_file_location("rs", os.path.join(ROOT, "recipes", "0473-release-set.py"))
    rs = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rs)
    spec = importlib.util.spec_from_file_location("cmp", os.path.join(ROOT, "recipes", "0461-compare-structure.py"))
    cmp = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cmp)
    empty = {"fields": set(), "props": set(), "types": set()}
    ka, kb = rs.BY_RELEASE.get(a, empty), rs.BY_RELEASE.get(b, empty)
    fields = rs.KNOWN_FIELDS | ka["fields"] | kb["fields"]
    props = rs.KNOWN_PROPS | ka["props"] | kb["props"]
    noisy = rs.NOISY_TYPES | ka["types"] | kb["types"]
    base_a, base_b = os.path.join(ROOT, "samples", "resave", a), os.path.join(ROOT, "samples", "resave", b)
    counts = {"SAME": 0, "DIFFERS": 0, "SKIPPED": 0}
    for doc in sorted(glob.glob(os.path.join(base_a, "**", "*.*"), recursive=True)):
        if not doc.endswith(tuple(APPS)):
            continue
        rel = os.path.relpath(doc, base_a)
        other = os.path.join(base_b, rel)
        try:
            if os.path.isdir(doc) or not os.path.exists(other):
                raise ValueError("folder package" if os.path.isdir(doc) else f"no {b} copy")
            (na, ta, va, pa, fa), (nb, tb, vb, pb, fb) = cmp.survey(other), cmp.survey(doc)
        except Exception as e:
            counts["SKIPPED"] += 1
            print(f"SKIPPED {rel}: {e}"[:200], flush=True)
            continue
        notes = []
        ea = {rs.data_name(n) for n in na if not rs.THUMB.match(n)}
        eb = {rs.data_name(n) for n in nb if not rs.THUMB.match(n)}
        if ea != eb:
            notes.append(f"entries only in {b} {sorted(ea - eb)[:4]}, only in {a} {sorted(eb - ea)[:4]}")
        for k in sorted((set(pa) | set(pb)) - props):
            if pa.get(k) != pb.get(k):
                notes.append(f"Properties.plist {k}: {pa.get(k)!r} -> {pb.get(k)!r}")
        for part in sorted(set(ta) | set(tb)):
            diff = {t: (ta[part][t], tb[part][t]) for t in set(ta[part]) | set(tb[part])
                    if ta[part][t] != tb[part][t] and (part, t) not in noisy
                    and not (part == "Index/DocumentStylesheet" and t == 2022 and abs(ta[part][t] - tb[part][t]) == 1)}
            if diff:
                notes.append(f"{part} records by type {dict(sorted(diff.items()))}")
        for t in sorted(set(va) & set(vb)):
            if va[t] != vb[t]:
                notes.append(f"type {t} version {sorted(va[t])} -> {sorted(vb[t])}")
        for t in sorted(set(fa) & set(fb)):
            if {(t, f) for f in fa[t] ^ fb[t]} - fields:
                notes.append(f"type {t} fields only in {b} {sorted(fa[t] - fb[t])}, only in {a} {sorted(fb[t] - fa[t])}")
        status = "SAME" if not notes else "DIFFERS"
        counts[status] += 1
        print(f"{status} {rel}" + ("" if not notes else ": " + "; ".join(notes)), flush=True)
    print(counts, flush=True)


def main(argv):
    if not argv or argv[0].startswith("-"):
        sys.exit(__doc__)
    release, rest = argv[0], argv[1:]
    base = os.path.join(ROOT, "samples", "resave", release)
    if "--pair" in rest:
        pair(release, rest[rest.index("--pair") + 1])
        return
    if "--compare" in rest:
        spec = importlib.util.spec_from_file_location("rs", os.path.join(ROOT, "recipes", "0473-release-set.py"))
        rs = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(rs)
        # Fields 5 and 16 of the engine's root, the locale, appear whenever a document is saved again,
        # in 15.4 too (0139's resaved.pages): not a difference between releases.
        # 14.5 also writes 16.0's view-state fields when it saves a document it opened (this experiment).
        rs.compare(release, base, prefer_theme=False,
                   also_known={(4000, 5), (4000, 16)} | rs.BY_RELEASE["16.0"]["fields"])
        return
    only = set(rest[rest.index("--only") + 1].split(",")) if "--only" in rest else None
    limit = int(rest[rest.index("--limit") + 1]) if "--limit" in rest else None
    skip = set(rest[rest.index("--skip") + 1].split(",")) if "--skip" in rest else set()
    apps = set(rest[rest.index("--apps") + 1].split(",")) if "--apps" in rest else set(APPS.values())
    counts = {"OK": 0, "FAILED": 0, "SKIPPED": 0}
    failed_in_a_row = 0
    for rel in [r for r in samples(only, skip) if APPS[os.path.splitext(r)[1]] in apps][:limit]:
        src, out = os.path.join(ROOT, "samples", rel), os.path.join(base, rel)
        if os.path.exists(out):
            counts["SKIPPED"] += 1
            continue
        os.makedirs(os.path.dirname(out), exist_ok=True)
        before = os.stat(src).st_mtime if not os.path.isdir(src) else None
        script = f'save d in POSIX file "{out}"\nreturn "saved"'
        try:
            r = subprocess.run(["sh", HELPER, APPS[os.path.splitext(rel)[1]], src, script],
                               capture_output=True, text=True, timeout=180)
            ok = r.returncode == 0 and os.path.exists(out)
            why = (r.stdout + r.stderr).strip().splitlines()[-1:] if not ok else []
        except subprocess.TimeoutExpired:
            ok, why = False, ["timed out"]
        if ok and before is not None and os.stat(src).st_mtime != before:
            ok, why = False, ["the original changed"]
        counts["OK" if ok else "FAILED"] += 1
        print(f"{'OK' if ok else 'FAILED'} {rel}" + ("" if ok else f" :: {' '.join(why)[:200]}"), flush=True)
        failed_in_a_row = 0 if ok else failed_in_a_row + 1
        if failed_in_a_row >= 5:
            print("stopping: five failures in a row", flush=True)
            break
    print(counts, flush=True)


if __name__ == "__main__":
    main(sys.argv[1:])
