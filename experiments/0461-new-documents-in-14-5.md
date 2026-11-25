# 0461: New documents in Pages and Numbers 14.5

**Status:** run

Everything so far was found with the 15.4 apps. This experiment saves the simplest documents with the older Pages and Numbers 14.5, using the recipes of the first experiments unchanged, and compares their structure with the 15.4 documents those recipes made.

## Setup

| | |
| --- | --- |
| Pages | 14.5 (build `M14.5-7045.0.17-4`), in Norwegian |
| Numbers | 14.5 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-23 |
| Compared with | `samples/0001/empty-a.pages`, `samples/0002/hello.pages` and `samples/0026/cells.numbers`, from Pages and Numbers 15.4 |
| Script | The new [`recipes/0461-compare-structure.py`](../recipes/0461-compare-structure.py), which compares two documents' ZIP entries, `Properties.plist` and `BuildVersionHistory.plist`, and for each part the records of each type, each type's version (header field 2.2) and the top-level fields each type uses |

The 14.5 apps are installed as `Pages` and `Numbers`, without the 15.4 apps' "Creator Studio" in their names. [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) now uses whichever is installed.

## Recipe

```bash
mkdir -p samples/0461
osascript recipes/0001-empty-document.applescript "$PWD/samples/0461/empty.pages"
osascript recipes/0002-one-word.applescript "$PWD/samples/0461/hello.pages"
osascript recipes/0026-numbers-cells.applescript "$PWD/samples/0461/cells.numbers"
python3 -I recipes/0461-compare-structure.py samples/0001/empty-a.pages samples/0461/empty.pages
python3 -I recipes/0461-compare-structure.py samples/0002/hello.pages samples/0461/hello.pages
python3 -I recipes/0461-compare-structure.py samples/0026/cells.numbers samples/0461/cells.numbers
```

## Observation

The same in all three pairs: the same ZIP entries, the same parts, the same number of records of every type in every part but one, and the same version in header field 2.2 for every type both releases write.

The differences, besides UUIDs:

| | 15.4 | 14.5 |
| --- | --- | --- |
| `Properties.plist` `fileFormatVersion` | `26.4.0` | `14.4.1` |
| `Properties.plist` flags | `hasExternalReferenceOrMissingData` and `hasUnmaterializedRemoteData`, both false | `hasExternalReferenceOrMissingOrUnmaterializedRemoteData`, false |
| `BuildVersionHistory.plist` | `Template: Blank (dev/15.4)`, `M15.4-7051.0.79-2` | `Template: Blank (13.2)` (Numbers: `(11.2)`), `M14.5-7045.0.17-4` |
| `CalculationEngine.iwa` | a type-4011 record, empty, named by field 15 of the engine's root (type 4000) | neither the record nor field 15 |
| Numbers' `DocumentStylesheet.iwa` | 245 paragraph styles (type 2022) | 244 |

## Conclusion

Pages and Numbers 14.5 write the same format as 15.4: everything the spec describes for these documents is laid out the same way, down to the record versions. The release that saved a document can be told from `fileFormatVersion` in `Properties.plist` and from the build in `BuildVersionHistory.plist`; the format version doesn't follow the app's version (14.5 writes 14.4.1, 15.4 writes 26.4.0). 15.4 adds an empty type-4011 record to the calculation engine, which a reader can ignore as it ignores the engine. Whether larger documents differ more is for the next experiments.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `empty.pages` | `0001/empty-a.pages` | `11006#2 7: x"1a0400" → x"0e0401"`, `records 4011: 1 → 0`, `records 2022: 242 → 242` | *Confirmed*: 14.5 writes the same parts, record types and versions, but for the format version, the build and type 4011 |
| `hello.pages` | `0002/hello.pages` | `11006#2 7: x"1a0400" → x"0e0401"`, `records 4011: 1 → 0` | *Confirmed*: as above |
| `cells.numbers` | `0026/cells.numbers` | `11006#2 7: x"1a0400" → x"0e0401"`, `records 4011: 1 → 0`, `records 2022: 245 → 244`, `2022 1.2: "text-12-paragraphstyle-Table Title 1" → absent` | *Confirmed*: as above, with one paragraph style fewer in a spreadsheet |

## Confidence

*Confirmed*: for an empty document, a one-word document and a spreadsheet with cells, 14.5 writes the same parts, record types and versions as 15.4, apart from the differences listed.
