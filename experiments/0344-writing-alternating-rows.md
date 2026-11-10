# 0344: Writing alternating row colours

**Status:** run

[0230](0230-alternating-rows.md) found that a table style (type 6003, named by the table model's field 3) shades alternate rows when its property 11.1 is 1. This experiment writes the property into a table's style and samples the exported sheet.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0226/plain.numbers`: one table whose style, record 905007, has no 11.1 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0344
cp samples/0226/plain.numbers samples/0344/plain.numbers
python3 -I recipes/0302-set-path.py samples/0344/plain.numbers samples/0344/alternating.numbers 905007 11.1 varint 1
```

Numbers opened each file on its own and exported it as PDF. The page was drawn and the background's brightness read down a column through the table's empty cells, three quarters of the way across.

## Observation

Runs of brightness down the column, each about 19 points, one row:

| File | Header, then body rows |
| --- | --- |
| `plain.numbers` | 0.75, then 1.00, 1.00, 1.00, 1.00 … |
| `alternating.numbers` | 0.75, then 1.00, 0.96, 1.00, 0.96 … |

## Conclusion

Table style property 11.1 = 1 shades every second body row, starting with the second, in a light grey from the style. The header row keeps its own colour.

## Confidence

*Confirmed*: table style 11.1 turns on alternating rows, by writing it.
