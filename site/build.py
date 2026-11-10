"""Build the specification site into docs/ as static HTML and CSS, with no JavaScript.

Usage: python3 -I site/build.py

Sources:
  spec/*.md            the specification for the current app release, one page per layer
  spec/versions/*/     the specification as frozen for earlier releases (site/archive.py)
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

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs")
REPO = "https://github.com/alehel/iwork-format"
TITLE = "iWork file format specification"

# The specification is versioned by the release of the apps it describes. spec/ holds the current
# release and is published at spec/. When a new release is taken up, site/archive.py freezes a copy
# of spec/ in spec/versions/<release>/, published at spec/<release>/, and CURRENT_VERSION moves on.
# Experiments and guides aren't versioned: each experiment records the release it ran on.
CURRENT_VERSION = "15.4"
SPEC_PAGES = [("README.md", "index.html"), ("container.md", "container.html"), ("text.md", "text.html"),
              ("keynote.md", "keynote.html"), ("numbers.md", "numbers.html")]


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
    if target.startswith("site/files/"):
        return relpath("files/" + target[len("site/files/"):], here_out(here)) + anchor
    if target.endswith(".md"):
        page = SITE_PAGES.get(target)
        if page:
            return relpath(page, here_out(here)) + anchor
    return f"{REPO}/blob/main/{target}{anchor}"


def inline(text, here):
    out = []
    parts = re.split(r"(`[^`]+`)", text)
    for part in parts:
        if part.startswith("`") and part.endswith("`") and len(part) > 1:
            out.append("<code>" + html.escape(part[1:-1]) + "</code>")
            continue
        s = html.escape(part, quote=False)
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

    def flush():
        if para:
            out.append("<p>" + inline(" ".join(para), here) + "</p>")
            para.clear()

    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            flush()
            lang = line[3:].strip()
            body = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                body.append(lines[i])
                i += 1
            cls = f' class="lang-{lang}"' if lang else ""
            out.append(f"<pre{cls}><code>" + html.escape("\n".join(body)) + "</code></pre>")
            i += 1
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            flush()
            level = len(m.group(1))
            text = inline(m.group(2), here)
            anchor = slug(m.group(2))
            if toc is not None and level == 2:
                toc.append((anchor, re.sub(r"<[^>]+>", "", text)))
            out.append(f'<h{level} id="{anchor}">{text}<a class="anchor" href="#{anchor}" aria-label="Link to this section">#</a></h{level}>')
            i += 1
            continue
        m = re.match(r"^<!--\s*include:\s*(\S+)\s*-->$", line.strip())
        if m:
            flush()
            out.append(include_excerpt(m.group(1)))
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
            while i < len(lines) and (re.match(r"^\s*([-*]|\d+\.)\s+", lines[i]) or (lines[i].startswith("   ") and lines[i].strip())):
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
    for line in block:
        indent = len(line) - len(line.lstrip())
        m = re.match(r"^\s*([-*]|\d+\.)\s+(.*)$", line)
        if m and indent == base:
            items.append([m.group(2)])
        elif items:
            items[-1].append(line[base + 2:] if len(line) > base + 2 else line.strip())
    tag = "ol" if ordered else "ul"
    out = [f"<{tag}>"]
    for item in items:
        head, rest = item[0], item[1:]
        if rest:
            inner = render("\n".join([head] + [r if not r.startswith(" ") else r for r in rest]), here)
            inner = re.sub(r"^<p>(.*?)</p>", r"\1", inner, count=1, flags=re.S)
            out.append(f"<li>{inner}</li>")
        else:
            out.append(f"<li>{inline(head, here)}</li>")
    out.append(f"</{tag}>")
    return "".join(out)


def include_excerpt(name):
    path = os.path.join(ROOT, "site", "examples", name)
    with open(path, encoding="utf-8") as f:
        text = f.read().rstrip("\n")
    return f'<pre class="excerpt"><code>{html.escape(text)}</code></pre>'


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
    ("2–5. Text, styles, objects, layout", "spec:text.html"),
    ("Keynote", "spec:keynote.html"),
    ("Numbers", "spec:numbers.html"),
    ("Evidence", None),
    ("All experiments", "experiments/index.html"),
]


VERSIONS = []      # filled by main(): (release, source folder, output folder), newest first
VERSION_PAGES = {}  # output folder -> the page names that version has


def version_switch(out_path, view, name):
    """A dropdown of each release's spec: to the same page where that release has it, else its overview."""
    links = []
    shown = ""
    for release, _, folder in VERSIONS:
        target = f"{folder}/{name}" if name in VERSION_PAGES[folder] else f"{folder}/index.html"
        label = html.escape(release + (" (current)" if release == CURRENT_VERSION else ""))
        if folder == view:
            shown = label
            links.append(f'<li><a class="current" aria-current="page" href="{relpath(target, out_path)}">{label}</a></li>')
        else:
            links.append(f'<li><a href="{relpath(target, out_path)}">{label}</a></li>')
    return ('<li class="versions"><details class="release"><summary><span class="label">App release</span>'
            f'<span class="value">{shown}</span></summary><ul>' + "".join(links) + "</ul></details></li>")


def page(out_path, title, body, toc=None, description="", version=None):
    """version is the output folder of the spec release this page belongs to, or None outside the spec."""
    view = version or "spec"
    name = out_path[len(view) + 1:] if version else "index.html"
    nav = []
    for label, href in NAV:
        if href is None:
            nav.append(f'<li class="group">{html.escape(label)}</li>')
            if label == "Specification":
                nav.append(version_switch(out_path, view, name))
            continue
        if href.startswith("spec:"):
            href = f"{view}/{href[5:]}"
        cls = ' class="current"' if href == out_path else ""
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
<header class="top"><a class="brand" href="{home}">iWork format</a><span class="sub">A clean-room specification of Pages, Keynote and Numbers files</span><a class="repo" href="{REPO}">Repository</a></header>
<p class="wip"><strong>Work in progress.</strong> This specification is incomplete and changes as new experiments run. Each finding says how sure it is: <em>confirmed</em>, <em>likely</em> or <em>unknown</em>. See <a href="{relpath("spec/index.html", out_path)}">what each layer covers so far</a>.</p>{archived}
<div class="layout">
<nav class="side" aria-label="Contents"><details open><summary>Contents</summary><ul>{''.join(nav)}</ul></details></nav>
<main>
{body}
<footer><p>Built from the repository's Markdown. Every finding links to the experiment behind it. Last built from <a href="{REPO}">alehel/iwork-format</a>.</p></footer>
</main>
{toc_html}
</div>
<script>
// On narrow screens the contents and on-this-page lists start folded; on wide ones they stay open.
(function () {{
  var narrow = window.matchMedia("(max-width: 48rem)");
  var lists = document.querySelectorAll(".side > details, .toc > details");
  function fit() {{ for (var i = 0; i < lists.length; i++) lists[i].open = !narrow.matches; }}
  fit();
  if (narrow.addEventListener) narrow.addEventListener("change", fit);
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
    if (narrow.matches && e.target.closest && e.target.closest(".toc a")) fit();
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

    VERSIONS[:] = spec_versions()
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
    guides = sorted(f for f in os.listdir(os.path.join(ROOT, "site", "guides")) if f.endswith(".md"))
    for f in guides:
        SITE_PAGES[f"site/guides/{f}"] = f"guides/{f[:-3]}.html"

    # Overview: the guide's own front page.
    md = read("site/guides/index.md")
    SITE_PAGES["site/guides/index.md"] = "index.html"
    toc = []
    page("index.html", "Overview", render(md, "site/guides/index.md", toc), toc)

    for src, (out, version) in spec_map.items():
        md = read(src)
        toc = []
        body = render(md, src, toc)
        page(out, title_of(md), body, toc, version=version)

    for f in guides:
        if f == "index.md":
            continue
        src = f"site/guides/{f}"
        md = read(src)
        toc = []
        page(f"guides/{f[:-3]}.html", title_of(md), render(md, src, toc), toc)

    rows = []
    for f in experiments:
        md = read(f"experiments/{f}")
        title = title_of(md)
        src = f"experiments/{f}"
        page(f"experiments/{f[:-3]}.html", title, render(md, src), None)
        num, _, name = title.partition(": ")
        rows.append(f'<tr><td class="num">{html.escape(num)}</td><td><a href="{f[:-3]}.html">{html.escape(name or title)}</a></td></tr>')
    body = ("<h1>All experiments</h1><p>Each experiment changes one thing in a document, saves it, and "
            "records what changed in the file. The specification cites them as its evidence. "
            f"{len(experiments)} have been run.</p><div class=\"table\"><table><thead><tr><th>No.</th><th>Experiment</th></tr></thead><tbody>"
            + "".join(rows) + "</tbody></table></div>")
    page("experiments/index.html", "All experiments", body)

    shutil.copy(os.path.join(ROOT, "site", "style.css"), os.path.join(OUT, "style.css"))
    files = os.path.join(ROOT, "site", "files")
    if os.path.isdir(files):
        shutil.copytree(files, os.path.join(OUT, "files"))
    open(os.path.join(OUT, ".nojekyll"), "w").close()
    print(f"built {len(experiments) + len(spec_map) + len(guides) + 1} pages into docs/")


if __name__ == "__main__":
    main()
