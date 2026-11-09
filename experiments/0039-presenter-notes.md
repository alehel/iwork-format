# 0039: Presenter notes

**Status:** run

This experiment asks where Keynote keeps a slide's presenter notes and how a reader finds them from the slide.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0025](0025-keynote-title.md), `empty.key` |

## Recipe

```bash
mkdir -p samples/0039
osascript recipes/0039-keynote-notes.applescript "$PWD/samples/0039/notes.key"
```

The recipe sets the `presenter notes` of the first slide of a new presentation to `notes here`.

## Observation

`iwork-probe text` finds the notes in `Index/Slide-2652175.iwa`, object 2652228, a type-2001 record with field 1 = 4. Header references lead to it as:

```
1 (type 1) → 2652410 (type 2) → 2652174 (type 4) → 2652175 (type 5, the slide)
  → 2652227 (type 15) → 2652228 (type 2001, "notes here")
```

The slide names 2652227 in its field 27. Record 2652227 holds only `1: { 1: 2652228 }`.

The empty presentation of 0025 already has object 2652227, of type 15, referring to 2652228 in the same way. There, 2652228 has no text.

## Conclusion

A slide's presenter notes are a text record, reached through the slide's field 27 and a type-15 notes record whose field 1 names the text. Every slide seems to have one, empty or not, so a reader can look for notes on every slide without a special case.

The notes text has field 1 = 4. That is a fourth value for field 1 of a text record ([0032](0032-reading-all-text.md)), alongside Pages' 0 (body) and 1 (header or footer). So field 1 seems to say what kind of text a record holds.

## Confidence

*Likely*:

- Slide field 27 names a type-15 notes record, and that record's field 1 names the notes text.
- Notes text has field 1 = 4.

*Unknown*: the full set of field-1 values.
