"""Experiment 0364: shrink a Numbers table by writing its size.

Usage: python3 -I recipes/0364-table-size.py IN OUT ROWS COLUMNS

Writes ROWS and COLUMNS into the table model (type 6001, fields 6 and 7) and into the type-6305
record (fields 3 and 2). In the type-6267 record, which lists a UUID per column (field 1) and per
row (field 4), each with a pair of index maps (fields 2 and 3, 5 and 6), it keeps the first
COLUMNS and ROWS UUIDs and the map entries below those counts. Only shrinking is supported, since
growing would need new UUIDs. Everything else is re-encoded unchanged by the writer of 0287.
"""
import importlib.util
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("w", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


def rtype(header):
    info = {f: v for f, _, v in w.parse_message({a: b for a, _, b in header}[2])}
    return w.read_varint(info[1], 0)[0]


def setv(payload, values):
    out = [(f, t, w.write_varint(values[f]) if f in values else v) for f, t, v in w.parse_message(payload)]
    return w.serialize_message(out)


def trim(payload, rows, cols):
    keep = {1: cols, 4: rows}
    seen = {1: 0, 4: 0}
    out = []
    for f, t, v in w.parse_message(payload):
        if f in keep:
            seen[f] += 1
            if seen[f] > keep[f]:
                continue
        elif f in (2, 3) and w.read_varint(v, 0)[0] >= cols:
            continue
        elif f in (5, 6) and w.read_varint(v, 0)[0] >= rows:
            continue
        out.append((f, t, v))
    return w.serialize_message(out)


def main(src, dst, rows, cols):
    rows, cols = int(rows), int(cols)
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            data = zin.read(info)
            if info.filename.endswith(".iwa"):
                recs = w.records(w.iwa_decode(data))
                for header, payloads in recs:
                    t = rtype(header)
                    if t == 6001:
                        payloads[0] = setv(payloads[0], {6: rows, 7: cols})
                    elif t == 6305:
                        payloads[0] = setv(payloads[0], {3: rows, 2: cols})
                    elif t == 6267:
                        payloads[0] = trim(payloads[0], rows, cols)
                    else:
                        continue
                    print(f"record {w.record_id(header)} (type {t}) written")
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)


if __name__ == "__main__":
    main(*sys.argv[1:5])
