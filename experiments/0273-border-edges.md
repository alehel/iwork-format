# 0273: Which edges a paragraph border is on

**Status:** run

[0262](0262-paragraph-border.md) found that a paragraph border on the top edge sets properties 15 and 45 to 1, alongside the stroke in property 32. This experiment moves the border to the bottom edge, then to all four, to tell the two properties apart.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0262](0262-paragraph-border.md), a border on the top edge |

## Recipe

1. With Pages in front, add a solid paragraph border to `One` as in 0262. It starts on the top edge.
2. In the Layout tab's edge buttons, turn on the bottom edge and turn off the top edge. Save as `samples/0273/bottom-border.pages`.
3. Click the box button, which puts the border on all four edges. Save as `samples/0273/all-edges.pages`.

## Observation

| Edges | Property 15 | Property 45 |
| --- | --- | --- |
| Top (0262) | 1 | 1 |
| Bottom | 2 | 2 |
| All four | 4 | 15 |

The stroke (property 32) is the same in all three.

## Conclusion

Property 45 is a bit set of edges: 1 top and 2 bottom. The value 15 for all four edges means 4 and 8 are the left and right edges, in an order not yet tested. Property 15 is a single choice rather than a bit set: 1 top, 2 bottom, 4 all edges. It is probably an older setting that Pages still writes alongside 45 for older readers. A reader should use property 45 and fall back on 15.

## Confidence

*Likely*:

- Property 45 is the border's edges as bits (1 top, 2 bottom, 15 all).
- Property 15 is an older single-valued form.

*Unknown*: which of 4 and 8 is the left edge.
