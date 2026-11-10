"""Experiment 0317: change a chart's type and one of its values by writing.

Usage: python3 -I recipes/0317-chart-data.py IN OUT ROW COLUMN VALUE [TYPE]

In the chart drawable (type 5021), the value at ROW and COLUMN (from 0) of the data grid in
10000.7.3 becomes VALUE, a double, and the chart type 10000.1 becomes TYPE if given. Everything
else is re-encoded unchanged with the writer of experiment 0287.
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


def record_type(header):
    return w.read_varint({f: v for f, _, v in w.parse_message({f: v for f, _, v in header}[2])}[1], 0)[0]


def main(src, dst, row, col, value, kind=None):
    row, col, value = int(row), int(col), float(value)
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            data = zin.read(info)
            if info.filename.endswith(".iwa"):
                recs = w.records(w.iwa_decode(data))
                for header, payloads in recs:
                    if record_type(header) != 5021:
                        continue
                    top = []
                    for f, t, v in w.parse_message(payloads[0]):
                        if f == 10000:
                            chart = []
                            r = -1
                            for cf, ct, cv in w.parse_message(v):
                                if cf == 1 and kind is not None:
                                    print(f"type {w.read_varint(cv, 0)[0]} -> {kind}")
                                    cv = w.write_varint(int(kind))
                                if cf == 7:
                                    grid = []
                                    for gf, gt, gv in w.parse_message(cv):
                                        if gf == 3:
                                            r += 1
                                            if r == row:
                                                cells, c = [], -1
                                                for vf, vt, vv in w.parse_message(gv):
                                                    if vf == 1:
                                                        c += 1
                                                        if c == col:
                                                            old = struct.unpack("<d", {k: x for k, _, x in w.parse_message(vv)}[1])[0]
                                                            vv = w.serialize_message([(1, 1, struct.pack("<d", value))])
                                                            print(f"row {row} column {col}: {old} -> {value}")
                                                    cells.append((vf, vt, vv))
                                                gv = w.serialize_message(cells)
                                        grid.append((gf, gt, gv))
                                    cv = w.serialize_message(grid)
                                chart.append((cf, ct, cv))
                            v = w.serialize_message(chart)
                        top.append((f, t, v))
                    payloads[0] = w.serialize_message(top)
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)


if __name__ == "__main__":
    main(*sys.argv[1:7])
