# 0144: A file name with spaces and ø

**Status:** run

This experiment places an image whose file name has a space and a non-ASCII letter, to see how the data file is named in the ZIP file.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0023](0023-an-image.md) |

## Recipe

```bash
mkdir -p samples/0144
cp samples/0023/red-8x4.png "samples/0144/rød bilde.png"
osascript recipes/0139-pages-container.applescript image "$PWD/samples/0144/odd-name.pages" "$PWD/samples/0144/rød bilde.png"
```

## Observation

`Metadata.iwa` names the data file `rød bilde-24.png`. In the ZIP file, the entry's name is those characters' UTF-8 bytes (`72 c3 b8 64 20 …`), but the entry doesn't set the ZIP flag that marks a name as UTF-8. Python's `zipfile` therefore reads the name as `r├╕d bilde-24.png`, and so did `iwork-probe` until this experiment.

## Conclusion

Pages writes ZIP entry names in UTF-8 without saying so. A reader must decode entry names as UTF-8 whatever the flag says, or names with non-ASCII letters won't match the names in `Metadata.iwa`. `iwork-probe` now does this.

Spaces are kept, and the data ID is added before the extension as usual.

## Confidence

*Likely*: ZIP entry names are UTF-8 without the UTF-8 flag.
