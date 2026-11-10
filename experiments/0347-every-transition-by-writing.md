# 0347: Every transition, by writing its identifier

**Status:** run

[0196](0196-every-transition.md) set each of AppleScript's transition effects and read the identifier stored in the slide's field 4.2.8.2. This experiment goes the other way: it writes each identifier into a file and reads the effect AppleScript reports.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0302/original.key`: one slide (record 2655467) with a transition |
| Identifiers | The 38 from [0196](0196-every-transition.md) and `none`, in [`recipes/0347-transition-ids.txt`](../recipes/0347-transition-ids.txt) |
| Script | [`recipes/0347-transition-sweep.sh`](../recipes/0347-transition-sweep.sh), using [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0347
zsh recipes/0347-transition-sweep.sh recipes/0347-transition-ids.txt "$PWD/samples/0347/effects.tsv"
```

For each identifier, the script writes it into field 4.2.8.2, opens the file in Keynote through Launch Services and reads the slide's `transition effect`. The results are in [`recipes/0347-transition-effects.tsv`](../recipes/0347-transition-effects.tsv).

## Observation

All 39 identifiers gave an effect. For the 38 in 0196's table, the effect AppleScript reports is the one 0196 set to get that identifier, with no exception; `none` reads as `no transition effect`. Some identifiers differ from AppleScript's names, for example `apple:revolve` is `flip`, `apple:bounce` is `drop`, `apple:FlipThrough` is `switch`, `apple:ca-isometric` is `perspective` and `com.apple.iWork.Keynote.BLTMosaicFlip` is `mosaic`.

## Conclusion

The mapping between stored transition identifiers and Keynote's effects holds in both directions, so the table in 0196 and `recipes/0347-transition-effects.tsv` can be used to read and to write transitions.

## Confidence

*Confirmed*: the identifiers of 38 transition effects and `none`, by writing them.
