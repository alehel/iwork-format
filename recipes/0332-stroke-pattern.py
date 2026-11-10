"""Experiment 0332: give a shape's stroke a dash pattern by writing its style.

Usage: python3 -I recipes/0332-stroke-pattern.py IN OUT STYLE_ID LENGTH [LENGTH ...]

In the shape style STYLE_ID, the stroke's pattern (1.11.2.6) becomes a dash (field 1 = 0) with
the given number of lengths (field 3) filling the first of its six length slots (field 4).
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


def at(b, path, fn):
    out = []
    for f, t, v in w.parse_message(b):
        if f == path[0] and t == 2:
            v = fn(v) if len(path) == 1 else at(v, path[1:], fn)
        out.append((f, t, v))
    return w.serialize_message(out)


def main(src, dst, style, lengths):
    style, lengths = int(style), [float(x) for x in lengths]

    def pattern(v):
        fields = w.parse_message(v)
        slots = [x for f, _, x in fields if f == 4]
        slots = [struct.pack("<f", x) for x in lengths] + slots[len(lengths):]
        out = [(1, 0, w.write_varint(0))]
        out += [(f, t, x) for f, t, x in fields if f == 2]
        out += [(3, 0, w.write_varint(len(lengths)))]
        out += [(4, 5, x) for x in slots]
        out += [(f, t, x) for f, t, x in fields if f not in (1, 2, 3, 4)]
        print(f"pattern: dash, lengths {lengths}")
        return w.serialize_message(out)

    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            data = zin.read(info)
            if info.filename.endswith(".iwa"):
                recs = w.records(w.iwa_decode(data))
                for header, payloads in recs:
                    if w.record_id(header) == style:
                        payloads[0] = at(payloads[0], [1, 11, 2, 6], pattern)
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:])
