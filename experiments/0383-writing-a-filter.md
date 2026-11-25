# 0383: Writing a filter's value and its hidden rows

**Status:** run; its conclusion is corrected by [0391](0391-writing-a-rule-value.md), which found the value Numbers uses in a field this experiment didn't write, 7.1.5.2.2

A filter's rule is a formula in two type-6220 records, `cell > 2` with the 2 as a number node, and the rows it hides are listed by ID in table model field 70.2.3, each with field 3 set to 1 ([0258](0258-filter.md)). Numbers' AppleScript can turn a table's filters on and off (`filtered`), and its exported PDF leaves out hidden rows. This experiment writes a new value into the rule, clears the hidden flags, and reads which rows Numbers shows.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-17 |
| Input | `samples/0258/filter.numbers`: `kind` a, b, a, b and `n` 1, 2, 3, 4, filtered to n > 2. The rule is in records 905584 (formula at 7.1.7, value also at 7.1.5.2.1) and 905585 (formula at 3.1.1); the number node holds 2 in field 4 (double) and field 42. Table model 904595 lists 19 hidden rows in 70.2.3 |
| Writer | The new [`recipes/0383-set-nth-path.py`](../recipes/0383-set-nth-path.py), which takes paths through repeated fields; read back with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and [`recipes/0374-pdf-text.swift`](../recipes/0374-pdf-text.swift) |

## Recipe

```bash
mkdir -p samples/0383
N=recipes/0383-set-nth-path.py
F=samples/0258/filter.numbers
O=samples/0383
cp $F $O/original.numbers
for v in 0 3; do
  python3 -I $N $F $O/x.numbers 905584 7.1.7.1.1:2.4 double $v 7.1.7.1.1:2.42 varint $v 7.1.5.2.1 double $v
  python3 -I $N $O/x.numbers $O/value-$v.numbers 905585 3.1.1.1.1:2.4 double $v 3.1.1.1.1:2.42 varint $v
  rm $O/x.numbers
done
args=(); for i in $(seq 1 19); do args+=(70.2.3.2:$i.3 varint 0); done
python3 -I $N $F $O/all-unhidden.numbers 904595 "${args[@]}"
```

Each file was exported as PDF as it opened. Copies of `original`, `value-0` and `value-3` were also exported after turning filters off and on again (`set filtered of t to false`, then `true`), and after turning them off. Scripts that change a document were run on copies: Numbers autosaved an earlier edit into a file despite closing it unsaved.

## Observation

Rows in each exported page, after the header:

| File | As opened | Filters off and on | Filters off |
| --- | --- | --- | --- |
| `original.numbers` (> 2) | a 3, b 4 | a 3, b 4 | a 1, b 2, a 3, b 4 |
| `value-0.numbers` (> 0) | a 3, b 4 | a 3, b 4 | a 1, b 2, a 3, b 4 |
| `value-3.numbers` (> 3) | a 3, b 4 | a 3, b 4 | a 1, b 2, a 3, b 4 |
| `all-unhidden.numbers` | a 3, b 4 | | |

`filtered` read true in every file as opened. Setting a hidden cell (B2) through AppleScript didn't change the rows shown either. The first attempt to open `all-unhidden.numbers` showed "can't be opened at the moment", while the previous file was still closing; it opened normally afterwards.

## Conclusion

Neither the value in the rule nor the hidden flags in 70.2.3, as written here, change which rows Numbers shows. With the rule rewritten to > 0 or > 3, Numbers kept showing the rows that passed > 2, even after its filters were turned off and on; with every hidden flag cleared, it still hid rows 1 and 2. So Numbers takes the rows it hides from somewhere this experiment didn't touch, and doesn't evaluate the stored rule when it opens a document or when filters are toggled by script. A reader can't yet rely on either for the rows to hide; turning filters off shows all rows as expected.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `original.numbers` | `0258/filter.numbers` | `same bytes`, `6001#904595 70.2.3.2.3 = 1` | *Control*: the filter > 2 shows a 3, b 4 |
| `value-0.numbers` | `original.numbers` | Only `6220#905584 7.1.5.2.1: 2.0 → 0.0`, `6220#905584 7.1.7.1.1.4: 2.0 → 0.0`, `6220#905584 7.1.7.1.1.42: 2 → 0`, `6220#905585 3.1.1.1.1.4: 2.0 → 0.0`, `6220#905585 3.1.1.1.1.42: 2 → 0` | *Superseded* by 0391: the same rows are shown, since the value Numbers uses is in a field not written here |
| `value-3.numbers` | `original.numbers` | Only `6220#905584 7.1.5.2.1: 2.0 → 3.0`, `6220#905584 7.1.7.1.1.4: 2.0 → 3.0`, `6220#905584 7.1.7.1.1.42: 2 → 3`, `6220#905585 3.1.1.1.1.4: 2.0 → 3.0`, `6220#905585 3.1.1.1.1.42: 2 → 3` | *Superseded* by 0391: as above |
| `all-unhidden.numbers` | `original.numbers` | Only `6001#904595 70.2.3.2.3: 1 → 0` | *Likely*: the hidden flags don't decide which rows are shown |
| `original-toggled.numbers` | `original.numbers` | `6220 2: 0 → 1` | *Control*: filters turned off and on by script show the same rows |
| `value-0-toggled.numbers` | `value-0.numbers` | `6220 2: 0 → 1`, `6220 3.1.1.1.1.4 = 0.0` | *Superseded* by 0391: the same rows still |
| `value-3-toggled.numbers` | `value-3.numbers` | `6220 2: 0 → 1`, `6220 3.1.1.1.1.4 = 3.0` | *Superseded* by 0391: the same rows still |
| `original-off.numbers` | `original.numbers` | `6001 70.2.3.2.3: 1 → absent` | *Likely*: with filters off all four rows are shown |
| `value-0-off.numbers` | `value-0.numbers` | `6001 70.2.3.2.3: 1 → absent` | *Likely*: as above |
| `value-3-off.numbers` | `value-3.numbers` | `6001 70.2.3.2.3: 1 → absent` | *Likely*: as above |
| `only-522-0.numbers` | `original.numbers` | Only `6220#905584 7.1.5.2.2: 2 → 0` | *Not used*: made and read in 0391 |
| `only-522-3.numbers` | `original.numbers` | Only `6220#905584 7.1.5.2.2: 2 → 3` | *Not used*: made and read in 0391 |

## Confidence

*Unknown*: where Numbers keeps the rows a filter hides, and when it re-evaluates the rule. The follow-up is to change a filter's value in Numbers itself and compare every part, not only the table model and the rule records.
