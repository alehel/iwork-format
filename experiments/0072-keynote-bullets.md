# 0072: Bulleted text in Keynote

**Status:** run

This experiment fills the body of a Keynote slide that uses the *Title & Bullets* layout, to see how Keynote's bulleted text is stored and whether a tab sets a list level.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiments [0014](0014-lists.md) and [0015](0015-list-levels.md) (lists in Pages) |

## Recipe

```bash
mkdir -p samples/0072
osascript recipes/0068-keynote-variants.applescript "$PWD/samples/0072/bullets.key" bullets
```

The recipe sets slide 1's layout to *Tittel og punkttegn* (Title & Bullets) and its body text to `one`, return, tab, `two`, return, `three`.

## Observation

The body's text record:

```
3: text "one\r\ttwo\rthree"
5: { 0 → 2651133, 4, 9 }        paragraph styles: Body (`text-8-paragraphstyle-Body`), then two entries with no style
6: { 0: level 0 }               one list-level entry
7: { 0 → 2651121 }              list style: `Punkttegn`, `text-1-liststyle-Bullet`, marker "•" in field 16
```

## Conclusion

Keynote's bulleted body text uses the same text record, run tables and list styles as Pages ([0014](0014-lists.md)). Its default list style is a bullet list whose marker, `•`, is in field 16. AppleScript kept the carriage returns as paragraph breaks. It stored the tab as a tab character instead of indenting `two`, so all three paragraphs are at level 0. Levels need the Keynote window, as in [0015](0015-list-levels.md).

## Confidence

*Likely*: Keynote lists are stored as in Pages, and the default body list style is a bullet with the marker in field 16.
