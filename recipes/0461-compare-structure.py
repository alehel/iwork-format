"""Experiment 0461: compare the structure of two documents, such as the same content saved by two releases.

Usage: python3 -I recipes/0461-compare-structure.py A B

Prints the ZIP entries only one has, the build and version strings in Metadata/Properties.plist,
and, per .iwa part, the number of records of each type, the version (header field 2.2) of each
type, and the top-level payload fields used by each type, where the two differ. Records are decoded with the writer of experiment 0287.
"""
import importlib.util
import os
import plistlib
import sys
import zipfile
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("w", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


def stem(name):
    base = name.rsplit("/", 1)[-1].removesuffix(".iwa")
    head, _, tail = base.partition("-")
    return name.rsplit("/", 1)[0] + "/" + (head if tail and tail.split("-")[0].isdigit() else base)


def survey(path):
    z = zipfile.ZipFile(path)
    names = {stem(n) if n.endswith(".iwa") else n for n in z.namelist()}
    types, versions, fields = defaultdict(Counter), defaultdict(set), defaultdict(set)
    for n in z.namelist():
        if not n.endswith(".iwa"):
            continue
        for header, _ in w.records(w.iwa_decode(z.read(n))):
            for f, _, v in header:
                if f != 2:
                    continue
                d = {k: x for k, _, x in w.parse_message(v)}
                t = w.read_varint(d[1], 0)[0]
                types[stem(n)][t] += 1
                ver, i = [], 0
                raw = d.get(2, b"")
                while i < len(raw):
                    x, i = w.read_varint(raw, i)
                    ver.append(x)
                versions[t].add(".".join(map(str, ver)))
                break
        for header, payloads in w.records(w.iwa_decode(z.read(n))):
            h = {k: x for k, _, x in w.parse_message([v for f, _, v in header if f == 2][0])}
            try:
                fields[w.read_varint(h[1], 0)[0]] |= {f for f, _, _ in w.parse_message(payloads[0])}
            except Exception:
                pass
    history = z.read("Metadata/BuildVersionHistory.plist") if "Metadata/BuildVersionHistory.plist" in z.namelist() else b""
    props = {"BuildVersionHistory": plistlib.loads(history) if history else None}
    if "Metadata/Properties.plist" in z.namelist():
        props.update(plistlib.loads(z.read("Metadata/Properties.plist")))
    return names, types, versions, props, fields


def main(a, b):
    na, ta, va, pa, fa = survey(a)
    nb, tb, vb, pb, fb = survey(b)
    print("entries only in A:", sorted(na - nb))
    print("entries only in B:", sorted(nb - na))
    for k in sorted(set(pa) | set(pb)):
        if pa.get(k) != pb.get(k):
            print(f"Properties.plist {k}: {pa.get(k)!r} -> {pb.get(k)!r}")
    for part in sorted(set(ta) | set(tb)):
        diff = {t: (ta[part][t], tb[part][t]) for t in set(ta[part]) | set(tb[part]) if ta[part][t] != tb[part][t]}
        print(f"{part}: {sum(ta[part].values())} -> {sum(tb[part].values())} records" + (f"; by type {dict(sorted(diff.items()))}" if diff else ""))
    for t in sorted(set(va) | set(vb)):
        if va[t] != vb[t]:
            print(f"type {t} version: {sorted(va[t])} -> {sorted(vb[t])}")
    for t in sorted(set(fa) & set(fb)):
        if fa[t] != fb[t]:
            print(f"type {t} fields only in A: {sorted(fa[t] - fb[t])}, only in B: {sorted(fb[t] - fa[t])}")


if __name__ == "__main__":
    main(*sys.argv[1:3])
