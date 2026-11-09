# 0124: Renaming a sheet

**Status:** run

[0037](0037-second-sheet.md) took a sheet's field 1 to be its name. This experiment renames a sheet.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0024](0024-keynote-and-numbers.md), `empty-a.numbers` |

## Recipe

```bash
mkdir -p samples/0124
osascript recipes/0113-numbers-variants.applescript "$PWD/samples/0124/sheetname.numbers" sheetname
```

## Observation

The recipe sets the sheet's name to `Data`. The sheet record (type 2) changed field 1 from `Ark 1` to `Data`.

## Conclusion

A sheet's field 1 is its name.

## Confidence

*Confirmed*: sheet field 1 is the name ([0037](0037-second-sheet.md) and this experiment).
