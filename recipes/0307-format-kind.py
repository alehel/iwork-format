"""Experiment 0307: change the kind of one format in a table's format list by writing.

Usage: python3 -I recipes/0307-format-kind.py IN OUT KEY KIND

In every type-6005 record, the field-3 entry whose key (3.1) is KEY and which holds a format
(3.6) gets KIND as the format's kind (3.6.1). Everything else is re-encoded unchanged with the
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


def record_type(header):
    info = {f: v for f, _, v in w.parse_message({f: v for f, _, v in header}[2])}
    return w.read_varint(info[1], 0)[0]


def main(src, dst, key, kind):
    key, kind = int(key), int(kind)
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
                            if any(k == 1 and w.read_varint(vv, 0)[0] == key for k, _, vv in entry) and any(k == 6 for k, _, _ in entry):
                                new = []
                                for k, tt, vv in entry:
                                    if k == 6:
                                        fmt = w.parse_message(vv)
                                        old = next(w.read_varint(x, 0)[0] for a, _, x in fmt if a == 1)
                                        vv = w.serialize_message([(a, b, w.write_varint(kind) if a == 1 else x) for a, b, x in fmt])
                                        print(f"{info.filename} record {w.record_id(header)} format key {key}: kind {old} -> {kind}")
                                    new.append((k, tt, vv))
                                v = w.serialize_message(new)
                        out.append((f, t, v))
                    payloads[0] = w.serialize_message(out)
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)


if __name__ == "__main__":
    main(*sys.argv[1:5])
