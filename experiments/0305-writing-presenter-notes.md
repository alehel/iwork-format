# 0305: Writing presenter notes, and the kinds of text storage

**Status:** run

[0039](0039-presenter-notes.md) found a slide's presenter notes in a text storage (type 2001) of their own. This experiment replaces that text by writing and asks Keynote for the notes. It also surveys field 1 of every text storage in the samples, which marks what a text is for.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/theme/0039/notes.key`: one slide whose notes are `notes here`, in the test theme |
| Writer | The writer of [0287](0287-rewriting-a-document.md), whose `--text` option sets a text storage's field 3 |

## Recipe

```bash
mkdir -p samples/0305
cp samples/theme/0039/notes.key samples/0305/original.key
python3 -I recipes/0287-iwa-writer.py samples/0305/original.key samples/0305/written.key \
  --text 2655508 "Notes written by a script"
```

Record 2655508, in `Index/Slide.iwa`, is the text storage holding `notes here`. Keynote opened each file on its own through Launch Services ([0302](0302-writing-a-transition.md)), read `presenter notes of slide 1`, and saved the written file again. A script then counted field 1 of every type-2001 record in the samples, by app.

## Observation

Keynote reads the original's notes as `notes here` and the written file's as `Notes written by a script`. The resaved file keeps the new text in the same record.

Field 1 of the type-2001 records:

| Field 1 | Where | Count |
| --- | --- | --- |
| 0 | Pages: the body | 191 |
| 1 | Pages: headers and footers ([0003](0003-non-ascii-word.md)); Numbers: text in `Document.iwa` | 3,456; 1,236 |
| 2 | Pages: a footnote's text, in 0041 | 1 |
| 4 | Keynote: presenter notes, one per slide | 136 |
| 7 | Pages: a table of contents, in 0202 | 1 |
| Absent | Text in shapes, text boxes, placeholders and table cells | 6,664 |

## Conclusion

A slide's presenter notes are an ordinary text storage, and writing its field 3 changes them. Field 1 of a text storage says what the text is for: 0 a document body, 1 a header or footer, 2 a footnote, 4 presenter notes and 7 a table of contents, while text inside objects leaves it out. What 1 means in Numbers, where it is common, isn't clear from this survey.

## Confidence

*Confirmed*: presenter notes are written through their text storage's field 3.

*Likely*: field 1 values 0, 1, 2, 4 and 7.
