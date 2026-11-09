# 0232: A hidden table title

**Status:** run

A Numbers table shows its name above it by default. [0229](0229-title.md) found that object titles are type-633 records named by drawable field 1.10, but a table's name is in its model ([0122](0122-table-name.md)). This experiment hides the title, to see which applies.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0230/plain.numbers` |

## Recipe

```bash
mkdir -p samples/0232
osascript recipes/0230-numbers-blank.applescript
```

Then untick Title (*Tittel*) in the Table tab and save as `samples/0232/no-title.numbers`.

## Observation

Apart from IDs, the only change is in the table model (type 6001): field 22, which was 1, is gone. No records are added or removed, and the drawable still names type-3097 records in 1.10 and 1.11.

## Conclusion

A table's title is its name (model field 8), and model field 22 says whether it's shown: 1 for shown, absent for hidden. Tables don't use the type-633 title of other objects. A reader should only draw the name when field 22 is 1.

## Confidence

*Likely*: table model field 22 is 1 when the table's name is shown.
