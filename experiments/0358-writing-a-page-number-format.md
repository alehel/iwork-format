# 0358: Writing a page number's format

**Status:** run

A page number field is an attachment (U+FFFC) pointing at a type-2043 record, whose field 4 is the number format, such as `decimal`, and field 1.2 chooses page number or page count ([0048](0048-page-number.md), [0201](0201-page-count.md)). Unlike a date field ([0357](0357-writing-a-date-field.md)), it has no text of its own in the body. This experiment writes other formats into field 4 and reads the exported page's text.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0048/page-number.pages`: the body `Page ` and a page number field, record 1732717 with field 4 = `decimal` |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0358
cp samples/0048/page-number.pages samples/0358/original.pages
for fmt in upper-roman lower-roman upper-alpha lower-alpha upper-latin lower-latin upper-alphabetic lower-alphabetic upper-letter; do
  python3 -I recipes/0302-set-path.py samples/0358/original.pages samples/0358/$fmt.pages 1732717 4 string $fmt
done
```

Pages opened each file on its own and exported it as PDF; PDFKit extracted the page's text.

## Observation

| Field 4 | Page text |
| --- | --- |
| `decimal` (original) | `Page 1` |
| `upper-roman` | `Page I` |
| `lower-roman` | `Page i` |
| `upper-alpha`, `lower-alpha`, `upper-latin`, `lower-latin`, `upper-alphabetic`, `lower-alphabetic`, `upper-letter` | `Page 1` |

## Conclusion

A page number is made when Pages lays out the page, in the format named by field 4: `decimal`, `upper-roman` and `lower-roman` work, and an unknown name falls back to decimal. Pages also offers letters, but their name wasn't among those tried.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `original.pages` | `0048/page-number.pages` | `same bytes`, `2043#1732717 4 = "decimal"` | *Confirmed*: this name is drawn as 1 |
| `upper-roman.pages` | `original.pages` | Only `2043#1732717 4: "decimal" → "upper-roman"` | *Confirmed*: this name is drawn as I |
| `lower-roman.pages` | `original.pages` | Only `2043#1732717 4: "decimal" → "lower-roman"` | *Confirmed*: this name is drawn as i |
| `upper-alpha.pages` | `original.pages` | Only `2043#1732717 4: "decimal" → "upper-alpha"` | *Likely*: a name Pages doesn't know is drawn as 1 |
| `lower-alpha.pages` | `original.pages` | Only `2043#1732717 4: "decimal" → "lower-alpha"` | *Likely*: as above |
| `upper-latin.pages` | `original.pages` | Only `2043#1732717 4: "decimal" → "upper-latin"` | *Likely*: as above |
| `lower-latin.pages` | `original.pages` | Only `2043#1732717 4: "decimal" → "lower-latin"` | *Likely*: as above |
| `upper-alphabetic.pages` | `original.pages` | Only `2043#1732717 4: "decimal" → "upper-alphabetic"` | *Likely*: as above |
| `lower-alphabetic.pages` | `original.pages` | Only `2043#1732717 4: "decimal" → "lower-alphabetic"` | *Likely*: as above |
| `upper-letter.pages` | `original.pages` | Only `2043#1732717 4: "decimal" → "upper-letter"` | *Likely*: as above |

## Confidence

*Confirmed*: page-number format names `decimal`, `upper-roman` and `lower-roman`, by writing them.

*Unknown*: the names of the letter formats.
