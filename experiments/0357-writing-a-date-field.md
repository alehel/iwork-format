# 0357: Writing a date field

**Status:** run

A date field is a smart field over a range of the body (run table 11) pointing at a type-2034 record ([0211](0211-date-field.md)). In `samples/0211/date.pages` that record holds a date pattern in field 2 (`EEEE d. MMMM y`), a locale in field 3 (`nb_NO`), 4 = 4, 5, 6 and 7 = 0, and the date in field 8.1 as a double of seconds since 2001. This experiment writes a new date, pattern and locale, and each of fields 5 to 7, and reads the exported page's text.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0211/date.pages`: `One` followed by a date field showing `mandag 9. november 2026`, record 1732708 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0357
cp samples/0211/date.pages samples/0357/original.pages
R=recipes/0302-set-path.py
python3 -I $R samples/0357/original.pages samples/0357/date.pages 1732708 8.1 double 920289600
python3 -I $R samples/0357/date.pages samples/0357/pattern.pages 1732708 2 string "yyyy-MM-dd" 3 string en_US
for f in 5 6 7; do python3 -I $R samples/0357/pattern.pages samples/0357/f$f.pages 1732708 $f varint 1; done
```

920289600 seconds is 2030-03-01 12:00. Pages opened each file on its own and exported it as PDF; PDFKit extracted the page's text.

## Observation

Every file, original and written, shows `One` and `mandag 9. november 2026`.

## Conclusion

Pages draws a date field's text as it is stored in the body, under the smart field's run, and doesn't recompute it from the type-2034 record when it opens or exports a document, even with a new date, pattern or locale, or with field 5, 6 or 7 set. The record holds the field's settings for when Pages next updates the field itself; to change what a date field shows, a writer has to write the text in the body too. Which setting makes Pages update the date on opening isn't one of fields 5 to 7.

## Confidence

*Likely*: a date field shows its stored body text, not text made from its record.

*Unknown*: the meaning of fields 4 to 7, and how automatic updating is stored.
