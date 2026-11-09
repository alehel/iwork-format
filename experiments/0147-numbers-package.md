# 0147: Numbers in the package format

**Status:** run

This experiment saves a Numbers spreadsheet as a package, to complete the folder form for all three apps.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0024](0024-keynote-and-numbers.md), `empty-a.numbers` |

## Recipe

```bash
mkdir -p samples/0147
osascript recipes/0024-empty-iwork-document.applescript Numbers "$PWD/samples/0147/package.numbers"
```

The saved file was changed to Package and saved in place as in 0146.

## Observation

`samples/0147/package.numbers` is a folder holding `Index.zip`, `Metadata/`, the previews and a `Data/` folder. `iwork-probe` reads it as 44 parts, including the table parts under `Index/Tables/` inside `Index.zip`. All 626 objects are reachable.

## Conclusion

Numbers saves the same folder form as Pages and Keynote. All three apps share it, so a reader can open folder documents from any of them the same way.

## Confidence

*Confirmed*: the folder form, with `.iwa` parts in `Index.zip`, is shared by all three apps ([0076](0076-package-format.md), [0146](0146-keynote-package.md) and this experiment).
