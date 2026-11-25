# 0454: Writing a rule's comparison

**Status:** run

A highlighting rule's settings hold its kind in 3.1.1.1, 7 for *greater than*, and its value in 3.1.1.5.2.2 ([0259](0259-conditional-highlighting.md), [0391](0391-writing-a-rule-value.md)); a filter's rule keeps its kind in 7.1.1 the same way ([0258](0258-filter.md)). This experiment writes every kind from 0 to 12 and reads which cells Numbers highlights.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0259/highlight.numbers`: `n` 1, 2, 3, 4 in B2:B5, highlighted green by rule 905589, *greater than 2* (3.1.1.1 = 7) |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0384-pdf-colours.swift`](../recipes/0384-pdf-colours.swift) |

## Recipe

```bash
mkdir -p samples/0454
O=samples/0454
for k in $(seq 0 12); do
  python3 -I recipes/0302-set-path.py samples/0259/highlight.numbers $O/kind-$k.numbers 905589 3.1.1.1 varint $k
  sh recipes/0372-in-app.sh Numbers $O/kind-$k.numbers "export d to POSIX file \"$PWD/$O/kind-$k.pdf\" as PDF"
  swift recipes/0384-pdf-colours.swift $O/kind-$k.pdf 220,130 220,150 220,170 220,190
done
```

A cell counts as highlighted when its red is below 0.9 at the cell's middle.

## Observation

H marks a highlighted cell, for the values 1, 2, 3 and 4, against the rule's value 2:

| Kind | 1 | 2 | 3 | 4 | Reads as |
| --- | --- | --- | --- | --- | --- |
| 0 | | | | | nothing matches |
| 1, 2, 3, 5 | | H | | | equal to 2 |
| 4, 6 | H | | H | H | not equal to 2 |
| 7 | | | H | H | greater than 2 |
| 8 | | H | H | H | greater than or equal to 2 |
| 9 | H | | | | less than 2 |
| 10 | H | H | | | less than or equal to 2 |
| 11, 12 | H | H | H | H | everything matches |

## Conclusion

The kind codes 7 to 10 are the four inequalities: greater than, greater than or equal, less than and less than or equal. Codes 4 and 6 match everything except 2, and 1, 2, 3 and 5 only 2: with one-digit numbers, tests of equality and text tests such as *starts with*, *ends with* or *contains* give the same answer, so these values can't tell those codes apart. Codes 11 and 12 match every cell: they are probably *between* and *not between*, which need a second value this rule doesn't have. The codes are their own list, as the pivot's summary codes are ([0279](0279-pivot-average.md)).

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `kind-0.numbers` | `0259/highlight.numbers` | Only `6010#905589 3.1.1.1: 7 → 0` | *Likely*: matches nothing; no cell is highlighted |
| `kind-1.numbers` | `0259/highlight.numbers` | Only `6010#905589 3.1.1.1: 7 → 1` | *Likely*: equality or a text match; only 2 highlighted |
| `kind-2.numbers` | `0259/highlight.numbers` | Only `6010#905589 3.1.1.1: 7 → 2` | *Likely*: equality or a text match; only 2 highlighted |
| `kind-3.numbers` | `0259/highlight.numbers` | Only `6010#905589 3.1.1.1: 7 → 3` | *Likely*: equality or a text match; only 2 highlighted |
| `kind-4.numbers` | `0259/highlight.numbers` | Only `6010#905589 3.1.1.1: 7 → 4` | *Likely*: not equal, or the opposite of a text match; all but 2 highlighted |
| `kind-5.numbers` | `0259/highlight.numbers` | Only `6010#905589 3.1.1.1: 7 → 5` | *Likely*: equality or a text match; only 2 highlighted |
| `kind-6.numbers` | `0259/highlight.numbers` | Only `6010#905589 3.1.1.1: 7 → 6` | *Likely*: not equal, or the opposite of a text match; all but 2 highlighted |
| `kind-7.numbers` | `0259/highlight.numbers` | Only written again: `same records`, `same parts`, `6010#905589 3.1.1.1 = 7` | *Confirmed*: greater than; 3 and 4 highlighted |
| `kind-8.numbers` | `0259/highlight.numbers` | Only `6010#905589 3.1.1.1: 7 → 8` | *Confirmed*: greater than or equal; 2, 3 and 4 highlighted |
| `kind-9.numbers` | `0259/highlight.numbers` | Only `6010#905589 3.1.1.1: 7 → 9` | *Confirmed*: less than; 1 highlighted |
| `kind-10.numbers` | `0259/highlight.numbers` | Only `6010#905589 3.1.1.1: 7 → 10` | *Confirmed*: less than or equal; 1 and 2 highlighted |
| `kind-11.numbers` | `0259/highlight.numbers` | Only `6010#905589 3.1.1.1: 7 → 11` | *Unknown*: what kind 11 is; every cell is highlighted |
| `kind-12.numbers` | `0259/highlight.numbers` | Only `6010#905589 3.1.1.1: 7 → 12` | *Unknown*: what kind 12 is; every cell is highlighted |

## Confidence

*Confirmed*: kinds 7, 8, 9 and 10 as greater than, greater than or equal, less than and less than or equal, by writing them. *Likely*: 1, 2, 3 and 5 test equality or a text match, 4 and 6 the opposite. *Unknown*: which is which among those, and 11 and 12.
