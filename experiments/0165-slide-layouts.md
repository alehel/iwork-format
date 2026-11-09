# 0165: The first six slide layouts

**Status:** run

[0046](0046-slide-layout.md) found that a slide names its layout in field 17. This experiment uses the first six layouts of the default theme, in the order Keynote lists them.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0046](0046-slide-layout.md) |

## Recipe

```bash
mkdir -p samples/0165
osascript recipes/0159-keynote-slides.applescript layouts "$PWD/samples/0165/layouts.key"
```

## Observation

Each slide's field 17 names a different template slide, and each template slide (type 5) has its name in field 10:

| Slide | Field 17 | Name (field 10) |
| --- | --- | --- |
| 1 | 2651742 | Tittel (Title) |
| 2 | 2651768 | Tittel og bilde (Title and photo) |
| 3 | 2651799 | Tittel og bilde alt. |
| 4 | 2651826 | Tittel og punkttegn (Title and bullets) |
| 5 | 2651849 | Punkttegn (Bullets) |
| 6 | 2651868 | Tittel, punkttegn og bilde |

## Conclusion

Keynote lists layouts in the order of their IDs here. The names in field 10 are in the language of the app, so a reader shouldn't rely on them to tell layouts apart. The new slides in [0162](0162-ten-slides.md) used `Tittel og punkttegn`.

## Confidence

*Likely*: field 10 of a template slide is its layout name, in the app's language.
