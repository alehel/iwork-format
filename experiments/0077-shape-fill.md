# 0077: A shape's fill

**Status:** run

[0050](0050-shape.md) found that a shape's look comes from its shape style (type 2025), but didn't decode one. AppleScript can't set a shape's fill (`background color` was refused), so this experiment applies one of the theme's shape style presets in the Format sidebar.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0050](0050-shape.md) (a default shape, style `shape-0-shapestyle`, drawn black) |

## Recipe

1. AppleScript makes a document with the body text `one` and a 200 × 100 shape at (100, 200), which Pages leaves selected.
2. In the Style tab of the Format sidebar, click the red swatch among the *Figurstiler* (shape styles). The shape turned red.
3. AppleScript saves the document as `samples/0077/red-shape.pages`.

## Observation

The shape's style reference (field 1.2) now names 1731556, a named preset, instead of a new unnamed style. The preset and the default style compared:

| | `shape-0-shapestyle` (1731553) | `shape-3-shapestyle` (1731556) |
| --- | --- | --- |
| 1.10 | 14 | 14 |
| 1.11.1.1, a colour | 0, 0, 0, alpha 1 | 0.930, 0.134, 0.052, alpha 1 |
| 1.11.2.1, a colour | 0, 0, 0, alpha 1 | 0, 0, 0, alpha 1 |
| 1.11.2.2 | 1.0 | 1.0 |
| 1.11.2.5 | 4.0 | 4.0 |

The colours have the same layout as text colour ([0013](0013-text-colour.md)): red, green and blue in fields 3–5 and alpha in 6.

## Conclusion

A shape style keeps its properties in field 1.11. That is one level deeper than character and paragraph styles keep theirs (field 11), because the whole style sits inside field 1. Field 1.11.1 is the fill: its field 1 is the fill colour. Field 1.11.2 is probably the stroke, with a colour in 2.1 and other values in 2.2 and 2.5. The sidebar showed no stroke for these shapes (*Kantlinje* crossed out), so a field not decoded here probably turns the stroke off.

Choosing a preset points the shape at the preset's named style instead of making an unnamed copy. A reader finds a shape's fill by following its style (field 1.2) and, if needed, the style's parents.

## Confidence

*Likely*: shape style field 1.11.1.1 is the fill colour.

*Unknown*:

- The stroke fields, and what turns the stroke off.
- Whether a fill changed by hand makes an unnamed shape style.
