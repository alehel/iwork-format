# 0234: Gridlines

**Status:** run

The Format sidebar's Table tab has five buttons that turn gridlines on and off. This experiment turns off the first, the horizontal lines between body rows.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0230/plain.numbers` |

## Recipe

```bash
mkdir -p samples/0234
osascript recipes/0230-numbers-blank.applescript
```

Then click the first Gridlines (*Rutenett*) button in the Table tab. The horizontal lines between body rows disappear. Save as `samples/0234/no-horizontal-lines.numbers`.

## Observation

The table model's field 3 now names a new table style (type 6003). The new style differs from the old one only in field 10 (1 → 2) and in one added property:

```
11.34: 0
```

## Conclusion

Gridlines are table style properties, like alternating rows ([0230](0230-alternating-rows.md)). Property 34 is the horizontal gridlines of the body, and 0 turns them off. A new table doesn't store the property, so it shows them. The other four buttons are probably neighbouring properties: vertical body lines, and the lines of header rows, header columns and footer rows.

## Confidence

*Likely*: table style property 34 = 0 hides the body's horizontal gridlines.

*Unknown*: the properties of the other four gridline buttons.
