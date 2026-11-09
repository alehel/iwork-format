# 0013: Text colour

**Status:** run

The Body paragraph style (see [0010](0010-alignment.md)) has a field 11.7 that holds a small message of floats, which could be a colour. AppleScript can set the colour of text, so this experiment colours one word and looks for the change.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0008](0008-runs-and-shared-styles.md), `middle.pages` (the same word made bold) |

## Recipe

```bash
mkdir -p samples/0013
R=recipes/0013-coloured-word.applescript
osascript $R "$PWD/samples/0013/red.pages" 65535 0 0
osascript $R "$PWD/samples/0013/blue.pages" 0 0 65535
osascript $R "$PWD/samples/0013/mixed.pages" 32768 16384 0
```

The recipe sets the body text to `one two three` and sets the `color` of word 2 to the given red, green and blue. Pages' AppleScript gives each component a range of 0 to 65535.

## Observation

Each file has the character-style runs of 0008's `middle.pages`: no style from 0, a new style from 4, and no style from 7. The new type-2021 style sets one property (field 10 is 1), and its field 11 holds two copies of the same message, in 11.7 and in 11.46.1:

```
red.pages
  7: message (29 bytes)
    1: varint 1
    3: fixed32 (as float 1)
    4: fixed32 (as float 0.1491003)
    5: fixed32 (as float 0)
    6: fixed32 (as float 1)
    12: varint 1
    13: fixed32 (as float 1)
  46: { 1: (the same 29 bytes) }
```

The colour fields of the three files, and of the Body style:

| File | AppleScript colour | 7.3 | 7.4 | 7.5 | 7.6 |
| --- | --- | --- | --- | --- | --- |
| `red.pages` | 65535, 0, 0 | 1 | 0.1491003 | 0 | 1 |
| `blue.pages` | 0, 0, 65535 | 0.0168419 | 0.19834146 | 1 | 1 |
| `mixed.pages` | 32768, 16384, 0 | 0.57689565 | 0.3204115 | 0 | 1 |
| Body style | (black) | 0 | 0 | 0 | 1 |

Fields 7.1 and 7.12 were 1, and 7.13 was the float 1, in every case.

Setting the mixed colour and reading it back through AppleScript gave `32767, 16381, 652`, not the values set.

An attempt to set an exact colour through the Pages colour panel didn't work. Clicking the colour well in the sidebar opened nothing the test could drive, so no sample was saved from it.

## Conclusion

Field 11.7 of a style is the text colour. Fields 3, 4 and 5 hold the red, green and blue components as floats from 0 to 1, and field 6 holds the alpha. Black is 0, 0, 0 with alpha 1.

The stored components aren't the AppleScript values divided by 65535. Pure red came out with green at 0.149, pure blue with red at 0.017 and green at 0.198, and the round trip through AppleScript changed the colour slightly. So Pages converts between the colour space AppleScript uses and the one it stores. This experiment can't say which space is stored. Fields 7.1 and 7.12 may name it, and both were 1 throughout.

Field 11.46.1 repeated the same colour in every file. Its purpose is unknown.

## Confidence

*Likely*:

- Field 11.7 is the text colour, with RGB components in 7.3–7.5 and alpha in 7.6.
- Black is stored as 0, 0, 0, 1.

*Unknown*:

- The colour space of the stored components, and the meaning of fields 7.1, 7.12 and 7.13. Follow-up: set an exact sRGB colour by its hex value through the Pages colour panel. If the stored components then match it, the stored space is sRGB.
- What field 11.46 is for.
