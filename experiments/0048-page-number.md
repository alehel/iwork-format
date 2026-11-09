# 0048: A page number field

**Status:** run

This experiment inserts Pages' page number field into the body text. It also tests a guess from [0032](0032-reading-all-text.md), where a Numbers sheet's text held a single U+FFFC anchored to a type-2043 record containing the word `decimal`.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0020](0020-a-table.md) (an object anchored in the text) |

## Recipe

1. AppleScript makes a new document with the body text `page`.
2. In the Pages window, click at the end of the text, type a space, and choose Insert → Page Number (*Sett inn → Sidetall*). Pages showed `Page 1`, capitalising the word.
3. AppleScript saves the document as `samples/0048/page-number.pages`.

## Observation

The body text is `Page `, then U+FFFC:

```
3: text (8 bytes) "Page \u{fffc}"          50 61 67 65 20 ef bf bc
```

The body's field 9 has one entry at 5, the U+FFFC:

```
9: { 1: { 1: 5, 2: { 1: 1732717 } } }
```

Object 1732717 is of type 2043, lists no references, and holds:

```
1: { 2: 0 }
2: 0
4: text "decimal"
```

That is the same content as the type-2043 record under the Numbers sheet's text in 0032.

## Conclusion

A page number field is a U+FFFC in the text, anchored through field 9 to a type-2043 record. Field 4 of that record is the number format, `decimal`. Unlike a table, the field-9 entry points at the field itself, not at a type-2003 attachment. So field-9 targets come in at least two kinds: attachments (type 2003) for objects and fields (type 2043) for computed text. A reader shows the current page number in its place.

This explains 0032: a Numbers sheet's text holds a page number field, probably for printing the sheet.

## Confidence

*Likely*:

- A page number field is U+FFFC anchored to a type-2043 record, with its number format in field 4.
- The Numbers sheet's text holds one.

*Unknown*:

- Fields 1 and 2 of type 2043.
- The other number formats. Follow-up: page numbers in roman numerals.
- How *Page Count* (*Sideantall*) is stored.
