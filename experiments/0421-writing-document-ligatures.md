# 0421: Writing document ligatures

**Status:** run

Field 10 of the type-10012 document settings is *Use ligatures*, 1 for on, the default ([0237](0237-document-ligatures.md)). This experiment writes it into a document whose text has letter pairs that form ligatures, and reads the exported page.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0002/hello.pages`, with its body (1732539) replaced by `office efficient affluent fifty flight`; settings record 1732614 has field 10 = 1 |
| Writer | The writer of [0287](0287-rewriting-a-document.md) for the text and [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh), read with [`recipes/0374-pdf-text.swift`](../recipes/0374-pdf-text.swift) and compared with [`recipes/0399-pdf-diff.swift`](../recipes/0399-pdf-diff.swift) |

## Recipe

```bash
mkdir -p samples/0421
O=samples/0421
python3 -I recipes/0287-iwa-writer.py samples/0002/hello.pages $O/text.pages --text 1732539 "office efficient affluent fifty flight"
python3 -I recipes/0302-set-path.py $O/text.pages $O/ligatures-off.pages 1732614 10 varint 0
python3 -I recipes/0302-set-path.py $O/text.pages $O/ligatures-on.pages 1732614 10 varint 1
for f in text ligatures-off ligatures-on; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF"
  swift recipes/0374-pdf-text.swift $O/$f.pdf
done
swift recipes/0399-pdf-diff.swift $O/text.pdf $O/ligatures-off.pdf $O/ligatures-on.pdf
```

## Observation

| File | Field 10 | Text of the page | Ligature characters | Drawing |
| --- | --- | --- | --- | --- |
| `text.pages` | 1 | oﬃce eﬃcient aﬄuent fifty flight | U+FB03 twice, U+FB04 once | |
| `ligatures-on.pages` | 1, written | the same | the same | the same as `text.pdf` |
| `ligatures-off.pages` | 0, written | office efficient affluent fifty flight | none | 540 pixels differ, in the first three words |

`fifty` and `flight` aren't joined in either case: Helvetica Neue, the font here, draws no separate `fi` or `fl` ligature, only `ffi` and `ffl`.

## Conclusion

Field 10 turns ligatures on and off for the whole document: at 0, Pages draws `ffi` and `ffl` as separate letters. A reader laying text out with ligatures should do so only when the field is 1, the default. Which pairs join depends on the font.

## Confidence

*Confirmed*: type-10012 field 10 as using ligatures in the whole document, by writing it.
