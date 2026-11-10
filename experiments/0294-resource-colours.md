# 0294: Colours for data kept in the app

**Status:** run

[0292](0292-test-theme-reruns.md) found six type-11014 colour records in every Basic White presentation that the test theme's presentations lack, and guessed they belong to Basic White's photos, which stay inside the app. This experiment finds what lists those colours and tests the guess against every sample.

## Setup

| | |
| --- | --- |
| Apps | Pages, Keynote and Numbers 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | Every sample in `samples/`, and the test-theme reruns in `samples/theme/` |
| Script | [`recipes/0294-resource-colours.py`](../recipes/0294-resource-colours.py), using the writer of [0287](0287-rewriting-a-document.md) |

## Recipe

```bash
python3 -I recipes/0294-resource-colours.py samples
```

The colour records of an empty Basic White presentation (0024) were traced through record headers. The script then compared, in every document, the data IDs that have a colour with the data list's entries that have no stored file but a path inside the app ([container.md](../spec/container.md#data-files)).

## Observation

All type-11014 records are listed by one type-11015 record in `Metadata.iwa`. Its repeated field 1 has an entry per colour: a data ID in field 1 and a reference to a type-11014 record in field 2. A type-11014 record's field 1 is a colour: 1.1 = 1 (RGB), then red, green, blue and alpha as floats in fields 1.3 to 1.6.

In the empty Basic White presentation, the ten entries name Basic White's six photos and four more resources: two paper textures (`tile_paper_medgray.jpeg`, `tile_paper_ltgray.jpeg`), a bullet image (`bullet_circle-blk.pdf`) and `blankMoviePosterImage.png`. With the test theme, the six photos are gone and the other four remain. A blank Pages document has four entries of its own kind (`ginger/00b_theme/tile_paper_medgray` and others). The project's own red image in 0023 has none.

Across 565 documents, the data IDs with a colour and the data entries kept as app resources were the same set in every document: 2,537 of each.

The colours aren't the images' average colours. The averages of Basic White's stored reduced copies are 0.63 to 0.82 grey-beige, against listed colours from 0.45 to 0.85. Two crops of the same photo, `660384004_1290x1720` and `660384004_rotate_1964x1473`, have the same average but listed colours of 0.45 and 0.56.

## Conclusion

A document keeps a colour for each data file that stays inside the app, and only for those: type 11015 maps the data ID to a type-11014 colour. It is probably what an app shows in place of the resource when it isn't available, but it isn't the image's average colour, so how it is chosen is *unknown*. The six colours the test theme lacks are the six Basic White photos it replaced with stored cards.

## Confidence

*Confirmed*: a colour exists for exactly the data entries kept as app resources (2,537 in 565 documents).

*Likely*: the type-11015 and type-11014 layout above.

*Unknown*: what the colour is used for and how it is chosen.
