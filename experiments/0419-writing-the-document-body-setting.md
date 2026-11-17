# 0419: Writing the document body setting

**Status:** run

Field 1 of the type-10012 document settings is the *Document body* switch: 1 for a word-processing document (the default), 0 for page layout ([0240](0240-no-document-body.md)). Pages' AppleScript has `document body`. This experiment writes the field both ways and reads the setting, the body text and the exported page.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0002/hello.pages`: the body `hello`, settings record 1732614 with field 1 = 1. `samples/0240/no-document-body.pages`: a document Pages turned into page layout, field 1 = 0 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0374-pdf-text.swift`](../recipes/0374-pdf-text.swift) |

## Recipe

```bash
mkdir -p samples/0419
R=recipes/0302-set-path.py
O=samples/0419
cp samples/0002/hello.pages $O/original.pages
cp samples/0240/no-document-body.pages $O/pages-no-body.pages
python3 -I $R $O/original.pages $O/no-body.pages 1732614 1 varint 0
python3 -I $R $O/pages-no-body.pages $O/pages-no-body-on.pages 1732614 1 varint 1
for f in original no-body pages-no-body pages-no-body-on; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF
return {document body of d, body text of d}"
  swift recipes/0374-pdf-text.swift $O/$f.pdf
done
```

## Observation

| File | Field 1 | `document body` | `body text` | Text on the exported page |
| --- | --- | --- | --- | --- |
| `original.pages` | 1 | true | hello | hello |
| `no-body.pages` | 0, written | false | missing value | hello |
| `pages-no-body.pages` | 0 (Pages') | false | missing value | none |
| `pages-no-body-on.pages` | 1, written | true | empty | none |

## Conclusion

Field 1 is what decides whether Pages treats a document as word processing or page layout: written 0, it reports no document body and no body text, and written 1 into a page-layout document, a body, empty. But it doesn't hide the body's text: the written page-layout document still draws `hello` where the body was. When Pages itself turns the body off, it also empties the body's text, so the two agree. A reader should go by field 1 for what kind of document it is, and still draw whatever text the body storage holds, which in a document Pages saved is nothing.

## Confidence

*Confirmed*: type-10012 field 1 as the document body switch, by writing it both ways. *Likely*: a body's text is drawn even with the switch off.
