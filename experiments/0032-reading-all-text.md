# 0032: Reading the text of every sample

**Status:** run

A check of the text layer against everything saved so far. `iwork-probe` gained a `text` command built only on [spec/text.md](../spec/text.md): it prints field 3 of every type-2001 record, with field 1's value. If the spec is right, it should print exactly the text each earlier experiment put in its documents.

## Setup

| | |
| --- | --- |
| Apps | Pages, Keynote and Numbers 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Documents | All 61 samples from experiments 0001–0031 |

## Recipe

```bash
cargo run --release -- text samples/0016/header.pages
for f in samples/*/*.pages samples/*/*.key samples/*/*.numbers; do cargo run --release -q -- text "$f"; done
```

`text` shows breaks as new lines, a page break (U+0005) as `[page break]` and an anchored object (U+FFFC) as `[object]`.

## Observation

`text` read all 61 documents without an error.

### Pages

For every Pages sample, the text matched what its experiment recorded:

- the body text, with its paragraphs, line breaks and page breaks (`one [page break] Two` in 0018 and 0019)
- `[object]` where a table was inserted (0020, 0021)
- the header and footer texts of 0016, 0018 and 0019, each in its own record with field 1 = 1

Empty documents (0001) printed nothing.

### Numbers

Every Numbers sample has one text record, in `Document.iwa`, with field 1 = 1 and the text U+FFFC alone. In `samples/0026/cells.numbers` it is object 904667. Header references lead to it from the root through the sheet: 1 (type 1) → 904532 (type 2, the sheet) → 904667 (type 2001).

Its field 9 has one entry, at position 0, like a Pages attachment run. But it points at object 904995, which isn't a type-2003 attachment. It is type 2043 with only these fields:

```
1: { 2: 0 }
2: 0
4: text "decimal"
```

It lists no references. The table itself is reached from the sheet's field 2, not from this text ([0029](0029-numbers-root-to-table.md)).

### Keynote

Besides the slide title of 0025, each Keynote sample has text records in the slide part and in the 17 template slide parts, with no field 1. The template slides hold the theme's placeholder texts in Norwegian, such as `Presentasjonstittel` (Presentation title) and `Brødtekst nivå én` (Body level one). Some contain U+00AD (soft hyphen), as in `Present\u{ad}asjons\u{ad}tittel`.

## Conclusion

The text layer holds for every document saved so far: a reader that knows only type 2001 and field 3 gets all the text of a Pages document. That includes its headers and footers and the positions of anchored objects.

Field 1 of a text record doesn't mean the same thing in every app. In Pages, 0 is the body and 1 a header or footer. In Numbers, a sheet owns a text record with field 1 = 1 whose only character is U+FFFC. Keynote leaves field 1 out. `iwork-probe text` therefore reports field 1's value rather than naming it.

*Note after [0048](0048-page-number.md):* the type-2043 record is a page number field, with `decimal` as its number format. So the sheet's text holds a page number. What the Numbers sheet's text is for isn't clear. Its single U+FFFC has a field-9 entry like an anchored object's, but the entry points at a type-2043 record holding the word `decimal`, not at the table. So field 9 entries can point at more than one kind of record. The table is not anchored through this text.

A Keynote theme's placeholder texts are stored in the template slides. Texts can contain U+00AD, so a reader that displays text should treat it as a soft hyphen.

## Confidence

*Confirmed*: field 3 of every type-2001 record is the text, in Pages, Keynote and Numbers. This holds over 61 documents with no exception.

*Likely*: field 1 = 1 doesn't mean "header or footer" outside Pages.

*Unknown*:

- What the Numbers sheet's text and its type-2043 field-9 target (`decimal`) are for. Follow-up: add a second table or a text box to a Numbers sheet, and see whether this text gains characters.
- Whether field 9 targets other than type 2003 occur in Pages.
