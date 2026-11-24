"""Experiment 0481: compare the file format version kept in Metadata.iwa with Properties.plist's.

Usage: python3 -I recipes/0481-format-version.py SAMPLES_DIR

For every .pages, .key and .numbers under SAMPLES_DIR (ZIP files and folder packages), reads field 7 of
the type-11006 record in Index/Metadata.iwa as packed varints, joins them with dots and compares them
with fileFormatVersion in Metadata/Properties.plist. Prints every document where they differ, then the
totals by folder, version and the release of the last build in BuildVersionHistory.plist. A document
under samples/release/R/, samples/resave/R/ or samples/resaved/R/ whose last build isn't R's is printed
too. Encrypted documents can't be read and are counted apart. Only the standard library is used.
"""
import importlib.util
import io
import os
import plistlib
import re
import sys
import zipfile
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("writer", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


def parts(path):
    """Metadata.iwa's stored bytes and the two property lists of a document."""
    if os.path.isdir(path):
        z = zipfile.ZipFile(os.path.join(path, "Index.zip"))
        meta = lambda n: open(os.path.join(path, "Metadata", n), "rb").read()
        return z.read("Index/Metadata.iwa"), plistlib.loads(meta("Properties.plist")), plistlib.loads(meta("BuildVersionHistory.plist"))
    z = zipfile.ZipFile(io.BytesIO(open(path, "rb").read()))
    return (z.read("Index/Metadata.iwa"), plistlib.loads(z.read("Metadata/Properties.plist")),
            plistlib.loads(z.read("Metadata/BuildVersionHistory.plist")))


def packed(value):
    out, i = [], 0
    while i < len(value):
        n, i = w.read_varint(value, i)
        out.append(n)
    return ".".join(map(str, out))


def field7(raw):
    for header, payloads in w.records(w.iwa_decode(raw)):
        for info, payload in zip([v for f, _, v in header if f == 2], payloads):
            kind = next(w.read_varint(v, 0)[0] for f, _, v in w.parse_message(info) if f == 1)
            if kind == 11006:
                return [packed(v) for f, wire, v in w.parse_message(payload) if f == 7 and wire == 2]
    return []


def documents(top):
    for d, subdirs, files in sorted(os.walk(top, followlinks=True)):
        names = [n for n in sorted(subdirs + files) if re.search(r"\.(pages|numbers|key)$", n)]
        subdirs[:] = [s for s in subdirs if s not in names]
        yield from (os.path.join(d, n) for n in names)


def main(top):
    totals, unread, wrong, builds = Counter(), Counter(), 0, 0
    for path in documents(top):
        rel = os.path.relpath(path, top)
        m = re.match(r"((?:release|resave|resaved)/([^/]+))/", rel)
        folder = m.group(1) if m else "the rest"
        try:
            raw, props, history = parts(path)
            got = field7(raw)
        except Exception:
            unread[folder] += 1
            continue
        version = props.get("fileFormatVersion")
        last = [b for b in history if re.match(r"M\d+\.\d+-", b)][-1][1:].split("-")[0]
        totals[(folder, version, last)] += 1
        if got != [version]:
            wrong += 1
            print(f"DIFFERS {rel}: field 7 {got}, fileFormatVersion {version}")
        if m and last != m.group(2):
            builds += 1
            if builds <= 5:
                print(f"SAVED BY {last}: {rel}")
    for (folder, version, last), n in sorted(totals.items()):
        print(f"{folder}: {n} documents of {version}, saved by {last}")
    for folder, n in sorted(unread.items()):
        print(f"{folder}: {n} not read")
    print(f"{sum(totals.values())} compared, {wrong} differ, {builds} saved by another release than their folder names")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
