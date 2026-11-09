# 0228: A caption

**Status:** run

Every shape and image so far came with two empty type-3097 records, named by drawable fields 1.10 and 1.11 ([0049](0049-text-box.md)). The Format sidebar can show a caption under an object. This experiment turns one on for an image, to see whether those records are where the caption goes.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0023/image.pages`, an image without a caption |

## Recipe

1. Make a document with an image on the page:
   ```bash
   osascript -e 'tell application "Pages"' \
     -e 'set d to make new document' -e 'set body text of d to "One"' \
     -e "tell page 1 of d to make new image with properties {file:POSIX file \"$PWD/samples/0023/red-8x4.png\", position:{300, 300}, width:200, height:100}" \
     -e 'end tell'
   ```
   The new image is left selected.
2. In the Format sidebar's Style tab, tick Caption (*Infotekst*). Pages shows the prompt `Infotekst` under the image.
3. Save it as `samples/0228/caption.pages`.

## Observation

In the image (type 3005), drawable field 1.11 no longer names a type-3097 record but a new record of type 633. Field 1.10 still names a type-3097 record.

The type-633 record:

```
1: a shape, with
   1.1: geometry (0, 0), 200 × 0, flags 1   ← below the image, as wide as it
   1.2: { 1: 1732647 }                      ← the image
   1.3: a path, a 200 × 0 rectangle
   2, 4: { 1: 1732703 }                     ← its text
   6: 1
2: { 1: 1732723 }                           ← type 634, { 1: 1, 2: 7 }
3: 1
```

Its text (type 2001) has no field 3: it is empty. The prompt `Infotekst` that Pages shows isn't stored in it.

## Conclusion

A caption is a type-633 record named by the object's drawable field 1.11. It is a text shape (like the type-2011 shapes of [0049](0049-text-box.md)) whose parent is the captioned object. Its field 3 is 1 for a caption. When an object has no caption, 1.11 names a type-3097 record instead: the empty records seen with every object are placeholders for a caption and a title that aren't shown. An empty caption stores no text. The prompt comes from the app.

## Confidence

*Likely*: drawable field 1.11 names the caption, a type-633 text shape with field 3 = 1, or a type-3097 placeholder when there's none.

*Unknown*: the type-634 record in field 2.
