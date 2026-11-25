# 0420: Writing hyphenation

**Status:** run

Field 9 of the type-10012 document settings is *Hyphenate the whole document*, 1 for on ([0236](0236-hyphenation.md)). This experiment writes a paragraph of long words into a document and turns the field on and off.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0002/hello.pages`, with its body (1732539) replaced by sixteen (first written as fifteen) long Norwegian compound words, such as `Arbeidsmiljølovgivningen`; settings record 1732614 has no hyphenation (field 9 = 0) |
| Writer | The writer of [0287](0287-rewriting-a-document.md) for the text and [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0374-pdf-text.swift`](../recipes/0374-pdf-text.swift) |

## Recipe

```bash
mkdir -p samples/0420
O=samples/0420
TXT="Arbeidsmiljølovgivningen fylkeskommunesammenslåingen sannsynlighetsberegningene kommunikasjonsteknologien vedlikeholdsarbeidene forskningsinstitusjonene arbeidsledighetstrygden energieffektiviseringen samfunnsvitenskapelige rettighetshaverne bygningsingeniørene konkurransedyktighetens personopplysningsloven utviklingsmulighetene forsikringsselskapene undervisningsopplegget"
python3 -I recipes/0287-iwa-writer.py samples/0002/hello.pages $O/text.pages --text 1732539 "$TXT"
python3 -I recipes/0302-set-path.py $O/text.pages $O/hyphenate.pages 1732614 9 varint 1
python3 -I recipes/0302-set-path.py $O/text.pages $O/no-hyphenate.pages 1732614 9 varint 0
for f in text hyphenate no-hyphenate; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF"
  swift recipes/0374-pdf-text.swift $O/$f.pdf
done
```

## Observation

| File | Field 9 | Lines | Lines ending in a hyphen |
| --- | --- | --- | --- |
| `text.pages` | 0 | 5 | 0 |
| `no-hyphenate.pages` | 0, written | 5 | 0 |
| `hyphenate.pages` | 1, written | 5 | 3 |

With hyphenation, the first line ends `kommu-`, the third `konkur-` and the fourth `under-`; without it, every line ends with a whole word.

## Conclusion

Field 9 turns on hyphenation for the whole document: Pages then breaks long words at the end of a line, at places its Norwegian hyphenation rules allow. A reader laying text out the same way should hyphenate when the field is 1, in the text's language.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `text.pages` | `0002/hello.pages` | Only `2001#1732539 3: changed`, `2001#1732539 3 ~ "kommunikasjonsteknologien"` | *Control*: no line ends in a hyphen |
| `hyphenate.pages` | `text.pages` | Only `10012#1732614 9: 0 → 1` | *Confirmed*: field 9 hyphenates the document; three lines end in a hyphen |
| `no-hyphenate.pages` | `text.pages` | `same bytes`, `10012#1732614 9 = 0` | *Control*: no line ends in a hyphen |

## Confidence

*Confirmed*: type-10012 field 9 as hyphenating the whole document, by writing it.
