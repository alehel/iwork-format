"""Experiment 0396: change one field of a record's header, for one of its payloads.

Usage: python3 -I recipes/0396-record-header.py IN OUT RECORD_ID PAYLOAD FIELD VALUE

PAYLOAD counts the header's field-2 messages from 1. FIELD is a field of that message: 1 (written
as a varint), 2 (VALUE is comma-separated numbers, written as packed varints), or any field with
VALUE `-` to remove it. Payload lengths (2.3) are rewritten as usual by the writer of experiment
0287; everything else is re-encoded unchanged.
"""
import importlib.util
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("w", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


def describe(f, v):
    if f == 2:
        out, i = [], 0
        while i < len(v):
            n, i = w.read_varint(v, i)
            out.append(n)
        return ",".join(map(str, out))
    if f == 1:
        return str(w.read_varint(v, 0)[0])
    return v.hex()


def main(src, dst, record, payload, field, value):
    record, payload, field = int(record), int(payload), int(field)
    done = False
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            data = zin.read(info)
            if info.filename.endswith(".iwa"):
                recs = w.records(w.iwa_decode(data))
                for rec in recs:
                    header = rec[0]
                    if w.record_id(header) != record:
                        continue
                    seen, new = 0, []
                    for f, t, v in header:
                        if f == 2:
                            seen += 1
                            if seen == payload:
                                fs = w.parse_message(v)
                                old = next((describe(k, x) for k, _, x in fs if k == field), "absent")
                                fs = [x for x in fs if x[0] != field]
                                if value != "-":
                                    raw = (w.write_varint(int(value)) if field == 1 else
                                           b"".join(w.write_varint(int(n)) for n in value.split(",")))
                                    fs.append((field, 0 if field == 1 else 2, raw))
                                    fs.sort(key=lambda x: x[0])
                                v = w.serialize_message(fs)
                                print(f"record {record} payload {payload} header 2.{field}: {old} -> {value}")
                                done = True
                        new.append((f, t, v))
                    rec[0] = new
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)
    if not done:
        raise SystemExit(f"no record {record} with payload {payload}")


if __name__ == "__main__":
    main(*sys.argv[1:7])
