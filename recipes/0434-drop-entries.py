"""Experiment 0434: copy a document's ZIP, leaving out the named entries.

Usage: python3 -I recipes/0434-drop-entries.py IN OUT NAME [NAME ...]

NAME is a ZIP entry name; a name ending in `*` drops every entry that starts with it. Everything
else is copied byte for byte. Only the standard library is used.
"""
import sys
import zipfile


def main(src, dst, *names):
    def dropped(n):
        return any(n == x or (x.endswith("*") and n.startswith(x[:-1])) for x in names)

    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            if dropped(info.filename):
                print("dropped", info.filename)
                continue
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), zin.read(info))


if __name__ == "__main__":
    main(*sys.argv[1:])
