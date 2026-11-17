# 0382: Writing a merged range

**Status:** run

Merged cells are recorded in the table model's field 47.2 as ranges in the node form of formulas, not in the cells ([0044](0044-merged-cells.md)). That experiment's recipe asked Numbers to merge B2:C3, and the range node it found has 40.3 = { 1: 2 } and 40.4 = { 1: 1, 2: 2 }, which it couldn't fully explain. AppleScript can't tell whether cells are merged, but Numbers draws a merged range as one cell when it exports PDF. This experiment draws the saved file and then writes new bounds.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-17 |
| Input | `samples/0044/merged.numbers`: table model 904595, with one merged range and 42 in B2 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and looked at as pictures |

## Recipe

```bash
mkdir -p samples/0382
R=recipes/0302-set-path.py
O=samples/0382
F=$O/original.numbers
cp samples/0044/merged.numbers $F
B=47.2.3.2.1.1.40
python3 -I $R $F $O/column-b.numbers 904595 $B.3.1 varint 1
python3 -I $R $F $O/columns-c-d.numbers 904595 $B.3.2 varint 3
python3 -I $R $F $O/rows-2-5.numbers 904595 $B.4.2 varint 4
for f in original column-b columns-c-d rows-2-5; do
  sh recipes/0372-in-app.sh Numbers $O/$f.numbers "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF"
  sips -s format png $O/$f.pdf --out $O/$f.png
done
```

The range node is the first node of the merge's expression, at 47.2.3.2.1.1. A first attempt one level higher created new fields instead of changing the bounds, and wasn't used.

## Observation

| File | 40.3 (written) | 40.4 (written) | Merged cell drawn | 42 drawn in |
| --- | --- | --- | --- | --- |
| `original.numbers` | { 1: 2 } | { 1: 1, 2: 2 } | C2:C3 | B2, an ordinary cell |
| `column-b.numbers` | { 1: 1 } | { 1: 1, 2: 2 } | B2:B3 | the merged cell |
| `columns-c-d.numbers` | { 1: 2, 2: 3 } | { 1: 1, 2: 2 } | C2:D3 | B2, an ordinary cell |
| `rows-2-5.numbers` | { 1: 2 } | { 1: 1, 2: 4 } | C2:C5 | B2, an ordinary cell |

AppleScript reads 42 from B2 and `missing value` from C2, B3 and C3 in the original.

## Conclusion

In a merged range's node, field 40.3 is the span of columns and 40.4 the span of rows, each as { 1: first, 2: last } with indices from 0; a missing last means a span of one. So the file 0044 saved holds a merge of C2:C3, not the B2:C3 its recipe asked for, and Numbers draws exactly that, with 42 left in an ordinary B2. Whatever made the saved merge differ from the script, the file and the drawing agree, and writing the bounds moves the merge as described.

The spec's earlier reading, that 40.4 = { 1, 2 } are columns B to C, was wrong.

## Confidence

*Confirmed*: field 40.3 of a merged range's node as its columns and 40.4 as its rows, first and last from 0, by writing them. Why 0044's script produced C2:C3 is *unknown*; rerunning it and reading the merge back would settle it.
