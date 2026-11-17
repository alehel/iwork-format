# 0395: Renaming and replacing a data file

**Status:** run

Embedded files are stored under `Data/`, named after the original file with the data ID before the extension, and `Metadata.iwa` record 2 lists them in its repeated field 4: the data ID (field 1), the file's SHA-1 (field 2), the original file name (field 3) and the stored file name (field 4) ([0023](0023-an-image.md)). This experiment renames the stored file, with and without its entry, changes the original name, and replaces the file's bytes.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0023/image.pages`: a red 8 × 4 PNG at (287, 398), data ID 24, stored as `Data/red-8x4-24.png`, original name `red-8x4.png` |
| Writer | The new [`recipes/0395-data-file.py`](../recipes/0395-data-file.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0384-pdf-colours.swift`](../recipes/0384-pdf-colours.swift) |

## Recipe

```bash
mkdir -p samples/0395
R=recipes/0395-data-file.py
F=samples/0023/image.pages
O=samples/0395
cp $F $O/original.pages
python3 -I $R $F $O/stored-renamed.pages 24 --store picture.png
python3 -I $R $F $O/stored-renamed-listed.pages 24 --store picture.png --list
python3 -I $R $F $O/original-name.pages 24 --original holiday.png
python3 -I $R $F $O/replaced.pages 24 --replace $O/green-8x4.png
for f in original stored-renamed stored-renamed-listed original-name replaced; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF
return {file name of image 1 of d, position of image 1 of d}"
  swift recipes/0384-pdf-colours.swift $O/$f.pdf 291,400
done
```

`green-8x4.png` is an 8 × 4 PNG of pure green, written with Python's standard library. Replacing it leaves the entry, and so the SHA-1 of the red file, unchanged.

## Observation

| File | Written | `file name` | Colour at the image's centre | Alert |
| --- | --- | --- | --- | --- |
| `original.pages` | nothing | red-8x4.png | 1, 0, 0 | |
| `stored-renamed.pages` | file renamed to `picture.png` | red-8x4.png | 0.51, 0.51, 0.51 | a document warning |
| `stored-renamed-listed.pages` | file renamed, and field 4 = `picture.png` | red-8x4.png | 1, 0, 0 | |
| `original-name.pages` | field 3 = `holiday.png` | holiday.png | 1, 0, 0 | |
| `replaced.pages` | the file's bytes now green | red-8x4.png | 0, 1, 0 | |

The image keeps its position and its size of 8 × 4 in every file.

## Conclusion

Pages finds a data file by the stored name in field 4 of its entry. The name needn't follow the `name-N.ext` pattern: `picture.png` works once the entry says so, and without it the image is drawn as a grey placeholder and Pages warns about the document. Field 3 is only the original name, which AppleScript reports as `file name`. The SHA-1 in field 2 isn't checked when opening: a file with other bytes is drawn as it is. A writer should still keep the SHA-1 right, since Pages uses it to store identical files once ([0142](0142-same-image-twice.md)).

## Confidence

*Confirmed*: field 4 of a data entry as the stored file name Pages uses, and field 3 as the original name, by writing them. *Likely*: the SHA-1 isn't checked on opening.
