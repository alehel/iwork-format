# 0229: A title on an image

**Status:** run

[0228](0228-caption.md) found that drawable field 1.11 names a caption, of type 633, in place of a type-3097 placeholder. Objects can also have a title. This experiment turns one on for the same image.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0228](0228-caption.md), `caption.pages` |

## Recipe

Continuing from 0228, with the image still selected, tick Title (*Tittel*) in the Format sidebar, then save as `samples/0229/title-and-caption.pages`.

## Observation

Drawable field 1.10 now names a second type-633 record, 1732732. It is laid out like the caption: a text shape whose parent is the image, 200 points wide, with an empty text record. It differs in:

| Field | Caption | Title |
| --- | --- | --- |
| 3 | 1 | 2 |
| 2, a type-634 record | `{ 1: 1, 2: 7 }` | another type-634 record |

Field 1.11 still names the caption.

## Conclusion

Drawable field 1.10 names the title and 1.11 the caption. Both are type-633 text shapes when shown and type-3097 placeholders when not, with field 3 saying which (2 a title, 1 a caption). A reader that shows titles and captions can find them through these two fields and draw them relative to their object. The position (above or below) is probably set in the type-634 record.

## Confidence

*Confirmed*, with 0228: titles and captions are type-633 records named by drawable fields 1.10 and 1.11, with type-3097 placeholders when hidden.

*Unknown*: the type-634 records.
