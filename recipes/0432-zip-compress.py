"""Experiment 0432: rewrite a document's ZIP with some entries compressed.

Usage: python3 -I recipes/0432-zip-compress.py IN OUT (all | iwa | data | none)

Copies every entry's bytes unchanged, choosing ZIP's Deflate method for the entries named (all of
them, the .iwa parts, or those under Data/) and Store for the rest. Only the standard library is
used.
"""
import sys
import zipfile


def main(src, dst, which):
    def deflate(name):
        return which == "all" or (which == "iwa" and name.endswith(".iwa")) or (which == "data" and name.startswith("Data/"))

    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w") as zout:
        for info in zin.infolist():
            out = zipfile.ZipInfo(info.filename, date_time=info.date_time)
            out.compress_type = zipfile.ZIP_DEFLATED if deflate(info.filename) else zipfile.ZIP_STORED
            zout.writestr(out, zin.read(info))
    print(f"{which}: written")


if __name__ == "__main__":
    main(*sys.argv[1:4])
