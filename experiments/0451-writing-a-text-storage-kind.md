# 0451: Writing what a text storage is for

**Status:** run; corrected on 2026-11-23: the body files crash Pages rather than failing to open

Field 1 of a type-2001 text record says what it is for: 0 a body, 1 a header or footer, 2 a footnote, 4 a slide's presenter notes and 7 a table of contents ([0003](0003-non-ascii-word.md), [0016](0016-header-and-footer.md), [text.md](../spec/text.md#the-body-text)). This experiment writes other kinds into the body and a header.

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
| `body-kind-1.pages` | body's kind 1 | Pages quits while opening it |
| `body-kind-2.pages` | body's kind 2 | Pages quits while opening it |
| `body-kind-7.pages` | body's kind 7 | Pages quits while opening it |
| `header-kind-0.pages` | header's kind 0 | Pages quits while opening it |

The recipe's helper reported only that these documents didn't open; macOS's crash reports, five between 01:28 and 01:30, one for each of these four opens and a second try of `body-kind-1.pages`, show that Pages quit each time. (Only the reports' names and times were read.) After the second try, the relaunched Pages opened no other document and declined to quit when asked through AppleScript.

## Conclusion

Pages relies on field 1: a body storage must say 0, and a header's storage mustn't. Given another kind, a body makes Pages quit while opening the document, and so does a header storage claiming to be a body. So the kind isn't only a label for readers: a writer must give each text storage the kind of the place it is used.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `header-text.pages` | `0002/hello.pages` | Only `2001#1732234 3: absent → "Header text"` | *Control*: Pages opens it |
| `body-kind-1.pages` | `0002/hello.pages` | Only `2001#1732539 1: 0 → 1` | *Confirmed*: a body must have kind 0; Pages quits while opening the file |
| `body-kind-2.pages` | `0002/hello.pages` | Only `2001#1732539 1: 0 → 2` | *Confirmed*: a body must have kind 0; Pages quits while opening the file |
| `body-kind-7.pages` | `0002/hello.pages` | Only `2001#1732539 1: 0 → 7` | *Confirmed*: a body must have kind 0; Pages quits while opening the file |
| `header-kind-0.pages` | `header-text.pages` | Only `2001#1732234 1: 1 → 0` | *Confirmed*: a header mustn't have kind 0; Pages quits while opening the file |

## Confidence

*Confirmed*: Pages needs a text storage's field 1 to match where it is used, by writing other kinds into a body and a header.
