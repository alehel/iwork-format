"""Experiment 0290: change a number cell's value in a Numbers tile, with the writer of experiment 0287.

Usage: python3 -I recipes/0290-numbers-cell.py IN OUT OLD NEW
Finds the one decimal128 equal to the integer OLD (exponent 0) in Index/Tables/Tile.iwa and writes the
integer NEW in its place. Both must be small positive integers. The tile's record is re-encoded
with the 0287 writer; previews are left out.
"""
import importlib.util
import os
import sys
import zipfile

spec = importlib.util.spec_from_file_location("writer", os.path.join(os.path.dirname(__file__), "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


def dec128(n):
    # Coefficient in the low bits, exponent 0 (biased 6176, giving the top bytes 0x3040), sign 0.
    return n.to_bytes(14, "little") + bytes([0x40, 0x30])


src, dst, old, new = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
    for info in zin.infolist():
        if info.filename.startswith("preview"):
            continue
        data = zin.read(info)
        if info.filename == "Index/Tables/Tile.iwa":
            raw = w.iwa_decode(data)
            if raw.count(dec128(old)) != 1:
                raise SystemExit(f"{old} isn't found exactly once")
            data = w.iwa_encode(raw.replace(dec128(old), dec128(new)))
        zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)
