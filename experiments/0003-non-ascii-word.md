# 0003: A word that isn't ASCII

**Status:** run

Experiment [0002](0002-one-word.md) found the body text in one record, but only for ASCII. This experiment repeats it with letters outside ASCII and with an emoji, to confirm where the text is and to settle how it's encoded.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0002](0002-one-word.md), `hello.pages`, and experiment [0001](0001-empty-document.md), `empty-a.pages` |

## Recipe

The recipe from 0002, with a different word:

```bash
mkdir -p samples/0003
osascript recipes/0002-one-word.applescript "$PWD/samples/0003/blabaer.pages" "blåbær"
osascript recipes/0002-one-word.applescript "$PWD/samples/0003/emoji.pages" "hi🙂"
cargo run --release -- records samples/0003/emoji.pages Index/Document.iwa
```

The two words were picked so that their lengths disagree depending on how they're counted:

| Word | Characters (code points) | UTF-8 bytes | UTF-16 code units |
| --- | --- | --- | --- |
| `hello` | 5 | 5 | 5 |
| `blåbær` | 6 | 8 | 6 |
| `hi🙂` | 3 | 6 | 4 |

Records were paired by position within each part and compared as `iwork-probe proto --decoded` trees, as in 0002.

## Observation

The chunk and record layout held for every `.iwa` part, and each part had the same records in the same type order as in 0002.

### The text

The same record as in 0002, `Document.iwa` object 1732539, type 2001, carries the word in field 3:

```
3: text (8 bytes) "blåbær"     62 6c c3 a5 62 c3 a6 72
3: text (6 bytes) "hi🙂"        68 69 f0 9f 99 82
```

Both are UTF-8: `å` is `c3 a5`, `æ` is `c3 a6` and 🙂 is the four bytes `f0 9f 99 82`. As in 0002, there is no terminator, and no other field in the record changed.

`Document.iwa` holds 19 records of type 2001, not one as the 0002 write-up first said. The other 18 are 65 bytes each in every sample so far. None has a field 3, and their field 1 is 1 where the body's is 0. They also name a different object in field 5 (1731520 instead of 1731511).

### A text length in `ViewState.iwa`

Compared with the empty document, two `ViewState.iwa` records hold a number that was 0 and is now the length of the word in UTF-16 code units: 5 for `hello`, 6 for `blåbær` and 4 for `hi🙂`.

Record type 10131, for `hi🙂`:

```
5: message (99 bytes)
  1: message (95 bytes)
    1: varint 1
    2: message (66 bytes)
      3: message (4 bytes)
        1: varint 0
        2: varint 4      ← 0 in the empty document
      4: varint 4        ← 0
      5: message (4 bytes)
        1: varint 0
        2: varint 4      ← 0
…
6: varint 4              ← 0
```

Record type 10132, for `hi🙂`:

```
2: message (4 bytes)
  1: varint 4            ← 0
  2: varint 0
10: varint 4             ← 0
12: message (4 bytes)
  1: varint 4            ← 0
  2: varint 0
```

The same fields hold 5 in `hello.pages` and 6 in `blåbær.pages`. None of them holds 8 (the UTF-8 length of `blåbær`) or 3 (the number of code points in `hi🙂`).

The same records also have floats that change between the empty document and every one-word document, but are equal across the three words. They aren't explained.

## Conclusion

The body text is UTF-8 in field 3 of the body's type-2001 record. That now holds for three words in two experiments.

Positions in the text seem to be counted in UTF-16 code units, not bytes or code points. The evidence is that every number in `ViewState.iwa` that tracks the word's length matches its UTF-16 length. A reader that wants to map such a position into the UTF-8 text must convert between the two.

The pairs `{1: 0, 2: n}` and `{1: n, 2: 0}` look like ranges written as a start and a length: the whole word, and an empty range at its end, such as an insertion point. This is a guess.

The 0002 write-up said that nothing but the known save-to-save noise changed outside record 2001. That missed these `ViewState.iwa` values, and it has been corrected.

## Confidence

*Confirmed*: the body text is field 3 of the body's type-2001 record in `Document.iwa`, as UTF-8 with no terminator, and an empty body leaves the field out (0002 and this experiment).

*Likely*: positions in the text count UTF-16 code units. Only `ViewState.iwa` has shown a position so far, and the values could mean something other than positions. Follow-up: making part of a word that contains `🙂` bold should put a run boundary in a type-2001 list, and its offset will say how the document itself counts.

*Unknown*: what the other 18 type-2001 records are for, and what the ranges in `ViewState.iwa` mean.
