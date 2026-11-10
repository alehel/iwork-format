"""Experiment 0293: check how the calculation engine's owners (type 4008) and lists (type 4009) pair up.

Usage: python3 -I recipes/0293-calculation-owners.py SAMPLES_DIR

For every document with a CalculationEngine part, it follows each type-4008 record's field 13.1
to its type-4009 list and compares the list's field 1 with the owner's field 2. Uses the writer
of experiment 0287.
"""
import glob
import importlib.util
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("w", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


def fields(b):
    return {k: v for k, _, v in w.parse_message(b)}


def main(root):
    agree = differ = docs = 0
    for path in sorted(glob.glob(os.path.join(root, "**", "*.*"), recursive=True)):
        if not path.endswith((".pages", ".key", ".numbers")) or not os.path.isfile(path):
            continue
        z = zipfile.ZipFile(path)
        parts = [n for n in z.namelist() if n.startswith("Index/CalculationEngine")]
        if not parts or ".iwpv2" in z.namelist():
            continue
        docs += 1
        recs = {}
        for n in parts:
            for header, payloads in w.records(w.iwa_decode(z.read(n))):
                info = fields({f: v for f, _, v in header}[2])
                recs[w.record_id(header)] = (w.read_varint(info[1], 0)[0], payloads[0] if payloads else b"")
        for kind, payload in recs.values():
            if kind != 4008:
                continue
            try:
                owner = fields(payload)
                target = w.read_varint(fields(fields(owner[13])[1])[1], 0)[0]
                number = w.read_varint(fields(recs[target][1])[1], 0)[0]
            except (KeyError, IndexError):
                continue
            if number == w.read_varint(owner[2], 0)[0]:
                agree += 1
            else:
                differ += 1
    print(f"{docs} documents: list field 1 equals owner field 2 in {agree} lists, differs in {differ}")


if __name__ == "__main__":
    main(sys.argv[1])
