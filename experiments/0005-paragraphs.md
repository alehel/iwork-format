# 0005: Paragraphs

**Status:** run

Two and three paragraphs instead of one. The experiment asks how a paragraph break is stored in the text, and how the paragraph-style runs (field 5 of the type-2001 record, from [0004](0004-larger-word.md)) mark where paragraphs start.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `one.pages`: the same letters with no break, saved by the same recipe |

## Recipe

```bash
mkdir -p samples/0005
R=recipes/0005-paragraphs.applescript
osascript $R "$PWD/samples/0005/one.pages" none onetwo
osascript $R "$PWD/samples/0005/two-cr.pages" return one two
osascript $R "$PWD/samples/0005/two-lf.pages" linefeed one two
osascript $R "$PWD/samples/0005/three-cr.pages" return one two three
```

The recipe joins its arguments with a carriage return (U+000D), a line feed (U+000A) or nothing, and sets the result as the body text. Records were paired by position within each part and compared as `iwork-probe proto --decoded` trees, as in 0002.

## Observation

### The break character

The body's type-2001 record (object 1732539) stores whichever character the recipe used, unchanged:

```
one.pages       3: text (6 bytes) "onetwo"
two-cr.pages    3: text (7 bytes) "one\rtwo"
two-lf.pages    3: text (7 bytes) "one\ntwo"
three-cr.pages  3: text (13 bytes) "one\rtwo\rthree"
```

`two-cr` and `two-lf` differ in that one byte and nothing else in any record, apart from save-to-save changes. There is no break after the last paragraph.

### Paragraph-style runs

Field 5 gains one entry per extra paragraph. For three paragraphs:

```
5: message (18 bytes)
  1: message (8 bytes)
    1: varint 0
    2: message (4 bytes)
      1: varint 1731511      ← the Body paragraph style
  1: message (2 bytes)
    1: varint 4
  1: message (2 bytes)
    1: varint 8
```

Each new entry starts at the character after a break, so the break belongs to the paragraph before it. The new entries have no field 2. Field 5 is the same in `two-cr` and `two-lf`.

No other field of record 2001 changed. In particular the list-style runs (field 7) keep their one entry at 0.

### `ViewState.iwa`

Besides the text length (6, 7, 7, 13), record type 10131 has a field 5.1.2.7 that is 1 in `one.pages`, 2 in both two-paragraph documents and 3 in `three-cr.pages`.

## Conclusion

A paragraph break is a character in the text, and Pages kept a carriage return and a line feed as given. Both start a new paragraph: each adds an entry to the paragraph-style runs, at the position after the break. The last paragraph has no break.

An entry in field 5 with no field 2 doesn't mean "no paragraph style". Every paragraph here uses the Body style, so such an entry probably means the paragraph keeps the style of the one before. That differs from the character-style runs in 0004, where an entry with no field 2 ended a run. It's also possible that the field 5 entries mark paragraphs and the styles are only listed where they change, which amounts to the same thing for a reader.

Typing a paragraph in Pages may not give the same character as AppleScript does. This experiment only shows that Pages accepts both and stores what it was given.

`ViewState.iwa` record type 10131 seems to hold a paragraph count.

## Confidence

*Likely*:

- A paragraph break is stored as a character in the text, and both U+000D and U+000A start a paragraph.
- Field 5 has one entry per paragraph, starting at the paragraph's first character.

*Unknown*:

- Whether an entry with no field 2 in field 5 repeats the previous style. Follow-up: give the second of two paragraphs a different paragraph style. This may need the Pages user interface, since the AppleScript dictionary doesn't seem to expose paragraph styles.
- Which character Pages writes when a user presses Return. Follow-up: type two paragraphs in the user interface and save.
- The meaning of `ViewState.iwa` field 5.1.2.7.
