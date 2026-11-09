# 0050: A shape

**Status:** run

[0049](0049-text-box.md) found that a Pages text box is a shape of type 2011. This experiment places a default shape with text, to see what tells a shape apart from a text box.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0020/plain.pages`; experiment [0049](0049-text-box.md) |

## Recipe

```bash
mkdir -p samples/0050
osascript recipes/0050-pages-shape.applescript "$PWD/samples/0050/shape.pages"
```

The recipe makes a document with the body text `one`, then a `shape` on page 1 with the `object text` `shape`.

## Observation

The same records were added as for the text box in 0049: one of type 2011, a text record, and two of type 3097. The type-2011 record differs from the text box's in:

| | Text box (0049) | Shape |
| --- | --- | --- |
| 1.1.2, size | 250 × 128 | 100 × 100 |
| 1.2, style | 1731559, type 2025, `textbox-0-shapestyle` | 1731553, type 2025, `shape-0-shapestyle` |
| Text's paragraph style (field 5) | 1731511 (Body) | 1731523 |

## Conclusion

A shape and a text box are the same kind of object, type 2011. They differ in their shape style (type 2025): `shape-0-shapestyle` against `textbox-0-shapestyle`. Their default sizes differ too, as does the paragraph style their text starts with. A reader draws both from their path (1.3) and style, so it doesn't need to tell them apart.

## Confidence

*Likely*: shapes and text boxes are both type 2011, told apart only by style and content. Shape styles are type 2025.

*Unknown*: the shape style's fields, such as fill and stroke. Follow-up: give a shape a fill colour (experiment 0077).
