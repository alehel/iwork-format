"""Experiments 0302 onward: set one value at a field path in one record, to test a reading by writing.

Usage: python3 -I recipes/0302-set-path.py IN OUT RECORD_ID PATH KIND VALUE [PATH KIND VALUE ...]

PATH is dotted field numbers from the record's payload, such as 1.1.4; each step takes the first
occurrence of that field and creates it if it is missing. KIND says how the last field is written:
varint, float (fixed32), double (fixed64) or string (UTF-8). Prints each old value. Everything else
is re-encoded unchanged by the writer of experiment 0287.
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


def encode(kind, value):
    if kind == "varint":
        return 0, w.write_varint(int(value))
    if kind == "float":
        return 5, struct.pack("<f", float(value))
    if kind == "double":
        return 1, struct.pack("<d", float(value))
    if kind == "string":
        return 2, value.encode("utf-8")
    raise SystemExit(f"unknown kind {kind}")


def decode(wire, raw):
    if wire == 0:
        return w.read_varint(raw, 0)[0]
    if wire == 5:
        return round(struct.unpack("<f", raw)[0], 4)
    if wire == 1:
        return struct.unpack("<d", raw)[0]
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw.hex()


def set_path(payload, path, wire, raw, old):
    fields = w.parse_message(payload)
    head, rest = path[0], path[1:]
    for i, (f, t, v) in enumerate(fields):
        if f == head:
            if rest:
                fields[i] = (f, 2, set_path(v, rest, wire, raw, old))
            else:
                old.append(decode(t, v))
                fields[i] = (f, wire, raw)
            return w.serialize_message(fields)
    fields.append((head, 2, set_path(b"", rest, wire, raw, old)) if rest else (head, wire, raw))
    old.append("absent")
    return w.serialize_message(sorted(fields, key=lambda x: x[0]))


def main(src, dst, record, edits):
    record = int(record)
    found = False
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            data = zin.read(info)
            if info.filename.endswith(".iwa"):
                recs = w.records(w.iwa_decode(data))
                for header, payloads in recs:
                    if w.record_id(header) != record:
                        continue
                    found = True
                    for i in range(0, len(edits), 3):
                        path = [int(p) for p in edits[i].split(".")]
                        wire, raw = encode(edits[i + 1], edits[i + 2])
                        old = []
                        payloads[0] = set_path(payloads[0], path, wire, raw, old)
                        print(f"record {record} field {edits[i]}: {old[0]} -> {edits[i + 2]}")
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)
    if not found:
        raise SystemExit(f"no record {record}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:])
