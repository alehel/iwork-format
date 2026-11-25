# 0315: Writing the function a formula calls

**Status:** run

Formulas are kept in the table's formula list as postfix lists of nodes, and a function call is node type 16 with the function's number in field 2: 15 AVERAGE, 126 ROUND, 168 SUM and so on ([0103](0103-round.md), [0104](0104-nested-functions.md), [0223](0223-functions.md)). AppleScript reads a cell's `formula` as text and its `value`. This experiment changes one function number and asks Numbers.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0104/nested.numbers`: B2 = 4, C2 = 2 and E2 = ROUND(AVERAGE(B2:C2) × 1.5; 0), which is 5 |
| Writer | [`recipes/0315-formula-function.py`](../recipes/0315-formula-function.py), using the writer of [0287](0287-rewriting-a-document.md) |

## Recipe

```bash
mkdir -p samples/0315
cp samples/0104/nested.numbers samples/0315/original.numbers
python3 -I recipes/0315-formula-function.py samples/0315/original.numbers samples/0315/sum.numbers 904540 15 168
```

The formula list (record 904540) holds E2's formula as six nodes: a range (67), function 15 with one argument, the number 1.5, multiplication (3), the number 0 and function 126 with two arguments. The script changes function 15 to 168 and leaves E2's cached value, 5. Numbers opened each file on its own and read the cells through AppleScript; the written file was saved again.

## Observation

| File | E2 formula (as Numbers shows it in Norwegian) | E2 value |
| --- | --- | --- |
| `original.numbers` | `=AVRUND(GJENNOMSNITT(B2:C2)×1,5;0)` | 5 |
| `sum.numbers` | `=AVRUND(SUMMER(B2:C2)×1,5;0)` | 9 |

ROUND((4 + 2) × 1.5; 0) = 9. In `sum.numbers` the cell still caches 5; saved again, it caches 9, as a decimal128 with coefficient 90.

## Conclusion

Function number 168 is SUM and 15 AVERAGE, and a formula can be changed by writing its nodes. Numbers recalculates formulas when it opens a document, so a writer doesn't have to update the cached result, though other readers that trust the cache will show the old value until the app saves again. The cached 9 was stored as 90 × 10⁻¹: a decimal128 isn't normalised.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `original.numbers` | `0104/nested.numbers` | `same bytes` | *Control*: E2 rounds an average and shows 5 |
| `sum.numbers` | `original.numbers` | Only `6005#904540 3.5.1.1.2: 15 → 168` | *Confirmed*: function 15 is AVERAGE and 168 SUM; Numbers shows SUM and 9 |
| `sum-resaved.numbers` | `sum.numbers` | `6002 5.6: changed`, `6002 5.6 ~ x"5a000000000000000000000000003e30"` | *Confirmed*: Numbers recalculates on opening; the saved cell caches 9 |

## Confidence

*Confirmed*: function numbers 15 and 168, and function-call nodes, by writing them; Numbers recalculates on opening.
