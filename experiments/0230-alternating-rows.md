# 0230: Alternating row colour

**Status:** run

The Format sidebar's Table tab can shade every other row. This experiment turns that on, to find where table-wide options are kept.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0230/plain.numbers`, a new document from the same recipe |

## Recipe

```bash
mkdir -p samples/0230
osascript recipes/0230-numbers-blank.applescript
```

Then tick Alternating Row Colour (*Annenhver rad*) in the Table tab and save as `samples/0230/alternating.numbers`. For the baseline, run the recipe again and save without changes.

## Observation

In the table model (type 6001), only field 3 changes: it named 905007 and now names 905230, a new record of type 6003 in `DocumentStylesheet.iwa`. The two type-6003 records differ in:

| Field | Before (905007) | After (905230) |
| --- | --- | --- |
| 10 | 1 | 2 |
| 11.1 | absent | 1 |

The rest of field 11, a 4-kilobyte block whose field 32 holds the default cell styles, is unchanged. Field 1.3 of the new record names the theme's table style as its parent.

## Conclusion

Table model field 3 is the table's style, a type-6003 table style in the stylesheet. Table-wide options such as alternating row colour live there, as properties in field 11: 11.1 = 1 shades alternate rows. As with text styles, changing an option makes a new style that inherits from the previous one. Field 10 is probably the style's version or a count of changed properties.

## Confidence

*Likely*: table model field 3 is the table style (type 6003), and its property 11.1 turns on alternating row colour.

*Unknown*: field 10 of the table style, and what colour the alternate rows get.
