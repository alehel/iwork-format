"""Experiment 0433: re-encode every .iwa part with chunks of a chosen decoded size.

Usage: python3 -I recipes/0433-chunk-size.py IN OUT SIZE

Each part's decoded bytes are cut into pieces of SIZE bytes (the last may be shorter), each written
as one chunk holding a literal-only Snappy block, as the writer of experiment 0287 does with 65,536.
The 3-byte chunk length limits a chunk to 16,777,215 bytes. Everything else is unchanged.
"""
import importlib.util
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("w", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


def main(src, dst, size):
    size = int(size)
    biggest = 0
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            data = zin.read(info)
            if info.filename.endswith(".iwa"):
                raw = w.iwa_decode(data)
                out = bytearray()
                for start in range(0, len(raw), size):
                    block = w.snappy_encode_literals(raw[start:start + size])
                    out += b"\x00" + len(block).to_bytes(3, "little") + block
                biggest = max(biggest, min(size, len(raw)))
                data = bytes(out)
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)
    print(f"chunks of up to {size} bytes; the largest chunk decodes to {biggest}")


if __name__ == "__main__":
    main(*sys.argv[1:4])
