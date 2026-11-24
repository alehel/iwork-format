"""Experiment 0473: make every scripted sample again with the installed release of the apps.

Usage: python3 -I recipes/0473-release-set.py RELEASE [--list | --compare] [--only NNNN,NNNN]

Collects, from the Recipe section of every experiment before 0461 (the release experiments), each
`osascript recipes/NNNN-*.applescript` command, each `for` or `while` loop around one, and each `cp`
of a document that a recipe then opens (taking the release's own copy of it), and runs
them in experiment order with every document or folder path under `samples/NNNN/` moved to
`samples/release/RELEASE/NNNN/`. Input media (images, sound, movies) are still read from samples/.
Keynote presentations are made with the project's test theme (IWORK_KEYNOTE_THEME, by default THEME),
also where a recipe line names one itself, so they can be
published. Commands that don't save into samples/ (those that act on a document already open in the
app), and the experiment that builds the test theme (0291), are left out, and so are documents that
were changed by hand after their recipe (HAND_EDITED).

Each command runs on its own in bash from the repository root, with a timeout of five minutes, so one
failure doesn't stop the rest. Prints one line per command, OK or FAILED with the reason, and a
total. With --list, prints the commands without running them. RELEASE is only a folder name, such as
16.0; the apps that run are whichever are installed.

With --compare, compares each document made with its namesake under samples/ (for a Keynote
presentation, the test-theme one under samples/theme/ when there is one), using the survey of
recipes/0461-compare-structure.py, and prints SAME when the two differ only in what every 16.0
document of that release differs in (BY_RELEASE), DIFFERS with what else differs, or SKIPPED with why
(encrypted, a folder package, or no namesake). Only the standard library is used.
"""
import glob
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIRST_RELEASE_EXPERIMENT = 461
SKIP = {"0291": "builds the test theme itself"}
# The test theme as it is in theme/, with cards at most 1024 pixels (0291). Keynote may also list the
# first, full-size version as "iwork-format test", which makes presentations 2.5 MB rather than 0.9 MB.
THEME = "iwork-format test v2"
# Documents a recipe makes that were then changed by hand in the app and saved under the same name:
# a rerun can only make the unchanged document, so it is removed again.
HAND_EDITED = {"0146/package.key", "0147/package.numbers",  # changed to a folder package in the app
               "0296/axis-title.key", "0296/axis-line.key", "0296/no-minimum.key", "0297/x-axis-name.key"}
# A path under samples/NNNN, up to its closing quote when quoted (it may hold spaces), else to a space.
DOC = re.compile(r'(?<=")\$PWD/samples/(\d{4})((?:/[^"]*)?)(?=")|(?<!")\$PWD/samples/(\d{4})((?:/[^"\s]*)?)(?=\s|$)')
MEDIA = (".png", ".jpg", ".jpeg", ".gif", ".tif", ".tiff", ".heic", ".mov", ".m4a", ".mp3", ".mp4", ".pdf", ".svg")


def rewrite(cmd, out):
    """Move document and folder paths under samples/NNNN/ to OUT/NNNN/; leave input media where they are."""
    def sub(m):
        exp, rest = (m.group(1), m.group(2)) if m.group(1) else (m.group(3), m.group(4))
        if rest.lower().endswith(MEDIA):
            return m.group(0)
        return f"{out}/{exp}{rest}"
    return DOC.sub(sub, cmd)


def statements(block):
    """Split a shell block into single lines and whole for/while loops."""
    lines, out, depth, cur = block.splitlines(), [], 0, []
    for line in lines:
        s = line.strip()
        if depth == 0 and re.match(r"(for|while)\b", s):
            depth, cur = 1, [line]
            if re.search(r"\bdone\b", s):
                out.append("\n".join(cur))
                depth = 0
            continue
        if depth:
            cur.append(line)
            if re.match(r"(for|while)\b", s):
                depth += 1
            if re.match(r"done\b", s):
                depth -= 1
                if depth == 0:
                    out.append("\n".join(cur))
            continue
        out.append(line)
    return out


def collect(out):
    cmds = []
    for path in sorted(glob.glob(os.path.join(ROOT, "experiments", "[0-9][0-9][0-9][0-9]-*.md"))):
        exp = os.path.basename(path)[:4]
        if int(exp) >= FIRST_RELEASE_EXPERIMENT or exp in SKIP:
            continue
        md = open(path, encoding="utf-8").read()
        m = re.search(r"^## Recipe\s*$(.*?)(?=^## )", md, re.M | re.S)
        if not m:
            continue
        for block in re.findall(r"```(?:bash|sh)?\n(.*?)```", m.group(1), re.S):
            # A recipe named once, as R=recipes/NNNN-*.applescript, and then called as osascript $R.
            for var, path in re.findall(r"^\s*([A-Z]\w*)=(recipes/\d{4}-[^\s]+\.applescript)\s*$", block, re.M):
                block = re.sub(rf"\$\{{?{var}\}}?(?=\s)", path, block)
            for st in statements(block):
                c = re.match(r"cp (samples/\d{4}/\S+\.(?:pages|key|numbers)) (samples/(\d{4})/\S+)$", st.strip())
                if c:  # a document copied for a recipe to open: copy the release's own instead
                    if not re.search(rf"osascript recipes/\d{{4}}-\S+\.applescript .*\$PWD/{re.escape(c.group(2))}\b", block):
                        continue  # copied for something other than a recipe, such as the writer
                    rel = out.removeprefix("$PWD/")
                    cmds.append((exp, f'cp "{rel}/{c.group(1)[8:]}" "{rel}/{c.group(2)[8:]}"'))
                    continue
                if not re.search(r"osascript recipes/\d{4}-[^ ]+\.applescript", st):
                    continue
                new = rewrite(st.strip(), out)
                if out not in new:
                    continue  # saves nothing into samples/: acts on a document already open
                cmds.append((exp, new))
    return cmds


# Differences that vary from run to run in any release (experiment 0469), and those every document of
# a release has from its 15.4 namesake (spec/releases.md): left out of what --compare reports.
KNOWN_FIELDS = {(4000, 17), (4011, 6)}
KNOWN_PROPS = {"BuildVersionHistory", "fileFormatVersion", "documentUUID", "privateUUID", "revision",
               "shareUUID", "stableDocumentUUID", "versionUUID"}
NOISY_TYPES = {("Index/CalculationEngine", 4008), ("Index/CalculationEngine", 4009)}
BY_RELEASE = {
    # 0469: one more view-state field per app.
    "16.0": {"fields": {(10133, 49), (12026, 34), (12026, 35), (3, 43), (23, 13)}, "props": set(), "types": set()},
    # 0461, 0466: one combined flag, no type-4011 record or the field naming it, no slide-node field 32.
    "14.5": {"fields": {(4000, 15), (4, 32)},
             "props": {"hasExternalReferenceOrMissingData", "hasUnmaterializedRemoteData",
                       "hasExternalReferenceOrMissingOrUnmaterializedRemoteData"},
             "types": {("Index/CalculationEngine", 4011)}},
}
THUMB = re.compile(r"^Data/(mt|st)-[0-9A-F-]{36}-\d+\.\w+$")


def data_name(n):
    """A Data/ entry without its data ID, which can change between runs."""
    return re.sub(r"-\d+(\.\w+)$", r"\1", n) if n.startswith("Data/") else n


def compare(release, base=None, prefer_theme=True, also_known=()):
    """Compare each document of the release set with its 15.4 namesake and print what isn't known."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("cmp", os.path.join(ROOT, "recipes", "0461-compare-structure.py"))
    cmp = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cmp)
    base = base or os.path.join(ROOT, "samples", "release", release)  # 0476 passes its resaved copies
    own = BY_RELEASE.get(release, {"fields": set(), "props": set(), "types": set()})
    known_fields, known_props = KNOWN_FIELDS | own["fields"] | set(also_known), KNOWN_PROPS | own["props"]
    noisy = NOISY_TYPES | own["types"]
    counts = {"SAME": 0, "DIFFERS": 0, "SKIPPED": 0}
    for doc in sorted(glob.glob(os.path.join(base, "*", "**", "*.*"), recursive=True)):
        if not doc.endswith((".pages", ".numbers", ".key")):
            continue
        rel = os.path.relpath(doc, base)
        old = os.path.join(ROOT, "samples", "theme", rel)
        if not (prefer_theme and rel.endswith(".key") and os.path.exists(old)):
            old = os.path.join(ROOT, "samples", rel)
        why = None
        if not os.path.exists(old):
            why = "no 15.4 document of that name"
        elif os.path.isdir(doc) or os.path.isdir(old):
            why = "folder package"
        if why is None:
            try:
                a, b = cmp.survey(old), cmp.survey(doc)
            except Exception as e:  # encrypted parts don't decode
                why = f"not compared: {type(e).__name__}"
        if why:
            counts["SKIPPED"] += 1
            print(f"SKIPPED {rel}: {why}", flush=True)
            continue
        (na, ta, va, pa, fa), (nb, tb, vb, pb, fb) = a, b
        notes = []
        ea = {data_name(n) for n in na if not THUMB.match(n)}
        eb = {data_name(n) for n in nb if not THUMB.match(n)}
        if ea != eb:
            notes.append(f"entries only in 15.4 {sorted(ea - eb)[:4]}, only in {release} {sorted(eb - ea)[:4]}")
        for k in sorted((set(pa) | set(pb)) - known_props):
            if pa.get(k) != pb.get(k):
                notes.append(f"Properties.plist {k}: {pa.get(k)!r} -> {pb.get(k)!r}")
        for part in sorted(set(ta) | set(tb)):
            diff = {t: (ta[part][t], tb[part][t]) for t in set(ta[part]) | set(tb[part])
                    if ta[part][t] != tb[part][t] and (part, t) not in noisy
                    and not (rel.endswith(".numbers") and part == "Index/DocumentStylesheet" and t == 2022
                             and ta[part][t] - tb[part][t] == 1)}
            if diff:
                notes.append(f"{part} records by type {dict(sorted(diff.items()))}")
        for t in sorted(set(va) & set(vb)):  # a type only one has shows as a record count above
            if va[t] != vb[t]:
                notes.append(f"type {t} version {sorted(va[t])} -> {sorted(vb[t])}")
        for t in sorted(set(fa) & set(fb)):
            extra = {(t, f) for f in fa[t] ^ fb[t]} - known_fields
            if extra:
                notes.append(f"type {t} fields only in 15.4 {sorted(fa[t] - fb[t])}, only in {release} {sorted(fb[t] - fa[t])}")
        status = "SAME" if not notes else "DIFFERS"
        counts[status] += 1
        print(f"{status} {rel}" + ("" if not notes else ": " + "; ".join(notes)), flush=True)
    print(counts, flush=True)


def main(argv):
    if not argv or argv[0].startswith("-"):
        sys.exit(__doc__)
    release, rest = argv[0], argv[1:]
    if "--compare" in rest:
        compare(release)
        return
    only = None
    if "--only" in rest:
        only = set(rest[rest.index("--only") + 1].split(","))
    out = f"$PWD/samples/release/{release}"
    cmds = [(e, c) for e, c in collect(out) if only is None or e in only]
    if "--list" in rest:
        for exp, cmd in cmds:
            print(f"# {exp}\n{cmd}")
        print(f"# {len(cmds)} commands from {len({e for e, _ in cmds})} experiments")
        return
    theme = os.environ.get("IWORK_KEYNOTE_THEME", THEME)
    env = dict(os.environ, IWORK_KEYNOTE_THEME=theme)
    made, counts = set(), {"OK": 0, "FAILED": 0}
    for exp, cmd in cmds:
        if exp not in made:
            os.makedirs(os.path.join(ROOT, "samples", "release", release, exp), exist_ok=True)
            made.add(exp)
        cmd = re.sub(r"IWORK_KEYNOTE_THEME='[^']*'", f"IWORK_KEYNOTE_THEME='{theme}'", cmd)  # 0295-0297 set it inline
        try:
            r = subprocess.run(["bash", "-c", cmd], cwd=ROOT, env=env, capture_output=True, text=True, timeout=300)
            ok, why = r.returncode == 0, (r.stderr.strip() or r.stdout.strip())
        except subprocess.TimeoutExpired:
            ok, why = False, "timed out"
        for name in HAND_EDITED:
            if name.startswith(exp + "/"):
                done = os.path.join(ROOT, "samples", "release", release, name)
                if os.path.exists(done):
                    os.remove(done)
                    print(f"LEFT OUT {name}: changed by hand after its recipe", flush=True)
        counts["OK" if ok else "FAILED"] += 1
        first = cmd.splitlines()[0][:110]
        print(f"{'OK' if ok else 'FAILED'} {exp}: {first}" + ("" if ok else f" :: {why[-200:]}"), flush=True)
    print(counts, flush=True)


if __name__ == "__main__":
    main(sys.argv[1:])
