"""Experiment 0482: write an 8 x 4 pixel PNG of solid blue, as recipes/0023-image.py writes red.

Usage: python3 -I recipes/0482-blue.py /absolute/path/blue-8x4.png
"""
import struct, sys, zlib

def chunk(kind, data):
    body = kind + data
    return struct.pack(">I", len(data)) + body + struct.pack(">I", zlib.crc32(body) & 0xFFFFFFFF)

width, height = 8, 4
rows = b"".join(b"\x00" + b"\x00\x00\xff" * width for _ in range(height))
png = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
png += chunk(b"IDAT", zlib.compress(rows)) + chunk(b"IEND", b"")
with open(sys.argv[1], "wb") as f:
    f.write(png)
