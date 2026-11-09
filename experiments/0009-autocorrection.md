# 0009: Autocorrection

**Status:** run

[0006](0006-typing-in-pages.md) found two fields in the body's type-2001 record that only appear when text is typed in the Pages window. They are field 19, with the language `nb`, and field 20, with UUIDs that lined up with words Pages capitalised. This experiment tests that reading. If field 20 records autocorrections, text typed without any correction should have no field 20, and a correction made mid-text should get a UUID range at exactly that word.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface and Pages' default autocorrection settings |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0006](0006-typing-in-pages.md) |

## Recipe

AppleScript makes a new document and sets its body text to `one`, which Pages doesn't autocorrect. Then the text is typed at the end of the line in the Pages window, and AppleScript saves the document:

| File | Typed | What Pages showed |
| --- | --- | --- |
| `no-capital.pages` | ` two` | `one two`, no changes |
| `capital.pages` | `. two ` | When `.` was typed, `one` became `One`. After the final space, `two` became `Two` and was underlined in blue, Pages' mark for an autocorrected word. |

## Observation

The body's type-2001 record:

```
no-capital.pages
3: text (7 bytes) "one two"
19: { 1: { 1: 0 },
      1: { 1: 3, 2: "nb" } }
(no field 20)

capital.pages
3: text (9 bytes) "One. Two "
19: { 1: { 1: 0, 2: "nb" } }
20: { 1: { 1: 0, 2: "09C2C8E6-72CD-4803-8A8E-826E1D2880A2" },
      1: { 1: 4 },
      1: { 1: 5, 2: "416C57A2-A63A-497E-8613-8792EF92052D" },
      1: { 1: 8 } }
```

In `no-capital.pages`, field 19 has no language for positions 0–3, the text AppleScript set, and `nb` from 3, where typing began. There is no field 20.

In `capital.pages`, field 20 has two UUID runs: 0–4 (`One.`) and 5–8 (`Two`). These are the two places Pages corrected. Field 19 covers the whole text with `nb`, including `One`, which Pages rewrote.

## Conclusion

Field 20 records autocorrections. Each corrected range is a run with its own UUID, closed by an entry without one. Text with no corrections has no field 20. A first correction ran over `One.`, not just `One`, probably because typing the full stop is what triggered it. That suggests the range covers what Pages replaced, not just the changed letter.

Field 19 holds language runs, and only on text that was typed or rewritten in the window. Text set through AppleScript has no language, shown either as no field 19 or as a run with no language.

A reader that only wants the text and its formatting can skip both fields.

## Confidence

*Confirmed*:

- Field 20 records autocorrected ranges with a UUID each. 0006 suggested it, and the prediction held here.
- Field 19 holds language runs on typed text (0006 and this experiment).

*Unknown*:

- What the UUIDs refer to. No other record in these files contains them.
- Whether undoing a correction in Pages removes its run. Follow-up: click the underlined word, choose to revert, then save.
