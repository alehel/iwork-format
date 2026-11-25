# 0101: A hidden title

**Status:** run

[0025](0025-keynote-title.md) found a slide's title in a type-7 placeholder. This experiment hides the title, to see how a hidden placeholder is stored.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0025](0025-keynote-title.md), `empty.key` |

## Recipe

```bash
mkdir -p samples/0101
osascript recipes/0096-keynote-objects.applescript "$PWD/samples/0101/notitle.key" notitle "$PWD/samples/0023/red-8x4.png"
```

## Observation

The recipe sets slide 1's `title showing` to false. The slide (type 5) lost its field 7, which named the title placeholder 2652199, and a field 42. The title placeholder no longer appears among the slide's references. A type-7 record with a different ID remains, with a different position.

## Conclusion

A slide's field 7 names its title placeholder. When the title is hidden, the slide stops referring to it, so a reader that follows the slide's fields won't draw a title. That fits the layout's placeholders being optional parts of a slide.

*Corrected 2026-11-25:* field 7 is a list of what the slide shows, as is field 42. Both lose the title placeholder, 2652199, when the title is hidden, and keep their other entries. Field 5 is what names the title placeholder, and still does; the placeholder's own record is unchanged. [keynote.md](../spec/keynote.md) describes this, which [0312](0312-writing-a-hidden-body.md) confirmed by writing.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `notitle.key` | `0025/empty.key` | `5 7: ×44 → ×43`, `5 42: ×44 → ×43` | *Likely*: slide field 7 stops naming the title placeholder when the title is hidden |

## Confidence

*Superseded* by the correction above: slide field 7 names the title placeholder, and is absent when the title is hidden.

*Unknown*: slide field 42.
