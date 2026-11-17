# 0394: Renaming a part

**Status:** run

Part names aren't fixed: saving again can rename a part after the ID of its new first record, such as `ViewState.iwa` becoming `ViewState-1732662.iwa` ([0139](0139-resave.md)). This experiment renames parts in the ZIP and asks whether Pages still opens the document, first with nothing else changed and then with `Metadata.iwa` updated.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0002/hello.pages`: the body `hello`, with the parts `Document.iwa`, `DocumentStylesheet.iwa`, `Metadata.iwa`, `ViewState.iwa`, `DocumentMetadata.iwa`, `AnnotationAuthorStorage-1732609.iwa` and `CalculationEngine-1732610.iwa` under `Index/` |
| Writer | The new [`recipes/0394-rename-part.py`](../recipes/0394-rename-part.py); read back with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) |

## Recipe

```bash
mkdir -p samples/0394
R=recipes/0394-rename-part.py
F=samples/0002/hello.pages
O=samples/0394
python3 -I $R $F $O/document-numbered.pages Index/Document.iwa Index/Document-1234567.iwa
python3 -I $R $F $O/document-other.pages Index/Document.iwa Index/Zebra.iwa
python3 -I $R $F $O/stylesheet-numbered.pages Index/DocumentStylesheet.iwa Index/DocumentStylesheet-42.iwa
python3 -I $R $F $O/stylesheet-own-id.pages Index/DocumentStylesheet.iwa Index/DocumentStylesheet-1732613.iwa
python3 -I $R $F $O/viewstate-own-id.pages Index/ViewState.iwa Index/ViewState-1732641.iwa
python3 -I $R $F $O/viewstate-other.pages Index/ViewState.iwa Index/ViewState-99.iwa
python3 -I $R $F $O/annotation-plain.pages Index/AnnotationAuthorStorage-1732609.iwa Index/AnnotationAuthorStorage.iwa
python3 -I $R $F $O/metadata-other.pages Index/Metadata.iwa Index/Alpha.iwa
python3 -I $R $F $O/viewstate-99-listed.pages Index/ViewState.iwa Index/ViewState-99.iwa --metadata
python3 -I $R $F $O/document-zebra-listed.pages Index/Document.iwa Index/Zebra.iwa --metadata
python3 -I $R $F $O/annotation-plain-listed.pages Index/AnnotationAuthorStorage-1732609.iwa Index/AnnotationAuthorStorage.iwa --metadata
for f in $O/*.pages; do sh recipes/0372-in-app.sh Pages $f 'return body text of d'; done
```

1732613 and 1732641 are the IDs of the first records in `DocumentStylesheet.iwa` and `ViewState.iwa`. Pages' alerts were read and dismissed through System Events.

A search of every record for the parts' names found them only in `Metadata.iwa` record 2. Its repeated field 3 lists the components, one per part: field 1 is an object ID (the part's first record, such as 1 for `Document`), field 2 the component's name, and field 3, present only for `AnnotationAuthorStorage` and `CalculationEngine`, the part's stored name, `AnnotationAuthorStorage-1732609`. With `--metadata`, the recipe also writes the new stored name into that entry's field 3, or removes field 3 when the new name is the component's name.

## Observation

| File | Part renamed | `Metadata.iwa` | Pages |
| --- | --- | --- | --- |
| `document-numbered.pages` | `Document` → `Document-1234567` | unchanged | "is damaged and can't be opened" |
| `document-other.pages` | `Document` → `Zebra` | unchanged | damaged |
| `stylesheet-numbered.pages` | `DocumentStylesheet` → `DocumentStylesheet-42` | unchanged | damaged |
| `stylesheet-own-id.pages` | `DocumentStylesheet` → `DocumentStylesheet-1732613` | unchanged | damaged |
| `viewstate-own-id.pages` | `ViewState` → `ViewState-1732641` | unchanged | damaged |
| `viewstate-other.pages` | `ViewState` → `ViewState-99` | unchanged | damaged |
| `annotation-plain.pages` | `AnnotationAuthorStorage-1732609` → `AnnotationAuthorStorage` | unchanged | damaged |
| `metadata-other.pages` | `Metadata` → `Alpha` | | "can't be opened at the moment" |
| `viewstate-99-listed.pages` | `ViewState` → `ViewState-99` | entry updated | opens, `hello` |
| `document-zebra-listed.pages` | `Document` → `Zebra` | entry updated | opens, `hello` |
| `annotation-plain-listed.pages` | `AnnotationAuthorStorage-1732609` → `AnnotationAuthorStorage` | entry updated | opens, `hello` |

## Conclusion

Pages finds each part through the component list in `Metadata.iwa` record 2, field 3: a part is stored as `Index/` plus the entry's field 3, or its field 2 when there is no field 3, plus `.iwa`. Any name works as long as the list says so, even `Zebra.iwa` for the body, and renaming a part without updating its entry makes the document damaged, even to the `-N` form that saving produces. `Metadata.iwa` itself can't move: it is where the list is.

So a reader can find parts by listing the ZIP, as the spec says, but a writer that renames or adds a part must update the component list.

## Confidence

*Confirmed*: `Metadata.iwa` record 2's field 3 as the list of components, with field 2 the name and field 3 the stored name when it differs, by renaming parts with and without it.
