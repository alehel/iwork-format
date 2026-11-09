# 0142: The same image twice

**Status:** run

This experiment places the same image file twice, to see whether its data is stored twice.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0023](0023-an-image.md) |

## Recipe

```bash
mkdir -p samples/0142
osascript recipes/0139-pages-container.applescript twice "$PWD/samples/0142/twice.pages" "$PWD/samples/0023/red-8x4.png"
```

## Observation

`Document.iwa` has two image records (type 3005), but the package has one data file, `Data/red-8x4-24.png`, and `Metadata.iwa` one data entry for it (ID 24).

## Conclusion

Images with the same file share one data file and one data ID. A reader may find the same data ID in several image records.

## Confidence

*Likely*: identical image files are stored once.
