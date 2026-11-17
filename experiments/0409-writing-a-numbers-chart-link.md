# 0409: Writing a Numbers chart's link to its cells

**Status:** run

A Numbers chart keeps a copy of its data in 10000.7, like charts in Pages and Keynote, and also links to its table: 10000.8 names a type-12006 record whose field 3 holds cell formulas for the series values (3.1), category labels (3.3) and series names (3.4) ([0225](0225-numbers-chart.md)). This experiment writes the copy, a cell, and the link, and compares the exported sheet with one where Numbers made the same change itself.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0225/linked.numbers`: x = 1, 3 and y = 2, 4 in B2:C3, charted as two series over r1 and r2. Chart 905458 has the values in 10000.7.3; its link, record 905524, has in 3.1 a first formula made of a reference to B2, a reference to B3 and node 29 |
| Writer | [`recipes/0383-set-nth-path.py`](../recipes/0383-set-nth-path.py) and [`recipes/0342-cell-number.py`](../recipes/0342-cell-number.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and compared with [`recipes/0399-pdf-diff.swift`](../recipes/0399-pdf-diff.swift), which can now compare part of a page |

## Recipe

```bash
mkdir -p samples/0409
N=recipes/0383-set-nth-path.py
F=samples/0225/linked.numbers
O=samples/0409
cp $F $O/original.numbers
python3 -I $N $F $O/cache-9.numbers 905458 10000.7.3:1.1:1.1 double 9
python3 -I recipes/0342-cell-number.py $F $O/cell-b2-9.numbers 1 1 9
python3 -I $N $F $O/link-to-c2.numbers 905524 3.1:1.1.1:1.26.1 varint 4
python3 -I $N $F $O/link-to-column-c.numbers 905524 3.1:1.1.1:1.26.1 varint 4 3.1:1.1.1:2.26.1 varint 4
for f in original cache-9 cell-b2-9 link-to-c2 link-to-column-c; do
  sh recipes/0372-in-app.sh Numbers $O/$f.numbers "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF"
done
```

As references, Numbers itself set B2 to 9 in one copy (`numbers-b2-9`), and B2 to 2 and B3 to 4 in another (`numbers-x-is-y`), through AppleScript, before exporting. Column 4 is index 2, column C, in the zigzag form of [0371](0371-writing-a-cell-reference.md).

## Observation

| File | Written | Compared with | Result |
| --- | --- | --- | --- |
| `cache-9.pdf` | the copy's first value: 9 | `original.pdf` | the same |
| `cell-b2-9.pdf` | cell B2: 9 | `numbers-b2-9.pdf` | the same, table and chart |
| `link-to-c2.pdf` | the first reference: C2 | | x has four bars, 1, 2, 3 and 4 |
| `link-to-column-c.pdf` | both references: C2 and C3 | `numbers-x-is-y.pdf` | the chart the same; only the digits in B2 and B3 differ |

## Conclusion

Numbers draws a chart from its link to the table, worked out when it opens the document, and ignores the copy of the data in 10000.7: a written copy changed nothing, and a written cell redrew the chart exactly as Numbers does when the cell is edited. The series formulas are ranges: a reference to the first cell and one to the last, joined by node 29. Moving only the first end to C2 made the range B2:C3, read across each row (1, 2, 3, 4), and moving both ends to column C made series x the same as y. A reader of a Numbers chart should evaluate its link formulas against the table and use 10000.7 only where there is no link, as in Pages and Keynote.

## Confidence

*Confirmed*: a Numbers chart's values come from its type-12006 link formulas, not its copy in 10000.7, and node 29 joins two references into a range, by writing them.
