# 0127: A text box on a sheet

**Status:** run

[0047](0047-second-table.md) found a sheet's drawables in its field 2. This experiment adds a text box to a sheet.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0024](0024-keynote-and-numbers.md), `empty-a.numbers` |

## Recipe

```bash
mkdir -p samples/0127
osascript recipes/0113-numbers-variants.applescript "$PWD/samples/0127/textbox.numbers" textbox
```

## Observation

The recipe adds a text item `note` to sheet 1. `Document.iwa` gained a type-2011 shape (905230) and its type-2001 text (`note`, no field 1). The sheet's field 2 now lists 904769 (the table's drawable) and 905230. The sheet's own text (904667) still holds a single U+FFFC.

## Conclusion

A text box on a sheet is the same type-2011 shape as in Pages and Keynote, and joins the sheet's list of drawables (field 2).

## Confidence

*Likely*: sheet field 2 lists every drawable on the sheet, of any type.
