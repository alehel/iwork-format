# 0326: Writing the top and right margins

**Status:** run

[0318](0318-writing-paper-size-and-margin.md) confirmed the paper size and the left margin (root field 32) by writing them. This experiment does the same for the right and top margins, fields 33 and 34, on a paragraph that wraps, measuring with [`recipes/0319-measure-pdf.swift`](../recipes/0319-measure-pdf.swift).

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0320/long.pages`: one wrapping paragraph on A4 (595.28 points wide) with all margins 56.69 points |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0326
cp samples/0320/long.pages samples/0326/long.pages
python3 -I recipes/0302-set-path.py samples/0326/long.pages samples/0326/top150.pages 1 34 float 150
python3 -I recipes/0302-set-path.py samples/0326/long.pages samples/0326/right150.pages 1 33 float 150
```

Each file was opened in Pages on its own, exported as PDF and measured.

## Observation

| File | Line 1: top, left – right | Line 2: top, left – right |
| --- | --- | --- |
| `long.pages` | 60.2, 57.5 – 506.0 | 72.2, 57.5 – 506.0 |
| `top150.pages` (34 = 150) | 153.5, 57.5 – 506.0 | 165.5, 57.5 – 506.0 |
| `right150.pages` (33 = 150) | 60.2, 57.5 – 415.5 | 72.2, 57.5 – 415.5 |

## Conclusion

Field 34 is the top margin: the text moves down by 93.3 points, the difference between 150 and 56.69. Field 33 is the right margin: the lines now wrap before 595.28 − 150 = 445.28 points. Both are floats in points, used as written.

## Confidence

*Confirmed*: root fields 33 and 34, by writing them and measuring.
