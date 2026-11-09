# 0129: A shape on a sheet

**Status:** run

This experiment places a shape on a sheet.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0024](0024-keynote-and-numbers.md), `empty-a.numbers` |

## Recipe

```bash
mkdir -p samples/0129
osascript recipes/0113-numbers-variants.applescript "$PWD/samples/0129/shape.numbers" shape
```

## Observation

The recipe adds a shape to sheet 1. As with the text box of 0127, `Document.iwa` gained a type-2011 shape and an empty text record, and the sheet's field 2 lists it after the table.

## Conclusion

Shapes on a sheet are type 2011, as in Pages and Keynote.

## Confidence

*Likely*: type 2011 is shared by all three apps.
