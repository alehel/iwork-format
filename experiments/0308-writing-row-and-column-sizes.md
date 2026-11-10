# 0308: Writing a row height and a column width

**Status:** run

[0045](0045-row-and-column-sizes.md) found sizes that differ from the default in header storage buckets (type 6006): one bucket for rows and one for columns, each listing entries of an index (2.1) and a size in points (2.2). This experiment writes new sizes and asks Numbers.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0045/sizes.numbers`: row index 2 is 50 points high, column index 1 is 200 points wide, and column indexes 5 and 6 are 98 |
| Writer | [`recipes/0308-header-size.py`](../recipes/0308-header-size.py), using the writer of [0287](0287-rewriting-a-document.md) |

## Recipe

```bash
mkdir -p samples/0308
cp samples/0045/sizes.numbers samples/0308/original.numbers
python3 -I recipes/0308-header-size.py samples/0308/original.numbers samples/0308/step.numbers 904914 2 80
python3 -I recipes/0308-header-size.py samples/0308/step.numbers samples/0308/written.numbers 904958 1 123.5
rm samples/0308/step.numbers
```

Bucket 904914 holds the rows and 904958 the columns. Numbers opened each file on its own and read sizes through AppleScript, whose rows and columns count from 1, so index 2 is row 3 and index 1 is column B. The written file was saved again.

## Observation

| File | Row 3 | Column B | Row 2 | Column F |
| --- | --- | --- | --- | --- |
| `original.numbers` | 50 | 200 | 20.27 | 98 |
| `written.numbers` | 80 | 123.5 | 20.27 | 98 |

Row 2 isn't in the bucket and keeps the table's default height.

## Conclusion

A bucket entry's index counts from 0 and its size is a float in points, which Numbers uses as written. Rows and columns not listed have the default size.

## Confidence

*Confirmed*: header storage bucket entries, by writing them.
