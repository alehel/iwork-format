# 0150: Arabic text

**Status:** run

This experiment sets the body to a right-to-left language, to see whether the direction is stored.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0020/plain.pages` (the body text `one`) |

## Recipe

```bash
mkdir -p samples/0150
osascript recipes/0149-pages-text.applescript rtl "$PWD/samples/0150/rtl.pages"
```

## Observation

The body text is `مرحبا بالعالم`, 25 UTF-8 bytes. Apart from the text, the body record is the same as for `one`: one paragraph-style run (Body), no language runs (field 19), and nothing new. The number of records of each type is the same in every part, and `DocumentStylesheet.iwa` has the same size.

## Conclusion

Pages stores no writing direction for this text. Either it works out the direction from the characters when it lays out the text, or a paragraph must be set to right-to-left in the app before anything is stored. A reader should lay out text by the Unicode bidirectional rules.

## Confidence

*Likely*: text set through AppleScript stores no direction.

*Unknown*: how a paragraph explicitly set to right to left is stored.
