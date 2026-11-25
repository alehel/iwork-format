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

*Corrected 2026-11-25:* only this template's IDs are lower. [0156](0156-page-layout-template.md)'s are near the blank document's, and those of 0158 and 0199 are higher.

## Conclusion

A book is an ordinary word-processing document. What makes it a book is its template and page setup: a 3 : 4 page of 768.24 × 1023.84 points (10.67 × 14.22 inches) that matches no named paper, so the paper name in field 44 is empty. A reader needs nothing special for books. An empty field 44 means a custom paper size, given by fields 30 and 31.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `book.pages` | `0179/plain.pages` | `10000 15.9: "Application/Blank/ISO" → "Application/00B_Blank_Portrait/ISO"`, `10000 30: 595.28 → 768.24`, `10000 31: 841.89 → 1023.84`, `10000 44: "iso-a4" → ""`, `10000 48 = absent` | *Likely*: a book is an ordinary document with a custom paper size, so without a paper name |
| `image-slides.key` | `0168/untouched.key` | `records 5: 18 → 20`, `part Data/red-8x4-9076.png: absent → present` | *Not used*: a leftover presentation with an image on two added slides |

## Confidence

*Likely*: book templates make ordinary documents, and an empty paper name means a custom size.
