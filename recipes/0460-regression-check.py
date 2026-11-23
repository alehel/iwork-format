"""Experiment 0460: the regression check of 0178 and 0247, over every sample document.

Usage: python3 -I recipes/0460-regression-check.py SAMPLES_DIR [PROBE]

For every .pages, .key and .numbers under SAMPLES_DIR (ZIP files and folder packages), runs three
checks and prints one line per document that fails any of them, then totals:
  1. framing: `iwork-probe records` succeeds on every .iwa part;
  2. reachability: from objects 1, 2 and 71, and 61 when the document has one, following only the
     IDs in record headers (fields 2.5 and 2.4.4), every object is reached;
  3. text: `iwork-probe text` succeeds.
Reachability decodes the parts with the writer of experiment 0287, so it covers ZIP documents and
skips encrypted ones, which `iwork-probe --password` reads (0266). Only the standard library is used.
"""
import glob
import importlib.util
import os
import subprocess
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("w", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


def packed(v):
    out, i = [], 0
    while i < len(v):
        n, i = w.read_varint(v, i)
        out.append(n)
    return out


def refs(header):
    out = []
    for f, _, v in header:
        if f != 2:
            continue
        for k, _, x in w.parse_message(v):
            if k == 5:
                out += packed(x)
            elif k == 4:
                for kk, _, xx in w.parse_message(x):
                    if kk == 4:
                        out += packed(xx)
    return out


def reach(path):
    """(objects, unreached) for a ZIP document, or None when it can't be decoded this way."""
    try:
        z = zipfile.ZipFile(path)
    except (zipfile.BadZipFile, IsADirectoryError):
        return None
    if any(n.endswith(".iwpv2") or n == ".iwph" for n in z.namelist()):
        return None
    graph = {}
    for n in z.namelist():
        if n.endswith(".iwa"):
            try:
                for header, _ in w.records(w.iwa_decode(z.read(n))):
                    graph[w.record_id(header)] = refs(header)
            except Exception:
                return None
    seen, todo = set(), [r for r in (1, 2, 71, 61) if r in graph]
    while todo:
        o = todo.pop()
        if o in seen:
            continue
        seen.add(o)
        todo += [r for r in graph.get(o, []) if r in graph and r not in seen]
    return len(graph), sorted(set(graph) - seen)


def main(samples, probe="target/release/iwork-probe"):
    docs = sorted(p for p in glob.glob(os.path.join(samples, "**", "*"), recursive=True)
                  if p.endswith((".pages", ".key", ".numbers")) and "/." not in p
                  and not os.path.dirname(p).endswith((".pages", ".key", ".numbers")))
    totals = {"documents": 0, "framing": 0, "text": 0, "unreached": 0, "reachability checked": 0, "objects": 0}
    for d in docs:
        totals["documents"] += 1
        problems = []
        listing = subprocess.run([probe, "list", d], capture_output=True, text=True)
        if listing.returncode != 0:
            problems.append("list: " + listing.stderr.strip()[:120])
            parts = []
        else:
            parts = [line.split()[-1] for line in listing.stdout.splitlines() if line.strip().endswith(".iwa")]
        for p in parts:
            r = subprocess.run([probe, "records", d, p], capture_output=True, text=True)
            if r.returncode != 0 and "password" not in r.stderr.lower():
                problems.append(f"framing {p}: " + r.stderr.strip()[:120])
                totals["framing"] += 1
        t = subprocess.run([probe, "text", d], capture_output=True, text=True)
        if t.returncode != 0 and "password" not in t.stderr.lower():
            problems.append("text: " + t.stderr.strip()[:120])
            totals["text"] += 1
        got = reach(d)
        if got is not None:
            n, unreached = got
            totals["reachability checked"] += 1
            totals["objects"] += n
            if unreached:
                totals["unreached"] += 1
                problems.append(f"{len(unreached)} of {n} objects unreached, such as {unreached[:3]}")
        if problems:
            print(os.path.relpath(d, samples) + ": " + "; ".join(problems))
    print(totals)


if __name__ == "__main__":
    main(*sys.argv[1:3])
