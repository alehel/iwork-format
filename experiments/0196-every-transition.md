# 0196: Every transition effect

**Status:** run

[0091](0091-move-in-transition.md) to [0095](0095-magic-move.md) found that a slide's transition is named by an identifier in field 4.2.8.2, and mapped six effects. This experiment maps the other 38 that Keynote's AppleScript offers.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiments [0091](0091-move-in-transition.md)–[0095](0095-magic-move.md) |

## Recipe

```bash
mkdir -p samples/0196
osascript recipes/0196-keynote-all-transitions.applescript "$PWD/samples/0196/all.key"
```

The recipe makes a presentation with 38 slides. Each slide's title is the AppleScript name of an effect, and its transition is that effect.

## Observation

Each slide record (type 5) has the effect's identifier in field 4.2.8.2:

| AppleScript effect | Identifier |
| --- | --- |
| `blinds` | `com.apple.iWork.Keynote.BLTBlinds` |
| `clothesline` | `apple:ClotheslinePush` |
| `color planes` | `com.apple.iWork.Keynote.KLNColorPlanes` |
| `confetti` | `com.apple.iWork.Keynote.KLNConfetti` |
| `doorway` | `apple:doorway` |
| `drop` | `apple:bounce` |
| `droplet` | `apple:droplet` |
| `fade and move` | `apple:fade-and-move` |
| `fade through color` | `com.apple.iWork.Keynote.BLTFadeThruColor` |
| `fall` | `apple:fall` |
| `flip` | `apple:revolve` |
| `flop` | `com.apple.iWork.Keynote.BUKFlop` |
| `grid` | `apple:apple-grid` |
| `iris` | `apple:wipe-iris` |
| `mosaic` | `com.apple.iWork.Keynote.BLTMosaicFlip` |
| `object cube` | `apple:ca-cube` |
| `object flip` | `apple:ca-dissolve-and-flip` |
| `object pop` | `apple:ca-pop` |
| `object push` | `apple:ca-push` |
| `object revolve` | `apple:ca-revolve` |
| `object zoom` | `apple:ca-zoom` |
| `page flip` | `apple:pageflip` |
| `perspective` | `apple:ca-isometric` |
| `pivot` | `apple:pivot` |
| `radial wipe` | `apple:radial wipe` |
| `reflection` | `com.apple.iWork.Keynote.BLTReflection` |
| `reveal` | `apple:reveal` |
| `revolving door` | `com.apple.iWork.Keynote.BLTRevolvingDoor` |
| `scale` | `apple:scale` |
| `shimmer` | `apple:ca-text-shimmer` |
| `sparkle` | `apple:ca-text-sparkle` |
| `swap` | `com.apple.iWork.Keynote.KLNSwap` |
| `swing` | `apple:ca-swing` |
| `switch` | `apple:FlipThrough` |
| `swoosh` | `com.apple.iWork.Keynote.BLTSwoosh` |
| `twirl` | `apple:twirl` |
| `twist` | `com.apple.iWork.Keynote.BUKTwist` |
| `wipe` | `apple:wipe` |

## Conclusion

Effect identifiers come in two forms:

- `apple:` followed by a name, as in 0091–0095.
- A reverse-DNS class name under `com.apple.iWork.Keynote.`, whose prefixes (`BLT`, `KLN`, `BUK`) probably name the internal plug-in the effect comes from.

The identifiers often differ from the names Keynote shows. For example, `drop` is `apple:bounce`, `flip` is `apple:revolve` and `switch` is `apple:FlipThrough`. One identifier contains a space (`apple:radial wipe`). Effects whose AppleScript names start with `object`, plus `perspective`, `shimmer`, `sparkle` and `swing`, use a `ca-` prefix. These are probably Keynote's object-level (Magic Move style) effects.

A reader that only needs to know whether a slide has a transition can treat any identifier other than `none` as one. A reader that converts to another format needs this table.

## Confidence

*Likely*: the identifiers in the table, from one sample each.
