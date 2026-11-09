# 0212: Placeholder text of my own

**Status:** run

Templates hold placeholder text as type-2031 smart fields ([0158](0158-essay-template.md), [0199](0199-letter-merge-fields.md)), always with field 2 set to 1. Pages lets any text be made into placeholder text. This experiment does that to one word, to confirm the record and see field 2 change.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiments [0158](0158-essay-template.md) and [0199](0199-letter-merge-fields.md) |

## Recipe

1. Make a document with the body text `One two`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "One two"'
   ```
2. Double-click `two`, then choose Format → Advanced → Define as Placeholder Text (*Format → Avansert → Definer som eksempeltekst*).
3. Save it as `samples/0212/placeholder.pages`.

## Observation

The body text is still `One two`, and no character style is added. Run table 11 has no field at 0, then at 4 a type-2031 record:

```
1: { 1: "74FB6F12-D794-4ADF-BCF4-47E22B2F8ECD" }
2: 0
```

## Conclusion

Placeholder text made in a document is the same type-2031 smart field as a template's, run over the placeholder's text. Field 2 differs: 0 here, against 1 in every template placeholder seen. It probably records where the placeholder came from, or whether its prompt should be selected as a whole when clicked. The prompt is the text the run covers.

## Confidence

*Confirmed*, with 0158 and 0199: placeholder text is a type-2031 smart field over its prompt.

*Unknown*: the meaning of field 2.
