# Test theme

`iwork-format test.kth` is a Keynote theme for making shareable sample presentations. Its master slides are those of Keynote 15.4's Basic White, with every photo replaced by a test card from `cards/`. Each card states its own name, size and format.

The cards and the theme's images were made by this project and are released under [CC0](https://creativecommons.org/publicdomain/zero/1.0/). The theme still contains Basic White's layouts, styles and placeholder text.

To rebuild it, see [experiment 0291](../experiments/0291-test-theme.md):

```bash
swift recipes/0291-test-cards.swift theme/cards
osascript recipes/0291-test-theme.applescript "$PWD/theme/cards" "$PWD/samples/0291/test-theme.key"
```

Then use every master on a slide, save, and choose File → Save Theme in Keynote.

On the Mac the experiments run on, Keynote lists it as `iwork-format test v2`, and the recipes use that name. It also lists a first version, with cards at full size, as `iwork-format test`; a presentation from that one is about 2.5 MB instead of 0.9 MB ([0473](../experiments/0473-every-scripted-sample-in-16-0.md)).
