# 0231: A table caption

**Status:** run

[0228](0228-caption.md) found that an object's caption is a type-633 text shape named by drawable field 1.11. Numbers can give a table a caption too. This experiment turns one on.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0230/plain.numbers` |

## Recipe

```bash
mkdir -p samples/0231
osascript recipes/0230-numbers-blank.applescript
```

Then tick Caption (*Infotekst*) in the Table tab and save as `samples/0231/table-caption.numbers`.

## Observation

`CalculationEngine.iwa` loses one type-3097 record and gains a type-633, a type-634 and a type-2001 record. The table's drawable (type 6000) now names the type-633 record in field 1.11. Field 1.10 still names a type-3097 record.

## Conclusion

Tables get captions the same way as other objects: drawable field 1.11 names a type-633 caption in place of a type-3097 placeholder. That holds in Numbers as in Pages, so a reader can handle captions once for every kind of object.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `table-caption.numbers` | `0230/plain.numbers` | `records 633: 0 → 1`, `records 634: 0 → 1`, `records 2001: 6 → 7`, `records 3097: 2 → 1` | *Confirmed*, with 0228: a table's caption is a type-633 record, as an image's is |

## Confidence

*Confirmed*, with 0228: captions are type-633 records named by drawable field 1.11, for tables as for images.
