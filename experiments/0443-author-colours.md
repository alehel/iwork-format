# 0443: The colours tracked changes are drawn in

**Status:** run

An author's colour (type-212 field 2) steers the colour Pages draws their tracked changes in, but Pages draws one of its own colours, not the one stored ([0377](0377-writing-a-tracked-change.md)). This experiment writes more colours, including the ones Pages drew, to find the set it draws from.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0377/deleted.pages`: `One two` with ` two` a tracked deletion by author 1732734 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with comments through [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0384-pdf-colours.swift`](../recipes/0384-pdf-colours.swift) |

## Recipe

```bash
mkdir -p samples/0443
O=samples/0443
for c in "1 1 0" "0 1 1" "1 0 1" "0.5 0.5 0.5" "1 0.5 0" "0.5 0 1" "0 0 0" "1 1 1" "0.98 0.6 0.21" "0.36 0.78 0.69"; do
  set -- $c; n="c-$1-$2-$3"
  python3 -I recipes/0302-set-path.py samples/0377/deleted.pages $O/$n.pages 1732734 2.3 float $1 2.4 float $2 2.5 float $3
  sh recipes/0372-in-app.sh Pages $O/$n.pages \
    "export d to POSIX file \"$PWD/$O/$n.pdf\" as PDF with properties {include comments:true}"
  swift recipes/0384-pdf-colours.swift $O/$n.pdf 232,177.5
done
```

The point (232, 177.5) is on the strike line through the deleted word, as in 0377.

## Observation

| Author colour written | Drawn |
| --- | --- |
| 1, 1, 0 (yellow) | 0.77, 0.64, 0.23 |
| 0, 1, 1 (cyan) | 0.36, 0.78, 0.69 |
| 1, 0, 1 (magenta) | 0.93, 0.53, 0.87 |
| 0.5, 0.5, 0.5 (grey) | 0.36, 0.78, 0.69 |
| 1, 0.5, 0 (orange) | 0.98, 0.60, 0.21 |
| 0.5, 0, 1 (violet) | 0.68, 0.52, 0.93 |
| 0, 0, 0 (black) | 0.98, 0.60, 0.21 |
| 1, 1, 1 (white) | 0.42, 0.52, 0.73 |
| 0.98, 0.60, 0.21 (a drawn colour) | 0.98, 0.60, 0.21 |
| 0.36, 0.78, 0.69 (a drawn colour) | 0.36, 0.78, 0.69 |

With 0377's red, green, blue and the original author colour (red → 0.98, 0.60, 0.21; green → 0.43, 0.76, 0.27; blue → 0.36, 0.78, 0.69; 0.98, 0.94, 0.35 → 0.77, 0.64, 0.23), fourteen colours gave only seven:

| Drawn colour | Looks |
| --- | --- |
| 0.98, 0.60, 0.21 | orange |
| 0.77, 0.64, 0.23 | ochre |
| 0.43, 0.76, 0.27 | green |
| 0.36, 0.78, 0.69 | teal |
| 0.42, 0.52, 0.73 | slate blue |
| 0.68, 0.52, 0.93 | violet |
| 0.93, 0.53, 0.87 | pink |

## Conclusion

Pages draws tracked changes in one of a set of seven colours. A stored colour that is one of the seven is drawn as itself, and any other is drawn as one of the seven. The choice doesn't follow hue or nearness: black became orange and grey teal, though both have no hue, and blue became teal. So a writer should give authors one of the seven colours above, and a reader that wants to match Pages should draw a stored colour as itself when it is one of them. How Pages chooses for other colours is *unknown*.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `c-1-1-0.pages` | `0377/deleted.pages` | Only `212#1732734 2.3: 0.9804 → 1.0000`, `212#1732734 2.4: 0.9373 → 1.0000`, `212#1732734 2.5: 0.3529 → 0.0000` | *Confirmed*: drawn in one of the seven colours, ochre |
| `c-0-1-1.pages` | `0377/deleted.pages` | Only `212#1732734 2.3: 0.9804 → 0.0000`, `212#1732734 2.4: 0.9373 → 1.0000`, `212#1732734 2.5: 0.3529 → 1.0000` | *Confirmed*: drawn in one of the seven colours, teal |
| `c-1-0-1.pages` | `0377/deleted.pages` | Only `212#1732734 2.3: 0.9804 → 1.0000`, `212#1732734 2.4: 0.9373 → 0.0000`, `212#1732734 2.5: 0.3529 → 1.0000` | *Confirmed*: drawn in one of the seven colours, pink |
| `c-0.5-0.5-0.5.pages` | `0377/deleted.pages` | Only `212#1732734 2.3: 0.9804 → 0.5000`, `212#1732734 2.4: 0.9373 → 0.5000`, `212#1732734 2.5: 0.3529 → 0.5000` | *Confirmed*: drawn in one of the seven colours, teal |
| `c-1-0.5-0.pages` | `0377/deleted.pages` | Only `212#1732734 2.3: 0.9804 → 1.0000`, `212#1732734 2.4: 0.9373 → 0.5000`, `212#1732734 2.5: 0.3529 → 0.0000` | *Confirmed*: drawn in one of the seven colours, orange |
| `c-0.5-0-1.pages` | `0377/deleted.pages` | Only `212#1732734 2.3: 0.9804 → 0.5000`, `212#1732734 2.4: 0.9373 → 0.0000`, `212#1732734 2.5: 0.3529 → 1.0000` | *Confirmed*: drawn in one of the seven colours, violet |
| `c-0-0-0.pages` | `0377/deleted.pages` | Only `212#1732734 2.3: 0.9804 → 0.0000`, `212#1732734 2.4: 0.9373 → 0.0000`, `212#1732734 2.5: 0.3529 → 0.0000` | *Confirmed*: drawn in one of the seven colours, orange |
| `c-1-1-1.pages` | `0377/deleted.pages` | Only `212#1732734 2.3: 0.9804 → 1.0000`, `212#1732734 2.4: 0.9373 → 1.0000`, `212#1732734 2.5: 0.3529 → 1.0000` | *Confirmed*: drawn in one of the seven colours, slate blue |
| `c-0.98-0.6-0.21.pages` | `0377/deleted.pages` | Only `212#1732734 2.3: 0.9804 → 0.9800`, `212#1732734 2.4: 0.9373 → 0.6000`, `212#1732734 2.5: 0.3529 → 0.2100` | *Confirmed*: one of the seven colours is drawn as written, orange |
| `c-0.36-0.78-0.69.pages` | `0377/deleted.pages` | Only `212#1732734 2.3: 0.9804 → 0.3600`, `212#1732734 2.4: 0.9373 → 0.7800`, `212#1732734 2.5: 0.3529 → 0.6900` | *Confirmed*: one of the seven colours is drawn as written, teal |

## Confidence

*Confirmed*: the seven colours Pages draws changes in, and that each of them is kept as written, by writing them. *Unknown*: how other colours are mapped.
