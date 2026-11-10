# 0368: Writing a build's delivery

**Status:** run

A build is a type-8 record whose field 2 is the delivery as text, such as `All at Once` ([0257](0257-build.md)). The slide's field 43 lists type-153 records, probably the build's steps. This experiment checks whether writing the delivery changes how a build plays. It counts the stages Keynote exports when asked for every stage of every build.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0257/build.key`: a title (text storage 2652192, "One") with a Dissolve build-in, record 2652689, delivery `All at Once`; and `samples/0257/plain.key`, the same slide without a build |
| Writer | The writer of [0287](0287-rewriting-a-document.md) and [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0368
cd samples/0368
R=../../recipes/0302-set-path.py
python3 -I ../../recipes/0287-iwa-writer.py ../0257/build.key three-words.key --text 2652192 "One two three"
python3 -I $R three-words.key by-word.key 2652689 2 string "By Word"
python3 -I $R three-words.key by-char.key 2652689 2 string "By Character"
python3 -I ../../recipes/0287-iwa-writer.py ../0257/build.key three-paras.key --text 2652192 "$(printf 'One\ntwo\nthree')"
python3 -I $R three-paras.key by-paragraph.key 2652689 2 string "By Paragraph"
python3 -I $R three-paras.key by-bullet.key 2652689 2 string "By Bullet"
```

`by-word.key` was also written with each of these set to 2, and 4.4 and 5 also to 3: fields 4.4, 4.20, 4.21 and 5 of the build. Keynote opened each file on its own and exported it with `as slide images with properties {image format:PNG, all stages:true}`.

## Observation

| File | Images |
| --- | --- |
| `plain.key` (no build) | 1 |
| `three-words.key`, `by-word.key`, `by-char.key` | 2 each |
| `by-word.key` with 4.4, 4.20, 4.21 or 5 changed | 2 each |
| `three-paras.key`, `by-paragraph.key`, `by-bullet.key` | 2 each |

With the title selected, Keynote's Animate sidebar showed a Text Animation menu (*Tekstanimasjon*, set to "By Object") above the Delivery menu (*Levering*, "All at Once"). Setting the delivery in the sidebar to make a reference file was tried. It couldn't be done: the menu is a pop-up that can't be opened without taking over the screen, and that approval got no answer.

The build's only type-153 record names the build in field 1. It has 1.0 in field 4, 0 in field 5 and 1 in field 6, and holds a 128-bit ID in fields 7.1 and 8.

## Conclusion

Writing the delivery text doesn't change how the build plays: the build stays one stage whatever field 2 says. Changing fields 4.4, 4.20, 4.21 or 5 doesn't either. A build's stages are probably its type-153 records, one per stage, so a delivery in steps would need one such record per paragraph. That is left for a later experiment, starting from a reference file made in Keynote.

## Confidence

*Confirmed*: field 2 alone doesn't set the number of stages. *Likely*: the type-153 records are the stages.
