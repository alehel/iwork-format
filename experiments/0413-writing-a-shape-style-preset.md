# 0413: Writing a shape's style preset

**Status:** run

Each shape style preset in the sidebar is a named style in the stylesheet, `shape-N-shapestyle`, and choosing one only changes the shape's style reference ([0215](0215-shape-style-preset.md)). This experiment writes the reference and reads the shape's colour from the exported page.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0213/plain-shape.pages`: shape 1732647, 100 × 100 at (300, 300), whose style reference (1.2.1) is `shape-0-shapestyle` (1731553, black). The stylesheet also has `shape-1-shapestyle` (1731554, blue) and `shape-3-shapestyle` (1731556, red). Pages' own blue version: `samples/0215/blue-style.pages` |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0384-pdf-colours.swift`](../recipes/0384-pdf-colours.swift) |

## Recipe

```bash
mkdir -p samples/0413
R=recipes/0302-set-path.py
F=samples/0213/plain-shape.pages
O=samples/0413
cp $F $O/original.pages
cp samples/0215/blue-style.pages $O/pages-blue.pages
for s in 1731554 1731556; do python3 -I $R $F $O/style-$s.pages 1732647 1.2.1 varint $s; done
for f in original style-1731554 style-1731556 pages-blue; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF"
  swift recipes/0384-pdf-colours.swift $O/$f.pdf 350,350
done
```

## Observation

| File | Style reference | Colour at the shape's centre |
| --- | --- | --- |
| `original.pages` | `shape-0-shapestyle` | 0, 0, 0 |
| `style-1731554.pages` | `shape-1-shapestyle` | 0, 0.63, 1.0 |
| `style-1731556.pages` | `shape-3-shapestyle` | 0.93, 0.13, 0.05 |
| `pages-blue.pages` | (Pages' own) | 0, 0.63, 1.0 |

## Conclusion

A shape takes its look from the style its 1.2 names: pointing it at another preset's style changes its fill to that preset's, the same blue Pages draws when the preset is chosen in the sidebar. A writer can give a shape a preset by reference alone, without copying any properties.

## Confidence

*Confirmed*: a shape's style reference (1.2) choosing its preset, by writing it.
