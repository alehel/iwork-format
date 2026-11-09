# 0154: Replacing formatted text

**Status:** run

This experiment formats a word and then replaces the whole body text, to see whether the formatting stays.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0020/plain.pages` (the body text `one`) |

## Recipe

```bash
mkdir -p samples/0154
osascript recipes/0149-pages-text.applescript replace "$PWD/samples/0154/replace.pages"
```

## Observation

The recipe makes word 2 of `one two three` 20 points, then sets the body text to `four five`. The body record is the same as `one`'s apart from the text: no character-style runs. The 20-point style is gone from `DocumentStylesheet.iwa`.

## Conclusion

Setting the body text replaces the formatting with the paragraph's style. Pages also drops the character style that nothing uses any more, as it drops unused data files ([0145](0145-deleted-image.md)).

## Confidence

*Likely*: unused character styles are removed on save.
