"""Experiment 0381: show an object on a slide by adding it to the slide's lists (the reverse of 0312).

Usage: python3 -I recipes/0381-show-object.py IN OUT SLIDE_ID OBJECT_ID [FIELD ...]

Adds an entry { 1: OBJECT_ID } to each of the given repeated fields (default 7 and 42) of the slide
record (type 5), after that field's last entry. The object must already be one the slide refers
to. Everything else is re-encoded unchanged with the writer of experiment 0287.
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
    fields = [int(f) for f in fields] or [7, 42]
    entry = w.serialize_message([(1, 0, w.write_varint(obj))])
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            data = zin.read(info)
            if info.filename.endswith(".iwa"):
                recs = w.records(w.iwa_decode(data))
                for header, payloads in recs:
                    if w.record_id(header) != slide:
                        continue
                    fs = w.parse_message(payloads[0])
                    for field in fields:
                        last = max((i for i, (f, _, _) in enumerate(fs) if f == field), default=None)
                        at = len(fs) if last is None else last + 1
                        fs.insert(at, (field, 2, entry))
                    payloads[0] = w.serialize_message(fs)
                    print(f"slide {slide}: added {obj} to fields {fields}")
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5:])
