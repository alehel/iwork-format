# 0158: The Essay template

**Status:** run

This experiment makes an unchanged document from the Essay template, to see how its placeholder text and automatic fields are stored.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0020/plain.pages` (the body text `one`) |

## Recipe

```bash
mkdir -p samples/0158
osascript recipes/0149-pages-text.applescript essay "$PWD/samples/0158/essay.pages"
```

## Observation

The body text begins with the author's name, `Instruktørens navn` (Instructor's name), a date, `Essaytittel` (Essay title), `Undertittel` (Subtitle), and paragraphs of instructions. The author's name came from the user's own contact card; it isn't quoted here.

The body record has a field 11 not seen before: a run table whose entries point at objects:

| From | To | Object type | Holds |
| --- | --- | --- | --- |
| 0 | 19 | 2036 | Field 2: `TPMailMerge_FullNamePseudoProperty` |
| 20 | 38 | 2031 | A UUID, and 2 = 1 |
| 39 | 55 | 2034 | Field 2: the date format `d. MMMM y`, field 3: the locale `nb_NO` |
| 58 | 69 | 2031 | |
| 70 | 82 | 2031 | |
| 83 | … | 2031 | |

Each range ends at an entry with no field 2. The root has extra fields 2, 3, 4, 6, 7, 20 and 47 compared with blank documents.

## Conclusion

Field 11 of a text record is a run table of smart fields over ranges of the text:

- **Type 2031:** placeholder text, which the user replaces by typing.
- **Type 2034:** a date field, with its format and locale.
- **Type 2036:** a merge field, here the author's full name.

The text inside each range is what the field shows now. A reader can show it as plain text and still be right; to update fields, it needs these records.

## Confidence

*Likely*: body field 11 marks smart-field ranges, with types 2031 placeholder, 2034 date and 2036 merge field.

*Unknown*: what fields 4–8 of the date field mean.
