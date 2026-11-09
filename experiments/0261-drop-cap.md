# 0261: A drop cap

**Status:** run

The Format sidebar can turn a paragraph's first letter into a drop cap. Every body text has had a run table 28 with a single empty entry. This experiment turns on a drop cap, to see whether that table holds it.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0236/plain.pages` |

## Recipe

1. Make a document with the body text `One`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "One"'
   ```
2. With Pages in front, click in `One` and tick Drop Cap (*Innfelt forbokstav*) in the Style tab. Pages draws a large `O` three lines high, and the sidebar shows 3 lines and 1 character.
3. Save it as `samples/0261/drop-cap.pages`.

## Observation

The text and the paragraph style are unchanged. The body's run table 28 changes from one entry with no value to:

```
28: { 1: { 1: 0, 2: { 1: 1732137 } } }
```

Record 1732137 is a type-10024 style in the stylesheet, named `dropcap-style-0`:

```
12.1: { 1: 0, 2: 3, 3: 0, 6: 0, 7: 0, 10: 1, 11: 0.0, 12: 0.0, 13: 0.2, 14: 0.8 }
```

## Conclusion

Run table 28 holds drop caps. Each entry points at a type-10024 drop-cap style, or at nothing for no drop cap. The style's field 12.1.2 is the number of lines the letter spans (3). The number of characters (1) is probably field 12.1.1, counted from 0, or field 10. The other fields are probably spacing and the letter's padding. As with other styles, the stylesheet holds named defaults (`dropcap-style-0`), and a paragraph points at one.

## Confidence

*Likely*: run table 28 holds drop caps, pointing at type-10024 styles whose field 12.1.2 is the number of lines.

*Unknown*: the field for the number of characters, and fields 13 and 14.
