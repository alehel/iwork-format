# 0198: The blank book template

**Status:** run

Pages has book templates, meant for publishing as EPUB. This experiment makes a document from the blank portrait book, to see whether a book is a different kind of document from a word-processing one.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0179/plain.pages`, from the blank template |

## Recipe

```bash
mkdir -p samples/0198
osascript recipes/0198-pages-book.applescript "$PWD/samples/0198/book.pages"
```

The recipe makes a document from the template `Application/00B_Blank_Portrait/ISO` (*Tom bok, stående*) and sets its body text to `one`.

## Observation

`iwork-probe text` gives `one`. The document root (type 10000) has the same fields as the blank document's, with no field 48, so this is not a page-layout document ([0156](0156-page-layout-template.md)). Apart from IDs, the root differs in:

| Field | Blank (A4) | Book |
| --- | --- | --- |
| 15.9, template | `Application/Blank/ISO` | `Application/00B_Blank_Portrait/ISO` |
| 30, 31, paper | 595.28 × 841.89 | 768.24 × 1023.84 |
| 32–35, margins | 56.69 | 54 |
| 36, 37, header and footer | 35.43, 42.52 | 36, 43.2 |
| 44, paper name | `iso-a4` | empty |

The template's object IDs are much lower (the body is 69187), as with every template other than the blank one.

## Conclusion

A book is an ordinary word-processing document. What makes it a book is its template and page setup: a 3 : 4 page of 768.24 × 1023.84 points (10.67 × 14.22 inches) that matches no named paper, so the paper name in field 44 is empty. A reader needs nothing special for books. An empty field 44 means a custom paper size, given by fields 30 and 31.

## Confidence

*Likely*: book templates make ordinary documents, and an empty paper name means a custom size.
