# 0306: Writing a shared string

**Status:** run

A text cell holds a key into the table's string table (type 6005), whose entries hold the key (3.1), the number of cells using it (3.2) and the string (3.3); equal texts share an entry ([0113](0113-shared-string.md)). If that is right, changing one entry's string should change every cell that uses it, and nothing else. This experiment writes such a change and asks Numbers.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0226/plain.numbers`: column A holds `a`, `b`, `a`, `b` in rows 2 to 5 |
| Writer | [`recipes/0306-rename-string.py`](../recipes/0306-rename-string.py), using the writer of [0287](0287-rewriting-a-document.md) |

## Recipe

```bash
mkdir -p samples/0306
cp samples/0226/plain.numbers samples/0306/original.numbers
python3 -I recipes/0306-rename-string.py samples/0306/original.numbers samples/0306/written.numbers 3 alpha
```

String key 3 is `a`, used by two cells. The script sets its string to `alpha`, leaving the cells alone. Numbers opened each file on its own through Launch Services ([0302](0302-writing-a-transition.md)), read A2 to A5 through AppleScript, and saved the written file again.

## Observation

| File | A2 | A3 | A4 | A5 |
| --- | --- | --- | --- | --- |
| `original.numbers` | a | b | a | b |
| `written.numbers` | alpha | b | alpha | b |

Saved again, the string table holds `kind` (key 1, 1 cell), `n` (2, 1), `alpha` (3, 2) and `b` (4, 2).

## Conclusion

Text cells hold only a key: both cells using key 3 show the new string, and Numbers keeps the entry and its use count as written. A writer can change every occurrence of a text by changing one entry.

## Confidence

*Confirmed*: string keys and the string table, by writing them.
