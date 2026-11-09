# 0276: Exact line spacing

**Status:** run

[0252](0252-line-spacing.md) found line spacing in paragraph property 13. Double spacing stored only field 2, the amount, and field 1 was guessed to be the kind of spacing. The Spacing section offers four kinds: Lines, At Least, Exactly and Between (*Linjer, Minst, Nøyaktig, Mellom*). This experiment sets exact spacing of 20 points.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0252](0252-line-spacing.md) |

## Recipe

1. Make a document with the body text `One`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "One"'
   ```
2. With Pages in front, click in `One`, expand Spacing in the Style tab, choose Exactly (*Nøyaktig*) from the kind pop-up, and type 20 into the value.
3. Save it as `samples/0276/exactly.pages`.

## Observation

The new paragraph style's only property is:

```
13: { 1: 2, 2: 20.0 }
```

## Conclusion

Line spacing (property 13) has a kind in field 1 and an amount in field 2. For kind 2, exactly, the amount is in points. For the default kind, lines, which isn't stored (0), the amount is a multiple of the line height, as in 0252. The menu's order suggests At Least is 1 and Between 3, but those weren't tested.

## Confidence

*Likely*: line spacing kind 2 is exact spacing in points, and 0 (absent) is a multiple of lines.

*Unknown*: the values for At Least and Between.
