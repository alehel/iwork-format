# 0393: Writing an unnamed style's parent

**Status:** run

Formatting a whole paragraph makes an unnamed paragraph style (type 2022) whose parent, in field 1.3, is the paragraph's style. Named styles set every property, and unnamed ones only what differs from their parent ([0008](0008-runs-and-shared-styles.md), [0010](0010-alignment.md)). This experiment points an unnamed style at other parents.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0010/center.pages`: one centred paragraph, in unnamed style 1732696, which sets only 12.1 = 2 (centred) and has the parent *Brødtekst* (Body, 1731511). The template's *Tittel* (Title) is 1731491 and *Overskrift* (Heading) 1731502 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); read back with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and measured with [`recipes/0319-measure-pdf.swift`](../recipes/0319-measure-pdf.swift) |

## Recipe

```bash
mkdir -p samples/0393
R=recipes/0302-set-path.py
F=samples/0010/center.pages
O=samples/0393
cp $F $O/original.pages
python3 -I $R $F $O/parent-title.pages 1732696 1.3.1 varint 1731491
python3 -I $R $F $O/parent-heading.pages 1732696 1.3.1 varint 1731502
for f in original parent-title parent-heading; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF
return {font of paragraph 1 of body text of d, size of paragraph 1 of body text of d}"
done
swift recipes/0319-measure-pdf.swift $O/*.pdf
```

## Observation

| File | Parent written | Font | Size | Ink, left – right | Middle |
| --- | --- | --- | --- | --- | --- |
| `original.pages` | *Brødtekst* | HelveticaNeue | 11 | 264.5 – 331.2 | 297.9 |
| `parent-title.pages` | *Tittel* | HelveticaNeue-Bold | 30 | 200.2 – 395.5 | 297.9 |
| `parent-heading.pages` | *Overskrift* | HelveticaNeue-Bold | 18 | 239.2 – 356.5 | 297.9 |

## Conclusion

An unnamed style takes every property it doesn't set from the style named in its field 1.3: with *Tittel* as its parent the paragraph is set in 30-point bold, with *Overskrift* in 18-point bold. The property the unnamed style does set, centring, stays, so the line is centred on the same middle whatever its width. This is the chain a reader follows to find a property.

## Confidence

*Confirmed*: field 1.3 as a style's parent, from which it inherits what it leaves out, by writing it.
