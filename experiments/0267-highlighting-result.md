# 0267: Where the highlighting result is kept

**Status:** run

[0259](0259-conditional-highlighting.md) found that cells under a conditional highlighting rule gain flag bits 0x80 and 0x100, each followed by a key. It concluded that the match isn't cached, but compared only the flags, not the keys of matching and non-matching cells. This experiment compares the keys, using the sample from 0259.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| Date | 2026-11-09 |
| Sample | `samples/0259/highlight.numbers`: n = 1, 2, 3, 4 in B2–B5, highlighted where greater than 2 |

## Recipe

Each cell of column B in `Index/Tables/Tile.iwa` was split as in [0031](0031-cell-kinds.md), and the 32-bit keys after the decimal value were read in the order of their flag bits.

## Observation

All four cells have the flags 0x3181 and four keys:

| Cell | Value | Matches | Key for 0x80 | Key for 0x100 | 0x1000 | 0x2000 |
| --- | --- | --- | --- | --- | --- | --- |
| B2 | 1 | no | 1 | 15 | 1 | 2 |
| B3 | 2 | no | 1 | 15 | 1 | 2 |
| B4 | 3 | yes | 1 | 0 | 1 | 2 |
| B5 | 4 | yes | 1 | 0 | 1 | 2 |

## Conclusion

The key for flag 0x80 is the cell's entry in the conditional-format list (type 9), here entry 1, shared by all four cells. The key for flag 0x100 records the result: 0 where the cell matches, and 15 where it doesn't. 0 is most likely the index of the first rule that matched, and 15 a value meaning none. So Numbers does cache which rule applies to each cell, and a reader can show the highlighting without evaluating the rule. This corrects the conclusion of 0259.

## Confidence

*Likely*:

- Flag 0x80's key is the cell's conditional-format entry.
- Flag 0x100's key is the matching rule, 15 for none.

*Unknown*: the value for a second rule. Follow-up: two rules matching different cells.
