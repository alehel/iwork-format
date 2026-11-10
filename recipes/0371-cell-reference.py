"""Experiment 0371: change a cell reference in a formula by writing its node.

Usage: python3 -I recipes/0371-cell-reference.py IN OUT RECORD N COL COL_ABS ROW ROW_ABS

RECORD is a formula list (type 6005). N counts the cell-reference nodes (node type 36) of its
first formula from 1. Field 26 of the node is the column and 27 the row; in each, field 1 is the
value and field 2 is 1 for absolute. A relative value is a zigzag-encoded offset from the
formula's cell, an absolute one the zigzag-encoded index (spec/text.md). COL and ROW are written
as given, already encoded. Everything else is re-encoded unchanged by the writer of 0287.
"""
import importlib.util
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("w", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


def axis(value, absolute):
    return w.serialize_message([(1, 0, w.write_varint(value)), (2, 0, w.write_varint(absolute))])


def main(src, dst, record, n, col, col_abs, row, row_abs):
    record, n = int(record), int(n)
    col, col_abs, row, row_abs = int(col), int(col_abs), int(row), int(row_abs)

    def nodes(payload):
        out, seen = [], 0
        for f, t, v in w.parse_message(payload):
            if f == 1:
                fs = w.parse_message(v)
                if any(k == 1 and w.read_varint(x, 0)[0] == 36 for k, _, x in fs):
                    seen += 1
                    if seen == n:
                        fs = [(k, tt, axis(col, col_abs) if k == 26 else axis(row, row_abs) if k == 27 else x)
                              for k, tt, x in fs]
                        v = w.serialize_message(fs)
            out.append((f, t, v))
        if seen < n:
            raise SystemExit(f"only {seen} reference nodes")
        return w.serialize_message(out)

    def step(payload, path):
        out, done = [], False
        for f, t, v in w.parse_message(payload):
            if not done and f == path[0]:
                v = nodes(v) if len(path) == 1 else step(v, path[1:])
                done = True
            out.append((f, t, v))
        return w.serialize_message(out)

    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            data = zin.read(info)
            if info.filename.endswith(".iwa"):
                recs = w.records(w.iwa_decode(data))
                for header, payloads in recs:
                    if w.record_id(header) == record:
                        payloads[0] = step(payloads[0], [3, 5, 1])
                        print(f"record {record}: reference {n} set to column {col} ({col_abs}), row {row} ({row_abs})")
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)


if __name__ == "__main__":
    main(*sys.argv[1:9])
