"""Experiment 0023: write a small PNG of known size and colour for Pages to place.

Usage: python3 recipes/0023-image.py /absolute/path/red-8x4.png
The image is 8 x 4 pixels of solid red (255, 0, 0), written from the public PNG specification.
"""
import struct, sys, zlib

def chunk(kind, data):
    body = kind + data
    return struct.pack(">I", len(data)) + body + struct.pack(">I", zlib.crc32(body) & 0xFFFFFFFF)

width, height = 8, 4
rows = b"".join(b"\x00" + b"\xff\x00\x00" * width for _ in range(height))
png = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
png += chunk(b"IDAT", zlib.compress(rows)) + chunk(b"IEND", b"")
with open(sys.argv[1], "wb") as f:
    f.write(png)
