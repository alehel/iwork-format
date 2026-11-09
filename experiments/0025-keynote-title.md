# 0025: Text on a Keynote slide

**Status:** run

[0024](0024-keynote-and-numbers.md) found that Keynote shares Pages' container, but left open whether the record types inside mean the same thing in both apps. This experiment puts a word in the title of a Keynote slide and checks whether it lands in the same kind of text record as Pages' body text ([0002](0002-one-word.md)).

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0024](0024-keynote-and-numbers.md), `empty-a.key`, copied as `samples/0025/empty.key` |

## Recipe

```bash
mkdir -p samples/0025
osascript recipes/0025-keynote-title.applescript "$PWD/samples/0025/hello.key"
osascript recipes/0025-keynote-title.applescript "$PWD/samples/0025/hullo.key" hullo
cp samples/0024/empty-a.key samples/0025/empty.key
```

The recipe makes a new presentation with the default theme and sets the `object text` of the first slide's default title item.

## Observation

Searching every record of `hello.key` for the text `hello` finds one: object 2652192, of type 2001, in `Index/Slide-2652175.iwa`.

```
2:  { 1: 2652414 }                     ← type 401 in DocumentStylesheet.iwa
3:  text "hello"
5:  { 1: { 1: 0, 2: { 1: 2651125 } } }  ← type 2022 "Tittel", text-0-paragraphstyle-Title
6:  { 1: { 1: 0, 2: 0, 3: 0 } }
7:  { 1: { 1: 0, 2: { 1: 2651120 } } }  ← type 2023 "Ingen", text-0-liststyle-None
10: 1
14: { 1: { 1: 0, 2: 0, 3: 0 } }
24: { 1: { 1: 0, 2: 0, 3: 0 } }
28: { 1: { 1: 0 } }
```

In `empty.key` the same record has no field 3, and is otherwise the same. Between `hello.key` and `hullo.key`, field 3 is the only difference in the record.

Compared with Pages' body record, fields 1, 12 and 17 are absent. Field 17 holds the section runs in Pages.

## Conclusion

Keynote stores a title's text in a type-2001 record laid out exactly like Pages' body text:

- the text in field 3, absent when empty
- the stylesheet in field 2
- paragraph styles, list levels and list styles in fields 5, 6 and 7, as run tables

The objects it refers to are a stylesheet (type 401), a paragraph style (type 2022) and a list style (type 2023), with the same kinds of names as in Pages. So these type numbers mean the same thing in Pages and Keynote, and the text layer of the spec applies to Keynote text too.

A slide has no sections, and its text record has no section runs (field 17), and no fields 1 or 12.

## Confidence

*Likely*:

- Keynote text is a type-2001 record laid out as in [spec/text.md](../spec/text.md).
- Type numbers 2001, 401, 2022 and 2023 mean the same thing in Pages and Keynote.

*Unknown*:

- What links a slide's title record to the slide.
- Whether Keynote's type 1 (the document root) means the same as Numbers' type 1.
