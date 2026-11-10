# 0332: Writing a dash pattern, measured on the page

**Status:** run

[0274](0274-dashed-border.md) found a stroke's dash pattern in field 6 of the stroke: the kind in field 1 (0 dash, 1 solid, 2 none), the number of lengths used in 3, and six length slots in 4. It didn't establish the lengths' unit. This experiment writes a pattern into a solid stroke and measures the dashes on the exported page.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0330/original.pages`: a 100 × 100 shape at (300, 300) with a solid black 5-point stroke in style 1732710, pattern 1 = 1, 3 = 0, six zero lengths |
| Writer | [`recipes/0332-stroke-pattern.py`](../recipes/0332-stroke-pattern.py), using the writer of [0287](0287-rewriting-a-document.md) |

## Recipe

```bash
mkdir -p samples/0332
python3 -I recipes/0332-stroke-pattern.py samples/0330/original.pages samples/0332/dashed.pages 1732710 2 2
```

The script sets the pattern to a dash with two lengths, 2 and 2. Pages opened the file on its own, exported it as PDF and saved it again. The page was drawn at 4 pixels per point and the dark runs listed along a line 1.5 points above the shape's top edge, inside the stroke.

## Observation

| File | Dark runs along the top edge |
| --- | --- |
| `samples/0330/original.pages` | one, 297.8 – 402.8 |
| `dashed.pages` | 300.2 – 310.2, 320.2 – 330.2, 340.2 – 350.2, 360.2 – 370.2, 380.2 – 390.2 |

## Conclusion

Field 1 = 0 makes the stroke dashed, field 3 says how many of the length slots are used, and the lengths alternate dash and gap. They are in units of the stroke's width: lengths of 2 on a 5-point stroke give 10-point dashes and 10-point gaps.

## Confidence

*Confirmed*: the dash pattern's kind, count and lengths, by writing them; the lengths are multiples of the stroke width (one stroke width tested).
