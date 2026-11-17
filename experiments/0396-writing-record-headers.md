# 0396: Writing a record header's type, version and references

**Status:** run

Each payload of a record has a message in header field 2. Field 2.1 differs between records whose payloads are shaped differently and is probably the payload's type; field 2.2, three packed varints such as `1 0 5`, is probably a version; both are *unknown* ([0001](0001-empty-document.md)). Field 2.5 lists the objects the payload refers to ([0022](0022-header-references.md)). This experiment changes each for the body text and asks whether Pages still opens the document and shows its text.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0002/hello.pages`: the body `hello` in text record 1732539, whose header has 2.1 = 2001, 2.2 = 1, 0, 5 and four IDs in 2.5. Of the document's 577 payloads, 562 have 2.2 = 1, 0, 5; the six records with two payloads have 2, 0, 0 and 2, 4, 0; two have 3, 2, 10 and one 1, 1, 0. Three headers have a field 2.6 |
| Writer | The new [`recipes/0396-record-header.py`](../recipes/0396-record-header.py); read back with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) |

## Recipe

```bash
mkdir -p samples/0396
R=recipes/0396-record-header.py
F=samples/0002/hello.pages
O=samples/0396
python3 -I $R $F $O/text-ver-106.pages 1732539 1 2 1,0,6
python3 -I $R $F $O/text-ver-900.pages 1732539 1 2 9,0,0
python3 -I $R $F $O/text-ver-000.pages 1732539 1 2 0,0,0
python3 -I $R $F $O/text-ver-none.pages 1732539 1 2 -
python3 -I $R $F $O/text-type-9999.pages 1732539 1 1 9999
python3 -I $R $F $O/text-type-2022.pages 1732539 1 1 2022
python3 -I $R $F $O/text-refs-none.pages 1732539 1 5 -
python3 -I $R $F $O/root-ver-900.pages 1 1 2 9,0,0
for f in $O/*.pages; do
  sh recipes/0372-in-app.sh Pages $f 'return {body text of d, font of word 1 of body text of d}'
done
```

Pages' alerts were read and dismissed through System Events.

## Observation

| File | Header written | Pages |
| --- | --- | --- |
| `text-ver-106.pages` | text 2.2 = 1, 0, 6 | opens: `hello`, HelveticaNeue |
| `text-ver-900.pages` | text 2.2 = 9, 0, 0 | opens: `hello`, HelveticaNeue |
| `text-ver-000.pages` | text 2.2 = 0, 0, 0 | opens: `hello`, HelveticaNeue |
| `text-ver-none.pages` | text 2.2 removed | opens: `hello`, HelveticaNeue |
| `root-ver-900.pages` | document root 2.2 = 9, 0, 0 | opens: `hello`, HelveticaNeue |
| `text-refs-none.pages` | text 2.5 removed | opens: `hello`, HelveticaNeue |
| `text-type-9999.pages` | text 2.1 = 9999 | opens with no body text |
| `text-type-2022.pages` | text 2.1 = 2022, a paragraph style's | "is damaged and can't be opened" |

## Conclusion

Field 2.1 is the payload's type: Pages decodes the payload by it. Given a type it doesn't know, it skips the record and the body is empty; given the type of a paragraph style, it reads the text's payload as a style and gives up. The type is the number this project has called each record's type all along.

Field 2.2 doesn't decide whether Pages can read a record: a higher, lower or missing value changes nothing, for the body text and for the document root. If it is a version, Pages 15.4 doesn't check it when opening.

Removing a payload's references in 2.5 changes nothing either. Pages doesn't need them to load this document; they matter to tools that follow the object tree from the headers alone.

## Confidence

*Confirmed*: header field 2.1 as the payload's type, by writing it. *Likely*: field 2.2 isn't checked when opening, and 2.5 isn't needed to load. What 2.2 and 2.6 mean is still *unknown*.
