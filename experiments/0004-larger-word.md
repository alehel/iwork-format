# 0004: A larger word

**Status:** run

The first style change. One word of two is set in a larger size, so the text has two runs, and a run table should show where the second starts. With an emoji in the text, the boundaries also show how the document itself counts positions.

The AppleScript dictionary has no bold, but it can set the size, font and colour of a range of text. Size was used because it changes one value and nothing else.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | The same text with no size change, saved by the same recipe (`plain.pages`, `emoji-plain.pages`) |

## Recipe

```bash
mkdir -p samples/0004
R=recipes/0004-larger-word.applescript
osascript $R "$PWD/samples/0004/plain.pages" "hello world" 0
osascript $R "$PWD/samples/0004/large.pages" "hello world"
osascript $R "$PWD/samples/0004/emoji-plain.pages" "hi🙂 world" 0
osascript $R "$PWD/samples/0004/emoji-large.pages" "hi🙂 world"
```

The recipe sets the body text, then sets the size of word 2 to 24 points. The body's default is 11 points. Pages splits `hi🙂 world` into three words, `hi`, `🙂` and `world`, so word 2 there is the emoji:

| Text | Word 2 | Starts at (UTF-16 / code points / bytes) | Ends at (UTF-16 / code points / bytes) |
| --- | --- | --- | --- |
| `hello world` | `world` | 6 / 6 / 6 | 11 / 11 / 11 |
| `hi🙂 world` | `🙂` | 2 / 2 / 2 | 4 / 3 / 6 |

Records were paired by position within each part and compared as `iwork-probe proto --decoded` trees, as in 0002.

## Observation

### A run table in the body's type-2001 record

The body's type-2001 record (object 1732539) gains a field 8 that the plain documents don't have. For `hello world`:

```
8: message (14 bytes)
  1: message (2 bytes)
    1: varint 0
  1: message (8 bytes)
    1: varint 6
    2: message (4 bytes)
      1: varint 1732647
```

For `hi🙂 world`:

```
8: message (18 bytes)
  1: message (2 bytes)
    1: varint 0
  1: message (8 bytes)
    1: varint 2
    2: message (4 bytes)
      1: varint 1732647
  1: message (2 bytes)
    1: varint 4
```

Each entry is a start position and, optionally, an object. In `hello world` the larger word runs to the end of the text, so there's no entry after it. In `hi🙂 world` the run ends at 4, and an entry with no object starts there. Nothing else in record 2001 changed, including the text.

### The new object

Both documents with a larger word have one record more in `DocumentStylesheet.iwa`: object 1732647, type 2021, 25 bytes:

```
1: message (14 bytes)
  3: message (4 bytes)
    1: varint 1731539
  4: varint 1
  5: message (4 bytes)
    1: varint 1732613
10: varint 1
11: message (5 bytes)
  3: fixed32 1103101952 (as float 24)
```

Object 1731539 is also of type 2021, and its payload holds the texts `Ingen` (Norwegian for "None") and `character-style-null`. Object 1732613 is the type-401 object that record 2001 names in its field 2. That object grew by 20 bytes, and `Metadata.iwa` record 2 gained entries naming 1732647.

### What the other lists point at

The objects named by the body's other lists, from 0002, hold these texts:

| Field of 2001 | Object | Type | Texts in it |
| --- | --- | --- | --- |
| 5 | 1731511 | 2022 | `Brødtekst`, `text-20-paragraphstyle-Body 1`, `HelveticaNeue` |
| 7 | 1731481 | 2023 | `Ingen`, `text-0-liststyle-None` |
| 12 | 1732607 | 2024 | (none) |

The 18 other type-2001 records name object 1731520 in field 5. It is of type 2022 and holds `Topptekst og bunntekst` (Norwegian for "Header and footer") and `text-29-paragraphstyle-Header & Footer`.

`DocumentStylesheet.iwa` holds 242 records of type 2022, 9 of type 2021 and 9 of type 2023.

## Conclusion

Field 8 of a type-2001 record is a table of character-style runs. Each entry starts a run at a position in the text, and its field 2 names the style for that run. An entry without field 2 means no character style. A run lasts until the next entry, or to the end of the text.

Setting a size made Pages create a new, unnamed character style (type 2021). It holds the size and inherits from the null character style. So type 2021 is a character style, 2022 a paragraph style and 2023 a list style, going by the identifiers and names they carry. Type 401, which holds them, is probably the stylesheet. Fields 5 and 7 of record 2001 are then likely the paragraph-style and list-style runs. They have one entry each, since the text has one paragraph.

The boundaries in `hi🙂 world` are 2 and 4, and the emoji is the only character between them. As code points that range would be 2 to 3, and as bytes 2 to 6. So positions in the text count UTF-16 code units, which agrees with what `ViewState.iwa` showed in 0003.

The 18 type-2001 records that use the header-and-footer paragraph style are probably the text of the document's headers and footers. They are empty in a new document.

## Confidence

*Confirmed*: positions in the text count UTF-16 code units (0003 and this experiment).

*Likely*: field 8 of type 2001 is the character-style run table, with entries as described. Type 2021 is a character style, and its field 11.3 is the font size as a float. Types 2022 and 2023 are paragraph and list styles, and fields 5 and 7 of type 2001 are their run tables. Follow-ups:

- Change the size of the middle of three words, then of two separate words. That should show whether the table always closes a run with an entry, and whether two runs share one style object.
- Use two paragraphs with different paragraph styles, which should add a second entry to field 5.

*Unknown*: what type 2024 is and what field 12 of type 2001 means. The same goes for fields 6, 14, 17, 24 and 28, and the other fields of a character style.
