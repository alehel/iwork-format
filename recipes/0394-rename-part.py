"""Experiment 0394: rename one .iwa part of a document, with or without updating Metadata.iwa.

Usage: python3 -I recipes/0394-rename-part.py IN OUT OLD_NAME NEW_NAME [--metadata]

OLD_NAME and NEW_NAME are ZIP entry names such as Index/ViewState.iwa. The part's bytes are
unchanged. With --metadata, the component entry in Metadata.iwa record 2 (a field 3 whose field 2
or 3 is the old stem) gets the new stem in its field 3; or loses field 3 when the new stem equals
its name in field 2. Everything else is re-encoded unchanged with the writer of experiment 0287.
"""
import importlib.util
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("w", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


def stem(name):
    return name.rsplit("/", 1)[-1].removesuffix(".iwa")


def relocate(payload, old, new):
    out, done = [], False
    for f, t, v in w.parse_message(payload):
        if f == 3 and t == 2 and not done:
            fs = w.parse_message(v)
            d = {k: x for k, _, x in fs}
            name = d.get(2, b"").decode("utf-8", "replace")
            where = d.get(3, d.get(2, b"")).decode("utf-8", "replace")
            if where == old:
                fs = [x for x in fs if x[0] != 3]
                if new != name:
                    fs.append((3, 2, new.encode("utf-8")))
                    fs.sort(key=lambda x: x[0])
                v, done = w.serialize_message(fs), True
                print(f"component {name}: stored as {where} -> {new}")
        out.append((f, t, v))
    if not done:
        raise SystemExit(f"no component stored as {old}")
    return w.serialize_message(out)


def main(src, dst, old, new, *opts):
    found = False
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            name, data = info.filename, zin.read(info)
            if name == old:
                name, found = new, True
            if "--metadata" in opts and info.filename == "Index/Metadata.iwa":
                recs = w.records(w.iwa_decode(data))
                for header, payloads in recs:
                    if w.record_id(header) == 2:
                        payloads[0] = relocate(payloads[0], stem(old), stem(new))
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(name, date_time=info.date_time), data)
    if not found:
        raise SystemExit(f"no part {old}")
    print(f"{old} -> {new}")


if __name__ == "__main__":
    main(*sys.argv[1:])
