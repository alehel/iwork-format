# 0145: A deleted image

**Status:** run

This experiment places an image and deletes it before saving, to see whether its data is left behind.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0023](0023-an-image.md) |

## Recipe

```bash
mkdir -p samples/0145
osascript recipes/0139-pages-container.applescript deleted "$PWD/samples/0145/deleted.pages" "$PWD/samples/0023/red-8x4.png"
```

## Observation

The package has no `Data/` files, and `Metadata.iwa` record 2 has no data entry for the image. Only the template's entries remain.

## Conclusion

Data that nothing uses is dropped when the document is saved. A reader doesn't have to skip unused files.

## Confidence

*Likely*: unused data files and their entries are removed on save.
