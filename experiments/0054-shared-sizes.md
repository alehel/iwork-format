# 0054: Shared sizes

**Status:** run

[0008](0008-runs-and-shared-styles.md) found that two words made bold in the Pages window share one style. This experiment sets sizes through AppleScript instead, giving two words the same size and one a different size, to see whether styles are shared the same way.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0008](0008-runs-and-shared-styles.md), `two-words.pages` |

## Recipe

```bash
mkdir -p samples/0054
osascript recipes/0054-pages-sizes.applescript "$PWD/samples/0054/sizes.pages"
```

The recipe sets the body text to `one two three`, then the `size` of word 1 to 14, word 2 to 20 and word 3 to 14.

## Observation

The character-style runs:

```
{ 1: 0, 2: { 1: 1732647 } }     one     (14 pt)
{ 1: 3 }                        space
{ 1: 4, 2: { 1: 1732650 } }     two     (20 pt)
{ 1: 7 }                        space
{ 1: 8, 2: { 1: 1732647 } }     three   (14 pt)
```

The stylesheet gained two type-2021 styles: 1732647 with 11.3 = 14 and 1732650 with 11.3 = 20. Both inherit from the null character style.

Pages reported `one` and `three` at 14 points and `two` at 20, and the 0033 rule predicted the same.

## Conclusion

Ranges given the same formatting share one style object even when they are set separately through AppleScript: `one` and `three` both point at 1732647. The spaces between the words, which weren't changed, have runs with no style.

## Confidence

*Confirmed*: ranges with the same formatting share one style ([0008](0008-runs-and-shared-styles.md) through the window, and this experiment through AppleScript).
