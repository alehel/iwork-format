"""Experiments 0455 onward: append a field, given as raw bytes, to a message inside one record.

Usage: python3 -I recipes/0455-append-field.py IN OUT RECORD_ID PATH FIELD HEX

PATH is the dotted path of the message to append to, in the FIELD:N form of
recipes/0383-set-nth-path.py, or `-` for the payload itself. The new field FIELD (length-delimited)
holds the bytes HEX and goes after the message's last field. Everything else is re-encoded unchanged
with the writer of experiment 0287.
"""
import importlib.util
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("w", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


def step(p):
    f, _, n = p.partition(":")
    return int(f), int(n or 1)


def append(payload, path, field, raw):
    fields = w.parse_message(payload)
    if not path:
        fields.append((field, 2, raw))
        return w.serialize_message(fields)
    (head, nth), rest = path[0], path[1:]
    seen = 0
    for i, (f, t, v) in enumerate(fields):
        if f == head:
            seen += 1
            if seen == nth:
                fields[i] = (f, 2, append(v, rest, field, raw))
                return w.serialize_message(fields)
    raise SystemExit(f"field {head}:{nth} not found")


def main(src, dst, record, path, field, hexdata):
    record, field = int(record), int(field)
    steps = [] if path == "-" else [step(p) for p in path.split(".")]
    done = False
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            data = zin.read(info)
            if info.filename.endswith(".iwa"):
                recs = w.records(w.iwa_decode(data))
                for header, payloads in recs:
                    if w.record_id(header) == record:
                        payloads[0] = append(payloads[0], steps, field, bytes.fromhex(hexdata))
                        print(f"record {record}: appended field {field} to {path}")
                        done = True
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)
    if not done:
        raise SystemExit(f"no record {record}")


if __name__ == "__main__":
    main(*sys.argv[1:7])
