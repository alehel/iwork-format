# 0397: Header field 2.6, the data a payload uses

**Status:** run

Some record headers have a field 2.6 whose meaning wasn't known ([0001](0001-empty-document.md), [0396](0396-writing-record-headers.md)). This experiment surveys where it appears, compares its values with the data IDs in `Metadata.iwa`, and writes it.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | Every sample document on this machine for the survey; `samples/0023/image.pages` for writing: a red 8 × 4 PNG, data ID 24, in image record 1732647, whose header has 2.6 = 24 |
| Writer | [`recipes/0396-record-header.py`](../recipes/0396-record-header.py); exported and saved with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) |

## Recipe

The survey read every payload message in every record header of the samples, and for each document the data IDs in `Metadata.iwa` record 2, field 4.1 ([container.md](../spec/container.md#data-files)). Then:

```bash
mkdir -p samples/0397
R=recipes/0396-record-header.py
F=samples/0023/image.pages
O=samples/0397
cp $F $O/original.pages
python3 -I $R $F $O/image-no-data-refs.pages 1732647 1 6 -
python3 -I $R $F $O/image-other-data-ref.pages 1732647 1 6 8
for f in original image-no-data-refs image-other-data-ref; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF
save d in POSIX file \"$PWD/$O/$f-saved.pages\""
  swift recipes/0384-pdf-colours.swift $O/$f.pdf 291,400
done
```

Data ID 8 is one of the template's background images, which the document lists but doesn't store.

## Observation

Field 2.6 appears in the headers of records of types 4 (a slide node), 9, 10, 26, 2023 (a list style), 3005 (an image), 3007 (a sound or movie), 10001 and 12009, as packed varints. In 952 documents, all 23,373 values are data IDs that the document lists. Examples from `image.pages`:

| Record | Type | 2.6 | Data |
| --- | --- | --- | --- |
| 1732647 | 3005, the image | 24 | `red-8x4.png` |
| 1731484 | 2023, a list style | 23, nine times | `bullet_circle-blk-resize.pdf`, the bullet image, once per level |
| 1731489 | 2023 | 14, twice | another bullet image |
| 1731480 | 10001 | 8, 9, 9, 9, 9, 9 | the template's paper textures |

Writing it:

| File | Image's 2.6 written | Drawn | Saved copy's `Data/` | Saved copy's 2.6 |
| --- | --- | --- | --- | --- |
| `original.pages` | 24 | red | `red-8x4-24.png` | 24 |
| `image-no-data-refs.pages` | removed | red | `red-8x4-24.png` | 24 |
| `image-other-data-ref.pages` | 8 | red | `red-8x4-24.png` | 24 |

## Conclusion

Field 2.6 lists the data files a payload uses, by data ID, once for each place in the payload that names one, much as 2.5 lists the objects it refers to. Pages doesn't rely on it: the image is drawn and kept on saving whatever 2.6 says, and on saving Pages writes 2.6 again from the payload. A reader can use it to find the files a record needs without decoding the payload, and a writer should fill it as Pages does.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `original.pages` | `0023/image.pages` | `same bytes`, `header 3005#1732647 6 = x"18"`, `part Data/red-8x4-24.png: present → present` | *Control*: 2.6 is 24, the data ID of the image's file |
| `image-no-data-refs.pages` | `original.pages` | Only `header 3005#1732647 6: x"18" → absent` | *Likely*: field 2.6 isn't read when opening: the image is red |
| `image-other-data-ref.pages` | `original.pages` | Only `header 3005#1732647 6: x"18" → x"08"` | *Likely*: as above |
| `original-saved.pages` | `original.pages` | `header 3005#1732647 6 = x"18"`, `part Data/red-8x4-24.png: same` | *Control*: Pages keeps 24 on saving |
| `image-no-data-refs-saved.pages` | `image-no-data-refs.pages` | `header 3005#1732647 6: absent → x"18"`, `part Data/red-8x4-24.png: same` | *Confirmed*: Pages writes 2.6 again on saving |
| `image-other-data-ref-saved.pages` | `image-other-data-ref.pages` | `header 3005#1732647 6: x"08" → x"18"`, `part Data/red-8x4-24.png: same` | *Confirmed*: as above |

## Confidence

*Confirmed*: header field 2.6 as the data IDs the payload uses, against every sample, and that Pages rebuilds it on saving. *Likely*: Pages doesn't read it when opening.
