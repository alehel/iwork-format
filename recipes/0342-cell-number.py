"""Experiment 0342: write an integer into a number cell's decimal128.

Usage: python3 -I recipes/0342-cell-number.py IN OUT ROW COLUMN VALUE

ROW and COLUMN count from 0. The cell must have flag 0x1. Its decimal128 becomes VALUE with
exponent 0: the coefficient in the low 14 bytes, then 0x40 0x30 (0x40 0xB0 when negative, the
sign bit set). Everything else is re-encoded unchanged with the writer of experiment 0287.
"""
import importlib.util
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("w", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


def main(src, dst, row, col, value):
    row, col, value = int(row), int(col), int(value)
    dec = abs(value).to_bytes(14, "little") + bytes([0x40, 0xB0 if value < 0 else 0x30])
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            data = zin.read(info)
            if info.filename.endswith(".iwa"):
                recs = w.records(w.iwa_decode(data))
                if info.filename == "Index/Tables/Tile.iwa":
                    header, payloads = recs[0]
                    tile = []
                    for f, t, v in w.parse_message(payloads[0]):
                        if f == 5:
                            entry = w.parse_message(v)
                            d = {k: x for k, _, x in entry}
                            if w.read_varint(d[1], 0)[0] == row:
                                offs = d[7 if 7 in d else 4]
                                start = int.from_bytes(offs[2 * col:2 * col + 2], "little")
                                cells = bytearray(d[6])
                                if not int.from_bytes(cells[start + 8:start + 12], "little") & 0x1:
                                    raise SystemExit(f"cell {row},{col} has no decimal128")
                                cells[start + 12:start + 28] = dec
                                print(f"cell {row},{col} -> {value}")
                                v = w.serialize_message([(k, tt, bytes(cells) if k == 6 else x) for k, tt, x in entry])
                        tile.append((f, t, v))
                    payloads[0] = w.serialize_message(tile)
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)


if __name__ == "__main__":
    main(*sys.argv[1:6])
