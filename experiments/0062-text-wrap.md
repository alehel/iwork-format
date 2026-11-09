# 0062: Text wrap in a cell

**Status:** run

[0043](0043-cell-styles.md) found that a cell's background is kept in a cell style (type 6004). This experiment changes a cell's vertical alignment and text wrap, to find more of the cell style's fields.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0043](0043-cell-styles.md) |

## Recipe

```bash
mkdir -p samples/0062
osascript recipes/0061-numbers-alignment.applescript "$PWD/samples/0062/top-nowrap.numbers" top-nowrap
```

The recipe sets B2 to `abc`, its `vertical alignment` to `top` and its `text wrap` to false. Reading a fresh cell through AppleScript showed that `top` and wrapping are the defaults, so only the wrap setting changed anything.

## Observation

The cell's flags are 0x00021028: 0x8 (string), 0x20 (cell style), 0x1000 and 0x20000. Its cell style key names record 905247, of type 6004:

```
10: 1
11: { 3: 0 }
```

## Conclusion

Field 11.3 of a cell style is text wrap, and 0 turns it off. Setting top alignment, already the default, added nothing to the style, so Numbers only stores what differs from its parent. Field 10 is 1, which agrees with it counting the properties a style sets. The background colour is field 11.1 ([0043](0043-cell-styles.md)).

## Confidence

*Likely*: cell style field 11.3 is text wrap, with 0 for off.

*Unknown*: where vertical alignment is stored. Follow-up: set it to bottom.
