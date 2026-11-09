# 0246: Header rows repeated on each page

**Status:** run

A Pages table that runs over several pages can repeat its header rows at the top of each page. The Format → Table menu has a toggle for this. This experiment toggles it on a new table, to find the field.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0246/plain-table.pages`, the same table untouched |

## Recipe

For the sample:

1. Make a document with the body text `One`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "One"'
   ```
2. Choose Insert → Table → Header Cells (*Sett inn → Tabell → Tittelceller*). The new table is selected.
3. Choose Format → Table → Repeat Header Rows on Each Page (*Format → Tabell → Repeter tittelrader på hver side*).
4. Save it as `samples/0246/no-repeat.pages`.

For the baseline, repeat steps 1 and 2 and save as `samples/0246/plain-table.pages`.

## Observation

Apart from IDs and UUIDs, the table models (type 6001) differ in one field. The untouched table has

```
29: 1
```

and after the menu command the field is gone. So the option is on in a new table, and the menu turned it off.

## Conclusion

Table model field 29 is 1 when header rows repeat on each page, and absent when they don't. Pages turns it on for new tables. Numbers tables have it set too (see the pivot source in [0227](0227-pivot-table.md)), though Numbers doesn't lay tables out over pages in the same way. A reader that splits a table over pages should repeat its header rows when field 29 is 1.

## Confidence

*Likely*: table model field 29 is 1 when header rows repeat on each page.
