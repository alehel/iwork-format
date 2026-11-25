# 0153: Setting a size a word already has

**Status:** run

This experiment sets a word to the size it already has, to see whether Pages makes a style anyway.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0020/plain.pages` (the body text `one`) |

## Recipe

```bash
mkdir -p samples/0153
osascript recipes/0149-pages-text.applescript defaultsize "$PWD/samples/0153/defaultsize.pages"
```

## Observation

The recipe reads word 2's size and sets it again. The body record is the same as `one`'s, apart from the text: there are no character-style runs (field 8), and `DocumentStylesheet.iwa` has the same size.

## Conclusion

Setting a property to the value it already resolves to makes no style. A reader won't find redundant character styles from that, though one made in other ways might still repeat an inherited value.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `defaultsize.pages` | `0020/plain.pages` | `2001 3: "one" → "one two three"`, `2001 8: ×0 → ×0`, `records 2021: 8 → 8` | *Likely*: setting a size a word already has stores nothing |

## Confidence

*Likely*: setting a property to its current value doesn't store anything.
