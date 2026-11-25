# 0455: Looking for a rule's second value

**Status:** run

Highlighting rule kinds 11 and 12 matched every cell when the rule had a single value, so they are probably *between* and *not between*, which need two ([0454](0454-writing-a-rule-s-comparison.md)). The value the rule compares with is in its settings' field 5.2.2 ([0391](0391-writing-a-rule-value.md)), and the settings have a field 6 holding `{ 1: 0 }`. This experiment writes a second value in two places that would fit.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0259/highlight.numbers`: `n` 1, 2, 3, 4 in B2:B5 and rule 905589, whose settings at 3.1.1 have 5 = `{ 1: 1, 2: { 1: 2.0, 2: 2 } }` and 6 = `{ 1: 0 }` |
| Writer | The new [`recipes/0455-append-field.py`](../recipes/0455-append-field.py) and [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0384-pdf-colours.swift`](../recipes/0384-pdf-colours.swift) |

## Recipe

```bash
mkdir -p samples/0455
O=samples/0455
F=samples/0259/highlight.numbers
V3=$(python3 -c "import struct; print((b'\x09' + struct.pack('<d', 3.0) + b'\x10\x03').hex())")
# A second entry in 5.2, beside the first:
for k in 11 12; do
  python3 -I recipes/0302-set-path.py $F $O/x.numbers 905589 3.1.1.1 varint $k
  python3 -I recipes/0455-append-field.py $O/x.numbers $O/kind-$k-repeated.numbers 905589 3.1.1.5 2 $V3
done
# The second value in field 6, shaped like field 5:
for k in 11 12; do
  python3 -I recipes/0302-set-path.py $F $O/kind-$k-2-3.numbers 905589 3.1.1.1 varint $k \
    3.1.1.6.1 varint 1 3.1.1.6.2.1 double 3 3.1.1.6.2.2 varint 3
done
```

Each file was exported and B2:B5 read as in 0454.

## Observation

| Kind | Second value 3 written | Highlighted |
| --- | --- | --- |
| 11 | as a second 5.2 | 1, 2, 3, 4 |
| 12 | as a second 5.2 | 1, 2, 3, 4 |
| 11 | in field 6 | 1, 2, 3, 4 |
| 12 | in field 6 | 1, 2, 3, 4 |

*Between 2 and 3* would highlight 2 and 3 only, and *not between* 1 and 4.

*Corrected 2026-11-25:* the two `-repeated` documents weren't kept, so that part can't be rechecked without making them again.

## Conclusion

Neither place holds a rule's second value: with either written, kinds 11 and 12 still match every cell. Where Numbers keeps the upper bound of *between* is still *unknown*; a rule made with *between* in Numbers would show it.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `kind-11-2-3.numbers` | `0259/highlight.numbers` | Only `6010#905589 3.1.1.1: 7 → 11`, `6010#905589 3.1.1.6.1: 0 → 1`, `6010#905589 3.1.1.6.2: absent → x"0900000000000008401003"` | *Unknown*: where a rule's second value is kept; it isn't field 6, as every cell is highlighted |
| `kind-12-2-3.numbers` | `0259/highlight.numbers` | Only `6010#905589 3.1.1.1: 7 → 12`, `6010#905589 3.1.1.6.1: 0 → 1`, `6010#905589 3.1.1.6.2: absent → x"0900000000000008401003"` | *Unknown*: where a rule's second value is kept; it isn't field 6, as every cell is highlighted |

## Confidence

*Unknown*: where a rule's second value is kept. Ruled out: a second entry in 3.1.1.5.2, and field 3.1.1.6 shaped like field 5.
