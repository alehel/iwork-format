"""Experiment 0391: write one 32-bit key of a table cell, chosen by its flag bit.

Usage: python3 -I recipes/0391-cell-key.py IN OUT ROW COLUMN FLAG VALUE

ROW and COLUMN count from 0; FLAG is a flag bit such as 0x100. A cell's bytes 8-11 are its flags,
and the values and keys follow from byte 12 in the order of their bits (spec/text.md). This recipe
handles cells whose only value is a decimal128 (flag 0x1, 16 bytes) and whose other bits from 0x80
up are 4-byte keys; it refuses any other cell. Everything else is re-encoded unchanged with the
writer of experiment 0287.
"""
import importlib.util
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("w", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


def key_offset(flags, flag):
    if flags & 0x7E or not flags & flag:
        raise SystemExit(f"flags {flags:#x}: not a cell this recipe handles for {flag:#x}")
    at = 12 + (16 if flags & 0x1 else 0)
    bit = 0x80
    while bit < flag:
        if flags & bit:
            at += 4
        bit <<= 1
    return at


def main(src, dst, row, col, flag, value):
    row, col, flag, value = int(row), int(col), int(flag, 0), int(value)
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
                                flags = int.from_bytes(cells[start + 8:start + 12], "little")
                                at = start + key_offset(flags, flag)
                                old = int.from_bytes(cells[at:at + 4], "little")
                                cells[at:at + 4] = value.to_bytes(4, "little")
                                print(f"cell {row},{col} key {flag:#x}: {old} -> {value}")
                                v = w.serialize_message([(k, tt, bytes(cells) if k == 6 else x) for k, tt, x in entry])
                        tile.append((f, t, v))
                    payloads[0] = w.serialize_message(tile)
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)


if __name__ == "__main__":
    main(*sys.argv[1:7])
