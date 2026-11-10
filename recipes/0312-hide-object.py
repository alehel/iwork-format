"""Experiment 0312: hide an object on a slide by removing it from the slide's lists.

Usage: python3 -I recipes/0312-hide-object.py IN OUT SLIDE_ID OBJECT_ID [FIELD ...]

Removes, from the slide record (type 5), every entry of the given repeated fields (default 7
and 42) whose reference (field 1) is OBJECT_ID. Everything else is re-encoded unchanged with the
writer of experiment 0287.
"""
import importlib.util
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("w", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


def main(src, dst, slide, obj, fields):
    slide, obj = int(slide), int(obj)
    fields = {int(f) for f in fields} or {7, 42}
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            data = zin.read(info)
            if info.filename.endswith(".iwa"):
                recs = w.records(w.iwa_decode(data))
                for header, payloads in recs:
                    if w.record_id(header) != slide:
                        continue
                    kept, removed = [], 0
                    for f, t, v in w.parse_message(payloads[0]):
                        if f in fields and t == 2:
                            ref = {k: x for k, _, x in w.parse_message(v)}.get(1)
                            if ref is not None and w.read_varint(ref, 0)[0] == obj:
                                removed += 1
                                continue
                        kept.append((f, t, v))
                    payloads[0] = w.serialize_message(kept)
                    print(f"slide {slide}: removed {removed} entries for {obj}")
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5:])
