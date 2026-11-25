# 0391: Writing the value of a highlighting rule and a filter

**Status:** run

A conditional highlighting rule is a type-6010 record whose condition is a formula, and cells under it cache the result in the key of their flag 0x100: the index of the first matching rule, or 15 for none ([0259](0259-conditional-highlighting.md), [0267](0267-highlighting-result.md)). Writing a filter's value into its formulas changed nothing Numbers showed ([0383](0383-writing-a-filter.md)). This experiment writes the cached results and then each copy of the rule's value in turn, and reads the cell fills from the exported PDF.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-17 |
| Input | `samples/0259/highlight.numbers`: `n` 1, 2, 3, 4 in B2:B5, with the rule *greater than 2* and a green fill, so B4 and B5 are green. The rule is record 905589 in `Tables/DataList-904538.iwa`. Its value 2 is in six places (first written as five): a number node (field 4, a double, and 42) in the formula at 2.1, the same in a second formula at 3.1.1.7, and 3.1.1.5.2, which holds { 1: 2.0 (a double), 2: 2 }. `samples/0258/filter.numbers` keeps its filter's value the same way in record 905584, at 7.1.5.2 |
| Writer | The new [`recipes/0391-cell-key.py`](../recipes/0391-cell-key.py) for the cached results and [`recipes/0383-set-nth-path.py`](../recipes/0383-set-nth-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0384-pdf-colours.swift`](../recipes/0384-pdf-colours.swift) and [`recipes/0374-pdf-text.swift`](../recipes/0374-pdf-text.swift) |

## Recipe

```bash
mkdir -p samples/0391
K=recipes/0391-cell-key.py
N=recipes/0383-set-nth-path.py
F=samples/0259/highlight.numbers
O=samples/0391
cp $F $O/original.numbers
python3 -I $K $F $O/b2-cached-match.numbers 1 1 0x100 0
python3 -I $K $F $O/b5-cached-none.numbers 4 1 0x100 15
python3 -I $N $F $O/rule-formula-3.numbers 905589 2.1.1.1.1:2.4 double 3 2.1.1.1.1:2.42 varint 3
python3 -I $N $F $O/rule-settings-3.numbers 905589 3.1.1.5.2.1 double 3 \
  3.1.1.7.1.1:2.4 double 3 3.1.1.7.1.1:2.42 varint 3
python3 -I $N $O/rule-formula-3.numbers $O/rule-all-3.numbers 905589 3.1.1.5.2.1 double 3 \
  3.1.1.7.1.1:2.4 double 3 3.1.1.7.1.1:2.42 varint 3
python3 -I $N $F $O/only-522.numbers 905589 3.1.1.5.2.2 varint 3
python3 -I $N $F $O/only-522-zero.numbers 905589 3.1.1.5.2.2 varint 0
for v in 0 3; do
  python3 -I $N samples/0258/filter.numbers samples/0383/only-522-$v.numbers 905584 7.1.5.2.2 varint $v
done
for f in $O/*.numbers; do
  sh recipes/0372-in-app.sh Numbers $f "export d to POSIX file \"$PWD/${f%.numbers}.pdf\" as PDF"
  swift recipes/0384-pdf-colours.swift ${f%.numbers}.pdf 220,130 220,150 220,170 220,190
done
```

The four points are the middles of B2 to B5 on the exported page. Copies of `original`, `rule-all-3` and a version with every copy set to 0 were also exported after setting B2 to 2.5 through AppleScript, to make Numbers recalculate. A search of every record of `rule-all-3.numbers` for 2 as a float, a double, a decimal128 or text found none outside the cells.

## Observation

| File | Written | B2 (1) | B3 (2) | B4 (3) | B5 (4) |
| --- | --- | --- | --- | --- | --- |
| `original.numbers` | nothing | white | white | green | green |
| `b2-cached-match.numbers` | B2's 0x100 key 15 → 0 | white | white | green | green |
| `b5-cached-none.numbers` | B5's 0x100 key 0 → 15 | white | white | green | green |
| `rule-formula-3.numbers` | 3 in the formula at 2.1 | white | white | green | green |
| `rule-settings-3.numbers` | 3 in 3.1.1.5.2.1 and the formula at 3.1.1.7 | white | white | green | green |
| `rule-all-3.numbers` | 3 in all three | white | white | green | green |
| `rule-all-3.numbers`, B2 set to 2.5 | | green | white | green | green |
| `only-522.numbers` | 3.1.1.5.2.2 = 3 | white | white | white | green |
| `only-522-zero.numbers` | 3.1.1.5.2.2 = 0 | green | green | green | green |

Green is 0.72, 0.90, 0.58 and white 1, 1, 1. The filter, read as the rows shown under the header:

| File | Written | Rows shown |
| --- | --- | --- |
| `samples/0258/filter.numbers` | nothing (n > 2) | a 3, b 4 |
| `samples/0383/only-522-0.numbers` | 905584 7.1.5.2.2 = 0 | a 1, b 2, a 3, b 4 |
| `samples/0383/only-522-3.numbers` | 905584 7.1.5.2.2 = 3 | b 4 |

## Conclusion

Numbers evaluates a highlighting rule and a filter when it opens a document, and doesn't use the results stored in the file: the cells' 0x100 keys and the filter's list of hidden rows are only caches. But it doesn't take the value from the rule's formulas either, nor from the double beside it. The value it compares with is the varint in field 2 of the rule's value message: 3.1.1.5.2.2 for a highlighting rule and 7.1.5.2.2 for a filter. Written alone, it changes the result, and changing every other copy without it doesn't, even after recalculating. The formulas and the double are probably what the rules editor shows.

So [0383](0383-writing-a-filter.md)'s conclusion, that neither the rule nor the hidden rows decide what is shown, holds for what it wrote, but the filter's value is in a field it didn't write.

Whether field 2 can hold a value that isn't a whole number wasn't tested.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `original.numbers` | `0259/highlight.numbers` | `same bytes`, `6010#905589 3.1.1.5.2.2 = 2` | *Control*: B4 and B5 are green |
| `b2-cached-match.numbers` | `original.numbers` | Only `6002#904547 5.6: changed`, `6002#904547 5.6 ~ x"01000000000000000000000000004030010000000000000001000000"` | *Confirmed*: the cached result isn't used: B2 stays white |
| `b5-cached-none.numbers` | `original.numbers` | Only `6002#904547 5.6: changed`, `6002#904547 5.6 ~ x"04000000000000000000000000004030010000000f00000001000000"` | *Confirmed*: as above: B5 stays green |
| `rule-formula-3.numbers` | `original.numbers` | Only `6010#905589 2.1.1.1.1.4: 2.0 → 3.0`, `6010#905589 2.1.1.1.1.42: 2 → 3` | *Likely*: the formula at 2.1 isn't used to evaluate the rule |
| `rule-settings-3.numbers` | `original.numbers` | Only `6010#905589 3.1.1.5.2.1: 2.0 → 3.0`, `6010#905589 3.1.1.7.1.1.4: 2.0 → 3.0`, `6010#905589 3.1.1.7.1.1.42: 2 → 3` | *Likely*: nor are the double and the second formula |
| `rule-all-3.numbers` | `rule-formula-3.numbers` | Only `6010#905589 3.1.1.5.2.1: 2.0 → 3.0`, `6010#905589 3.1.1.7.1.1.4: 2.0 → 3.0`, `6010#905589 3.1.1.7.1.1.42: 2 → 3` | *Likely*: nor all three together: B4 stays green |
| `rule-all-3-edited.numbers` | `rule-all-3.numbers` | `6002 5.6: changed`, `6002 5.6 ~ x"19000000000000000000000000003e30"` (2.5) | *Likely*: the written values aren't used after a recalculation either: B2 at 2.5 is green |
| `only-522.numbers` | `original.numbers` | Only `6010#905589 3.1.1.5.2.2: 2 → 3` | *Confirmed*: field 2 of the value message is the value compared with: only B5 is green |
| `only-522-zero.numbers` | `original.numbers` | Only `6010#905589 3.1.1.5.2.2: 2 → 0` | *Confirmed*: as above: all four are green |
| `0383/only-522-0.numbers` | `0258/filter.numbers` | Only `6220#905584 7.1.5.2.2: 2 → 0` | *Confirmed*: 7.1.5.2.2 is a filter's value: all four rows are shown |
| `0383/only-522-3.numbers` | `0258/filter.numbers` | Only `6220#905584 7.1.5.2.2: 2 → 3` | *Confirmed*: as above: only b 4 is shown |
| `original-edited.numbers` | `original.numbers` | `6002 5.6: changed`, `6002 5.6 ~ x"19000000000000000000000000003e30"` (2.5) | *Control*: B2 set to 2.5 with the rule unchanged |
| `rule-all-0.numbers` | `original.numbers` | Only `6010#905589 2.1.1.1.1.4: 2.0 → 0.0`, `6010#905589 2.1.1.1.1.42: 2 → 0`, `6010#905589 3.1.1.5.2.1: 2.0 → 0.0`, `6010#905589 3.1.1.7.1.1.4: 2.0 → 0.0`, `6010#905589 3.1.1.7.1.1.42: 2 → 0` | *Not used*: every copy but field 2 set to 0; the text gives no result |
| `rule-all-0-edited.numbers` | `rule-all-0.numbers` | `6002 5.6: changed`, `6002 5.6 ~ x"19000000000000000000000000003e30"` (2.5) | *Not used*: that with B2 set to 2.5; the text gives no result |
| `rule-all-3-and-522.numbers` | `rule-all-3.numbers` | Only `6010#905589 3.1.1.5.2.2: 2 → 3` | *Not used*: every copy and field 2 set to 3 |

## Confidence

*Confirmed*: field 2 of the rule's value message (3.1.1.5.2.2, and 7.1.5.2.2 for a filter) as the value Numbers compares with, by writing it, and that the cached results are recomputed on opening. *Likely*: the formulas and the double aren't used to evaluate the rule.
