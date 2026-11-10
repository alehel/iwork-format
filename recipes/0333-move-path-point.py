"""Experiment 0333: move one point of an editable shape's path by writing it.

Usage: python3 -I recipes/0333-move-path-point.py IN OUT SHAPE_ID INDEX X Y

In shape SHAPE_ID (type 2011), the INDEX-th point (from 0) of the editable path 1.3.8.1.1 gets
X and Y in fields 1, 2 and 3 (the point and both of its control points). Coordinates are in the
path's own space, whose natural size is in 1.3.8.2. Everything else is re-encoded unchanged with
the writer of experiment 0287.
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


def at(b, path, fn):
    out = []
    for f, t, v in w.parse_message(b):
        if f == path[0] and t == 2:
            v = fn(v) if len(path) == 1 else at(v, path[1:], fn)
        out.append((f, t, v))
    return w.serialize_message(out)


def main(src, dst, shape, index, x, y):
    shape, index, x, y = int(shape), int(index), float(x), float(y)
    xy = w.serialize_message([(1, 5, struct.pack("<f", x)), (2, 5, struct.pack("<f", y))])

    def points(v):
        out, i = [], -1
        for f, t, pv in w.parse_message(v):
            if f == 1:
                i += 1
                if i == index:
                    pv = w.serialize_message([(k, kt, xy if k in (1, 2, 3) else kv) for k, kt, kv in w.parse_message(pv)])
                    print(f"point {index} -> ({x}, {y})")
            out.append((f, t, pv))
        return w.serialize_message(out)

    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            data = zin.read(info)
            if info.filename.endswith(".iwa"):
                recs = w.records(w.iwa_decode(data))
                for header, payloads in recs:
                    if w.record_id(header) == shape:
                        payloads[0] = at(payloads[0], [1, 3, 8, 1], points)
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)


if __name__ == "__main__":
    main(*sys.argv[1:7])
