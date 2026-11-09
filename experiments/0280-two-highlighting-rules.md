# 0280: Two highlighting rules

**Status:** run

[0267](0267-highlighting-result.md) found that each highlighted cell caches its result in the key of flag 0x100: 0 where the single rule matched and 15 where it didn't. It guessed that 0 is the index of the matching rule. This experiment adds a second rule, to test that.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiments [0259](0259-conditional-highlighting.md) and [0267](0267-highlighting-result.md) |

## Recipe

```bash
mkdir -p samples/0280
osascript recipes/0226-numbers-grouping-data.applescript B2:B5
```

Then, with Numbers in front, open Format → Conditional Highlighting and add two Number rules to B2:B5:

1. Greater Than 2, with the default Green Fill.
2. Less Than 2, which gets the default Red Fill.

The cell holding 1 turns red, 3 and 4 turn green, and 2 stays plain. Save as `samples/0280/two-rules.numbers`.

## Observation

| Cell | Value | Rule matched | Key for 0x80 | Key for 0x100 |
| --- | --- | --- | --- | --- |
| B2 | 1 | second (< 2) | 2 | 1 |
| B3 | 2 | none | 2 | 15 |
| B4 | 3 | first (> 2) | 2 | 0 |
| B5 | 4 | first (> 2) | 2 | 0 |

## Conclusion

Flag 0x100's key is the index, from 0, of the first rule a cell matches, or 15 when it matches none. So a reader can apply the highlighting from the cells alone: look up the cell's entry in the conditional-format list (flag 0x80's key, here 2), then take that entry's rule at the cached index and apply its style. 15 is probably a "none" value rather than a limit, but more than 15 rules weren't tested.

## Confidence

*Confirmed*, with 0267: flag 0x100's key caches which rule matched, by index, with 15 for none.
