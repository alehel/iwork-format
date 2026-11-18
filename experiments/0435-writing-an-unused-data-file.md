# 0435: Writing a data file that nothing uses

**Status:** run

Files nothing uses are dropped on save ([0145](0145-deleted-image.md)): when an image was deleted, its file and its entry in `Metadata.iwa` record 2 went with it. This experiment adds a file that no record uses, with and without an entry, and has Pages save the document.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0023/image.pages`: one image, data ID 24, stored as `Data/red-8x4-24.png`; record 2 lists data IDs 8, 9, 14, 23 (the template's resources) and 24. The added file is the green 8 × 4 PNG of [0395](0395-writing-a-data-file.md) |
| Writer | The new [`recipes/0435-add-data.py`](../recipes/0435-add-data.py); saved with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) |

## Recipe

```bash
mkdir -p samples/0435
O=samples/0435
cp samples/0395/green-8x4.png $O/green.png
python3 -I recipes/0435-add-data.py samples/0023/image.pages $O/extra-listed.pages 99 $O/green.png
python3 -I recipes/0435-add-data.py samples/0023/image.pages $O/extra-unlisted.pages 99 $O/green.png --no-entry
for f in extra-listed extra-unlisted; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages "save d in POSIX file \"$PWD/$O/$f-saved.pages\""
  unzip -l $O/$f-saved.pages | grep Data/
done
```

Both written files store `Data/green-99.png`; `extra-listed.pages` also lists it in record 2 as data ID 99 with its SHA-1 and names.

## Observation

| File | Written | Opens | Saved copy's `Data/` | Saved copy's data IDs |
| --- | --- | --- | --- | --- |
| `extra-listed.pages` | file and entry 99 | yes, `one` | `red-8x4-24.png` | 8, 9, 14, 23, 24 |
| `extra-unlisted.pages` | file only | yes, `one` | `red-8x4-24.png` | 8, 9, 14, 23, 24 |

## Conclusion

Pages opens a document with data nothing uses, listed or not, and drops it when it saves: both the file and its entry are gone. What it keeps is what the records use, as listed in their headers' field 2.6 ([0397](0397-the-data-references-field.md)) and the template's resources. So a reader can ignore files no record names, and a writer doesn't need to tidy up after itself for Pages' sake.

## Confidence

*Confirmed*: Pages drops unused data files and their entries on saving, and opens documents that have them, by writing them.
