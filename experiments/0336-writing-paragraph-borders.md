# 0336: Writing a paragraph border's edges, measured on the page

**Status:** run

A paragraph border is property 12.32 (its stroke) with its edges in two places: 12.45 as bits (1 top, 2 bottom, 15 all) and 12.15 as an older single value (1 top, 2 bottom, 4 all) ([0262](0262-paragraph-border.md), [0273](0273-border-edges.md)). This experiment writes each and measures which edges Pages draws.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0262/border.pages`: the paragraph `One` with a top border, through an unnamed child of Body (record 1732697) holding 12.15 = 1, 12.32 and 12.45 = 1 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0336
cp samples/0262/border.pages samples/0336/original.pages
R=recipes/0302-set-path.py
python3 -I $R samples/0336/original.pages samples/0336/new-bottom.pages 1732697 12.45 varint 2
python3 -I $R samples/0336/original.pages samples/0336/new-all.pages 1732697 12.45 varint 15
python3 -I $R samples/0336/original.pages samples/0336/old-bottom.pages 1732697 12.15 varint 2
python3 -I $R samples/0336/original.pages samples/0336/old-all.pages 1732697 12.15 varint 4
```

Each file was opened in Pages on its own and exported as PDF; the page was drawn at 4 pixels per point and scanned for long horizontal and tall vertical lines. Earlier attempts wrote the same values into Heading 3 and into Body and changed nothing, because the paragraph's own child style holds the border.

## Observation

| File | Horizontal lines (y) | Vertical lines (x) |
| --- | --- | --- |
| `original.pages` (15 = 1, 45 = 1) | 56.8 – 57.5 | none |
| `new-bottom.pages` (45 = 2) | 56.8 – 57.5 | none |
| `new-all.pages` (45 = 15) | 56.8 – 57.5 | none |
| `old-bottom.pages` (15 = 2) | 74.8 – 75.5 | none |
| `old-all.pages` (15 = 4) | 56.8 – 57.5 and 81.8 – 82.5 | 50.0 – 51.0 and 544.8 – 545.8 |

## Conclusion

Pages draws a paragraph border's edges from 12.15: 1 a line above, 2 a line below, 4 a box around the paragraph, set about 6.7 points outside the margins at the sides. 12.45, the bit set that Pages also writes, doesn't change what is drawn here, at least while 12.15 is present. A writer should set both, as Pages does.

## Confidence

*Confirmed*: 12.15 decides the edges drawn (1 top, 2 bottom, 4 all), by writing it and measuring.

*Unknown*: when 12.45 is used, since changing it alone had no effect.
