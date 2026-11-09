# 0044: Merged cells

**Status:** run

This experiment merges a block of cells in a Numbers table, to see where a merge is recorded and where the merged cell's value goes.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0024](0024-keynote-and-numbers.md), `empty-a.numbers`; experiment [0026](0026-numbers-cells.md), `cells.numbers` |

## Recipe

```bash
mkdir -p samples/0044
osascript recipes/0044-numbers-merge.applescript "$PWD/samples/0044/merged.numbers"
```

The recipe merges the range B2:C3 of the first table and sets B2 to 42.

## Observation

The tile holds one row entry with one cell, at row 1, column 1 (B2), with the value 42. No other cell is stored.

The table model (type 6001) differs from the empty spreadsheet's in field 47.2:

```
empty:   47.2: { 2: 0 }
merged:  47.2: { 2: 1,
                 3: { 1: 0,
                      2: { 1: { 1: 67,                                  ← a range node
                                28: { 1: { 2: …, 3: …, 4: …, 5: … } },  ← four large varints
                                33: { 1: 1, 2: 1, 3: 1, 4: 1 },
                                40: { 3: { 1: 2 }, 4: { 1: 1, 2: 2 }, 5: 1 } },
                           { 1: 16, 2: 168, 3: 1 } } } }
```

## Conclusion

A merge is recorded in the table model, not in the cells. Field 47.2 holds the merged ranges: 47.2.2 is probably their count, and 47.2.3 holds each range as an expression in the same node format as formulas ([0035](0035-formula-references.md)). The merged cell keeps its value in its top-left cell. The other cells of the range are simply absent from the tile.

The range node differs from the one in `=SUM(B2:C3)`. It has a field 28, like the four 32-bit parts of a UUID, probably naming the table, and a field 33 of four 1s, probably the absolute flags of the range's four edges. Its field 40 uses parts 3 and 4 instead of 1 and 2. Field 40.4 = {1, 2} fits columns 1 to 2 (B to C) as absolute indices. Field 40.3 = {1: 2}, with no field 2, doesn't obviously fit rows 1 to 2, so how this form encodes rows is open. The expression also ends with the node `16, 168, 1`, which in 0035 belonged to `SUM`, so 168 may not mean SUM in particular.

## Confidence

*Likely*:

- Merges are kept in table model field 47.2, as ranges in formula node form.
- A merged cell's value is in its top-left cell.

*Unknown*:

- The absolute range form (fields 28, 33, 40.3 and 40.4) and the trailing node.
- What function number 168 is. Follow-up: merge a range of a different shape (one row, three columns) and a second range, and write formulas with other functions.
