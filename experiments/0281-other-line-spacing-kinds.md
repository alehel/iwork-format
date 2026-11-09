# 0281: The other line spacing kinds

**Status:** run

[0276](0276-exact-line-spacing.md) found that line spacing kind 2 is Exactly, and guessed from the menu order that At Least is 1 and Between 3. This experiment sets both.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0276](0276-exact-line-spacing.md) |

## Recipe

As in 0276, in two new documents with the body text `One`:

- Choose At Least (*Minst*) and type 20. Save as `samples/0281/at-least.pages`.
- Choose Between (*Mellom*) and keep the value Pages proposes, 13 pt. Save as `samples/0281/between.pages`.

## Observation

| Document | Paragraph property 13 |
| --- | --- |
| `at-least.pages` | `{ 1: 1, 2: 20.0 }` |
| `between.pages` | `{ 1: 4, 2: 13.0 }` |

## Conclusion

Line spacing kinds are 0 (absent) lines, 1 at least, 2 exactly and 4 between, the space added between lines. Kind 3 isn't offered by the menu, so the codes don't follow the menu's order. For kinds 1, 2 and 4 the amount is in points.

## Confidence

*Likely*: line spacing kinds 1 at least and 4 between.
