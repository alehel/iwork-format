# 0329: The colour space field

**Status:** run

Colour messages hold red, green and blue in fields 3, 4 and 5, which matched sRGB in five colours ([0309](0309-writing-a-cell-colour.md), [0328](0328-writing-a-page-background.md)), and also have a field 12, always 1 so far. This experiment writes other values of field 12 into a page background and measures the colour drawn.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0328/background.pages`: a page background of 0.6, 0.8, 1.0, without field 12 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0329
for v in 0 1 2 3; do
  python3 -I recipes/0302-set-path.py samples/0328/background.pages samples/0329/space$v.pages 1732296 30.1.12 varint $v
done
```

Pages opened each file on its own and exported it as PDF; each page was drawn and its corner pixel read in sRGB. The same components read as Display P3 were converted to sRGB with macOS's colour conversion, for comparison.

## Observation

| Field 12 | Corner pixel (sRGB) |
| --- | --- |
| absent ([0328](0328-writing-a-page-background.md)) | 0.600, 0.800, 1.000 |
| 0 | 0.600, 0.800, 1.000 |
| 1 | 0.600, 0.800, 1.000 |
| 2 | 0.541, 0.808, 1.000 |
| 3 | 0.600, 0.800, 1.000 |

0.6, 0.8, 1.0 in Display P3 is 0.541, 0.807, 1.000 in sRGB.

## Conclusion

Field 12 of a colour message is its colour space: 1 (or absent, or 0) for sRGB and 2 for Display P3, which the apps convert when drawing. Other values seem to fall back to sRGB. The apps write 1 for the colours seen so far; a colour picked in Display P3 would presumably be stored with 2. A reader must check field 12 before treating the components as sRGB.

## Confidence

*Likely*: field 12 is the colour space, 1 sRGB and 2 Display P3 (one colour, matched to three decimals).
