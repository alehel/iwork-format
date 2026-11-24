# 0481: The format version in Metadata.iwa

**Status:** run

The comparisons between releases ([0461](0461-new-documents-in-14-5.md), [0473](0473-every-scripted-sample-in-16-0.md), [0476](0476-resaving-every-sample.md)) list the top-level fields each record type uses, not what nested messages or packed values hold. Before the spec moves to describing 16.0, this experiment looks one step further for anything they missed. Comparing the nested fields of the published samples between releases found one: field 7 of the package metadata record, type 11006 in `Index/Metadata.iwa`, whose bytes differ in every release.

## Setup

| | |
| --- | --- |
| Tool | No app: the new [`recipes/0481-format-version.py`](../recipes/0481-format-version.py), which reads field 7 as packed varints and compares it with `fileFormatVersion` in `Properties.plist`, and checks each copy's last build against the release its folder names |
| Date | 2026-11-25 |
| Input | Every `.pages`, `.numbers` and `.key` in `samples/`, the sets for each release and the resaved copies included: 6,140 documents that aren't encrypted |

## Recipe

```bash
python3 -I recipes/0481-format-version.py samples
```

## Observation

Field 7 is the file format version, as packed varints:

| Release | Field 7, bytes | Read | `fileFormatVersion` |
| --- | --- | --- | --- |
| 16.0 | `1b 00 01` | 27, 0, 1 | `27.0.1` |
| 15.4 | `1a 04 00` | 26, 4, 0 | `26.4.0` |
| 14.5 | `0e 04 01` | 14, 4, 1 | `14.4.1` |
| 13.1 | `0d 01 02` | 13, 1, 2 | `13.1.2` |

It equals `fileFormatVersion` in all 6,140 documents, in all three apps and in folder packages. The 31 documents that couldn't be read are encrypted.

| Documents | Format version | Last saved by |
| --- | --- | --- |
| 1,260 samples | 26.4.0 | 15.4 |
| 60 samples and 313 under `release/14.5/` | 14.4.1 | 14.5 |
| 66 samples, 313 under `release/16.0/`, 1,211 under `resave/16.0/` and 182 under `resaved/16.0/` | 27.0.1 | 16.0 |
| 313 under `release/13.1/` and 1,211 under `resave/13.1/` | 13.1.2 | 13.1 |
| 1,211 under `resave/14.5/` | 27.0.1 | **16.0** |

The last row is a mistake in [0476](0476-resaving-every-sample.md): its 14.5 copies were saved by the installed 16.0 apps. [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) opens "Pages Creator Studio" and so on when they are installed, and they were, whatever else was running. 0476 is corrected, and [`recipes/0476-resave.py`](../recipes/0476-resave.py) now counts a copy as failed when the release that saved it isn't the one named.

The nested comparison found no other field that only one release writes, apart from those already listed on the [releases](../spec/releases.md) page. It covers which fields are present, not all their values.

## Conclusion

`Metadata.iwa` repeats the file format version, so a reader of the records alone can tell it. What the app does with it on opening, and whether a writer that changes one has to change the other, is *unknown*.

Every set of samples was saved by the release it is named for, except the copies 0476 called 14.5's.

## Confidence

*Confirmed*: for 6,140 documents from four releases, field 7 of type 11006 is `fileFormatVersion` as packed varints.
