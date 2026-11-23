"""Experiment 0465: check which app release saved each sample against what its experiment says.

Usage: python3 -I recipes/0465-saved-by.py SAMPLES_DIR

For every .pages, .key and .numbers under SAMPLES_DIR (ZIP files and folder packages), reads the
builds listed in Metadata/BuildVersionHistory.plist (such as M15.4-7051.0.79-2), and compares the
release of the last one with the releases the experiment's setup names (as site/build.py reads
them). Prints every document saved by more than one release or by a release its experiment
doesn't name, then totals by kind of document and release. Encrypted documents, whose build history
is encrypted, are counted apart. Only the standard library is used.
"""
import glob
import importlib.util
import os
import plistlib
import re
import sys
import zipfile
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
spec = importlib.util.spec_from_file_location("b", os.path.join(ROOT, "site", "build.py"))
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)


def history(path):
    if os.path.isdir(path):
        data = open(os.path.join(path, "Metadata", "BuildVersionHistory.plist"), "rb").read()
    else:
        data = zipfile.ZipFile(path).read("Metadata/BuildVersionHistory.plist")
    return [x for x in plistlib.loads(data) if isinstance(x, str) and re.match(r"^M\d+\.\d+-", x)]


def main(samples):
    stated = {}
    for f in os.listdir(os.path.join(ROOT, "experiments")):
        m = re.match(r"^(\d{4})-.*\.md$", f)
        if m:
            with open(os.path.join(ROOT, "experiments", f), encoding="utf-8") as fh:
                stated[m.group(1)] = b.experiment_releases(fh.read())
    totals, builds = Counter(), Counter()
    encrypted = several = mismatched = 0
    for p in sorted(glob.glob(os.path.join(samples, "**", "*"), recursive=True)):
        if not p.endswith((".pages", ".key", ".numbers")) or os.path.dirname(p).endswith((".pages", ".key", ".numbers")):
            continue
        try:
            hist = history(p)
        except Exception:
            encrypted += 1
            continue
        parts = os.path.relpath(p, samples).split(os.sep)
        exp = parts[1] if parts[0] == "theme" else parts[0]
        releases = sorted({h[1:].split("-")[0] for h in hist})
        builds.update(set(hist))
        totals[(os.path.splitext(p)[1], ", ".join(releases))] += 1
        if len(releases) > 1:
            several += 1
            print("SEVERAL", "/".join(parts), releases)
        want = stated.get(exp, [])
        if want and releases and hist[-1][1:].split("-")[0] not in want:
            mismatched += 1
            print("MISMATCH", "/".join(parts), "saved by", releases, "experiment names", want)
    print(f"{sum(totals.values())} documents read, {encrypted} unreadable (encrypted); "
          f"{several} saved by more than one release, {mismatched} by a release their experiment doesn't name")
    for (kind, rel), n in sorted(totals.items()):
        print(f"  {kind} saved by {rel}: {n}")
    for build, n in builds.most_common():
        print(f"  build {build}: {n}")


if __name__ == "__main__":
    main(*sys.argv[1:2])
