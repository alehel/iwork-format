"""Experiments 0383 onward: set one value at a field path that runs through repeated fields.

Usage: python3 -I recipes/0383-set-nth-path.py IN OUT RECORD_ID PATH KIND VALUE [PATH KIND VALUE ...]

As recipes/0302-set-path.py, except that each step of PATH may be FIELD:N, the Nth occurrence of
that field counting from 1 (a plain FIELD is FIELD:1), and that every step must already exist.
KIND is varint, float, double or string. Prints each old value.
"""
import importlib.util
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("s", os.path.join(HERE, "0302-set-path.py"))
s = importlib.util.module_from_spec(spec)
spec.loader.exec_module(s)
w = s.w


def set_path(payload, path, wire, raw, old):
    fields = w.parse_message(payload)
    (head, nth), rest = path[0], path[1:]
    seen = 0
    for i, (f, t, v) in enumerate(fields):
        if f == head:
            seen += 1
            if seen < nth:
                continue
            if rest:
                fields[i] = (f, 2, set_path(v, rest, wire, raw, old))
            else:
                old.append(s.decode(t, v))
                fields[i] = (f, wire, raw)
            return w.serialize_message(fields)
    raise SystemExit(f"field {head}:{nth} not found")


def step(p):
    f, _, n = p.partition(":")
    return int(f), int(n or 1)


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
                        path = [step(p) for p in edits[i].split(".")]
                        wire, raw = s.encode(edits[i + 1], edits[i + 2])
                        old = []
                        payloads[0] = set_path(payloads[0], path, wire, raw, old)
                        print(f"record {record} field {edits[i]}: {old[0]} -> {edits[i + 2]}")
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)
    if not found:
        raise SystemExit(f"no record {record}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:])
