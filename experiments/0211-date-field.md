# 0211: A date field

**Status:** run

[0158](0158-essay-template.md) found a type-2034 date field in the Essay template, with a format and a locale. This experiment inserts a date field through the menus, to confirm the reading and look for the date itself.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0158](0158-essay-template.md) |

## Recipe

1. Make a document with the body text `One`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "One"'
   ```
2. Click after `One`, then choose Insert → Date & Time (*Sett inn → Dato og tid*). Pages shows `Onemandag 9. november 2026`.
3. Save it as `samples/0211/date.pages`.

## Observation

The body text is `Onemandag 9. november 2026`: the date is stored as ordinary text. Run table 11 has no field at 0, then at 3 a type-2034 record:

```
1: { 1: "0C451A4D-9FFC-4441-9506-0DECA302B808" }
2: "EEEE d. MMMM y"
3: "nb_NO"
4: 4
5: 0
6: 0
7: 0
8: { 1: 815943303.40 }   ← seconds since 2001-01-01: 2026-11-09 18:55:03 UTC
10: 0
```

## Conclusion

A date field is a type-2034 smart field over the date's text. Field 2 is the format as a Unicode date pattern (`EEEE` the weekday, `MMMM` the month's name, `y` the year), field 3 the locale and field 8 the date itself, in seconds since 2001 like other times in the format. The text in the body is the date already formatted. A reader can show it as it is, or format field 8 again. Field 4 is probably the date style chosen in the app (4 being the full style), and fields 5–7 options such as showing the time and updating automatically.

## Confidence

*Confirmed*, with 0158: a date field is type 2034, with its format in field 2 and its locale in field 3.

*Likely*: field 8 is the date.

*Unknown*: fields 4–7 and 10.
