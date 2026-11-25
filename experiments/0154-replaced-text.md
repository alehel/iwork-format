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

*Corrected 2026-11-25:* the stylesheet (type 401) still names the ID 1732647, which no record has, in fields 1.1 and 5.2.1, as it also does in [0152](0152-size-and-colour.md)'s `sizecolour.pages`.

## Conclusion

Setting the body text replaces the formatting with the paragraph's style. Pages also drops the character style that nothing uses any more, as it drops unused data files ([0145](0145-deleted-image.md)).

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `replace.pages` | `0020/plain.pages` | `2001 3: "one" → "four five"`, `2001 8: ×0 → ×0`, `records 2021: 8 → 8`, `2021 11.3 ≠ 20.0` | *Likely*: an unused character style is removed on save |

## Confidence

*Likely*: unused character styles are removed on save.
