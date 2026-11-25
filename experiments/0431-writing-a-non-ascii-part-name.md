# 0431: Writing a non-ASCII name into the ZIP

**Status:** run

ZIP entry names in iWork documents are UTF-8, but Pages doesn't set the ZIP flag that says so (general purpose bit 11), so a reader should read them as UTF-8 regardless ([0144](0144-non-ascii-file-name.md)). This experiment gives an image's data file a name with non-ASCII letters, with the flag set and cleared.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0023/image.pages`: a red 8 × 4 PNG, data ID 24, stored as `Data/red-8x4-24.png` |
| Writer | [`recipes/0395-data-file.py`](../recipes/0395-data-file.py) for the name and the new [`recipes/0431-zip-utf8-flag.py`](../recipes/0431-zip-utf8-flag.py) for the flag; exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0384-pdf-colours.swift`](../recipes/0384-pdf-colours.swift) |

## Recipe

```bash
mkdir -p samples/0431
O=samples/0431
cp samples/0023/image.pages $O/original.pages
python3 -I recipes/0395-data-file.py $O/original.pages $O/blabaer-flag-set.pages 24 --store "blåbær.png" --list
python3 -I recipes/0431-zip-utf8-flag.py $O/blabaer-flag-set.pages $O/blabaer-flag-clear.pages clear
for f in original blabaer-flag-set blabaer-flag-clear; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF"
  swift recipes/0384-pdf-colours.swift $O/$f.pdf 291,400
done
```

Python's `zipfile` writes a non-ASCII name as UTF-8 and sets the flag. `recipes/0431-zip-utf8-flag.py` then clears it in the local and central headers, leaving the name's bytes alone.

## Observation

| File | Entry name, as Python reads it | Flag | Image drawn |
| --- | --- | --- | --- |
| `original.pages` | `Data/red-8x4-24.png` | clear | red |
| `blabaer-flag-set.pages` | `Data/blåbær.png` | set | red |
| `blabaer-flag-clear.pages` | `Data/bl├Ñb├ªr.png` | clear | red |

With the flag clear, Python decodes the same bytes as code page 437, as the ZIP specification says it should.

## Conclusion

Pages reads ZIP entry names as UTF-8 whether or not the flag is set: it found `blåbær.png` both ways, matching the name in `Metadata.iwa`, which is UTF-8 text. A reader that follows the ZIP specification strictly would get the wrong name when the flag is clear, as Pages leaves it, so it should decode names as UTF-8 regardless, as the spec says.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `original.pages` | `0023/image.pages` | `same bytes` | *Control*: the image is drawn |
| `blabaer-flag-set.pages` | `original.pages` | Only `11006#2 4.4: "red-8x4-24.png" → "blåbær.png"`, `part Data/red-8x4-24.png: present → absent`, `part Data/blåbær.png: absent → present` | *Confirmed*: Pages finds the image by its UTF-8 name with the flag set |
| `blabaer-flag-clear.pages` | `blabaer-flag-set.pages` | Only the UTF-8 flag cleared: `same records`, `same parts` | *Confirmed*: Pages reads the name as UTF-8 with the flag clear too |

## Confidence

*Confirmed*: Pages reads ZIP entry names as UTF-8 with or without the UTF-8 flag, by writing one.
