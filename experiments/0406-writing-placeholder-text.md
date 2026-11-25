# 0406: Writing placeholder text

**Status:** run

Placeholder text is a type-2031 smart field in run table 11, over the text of its prompt. Its field 1 holds a UUID, and field 2 is 0 for a placeholder made in the document and 1 in templates ([0212](0212-placeholder-text.md)). Pages' AppleScript lists a document's `placeholder texts`, each with a `tag`. This experiment writes the run and the record.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0212/placeholder.pages`: `One two` in text 1732539, with `two` a placeholder: run table 11 has an entry at 0 with no field and one at 4 naming record 1732700 |
| Writer | [`recipes/0351-add-run.py`](../recipes/0351-add-run.py) for the run table, [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) for the record; read back with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) |

## Recipe

```bash
mkdir -p samples/0406
A=recipes/0351-add-run.py
R=recipes/0302-set-path.py
F=samples/0212/placeholder.pages
O=samples/0406
cp $F $O/original.pages
python3 -I $A $F $O/whole.pages 1732539 11 0 1732700
python3 -I $A $F $O/first-word.pages 1732539 11 0 1732700 3 0
python3 -I $A $F $O/none.pages 1732539 11 0 0
python3 -I $R $F $O/field3.pages 1732700 3 string mytag
python3 -I $R $F $O/template-kind.pages 1732700 2 varint 1
for f in original whole first-word none field3 template-kind; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages 'set out to {}
repeat with p in placeholder texts of d
  set end of out to {tag of p, (p as text)}
end repeat
return {body text of d, count of placeholder texts of d, out}'
done
```

A style of 0 in `recipes/0351-add-run.py` writes an entry with no field 2.

## Observation

| File | Written | Body | Placeholders | Tag, text |
| --- | --- | --- | --- | --- |
| `original.pages` | | One two | 1 | two, two |
| `whole.pages` | table 11: 0 → 1732700 | One two | 1 | One two, One two |
| `first-word.pages` | 0 → 1732700, 3 → none | One two | 1 | One, One |
| `none.pages` | 0 → none | One two | 0 | |
| `field3.pages` | 2031 field 3 = `mytag` | One two | 1 | mytag, two |
| `template-kind.pages` | 2031 field 2 = 1 | One two | 1 | two, two |

## Conclusion

A placeholder is exactly the range its table-11 run covers: moving the run's ends moves the placeholder, and without the run there is none, while the body text stays the same. Field 3 of the type-2031 record is the placeholder's script tag, a string, which AppleScript reports as `tag`; with no field 3, the tag is the placeholder's own text. Field 2 made no difference that AppleScript shows.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `original.pages` | `0212/placeholder.pages` | `same bytes`, `2001#1732539 11.1.1 = 4`, `2031#1732700 3 = absent` | *Control*: the placeholder is the second word |
| `whole.pages` | `original.pages` | Only `2001#1732539 11.1: ×2 → ×1`, `2001#1732539 11 = x"0a080800120408dce069"` (0 → 1732700) | *Confirmed*: the run is the placeholder's range: the whole text |
| `first-word.pages` | `original.pages` | Only `2001#1732539 11 = x"0a080800120408dce0690a020803"` (0 → 1732700, 3 → none) | *Confirmed*: as above, the first word |
| `none.pages` | `original.pages` | Only `2001#1732539 11.1: ×2 → ×1`, `2001#1732539 11 = x"0a020800"` (0 → none) | *Confirmed*: without a run there is no placeholder |
| `field3.pages` | `original.pages` | Only `2031#1732700 3: absent → "mytag"` | *Confirmed*: field 3 is the script tag |
| `template-kind.pages` | `original.pages` | Only `2031#1732700 2: 0 → 1` | *Unknown*: what field 2 changes; AppleScript shows no difference |

## Confidence

*Confirmed*: the table-11 run as the placeholder's range and field 3 of type 2031 as its script tag, by writing them. What field 2 changes is *unknown*.
