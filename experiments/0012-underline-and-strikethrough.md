# 0012: Underline and strikethrough

**Status:** run

[0007](0007-bold-and-italic.md) mapped the Bold and Italic buttons to fields 11.1 and 11.2 of a character style. This experiment does the same for the other two buttons in the row, Underline and Strikethrough.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0008](0008-runs-and-shared-styles.md), `middle.pages` (the same word made bold) |

## Recipe

As in 0008: AppleScript makes a new document and sets its body text to `one two three`. In the Pages window, double-click `two`, then click one button in the Style tab of the Format sidebar. AppleScript saves the document.

| File | Button |
| --- | --- |
| `underline.pages` | Underline (*understreking*) |
| `strikethrough.pages` | Strikethrough (*gjennomstreket*) |

## Observation

Both files have the same character-style runs as `middle.pages` in 0008: no style from 0, a new style from 4, and no style from 7. The new type-2021 styles differ from 0008's bold style only in field 11:

```
underline.pages       10: varint 1   11: { 11: varint 1 }
strikethrough.pages   10: varint 1   11: { 12: varint 1 }
```

The Body paragraph style (see [0010](0010-alignment.md)) sets both fields to 0.

## Conclusion

Field 11.11 of a style is underline and 11.12 is strikethrough. In both, 1 is what the sidebar button sets and 0 is off.

The format may allow other values, such as for double underlines, which the sidebar buttons don't make. A reader that meets a value other than 0 or 1 should treat it as "on" until an experiment says more.

## Confidence

*Likely*: field 11.11 is underline and 11.12 is strikethrough, with 0 off and 1 for the default line.

*Unknown*: other values. Follow-up: choose a double underline in Pages' Font panel (Format → Font → Show Fonts).
