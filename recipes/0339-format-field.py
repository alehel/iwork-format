"""Experiment 0339: change one field of one format in a table's format list by writing.

Usage: python3 -I recipes/0339-format-field.py IN OUT KEY FIELD KIND VALUE

In every type-6005 record, the entry whose key (3.1) is KEY and which holds a format (3.6) gets
VALUE in format field FIELD, written as KIND (varint or string). Everything else is re-encoded
unchanged with the writer of experiment 0287.
"""
import importlib.util
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("w", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


def main(src, dst, key, field, kind, value):
    key, field = int(key), int(field)
    raw = w.write_varint(int(value)) if kind == "varint" else value.encode()
    wire = 0 if kind == "varint" else 2
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            data = zin.read(info)
            if info.filename.endswith(".iwa"):
                recs = w.records(w.iwa_decode(data))
                for header, payloads in recs:
                    if w.read_varint({f: v for f, _, v in w.parse_message({f: v for f, _, v in header}[2])}[1], 0)[0] != 6005:
                        continue
                    out = []
                    for f, t, v in w.parse_message(payloads[0]):
                        if f == 3:
                            entry = w.parse_message(v)
                            d = {k: x for k, _, x in entry}
                            if 6 in d and 1 in d and w.read_varint(d[1], 0)[0] == key:
                                fmt = [(k, kt, x) for k, kt, x in w.parse_message(d[6]) if k != field] + [(field, wire, raw)]
                                fmt.sort(key=lambda x: x[0])
                                v = w.serialize_message([(k, kt, w.serialize_message(fmt) if k == 6 else x) for k, kt, x in entry])
                                print(f"format key {key}: field {field} -> {value!r}")
                        out.append((f, t, v))
                    payloads[0] = w.serialize_message(out)
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)


if __name__ == "__main__":
    main(*sys.argv[1:7])
