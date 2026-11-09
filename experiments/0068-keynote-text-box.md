# 0068: A text box in Keynote

**Status:** run

[0049](0049-text-box.md) found that a Pages text box is a type-2011 shape. This experiment adds a text box to a Keynote slide, to see whether Keynote uses the same type.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0025](0025-keynote-title.md), `empty.key` |

## Recipe

```bash
mkdir -p samples/0068
osascript recipes/0068-keynote-variants.applescript "$PWD/samples/0068/textbox.key" textbox
```

The recipe makes a `text item` on slide 1 with the `object text` `box`.

## Observation

The slide's part gained a record of type 2011, a type-2001 text record holding `box`, and two type-3097 records, the same set as in Pages. The type-2011 record's geometry has field 1.2 naming the slide (2652175).

## Conclusion

Keynote's text boxes are the same type-2011 shapes as Pages', with their text in a type-2001 record. Their geometry's field 1.2 names the slide they are on, where an object on a Pages page has no field 1.2 ([0052](0052-floating-table.md)). The title box from [0025](0025-keynote-title.md) is type 7, so Keynote has two kinds of shape: placeholders from the layout (type 7) and shapes added by the user (type 2011).

## Confidence

*Likely*: type 2011 is shared between Pages and Keynote. A Keynote drawable's field 1.2 names its slide.
