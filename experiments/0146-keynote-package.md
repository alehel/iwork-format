# 0146: Keynote in the package format

**Status:** run

[0076](0076-package-format.md) found Pages' folder form, but no data files in it. This experiment saves a Keynote presentation, whose theme brings images, as a package.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0024](0024-keynote-and-numbers.md), `empty-a.key` |

## Recipe

```bash
mkdir -p samples/0146
osascript recipes/0024-empty-iwork-document.applescript Keynote "$PWD/samples/0146/package.key"
```

The saved file was opened in Keynote, changed with File → Advanced → Change File Type → Package, and saved in place through AppleScript, as in 0076.

## Observation

`samples/0146/package.key` is a folder holding `Index.zip`, `Metadata/`, the previews, and a `Data/` folder with the theme's 23 images as separate files. `iwork-probe` reads it as 55 parts, and all 962 objects are reachable from objects 1, 2 and 71.

## Conclusion

Keynote saves the same folder form as Pages. The `.iwa` parts go inside `Index.zip`, while data files go in a `Data/` folder beside it, not inside the ZIP.

## Confidence

*Likely*: in the folder form, data files are in a `Data/` folder beside `Index.zip`.
