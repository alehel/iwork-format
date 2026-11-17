# 0414: Writing a Keynote bullet

**Status:** run

Keynote's bulleted body text uses the same list styles as Pages, and the theme's default body list style, `Punkttegn` (`text-1-liststyle-Bullet`), has the bullet `•` in field 16 ([0072](0072-keynote-bullets.md)). In Pages, list markers were confirmed by writing them ([0334](0334-writing-list-markers.md)). This experiment writes Keynote's bullet and reads the exported slide's text.

## Setup

| | |
| --- | --- |
| Keynote | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/theme/0072/bullets.key`: a body of three bulleted lines, `one`, `two` and `three`, in list style 2651121, whose field 16 is repeated nine times, `•` each time, one per level |
| Writer | [`recipes/0334-set-repeated.py`](../recipes/0334-set-repeated.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0374-pdf-text.swift`](../recipes/0374-pdf-text.swift) |

## Recipe

```bash
mkdir -p samples/0414
S=recipes/0334-set-repeated.py
F=samples/theme/0072/bullets.key
O=samples/0414
cp $F $O/original.key
python3 -I $S $F $O/arrow-level0.key 2651121 16 string "→" 1
python3 -I $S $F $O/star-all.key 2651121 16 string "*"
for f in original arrow-level0 star-all; do
  sh recipes/0372-in-app.sh Keynote $O/$f.key "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF"
  swift recipes/0374-pdf-text.swift $O/$f.pdf
done
```

## Observation

| File | Field 16 written | Text of the slide |
| --- | --- | --- |
| `original.key` | | • one / • two / • three |
| `arrow-level0.key` | the first only: `→` | →one / → two / →three |
| `star-all.key` | all nine: `*` | * one / * two / * three |

(The spacing after the marker is as PDFKit extracts it.)

## Conclusion

The first field 16 of a list style is the marker of its first level, and Keynote draws whatever text is written there, as Pages does. All three lines are at the first level, so writing only the first occurrence changed every marker. A reader can take a Keynote slide's bullets from the list style exactly as in Pages.

## Confidence

*Confirmed*: list style field 16 as the bullet, per level, in Keynote, by writing it.
