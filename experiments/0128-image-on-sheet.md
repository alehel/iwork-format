# 0128: An image on a sheet

**Status:** run

This experiment places an image on a sheet.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0024](0024-keynote-and-numbers.md), `empty-a.numbers` |

## Recipe

```bash
mkdir -p samples/0128
osascript recipes/0113-numbers-variants.applescript "$PWD/samples/0128/image.numbers" image "$PWD/samples/0023/red-8x4.png"
```

## Observation

The recipe places the PNG of 0023 on sheet 1. `Document.iwa` gained an image record (type 3005), which the sheet's field 2 now lists after the table. The package gained `Data/red-8x4-16.png`.

## Conclusion

Images on a sheet are the same records and data files as in Pages and Keynote, listed in the sheet's field 2.

## Confidence

*Likely*: images are stored the same way in all three apps.
