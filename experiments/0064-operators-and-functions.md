# 0064: Operators and functions

**Status:** run

[0031](0031-cell-kinds.md) and [0035](0035-formula-references.md) found the formula nodes for numbers, cell references, ranges, addition, multiplication and one function (168). [0044](0044-merged-cells.md) then raised doubts about whether 168 is SUM. This experiment writes formulas with more operators and functions, to map their numbers.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0035](0035-formula-references.md) |

## Recipe

```bash
mkdir -p samples/0064
osascript recipes/0064-numbers-functions.applescript "$PWD/samples/0064/functions.numbers"
```

The recipe sets B2 to 4 and C2 to 2, then writes nine formulas in E2 to E10. The formula list was printed as node types with a throwaway script, and each cell's shown value was read back through AppleScript.

## Observation

| Cell | Formula | Shown | Nodes, in postfix order |
| --- | --- | --- | --- |
| E2 | `=B2-C2` | 2 | 36 36 **2** |
| E3 | `=B2/C2` | 2 | 36 36 **4** |
| E4 | `=B2^2` | 16 | 36 17(2) **5** |
| E5 | `=B2&C2` | 42 | 36 36 **6** |
| E6 | `=AVERAGE(B2:C2)` | 3 | 67 16(function **15**, 1 argument) |
| E7 | `=MIN(B2:C2)` | 2 | 67 16(function **88**, 1) |
| E8 | `=MAX(B2:C2)` | 4 | 67 16(function **84**, 1) |
| E9 | `=IF(B2>1,1,0)` | empty | (no entry) |
| E10 | `=COUNT(B2:C2)` | 2 | 67 16(function **30**, 1) |

The formula list's keys 1–8 follow the order of the cells that hold formulas.

## Conclusion

Operator nodes, together with those from 0031 and 0035:

| Node | Operator |
| --- | --- |
| 1 | `+` |
| 2 | `-` |
| 3 | `*` |
| 4 | `/` |
| 5 | `^` |
| 6 | `&` (join text) |

Function numbers (node 16, field 2): AVERAGE 15, COUNT 30, MAX 84, MIN 88, and SUM 168 ([0035](0035-formula-references.md)). They rise in the alphabetical order of the English names, which makes SUM = 168 likely. So the node `16, 168` that ended the merged range in 0044 really is SUM, and what it does there is still open.

The IF formula was rejected and left E9 empty. In Norwegian, Numbers separates function arguments with `;`, not `,`, so the formula was probably invalid as typed.

## Confidence

*Likely*: the operator nodes 1–6, and the function numbers 15, 30, 84, 88 and 168, which seem to be numbered in alphabetical order.

*Unknown*:

- Comparison operators and IF. Follow-up: write `=IF(B2>1;1;0)` with semicolons.
- The function numbering beyond these five.
