"""Experiment 0431: set or clear the UTF-8 flag (general purpose bit 11) on every entry of a ZIP.

Usage: python3 -I recipes/0431-zip-utf8-flag.py IN OUT (set | clear)

Copies IN to OUT byte for byte, changing only bit 11 (0x800) of the flags in each local file header
and central directory header. The names' bytes are left as they are. Only the standard library is
used; the ZIP layout follows the public specification (APPNOTE.TXT).
"""
import struct
import sys


def main(src, dst, mode):
    data = bytearray(open(src, "rb").read())
    changed = 0
    for sig, flag_at in ((b"PK\x03\x04", 6), (b"PK\x01\x02", 8)):
        i = data.find(sig)
        while i != -1:
            (flags,) = struct.unpack_from("<H", data, i + flag_at)
            new = flags | 0x800 if mode == "set" else flags & ~0x800
            if new != flags:
                struct.pack_into("<H", data, i + flag_at, new)
                changed += 1
            i = data.find(sig, i + 4)
    open(dst, "wb").write(data)
    print(f"{mode}: {changed} headers changed")


if __name__ == "__main__":
    main(*sys.argv[1:4])
