"""Experiment 0435: add a data file that nothing uses, with an entry in Metadata.iwa record 2.

Usage: python3 -I recipes/0435-add-data.py IN OUT DATA_ID FILE [--no-entry]

Stores FILE as Data/<stem>-<DATA_ID><ext> and, unless --no-entry, appends to field 4 of Metadata.iwa
record 2 an entry { 1: DATA_ID, 2: SHA-1 of FILE, 3: FILE's name, 4: the stored name }, the fields
spec/container.md describes. Everything else is re-encoded unchanged with the writer of 0287.
"""
import hashlib
import importlib.util
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("w", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


def main(src, dst, data_id, path, *opts):
    data_id = int(data_id)
    body = open(path, "rb").read()
    name = os.path.basename(path)
    stem, ext = os.path.splitext(name)
    stored = f"{stem}-{data_id}{ext}"
    entry = w.serialize_message([(1, 0, w.write_varint(data_id)), (2, 2, hashlib.sha1(body).digest()),
                                 (3, 2, name.encode()), (4, 2, stored.encode())])
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            data = zin.read(info)
            if info.filename == "Index/Metadata.iwa" and "--no-entry" not in opts:
                recs = w.records(w.iwa_decode(data))
                for header, payloads in recs:
                    if w.record_id(header) == 2:
                        fs = w.parse_message(payloads[0])
                        last = max(i for i, x in enumerate(fs) if x[0] == 4)
                        fs.insert(last + 1, (4, 2, entry))
                        payloads[0] = w.serialize_message(fs)
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)
        zout.writestr(zipfile.ZipInfo("Data/" + stored, date_time=(2026, 11, 18, 0, 0, 0)), body)
    print(f"added Data/{stored}" + ("" if "--no-entry" in opts else " with an entry"))


if __name__ == "__main__":
    main(*sys.argv[1:])
