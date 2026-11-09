# 0259: Conditional highlighting

**Status:** run

Numbers can style cells that meet a rule (Format → Conditional Highlighting). [0258](0258-filter.md) found that a filter's rule is stored as a formula. This experiment adds a highlighting rule with the same condition, n greater than 2, to compare.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0226/plain.numbers` |

## Recipe

```bash
mkdir -p samples/0259
osascript recipes/0226-numbers-grouping-data.applescript B2:B5
```

The recipe fills table 1 as in [0226](0226-category.md) and selects the `n` cells, B2:B5. Then, with Numbers in front:

1. Choose Format → Conditional Highlighting (*Format → Betinget utheving…*), Add a Rule → Number → Greater Than (*Legg til en regel → Tall → Større enn*), type 2, keep the default style Green Fill (*Grønt fyll*), and click Done. The cells holding 3 and 4 turn green.
2. Save it as `samples/0259/highlight.numbers`.

## Observation

The table model's list of type 9 (`DataList-904538.iwa`), empty before, gains one entry naming a type-6010 record:

```
2: { 1: { 1: formula,      ← node 63 (with the table's UUID in 28.1), the number 2, node 7 (>)
          2: 7, 5: 1, … },
     2: { 1: 905591 },    ← a type-6004 cell style: fill 0.686, 0.894, 0.537, alpha 0.9
     3: { 1: 905590 } }   ← a type-2022 text style named "Grønt fyll", black text
3: the rule again, in the layout of the filter's type-6220 records
```

The two styles are in a new part, `ObjectContainer.iwa`, under a type-11008 root (object 61), as chart styles are ([0067](0067-chart.md)).

The cells B2–B5 have the flags 0x3181 instead of 0x3001: bits 0x80 and 0x100 are added, with two more keys after the value. The cells' values are unchanged.

## Conclusion

A conditional highlighting rule is a type-6010 record in the table's list of type 9. It holds:

- **The condition:** a formula in the node form of cell formulas, as in a filter. Here it starts with node type 63 rather than a cell reference (36). Type 63 names only the table, so it probably stands for "the cell being tested".
- **The style to apply when the condition holds:** a cell style for the fill and a text style for the text, both kept in `ObjectContainer.iwa`.

The comparison's kind also appears as a number (7, `>`) outside the formula. Cells under a rule get new flag bits, one of which probably keys them to the rule. Numbers doesn't store whether each cell currently matches, so a reader that wants the highlighting has to evaluate the rule.

## Confidence

*Likely*:

- Highlighting rules are type-6010 records in the type-9 list, holding a formula and two styles.
- Node 63 is the tested cell.

*Unknown*:

- The meaning of cell flags 0x80 and 0x100 and their keys.
- Whether the match is cached anywhere. Follow-up: compare the keys of a matching and a non-matching cell.
