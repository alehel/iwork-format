# 0432: Writing compressed ZIP entries

**Status:** run

A document's ZIP entries are stored without ZIP compression ([0001](0001-empty-document.md), [0002](0002-one-word.md)); the `.iwa` parts are compressed inside with Snappy instead. This experiment asks whether Pages also opens a document whose entries use ZIP's Deflate method.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0023/image.pages`: the body `one` and a red PNG, 91,240 bytes, all 14 entries (first written as 13) stored |
| Writer | The new [`recipes/0432-zip-compress.py`](../recipes/0432-zip-compress.py); opened with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0384-pdf-colours.swift`](../recipes/0384-pdf-colours.swift) |

## Recipe

```bash
mkdir -p samples/0432
O=samples/0432
cp samples/0023/image.pages $O/original.pages
for w in all iwa data; do
  python3 -I recipes/0432-zip-compress.py $O/original.pages $O/deflate-$w.pages $w
  sh recipes/0372-in-app.sh Pages $O/deflate-$w.pages "export d to POSIX file \"$PWD/$O/deflate-$w.pdf\" as PDF
return {body text of d, file name of image 1 of d}"
  swift recipes/0384-pdf-colours.swift $O/deflate-$w.pdf 291,400
done
```

## Observation

| File | Entries deflated | Size | Pages |
| --- | --- | --- | --- |
| `original.pages` | none | 91,240 | |
| `deflate-iwa.pages` | the `.iwa` parts | 62,171 | opens: `one`, `red-8x4.png`, drawn red |
| `deflate-data.pages` | `Data/` | 91,116 | opens: `one`, `red-8x4.png`, drawn red |
| `deflate-all.pages` | every entry | 48,586 | opens: `one`, `red-8x4.png`, drawn red |

No alert was shown.

## Conclusion

Pages reads Deflate-compressed entries as well as stored ones, for the parts, the data files and everything else. It stores its own uncompressed, but a writer may compress: here that halved the file, since the `.iwa` parts' Snappy blocks and the previews compress further. A reader must handle both methods.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `original.pages` | `0023/image.pages` | `same bytes` | *Control*: every entry is stored |
| `deflate-iwa.pages` | `original.pages` | Only the .iwa parts deflated instead of stored: `same records`, `same parts` | *Confirmed*: Pages opens it and draws the image |
| `deflate-data.pages` | `original.pages` | Only the data file deflated instead of stored: `same records`, `same parts` | *Confirmed*: Pages opens it and draws the image |
| `deflate-all.pages` | `original.pages` | Only every entry deflated instead of stored: `same records`, `same parts` | *Confirmed*: Pages opens it and draws the image |

## Confidence

*Confirmed*: Pages opens documents whose ZIP entries are Deflate-compressed, by writing them.
