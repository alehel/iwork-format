# 0046: A slide's layout

**Status:** run

Each Keynote theme comes with layouts, which Keynote's AppleScript calls master slides. A new presentation has 17 `TemplateSlide-N.iwa` parts, one per layout ([0024](0024-keynote-and-numbers.md)). This experiment switches a slide to a different layout, to see how a slide names its layout.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0025](0025-keynote-title.md), `empty.key` (slide 1 on the layout *Tittel*, Title) |

## Recipe

```bash
mkdir -p samples/0046
osascript recipes/0046-keynote-layout.applescript "$PWD/samples/0046/blank-layout.key" "Tom"
```

The theme's layouts, as AppleScript lists them, are:

> Tittel, Tittel og bilde, Tittel og bilde alt., Tittel og punkttegn, Punkttegn, Tittel, punkttegn og bilde, Tittel, punkttegn og direktevideo – liten, Tittel, punkttegn og direktevideo – stor, Inndeling, Kun tittel, Dagsorden, Melding, Fakta, stor, Sitat, Bilde – 3 per side, Bilde, Tom

The recipe sets slide 1's `base slide` to the layout *Tom* (Blank).

## Observation

| Slide field | `empty.key` (Title) | `blank-layout.key` (Blank) |
| --- | --- | --- |
| 1 | `{ 1: 2651744 }` | `{ 1: 2652159 }` |
| 17 | `{ 1: 2651742 }` | `{ 1: 2652157 }` |
| 19 | 1 | 1 |
| 20 | `{ 1: 2652224 }` | `{ 1: 2652224 }` |

The slide's header references also lost 2652180 and kept the title shape (2652199) and the notes (2652227).

Records 2651742 and 2652157 are both of type 5 and are the first records of `TemplateSlide-2651742.iwa` and `TemplateSlide-2652157.iwa`. Their field 10 is `Tittel` and `Tom`, and both hold the texts `Transition` and `none`.

## Conclusion

A slide's field 17 names its layout: a template slide, which is itself a slide (type 5) in its own `TemplateSlide-N.iwa` part, named in its field 10. Field 1 changes along with it, so it is probably the slide's style, taken from the layout. A reader can show a slide by drawing its layout's template slide first and then the slide's own shapes on top. That drawing order isn't tested.

## Confidence

*Likely*:

- Slide field 17 names its layout (a type-5 template slide).
- A template slide's field 10 is its name.

*Unknown*:

- Slide field 1, and why the slide stopped referring to 2652180.
- How a slide's shapes relate to its layout's placeholders.
