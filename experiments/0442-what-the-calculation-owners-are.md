# 0442: What the calculation engine's owners are

**Status:** run

The calculation engine lists type-4008 owners, each with a UUID in field 1 and a number in field 2; what each owner stands for was *unknown* ([0293](0293-calculation-owners.md)). This experiment looks for every owner's UUID in the rest of each document.

## Setup

| | |
| --- | --- |
| Apps | Pages, Keynote and Numbers 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | Every sample document on this machine that has owners: 1,139 documents with 6,674 owners. For a close look, `samples/0106/mixed.numbers`, one table with a formula |
| Method | Each owner's field 1, a message of two varints, was searched for, byte for byte, as a field of any other record, at any depth, using the writer of [0287](0287-rewriting-a-document.md) to decode records |

## Recipe

For every document: collect the field 1 of every type-4008 record; walk every other record's payload, field by field, and note the record type and field path wherever a message equals one of those UUIDs. Count the paths over all documents.

## Observation

4,462 of the 6,674 owners are named somewhere else. The places, with the number of documents:

| Record | Field | Documents |
| --- | --- | --- |
| 6366 | 1 | 1,139 (every document) |
| 6366 | 2 | 552 |
| 6366 | 3.1 | 389 |
| 6365 | 3.3.1.1 | 422 |
| 6000, a table's drawable | 7 and 8 | 389 |
| 6001, a table's model | 70.1, 70.2.1, 70.2.2.1, 70.2.3.1, 84.1, 93.1 | 397 |
| 6001 | 81.2.1 | 389 |
| 6316 | 4 | 389 |
| 6373 | 1 | 397 |
| 4000, the engine | 7.1.1, 13.1.1, 17 | 45, 6, 13 |
| 6005, formulas | 3.5.1.1.39.1.1 | 24, all in pivot tables |
| 6010, highlighting rules; 6220, filter rules | 3.1.1.4.4.3; 7.1.4.4.3 | 16; 13 |

In `mixed.numbers` the one table names these owners:

| Owner number | Named by |
| --- | --- |
| 9 | drawable field 8; model fields 70.1, 70.2.1 and 70.2.3.1, the filter's hidden rows ([0258](0258-filter.md)) |
| 10 | model field 70.2.2.1, beside the filter's rules |
| 15 | model field 84.1 |
| 16 | model field 93.1 |
| 17 | drawable field 7; model field 81.2.1, the categories ([0226](0226-category.md)); type 6373, field 1 |
| 18 | type 6316, field 4 |

Owners 1, 20 and 8 are named by the type-6366 record, and owners 11 to 14 nowhere outside the engine.

## Conclusion

Owners are the parts of a document that the calculation engine tracks, and most belong to tables: each table registers one owner for itself, named by its drawable's field 8 and by its filter's row list, one for its filter's rules, one for its categories, named by its drawable's field 7, and others named by its model's fields 84 and 93 and by a type-6316 record. A document-wide type-6366 record names one owner in every document, probably the document itself. Pivot formulas, highlighting rules and filter rules name owners too, where they refer to a table's parts. So owners are bookkeeping for recalculation: a reader can still skip them, and a writer that adds a table would have to register its owners.

## Confidence

*Confirmed*: where owners' UUIDs are named, across 1,139 documents. *Likely*: owners stand for a table, its filter, its categories and other table parts. What model fields 84 and 93, and records 6316, 6365, 6366 and 6373, are is *unknown*.
