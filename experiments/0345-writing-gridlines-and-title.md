# 0345: Writing a table's gridlines and name visibility

**Status:** run

Table style property 11.34 = 0 was read as hiding the body's horizontal gridlines ([0234](0234-gridlines.md)), and table model field 22 as showing the table's name above it, absent when hidden ([0232](0232-hidden-table-title.md)). This experiment writes each and measures the exported sheet.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0226/plain.numbers`: a table of 22 rows named `Tabell 1`, shown above it; table style 905007 without 11.34, model 904595 with 22 = 1 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0345
cp samples/0226/plain.numbers samples/0345/plain.numbers
python3 -I recipes/0302-set-path.py samples/0345/plain.numbers samples/0345/no-hlines.numbers 905007 11.34 varint 0
python3 -I recipes/0302-set-path.py samples/0345/plain.numbers samples/0345/no-title.numbers 904595 22 varint 0
```

Numbers opened each file on its own and exported it as PDF. The page was drawn, dark lines crossing a column through the table's empty cells were counted, and dark ink above the table's top edge, in the middle third of the page, was counted for the name.

## Observation

| File | Lines crossed down the column | Ink of the name above the table |
| --- | --- | --- |
| `plain.numbers` | 22 | 1917 pixels |
| `no-hlines.numbers` (11.34 = 0) | 2 | 1917 pixels |
| `no-title.numbers` (22 = 0) | 22 | 0 |

## Conclusion

Table style 11.34 = 0 removes the body's horizontal gridlines, leaving only the lines along the header and the table's outer edge. Model field 22 = 0 hides the table's name; Numbers itself leaves the field out for a hidden name, and 0 does the same.

## Confidence

*Confirmed*: table style 11.34 and model field 22, by writing them.
