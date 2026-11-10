"""Experiment 0294: check that type-11015 colours cover exactly the data kept as app resources.

Usage: python3 -I recipes/0294-resource-colours.py SAMPLES_DIR

For each document, it reads the data list (Metadata.iwa record 2, field 4) and the type-11015
record, and checks both ways: every data ID with a colour has no stored file and a resource path
(field 5), and every such resource entry has a colour. Uses the writer of experiment 0287.
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
    docs = coloured = resources = mismatched = 0
    for path in sorted(glob.glob(os.path.join(root, "**", "*.*"), recursive=True)):
        if not path.endswith((".pages", ".key", ".numbers")) or not os.path.isfile(path):
            continue
        z = zipfile.ZipFile(path)
        if ".iwpv2" in z.namelist() or "Index/Metadata.iwa" not in z.namelist():
            continue
        recs = {}
        for header, payloads in w.records(w.iwa_decode(z.read("Index/Metadata.iwa"))):
            kind = w.read_varint(fields({f: v for f, _, v in header}[2])[1], 0)[0]
            recs[w.record_id(header)] = (kind, payloads[0] if payloads else b"")
        if 2 not in recs:
            continue
        docs += 1
        resource = set()
        for f, _, v in w.parse_message(recs[2][1]):
            if f == 4:
                e = fields(v)
                if not e.get(4) and e.get(5):
                    resource.add(w.read_varint(e[1], 0)[0])
        with_colour = set()
        for kind, payload in recs.values():
            if kind == 11015:
                for f, _, v in w.parse_message(payload):
                    with_colour.add(w.read_varint(fields(v)[1], 0)[0])
        coloured += len(with_colour)
        resources += len(resource)
        if with_colour != resource:
            mismatched += 1
            print(f"{path}: colours {sorted(with_colour - resource)} without a resource, resources {sorted(resource - with_colour)} without a colour")
    print(f"{docs} documents, {coloured} colours, {resources} resource entries, {mismatched} documents where they differ")


if __name__ == "__main__":
    main(sys.argv[1])
