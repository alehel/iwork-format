# 0023: An image

**Status:** run

This experiment places a small image of known size and content on a page, to see where Pages keeps the image file and how a record refers to it.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `plain.pages`: the body text `one`, made by the [0002](0002-one-word.md) recipe |

## Recipe

```bash
mkdir -p samples/0023
python3 recipes/0023-image.py "$PWD/samples/0023/red-8x4.png"
osascript recipes/0023-image.applescript "$PWD/samples/0023/image.pages" "$PWD/samples/0023/red-8x4.png"
osascript recipes/0002-one-word.applescript "$PWD/samples/0023/plain.pages" one
```

`recipes/0023-image.py` writes an 8 × 4 pixel PNG of solid red, 75 bytes, from the public PNG specification. Its SHA-1 is `9386b0525252e1123578796d7d71d976c2228023`. The AppleScript sets the body text to `one`, then asks Pages to make an image from the file on page 1. Pages only accepted `make new image` when told to make it on a page. Asking the document failed with error −2763.

## Observation

### The file

`image.pages` has one part more than `plain.pages`: `Data/red-8x4-24.png`, 75 bytes, byte-for-byte the PNG that was placed. Its name is the original name with `-24` before the extension.

### The image record

`Document.iwa` gained a record of type 3005 (1732647) and two of type 3097. Record 1732647:

```
1.1.1: { 1: 286.8, 2: 397.6 }        position, floats
1.1.2: { 1: 8.0,   2: 4.0 }          size
3:     { 1: 1731560 }                an object in the stylesheet
4:     { 1: 8.0,   2: 4.0 }
9:     { 1: 8.0,   2: 4.0 }
11:    { 1: 24 }
19:    a path: point (0,0), lines to (8,0), (8,4) and (0,4), then an entry with only 1: 5
```

Pages placed the image at its pixel size, 8 × 4 points. The 24 in field 11 is the number in the part name.

### The data entry

`Metadata.iwa` record 2 (type 11006) gained an entry in its field 4:

```
4:
  1: varint 24
  2: bytes (20) 93 86 b0 52 52 52 e1 12 35 78 79 6d 7d 71 d9 76 c2 22 80 23
  3: text "red-8x4.png"
  4: text "red-8x4-24.png"
  10: { 100: { 1: { 1: 8.0, 2: 4.0 }, … } }
```

Field 2 is the SHA-1 of the file. The other field-4 entries in record 2 name resources of the Blank template, such as `ginger/01_theme/hardcover_bullet_black`, and none of them has a part in the package.

### What holds the image

Two records list the image (header references, as in [0022](0022-header-references.md)):

```
1732364, type 10015:  1: { 1: 1732539 }   1: { 1: 1732647 }       ← the body text and the image
1732278, type 10010:  1: { 1: 0, 4: { 1: { 1: 1732647 } } }
```

The body text didn't change. An image placed this way isn't in the text, so there is no U+FFFC and no attachment.

## Conclusion

An image file is kept as-is under `Data/`, named after its original file name plus `-N`, where N is a data ID. Records refer to it by that ID: the image record's field 11.1. `Metadata.iwa` record 2 maps each data ID (field 4.1) to the stored file name (4.4). It also gives the original name (4.3), the file's SHA-1 (4.2) and, for an image, the pixel size (4.10.100.1). A reader that finds a data ID can look up the file by name in this table rather than guessing it from the part name.

The image's record, type 3005, holds its position and size on the page in field 1.1, like the table's drawable in [0020](0020-a-table.md). Its natural size is in fields 4 and 9, and its outline as a path in field 19.

An image placed on the page, rather than in the text, is listed by page-level records (types 10015 and 10010), next to the body text itself.

## Confidence

*Likely*:

- Image files are stored unchanged under `Data/` as `name-N.ext`.
- `Metadata.iwa` record 2 field 4 maps data IDs to files, with SHA-1, original name and stored name.
- Type 3005 is an image, with its data ID in field 11.1 and its position and size in 1.1.

*Unknown*:

- What types 10015, 10010 and 3097 are, and what fields 4, 9 and 19 of the image record mean exactly.
- Whether an image placed in the text uses an attachment like a table's. Follow-up: drag the image into a line of text, or insert it at the cursor in the Pages window.
