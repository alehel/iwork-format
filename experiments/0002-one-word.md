# 0002: One word

**Status:** run

The first change from the baseline: a document whose body text is a single word. It asks where Pages stores the body text, and how.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0001](0001-empty-document.md), `empty-a.pages` |

## Recipe

```bash
mkdir -p samples/0002
osascript recipes/0002-one-word.applescript "$PWD/samples/0002/hello.pages"
osascript recipes/0002-one-word.applescript "$PWD/samples/0002/hullo.pages" hullo
cargo run --release -- records samples/0002/hello.pages Index/Document.iwa
```

The recipe makes a new document, sets its body text through AppleScript and saves it. `hullo` differs from `hello` by one letter, so comparing the two separates the text from everything else that changes when there is text at all.

The records were paired by position within each part, since the type sequence of every part matched between files. Each pair's payload was then compared as `iwork-probe proto --decoded` trees.

## Observation

Both files hold the same 13 parts as in 0001. The chunk and record layout from 0001 held for every byte of all 14 `.iwa` parts, every chunk had type 0, and every part had the same number of records, in the same type order, as the baseline.

Sizes that changed from the empty document: `Document.iwa` (7,683 → 7,690 bytes stored, 14,148 → 14,155 decoded), `CalculationEngine-1732610.iwa`, and the three previews.

### Where the word is

One record carries the text: `Document.iwa`, object 1732539, type 2001. (`Document.iwa` holds 19 records of type 2001; this is the only one that changed. See [0003](0003-non-ascii-word.md).) In the empty document its payload is 97 bytes. With `hello` it is 104 bytes, and the only difference is one new field:

```
 1: varint 0
 2: message (4 bytes)
   1: varint 1732613
+3: text (5 bytes) "hello"
 5: message (10 bytes)
```

The empty document has no field 3 at all, not an empty one. The word is stored as its five bytes with no terminator, no length prefix beyond the field's own, and no trailing paragraph break.

Comparing `hello` with `hullo`, the same field is the only part of any record that changed, apart from the save-to-save changes listed below. Unlike in 0001, the IDs of objects made at save time came out the same in both files.

```
## Document id 1732539 type 2001 len 104->104
-3: text (5 bytes) "hello"
+3: text (5 bytes) "hullo"
```

### The rest of record 2001

The other fields are identical in the empty and one-word documents. Several share one shape: a message holding a list of entries, each a number (0 in every entry here) and a message whose field 1 is an object ID:

| Field | Entry | Object it names |
| --- | --- | --- |
| 2 | (no list) | 1732613: `DocumentStylesheet.iwa`, type 401, 19,816 bytes |
| 5 | 0 → 1731511 | `DocumentStylesheet.iwa`, type 2022 |
| 7 | 0 → 1731481 | `DocumentStylesheet.iwa`, type 2023 |
| 12 | 0 → 1732607 | `DocumentStylesheet.iwa`, type 2024 |
| 17 | 0 → 1732296 | `Document.iwa`, type 10011 |

Fields 6, 14 and 24 each hold an entry of three zeros, field 28 an entry of one zero, and field 10 is the varint 1. A single-entry list starting at 0 is what a table of runs over the text would look like when one run covers everything, but nothing here shows the runs yet.

### What else changed

*Corrected after [0003](0003-non-ascii-word.md):* two records in `ViewState.iwa` also hold the text's length (5 here, 0 in the empty document), and some floats in them change. The first version of this write-up missed both.

Everything else that differs from the baseline also differed between the two empty documents in 0001: the UUIDs, the creation time in record type 10012, the IDs of objects made at save time and the references to them, and a list in `Metadata.iwa` record 2 whose entries come in a different order. That reordering turns up between `empty-a` and `empty-b` as well, so it is noise.

`CalculationEngine-1732610.iwa` record type 4000 holds a fixed64 that reads as a double of seconds since 2001-01-01 (815,918,420 → 2026-11-09), next to the text `Europe/Oslo`. It and several 128-bit-looking values (four varints in a message) change on every save, empty or not.

## Conclusion

The body text of a Pages document is stored as UTF-8 (at least for ASCII) in field 3 of one of the type-2001 records in `Document.iwa`. An empty body leaves the field out. Nothing else in the file changes when only the text's letters change, so a reader can find the text without understanding any other record.

Record 2001 also points at the stylesheet (field 2) and at four other objects through lists that start at 0. Those look like the run tables that attach styles to ranges of the text, but this experiment can't tell, because a single word has only one run.

The chunk and record layout from 0001 held again, so it is now *confirmed* and written up in [spec/container.md](../spec/container.md).

## Confidence

*Confirmed*: the chunk and record layout (agrees with 0001).

*Likely*: body text is field 3 of the type-2001 record in `Document.iwa`, as bytes with no terminator. Two documents agree, but from one experiment. Follow-up: 0003 with a non-ASCII word, which also shows whether the text is UTF-8 and whether any offsets count bytes or characters.

*Unknown*: what types 401, 2022, 2023, 2024 and 10011 are, and what the lists in fields 5 to 28 mean. Follow-up: an experiment that makes part of the text bold, which should add a second entry to one of the lists.
