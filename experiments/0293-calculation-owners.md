# 0293: The calculation engine's owners

**Status:** run

[0292](0292-test-theme-reruns.md) found that Keynote tables made with the test theme have one or two more type-4009 records than the same tables in Basic White. This experiment works out what type-4009 records belong to, from the samples already made.

## Setup

| | |
| --- | --- |
| Apps | Pages, Keynote and Numbers 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | Every sample in `samples/`, and the test-theme reruns in `samples/theme/` |
| Script | [`recipes/0293-calculation-owners.py`](../recipes/0293-calculation-owners.py), using the writer of [0287](0287-rewriting-a-document.md) |

## Recipe

```bash
python3 -I recipes/0293-calculation-owners.py samples
```

The type-4009 records of the 0073 table, in both themes, were first traced back through record headers to the records that list them. The script then checked the pattern found across every document.

## Observation

Every type-4009 record in `CalculationEngine.iwa` is listed by exactly one type-4008 record. All type-4008 records are listed by the part's type-4000 record, the calculation engine's root. In the 0073 table presentation, Basic White has 13 type-4008 records and the test theme 13 as well, with different IDs.

A type-4008 record's fields, from the 0073 table:

| Field | Value | Reading |
| --- | --- | --- |
| 1 | A message of two 64-bit varints | A UUID |
| 2 | 13 | A small number, different for each record |
| 3 | 8 | |
| 4 | Entries with fields 1, 2 and 6 | |
| 7, 8 | Ranges whose bounds are 32767 and 2147483647 | The largest 16-bit and 32-bit signed numbers: probably "everything" |
| 12 | The same UUID as the root's field 17 | The calculation engine's UUID |
| 13.1 | A reference to a type-4009 record | |

The type-4009 record's field 1 is the number in its type-4008 record's field 2. That held for all 1,215 pairs in the 565 documents that have a calculation engine, with no exception.

An empty presentation has two type-4008 records. One is the same in both themes. The other comes with the theme and has a different ID and UUID in each, so it comes from the theme's own history. In Basic White's table presentations, the lists are numbered 1, 11 and 13, plus 4 when a cell holds a formula. With the test theme they're numbered 1, 3, 5, 12 and 14, in both runs of [0292](0292-test-theme-reruns.md).

## Conclusion

Type 4008 is a record the calculation engine keeps for something that can take part in formulas, here called an owner. Its field 1 is the owner's UUID and field 2 the number the engine knows it by, and each owner has one type-4009 list, numbered the same. The test theme's tables have more owners, numbered differently, because the theme brings a different set of earlier owners with it. These records don't hold cells, values or formulas, so a reader doesn't need them to read a table. What each owner stands for, and what the lists' entries record, is *unknown*.

## Confidence

*Confirmed*: a type-4009 list's field 1 equals its owner's field 2 (1,215 pairs).

*Likely*: type 4008 records are formula owners, numbered in field 2 and named by a UUID in field 1, and the difference between the themes comes from the theme, not the table.

*Unknown*: what each owner is, and what the type-4009 entries hold.
