"""Experiment 0438: turn a ZIP document into the folder form (a package).

Usage: python3 -I recipes/0438-to-package.py IN.pages OUT.pages

OUT becomes a folder: the entries under Index/ go into OUT/Index.zip under their own names (stored,
as in a ZIP document), entries under Data/ into OUT/Data/, and every other entry, such as the
Metadata/ files and the previews, into OUT at its own path. Only the standard library is used.
"""
import os
import sys
import zipfile


def main(src, dst):
    os.makedirs(os.path.join(dst, "Data"), exist_ok=True)
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(os.path.join(dst, "Index.zip"), "w", zipfile.ZIP_STORED) as idx:
        for info in zin.infolist():
            data = zin.read(info)
            if info.filename.startswith("Index/"):
                idx.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)
            else:
                path = os.path.join(dst, info.filename)
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, "wb") as f:
                    f.write(data)
    print(f"{dst}: package written")


if __name__ == "__main__":
    main(*sys.argv[1:3])
