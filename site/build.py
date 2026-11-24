"""Build the specification site into docs/ as static HTML and CSS, with no JavaScript.

Usage: python3 -I site/build.py

Sources:
  spec/*.md            the specification, which describes the newest app release, one page per layer

A statement in the spec that doesn't hold for every release checked begins with a version note:
`[since: 15.4]` for what 15.4 was the first checked release to have, `[until: 14.5]` for what the
newest release no longer does and 14.5 was the last checked release to do. It is drawn as a badge, and
spec/releases.md gathers every noted statement where it says `<!-- release-history -->`.
  experiments/*.md     every experiment, one page each
  site/guides/*.md     walkthroughs written for the site, which may embed generated excerpts
  site/examples/*.txt  excerpts of iwork-probe output, made by site/examples.py from local samples
  site/files/          sample documents published for download, and renders of them

Only the Python standard library is used. Markdown is converted by the small converter below,
which handles the subset the repository's writing uses.
"""
import html
import json
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs")
REPO = "https://github.com/alehel/iwork-format"
TITLE = "iWork file format specification"

# The releases experiments have run with, newest first. The specification describes the newest one; what
# older ones lack or do differently is marked with version notes where it stands. Experiments aren't
# versioned: each records the release it ran with. main() stops when an experiment names another one.
RELEASES = ("16.0", "15.4", "14.5", "13.1")
CURRENT = RELEASES[0]
SPEC_PAGES = [("README.md", "index.html"), ("container.md", "container.html"), ("text.md", "text.html"),
              ("styles.md", "styles.html"), ("tables.md", "tables.html"), ("drawables.md", "drawables.html"),
              ("pages.md", "pages.html"), ("keynote.md", "keynote.html"), ("numbers.md", "numbers.html"),
              ("releases.md", "releases.html"), ("features.md", "features.html")]
GENERATED = {"spec/types.html", "experiments/topics.html", "search.html", "spec/features.json"}  # pages the build makes without a Markdown source, which Markdown may link to
VERSION_NOTE = re.compile(r"\[(since|until): ([^\]]+)\](?!\()")
OLD_MARK = re.compile(r"\[release: [^\]]+\]")


def version_key(name):
    return tuple(int(p) if p.isdigit() else -1 for p in name.split("."))


def version_note(kind, release):
    """A note's badge and what it means in words, or None when it names no release that can carry it."""
    if release not in RELEASES:
        return None
    i = RELEASES.index(release)
    if kind == "since" and i + 1 < len(RELEASES):
        return f"Since {release}", f"In {release} and later; not in {RELEASES[i + 1]} or earlier"
    if kind == "until" and i > 0:
        return f"Until {release}", f"In {release} and earlier; no longer in {RELEASES[i - 1]} or later"
    return None


# --- Markdown subset -------------------------------------------------------------------------

PROBLEMS = []  # (source, message) for Markdown the builder can't render faithfully; main() fails if any


def problem(here, message):
    PROBLEMS.append((here, message))


def slug(text):
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[^\w\s-]", "", text.lower(), flags=re.UNICODE)
    return re.sub(r"[\s]+", "-", text.strip())


def link_target(url, here):
    """Point repository links at the right place: site pages for .md files, GitHub for the rest."""
    if re.match(r"^[a-z]+:", url) or url.startswith("#"):
        return url
    path, _, anchor = url.partition("#")
    anchor = "#" + anchor if anchor else ""
    target = os.path.normpath(os.path.join(os.path.dirname(here), path)).replace(os.sep, "/")
    if target in GENERATED:
        return relpath(target, here_out(here)) + anchor
    if target.startswith("site/files/"):
        return relpath("files/" + target[len("site/files/"):], here_out(here)) + anchor
    if target.endswith(".md"):
        page = SITE_PAGES.get(target)
        if page:
            return relpath(page, here_out(here)) + anchor
        if SITE_PAGES and not os.path.isfile(os.path.join(ROOT, target)):
            problem(here, f"link to a missing file: {url}")
    return f"{REPO}/blob/main/{target}{anchor}"


def note_badge(kind, release, here):
    note = version_note(kind, release)
    if not note:
        problem(here, f"version note [{kind}: {release}] doesn't name a release that can carry it")
        return ""
    return f'<span class="release" title="{note[1]}">{note[0]}</span>'


def inline(text, here):
    codes = []

    def keep(m):  # inline code is set aside so that nothing inside it is read as Markdown
        codes.append("<code>" + html.escape(m.group(0)[1:-1]) + "</code>")
        return f"\x00{len(codes) - 1}\x00"

    s = html.escape(re.sub(r"`[^`]+`", keep, text), quote=False)
    if OLD_MARK.search(s):
        problem(here, f"release mark, which version notes replaced: {OLD_MARK.search(s).group(0)}")
    s = VERSION_NOTE.sub(lambda m: note_badge(m.group(1), m.group(2), here), s)
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", lambda m: f'<a href="{html.escape(link_target(html.unescape(m.group(2)), here))}">{m.group(1)}</a>', s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*([^*\s][^*]*?)\*(?![\w*])", r"<em>\1</em>", s)
    return re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], s)


def render(md, here, toc=None):
    lines = md.split("\n")
    out = []
    i = 0
    para = []
    anchors = set()

    def flush():
        if para:
            out.append("<p>" + inline(" ".join(para), here) + "</p>")
            para.clear()

    while i < len(lines):
        line = lines[i]
        fence = re.match(r"^( {0,3})```", line)  # a fence may be indented up to three spaces, as in Markdown
        if fence:
            flush()
            pad = len(fence.group(1))
            lang = line.strip()[3:].strip()
            body = []
            i += 1
            while i < len(lines) and not re.match(r"^ {0,3}```", lines[i]):
                body.append(lines[i][min(pad, len(lines[i]) - len(lines[i].lstrip(" "))):])
                i += 1
            if i >= len(lines):
                problem(here, "code block not closed with ```")
            cls = f' class="lang-{lang}"' if lang else ""
            out.append(f"<pre{cls}><code>" + html.escape("\n".join(body)) + "</code></pre>")
            i += 1
            continue
        if re.match(r"^#{5,}\s", line):
            problem(here, f"heading deeper than ####: {line.strip()[:60]}")
        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            flush()
            level = len(m.group(1))
            text = inline(m.group(2), here)
            anchor = slug(m.group(2))
            # A repeated heading gets -2, -3 and so on, so every section keeps its own link.
            n = 2
            while anchor in anchors:
                anchor = f"{slug(m.group(2))}-{n}"
                n += 1
            anchors.add(anchor)
            if toc is not None and level == 2:
                toc.append((anchor, re.sub(r"<[^>]+>", "", text)))
            out.append(f'<h{level} id="{anchor}">{text}<a class="anchor" href="#{anchor}" aria-label="Link to this section: {html.escape(re.sub(r'<[^>]+>', '', text), quote=True)}">#</a></h{level}>')
            i += 1
            continue
        if line.strip() == "<!-- release-history -->":
            flush()
            out.append(release_history(here))
            i += 1
            continue
        if line.strip() == "<!-- feature-inventory -->":
            flush()
            i += 1
            while i < len(lines) and not lines[i].strip():
                i += 1
            header = [c.strip() for c in lines[i].strip().strip("|").split("|")] if i < len(lines) else []
            if header != FEATURE_COLUMNS:
                problem(here, f"the feature inventory needs the columns {' | '.join(FEATURE_COLUMNS)}")
            i += 2
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                if len(rows[-1]) != len(FEATURE_COLUMNS):
                    problem(here, f"table row has {len(rows[-1])} cells, its header {len(FEATURE_COLUMNS)}: {lines[i][:60]}")
                i += 1
            out.append(feature_inventory(rows, here))
            continue
        m = re.match(r"^<!--\s*include:\s*(\S+)\s*-->$", line.strip())
        if m:
            flush()
            out.append(include_excerpt(m.group(1), here))
            i += 1
            continue
        m = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)$", line.strip())
        if m:
            flush()
            src = m.group(2)
            target = os.path.normpath(os.path.join(os.path.dirname(here), src)).replace(os.sep, "/")
            if target.startswith("site/files/"):
                src = link_target(src, here)
            # The caption repeats the image's description, so screen readers are given it once, as the alt text.
            out.append(f'<figure><img src="{html.escape(src)}" alt="{html.escape(m.group(1))}" loading="lazy"><figcaption aria-hidden="true">{inline(m.group(1), here)}</figcaption></figure>')
            i += 1
            continue
        if line.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|$", lines[i + 1].strip()):
            flush()
            header = [c.strip() for c in line.strip().strip("|").split("|")]
            i += 2
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                if len(rows[-1]) != len(header):
                    problem(here, f"table row has {len(rows[-1])} cells, its header {len(header)}: {lines[i][:60]}")
                i += 1
            t = ['<div class="table"><table>']
            keyed = not any(header)  # "| | |": a two-column list of names and values, as in an experiment's setup
            if not keyed:
                t.append("<thead><tr>" + "".join(f'<th scope="col">{inline(c, here)}</th>' for c in header) + "</tr></thead>")
            t.append("<tbody>")
            for r in rows:
                first = f'<th scope="row">{inline(r[0], here)}</th>' if keyed and r else ""
                t.append("<tr>" + first + "".join(f"<td>{inline(c, here)}</td>" for c in (r[1:] if keyed else r)) + "</tr>")
            t.append("</tbody></table></div>")
            out.append("".join(t))
            continue
        if re.match(r"^\s*([-*]|\d+\.)\s+", line):
            flush()
            block = []
            # An item goes on through indented lines, and through a blank line when the next line is indented.
            while i < len(lines) and (re.match(r"^\s*([-*]|\d+\.)\s+", lines[i]) or (lines[i].startswith("  ") and lines[i].strip())
                                      or (not lines[i].strip() and i + 1 < len(lines) and lines[i + 1].startswith("  ")
                                          and lines[i + 1].strip())):
                block.append(lines[i])
                i += 1
            out.append(render_list(block, here))
            continue
        if line.startswith(">"):
            flush()
            quote = []
            while i < len(lines) and lines[i].startswith(">"):
                quote.append(lines[i].lstrip("> "))
                i += 1
            out.append("<blockquote>" + render("\n".join(quote), here) + "</blockquote>")
            continue
        if not line.strip():
            flush()
            i += 1
            continue
        if re.match(r"^\s*<(?!https?:)[A-Za-z!/]", line):
            problem(here, f"raw HTML or an unknown directive isn't supported: {line.strip()[:60]}")
        para.append(line.strip())
        i += 1
    flush()
    return "\n".join(out)


def render_list(block, here):
    """Lists, nested by indentation; continuation lines and code inside items are kept."""
    first = block[0]
    ordered = bool(re.match(r"^\s*\d+\.", first))
    base = len(first) - len(first.lstrip())
    items = []
    offset = base + 2
    for line in block:
        indent = len(line) - len(line.lstrip())
        m = re.match(r"^(\s*([-*]|\d+\.)\s+)(.*)$", line)
        if m and indent == base:
            items.append([m.group(3)])
            offset = len(m.group(1))  # where the item's text starts: 2 after "- ", 3 after "1. "
        elif items:
            # Continuation lines lose the item's indentation, so code fences and nested lists inside start at column 0.
            items[-1].append(line[min(offset, indent):] if line.strip() else "")
    tag = "ol" if ordered else "ul"
    out = [f"<{tag}>"]
    for item in items:
        head, rest = item[0], item[1:]
        if rest:
            inner = render("\n".join([head] + rest), here)
            inner = re.sub(r"^<p>(.*?)</p>", r"\1", inner, count=1, flags=re.S)
            out.append(f"<li>{inner}</li>")
        else:
            out.append(f"<li>{inline(head, here)}</li>")
    out.append(f"</{tag}>")
    return "".join(out)


def include_excerpt(name, here=None):
    path = os.path.join(ROOT, "site", "examples", name)
    if not os.path.isfile(path):
        problem(here, f"included excerpt site/examples/{name} doesn't exist; run site/examples.py")
        return f'<pre class="excerpt"><code>(missing excerpt: {html.escape(name)})</code></pre>'
    with open(path, encoding="utf-8") as f:
        text = f.read().rstrip("\n")
    return f'<pre class="excerpt"><code>{html.escape(text)}</code></pre>'



RELEASE_NOTES = []  # (kind, release, statement Markdown, source page, section anchor, section title), filled by main()


def statement_after(text, start):
    """The sentence a version note begins, up to its full stop (links and code kept whole)."""
    rest = text[start:]
    i = 0
    while i < len(rest):
        c = rest[i]
        if c in "([`":
            close = {"(": ")", "[": "]", "`": "`"}[c]
            j = rest.find(close, i + 1)
            i = j + 1 if j > 0 else i + 1
            continue
        if c == "." and (i + 1 == len(rest) or rest[i + 1] in " |"):
            return rest[:i + 1].strip()
        if c == "|":
            return rest[:i].strip()
        i += 1
    return rest.strip()


def collect_release_notes(sources):
    notes = []
    for src in sources:
        anchor, section = "", ""
        for line in read(src).split("\n"):
            m = re.match(r"^#{2,3}\s+(.*)$", line)
            if m:
                anchor, section = slug(m.group(1)), m.group(1)
                continue
            for note in VERSION_NOTE.finditer(line):
                notes.append((note.group(1), note.group(2), statement_after(line, note.end()), src, anchor, section))
    return notes


def release_history(here):
    """What each release added and stopped doing, newest first, gathered from the version notes."""
    rows = []
    for newer, older in zip(RELEASES, RELEASES[1:]):
        changes = [("Added", n) for n in RELEASE_NOTES if n[:2] == ("since", newer)]
        changes += [(f"Until {older}", n) for n in RELEASE_NOTES if n[:2] == ("until", older)]
        for what, (_, _, statement, src, anchor, section) in changes:
            where = relpath(SITE_PAGES[src] + (f"#{anchor}" if anchor else ""), here_out(here))
            rows.append(f'<tr><td><span class="release">{newer}</span></td><td>{what}</td><td>{inline(statement, src)}'
                        f'<span class="where">In <a href="{html.escape(where)}">{html.escape(title_of(read(src)))}'
                        f'{": " + inline(section, src) if section else ""}</a></span></td></tr>')
        if not changes:
            rows.append(f'<tr><td><span class="release">{newer}</span></td><td>—</td><td>No change noted from {older}.</td></tr>')
    return ('<div class="table"><table class="differences"><thead><tr><th scope="col">Release</th><th scope="col">Change</th>'
            '<th scope="col">Statement</th></tr></thead><tbody>' + "".join(rows) + "</tbody></table></div>")


def experiment_releases(md):
    """The app releases an experiment ran with, from the Pages, Numbers, Keynote or Apps rows of its setup."""
    found = []
    app = r"(?:Pages|Numbers|Keynote|Apps)"
    # Only the Setup section counts: an observation may list other copies of the apps it found.
    setup = re.search(r"^## Setup\s*$(.*?)(?=^## |\Z)", md, re.M | re.S)
    md = setup.group(1) if setup else md
    for m in re.finditer(rf"^\|\s*({app}(?:,?\s+(?:and\s+)?{app})*)\s*\|([^|\n]*)\|", md, re.M):
        for v in re.findall(r"\b(\d{2}\.\d+)\b", m.group(2)):
            if v not in found:
                found.append(v)
    return found


# --- Feature inventory -------------------------------------------------------------------------

# spec/features.md lists every feature in one table after `<!-- feature-inventory -->`. The table says
# which apps have the feature, which experiments are its evidence and which issue owns it; the builder
# works out from each cited experiment's setup which app and release it ran with and whether it wrote
# the document, so what the coverage columns say is never typed by hand. It also writes the result to
# spec/features.json for other tools.
APPS = ("Pages", "Numbers", "Keynote")
CAPABILITIES = ("read", "edit", "create", "render")  # every feature has these
EXTRA_CAPABILITIES = ("calculate", "play")            # a feature has these when its Also column names them
FEATURE_COLUMNS = ["ID", "Feature", "Apps", "Also", "Evidence", "Owner", "Spec"]
FEATURE_ID = re.compile(r"^[a-z]+(?:\.[a-z0-9]+(?:-[a-z0-9]+)*)+$")
EVIDENCE_ITEM = re.compile(rf"^(?:({'|'.join(CAPABILITIES + EXTRA_CAPABILITIES)})\s+)?(\d{{4}})$")
STATE_TEXT = {"shown": "Shown", "not tested": "Not tested", "not applicable": "Doesn't apply",
              "not checked": "Not checked whether the app has it"}
FEATURES = []        # filled by render() from the current spec/features.md, for spec/features.json
_EXPERIMENT_FILES = {}


def experiment_file(number):
    """The experiment's Markdown file name for a four-digit number, or None."""
    if not _EXPERIMENT_FILES:
        for f in os.listdir(os.path.join(ROOT, "experiments")):
            if re.match(r"^\d{4}-.*\.md$", f):
                _EXPERIMENT_FILES[f[:4]] = f
    return _EXPERIMENT_FILES.get(number)


def experiment_apps(md):
    """The apps an experiment ran with, from the Pages, Numbers, Keynote or Apps rows of its setup."""
    setup = re.search(r"^## Setup\s*$(.*?)(?=^## |\Z)", md, re.M | re.S)
    md = setup.group(1) if setup else md
    found = []
    for m in re.finditer(r"^\|\s*([^|\n]+?)\s*\|([^|\n]*)\|", md, re.M):
        label, value = m.group(1), m.group(2)
        if label == "Apps":
            names = re.split(r"\d", value, maxsplit=1)[0]  # "Pages and Numbers 14.5 ...; no Keynote there"
        elif re.fullmatch(r"(?:Pages|Numbers|Keynote)(?:,?\s+(?:and\s+)?(?:Pages|Numbers|Keynote))*", label):
            names = label
        else:
            continue
        found += [a for a in APPS if re.search(rf"\b{a}\b", names) and a not in found]
    return [a for a in APPS if a in found]


def experiment_writes(name, md):
    """Whether an experiment changed a saved document with the project's writer, rather than only reading one."""
    setup = re.search(r"^## Setup\s*$(.*?)(?=^## |\Z)", md, re.M | re.S)
    return "-writing-" in name or bool(setup and re.search(r"^\|\s*Writers?\s*\|", setup.group(1), re.M))


def parse_features(rows, here):
    """The inventory's rows as feature records, reporting anything the coverage can't be worked out from."""
    features, seen = [], set()
    for r in rows:
        if len(r) != len(FEATURE_COLUMNS):
            continue  # render() has reported the row already
        fid, name, apps, also, evidence, owner, spec = r
        fid = fid.strip("`")
        if not FEATURE_ID.match(fid):
            problem(here, f"feature ID isn't area.name in lower case: {fid}")
        if fid in seen:
            problem(here, f"feature ID used twice: {fid}")
        seen.add(fid)
        applies = {a: "no" for a in APPS}
        for token in [t.strip() for t in apps.split(",") if t.strip()]:
            if token.rstrip("?") not in APPS:
                problem(here, f"{fid}: unknown app {token!r}")
                continue
            applies[token.rstrip("?")] = "unverified" if token.endswith("?") else "yes"
        caps = list(CAPABILITIES)
        for token in [t.strip() for t in also.split(",") if t.strip() not in ("", "—")]:
            if token not in EXTRA_CAPABILITIES:
                problem(here, f"{fid}: unknown capability in Also: {token!r}")
            elif token not in caps:
                caps.append(token)
        owners = re.findall(r"\[#(\d+)\]\(https://github\.com/alehel/iwork-format/issues/(\d+)\)", owner)
        if len(owners) != 1 or owners[0][0] != owners[0][1]:
            problem(here, f"{fid}: the Owner column needs exactly one issue link, [#N]({REPO}/issues/N)")
        formats = {a: {"applies": applies[a], "releases": [], "capabilities": {c: [] for c in caps}} for a in APPS}
        cited = []
        for token in [t.strip() for t in evidence.split(",") if t.strip() not in ("", "—")]:
            m = EVIDENCE_ITEM.match(token)
            f = experiment_file(m.group(2)) if m else None
            if not f:
                problem(here, f"{fid}: evidence isn't an experiment number: {token!r}")
                continue
            md = read(f"experiments/{f}")
            cap = m.group(1) or ("edit" if experiment_writes(f, md) else "read")
            if cap not in caps:
                problem(here, f"{fid}: evidence for {cap}, which the feature doesn't have: {token}")
                continue
            cited.append(f)
            for a in experiment_apps(md):
                if applies[a] == "no":
                    problem(here, f"{fid}: {m.group(2)} ran in {a}, which its Apps column leaves out")
                    continue
                applies[a] = formats[a]["applies"] = "yes"
                if m.group(2) not in formats[a]["capabilities"][cap]:
                    formats[a]["capabilities"][cap].append(m.group(2))
                for rel in experiment_releases(md):
                    if rel not in formats[a]["releases"]:
                        formats[a]["releases"].append(rel)
        for a in APPS:
            formats[a]["releases"].sort(key=version_key)
        features.append({"id": fid, "name": name, "owner": int(owners[0][0]) if owners else None,
                         "spec": spec, "capabilities": caps, "formats": formats, "experiments": cited})
    return features


def capability_state(feature, app, cap):
    fmt = feature["formats"][app]
    if fmt["applies"] == "no":
        return "not applicable"
    if fmt["applies"] == "unverified":
        return "not checked"
    return "shown" if fmt["capabilities"][cap] else "not tested"


def feature_cell(feature, app):
    fmt = feature["formats"][app]
    states = {c: capability_state(feature, app, c) for c in feature["capabilities"]}
    if fmt["applies"] != "yes":
        return f'<span class="state">{STATE_TEXT[states["read"]]}</span>'
    shown = [c for c in feature["capabilities"] if states[c] == "shown"]
    untested = [c for c in feature["capabilities"] if states[c] == "not tested"]
    parts = []
    if shown:
        parts.append(f'<span class="state shown">Shown: {", ".join(shown)}</span>'
                     + (f' <span class="release">{html.escape(", ".join(fmt["releases"]))}</span>' if fmt["releases"] else ""))
    if untested:
        parts.append(f'<span class="state">Not tested: {", ".join(untested)}</span>')
    return "<br>".join(parts)


def feature_inventory(rows, here):
    """The inventory table, with each app's coverage worked out from the cited experiments."""
    features = parse_features(rows, here)
    if here == "spec/features.md":
        FEATURES[:] = features
    out_here = here_out(here)
    counts = []
    for a in APPS:
        has = [f for f in features if f["formats"][a]["applies"] == "yes"]
        unchecked = sum(1 for f in features if f["formats"][a]["applies"] == "unverified")
        shown = {c: sum(1 for f in has if f["formats"][a]["capabilities"].get(c)) for c in CAPABILITIES}
        counts.append(f'<tr><th scope="row">{a}</th><td>{len(has)}</td><td>{unchecked}</td>'
                      + "".join(f"<td>{shown[c]}</td>" for c in CAPABILITIES) + "</tr>")
    summary = ('<div class="table"><table><thead><tr><th scope="col">App</th><th scope="col">Has the feature</th>'
               '<th scope="col">Not checked</th>' + "".join(f'<th scope="col">{c.capitalize()} shown</th>' for c in CAPABILITIES)
               + "</tr></thead><tbody>" + "".join(counts) + "</tbody></table></div>")
    body = []
    for f in features:
        links = ", ".join(f'<a href="{html.escape(relpath(SITE_PAGES.get("experiments/" + e, "experiments/" + e[:-3] + ".html"), out_here))}">{e[:4]}</a>'
                          for e in f["experiments"])
        n = len(f["experiments"])
        links = (f'<details><summary>{n} experiment{"s" if n != 1 else ""}</summary>{links}</details>' if n else "None yet")
        owner = f'<a href="{REPO}/issues/{f["owner"]}">#{f["owner"]}</a>' if f["owner"] else ""
        spec = f'<span class="where">{inline(f["spec"], here)}</span>' if f["spec"] not in ("", "—") else ""
        body.append(f'<tr id="feature-{html.escape(f["id"].replace(".", "-"))}"><th scope="row"><code>{html.escape(f["id"])}</code> '
                    f'{inline(f["name"], here)}{spec}</th>'
                    + "".join(f'<td><span class="app">{a}: </span>{feature_cell(f, a)}</td>' for a in APPS)
                    + f'<td class="exps">{links}</td><td class="owner"><span class="app">Owner: </span>{owner}</td></tr>')
    table = ('<div class="table"><table class="features"><thead><tr><th scope="col">Feature</th>'
             + "".join(f'<th scope="col">{a}</th>' for a in APPS)
             + '<th scope="col">Evidence</th><th scope="col">Owner</th></tr></thead><tbody>'
             + "".join(body) + "</tbody></table></div>")
    return summary + table


def features_json():
    """spec/features.json: the inventory with every capability's state spelled out, for other tools."""
    out = []
    for f in FEATURES:
        formats = {}
        for a in APPS:
            fmt = f["formats"][a]
            formats[a] = {"applies": fmt["applies"], "releases": fmt["releases"],
                          "capabilities": {c: {"state": capability_state(f, a, c), "evidence": fmt["capabilities"][c]}
                                           for c in f["capabilities"]}}
        spec = re.match(r"^\[[^\]]+\]\(([^)]+)\)", f["spec"])
        out.append({"id": f["id"], "feature": re.sub(r"[`*]", "", f["name"]), "owner": f["owner"],
                    "owner_url": f"{REPO}/issues/{f['owner']}" if f["owner"] else None,
                    "spec": "spec/" + link_target(spec.group(1), "spec/features.md") if spec else None,
                    "page": f"spec/features.html#feature-{f['id'].replace('.', '-')}",
                    "formats": formats, "experiments": [e[:4] for e in f["experiments"]]})
    return {"producer": "Apple Pages, Numbers and Keynote for macOS",
            "states": list(STATE_TEXT), "capabilities": list(CAPABILITIES + EXTRA_CAPABILITIES), "features": out}


# --- Record type index -------------------------------------------------------------------------

# "type 6001", "type-6001 record", "types 401, 2022 and 2023", "Type-10012 field"
TYPE_MENTION = re.compile(r"\b[Tt]ypes?[- ](\d{1,5}(?:(?:,\s*(?:and\s+|or\s+)?|\s+and\s+|\s+or\s+|–)\d{1,5})*)\b")
# Numbers that aren't record types: formula node types, list types, a cell value's type
NOT_RECORD_BEFORE = re.compile(r"(?:node|list|list of|value|cell|boolean \()\s*$", re.I)
NOT_RECORD_AFTER = re.compile(r"^\s+list\b")


def record_types(text):
    """The record type numbers a piece of text names."""
    for m in TYPE_MENTION.finditer(text):
        if NOT_RECORD_BEFORE.search(text[max(0, m.start() - 12):m.start()]) or NOT_RECORD_AFTER.match(text[m.end():]):
            continue
        for n in re.findall(r"\d+", m.group(1)):
            yield int(n)


CHAPTERS = {"README.md": "Layers and status", "container.md": "Container", "text.md": "Text", "styles.md": "Styles",
            "tables.md": "Tables", "drawables.md": "Drawables", "pages.md": "Pages", "keynote.md": "Keynote",
            "numbers.md": "Numbers", "features.md": "Features and scope"}


def type_mentions(md):
    """Yield (type, heading of the section it is in, row of a type table or None) for each record type named."""
    heading, in_type_table = None, False
    for line in md.split("\n"):
        m = re.match(r"^#{1,4}\s+(.*)$", line)
        if m:
            heading, in_type_table = m.group(1), False
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")] if line.startswith("|") else None
        if cells is None:
            in_type_table = False
        elif cells[0] == "Type":
            in_type_table = True
            continue
        elif in_type_table and re.fullmatch(r"\d{1,5}", cells[0]):
            yield int(cells[0]), heading, cells
        for n in record_types(line):
            yield n, heading, None


def plain(md_text, here):
    return re.sub(r"<[^>]+>", "", html.unescape(inline(md_text, here)))


def first_sentence(text, limit=160):
    m = re.match(r"(.+?[.:])(?:\s|$)", text)
    text = m.group(1).rstrip(":") if m else text
    return text if len(text) <= limit else text[:limit].rsplit(" ", 1)[0] + "…"


def excerpt(sentence, number, limit=240):
    """The sentence, or a window of it around the first place it names the number when it is long."""
    if len(sentence) <= limit:
        return sentence
    at = sentence.find(number)
    start = 0 if at < limit // 2 else sentence.rfind(" ", 0, at - limit // 3) + 1
    window = sentence[start:start + limit]
    if start + limit < len(sentence):
        window = window.rsplit(" ", 1)[0] + "…"
    return ("…" if start else "") + window


def types_page(spec_sources, experiments):
    """Build spec/types.html: every record type the current spec names, where it is described and which experiments name it."""
    out_path = "spec/types.html"
    found = {}  # type -> {"holds": str, "part": str, "where": [(src, heading)], "experiments": [file]}
    for src in spec_sources:
        md = read(f"spec/{src}")
        for n, heading, row in type_mentions(md):
            t = found.setdefault(n, {"holds": "", "part": "", "where": [], "experiments": []})
            if row and not t["holds"]:
                t["holds"] = f"{CHAPTERS[src]}: " + first_sentence(plain(row[1], f"spec/{src}"))
                t["part"] = plain(row[2], f"spec/{src}") if len(row) > 2 else ""
            if (src, heading) not in t["where"]:
                t["where"].append((src, heading))
    # Types no table describes get the first sentence of the spec that names them, as context.
    for src in spec_sources:
        for line in read(f"spec/{src}").split("\n"):
            if line.startswith(("#", "```")):
                continue
            for chunk in line.strip("|").split(" | ") if line.startswith("|") else [line]:
                for sentence in re.split(r"(?<=[.)])\s+(?=[A-Z*`(])", plain(chunk, f"spec/{src}")):
                    for n in record_types(sentence):
                        t = found.get(n)
                        if t and not t["holds"] and not t.get("said"):
                            t["said"] = excerpt(sentence.strip(), str(n))
    for f in experiments:
        for n in sorted({n for n, _, _ in type_mentions(read(f"experiments/{f}"))}):
            if n in found:
                found[n]["experiments"].append(f)
    rows = []
    for n in sorted(found):
        t = found[n]
        where = []
        for src, heading in t["where"]:
            target = SITE_PAGES[f"spec/{src}"] + (f"#{slug(heading)}" if heading and not heading.startswith(title_of(read(f'spec/{src}'))) else "")
            label = CHAPTERS.get(src, src) + (f" › {plain(heading, f'spec/{src}')}" if heading and not re.match(r"^\d", heading) else "")
            where.append(f'<a href="{relpath(target, out_path)}">{html.escape(label)}</a>')
        exps = t["experiments"]
        ex_html = ""
        if exps:
            links = ", ".join(f'<a href="{relpath(SITE_PAGES["experiments/" + f], out_path)}">{f[:4]}</a>' for f in exps)
            ex_html = f"<details><summary>{len(exps)}</summary>{links}</details>"
        if t["holds"]:
            holds = html.escape(t["holds"]) + (f' <span class="part">in {html.escape(t["part"])}</span>' if t["part"] else "")
        else:
            holds = f'<span class="said">{html.escape(t.get("said", ""))}</span>'

        SEARCH_ENTRIES.append({"k": "type", "t": f"Type {n}", "u": f"{out_path}#type-{n}",
                               "x": text_of(holds) + " Described in: " + "; ".join(text_of(w) for w in where)})
        rows.append(f'<tr id="type-{n}"><td class="num"><a href="#type-{n}">{n}</a></td><td>{holds}</td>'
                    f'<td class="where">{"<br>".join(where)}</td><td class="exps">{ex_html}</td></tr>')
    body = ("<h1>Record types</h1>"
            f"<p>Every record type the specification names, {len(found)} in all, with the sections that describe it. "
            "Types are the numbers in field 2.1 of a record's header (<a href=\"container.html\">Container</a>). "
            "The same number means the same kind of record in Pages, Keynote and Numbers wherever the spec has compared them, "
            "but most types have been seen in one app only. <em>What it is</em> comes from the type tables in the "
            "Keynote and Numbers chapters where there is one; otherwise it is the first sentence of the spec that names the "
            "type, shown in grey, for context only. The linked sections give the rules, with their confidence. "
            "<em>Experiments</em> lists those that name the type, as evidence.</p>"
            "<p>This page is generated from the specification's Markdown each time the site is built. "
            "Link to a type as <code>types.html#type-6001</code>.</p>"
            '<div class="table"><table class="types"><thead><tr><th>Type</th><th>What it is</th><th>Described in</th>'
            "<th>Experiments</th></tr></thead><tbody>" + "".join(rows) + "</tbody></table></div>")
    page(out_path, "Record types", body, description="Every iWork record type the specification names, with where it is described.", wide=True)
    return len(found)


# --- Search and the experiments-by-topic index -----------------------------------------------

SEARCH_ENTRIES = []  # filled by main(): {"k": kind, "t": title, "u": site path, "x": plain text}
SEARCH_KINDS = {"type": "Record types", "spec": "Specification", "guide": "Guides", "exp": "Experiments"}
HEADING = re.compile(r'<h([1-4]) id="([^"]+)">(.*?)<a class="anchor"[^>]*>#</a></h\1>', re.S)


def text_of(fragment):
    """Rendered HTML as plain text on one line."""
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", fragment))).strip()


def index_sections(kind, out_path, page_title, body, only=None):
    """Add one search entry per section of a rendered page. Text before the first section heading
    goes with the page's title. only, if given, keeps just the sections with those headings."""
    marks = list(HEADING.finditer(body))
    starts = [m for m in marks if m.group(1) != "1"]
    first = starts[0].start() if starts else len(body)
    intro = HEADING.sub("", body[:first], count=1) if marks and marks[0].group(1) == "1" else body[:first]
    if text_of(intro):
        SEARCH_ENTRIES.append({"k": kind, "t": page_title, "u": out_path, "x": text_of(intro)})
    for n, m in enumerate(starts):
        heading = text_of(m.group(3))
        if only is not None and heading not in only:
            continue
        end = starts[n + 1].start() if n + 1 < len(starts) else len(body)
        text = text_of(body[m.end():end])
        if text:
            SEARCH_ENTRIES.append({"k": kind, "t": f"{page_title} › {heading}", "u": f"{out_path}#{m.group(2)}", "x": text})


EXPERIMENT_LINK = re.compile(r"\]\((?:\.\./)?experiments/(\d{4}-[^)#]+)\.md")


def topics_page(spec_sources, experiments):
    """Build experiments/topics.html: for each section of the current spec, the experiments it cites."""
    out_path = "experiments/topics.html"
    titles = {f: title_of(read(f"experiments/{f}")).partition(": ")[2] for f in experiments}
    cited = set()
    rows = []
    for src in spec_sources:
        md = read(f"spec/{src}")
        chapter = CHAPTERS.get(src, src)
        sections = [(None, [])]
        anchors = set()
        for line in md.split("\n"):
            m = re.match(r"^(#{2,4})\s+(.*)$", line)
            if m:
                anchor = slug(m.group(2))
                n = 2
                while anchor in anchors:
                    anchor, n = f"{slug(m.group(2))}-{n}", n + 1
                anchors.add(anchor)
                sections.append(((m.group(2), anchor), []))
            elif not line.startswith("#"):
                sections[-1][1].extend(f + ".md" for f in EXPERIMENT_LINK.findall(line))
        for heading, found in sections:
            found = sorted(set(f for f in found if f in titles))
            if not found:
                continue
            cited.update(found)
            target = SITE_PAGES[f"spec/{src}"] + (f"#{heading[1]}" if heading else "")
            label = chapter + (f" › {plain(heading[0], f'spec/{src}')}" if heading else "")
            links = "".join(f'<li><a href="{f[:-3]}.html">{f[:4]}</a> {html.escape(titles[f])}</li>' for f in found)
            rows.append(f'<tr><td><a href="{relpath(target, out_path)}">{html.escape(label)}</a></td>'
                        f'<td class="exps"><details><summary>{len(found)}</summary><ul>{links}</ul></details></td></tr>')
    uncited = [f for f in experiments if f not in cited]
    rest = "".join(f'<li><a href="{f[:-3]}.html">{f[:4]}</a> {html.escape(titles[f])}</li>' for f in uncited)
    body = ("<h1>Experiments by topic</h1>"
            "<p>Each section of the specification, with the experiments it cites as evidence. An experiment cited "
            "in several sections is listed under each. The section states the rule and how sure it is; the experiments "
            "are the observations behind it. Generated from the specification's links each time the site is built.</p>"
            '<div class="table"><table class="topics"><thead><tr><th>Section</th><th>Experiments</th></tr></thead><tbody>'
            + "".join(rows) + "</tbody></table></div>"
            f'<h2 id="not-cited">Not cited by the specification<a class="anchor" href="#not-cited" '
            f'aria-label="Link to this section: Not cited by the specification">#</a></h2>'
            f"<p>{len(uncited)} experiments no section links to yet: some found nothing new, some only checked a tool or a "
            "release, and some are evidence the spec hasn't taken in yet.</p>"
            f'<ul class="uncited">{rest}</ul>')
    page(out_path, "Experiments by topic", body, description="The experiments behind each section of the iWork specification.", wide=True)
    return len(rows)


SEARCH_SCRIPT = r"""
(function () {
  var form = document.getElementById("search-form"), box = document.getElementById("search-q");
  var out = document.getElementById("search-results"), status = document.getElementById("search-status");
  var kinds = KINDS, entries = window.SEARCH_INDEX || [];
  form.hidden = false;
  document.getElementById("search-needs-script").hidden = true;
  function esc(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); }
  function source(tok) {
    // A number or field path matches whole, so 6001 doesn't find 60010 and 4.3 doesn't find 4.3.1.
    return /^[0-9][0-9.]*$/.test(tok) ? "(?<![0-9.])" + esc(tok) + "(?![0-9]|\\.[0-9])" : esc(tok);
  }
  function snippet(text, srcs) {
    var first = new RegExp(srcs.join("|"), "i").exec(text), at = first ? first.index : 0;
    var start = Math.max(0, at - 90), end = Math.min(text.length, at + 170);
    if (start > 0) start = text.indexOf(" ", start) + 1;
    var s = (start > 0 ? "… " : "") + text.slice(start, end) + (end < text.length ? " …" : "");
    var frag = document.createDocumentFragment(), re = new RegExp(srcs.join("|"), "gi"), last = 0, m;
    while ((m = re.exec(s)) && m[0].length) {
      frag.appendChild(document.createTextNode(s.slice(last, m.index)));
      var mark = document.createElement("mark"); mark.textContent = m[0]; frag.appendChild(mark);
      last = m.index + m[0].length;
    }
    frag.appendChild(document.createTextNode(s.slice(last)));
    return frag;
  }
  function run(q) {
    out.textContent = "";
    var toks = q.trim().split(/\s+/).filter(Boolean);
    if (!toks.length) { status.textContent = ""; return; }
    var srcs = toks.map(source), pats = srcs.map(function (x) { return new RegExp(x, "i"); }), groups = {};
    entries.forEach(function (e) {
      var score = 0;
      for (var i = 0; i < pats.length; i++) {
        var inT = pats[i].test(e.t), inX = pats[i].test(e.x);
        if (!inT && !inX) return;
        score += inT ? 10 : 1;
      }
      (groups[e.k] = groups[e.k] || []).push({ e: e, s: score });
    });
    var total = 0, shown = 0;
    Object.keys(kinds).forEach(function (k) {
      var list = groups[k];
      if (!list) return;
      list.sort(function (a, b) { return b.s - a.s; });
      total += list.length;
      var h = document.createElement("h2"); h.textContent = kinds[k] + " (" + list.length + ")";
      out.appendChild(h);
      var ol = document.createElement("ol"); ol.className = "results";
      list.slice(0, 40).forEach(function (r) {
        var li = document.createElement("li"), a = document.createElement("a");
        a.href = PREFIX + r.e.u; a.textContent = r.e.t; li.appendChild(a);
        var p = document.createElement("p"); p.appendChild(snippet(r.e.x, srcs)); li.appendChild(p);
        ol.appendChild(li); shown++;
      });
      out.appendChild(ol);
      if (list.length > 40) {
        var more = document.createElement("p"); more.className = "more";
        more.textContent = (list.length - 40) + " more " + kinds[k].toLowerCase() + " results; add a word to narrow them.";
        out.appendChild(more);
      }
    });
    status.textContent = total ? total + (total === 1 ? " result" : " results") + " for " + q.trim()
      : "Nothing found for " + q.trim() + ". Try fewer words, a record type such as 6001, or a field path such as 4.3.1.2, or browse the indexes below.";
  }
  var timer;
  box.addEventListener("input", function () {
    clearTimeout(timer);
    timer = setTimeout(function () {
      var u = new URL(location.href);
      if (box.value) u.searchParams.set("q", box.value); else u.searchParams.delete("q");
      history.replaceState(null, "", u);
      run(box.value);
    }, 150);
  });
  form.addEventListener("submit", function (e) { e.preventDefault(); run(box.value); });
  var q = new URLSearchParams(location.search).get("q") || "";
  box.value = q;
  run(q);
})();
"""


def search_page():
    """Build search.html and search-index.js. The index is a script, not JSON, so it also loads from file://."""
    with open(os.path.join(OUT, "search-index.js"), "w", encoding="utf-8") as f:
        f.write("window.SEARCH_INDEX=" + json.dumps(SEARCH_ENTRIES, ensure_ascii=False, separators=(",", ":")) + ";\n")
    script = SEARCH_SCRIPT.replace("KINDS", json.dumps(SEARCH_KINDS)).replace("PREFIX", json.dumps(""))
    body = ("<h1>Search</h1>"
            "<p>Searches the specification, the guides, the record types and each experiment's summary and conclusion. "
            "Results from the specification are the rules; results from experiments are what was observed. "
            "A number or field path, such as <code>6001</code> or <code>4.3.1.2</code>, matches only whole.</p>"
            '<form id="search-form" class="search-page" role="search" hidden><label for="search-q">Search for</label>'
            '<input id="search-q" type="search" name="q" autocomplete="off" spellcheck="false">'
            '<button type="submit">Search</button></form>'
            '<p id="search-needs-script" class="note">Search needs JavaScript. Without it, use the indexes below.</p>'
            '<p id="search-status" role="status" aria-live="polite"></p><div id="search-results"></div>'
            '<h2 id="indexes">Indexes<a class="anchor" href="#indexes" aria-label="Link to this section: Indexes">#</a></h2><ul>'
            '<li><a href="spec/types.html">Record types</a>: every type number, what it is and where it is described</li>'
            '<li><a href="experiments/topics.html">Experiments by topic</a>: the experiments behind each section of the spec</li>'
            '<li><a href="experiments/index.html">All experiments</a>, by number</li>'
            '<li><a href="spec/index.html">The specification\'s chapters</a></li></ul>'
            '<script src="search-index.js"></script><script>' + script + "</script>")
    page("search.html", "Search", body, description="Search the iWork file format specification and its experiments.")
    return len(SEARCH_ENTRIES)


# --- Pages -----------------------------------------------------------------------------------

SITE_PAGES = {}


def here_out(source):
    return SITE_PAGES.get(source, "index.html")


def relpath(target, start):
    return os.path.relpath(target, os.path.dirname(start) or ".").replace(os.sep, "/")


NAV = [
    ("Overview", "index.html"),
    ("Guides", None),
    ("Reading a Pages document", "guides/anatomy.html"),
    ("Reading a Numbers table", "guides/numbers-table.html"),
    ("Writing a document", "guides/writing.html"),
    ("Sample files", "guides/samples.html"),
    ("Specification", None),
    ("Layers and status", "spec/index.html"),
    ("1. Container", "spec/container.html"),
    ("2. Text", "spec/text.html"),
    ("3. Styles", "spec/styles.html"),
    ("4. Tables", "spec/tables.html"),
    ("5. Drawables, media and charts", "spec/drawables.html"),
    ("Apps", None),
    ("Pages", "spec/pages.html"),
    ("Keynote", "spec/keynote.html"),
    ("Numbers", "spec/numbers.html"),
    ("Reference", None),
    ("Search", "search.html"),
    ("Record types", "spec/types.html"),
    ("Features and scope", "spec/features.html"),
    ("Releases", "spec/releases.html"),
    ("Evidence", None),
    ("All experiments", "experiments/index.html"),
    ("By topic", "experiments/topics.html"),
]


BUILD_REVISION = None  # filled by main(): (commit the build was made on, whether sources had uncommitted changes)


def releases_line(out_path):
    """What the spec describes and which other releases were checked, linking to the releases page."""
    text = f"Describes {CURRENT} · also checked: " + ", ".join(RELEASES[1:])
    return f'<li class="releases-line"><a href="{relpath("spec/releases.html", out_path)}">{html.escape(text)}</a></li>'


def page(out_path, title, body, toc=None, description="", source=None, wide=False):
    """source is the repository path of the Markdown the page is built from, linked in the footer.
    wide lets a page without an on-this-page list use that column too, for wide tables."""
    nav = []
    for label, href in NAV:
        if href is None:
            nav.append(f'<li class="group">{html.escape(label)}</li>')
            if label == "Specification":
                nav.append(releases_line(out_path))
            continue
        cls = ' class="current" aria-current="page"' if href == out_path else ""
        nav.append(f'<li><a{cls} href="{relpath(href, out_path)}">{html.escape(label)}</a></li>')
    toc_html = ""
    if toc:
        toc_html = '<nav class="toc" aria-label="On this page"><details open><summary>On this page</summary><ul>' + "".join(
            f'<li><a href="#{a}">{html.escape(t)}</a></li>' for a, t in toc) + "</ul></details></nav>"
    css = relpath("style.css", out_path)
    home = relpath("index.html", out_path)
    footer = "Built from the repository's Markdown. Every finding links to the experiment behind it."
    if source:
        footer += f' Source: <a href="{REPO}/blob/main/{html.escape(source)}"><code>{html.escape(source)}</code></a>.'
    if out_path == "index.html" and BUILD_REVISION:
        rev, dirty = BUILD_REVISION
        footer += (f' Built on revision <a href="{REPO}/commit/{rev}"><code>{rev[:7]}</code></a>'
                   + (", with the changes committed alongside this build." if dirty else "."))
    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} · {TITLE}</title>
<meta name="description" content="{html.escape(description or TITLE)}">
<link rel="stylesheet" href="{css}">
</head>
<body>
<a class="skip" href="#page-content">Skip to content</a>
<header class="top"><a class="brand" href="{home}">iWork format</a><span class="sub">A clean-room specification of Pages, Keynote and Numbers files</span><form class="search" action="{relpath("search.html", out_path)}" role="search"><input type="search" name="q" aria-label="Search the specification" placeholder="Search, e.g. 6001"></form><a class="repo" href="{REPO}">Repository</a></header>
<p class="wip"><strong>Work in progress.</strong> This specification is incomplete and changes as new experiments run. Each finding says how sure it is: <em>confirmed</em>, <em>likely</em> or <em>unknown</em>. See <a href="{relpath("spec/index.html", out_path)}">what each chapter covers so far</a>.</p>
<div class="layout{'' if toc_html else ' no-toc'}{' wide' if wide and not toc_html else ''}">
<nav class="side" aria-label="Contents"><details open><summary>Contents</summary><ul>{''.join(nav)}</ul></details></nav>
{toc_html}
<main id="page-content" tabindex="-1">
{body}
<footer><p>{footer}</p></footer>
</main>
</div>
<script>
// On narrow screens the contents and on-this-page lists start folded; on wide ones they stay open.
(function () {{
  // From 48rem to 72rem the on-this-page list sits folded above the page instead of beside it.
  var narrow = window.matchMedia("(max-width: 48rem)");
  var middle = window.matchMedia("(max-width: 72rem)");
  var side = document.querySelector(".side > details"), toc = document.querySelector(".toc > details");
  var tocSummary = document.querySelector(".toc summary");
  function fit() {{
    if (side) side.open = !narrow.matches;
    if (toc) toc.open = !middle.matches;
    // On wide screens the list can't fold, so its heading isn't a control.
    if (tocSummary) {{ if (middle.matches) tocSummary.removeAttribute("tabindex"); else tocSummary.tabIndex = -1; }}
    scrollers();
  }}
  // A table or code block wider than the page scrolls sideways; make it reachable by keyboard, with a name.
  function scrollers() {{
    var boxes = document.querySelectorAll("main .table, main pre");
    for (var i = 0; i < boxes.length; i++) {{
      var b = boxes[i];
      if (b.scrollWidth > b.clientWidth + 1) {{
        b.tabIndex = 0; b.setAttribute("role", "region");
        b.setAttribute("aria-label", (b.tagName === "PRE" ? "Code" : "Table") + ", scrolls sideways");
      }} else if (b.hasAttribute("role")) {{
        b.removeAttribute("tabindex"); b.removeAttribute("role"); b.removeAttribute("aria-label");
      }}
    }}
  }}
  window.addEventListener("resize", scrollers);
  fit();
  if (narrow.addEventListener) {{ narrow.addEventListener("change", fit); middle.addEventListener("change", fit); }}
  document.addEventListener("click", function (e) {{
    if (middle.matches && e.target.closest && e.target.closest(".toc a")) fit();
  }});
}})();
</script>
</body>
</html>
"""
    path = os.path.join(OUT, out_path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(doc)


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return f.read()


def title_of(md):
    m = re.search(r"^#\s+(.*)$", md, re.M)
    return re.sub(r"`", "", m.group(1)) if m else "Untitled"


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)

    global BUILD_REVISION
    BUILD_REVISION = build_revision()
    spec_map = {f"spec/{src}": f"spec/{out}" for src, out in SPEC_PAGES}
    SITE_PAGES.update(spec_map)
    SITE_PAGES["README.md"] = "index.html"
    experiments = sorted(f for f in os.listdir(os.path.join(ROOT, "experiments")) if re.match(r"^\d{4}-.*\.md$", f))
    for f in experiments:
        SITE_PAGES[f"experiments/{f}"] = f"experiments/{f[:-3]}.html"
    for f in experiments:
        for r in experiment_releases(read(f"experiments/{f}")):
            if r not in RELEASES:
                problem(f"experiments/{f}", f"ran with {r}, which RELEASES in site/build.py doesn't list")
    RELEASE_NOTES[:] = collect_release_notes([src for src in spec_map if not src.endswith("releases.md")])
    guides = sorted(f for f in os.listdir(os.path.join(ROOT, "site", "guides")) if f.endswith(".md"))
    for f in guides:
        SITE_PAGES[f"site/guides/{f}"] = f"guides/{f[:-3]}.html"

    # Overview: the guide's own front page.
    md = read("site/guides/index.md")
    SITE_PAGES["site/guides/index.md"] = "index.html"
    toc = []
    page("index.html", "Overview", render(md, "site/guides/index.md", toc), toc, source="site/guides/index.md")

    for src, out in spec_map.items():
        md = read(src)
        toc = []
        body = render(md, src, toc)
        page(out, title_of(md), body, toc, source=src)
        if not src.endswith(("README.md", "releases.md")):
            index_sections("spec", out, CHAPTERS.get(os.path.basename(src), title_of(md)), body)

    for f in guides:
        if f == "index.md":
            continue
        src = f"site/guides/{f}"
        md = read(src)
        toc = []
        body = render(md, src, toc)
        page(f"guides/{f[:-3]}.html", title_of(md), body, toc, source=src)
        index_sections("guide", f"guides/{f[:-3]}.html", title_of(md), body)

    rows = []
    for f in experiments:
        md = read(f"experiments/{f}")
        title = title_of(md)
        src = f"experiments/{f}"
        releases = experiment_releases(md)
        body = render(md, src)
        if releases:
            badge = f'<p class="ran">App release: ' + ", ".join(f'<span class="release">{html.escape(r)}</span>' for r in releases) + "</p>"
            body = body.replace("</h1>", "</h1>" + badge, 1)
        page(f"experiments/{f[:-3]}.html", title, body, None, source=src)
        index_sections("exp", f"experiments/{f[:-3]}.html", title, body, only={"Conclusion", "Confidence"})
        num, _, name = title.partition(": ")
        rel = ", ".join(releases) or "tool only"
        rows.append(f'<tr><td class="num">{html.escape(num)}</td><td><a href="{f[:-3]}.html">{html.escape(name or title)}</a></td>'
                    f'<td class="rel">{html.escape(rel)}</td></tr>')
    counts = {}
    for f in experiments:
        for r in experiment_releases(read(f"experiments/{f}")):
            counts[r] = counts.get(r, 0) + 1
    by_release = ", ".join(f"{n} with the {r} apps" for r, n in sorted(counts.items(), key=lambda x: version_key(x[0]), reverse=True))
    tool_only = sum(1 for f in experiments if not experiment_releases(read(f"experiments/{f}")))
    body = ("<h1>All experiments</h1><p>Each experiment changes one thing in a document, saves it, and "
            "records what changed in the file. The specification cites them as its evidence. "
            f"{len(experiments)} have been run: {by_release}, as each one's setup records"
            + (f", and {tool_only} with the tool alone. " if tool_only else ". ") +
            f'The <a href="../spec/releases.html">releases</a> page says how the releases differ.</p>'
            "<div class=\"table\"><table><thead><tr><th>No.</th><th>Experiment</th><th>App release</th></tr></thead><tbody>"
            + "".join(rows) + "</tbody></table></div>")
    page("experiments/index.html", "All experiments", body)
    chapters = [src for src, _ in SPEC_PAGES if src not in ("releases.md", "features.md")]
    n_types = types_page(chapters, experiments)
    n_topics = topics_page([src for src in chapters if src != "README.md"], experiments)
    n_search = search_page()
    with open(os.path.join(OUT, "spec", "features.json"), "w", encoding="utf-8") as f:
        json.dump(features_json(), f, indent=1, ensure_ascii=False)
        f.write("\n")

    shutil.copy(os.path.join(ROOT, "site", "style.css"), os.path.join(OUT, "style.css"))
    files = os.path.join(ROOT, "site", "files")
    if os.path.isdir(files):
        shutil.copytree(files, os.path.join(OUT, "files"))
    open(os.path.join(OUT, ".nojekyll"), "w").close()
    print(f"built {len(experiments) + len(spec_map) + len(guides) + 4} pages into docs/, indexing {n_types} record types, "
          f"{n_topics} topics, {n_search} search entries and {len(FEATURES)} features")
    for here, message in PROBLEMS:
        print(f"markdown: {here}: {message}", file=sys.stderr)
    problems = check_links(OUT)
    for p in problems:
        print("broken:", p, file=sys.stderr)
    if problems or PROBLEMS:
        sys.exit(f"{len(PROBLEMS)} Markdown problems and {len(problems)} broken links or fragments; "
                 "fix the Markdown they come from")


def build_revision():
    """The commit the site is built on, and whether anything outside docs/ differs from it; None outside git."""
    try:
        rev = subprocess.run(["git", "-C", ROOT, "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
        dirty = subprocess.run(["git", "-C", ROOT, "status", "--porcelain", "--", ".", ":!docs"],
                               capture_output=True, text=True, check=True).stdout.strip()
        return rev, bool(dirty)
    except (OSError, subprocess.CalledProcessError):
        return None


def check_links(out):
    """Every local link and image in the built site must reach a file, and every #fragment an id on that page.
    Also reports ids used twice on one page. Returns a list of problems."""
    ids, links, problems = {}, [], []
    for d, _, fs in os.walk(out):
        for f in fs:
            if not f.endswith(".html"):
                continue
            p = os.path.join(d, f)
            with open(p, encoding="utf-8") as fh:
                text = fh.read()
            found = re.findall(r'\sid="([^"]+)"', text)
            seen = set()
            for i in found:
                if i in seen:
                    problems.append(f"{os.path.relpath(p, out)}: id {i} used twice")
                seen.add(i)
            ids[os.path.normpath(p)] = seen
            links += [(p, html.unescape(h)) for h in re.findall(r'(?:href|src)="([^"]+)"', text)]
    for p, h in links:
        if re.match(r"^(?:[a-z]+:|#$)", h):
            continue
        path, _, frag = h.partition("#")
        target = os.path.normpath(os.path.join(os.path.dirname(p), path)) if path else os.path.normpath(p)
        if not os.path.exists(target):
            problems.append(f"{os.path.relpath(p, out)}: {h} (no such file)")
        elif frag and target.endswith(".html") and frag not in ids.get(target, ()):
            problems.append(f"{os.path.relpath(p, out)}: {h} (no such section)")
    return problems


if __name__ == "__main__":
    main()
