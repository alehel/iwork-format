# 0438: Writing a document as a package

**Status:** run

A document can also be a folder, a package: the metadata files and previews are files in the folder, the `.iwa` parts are inside an `Index.zip` in it under the same `Index/` names, and data files are in a `Data/` folder ([0076](0076-package-format.md)). This experiment builds a package from a ZIP document by that description alone and opens it.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0023/image.pages`: the body `one` and a red PNG, as a ZIP |
| Writer | The new [`recipes/0438-to-package.py`](../recipes/0438-to-package.py); opened with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh), which now also finds a package, whose path Pages reports with a trailing slash |

## Recipe

```bash
mkdir -p samples/0438
O=samples/0438
python3 -I recipes/0438-to-package.py samples/0023/image.pages $O/image-package.pages
sh recipes/0372-in-app.sh Pages $O/image-package.pages "export d to POSIX file \"$PWD/$O/image-package.pdf\" as PDF
return {body text of d, file name of image 1 of d}"
swift recipes/0384-pdf-colours.swift $O/image-package.pdf 291,400
```

## Observation

The package holds `Index.zip` (the seven parts, 72,080 bytes in all, stored; the file is 73,004), `Data/red-8x4-24.png`, `Metadata/` with its three files, and the three previews. Pages opened it as `image-package.pages` without an alert, with the body `one`, the image `red-8x4.png`, and the image drawn red at its place.

## Conclusion

The folder form works as described: a writer can produce a package by moving the `Index/` entries into `Index.zip`, the data files into `Data/` and the rest into the folder, with nothing else to change. The parts' names inside `Index.zip`, `Metadata.iwa`'s lists and the data names are the same in both forms.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `image-package.pages` | `0023/image.pages` | Only `part Index.zip: absent → present`, `same records`; a folder instead of a ZIP | *Confirmed*: the package layout; Pages opens it and draws the image |

## Confidence

*Confirmed*: the package layout, by writing one from a ZIP document.
