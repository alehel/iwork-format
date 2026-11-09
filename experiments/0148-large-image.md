# 0148: A large image

**Status:** run

Keynote's theme images include files named `…-small-N`. This experiment places a large image in Pages, to see whether Pages makes such a copy.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0023](0023-an-image.md) |

## Recipe

```bash
mkdir -p samples/0148
# a 3000 × 2000 PNG made with a short Python script (a colour gradient, 1.58 MB)
osascript recipes/0139-pages-container.applescript image "$PWD/samples/0148/large.pages" "$PWD/samples/0148/gradient-3000x2000.png"
```

## Observation

The package holds two data files:

- `Data/gradient-3000x2000-24.png`, 1,580,847 bytes: the placed file, unchanged.
- `Data/gradient-3000x2000-small-25.png`, 32,505 bytes: a smaller copy.

`Metadata.iwa` has data entries for both, the second named `gradient-3000x2000-small.png`. The image record names data 24 in its field 11 and data 25 in its field 12.

## Conclusion

For a large image, Pages stores the original and a reduced copy for display, each with its own data ID. The image record names the original in field 11 and the reduced copy in field 12. A reader can draw the small copy quickly and use the original when it needs full resolution.

## Confidence

*Likely*: image field 12 names a reduced copy, made for large images.

*Unknown*: above what size Pages makes one.
