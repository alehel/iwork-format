# 0041: A footnote

**Status:** run

This experiment inserts a footnote after a word, to see how a footnote's mark sits in the text and where the footnote's own text is kept.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0020/plain.pages` (the body text `one`) |

## Recipe

1. AppleScript makes a new document with the body text `one`.
2. In the Pages window, click at the end of `one`, choose Insert → Footnote (*Sett inn → Fotnote*), and type `note`. Pages put the cursor in the footnote at the foot of the page.
3. AppleScript saves the document as `samples/0041/footnote.pages`.

## Observation

The body text gained one character, U+000E, after `one`:

```
3: bytes (4) 6f 6e 65 0e
```

The body gained a field 16 with one entry at 3, the U+000E, and a field 8, the character-style runs:

```
16: { 1: { 1: 3, 2: { 1: 1732722 } } }
```

| Object | Type | Holds |
| --- | --- | --- |
| 1732722 | 2008 | `1: bytes (0)`, `2: { 1: 1732708 }` |
| 1732708 | 2001 | a text record with field 1 = 2, text U+FFFC, space, `note` |
| 1732723 | 2004 | the target of the footnote text's field-9 entry at 0, its U+FFFC |

Following header references, the path is: 1 (type 10000) → 1732539 (the body) → 1732722 (type 2008) → 1732708 (the footnote's text).

## Conclusion

A footnote's mark is the character U+000E in the text. Field 16 of the text record is a run table of footnotes. Its entry at the mark points at a type-2008 footnote record, whose field 2 names the footnote's text. That text is a type-2001 record with field 1 = 2, another value for field 1 alongside 0 (body), 1 (header or footer) and 4 (presenter notes, [0039](0039-presenter-notes.md)).

The footnote's text starts with U+FFFC, which its own field 9 anchors to a type-2004 record. That is probably the footnote number, which Pages draws at the start of the note and works out itself. So a reader should number footnotes in order rather than look for the number as text.

The body's new character-style run is most likely the superscript style of the mark. Superscript hasn't been decoded.

`iwork-probe text` now shows U+000E as `[footnote]`.

## Confidence

*Likely*:

- A footnote mark is U+000E.
- Body field 16 holds footnote runs pointing at type-2008 records, which name the footnote text (field 1 = 2).
- The footnote text starts with an anchored number (type 2004).

*Unknown*:

- Type 2004.
- The superscript style of the mark.
