"""Experiment 0299: mark a slide skipped by writing its slide node.

Usage: python3 -I recipes/0299-skip-slide.py IN OUT NODE_ID

Sets field 4 = 1 in the slide node (type 4) with the given ID, which experiment 0070 read as
the skipped flag, and re-encodes everything else unchanged with the writer of experiment 0287.
"""
import importlib.util
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("w", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


def main(src, dst, node):
    node = int(node)
    changed = 0
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            data = zin.read(info)
            if info.filename.endswith(".iwa"):
                recs = w.records(w.iwa_decode(data))
                for header, payloads in recs:
                    if w.record_id(header) == node:
                        fields = [(f, t, v) for f, t, v in w.parse_message(payloads[0]) if f != 4]
                        fields.append((4, 0, w.write_varint(1)))
                        payloads[0] = w.serialize_message(sorted(fields, key=lambda x: x[0]))
                        changed += 1
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)
    print(f"node {node}: {changed} changed")


if __name__ == "__main__":
    main(*sys.argv[1:4])
