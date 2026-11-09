# 0052: A floating table

**Status:** run

In [0020](0020-a-table.md), a table inserted from the menu sat in the text as U+FFFC, attached through a type-2003 record. This experiment makes a table on the page through AppleScript instead, and compares how the two are held.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0020](0020-a-table.md), `table.pages` (a table in the text) |

## Recipe

```bash
mkdir -p samples/0052
osascript recipes/0052-pages-floating-table.applescript "$PWD/samples/0052/table.pages"
```

The recipe makes a document with the body text `one`, then a table of 3 rows and 3 columns on page 1.

## Observation

The body text is still `one`, with no U+FFFC, and `Document.iwa` has no type-2003 record. Header references reach the table's drawable straight from the page-level record:

```
1 (type 10000) → 1732364 (type 10015) → 1732671 (type 6000)
```

The two drawables (type 6000) differ in field 1:

| | In the text (0020) | On the page |
| --- | --- | --- |
| 1.1.1, position | 100.1, 70.7 | 92.8, 342.6 |
| 1.1.2, size | 481.9 × 114 | 392 × 110 |
| 1.2 | `{ 1: 1732539 }`, the body | absent |

## Conclusion

Pages has two ways of placing an object:

- **In the text:** a U+FFFC with an attachment (type 2003), as in 0020. The drawable's field 1.2 names the text it sits in.
- **On the page:** listed by the page-level record (type 10015), with no field 1.2. Images ([0023](0023-an-image.md)) and text boxes ([0049](0049-text-box.md)) placed through AppleScript were also on the page.

Field 1.2 of a drawable's geometry block is therefore its parent text, when it has one. For an object on the page, the position in 1.1.1 is relative to the page. For an object in the text, it is probably filled in by Pages' layout and can't be relied on without laying out the text.

## Confidence

*Likely*:

- Drawables on the page are listed by type 10015 and have no field 1.2.
- Drawables in the text name their text in field 1.2.

*Unknown*: whether the position of an object in the text is kept up to date.
