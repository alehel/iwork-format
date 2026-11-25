"""Unpack the fixtures zips into the checkout of the samples repository, one file per document.

Usage: python3 -I fixtures/samples_repo.py ZIP_DIR REPO_DIR

ZIP_DIR holds the zips fixtures/build.py made. Writes each document of the release zips to REPO_DIR under
its published path, so an experiment can link to it, with LICENSE.md and a README.md. A folder package is
written as a ZIP of the folder, NAME.zip, since a folder can't be downloaded by one link and Git doesn't
keep its empty folders. Every document must have the checksum fixtures/INDEX.md lists, and every document
listed must be there; documents in REPO_DIR that are no longer published are removed. Only the standard
library is used.
"""
import glob
import hashlib
import os
import re
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXT = (".pages", ".key", ".numbers")
README = """# iwork-format samples

The sample documents of the [iwork-format](https://github.com/alehel/iwork-format) experiments, one file each, so that the experiments can link to the documents they rest on. Each is listed with its experiment and SHA-256 in the [fixtures index](https://github.com/alehel/iwork-format/blob/main/fixtures/INDEX.md). To get them all, download the zips of the [fixtures release](https://github.com/alehel/iwork-format/releases/tag/fixtures), which hold the same documents.

The files are made by `fixtures/samples_repo.py` in that repository; don't change them here. A folder package is a ZIP of the folder. What the project contributed is released under CC0; see [LICENSE.md](LICENSE.md).
"""


def main(zip_dir, repo):
    with open(os.path.join(ROOT, "fixtures", "INDEX.md"), encoding="utf-8") as f:
        listed = dict(re.findall(r"^\| `([^`]+)` \| .*? \| [\d,]+ \| `([0-9a-f]{64})` \|", f.read(), re.M))
    if not os.path.isdir(os.path.join(repo, ".git")):
        sys.exit(f"{repo} isn't a Git checkout")
    written = set()

    def write(path, data):
        full = os.path.join(repo, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "wb") as f:
            f.write(data)
        written.add(path)

    seen = set()
    for name in sorted(glob.glob(os.path.join(zip_dir, "iwork-format-fixtures-[0-9]*.zip"))):
        with zipfile.ZipFile(name) as z:
            folders = {}
            for info in z.infolist():
                m = re.match(r"^(.*?\.(?:pages|key|numbers))/(.*)$", info.filename)
                if m:
                    folders.setdefault(m[1], []).append((m[2], info))
                elif info.filename in listed:
                    data = z.read(info)
                    if hashlib.sha256(data).hexdigest() != listed[info.filename]:
                        sys.exit(f"{info.filename}: not the document INDEX.md lists")
                    write(info.filename, data)
                    seen.add(info.filename)
                elif info.filename == "LICENSE.md":
                    write("LICENSE.md", z.read(info))
                else:
                    sys.exit(f"{info.filename}: not in INDEX.md")
            for path, entries in folders.items():
                h = hashlib.sha256()
                for inner, info in sorted(entries, key=lambda x: x[0]):
                    if not inner.endswith("/") and inner:
                        h.update(inner.encode() + b"\0" + z.read(info))
                if h.hexdigest() != listed.get(path):
                    sys.exit(f"{path}: not the folder INDEX.md lists")
                out = os.path.join(repo, path + ".zip")
                os.makedirs(os.path.dirname(out), exist_ok=True)
                with zipfile.ZipFile(out, "w", zipfile.ZIP_STORED) as packed:
                    for inner, info in sorted(entries, key=lambda x: x[0]):
                        new = zipfile.ZipInfo(f"{os.path.basename(path)}/{inner}")  # no times, so a rerun gives the same file
                        new.external_attr = info.external_attr
                        packed.writestr(new, z.read(info) if not inner.endswith("/") and inner else b"")
                written.add(path + ".zip")
                seen.add(path)
    missing = set(listed) - seen
    if missing:
        sys.exit(f"INDEX.md lists {len(missing)} documents the zips don't hold, such as {sorted(missing)[0]}")
    write("README.md", README.encode())
    write(".gitattributes", "".join(f"*{e} binary\n" for e in EXT + (".zip",)).encode())
    removed = 0
    for d, subdirs, files in os.walk(repo):
        subdirs[:] = [s for s in subdirs if s != ".git"]
        for f in files:
            rel = os.path.relpath(os.path.join(d, f), repo)
            if rel not in written and rel.endswith(EXT + (".zip",)):
                os.remove(os.path.join(d, f))
                removed += 1
    print(f"{len(seen)} documents in {repo}; {removed} removed")


if __name__ == "__main__":
    main(*sys.argv[1:])
