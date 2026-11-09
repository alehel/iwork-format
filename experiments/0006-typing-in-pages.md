# 0006: Typing in Pages

**Status:** run

Experiment [0005](0005-paragraphs.md) set paragraphs through AppleScript, so it couldn't say what Pages writes when someone types. This experiment types in the Pages window instead. It covers pressing Return, pressing Shift-Return, and giving the second paragraph a different paragraph style.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0005](0005-paragraphs.md), `two-lf.pages` |

## Recipe

This experiment has no AppleScript recipe, because its point is the steps AppleScript can't take. Each document was made like this:

1. Make a new document with AppleScript: `tell application "Pages" to make new document`.
2. In the Pages window, click in the body and type the keys below.
3. Save it with AppleScript, `save front document in POSIX file "…"`, then close it.

| File | Keys typed | Then |
| --- | --- | --- |
| `return-ui.pages` | `one`, Return, `two` | — |
| `line-break-ui.pages` | `one`, Shift-Return, `two` | — |
| `heading-ui.pages` | `one`, Return, `two` | With the cursor in the second paragraph, choose *Overskrift* (Heading) in the paragraph style menu of the Format sidebar |

Pages capitalised some of the words as they were typed, as its autocorrection does at the start of a sentence. The text that ended up in each file is shown below.

## Observation

### Return and Shift-Return

The body's type-2001 record (object 1732539):

```
return-ui.pages      3: text (7 bytes) "One\nTwo"
line-break-ui.pages  3: text (9 bytes) "One\u{2028}two"     4f 6e 65 e2 80 a8 74 77 6f
```

Return wrote U+000A (line feed). Shift-Return wrote U+2028 (line separator), which is three bytes in UTF-8.

With Return, the paragraph-style runs (field 5) have a second entry at 4, as in 0005. With Shift-Return, field 5 keeps its single entry at 0.

### A second paragraph style

In `heading-ui.pages`, field 5 is:

```
5: message (20 bytes)
  1: message (8 bytes)
    1: varint 0
    2: message (4 bytes)
      1: varint 1731511      ← "Brødtekst", text-20-paragraphstyle-Body 1
  1: message (8 bytes)
    1: varint 4
    2: message (4 bytes)
      1: varint 1731502      ← "Overskrift", text-11-paragraphstyle-Heading 1
```

Object 1731502 is of type 2022 in `DocumentStylesheet.iwa`. Choosing the style created no new object, and no record other than 2001 changed apart from save-to-save changes. The list-style runs (field 7) keep their single entry.

### Two run tables that typing adds

Every document typed in the window has two fields in record 2001 that no document set through AppleScript has had. From `return-ui.pages`:

```
19: message (8 bytes)
  1: message (6 bytes)
    1: varint 0
    2: text (2 bytes) "nb"
20: message (88 bytes)
  1: message (40 bytes)
    1: varint 0
    2: text (36 bytes) "40F91214-FB92-4870-9744-CA22B49B4EB1"
  1: message (2 bytes)
    1: varint 3
  1: message (40 bytes)
    1: varint 4
    2: text (36 bytes) "C8C6D8C1-B294-4C8C-ADC9-84117C3AFF2E"
```

Field 19 has one entry: position 0 and the text `nb`, the language of the user interface.

Field 20 has the same run-table shape, but its field 2 is a UUID as text instead of an object reference. Its entries line up with the words Pages capitalised:

| File | Text | Capitalised | Field 20 entries |
| --- | --- | --- | --- |
| `return-ui` | `One\nTwo` | `One`, `Two` | 0 → UUID, 3 → none, 4 → UUID |
| `line-break-ui` | `One\u{2028}two` | `One` | 0 → UUID, 3 → none |
| `heading-ui` | `One\ntwo` | `One` | 0 → UUID, 3 → none |

## Conclusion

Pressing Return writes U+000A and starts a paragraph, as a line feed did in 0005. Pressing Shift-Return writes U+2028 and doesn't: it is a line break within a paragraph.

The paragraph-style runs name a paragraph style wherever one begins, so field 5 is a run table like field 8. In 0005 every entry after the first had no field 2, and all paragraphs used the same style, so an entry without field 2 most likely keeps the previous style. Here, the paragraph with a different style named it.

Field 19 is probably a table of language runs.

Field 20 looks like a record of autocorrections. Each capitalised word is covered by a run with its own UUID, and a run with no UUID follows it. This would let Pages offer to undo a correction later. It is a hypothesis from three documents.

AppleScript and typing don't produce the same file for the same text: typing adds fields 19 and 20, and typing triggers autocorrection. Later experiments that type in the window should say so and keep that in mind when comparing with documents made through AppleScript.

## Confidence

*Likely*:

- Return writes U+000A, and Shift-Return writes U+2028 without starting a paragraph.
- Field 5 entries name a paragraph style (type 2022) where it changes.
- Field 19 holds language runs.

*Unknown*:

- That field 20 records autocorrections. Follow-up: type with autocorrection turned off in Pages' settings, and type a word that autocorrection changes in the middle of a sentence.
- Whether an entry with no field 2 in field 5 always means "same style as before". Follow-up: three paragraphs where only the middle one has a different style.
