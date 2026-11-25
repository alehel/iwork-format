# 0424: Writing the list of objects on the page

**Status:** run

An object is either in the text, with a U+FFFC and an attachment, or on the page, listed by a type-10015 record and without a parent in its drawable's field 1.2 ([0020](0020-a-table.md), [0052](0052-floating-table.md)). This experiment changes that list.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0213/plain-shape.pages`: the body `One` and a black square, 1732647, at (300, 300). Record 1732364 (type 10015) lists two entries in field 1: the body's text, 1732539, then the shape |
| Writer | [`recipes/0416-reorder.py`](../recipes/0416-reorder.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and measured with [`recipes/0319-measure-pdf.swift`](../recipes/0319-measure-pdf.swift) |

## Recipe

```bash
mkdir -p samples/0424
X=recipes/0416-reorder.py
F=samples/0213/plain-shape.pages
O=samples/0424
cp $F $O/original.pages
python3 -I $X $F $O/shape-dropped.pages 1732364 1 1
python3 -I $X $F $O/shape-first.pages 1732364 1 2,1
python3 -I $X $F $O/body-dropped.pages 1732364 1 2
for f in original shape-dropped shape-first body-dropped; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF
return {count of shapes of d, body text of d}"
  swift recipes/0319-measure-pdf.swift $O/$f.pdf
done
```

## Observation

| File | Field 1 written | `shapes`, body | Drawn |
| --- | --- | --- | --- |
| `original.pages` | body, shape | 1, One | `One`, and the square at 300–400 |
| `shape-dropped.pages` | body | 1, One | `One` only |
| `shape-first.pages` | shape, body | 1, One | `One`, and the square at 300–400 |
| `body-dropped.pages` | shape | | Pages quit while opening it |

(The last row: AppleScript reported that the connection to Pages was no longer valid; Pages had quit.)

## Conclusion

The type-10015 list decides what is drawn on the page: a shape left out of it isn't drawn, though it is still in the file and AppleScript still counts it. The body's text must be in the list too; without it Pages fails to open the document. Putting the shape before the body changed nothing visible here, where they don't overlap; the order is probably the stacking order. A reader should draw the page's objects from this list, and a writer adding an object to the page must list it.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `original.pages` | `0213/plain-shape.pages` | `same bytes`, `10015#1732364 1.1 = 1732539`, `10015#1732364 1.1 = 1732647` | *Control*: the word and the square are drawn |
| `shape-dropped.pages` | `original.pages` | Only `10015#1732364 1: ×2 → ×1`, `10015#1732364 1.1 ≠ 1732647` | *Confirmed*: a shape left out of the list isn't drawn |
| `shape-first.pages` | `original.pages` | Only `10015#1732364 1: changed`, the two entries the other way round | *Likely*: the order is the stacking order; nothing drawn changes here |
| `body-dropped.pages` | `original.pages` | Only `10015#1732364 1: ×2 → ×1`, `10015#1732364 1.1 ≠ 1732539` | *Confirmed*: the list must hold the body; Pages quits while opening the file |

## Confidence

*Confirmed*: type 10015's field 1 as the list of what is drawn on the page, which must include the body, by writing it. *Likely*: its order is the stacking order.
