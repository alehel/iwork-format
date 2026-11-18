# 0451: Writing what a text storage is for

**Status:** run

Field 1 of a type-2001 text record says what it is for: 0 a body, 1 a header or footer, 2 a footnote, 4 a slide's presenter notes and 7 a table of contents ([0003](0003-non-ascii-word.md), [0016](0016-header-and-footer.md), [text.md](../spec/text.md#where-the-text-is)). This experiment writes other kinds into the body and a header.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0002/hello.pages`: the body `hello`, text record 1732539 with field 1 = 0, and the first header box, 1732234, with field 1 = 1 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); opened and exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) |

## Recipe

```bash
mkdir -p samples/0451
R=recipes/0302-set-path.py
F=samples/0002/hello.pages
O=samples/0451
for k in 1 2 7; do python3 -I $R $F $O/body-kind-$k.pages 1732539 1 varint $k; done
python3 -I $R $F $O/header-text.pages 1732234 3 string "Header text"
python3 -I $R $O/header-text.pages $O/header-kind-0.pages 1732234 1 varint 0
for f in header-text body-kind-1 body-kind-2 body-kind-7 header-kind-0; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF
return body text of d"
done
```

## Observation

| File | Written | Pages |
| --- | --- | --- |
| `header-text.pages` | header text, kinds as made | opens: header `Header text`, body `hello` |
| `body-kind-1.pages` | body's kind 1 | doesn't open, with no alert |
| `body-kind-2.pages` | body's kind 2 | doesn't open, with no alert |
| `body-kind-7.pages` | body's kind 7 | doesn't open, with no alert |
| `header-kind-0.pages` | header's kind 0 | Pages quits while opening it |

After `body-kind-1.pages` was opened a second time, Pages opened no other document, as after the files of [0434](0434-leaving-out-package-files.md), and declined to quit when asked through AppleScript.

## Conclusion

Pages relies on field 1: a body storage must say 0, and a header's storage mustn't. Given another kind, the body isn't opened at all, and a header storage claiming to be a body makes Pages quit. So the kind isn't only a label for readers: a writer must give each text storage the kind of the place it is used.

## Confidence

*Confirmed*: Pages needs a text storage's field 1 to match where it is used, by writing other kinds into a body and a header.
