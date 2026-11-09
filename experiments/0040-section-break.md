# 0040: A section break

**Status:** run

Since [0016](0016-header-and-footer.md), the body's field 17 has held a single run pointing at one section (type 10011). This experiment inserts a section break, to see how a second section is stored in the text and in the section runs.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0018](0018-page-break-and-left-page.md) (a page break) |

## Recipe

1. AppleScript makes a new document with the body text `one`.
2. In the Pages window, click at the end of `one`, choose Insert → Section Break (*Sett inn → Inndelingsskift*) and type `two`. The new section started on a new page.
3. Dismiss Pages' `Two` suggestion, which blocks AppleScript ([0014](0014-lists.md)), so the word stays lowercase.
4. AppleScript saves the document as `samples/0040/section-break.pages`.

## Observation

The body text:

```
3: bytes (7) 6f 6e 65 04 74 77 6f          "one", U+0004, "two"
```

The paragraph-style runs (field 5) have a second entry at 4. The section runs (field 17) have two entries:

```
17: { 1: { 1: 0, 2: { 1: 1732296 } },
      1: { 1: 4, 2: { 1: 1732696 } } }
```

Both sections are type 10011 and have the same switches (17 = 1, 18–20 = 0, 28 = 0) and template name (`Blank`). Their header-and-footer sets differ:

| | Section 1732296 | Section 1732696 |
| --- | --- | --- |
| 23 | 1732380 | 1732697 |
| 24 | 1732482 | 1732704 |
| 25 | 1732544 | 1732711 |

`iwork-probe text` first printed `onetwo`, because it didn't treat U+0004 specially. It now shows `[section break]` on its own line.

## Conclusion

A section break is the character U+0004 in the text. Like a page break (U+0005), it ends a paragraph. The section runs (field 17) gain an entry at the position after it, pointing at a new section record. A section's range in the text therefore runs from its entry to the next.

A new section gets its own three header-and-footer sets. Its *Same as previous section* switch (field 17, see [0017](0017-section-switches.md)) is on, so it presumably shows the previous section's headers until that is turned off.

## Confidence

*Likely*:

- A section break is U+0004 and starts a paragraph.
- Body field 17 has one entry per section, at its first character.
- Each section has its own header-and-footer sets.

*Unknown*: what a reader should show for a section whose *Same as previous section* is on but whose own sets have text.
