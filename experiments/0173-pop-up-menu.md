# 0173: A pop-up menu

**Status:** run

This experiment tries to give a cell the pop-up menu format.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0036](0036-more-cell-formats.md), `formats.numbers` |

## Recipe

```bash
mkdir -p samples/0173
osascript recipes/0169-numbers-controls.applescript popup "$PWD/samples/0173/popup.numbers"
```

Cell B2 of table 1 is decoded from `Index/Tables/Tile.iwa` as in [0036](0036-more-cell-formats.md).

## Observation

Numbers accepted the script, but read the cell back with the format `text` and the value `x`. B2 is a text cell (type 3) with flags 0x00021008, the same as the text-format cell F2 in 0036. There's no cell-control entry.

## Conclusion

Setting the pop-up menu format through AppleScript didn't take, probably because a pop-up menu needs a list of choices that the script can't give. This experiment found nothing about pop-up menus. Making one will need Numbers' own interface.

## Confidence

*Unknown*: how a pop-up menu is stored.
