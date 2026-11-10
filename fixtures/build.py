"""Collect the experiments' sample documents that can be published, check them, and pack them.

Usage: python3 -I fixtures/build.py OUT.zip

Reads the local samples/ folder (gitignored), writes fixtures/INDEX.md (committed) and OUT.zip
(published as a GitHub release asset). A document is published only if:
  - it isn't from an experiment on Apple's templates (0090, 0155-0158, 0198, 0199);
  - a Keynote presentation comes from samples/theme/, made with the project's test theme
    (experiments 0291, 0292), never from Basic White;
  - every file under Data/ is one the project made: the test cards, Keynote's thumbnails of
    them, or the project's own images, sound and movie;
  - no part, decoded or decrypted, holds a name this Mac knows its user by (site/examples.py).
Folder packages and documents that fail a check are listed as left out, with the reason.
"""
import hashlib
import importlib.util
import os
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
                "samples/0249/comment.pages", "samples/0268/accepted.pages", "samples/0269/rejected.pages"}
PASSWORDS = {"samples/0179/locked.pages": "pw1234", "samples/0179/locked2.pages": "pw1234",
             "samples/0180/accent.pages": "påss", "samples/0180/image.pages": "pw1234",
             "samples/0180/locked.numbers": "pw1234",
             "samples/theme/0180/locked.key": "pw1234"}


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
    if rel.endswith(".key") and not rel.startswith("samples/theme/"):
        if num in ("0291", "0292"):
            return "a step in building or testing the test theme, which is in theme/"
        if os.path.exists(rel.replace("samples/", "samples/theme/")):
            return "Keynote with Basic White's photos; see samples/theme/"
        return "Keynote with Basic White's photos, not yet rerun with the test theme"
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
    password = PASSWORDS.get(rel)
    parts = folder_parts(path) if os.path.isdir(path) else decrypted_parts(path, password) if password else plain_parts(path)
    for name, data in parts:
        low = data.lower()
        for word in words:
            if word in low or word.decode().encode("utf-16-le") in low or word.decode().encode("utf-16-be") in low:
                return "holds the user's name"
    return None


def main(out_zip):
    os.chdir(ROOT)
    candidates = []
    for d in sorted(os.listdir("samples")):
        if re.fullmatch(r"\d{4}", d):
            candidates += [f"samples/{d}/{f}" for f in sorted(os.listdir(f"samples/{d}"))]
    candidates += [f"samples/theme/{d}/{f}" for d in sorted(os.listdir("samples/theme")) for f in sorted(os.listdir(f"samples/theme/{d}"))]
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

    with zipfile.ZipFile(out_zip, "w", zipfile.ZIP_STORED) as z:
        rows = []
        for rel, _ in kept:
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
            pw = PASSWORDS.get(rel)
            rows.append(f"| `{arc}` | [{title}](../experiments/{titles.get(num, (num,))[0]}) | {size:,} | `{digest}` |"
                        + (f" password `{pw}` |" if pw else " names its author |" if rel in AUTHOR_NAMED else " a folder package |" if os.path.isdir(rel) else " |"))
        z.write("fixtures/LICENSE.md", "LICENSE.md")

    index = ["# Fixtures", "",
             "Sample documents from the experiments, for testing readers and writers. They are published as a zip "
             "attached to the repository's GitHub release `fixtures`, not committed. Built by `python3 -I fixtures/build.py`, "
             "which leaves out anything from Apple's templates or images, and anything holding a personal name except the six whose comments, highlights or tracked changes name the project owner as their author. "
             f"See [LICENSE.md](LICENSE.md).", "",
             f"{len(kept)} documents. Keynote presentations, under `keynote/`, were made with the project's test theme "
             "([0291](../experiments/0291-test-theme.md), [0292](../experiments/0292-test-theme-reruns.md)). "
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
    print(f"{len(kept)} kept, {len(left)} left out, {os.path.getsize(out_zip) / 1e6:.1f} MB")


if __name__ == "__main__":
    main(sys.argv[1])
