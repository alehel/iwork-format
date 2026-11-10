# 0322: Writing character properties, measured on the page

**Status:** run

Character properties were read as fields of a style's field 11: 10 the baseline (1 superscript, 2 subscript), 13 capitals (1 all caps, 2 small caps), 14 the baseline shift in points and 27 tracking ([0203](0203-superscript.md)–[0209](0209-raised-baseline.md)). This experiment writes each into the Body style and measures the text on the exported page with [`recipes/0319-measure-pdf.swift`](../recipes/0319-measure-pdf.swift).

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0002/hello.pages` (the word `hello`, 11-point Body) and `samples/0320/long.pages` (a paragraph wrapping to several lines) |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0322
cp samples/0002/hello.pages samples/0322/original.pages
R=recipes/0302-set-path.py
python3 -I $R samples/0322/original.pages samples/0322/caps.pages 1731511 11.13 varint 1
python3 -I $R samples/0322/original.pages samples/0322/super.pages 1731511 11.10 varint 1
python3 -I $R samples/0322/original.pages samples/0322/shift10.pages 1731511 11.14 float 10
python3 -I $R samples/0322/original.pages samples/0322/tracking.pages 1731511 11.27 float 0.5
python3 -I $R samples/0320/long.pages samples/0322/long-shift10.pages 1731511 11.14 float 10
```

Each file was opened in Pages on its own, exported as PDF and measured.

## Observation

The word's ink, in points:

| File | Left – right | Top – bottom |
| --- | --- | --- |
| `original.pages` | 57.5 – 79.5 | 58.2 – 66.2 |
| `caps.pages` (13 = 1) | 57.8 – 91.5 | 58.0 – 66.2 |
| `super.pages` (10 = 1) | 57.5 – 72.0 | 58.2 – 63.2 |
| `shift10.pages` (14 = 10) | 57.5 – 79.5 | 58.2 – 66.2 |
| `tracking.pages` (27 = 0.5) | 57.5 – 101.5 | 58.2 – 66.2 |

The first three lines of the long paragraph, top – bottom: 60.2 – 66.2, 72.2 – 78.2 and 84.2 – 90.2 as written; 60.2 – 66.2, 82.2 – 88.2 and 104.2 – 110.2 with 14 = 10.

## Conclusion

All caps sets `HELLO` in capitals, 12 points wider. Superscript sets the word smaller and raised: it is 7.5 points narrower and its bottom 3 points higher. Tracking 0.5 adds half an em, 5.5 points, after each of the word's letters, 22 points in all for the four gaps and the end. The baseline shift raises the text by 10 points, and each line grows by the same amount to make room, so on the first line the text stays where it was while the spacing between lines grows from 12 to 22 points.

## Confidence

*Confirmed*: character properties 11.10, 11.13, 11.14 and 11.27, by writing them and measuring.
