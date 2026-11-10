"""Experiment 0338: change a boolean cell's value by writing its bytes.

Usage: python3 -I recipes/0338-cell-double.py IN OUT ROW COLUMN VALUE

ROW and COLUMN count from 0. The cell must have flag 0x2. Its value, a little-endian double
(1.0 true and 0.0 false for a boolean, spec/text.md), becomes VALUE. It follows the cell's
12-byte prefix, after a decimal128 (flag 0x1, 16 bytes) if there is one. Everything else is
re-encoded unchanged with the writer of experiment 0287.
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


def main(src, dst, row, col, value):
    row, col, value = int(row), int(col), float(value)
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            data = zin.read(info)
            if info.filename == "Index/Tables/Tile.iwa":
                recs = w.records(w.iwa_decode(data))
                header, payloads = recs[0]
                tile = []
                for f, t, v in w.parse_message(payloads[0]):
                    if f == 5:
                        entry = w.parse_message(v)
                        d = {k: x for k, _, x in entry}
                        if w.read_varint(d[1], 0)[0] == row:
                            offs_field = 7 if 7 in d else 4
                            offs = d[offs_field]
                            starts = [int.from_bytes(offs[i:i + 2], "little") for i in range(0, len(offs), 2)]
                            start = starts[col]
                            cells = bytearray(d[6])
                            flags = int.from_bytes(cells[start + 8:start + 12], "little")
                            if not flags & 0x2:
                                raise SystemExit(f"cell {row},{col} has no double (flags {flags:#x})")
                            at = start + 12 + (16 if flags & 0x1 else 0)
                            old = struct.unpack("<d", cells[at:at + 8])[0]
                            cells[at:at + 8] = struct.pack("<d", value)
                            print(f"cell {row},{col}: {old} -> {value}")
                            v = w.serialize_message([(k, tt, bytes(cells) if k == 6 else x) for k, tt, x in entry])
                    tile.append((f, t, v))
                payloads[0] = w.serialize_message(tile)
                data = w.iwa_encode(w.encode_records(recs))
            elif info.filename.endswith(".iwa"):
                data = w.iwa_encode(w.encode_records(w.records(w.iwa_decode(data))))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)


if __name__ == "__main__":
    main(*sys.argv[1:6])
