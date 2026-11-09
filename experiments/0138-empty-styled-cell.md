# 0138: A styled empty cell

**Status:** run

[0043](0043-cell-styles.md) found a cell's background in a cell style. This experiment colours an empty cell's background in a Pages table, to see how a cell with style but no value is stored.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0043](0043-cell-styles.md) |

## Recipe

```bash
mkdir -p samples/0138
osascript recipes/0131-app-table.applescript Pages "$PWD/samples/0138/fill.pages" fill
```

The recipe makes a 5 × 5 table through Pages's AppleScript, using the same table commands as Numbers'.

## Observation

The recipe sets B2's `background color` to red without giving it a value. The tile has one cell:

```
05 00 00 00 00 00 00 00 20 00 00 00 01 00 00 00
```

That is type 0, flags 0x0020 (a cell style) and the style key 1.

## Conclusion

A cell with formatting but no value is stored as type 0, with no value flags, only its style keys. A reader draws its background but shows no content.

## Confidence

*Likely*: cell type 0 is a cell with no value.
