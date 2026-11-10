"""Experiment 0298: turn on a chart's title and legend by writing its settings record.

Usage: python3 -I recipes/0298-chart-switches.py IN OUT [title] [legend]

Finds the chart drawable (type 5021), follows its field 10000.10 to its settings record (type
5023), and sets 10000.21 = 1 for the title and 10000.20 = 1 for the legend, as found in
experiment 0295. Everything else is re-encoded unchanged, using the writer of experiment 0287.
"""
import importlib.util
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("w", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


def fields(b):
    return {f: v for f, _, v in w.parse_message(b)}


def record_type(header):
    return w.read_varint(fields({f: v for f, _, v in header}[2])[1], 0)[0]


def set_varints(payload, field, values):
    """Set varint subfields of a message subfield, adding the subfield if it's missing."""
    out, done = [], False
    for f, t, v in w.parse_message(payload):
        if f == field and t == 2:
            inner = [(k, wt, vv) for k, wt, vv in w.parse_message(v) if k not in values]
            inner += [(k, 0, w.write_varint(n)) for k, n in sorted(values.items())]
            v = w.serialize_message(inner)
            done = True
        out.append((f, t, v))
    if not done:
        out.append((field, 2, w.serialize_message([(k, 0, w.write_varint(n)) for k, n in sorted(values.items())])))
    return w.serialize_message(out)


def main(src, dst, wanted):
    values = {}
    if "title" in wanted:
        values[21] = 1
    if "legend" in wanted:
        values[20] = 1
    with zipfile.ZipFile(src) as zin:
        parts = {i.filename: (i, zin.read(i)) for i in zin.infolist()}
    decoded = {n: w.records(w.iwa_decode(d)) for n, (_, d) in parts.items() if n.endswith(".iwa")}
    settings = None
    for recs in decoded.values():
        for header, payloads in recs:
            if record_type(header) == 5021:
                ref = fields(fields(payloads[0])[10000])[10]
                settings = w.read_varint(fields(ref)[1], 0)[0]
    changed = 0
    for recs in decoded.values():
        for header, payloads in recs:
            if w.record_id(header) == settings and record_type(header) == 5023:
                payloads[0] = set_varints(payloads[0], 10000, values)
                changed += 1
    with zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for name, (info, data) in parts.items():
            if name in decoded:
                data = w.iwa_encode(w.encode_records(decoded[name]))
            zout.writestr(zipfile.ZipInfo(name, date_time=info.date_time), data)
    print(f"settings record {settings}: {changed} changed, set {values}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], set(sys.argv[3:]))
