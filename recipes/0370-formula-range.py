"""Experiment 0370: change the range in a cell formula by writing its offsets.

Usage: python3 -I recipes/0370-formula-range.py IN OUT RECORD FIRST_COL LAST_COL [FIRST_ROW LAST_ROW]

RECORD is a formula list (type 6005). In the first range node (node type 67) of its first formula,
40.1 holds the first and last column and 40.2 the first and last row, as signed offsets from the
formula's own cell (spec/text.md). This writes the columns, and the rows if given. Everything else
is re-encoded unchanged by the writer of experiment 0287.
"""
import importlib.util
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("w", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


def signed(n):
    return w.write_varint(n if n >= 0 else n + (1 << 64))


def edit(fields, path, fn):
    """Apply fn to the message at the first occurrence of each step in path; return new bytes."""
    out, done = [], False
    for f, t, v in fields:
        if not done and f == path[0]:
            v = fn(v) if len(path) == 1 else edit(w.parse_message(v), path[1:], fn)
            done = True
        out.append((f, t, v))
    return w.serialize_message(out)


def main(src, dst, record, *bounds):
    record = int(record)
    bounds = [int(b) for b in bounds]

    def node(payload):
        # payload is the node list (field 3.5.1 of the formula list); find the first node with type 67
        out, done = [], False
        for f, t, v in w.parse_message(payload):
            fs = w.parse_message(v) if f == 1 else []
            if f == 1 and not done and any(k == 1 and w.read_varint(x, 0)[0] == 67 for k, _, x in fs):
                def ranges(r):
                    parts = []
                    for k, tt, x in w.parse_message(r):
                        if k == 1:
                            x = w.serialize_message([(1, 0, signed(bounds[0])), (2, 0, signed(bounds[1]))])
                        elif k == 2 and len(bounds) == 4:
                            x = w.serialize_message([(1, 0, signed(bounds[2])), (2, 0, signed(bounds[3]))])
                        parts.append((k, tt, x))
                    return w.serialize_message(parts)
                v = edit(fs, [40], ranges)
                done = True
            out.append((f, t, v))
        if not done:
            raise SystemExit("no range node")
        return w.serialize_message(out)

    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            data = zin.read(info)
            if info.filename.endswith(".iwa"):
                recs = w.records(w.iwa_decode(data))
                for header, payloads in recs:
                    if w.record_id(header) == record:
                        payloads[0] = edit(w.parse_message(payloads[0]), [3, 5, 1], node)
                        print(f"record {record}: range set to {bounds}")
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)


if __name__ == "__main__":
    main(*sys.argv[1:])
