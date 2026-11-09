# 0059: A table's position and size

**Status:** run

[0020](0020-a-table.md) took a table drawable's field 1.1 to be its position and size. This experiment moves and resizes a Numbers table through AppleScript, and checks the stored values against what Numbers reports.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0024](0024-keynote-and-numbers.md), `empty-a.numbers` |

## Recipe

```bash
mkdir -p samples/0059
osascript recipes/0059-numbers-table-geometry.applescript "$PWD/samples/0059/geometry.numbers"
```

The recipe sets the first table's `position` to (50, 60), `width` to 300 and `height` to 150. The saved file was opened again through AppleScript to read back the table's position, width and height.

## Observation

| | Empty spreadsheet | After the recipe | Numbers reports |
| --- | --- | --- | --- |
| Drawable 1.1.1, position | 0, 0.32 | 50, 32 | 50, 60 |
| Drawable 1.1.2, size | 494 × 231 | 494 × 231 | 300 × 184 |

The header storage buckets (see [0045](0045-row-and-column-sizes.md)) now list every row and column:

- The 7 columns are 42.857 points each, 300 in all.
- The 22 rows are two of 8.55 and twenty of 8.35, 184.1 in all.

Numbers didn't make the rows as small as the requested height of 150 needed.

## Conclusion

A Numbers table's size isn't kept in its drawable's geometry. Field 1.1.2 still held the old 494 × 231 after the table was resized. The size Numbers uses is the sum of the column widths and row heights in the header storage buckets. A reader should add those up rather than trust the drawable's size.

The position's x (50) matches what Numbers reports, but its y is 28 points less (32 against 60). The difference may be the room for the table's name above it, but that isn't established. Resizing a table through AppleScript writes every row and column into the header buckets, not just the ones that differ from the default.

## Confidence

*Likely*: a Numbers table's real size is the sum of its row heights and column widths, and drawable field 1.1.2 can be out of date.

*Unknown*:

- Why the stored y is 28 points less than the reported one.
- Whether Pages' table drawables behave the same.
