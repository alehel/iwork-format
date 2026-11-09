# 0235: The other gridline buttons

**Status:** run

[0234](0234-gridlines.md) found that the first gridline button sets table style property 34. This experiment clicks each of the other four buttons, one per new spreadsheet, to find their properties.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0230/plain.numbers` |

## Recipe

For each of the second to fifth Gridlines (*Rutenett*) buttons in the Table tab:

```bash
mkdir -p samples/0235
osascript recipes/0230-numbers-blank.applescript
```

then click the button and save as `samples/0235/buttonN.numbers`. The sidebar groups the buttons in two sets: two for the body (horizontal and vertical lines), and three for the header rows, header columns and footer rows.

## Observation

Each change makes a new table style (type 6003) that differs from the plain one in field 10 (1 → 2) and one property:

| Button | Property |
| --- | --- |
| 1, from 0234 | 11.34: 0 |
| 2 | 11.33: 0 |
| 3 | 11.42: 0 |
| 4 | 11.43: 0 |
| 5 | none: the style is unchanged |

## Conclusion

Each gridline button turns off one table style property:

- 34: horizontal lines in the body.
- 33: vertical lines in the body.
- 42: lines in the header rows.
- 43: lines in the header columns.

These meanings follow the order of the sidebar's icons, which wasn't checked visually for buttons 3 and 4. The fifth button, for footer rows, had no effect: a new table has no footer rows, so it is probably disabled. A reader draws a set of gridlines unless its property is 0.

## Confidence

*Likely*: properties 33 and 34 are the body's vertical and horizontal gridlines.

*Unknown*:

- Which of 42 and 43 is header rows and which is header columns.
- The footer rows' property. Follow-up: repeat the fifth button on a table with a footer row.
