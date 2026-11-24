# 0472: Keynote 16.0 with the test theme

**Status:** run

The Keynote presentations of [0466](0466-keynote-14-5.md) and [0469](0469-the-16-0-apps.md) were made with Basic White, whose photos are Apple's, so none can be published with the fixtures. This experiment reruns the same 14 recipes in Keynote 16.0 with the project's test theme ([0291](0291-test-theme.md)), and compares each presentation with the test-theme one Keynote 15.4 made from the same recipe in [0292](0292-test-theme-reruns.md).

## Setup

| | |
| --- | --- |
| Keynote | 16.0 (build `M16.0-7052.0.68-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-24 |
| Theme | `iwork-format test`, made with 15.4 in [0291](0291-test-theme.md), which 16.0 still lists among its themes |
| Recipes | The 14 Keynote recipes of 0466 and 0469: 16 presentations |
| Compared with | Each recipe's test-theme presentation from 15.4, under `samples/theme/`, with [`recipes/0461-compare-structure.py`](../recipes/0461-compare-structure.py) |
| Script | The new [`recipes/0472-keynote-test-theme-rerun.sh`](../recipes/0472-keynote-test-theme-rerun.sh) |

## Recipe

```bash
bash recipes/0472-keynote-test-theme-rerun.sh samples/theme/0472
python3 -I fixtures/build.py /tmp/iwork-format-fixtures.zip
```

The presentations of 0197 and 0243 are saved into folders by their recipes and then moved up as `0197-default.key` and so on, since the fixtures builder reads only the files directly under an experiment's folder.

## Observation

Every recipe ran, 0196 with its radial wipe. In all 16 pairs: the same parts, the same number of records of every type, the same version in header field 2.2 for every type, and the same top-level fields for every type but two. The differences, besides UUIDs, the build history and the format version ([0469](0469-the-16-0-apps.md)):

| | 15.4 | 16.0 |
| --- | --- | --- |
| `ViewState.iwa`, types 3 and 23 | | type 3 field 43 and type 23 field 13, as in 0469 |
| Master thumbnails `Data/mt-UUID-N.jpg` | 16 | 16, with other UUIDs and data IDs; in 0024's pair, 4 of the 16 images are byte for byte the same as one of 15.4's, and the other 12 differ |

The build history differs from 0469's too: a presentation made from the test theme keeps the theme's own history, `Template: 21_BasicWhite (dev/15.4)` and `M15.4-7051.0.79-2`, since 15.4 saved the theme, and 16.0 adds its build after them. Its last build, `M16.0-7052.0.68-2`, is the release that saved it; [`recipes/0465-saved-by.py`](../recipes/0465-saved-by.py) reports these presentations as saved by more than one release.

So the test theme gives the same structure in 16.0 as Basic White does ([0469](0469-the-16-0-apps.md)), and the same as it gave in 15.4.

The fixtures builder keeps all 16: their `Data/` holds only the test cards and Keynote's thumbnails of them, and no part holds a personal name.

## Conclusion

Keynote 16.0 makes the same presentations with the test theme as 15.4 did, apart from the view-state fields every 16.0 document has and its own drawing of the master thumbnails. The 16 presentations are published with the fixtures under `keynote/0472/`, the first from a release other than 15.4.

## Confidence

*Confirmed*: for the 16 presentations of these recipes, Keynote 16.0 with the test theme writes the same structure as 15.4 with it.
