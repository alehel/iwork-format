# 0233: A border around the table title

**Status:** run

[0230](0230-alternating-rows.md) found that some table options live in the table style, and [0232](0232-hidden-table-title.md) that showing the title is a table model field. This experiment turns on the border around the table title, to see which of the two holds it.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0230/plain.numbers` |

## Recipe

```bash
mkdir -p samples/0233
osascript recipes/0230-numbers-blank.applescript
```

Then tick Outline Table Title (*Kantlinje rundt tabelltittel*) in the Table tab and save as `samples/0233/title-border.numbers`.

## Observation

The table model (type 6001) gains field 37 with the value 1. Its field 3 still names the same table style, so no new style is made.

## Conclusion

Table model field 37 is 1 when the table's title has a border around it. Like field 22 (the title shown), it is a table model field, not a style property. Options about the title sit in the model, and options about the cells in the style.

## Confidence

*Likely*: table model field 37 is the border around the title.
