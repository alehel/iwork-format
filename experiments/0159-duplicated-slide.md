# 0159: A duplicated slide

**Status:** run

This experiment duplicates a slide, to see whether the copy shares anything with the original.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0038](0038-second-slide.md), `two-slides.key` |

## Recipe

```bash
mkdir -p samples/0159
osascript recipes/0159-keynote-slides.applescript dup "$PWD/samples/0159/dup.key"
```

## Observation

The presentation (type 2) lists two slide nodes in field 3.2: 2652174, the original, and a new node 2652546. The new node names a new slide, 2652544, in `Index/Slide.iwa`. Both slides use the same layout (field 17: 2651742).

The copy has its own records throughout. Its title text is a new type-2001 record (2652563) holding `A`, and it has its own notes record.

## Conclusion

A duplicated slide is a full copy with new IDs: a new slide node, a new slide and new text records. It shares only what any two slides share, such as the layout and the stylesheet. A reader can treat it like any other slide.

## Confidence

*Likely*: a duplicate is a full copy with new IDs, sharing only its layout and styles.
