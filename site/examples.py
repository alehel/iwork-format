"""Make the excerpts, renders and downloadable samples the site's guides use.

Usage: python3 -I site/examples.py

Needs the local samples/ folder (gitignored) and target/release/iwork-probe. Writes:
  site/examples/*.txt   iwork-probe output, trimmed, embedded by the guides
  site/files/           published samples, chosen because they hold only text we typed, no images
                        from Apple's themes, and no personal details; plus PNG renders of them
Renders are made by exporting each document to PDF with its app, then converting the first page
with sips. Run it on a Mac with Pages and Numbers.
"""
import os
import re
import shutil
import subprocess
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROBE = os.path.join(ROOT, "target", "release", "iwork-probe")
EX = os.path.join(ROOT, "site", "examples")
FILES = os.path.join(ROOT, "site", "files")

# Published samples: (sample path, published name, app for rendering, experiment)
# The render is cropped to (height, width, top) pixels of the page scaled to 1100 pixels.
PAGE = (130, 778, 30)
PAGE_TABLE = (260, 778, 30)
SHEET = (330, 1100, 80)
SAMPLES = [
    ("samples/0002/hello.pages", "hello.pages", "Pages", PAGE),
    ("samples/0005/two-lf.pages", "two-paragraphs.pages", "Pages", PAGE),
    ("samples/0020/table.pages", "table.pages", "Pages", PAGE_TABLE),
    ("samples/0226/plain.numbers", "kinds-and-numbers.numbers", "Numbers", SHEET),
    ("samples/0288/hello.pages", "written-by-script.pages", "Pages", PAGE),
    ("samples/0290/forty-two.numbers", "written-cell.numbers", "Numbers", SHEET),
]
def forbidden():
    """Words that must not appear in a published file, in any part, decoded: the names this
    machine knows its user by (login, full name, git user and email), and any listed one per line
    in samples/private-words.txt, which is gitignored with the rest of samples/."""
    words = {os.environ.get("USER", "")}
    for cmd in (["id", "-F"], ["git", "config", "user.name"], ["git", "config", "user.email"]):
        out = subprocess.run(cmd, capture_output=True, text=True).stdout.strip()
        words.add(out)
        words.update(out.replace("@", " ").replace(".", " ").split())
    extra = os.path.join(ROOT, "samples", "private-words.txt")
    if os.path.exists(extra):
        words.update(open(extra, encoding="utf-8").read().split())
    return [w.lower().encode() for w in words if len(w) >= 4 and w.lower() not in ("com", "mail")]


def probe(*args):
    return subprocess.run([PROBE, *args], capture_output=True, text=True, check=True).stdout


def save(name, text):
    with open(os.path.join(EX, name), "w", encoding="utf-8") as f:
        f.write(text.rstrip("\n") + "\n")


def lines(text, start, end):
    return "\n".join(text.splitlines()[start:end])


def record_bounds(doc, part, object_id):
    for line in probe("records", doc, part).splitlines()[2:]:
        c = line.split()
        if c[4] == str(object_id):
            return int(c[2]), int(c[3]), int(c[0]), int(c[1])
    raise KeyError(object_id)


def decoded_iwa(stored):
    return writer().iwa_decode(stored)


def writer():
    import importlib.util
    spec = importlib.util.spec_from_file_location("w", os.path.join(ROOT, "recipes", "0287-iwa-writer.py"))
    w = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(w)
    return w


def rows(doc):
    """Each row's offsets and cell bytes, split into cells."""
    w = writer()
    with zipfile.ZipFile(doc) as z:
        recs = w.records(w.iwa_decode(z.read("Index/Tables/Tile.iwa")))
    out = []
    for f, _, v in w.parse_message(recs[0][1][0]):
        if f != 5:
            continue
        d = {ff: vv for ff, _, vv in w.parse_message(v)}
        row = w.read_varint(d[1], 0)[0]
        offs = d.get(7) or d.get(4)
        starts = [o for o in (int.from_bytes(offs[i:i + 2], "little") for i in range(0, len(offs), 2)) if o != 0xFFFF]
        cells = d[6]
        out.append(f"row {row}: offsets {', '.join(map(str, starts))}, then ffff")
        for col, start in enumerate(starts):
            end = starts[col + 1] if col + 1 < len(starts) else len(cells)
            out.append(f"  column {col}: {cells[start:end].hex(' ')}")
    return "\n".join(out)


def check_private(path):
    with zipfile.ZipFile(path) as z:
        for n in z.namelist():
            data = z.read(n)
            if n.endswith(".iwa"):
                data = decoded_iwa(data)
            low = data.lower()
            for word in forbidden():
                if word in low or word.decode().encode("utf-16-le") in low or word.decode().encode("utf-16-be") in low:
                    raise SystemExit(f"{path}: {n} holds personal data; not publishing")
            if n.startswith("Data/"):
                raise SystemExit(f"{path}: holds a data file ({n}); not publishing")


def render(path, app, png, crop):
    pdf = png[:-4] + ".pdf"
    script = f'''with timeout of 120 seconds
tell application "{app}"
set d to open POSIX file "{os.path.abspath(path)}"
export d to POSIX file "{pdf}" as PDF
close d saving no
end tell
end timeout'''
    subprocess.run(["osascript", "-e", script], check=True, capture_output=True)
    subprocess.run(["sips", "-s", "format", "png", "-Z", "1100", pdf, "--out", png], check=True, capture_output=True)
    height, width, top = crop
    subprocess.run(["sips", "-c", str(height), str(width), "--cropOffset", str(top), "0", png], check=True, capture_output=True)
    os.remove(pdf)


def main():
    os.makedirs(EX, exist_ok=True)
    if os.path.isdir(FILES):
        shutil.rmtree(FILES)
    os.makedirs(FILES)

    # --- Reading a Pages document (samples/0002/hello.pages) ---
    os.chdir(ROOT)
    doc = "samples/0002/hello.pages"
    save("hello-list.txt", probe("list", doc).replace("samples/0002/hello.pages", "hello.pages"))
    save("hello-chunks.txt", probe("chunks", doc, "Index/Document.iwa"))
    save("hello-stored-hex.txt", probe("hex", doc, "Index/Document.iwa", "--len", "48"))
    save("hello-records.txt", lines(probe("records", doc, "Index/Document.iwa"), 0, 8) + "\n   …")
    off, length, hoff, hlen = record_bounds(doc, "Index/Document.iwa", 1)
    save("hello-header-hex.txt", probe("hex", doc, "Index/Document.iwa", "--decoded", "--offset", str(hoff - 1), "--len", "32"))
    save("hello-header-proto.txt", probe("proto", doc, "Index/Document.iwa", "--decoded", "--offset", str(hoff), "--len", str(hlen)))
    root = probe("proto", doc, "Index/Document.iwa", "--decoded", "--offset", str(off), "--len", str(length), "--depth", "1")
    save("hello-root.txt", "\n".join(root.splitlines()[:12]) + "\n…\n" + "\n".join(l for l in root.splitlines() if re.match(r"^(30|31|32|33|34|35):", l)))
    off, length, hoff, hlen = record_bounds(doc, "Index/Document.iwa", 1732539)
    body = probe("proto", doc, "Index/Document.iwa", "--decoded", "--offset", str(off), "--len", str(length), "--depth", "4")
    save("hello-body.txt", "\n".join(body.splitlines()[:16]) + "\n…")
    save("hello-body-hex.txt", probe("hex", doc, "Index/Document.iwa", "--decoded", "--offset", str(off), "--len", "16"))
    save("hello-text.txt", probe("text", doc))
    style = probe("records", doc, "Index/DocumentStylesheet.iwa")
    for line in style.splitlines()[2:]:
        c = line.split()
        if c[4] == "1731511":
            text = probe("proto", doc, "Index/DocumentStylesheet.iwa", "--decoded", "--offset", c[2], "--len", c[3], "--depth", "3")
            save("hello-body-style.txt", "\n".join(text.splitlines()[:8]) + "\n…")
            break

    # --- Reading a Numbers table (samples/0226/plain.numbers) ---
    doc = "samples/0226/plain.numbers"
    off, length, _, _ = [(int(c[2]), int(c[3]), 0, 0) for c in (l.split() for l in probe("records", doc, "Index/CalculationEngine.iwa").splitlines()[2:]) if c[5] == "6001"][0]
    model = probe("proto", doc, "Index/CalculationEngine.iwa", "--decoded", "--offset", str(off), "--len", str(length), "--depth", "1")
    save("numbers-model.txt", "\n".join(l for l in model.splitlines() if re.match(r"^(1|6|7|8|9|10|12|13|22):", l)))
    tile = probe("records", doc, "Index/Tables/Tile.iwa").splitlines()[2].split()
    tree = probe("proto", doc, "Index/Tables/Tile.iwa", "--decoded", "--offset", tile[2], "--len", tile[3], "--depth", "2")
    save("numbers-tile.txt", "\n".join(tree.splitlines()[:14]) + "\n…")
    save("numbers-rows.txt", rows(doc))
    storage = probe("proto", doc, "Index/CalculationEngine.iwa", "--decoded", "--offset", str(off), "--len", str(length), "--depth", "3")
    keep, inside = [], False
    for l in storage.splitlines():
        if l.startswith("4:"):
            inside = True
        elif not l.startswith(" "):
            inside = False
        if inside and (l.startswith("4:") or re.match(r"^  ([1-4]|22): ", l) or l.startswith("    ") and len(keep) < 14):
            keep.append(l)
    save("numbers-storage.txt", "\n".join(keep[:14]) + "\n  …")
    for part, name in (("DataList-904552", "numbers-strings.txt"), ("DataList-904541", "numbers-formats.txt")):
        full = f"Index/Tables/{part}.iwa"
        c = probe("records", doc, full).splitlines()[2].split()
        save(name, probe("proto", doc, full, "--decoded", "--offset", c[2], "--len", c[3], "--depth", "3"))
    save("numbers-tile-hex.txt", probe("hex", doc, "Index/Tables/Tile.iwa", "--decoded", "--len", "160"))

    # --- Published samples and renders ---
    for src, name, app, crop in SAMPLES:
        check_private(src)
        shutil.copy(src, os.path.join(FILES, name))
        render(src, app, os.path.join(FILES, name.rsplit(".", 1)[0] + ".png"), crop)
    print("examples and files written")


if __name__ == "__main__":
    main()
