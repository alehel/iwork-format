"""Experiment 0306: change one entry of a table's string table (type 6005) by writing.

Usage: python3 -I recipes/0306-rename-string.py IN OUT KEY NEW_TEXT

In every type-6005 record, the field-3 entry whose key (3.1) is KEY gets NEW_TEXT as its string
(3.3). Everything else is re-encoded unchanged with the writer of experiment 0287.
"""
import importlib.util
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("w", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


def record_type(header):
    info = {f: v for f, _, v in w.parse_message({f: v for f, _, v in header}[2])}
    return w.read_varint(info[1], 0)[0]


def main(src, dst, key, text):
    key = int(key)
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            data = zin.read(info)
            if info.filename.endswith(".iwa"):
                recs = w.records(w.iwa_decode(data))
                for header, payloads in recs:
                    if record_type(header) != 6005:
                        continue
                    out = []
                    for f, t, v in w.parse_message(payloads[0]):
                        if f == 3:
                            entry = w.parse_message(v)
                            if any(k == 1 and w.read_varint(vv, 0)[0] == key for k, _, vv in entry) and any(k == 3 for k, _, _ in entry):
                                old = next(vv for k, _, vv in entry if k == 3).decode()
                                entry = [(k, tt, text.encode() if k == 3 else vv) for k, tt, vv in entry]
                                v = w.serialize_message(entry)
                                print(f"{info.filename} record {w.record_id(header)} key {key}: {old!r} -> {text!r}")
                        out.append((f, t, v))
                    payloads[0] = w.serialize_message(out)
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)


if __name__ == "__main__":
    main(*sys.argv[1:5])
