"""Build the specification site into docs/ as static HTML and CSS, with no JavaScript.

Usage: python3 -I site/build.py

Sources:
  spec/*.md            the specification for the current app release, one page per layer
  spec/versions/*/     the specification as frozen for earlier releases (site/archive.py)

A statement in the spec that holds for some releases only carries a release mark, `[release: TEXT]`,
such as `[release: 15.4 only]`. It is drawn as a badge, and spec/releases.md gathers every marked
statement where it says `<!-- release-differences -->`.
  experiments/*.md     every experiment, one page each
  site/guides/*.md     walkthroughs written for the site, which may embed generated excerpts
  site/examples/*.txt  excerpts of iwork-probe output, made by site/examples.py from local samples
  site/files/          sample documents published for download, and renders of them

Only the Python standard library is used. Markdown is converted by the small converter below,
which handles the subset the repository's writing uses.
"""
import html
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs")
REPO = "https://github.com/alehel/iwork-format"
TITLE = "iWork file format specification"

# The specification is versioned by the release of the apps it describes. spec/ holds the current
# release and is published at spec/. When a new release is taken up, site/archive.py freezes a copy
# of spec/ in spec/versions/<release>/, published at spec/<release>/, and CURRENT_VERSION moves on.
# That is for a release that changes the format. Releases that write the same format share one spec,
# whose release marks note what differs (spec/releases.md). Experiments and guides aren't versioned:
# each experiment records the release it ran on, which the experiment list shows.
CURRENT_VERSION = "15.4"
SPEC_PAGES = [("README.md", "index.html"), ("container.md", "container.html"), ("text.md", "text.html"),
              ("styles.md", "styles.html"), ("tables.md", "tables.html"), ("drawables.md", "drawables.html"),
              ("pages.md", "pages.html"), ("keynote.md", "keynote.html"), ("numbers.md", "numbers.html"),
              ("releases.md", "releases.html")]
GENERATED = {"spec/types.html"}  # pages the build makes without a Markdown source, which Markdown may link to
RELEASE_MARK = re.compile(r"\[release: ([^\]]+)\]")


def version_key(name):
    return tuple(int(p) if p.isdigit() else -1 for p in name.split("."))


def spec_versions():
    """Every version of the spec, newest first, as (release, source folder, output folder)."""
    found = [("CURRENT", "spec", "spec")]
    archive = os.path.join(ROOT, "spec", "versions")
    if os.path.isdir(archive):
        for name in sorted(os.listdir(archive), key=version_key, reverse=True):
            if os.path.isdir(os.path.join(archive, name)) and name != CURRENT_VERSION:
                found.append((name, f"spec/versions/{name}", f"spec/{name}"))
    found[0] = (CURRENT_VERSION,) + found[0][1:]
    return found


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


def inline(text, here):
    out = []
    parts = re.split(r"(`[^`]+`)", text)
    for part in parts:
        if part.startswith("`") and part.endswith("`") and len(part) > 1:
            out.append("<code>" + html.escape(part[1:-1]) + "</code>")
            continue
        s = html.escape(part, quote=False)
        s = RELEASE_MARK.sub(lambda m: f'<span class="release" title="Holds for some releases only">{m.group(1)}</span>', s)
        s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", lambda m: f'<a href="{html.escape(link_target(html.unescape(m.group(2)), here))}">{m.group(1)}</a>', s)
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<![\w*])\*([^*\s][^*]*?)\*(?![\w*])", r"<em>\1</em>", s)
        out.append(s)
    return "".join(out)


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
        if line.strip() == "<!-- release-differences -->":
            flush()
            out.append(release_differences(here))
            i += 1
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
            out.append(f'<figure><img src="{html.escape(src)}" alt="{html.escape(m.group(1))}" loading="lazy"><figcaption>{inline(m.group(1), here)}</figcaption></figure>')
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
            t = ["<div class=\"table\"><table><thead><tr>"]
            t += [f"<th>{inline(c, here)}</th>" for c in header]
            t.append("</tr></thead><tbody>")
            for r in rows:
                t.append("<tr>" + "".join(f"<td>{inline(c, here)}</td>" for c in r) + "</tr>")
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



RELEASE_NOTES = []  # (mark, statement Markdown, source page, section anchor, section title), filled by main()


def statement_after(text, start):
    """The sentence a release mark begins, up to its full stop (links and code kept whole)."""
    rest = text[start:]
    depth, i = 0, 0
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
            for mark in RELEASE_MARK.finditer(line):
                notes.append((mark.group(1), statement_after(line, mark.end()), src, anchor, section))
    return notes


def release_differences(here):
    if not RELEASE_NOTES:
        return "<p>No statement in the specification is marked as holding for some releases only.</p>"
    rows = []
    for mark, statement, src, anchor, section in sorted(RELEASE_NOTES, key=lambda n: (n[0], n[2])):
        where = relpath(SITE_PAGES[src] + (f"#{anchor}" if anchor else ""), here_out(here))
        page_name = title_of(read(src))
        rows.append(f'<tr><td><span class="release">{html.escape(mark)}</span></td><td>{inline(statement, src)}'
                    f'<span class="where">In <a href="{html.escape(where)}">{html.escape(page_name)}'
                    f'{": " + inline(section, src) if section else ""}</a></span></td></tr>')
    return ('<div class="table"><table class="differences"><thead><tr><th>Release</th><th>Statement</th></tr></thead><tbody>'
            + "".join(rows) + "</tbody></table></div>")


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
            "numbers.md": "Numbers"}


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
    ("Layers and status", "spec:index.html"),
    ("1. Container", "spec:container.html"),
    ("2. Text", "spec:text.html"),
    ("3. Styles", "spec:styles.html"),
    ("4. Tables", "spec:tables.html"),
    ("5. Drawables, media and charts", "spec:drawables.html"),
    ("Apps", None),
    ("Pages", "spec:pages.html"),
    ("Keynote", "spec:keynote.html"),
    ("Numbers", "spec:numbers.html"),
    ("Reference", None),
    ("Record types", "spec/types.html"),
    ("Releases", "spec:releases.html"),
    ("Evidence", None),
    ("All experiments", "experiments/index.html"),
]


VERSIONS = []      # filled by main(): (release, source folder, output folder), newest first
BUILD_REVISION = None  # filled by main(): (commit the build was made on, whether sources had uncommitted changes)
OTHER_RELEASES = []  # filled by main(): releases other than CURRENT_VERSION that experiments ran with
VERSION_PAGES = {}  # output folder -> the page names that version has


def version_switch(out_path, view, name):
    """A dropdown of each release's spec: to the same page where that release has it, else its overview."""
    links = []
    shown = ""
    for release, _, folder in VERSIONS:
        target = f"{folder}/{name}" if name in VERSION_PAGES[folder] else f"{folder}/index.html"
        label = html.escape(f"Format of {release}" + (" (current)" if release == CURRENT_VERSION else ""))
        if folder == view:
            shown = label
            links.append(f'<li><a class="current" aria-current="page" href="{relpath(target, out_path)}">{label}</a></li>')
        else:
            links.append(f'<li><a href="{relpath(target, out_path)}">{label}</a></li>')
    return ('<li class="versions"><details class="release"><summary><span class="label">Spec version</span>'
            f'<span class="value">{shown}</span></summary><ul>' + "".join(links) + "</ul></details></li>")


def releases_line(out_path, view):
    """What the spec describes and which other releases were checked, linking to the releases page."""
    shown = next((r for r, _, f in VERSIONS if f == view), CURRENT_VERSION)
    text = f"Describes {shown}"
    if view == "spec" and OTHER_RELEASES:
        text += " · also checked: " + ", ".join(OTHER_RELEASES)
    target = f"{view}/releases.html" if "releases.html" in VERSION_PAGES.get(view, ()) else "spec/releases.html"
    return f'<li class="releases-line"><a href="{relpath(target, out_path)}">{html.escape(text)}</a></li>'


def page(out_path, title, body, toc=None, description="", version=None, source=None, wide=False):
    """version is the output folder of the spec release this page belongs to, or None outside the spec.
    source is the repository path of the Markdown the page is built from, linked in the footer.
    wide lets a page without an on-this-page list use that column too, for wide tables."""
    view = version or "spec"
    name = out_path[len(view) + 1:] if version else "index.html"
    nav = []
    for label, href in NAV:
        if href is None:
            nav.append(f'<li class="group">{html.escape(label)}</li>')
            if label == "Specification":
                # The picker only appears once a copy of the spec has been frozen for an earlier format.
                if len(VERSIONS) > 1:
                    nav.append(version_switch(out_path, view, name))
                nav.append(releases_line(out_path, view))
            continue
        if href.startswith("spec:"):
            href = f"{view}/{href[5:]}"
        cls = ' class="current" aria-current="page"' if href == out_path else ""
        nav.append(f'<li><a{cls} href="{relpath(href, out_path)}">{html.escape(label)}</a></li>')
    archived = ""
    if version and version != "spec":
        release = next(r for r, _, f in VERSIONS if f == version)
        current = f"spec/{name}" if name in VERSION_PAGES["spec"] else "spec/index.html"
        archived = (f'\n<p class="wip archived"><strong>Earlier release.</strong> This is the specification as it stood for '
                    f'the {html.escape(release)} apps, kept for documents they wrote. The current one describes '
                    f'{html.escape(CURRENT_VERSION)}: <a href="{relpath(current, out_path)}">read this page there</a>.</p>')
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
<header class="top"><a class="brand" href="{home}">iWork format</a><span class="sub">A clean-room specification of Pages, Keynote and Numbers files</span><a class="repo" href="{REPO}">Repository</a></header>
<p class="wip"><strong>Work in progress.</strong> This specification is incomplete and changes as new experiments run. Each finding says how sure it is: <em>confirmed</em>, <em>likely</em> or <em>unknown</em>. See <a href="{relpath("spec/index.html", out_path)}">what each chapter covers so far</a>.</p>{archived}
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
  function fit() {{
    if (side) side.open = !narrow.matches;
    if (toc) toc.open = !middle.matches;
  }}
  fit();
  if (narrow.addEventListener) {{ narrow.addEventListener("change", fit); middle.addEventListener("change", fit); }}
  // The release dropdown closes when you click anywhere else.
  document.addEventListener("click", function (e) {{
    var release = document.querySelector(".side .release[open]");
    if (release && !release.contains(e.target)) release.open = false;
  }});
  document.addEventListener("keydown", function (e) {{
    var release = document.querySelector(".side .release[open]");
    if (release && e.key === "Escape") {{ release.open = false; release.querySelector("summary").focus(); }}
  }});
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
    VERSIONS[:] = spec_versions()
    found = set()
    for f in os.listdir(os.path.join(ROOT, "experiments")):
        if re.match(r"^\d{4}-.*\.md$", f):
            found.update(experiment_releases(read(f"experiments/{f}")))
    OTHER_RELEASES[:] = sorted(found - {CURRENT_VERSION}, key=version_key, reverse=True)
    spec_map = {}  # source -> (output, version folder)
    for _, src_dir, out_dir in VERSIONS:
        VERSION_PAGES[out_dir] = set()
        for src, out in SPEC_PAGES:
            if os.path.isfile(os.path.join(ROOT, src_dir, src)):
                spec_map[f"{src_dir}/{src}"] = (f"{out_dir}/{out}", out_dir)
                VERSION_PAGES[out_dir].add(out)
    SITE_PAGES.update({src: out for src, (out, _) in spec_map.items()})
    SITE_PAGES["README.md"] = "index.html"
    experiments = sorted(f for f in os.listdir(os.path.join(ROOT, "experiments")) if re.match(r"^\d{4}-.*\.md$", f))
    for f in experiments:
        SITE_PAGES[f"experiments/{f}"] = f"experiments/{f[:-3]}.html"
    RELEASE_NOTES[:] = collect_release_notes([src for src, (_, version) in spec_map.items()
                                                if version == "spec" and not src.endswith("releases.md")])
    guides = sorted(f for f in os.listdir(os.path.join(ROOT, "site", "guides")) if f.endswith(".md"))
    for f in guides:
        SITE_PAGES[f"site/guides/{f}"] = f"guides/{f[:-3]}.html"

    # Overview: the guide's own front page.
    md = read("site/guides/index.md")
    SITE_PAGES["site/guides/index.md"] = "index.html"
    toc = []
    page("index.html", "Overview", render(md, "site/guides/index.md", toc), toc, source="site/guides/index.md")

    for src, (out, version) in spec_map.items():
        md = read(src)
        toc = []
        body = render(md, src, toc)
        page(out, title_of(md), body, toc, version=version, source=src)

    for f in guides:
        if f == "index.md":
            continue
        src = f"site/guides/{f}"
        md = read(src)
        toc = []
        page(f"guides/{f[:-3]}.html", title_of(md), render(md, src, toc), toc, source=src)

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
        num, _, name = title.partition(": ")
        rel = ", ".join(releases) or "tool only"
        rows.append(f'<tr><td class="num">{html.escape(num)}</td><td><a href="{f[:-3]}.html">{html.escape(name or title)}</a></td>'
                    f'<td class="rel">{html.escape(rel)}</td></tr>')
    counts = {}
    for f in experiments:
        for r in experiment_releases(read(f"experiments/{f}")):
            counts[r] = counts.get(r, 0) + 1
    by_release = " and ".join(f"{n} with the {r} apps" for r, n in sorted(counts.items(), key=lambda x: version_key(x[0]), reverse=True))
    tool_only = sum(1 for f in experiments if not experiment_releases(read(f"experiments/{f}")))
    body = ("<h1>All experiments</h1><p>Each experiment changes one thing in a document, saves it, and "
            "records what changed in the file. The specification cites them as its evidence. "
            f"{len(experiments)} have been run: {by_release}, as each one's setup records"
            + (f", and {tool_only} with the tool alone. " if tool_only else ". ") +
            f'The <a href="../spec/releases.html">releases</a> page says how the releases differ.</p>'
            "<div class=\"table\"><table><thead><tr><th>No.</th><th>Experiment</th><th>App release</th></tr></thead><tbody>"
            + "".join(rows) + "</tbody></table></div>")
    page("experiments/index.html", "All experiments", body)
    n_types = types_page([src for src, _ in SPEC_PAGES if src != "releases.md"], experiments)

    shutil.copy(os.path.join(ROOT, "site", "style.css"), os.path.join(OUT, "style.css"))
    files = os.path.join(ROOT, "site", "files")
    if os.path.isdir(files):
        shutil.copytree(files, os.path.join(OUT, "files"))
    open(os.path.join(OUT, ".nojekyll"), "w").close()
    print(f"built {len(experiments) + len(spec_map) + len(guides) + 2} pages into docs/, indexing {n_types} record types")
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
