# 0436: Writing a soft hyphen

**Status:** run

Text can contain U+00AD, the soft hyphen, as found in the samples ([0032](0032-reading-all-text.md)). This experiment writes soft hyphens into long words in a document without hyphenation and reads where Pages breaks the lines.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0002/hello.pages`, with its body (1732539) replaced by seven long Norwegian compound words; hyphenation is off (settings field 9 = 0, [0420](0420-writing-hyphenation.md)) |
| Writer | The writer of [0287](0287-rewriting-a-document.md); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0374-pdf-text.swift`](../recipes/0374-pdf-text.swift) |

## Recipe

```bash
mkdir -p samples/0436
O=samples/0436
TXT="Arbeidsmiljølovgivningen fylkeskommunesammenslåingen sannsynlighetsberegningene kommunikasjonsteknologien vedlikeholdsarbeidene forskningsinstitusjonene arbeidsledighetstrygden"
SH=$(printf '\xc2\xad')
SOFT=$(echo "$TXT" | sed "s/kommunikasjons/kommunikasjons$SH/; s/arbeidsledighets/arbeidsledighets$SH/")
python3 -I recipes/0287-iwa-writer.py samples/0002/hello.pages $O/plain.pages --text 1732539 "$TXT"
python3 -I recipes/0287-iwa-writer.py samples/0002/hello.pages $O/soft-hyphens.pages --text 1732539 "$SOFT"
for f in plain soft-hyphens; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF
return count of characters of body text of d"
  swift recipes/0374-pdf-text.swift $O/$f.pdf
done
```

The soft hyphens go after `kommunikasjons` and after `arbeidsledighets`.

## Observation

| File | Characters | Lines |
| --- | --- | --- |
| `plain.pages` | 176 | … `sannsynlighetsberegningene` / … `forskningsinstitusjonene` / `arbeidsledighetstrygden` |
| `soft-hyphens.pages` | 178 | … `sannsynlighetsberegningene` / … `forskningsinstitusjonene arbeidsledighets-` / `trygden` |

The first line ends at the same place in both; `kommunikasjons-` wouldn't have fitted on it.

## Conclusion

A soft hyphen is a place where Pages may break a word, even with hyphenation off: where the word reaches the end of the line, Pages breaks there and draws a hyphen; elsewhere the soft hyphen isn't drawn. AppleScript counts it as a character. A reader laying out text should treat U+00AD the same way.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `plain.pages` | `0002/hello.pages` | Only `2001#1732539 3: changed`, `2001#1732539 3 ~ "arbeidsledighetstrygden"` | *Control*: the last word is on a line of its own |
| `soft-hyphens.pages` | `plain.pages` | Only `2001#1732539 3: changed`, `2001#1732539 3 ~ "kommunikasjons\u00adteknologien"`, `2001#1732539 3 ~ "arbeidsledighets\u00adtrygden"` | *Confirmed*: U+00AD is an optional break, drawn as a hyphen only at the end of a line |

## Confidence

*Confirmed*: U+00AD as an optional break that Pages draws as a hyphen only at the end of a line, by writing it.
