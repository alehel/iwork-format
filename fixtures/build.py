"""Collect the experiments' sample documents that can be published, check them, and pack them.

Usage: python3 -I fixtures/build.py OUT_DIR

Reads the local samples/ folder (gitignored), writes fixtures/INDEX.md (committed) and, in OUT_DIR,
one zip per app release, iwork-format-fixtures-RELEASE.zip, holding the documents that release saved
(published as GitHub release assets; one zip per release keeps each well under the size limit for an
asset). A document is published only if:
  - it isn't from an experiment on Apple's templates (0090, 0155-0158, 0198, 0199);
  - a Keynote presentation comes from samples/theme/ or samples/release/, made with the project's
    test theme (experiments 0291, 0292, 0473), never from Basic White;
  - every file under Data/ is one the project made: the test cards, Keynote's thumbnails of
    them, or the project's own images, sound and movie;
  - no part, decoded or decrypted, holds a name this Mac knows its user by (site/examples.py).
Folder packages and documents that fail a check are listed as left out, with the reason.
"""
import hashlib
import importlib.util
import os
import plistlib
import re
import subprocess
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROBE = os.path.join(ROOT, "target", "release", "iwork-probe")


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


examples = load("examples", "site/examples.py")
writer = load("writer", "recipes/0287-iwa-writer.py")

# Experiments whose documents carry Apple's own theme images (0090) or placeholder prose (0158,
# 0199). The other template experiments' documents hold only a template's styles and layout.
TEMPLATES = {"0090", "0158", "0199"}
SKIP = {"samples/0198/image-slides.key": "a dead end, not part of an experiment's result"}
OURS = re.compile(
    r"^(photo-[a-f](-small)?|background|alpha|small|red-8x4(-filtered)?|rød bilde|gradient-3000x2000(-small)?|"
    r"square|data|tone|clip|posterImage|mt-[0-9A-F-]+|st-[0-9A-F-]+)-\d+\.\w+$")
# Test passwords, from experiments 0179 and 0180.
# Documents whose comments, highlights or tracked changes record the project owner's name as
# their author (record type 212). Published with the owner's agreement; the name is in that
# record only.
AUTHOR_NAMED = {"samples/0193/tracked.pages", "samples/0194/deleted.pages", "samples/0200/highlight.pages",
                "samples/0249/comment.pages", "samples/0268/accepted.pages", "samples/0269/rejected.pages",
                # Copies of those written in experiments 0375-0377 and 0443, also published with the owner's
                # agreement (2026-11-23); the name is still only in the type-212 record.
                "samples/0375/text.pages", "samples/0375/time.pages", "samples/0376/comment-emptied.pages",
                "samples/0376/comment.pages", "samples/0376/highlight-with-text.pages",
                "samples/0376/highlight.pages", "samples/0377/deleted-as-insertion.pages",
                "samples/0377/deleted-blue.pages", "samples/0377/deleted-green.pages",
                "samples/0377/deleted-red.pages", "samples/0377/deleted.pages",
                "samples/0377/inserted-as-deletion.pages", "samples/0377/inserted.pages",
                "samples/0443/c-0-0-0.pages", "samples/0443/c-0-1-1.pages",
                "samples/0443/c-0.36-0.78-0.69.pages", "samples/0443/c-0.5-0-1.pages",
                "samples/0443/c-0.5-0.5-0.5.pages", "samples/0443/c-0.98-0.6-0.21.pages",
                "samples/0443/c-1-0-1.pages", "samples/0443/c-1-0.5-0.pages", "samples/0443/c-1-1-0.pages",
                "samples/0443/c-1-1-1.pages"}
PASSWORDS = {"samples/0179/locked.pages": "pw1234", "samples/0179/locked2.pages": "pw1234",
             "samples/0180/accent.pages": "påss", "samples/0180/image.pages": "pw1234",
             "samples/0180/locked.numbers": "pw1234",
             "samples/theme/0180/locked.key": "pw1234"}


def password(rel):
    """The test password of an encrypted document, also for its copy in a release set (0473)."""
    m = re.match(r"samples/release/[^/]+/(.*)$", rel)
    if m:
        return PASSWORDS.get(f"samples/{m.group(1)}") or PASSWORDS.get(f"samples/theme/{m.group(1)}")
    return PASSWORDS.get(rel)


def saved_by(rel):
    """A note naming the release that last saved a document, when it isn't 15.4, from its build history."""
    try:
        if os.path.isdir(rel):
            data = open(os.path.join(rel, "Metadata", "BuildVersionHistory.plist"), "rb").read()
        else:
            with zipfile.ZipFile(rel) as z:
                data = z.read("Metadata/BuildVersionHistory.plist")
        builds = [b for b in plistlib.loads(data) if isinstance(b, str) and re.match(r"^M\d+\.\d+-", b)]
    except Exception:
        # An encrypted build history can't be read; a release set's documents are that release's.
        m = re.match(r"samples/release/([^/]+)/", rel)
        return f"saved by {m.group(1)}" if m and m.group(1) != "15.4" else ""
    release = builds[-1][1:].split("-")[0] if builds else ""
    return f"saved by {release}" if release and release != "15.4" else ""


def fix_name(info):
    """A ZIP entry's name as UTF-8: Pages writes UTF-8 names without the flag that says so (container.md)."""
    if info.flag_bits & 0x800:
        return info.filename
    try:
        return info.filename.encode("cp437").decode("utf-8")
    except UnicodeError:
        return info.filename


def decrypted_parts(path, password):
    """Each part's plain bytes, through iwork-probe's decryption (experiment 0266)."""
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
    for name in names:
        if name.endswith("/"):
            continue
        out = subprocess.run([PROBE, "hex", path, name, "--password", password, "--len", "999999999"] + (["--decoded"] if name.endswith(".iwa") else []),
                             capture_output=True, text=True)
        if out.returncode:
            yield name, b""
            continue
        data = bytearray()
        for line in out.stdout.splitlines():
            m = re.match(r"^[0-9a-f]{8}  ((?:[0-9a-f]{2} ){1,16})", line + " ")
            if m:
                data += bytes.fromhex(m.group(1).replace(" ", ""))
        yield name, bytes(data)


def plain_parts(path):
    with zipfile.ZipFile(path) as z:
        for name in z.namelist():
            data = z.read(name)
            if name.endswith(".iwa"):
                data = writer.iwa_decode(data)
            yield name, data


def folder_parts(path):
    """A folder package's files, with the parts inside its Index.zip, decoded."""
    for dirpath, _, files in os.walk(path):
        for f in sorted(files):
            full = os.path.join(dirpath, f)
            name = os.path.relpath(full, path)
            if name == "Index.zip":
                with zipfile.ZipFile(full) as z:
                    for inner in z.namelist():
                        data = z.read(inner)
                        yield inner, writer.iwa_decode(data) if inner.endswith(".iwa") else data
            else:
                yield name, open(full, "rb").read()


def folder_files(path):
    return sorted(os.path.relpath(os.path.join(d, f), path) for d, _, fs in os.walk(path) for f in fs)


def problem(path, rel):
    if rel in SKIP:
        return SKIP[rel]
    num = re.search(r"/(\d{4})/", rel).group(1)
    if num in TEMPLATES:
        return "holds Basic Black's photos" if num == "0090" else "holds the template's placeholder text, written by Apple"
    if rel.endswith(".key") and not rel.startswith(("samples/theme/", "samples/release/", "samples/resaved/")):
        if num in ("0291", "0292"):
            return "a step in building or testing the test theme, which is in theme/"
        if os.path.exists(rel.replace("samples/", "samples/theme/")):
            return "Keynote with Basic White's photos; see samples/theme/"
        # Otherwise it may have been made with the test theme from the start: the media check decides.
    words = examples.forbidden()
    if os.path.isdir(path):
        names = folder_files(path)
    else:
        with zipfile.ZipFile(path) as z:
            names = [fix_name(i) for i in z.infolist()]
    foreign = [n[5:] for n in names if n.startswith("Data/") and not OURS.match(n[5:])]
    if foreign:
        return "media not made by the project: " + ", ".join(foreign[:3])
    if rel in AUTHOR_NAMED:
        return None
    pw = password(rel)
    parts = folder_parts(path) if os.path.isdir(path) else decrypted_parts(path, pw) if pw else plain_parts(path)
    for name, data in parts:
        low = data.lower()
        for word in words:
            if word in low or word.decode().encode("utf-16-le") in low or word.decode().encode("utf-16-be") in low:
                return "holds the user's name"
    return None


def zip_name(release):
    return f"iwork-format-fixtures-{release}.zip"


def main(out_dir):
    out_dir = os.path.abspath(out_dir)
    os.makedirs(out_dir, exist_ok=True)
    os.chdir(ROOT)
    candidates = []
    for d in sorted(os.listdir("samples")):
        if re.fullmatch(r"\d{4}", d):
            candidates += [f"samples/{d}/{f}" for f in sorted(os.listdir(f"samples/{d}"))]
    candidates += [f"samples/theme/{d}/{f}" for d in sorted(os.listdir("samples/theme")) for f in sorted(os.listdir(f"samples/theme/{d}"))]
    # Each release's set of every scripted sample, made again with that release (experiment 0473).
    for v in sorted(os.listdir("samples/release")) if os.path.isdir("samples/release") else []:
        for d in sorted(os.listdir(f"samples/release/{v}")):
            candidates += [f"samples/release/{v}/{d}/{f}" for f in sorted(os.listdir(f"samples/release/{v}/{d}"))]
    # Samples a release changed when it saved them again (experiment 0476), beside their originals.
    for v in sorted(os.listdir("samples/resaved")) if os.path.isdir("samples/resaved") else []:
        for d, _, files in sorted(os.walk(f"samples/resaved/{v}")):
            candidates += [f"{d}/{f}" for f in sorted(files)]
    candidates = [c for c in candidates if re.search(r"\.(pages|numbers|key)$", c)]

    kept, left = [], []
    for rel in candidates:
        why = problem(rel, rel)
        (left if why else kept).append((rel, why))

    titles = {}
    for f in os.listdir("experiments"):
        m = re.match(r"^(\d{4})-.*\.md$", f)
        if m:
            first = open(os.path.join("experiments", f), encoding="utf-8").readline()
            titles[m.group(1)] = (f, first.lstrip("# ").strip())

    zips, rows, per_release = {}, [], {}
    try:
        for rel, _ in kept:
            release = (saved_by(rel).removeprefix("saved by ") or "15.4")
            if release not in zips:
                zips[release] = zipfile.ZipFile(os.path.join(out_dir, zip_name(release)), "w", zipfile.ZIP_STORED)
            z = zips[release]
            per_release[release] = per_release.get(release, 0) + 1
            arc = rel.replace("samples/theme/", "keynote/").replace("samples/", "")
            if os.path.isdir(rel):
                h, size = hashlib.sha256(), 0
                for d, subdirs, files in os.walk(rel):
                    if not subdirs and not files:
                        z.writestr(f"{arc}/{os.path.relpath(d, rel)}/", b"")
                for f in folder_files(rel):
                    z.write(os.path.join(rel, f), f"{arc}/{f}")
                    data = open(os.path.join(rel, f), "rb").read()
                    h.update(f.encode() + b"\0" + data)
                    size += len(data)
                digest = h.hexdigest()
            else:
                z.write(rel, arc)
                digest = hashlib.sha256(open(rel, "rb").read()).hexdigest()
                size = os.path.getsize(rel)
            num = arc.split("/")[-2]
            title = titles.get(num, ("", num))[1]
            pw = password(rel)
            notes = [f"password `{pw}`" if pw else "names its author" if rel in AUTHOR_NAMED else "a folder package" if os.path.isdir(rel) else ""]
            m = re.match(r"samples/resaved/[^/]+/(.*)$", rel)
            if m:  # name the original, as the zips and the index call it
                notes.append(f"`{m.group(1).replace('theme/', 'keynote/', 1) if m.group(1).startswith('theme/') else m.group(1)}` saved again")
            notes.append(saved_by(rel))
            note = "; ".join(n for n in notes if n)
            rows.append(f"| `{arc}` | [{title}](../experiments/{titles.get(num, (num,))[0]}) | {size:,} | `{digest}` |"
                        + (f" {note} |" if note else " |"))
    finally:
        for z in zips.values():
            z.write("fixtures/LICENSE.md", "LICENSE.md")
            z.close()
    order = sorted(per_release, key=lambda r: tuple(int(x) for x in r.split(".")), reverse=True)
    listing = ", ".join(f"`{zip_name(r)}` ({per_release[r]:,} documents)" for r in order)

    index = ["# Fixtures", "",
             "Sample documents from the experiments, for testing readers and writers. They are published as one zip "
             "per app release, attached to the repository's GitHub release `fixtures`, not committed: each zip holds the documents that release saved, "
             f"under the paths listed here. {listing}. Built by `python3 -I fixtures/build.py`, "
             "which leaves out anything from Apple's templates or images, and anything holding a personal name except those whose comments, highlights or tracked changes name the project owner as their author. "
             f"See [LICENSE.md](LICENSE.md).", "",
             f"{len(kept)} documents. Keynote presentations, under `keynote/`, were made with the project's test theme "
             "([0291](../experiments/0291-test-theme.md), [0292](../experiments/0292-test-theme-reruns.md)). "
             "Documents were saved by the 15.4 apps unless their note names another release, such as 14.5. "
             "Under `release/16.0/` (and so on for later releases) is every sample a recipe can make on its own, made again with that release, "
             "Keynote with the test theme ([0473](../experiments/0473-every-scripted-sample-in-16-0.md)). "
             "Under `resaved/16.0/` are the samples 16.0 changed when it opened and saved them again, each noting its original "
             "([0476](../experiments/0476-resaving-every-sample.md)). "
             "Encrypted documents list their test password. A folder package's SHA-256 is taken over each of its files in path order, as the path, a zero byte and the contents.", "",
             "| File | Experiment | Bytes | SHA-256 | Note |", "| --- | --- | --- | --- | --- |"] + rows
    kept_paths = {rel for rel, _ in kept}
    replaced = [rel for rel, why in left if why.endswith("see samples/theme/")
                and rel.replace("samples/", "samples/theme/") in kept_paths]
    index += ["", "## Left out", "",
              f"{len(left) - len(replaced)} documents, besides {len(replaced)} Keynote presentations in Basic White "
              "that are included as their test-theme versions under `keynote/`.", "", "| File | Why |", "| --- | --- |"]
    left = [(rel, "Keynote with Basic White's photos; its test-theme version is left out too"
             if why.endswith("see samples/theme/") else why) for rel, why in left]
    index += [f"| `{rel.replace('samples/', '')}` | {why} |" for rel, why in left if rel not in replaced]
    open("fixtures/INDEX.md", "w", encoding="utf-8").write("\n".join(index) + "\n")
    sizes = ", ".join(f"{r}: {per_release[r]} documents, {os.path.getsize(os.path.join(out_dir, zip_name(r))) / 1e6:.1f} MB" for r in order)
    print(f"{len(kept)} kept, {len(left)} left out; {sizes}")


if __name__ == "__main__":
    main(sys.argv[1])
