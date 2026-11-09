# 0049: A text box

**Status:** run

[0025](0025-keynote-title.md) found that a Keynote shape (type 7) owns a text record in its fields 2 and 4. This experiment places a text box on a Pages page, to see how Pages stores a shape with text.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0020/plain.pages` (the body text `one`) |

## Recipe

```bash
mkdir -p samples/0049
osascript recipes/0049-pages-text-box.applescript "$PWD/samples/0049/text-box.pages"
```

The recipe makes a document with the body text `one`, then a `text item` on page 1 with the `object text` `box`.

## Observation

`Document.iwa` gained a record of type 2011 (1732647), a type-2001 text record (1732650), and two empty records of type 3097. `ViewState.iwa` gained one record each of types 2002 and 3061.

Record 1732647, type 2011:

```
1.1.1: x 165.8, y 335.6            (fixed32 floats in fields 1 and 2)
1.1.2: width 250.0, height 128.0
1.2:   { 1: 1731559 }              ← an object in the stylesheet
1.3:   a path: the 250 × 128 rectangle
2:     { 1: 1732650 }              ← the text
4:     { 1: 1732650 }
6:     1
```

The text record has `box` in field 3, no field 1, and the same run tables as a body with one paragraph. Header references lead to the box as 1 (type 10000) → 1732364 (type 10015) → 1732647 (type 2011) → 1732650 (type 2001).

## Conclusion

A Pages text box is a shape of type 2011. Its position and size are in field 1.1, in points, as for an image ([0023](0023-an-image.md)) or a table's drawable ([0020](0020-a-table.md)). Its outline is a path in 1.3 and its style in 1.2. Fields 2 and 4 name its text, as with Keynote's type-7 shapes. The text has no field 1, like Keynote's shape text.

A box placed on the page is listed by the page-level record of type 10015 next to the body, like an image.

## Confidence

*Likely*:

- A Pages text box is type 2011, with its text in fields 2 and 4 and its geometry in 1.1.
- The text of a shape has no field 1.

*Unknown*: why the text is named twice (fields 2 and 4), and what type 3097 is.
