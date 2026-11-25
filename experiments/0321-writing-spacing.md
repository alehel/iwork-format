# 0321: Writing paragraph and line spacing, measured on the page

**Status:** run

A paragraph style's spacing was read as properties 12.20 (space after) and 12.21 (space before), in points, and 12.13 (line spacing): a message with the kind in field 1 (0 lines, 1 at least, 2 exactly, 4 between) and the amount in field 2 ([0252](0252-line-spacing.md), [0256](0256-paragraph-spacing.md), [0276](0276-exact-line-spacing.md), [0281](0281-other-line-spacing-kinds.md)). This experiment writes them into the Body style and measures the lines on the exported page with [`recipes/0319-measure-pdf.swift`](../recipes/0319-measure-pdf.swift).

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0005/two-lf.pages` (paragraphs `one` and `two`) and `samples/0320/long.pages` (one paragraph wrapping to several lines), both in the 11-point Body style, whose 12.13 is an empty message (first written as absent) |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0321
cp samples/0005/two-lf.pages samples/0321/two.pages
cp samples/0320/long.pages samples/0321/long.pages
python3 -I recipes/0302-set-path.py samples/0321/two.pages samples/0321/after24.pages 1731511 12.20 float 24
python3 -I recipes/0302-set-path.py samples/0321/two.pages samples/0321/before24.pages 1731511 12.21 float 24
python3 -I recipes/0302-set-path.py samples/0321/long.pages samples/0321/double.pages 1731511 12.13.1 varint 0 12.13.2 float 2
python3 -I recipes/0302-set-path.py samples/0321/long.pages samples/0321/exactly30.pages 1731511 12.13.1 varint 2 12.13.2 float 30
```

Each file was opened in Pages on its own, exported as PDF and measured. Line bottoms are compared, since they don't depend on which letters a line holds.

## Observation

Bottoms of the first lines, in points from the top of the page:

| File | Line 1 | Line 2 | Line 3 |
| --- | --- | --- | --- |
| `two.pages` | 66.2 | 78.2 | |
| `after24.pages` (12.20 = 24) | 66.2 | 102.2 | |
| `before24.pages` (12.21 = 24) | 66.2 | 102.2 | |
| `long.pages` | 66.2 | 78.2 | 90.2 |
| `double.pages` (12.13 = 0, 2) | 66.2 | 90.0 | 113.5 |
| `exactly30.pages` (12.13 = 2, 30) | 80.8 | 110.8 | 140.8 |

## Conclusion

12.20 adds space after each paragraph and 12.21 before it, in points. Pages leaves out the space before the first paragraph at the top of the page. Line spacing kind 0 multiplies the normal line height: twice 12 is close to the 23.5 to 23.8 measured. Kind 2 sets the distance between baselines to exactly the amount, 30 points, and moves the first line down to suit.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `two.pages` | `0005/two-lf.pages` | `same bytes` | *Control*: lines 12 points apart |
| `long.pages` | `0320/long.pages` | `same bytes` | *Control*: lines 12 points apart |
| `after24.pages` | `two.pages` | Only `2022#1731511 12.20: 0.0 → 24.0` | *Confirmed*: 12.20 is the space after; the second line is 24 points lower |
| `before24.pages` | `two.pages` | Only `2022#1731511 12.21: 0.0 → 24.0` | *Confirmed*: 12.21 is the space before; the second line is 24 points lower |
| `double.pages` | `long.pages` | Only `2022#1731511 12.13: changed`, `2022#1731511 12.13.1: absent → 0`, `2022#1731511 12.13.2: absent → 2.0` | *Confirmed*: kind 0 multiplies the line height; the lines are 23.5 to 23.8 points apart |
| `exactly30.pages` | `long.pages` | Only `2022#1731511 12.13: changed`, `2022#1731511 12.13.1: absent → 2`, `2022#1731511 12.13.2: absent → 30.0` | *Confirmed*: kind 2 is exact; the lines are 30 points apart |

## Confidence

*Confirmed*: 12.20, 12.21, and 12.13 kinds 0 and 2, by writing them and measuring.
