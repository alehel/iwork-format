# 0311: Writing a paragraph style's character properties

**Status:** run

[0310](0310-writing-a-cell-text-style.md) confirmed the font, size and colour properties in a Numbers cell's text style. This experiment does the same in Pages, by writing the Body paragraph style that the whole body uses, and adds bold and italic (11.1 and 11.2, [0007](0007-bold-and-italic.md)).

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0002/hello.pages`: the word `hello` in the Body style (record 1731511): HelveticaNeue, 11 points, black, not bold or italic |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0311
cp samples/0002/hello.pages samples/0311/original.pages
python3 -I recipes/0302-set-path.py samples/0311/original.pages samples/0311/written.pages 1731511 \
  11.3 float 24 11.5 string Georgia 11.1 varint 1 11.2 varint 1 \
  11.46.1.3 float 0.8 11.46.1.4 float 0.1 11.46.1.5 float 0.1 \
  11.7.3 float 0.8 11.7.4 float 0.1 11.7.5 float 0.1
```

Pages opened each file on its own through Launch Services and read the first word's `size`, `font` and `color` through AppleScript; the written file was saved again.

## Observation

| File | Size | Font | Colour |
| --- | --- | --- | --- |
| `original.pages` | 11 | HelveticaNeue | 0, 0, 0 |
| `written.pages` | 24 | Georgia-BoldItalic | 48833, 0, 5356 |

0.8, 0.1, 0.1 in sRGB is 48833, 0, 5356 in Generic RGB.

## Conclusion

A paragraph style's character properties work as read: 11.3 size, 11.5 font family face, 11.1 bold and 11.2 italic applied on top of it, and the colour in 11.46.1 with its copy in 11.7. Changing the style changes all text that uses it, with no change to the text's runs.

## Confidence

*Confirmed*: paragraph style properties 11.1, 11.2, 11.3, 11.5 and 11.46, by writing them in Pages.
