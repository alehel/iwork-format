# 0161: A deleted slide

**Status:** run

This experiment deletes the middle of three slides, to see whether anything of it is left behind.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0038](0038-second-slide.md), `two-slides.key` |

## Recipe

```bash
mkdir -p samples/0161
osascript recipes/0159-keynote-slides.applescript delete "$PWD/samples/0161/delete.key"
```

## Observation

Field 3.2 lists two nodes, for `A` and `C`. No record holds the text `B`, and no part is left for the deleted slide. `C`'s slide, 2652616, is in `Index/Slide.iwa`, the part name that the second slide had in [0038](0038-second-slide.md).

## Conclusion

A deleted slide leaves nothing behind. Part names can move between slides from one save to the next: `Slide.iwa` held the second slide here, which is `C` once `B` is gone.

## Confidence

*Likely*: a deleted slide's records and part are removed.
