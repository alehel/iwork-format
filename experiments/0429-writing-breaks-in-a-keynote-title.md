# 0429: Writing breaks in a Keynote title

**Status:** run

Line feeds in Keynote titles and presenter notes are paragraph breaks ([0163](0163-multi-paragraph-notes.md), [0164](0164-two-line-title.md)). In Pages, a paragraph can end in a line feed or a carriage return, and U+2028 is a line break within a paragraph ([0005](0005-paragraphs.md), [0360](0360-writing-line-and-column-breaks.md)). This experiment writes each into a slide's title.

## Setup

| | |
| --- | --- |
| Keynote | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/theme/0025/hello.key`: one slide titled `hello`, in text record 2655470, whose run table 5 has one entry, at 0, naming paragraph style 2651125 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) for the text and [`recipes/0351-add-run.py`](../recipes/0351-add-run.py) for the paragraph runs; exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and measured with [`recipes/0319-measure-pdf.swift`](../recipes/0319-measure-pdf.swift) |

## Recipe

```bash
mkdir -p samples/0429
R=recipes/0302-set-path.py
A=recipes/0351-add-run.py
F=samples/theme/0025/hello.key
O=samples/0429
cp $F $O/original.key
python3 -I $R $F $O/x.key 2655470 3 string "$(printf 'hello\nworld')"
python3 -I $A $O/x.key $O/lf.key 2655470 5 0 2651125 6 2651125
python3 -I $R $F $O/x.key 2655470 3 string "$(printf 'hello\rworld')"
python3 -I $A $O/x.key $O/cr.key 2655470 5 0 2651125 6 2651125
python3 -I $R $F $O/x.key 2655470 3 string "$(printf 'hello\xe2\x80\xa8world')"
python3 -I $A $O/x.key $O/line-sep.key 2655470 5 0 2651125
rm $O/x.key
for f in original lf cr line-sep; do
  sh recipes/0372-in-app.sh Keynote $O/$f.key "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF
set t to object text of default title item of slide 1 of d
return {count of paragraphs of t, count of words of t}"
  swift recipes/0319-measure-pdf.swift $O/$f.pdf
done
```

Each new paragraph is given its own entry in run table 5, since a table with fewer entries than paragraphs isn't used ([0427](0427-writing-paragraph-runs-without-a-style.md)).

## Observation

| File | Between the words | Paragraphs | Words | Lines drawn |
| --- | --- | --- | --- | --- |
| `original.key` | | 1 | 1 | 1 |
| `lf.key` | U+000A | 2 | 2 | 2 |
| `cr.key` | U+000D | 2 | 2 | 2 |
| `line-sep.key` | U+2028 | 1 | 2 | 2 |

## Conclusion

Keynote's text breaks work as in Pages: a line feed or a carriage return ends a paragraph, and U+2028 starts a new line within the same paragraph. A reader can split Keynote text into paragraphs and lines by the same rules as Pages text.

## Confidence

*Confirmed*: line feeds and carriage returns as paragraph breaks and U+2028 as a line break in Keynote text, by writing them.
