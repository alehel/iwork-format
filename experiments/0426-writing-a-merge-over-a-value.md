# 0426: Writing a merge over a value that isn't in its first cell

**Status:** run

A merged cell keeps its value in its top-left cell, and the other cells of the range are absent from the tile ([0044](0044-merged-cells.md)). A merge's bounds are columns in 40.3 and rows in 40.4 of its range node ([0382](0382-writing-merged-cells.md)). This experiment writes merges in which the only value, 42 in B2, isn't the top-left cell.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0044/merged.numbers`: 42 in B2 and a merge of C2:C3, in table model 904595. Row 1 is a header row and column A a header column |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and looked at as pictures |

## Recipe

```bash
mkdir -p samples/0426
R=recipes/0302-set-path.py
O=samples/0426
B=47.2.3.2.1.1.40
python3 -I $R samples/0044/merged.numbers $O/b2-b3.numbers 904595 $B.3.1 varint 1
python3 -I $R $O/b2-b3.numbers $O/b1-b2.numbers 904595 $B.4.1 varint 0 $B.4.2 varint 1
python3 -I $R $O/b2-b3.numbers $O/a2-b3.numbers 904595 $B.3.1 varint 0 $B.3.2 varint 1
for f in b2-b3 b1-b2 a2-b3; do
  sh recipes/0372-in-app.sh Numbers $O/$f.numbers "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF"
  sips -s format png $O/$f.pdf --out $O/$f.png
done
```

## Observation

| File | Merge written | Top-left cell | Where 42 is drawn |
| --- | --- | --- | --- |
| `b2-b3.numbers` | B2:B3 | B2, holding 42 | in the merged cell, in the body's style |
| `b1-b2.numbers` | B1:B2 | B1, empty, in the header row | in the merged cell, grey like the header row |
| `a2-b3.numbers` | A2:B3 | A2, empty, in the header column | in the merged cell, grey like the header column |

The PDF's text is `42` and the table's name in all three; no cell lost its value.

## Conclusion

A merged cell shows the value of the range even when it isn't stored in the range's top-left cell: with B2 in the middle or bottom of a merge whose first cell is empty, Numbers still draws 42 in the merged cell. The merged cell takes its look from its top-left cell, here a header row or column. Numbers itself stores a merged cell's value in the top-left cell, so a reader of a file Numbers made can keep looking there; with only one value in the range, which cell holds it doesn't matter. Which value wins when several cells of a merge hold one wasn't tested.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `b2-b3.numbers` | `0044/merged.numbers` | Only `6001#904595 47.2.3.2.1.1.40.3.1: 2 → 1` | *Likely*: 42 in the first cell of the merge is drawn in the merged cell |
| `b1-b2.numbers` | `b2-b3.numbers` | Only `6001#904595 47.2.3.2.1.1.40.4.1: 1 → 0`, `6001#904595 47.2.3.2.1.1.40.4.2: 2 → 1` | *Confirmed*: 42 is drawn though it isn't in the first cell, in the header row's grey |
| `a2-b3.numbers` | `b2-b3.numbers` | Only `6001#904595 47.2.3.2.1.1.40.3.1: 1 → 0`, `6001#904595 47.2.3.2.1.1.40.3.2: absent → 1` | *Confirmed*: 42 is drawn though it isn't in the first cell, in the header column's grey |

## Confidence

*Confirmed*: a merged cell shows a value stored in another cell of the range when the top-left is empty, and takes its look from the top-left, by writing it.
