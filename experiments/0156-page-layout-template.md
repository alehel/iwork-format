# 0156: The page layout template

**Status:** run

Pages makes word-processing and page-layout documents. This experiment makes a document from the blank page layout template, to see what tells them apart.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0020/plain.pages` (the body text `one`) |

## Recipe

```bash
mkdir -p samples/0156
osascript recipes/0149-pages-text.applescript layout "$PWD/samples/0156/layout.pages"
```

## Observation

The document root has the usual fields, and its field 4 still names a type-2001 text record, but that record has no text (no field 3). Field 15.9 is `Application/21_Blank_Layout/ISO`.

The root also has a field 48, absent from word-processing documents, which names a record of type 10017. That record has the name `Tom` (the app's word for Blank) in field 1, and field 7 names an empty record of type 3047. Pages reports `document body` as false for the document.

## Conclusion

A page-layout document still has a body text record, but it's empty, and the document has no body to flow text into. What marks the document as page layout is probably root field 48, which names a page template (type 10017). A reader should take a page-layout document's content from the objects on its pages.

## Confidence

*Likely*: root field 48 is present only in page-layout documents and names a page template (type 10017).

*Unknown*: whether any other flag marks the document type.
