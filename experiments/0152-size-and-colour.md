# 0152: Size and colour on one word

**Status:** run

This experiment gives one word both a size and a colour, to see whether they share a character style.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiments [0004](0004-larger-word.md) and [0013](0013-text-colour.md) |

## Recipe

```bash
mkdir -p samples/0152
osascript recipes/0149-pages-text.applescript sizecolour "$PWD/samples/0152/sizecolour.pages"
```

## Observation

The character-style runs are as for one formatted word: none from 0, style 1732650 from 4, none from 7. Style 1732650 (type 2021) has field 10 = 2, and in field 11 the size (11.3 = 20) and the colour (11.7, with the same values as `red.pages` in 0013: 1, 0.149, 0, 1), repeated in 11.46.1.

## Conclusion

Two properties on the same range go into one character style. As [0010](0010-alignment.md) found, field 10 matched the number of properties set: 1 for the one-property styles of 0013 and 0149, and 2 here, not counting 11.46. Body's 57 doesn't match exactly, as it sets 59 fields in 11 and 12.

## Confidence

*Likely*: formatting on one range goes into one character style.

*Unknown*: what field 10 counts. It matches the properties set in small styles, but not quite in Body.
