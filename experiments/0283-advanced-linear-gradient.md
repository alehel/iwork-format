# 0283: An advanced linear gradient

**Status:** run

[0275](0275-radial-gradient.md) found gradient field 4 set to 1 on a radial gradient made in the advanced editor, and 0 on the simple linear gradient of [0260](0260-gradient-fill.md). That left two explanations: field 4 marks the advanced editor, or it goes with the radial kind. This experiment makes a linear gradient in the advanced editor.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiments [0260](0260-gradient-fill.md) and [0275](0275-radial-gradient.md) |

## Recipe

```bash
mkdir -p samples/0283
osascript recipes/0213-pages-shape.applescript 1
```

The new shape is left selected. With Pages in front, choose Advanced Gradient Fill from the Fill pop-up and leave it linear, at 270°. Save as `samples/0283/advanced-linear.pages`.

## Observation

| Field | Simple linear (0260) | Advanced linear | Advanced radial (0275) |
| --- | --- | --- | --- |
| 1, kind | 0 | 0 | 1 |
| 4 | 0 | 1 | 1 |
| 5.2, angle | 4.712389 | 4.712389 | 5.497787 |

The stops are the same two blue stops in all three.

## Conclusion

Gradient field 4 is 1 for a gradient made in the advanced editor and 0 for the simple one, whatever its kind. Only field 1 says whether the gradient is linear or radial. A reader can ignore field 4: it only tells Pages which editor to show.

## Confidence

*Likely*: gradient field 4 marks the advanced editor, and field 1 alone gives the kind.
