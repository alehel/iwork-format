# 0166: A line on a slide

**Status:** run

[0051](0051-line.md) drew a line in Pages. This experiment draws the same line on a Keynote slide.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0051](0051-line.md) |

## Recipe

```bash
mkdir -p samples/0166
osascript recipes/0159-keynote-slides.applescript line "$PWD/samples/0166/line.key"
```

## Observation

The slide gained a type-2011 record with a text record and two type-3097 records, as in Pages. Its geometry (field 1.1) is position (88.2, 150), size 223.6 × 0, rotation 333.43°, the same values as in Pages. Its style is `line-0-shapestyle`. Field 1.2 names the slide (2652175).

## Conclusion

A line is stored the same way in Keynote as in Pages, with the same geometry and the same style identifier. The only difference is field 1.2, which names the slide the line is on. Keynote coordinates are in points from the slide's top left corner.

## Confidence

*Confirmed*: a line is a type-2011 shape with zero height, rotated about its centre ([0051](0051-line.md) and this experiment).
