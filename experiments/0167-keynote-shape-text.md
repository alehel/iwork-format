# 0167: A shape with text on a slide

**Status:** run

This experiment places a default shape with text on a slide, to compare it with Pages' shape ([0050](0050-shape.md)).

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0050](0050-shape.md) |

## Recipe

```bash
mkdir -p samples/0167
osascript recipes/0159-keynote-slides.applescript shapetext "$PWD/samples/0167/shapetext.key"
```

## Observation

The slide gained the same records as for the line in [0166](0166-keynote-line.md). The shape is type 2011 with style `shape-0-shapestyle`, size 100 × 100 at (910, 490), the centre of the 1920 × 1080 slide. Fields 2 and 4 name its text, `shape`. Field 6 is 0; it was 1 for Pages' text box in [0049](0049-text-box.md).

## Conclusion

Shapes are the same type with the same style identifier in Keynote and Pages. A new shape is centred on the slide. Field 6 differs between the apps; its meaning is unknown.

## Confidence

*Confirmed*: shapes with text are type 2011, with fields 2 and 4 naming the text ([0049](0049-text-box.md), [0050](0050-shape.md) and this experiment).

*Unknown*: field 6.
