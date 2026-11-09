# 0290: Writing a cell

**Status:** run

[0287](0287-rewriting-a-document.md) to [0289](0289-writing-two-paragraphs.md) wrote Pages text. This experiment writes a Numbers cell value, to test the spec's reading of number cells: a decimal128 value at a fixed place in the cell's bytes ([0031](0031-cell-kinds.md)).

## Setup

| | |
| --- | --- |
| Numbers | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Input | `samples/0226/plain.numbers`: `n` = 1, 2, 3, 4 in B2:B5 |
| Writer | [`recipes/0290-numbers-cell.py`](../recipes/0290-numbers-cell.py), using the writer of [0287](0287-rewriting-a-document.md) |

## Recipe

```bash
mkdir -p samples/0290
python3 -I recipes/0290-numbers-cell.py samples/0226/plain.numbers samples/0290/forty-two.numbers 1 42
```

The script decodes `Index/Tables/Tile.iwa` and finds the 16 bytes of the decimal128 value 1, `01 00 … 00 40 30`: coefficient 1, unbiased exponent 0, positive. It checks that the value occurs only once, writes the bytes of 42 in its place, and encodes the part again. The file was then opened in Numbers through AppleScript and cells B2 and B3 read.

## Observation

Numbers opens the file without a warning. B2's value is 42 and its formatted value `42`. B3 is still 2.

## Conclusion

The spec's reading of number cells is precise enough to write: a decimal128 in IEEE 754 BID form, where `40 30` in the last two bytes is exponent 0 (a bias of 6176). Changing those 16 bytes changes the cell. Nothing else holds a copy of the value that Numbers checks: not a cached display string, not a checksum. A reader can trust the decimal128 alone.

## Confidence

*Likely*: a number cell's value is its decimal128 alone, and can be written in place.
