"""Experiment 0334: set every occurrence of a repeated top-level field in one record.

Usage: python3 -I recipes/0334-set-repeated.py IN OUT RECORD_ID FIELD KIND VALUE [FIRST_ONLY]

KIND is varint, float or string. With FIRST_ONLY set to 1, only the first occurrence changes.
Everything else is re-encoded unchanged with the writer of experiment 0287.
"""
import importlib.util
import os
import struct
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("w", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


def main(src, dst, record, field, kind, value, first_only="0"):
    record, field = int(record), int(field)
    raw = {"varint": lambda: w.write_varint(int(value)), "float": lambda: struct.pack("<f", float(value)),
           "string": lambda: value.encode()}[kind]()
    changed = 0
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            data = zin.read(info)
            if info.filename.endswith(".iwa"):
                recs = w.records(w.iwa_decode(data))
                for header, payloads in recs:
                    if w.record_id(header) != record:
                        continue
                    out = []
                    for f, t, v in w.parse_message(payloads[0]):
                        if f == field and not (first_only == "1" and changed):
                            v = raw
                            changed += 1
                        out.append((f, t, v))
                    payloads[0] = w.serialize_message(out)
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)
    print(f"record {record} field {field}: {changed} occurrence(s) set to {value!r}")


if __name__ == "__main__":
    main(*sys.argv[1:8])
