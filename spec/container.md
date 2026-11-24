# 1. Container

How a Pages document is packaged, and how its parts are encoded. Every finding links to the experiments that support it, with a confidence level as defined in [CONTRIBUTING.md](../CONTRIBUTING.md#confidence).

Observed with Pages 15.4 on macOS 26.5.2. Keynote 15.4 and Numbers 15.4 write the same container: the package, chunk, record and reference findings below hold for their documents too ([0024](../experiments/0024-keynote-and-numbers.md)). The apps differ in their document root (object 1: type 10000 in Pages, type 1 in Keynote and Numbers) and in the parts they add, such as `Slide-N` and `TemplateSlide-N` in Keynote.

## The package

A document saved by Pages is a ZIP file by default. *Likely* ([0001](../experiments/0001-empty-document.md), [0002](../experiments/0002-one-word.md)). It can also be a folder (File → Advanced → Change File Type → Package): the metadata files and previews are files in the folder, the `.iwa` parts are inside an `Index.zip` in it, under the same `Index/` names, and data files are in a `Data/` folder beside it. *Confirmed* for all three apps ([0076](../experiments/0076-package-format.md), [0146](../experiments/0146-keynote-package.md), [0147](../experiments/0147-numbers-package.md)), and by writing a package from a ZIP document, which Pages opens ([0438](../experiments/0438-writing-a-package.md))

Pages opens a document without any one of the `Metadata/` files (`Properties.plist`, `DocumentIdentifier`, `BuildVersionHistory.plist`) or the previews, and without all of `Metadata/`. But it doesn't open one without `Index/ViewState.iwa`, nor a ZIP with nothing outside `Index/`, and afterwards opens no document until it is restarted; so a writer should include the view state and the `Metadata/` files. *Confirmed* by writing them ([0434](../experiments/0434-leaving-out-package-files.md)); why is *unknown*.

ZIP entry names are UTF-8, but Pages doesn't set the ZIP flag that says so; read them as UTF-8 regardless. *Likely* ([0144](../experiments/0144-non-ascii-file-name.md)). Pages itself reads them as UTF-8 with or without the flag, *confirmed* by writing one ([0431](../experiments/0431-writing-a-non-ascii-part-name.md)).

Part names aren't fixed: after a document is saved again, a part can be renamed after the ID of its new first record (`ViewState.iwa` became `ViewState-1732662.iwa`). Find parts by listing them. *Likely* ([0139](../experiments/0139-resave.md))

The names come from a list of components in `Metadata.iwa` record 2, its repeated field 3: field 1 is the ID of the part's first record, field 2 the component's name, and field 3, only when it differs, the name it is stored under. A part is `Index/` plus field 3 (or field 2) plus `.iwa`. Any name works if the list says so, and a part renamed without its entry makes the document damaged, so a writer that renames or adds a part must update the list. *Confirmed* ([0394](../experiments/0394-renaming-a-part.md))

Its entries are stored without ZIP compression. *Confirmed* ([0001](../experiments/0001-empty-document.md), [0002](../experiments/0002-one-word.md)). Pages also opens a document whose entries are Deflate-compressed, so a reader must handle both methods and a writer may compress (*confirmed* by writing them, [0432](../experiments/0432-writing-compressed-zip-entries.md)).

A new document holds these 13 parts. *Confirmed* ([0001](../experiments/0001-empty-document.md), [0002](../experiments/0002-one-word.md))

| Part | Holds |
| --- | --- |
| `Index/*.iwa` (seven parts) | The document's objects, encoded as below |
| `Metadata/DocumentIdentifier` | A UUID as 36 ASCII characters, with no line ending |
| `Metadata/Properties.plist` | A binary property list of UUIDs, a file format version and flags. [release: differs by release] Its `fileFormatVersion` is `26.4.0` from the 15.4 apps, `27.0.1` from 16.0 and `14.4.1` from 14.5, and 14.5 writes one flag, `hasExternalReferenceOrMissingOrUnmaterializedRemoteData`, where 15.4 and 16.0 write two. `isMultiPage` says whether the document has more than one page, slide or sheet; the app sets it when it saves, and a writer that adds or removes pages should too, though Pages reads a document either way ([0476](../experiments/0476-resaving-every-sample.md)) ([0461](../experiments/0461-new-documents-in-14-5.md), [0469](../experiments/0469-the-16-0-apps.md)). |
| `Metadata/BuildVersionHistory.plist` | A list of strings naming the template and the Pages build. [release: differs by release] The build is `M15.4-7051.0.79-2` from 15.4, `M16.0-7052.0.68-2` from 16.0 and `M14.5-7045.0.17-4` from 14.5 ([0461](../experiments/0461-new-documents-in-14-5.md), [0469](../experiments/0469-the-16-0-apps.md)). |
| `preview.jpg`, `preview-web.jpg`, `preview-micro.jpg` | JPEG previews of the first page |

The seven `.iwa` parts of a new document are `AnnotationAuthorStorage-N`, `CalculationEngine-N`, `Document`, `DocumentMetadata`, `DocumentStylesheet`, `Metadata` and `ViewState`. Where a name ends in a number, it is the ID of the part's first object. *Confirmed* ([0001](../experiments/0001-empty-document.md), [0002](../experiments/0002-one-word.md))

A document with a table also has parts under `Index/Tables/`: `DataList`, `HeaderStorageBucket` and `Tile`, each holding one record. Each is named `Name.iwa`, `Name-N.iwa` or `Name-N-2.iwa`, where N is the ID of the record inside. Both Pages and Numbers use all three forms. What the `-2` ending means is *unknown*. *Likely* ([0020](../experiments/0020-a-table.md), [0026](../experiments/0026-numbers-cells.md), [0030](../experiments/0030-tiles.md))

## Data files

Files a document embeds, such as images, are stored unchanged under `Data/`, each named after its original file name with `-N` before the extension. N is a data ID, by which records refer to the file. *Likely* ([0023](../experiments/0023-an-image.md))

Identical files are stored once ([0142](../experiments/0142-same-image-twice.md)), in their original format ([0143](../experiments/0143-jpeg-image.md)), and files nothing uses are dropped on save ([0145](../experiments/0145-deleted-image.md)) (*confirmed* by writing such a file, listed or not: Pages opens the document and drops the file and its entry on saving, [0435](../experiments/0435-writing-an-unused-data-file.md)). For a large image, Pages also stores a reduced copy (`name-small-N.ext`), which the image record names in field 12 ([0148](../experiments/0148-large-image.md)). Keynote does the same, with the copy at most 256 pixels on the longer side, and stores an image used twice once ([0291](../experiments/0291-test-theme.md)). *Likely*

`Metadata.iwa` record 2 (type 11006) lists the data in its repeated field 4. Each entry holds the data ID (field 1), the file's SHA-1 (field 2), the original file name (field 3) and the stored file name (field 4). Entries for resources of the template have no file in the package. *Likely* ([0023](../experiments/0023-an-image.md)). Pages finds the file by field 4, whatever its pattern; a file renamed without its entry is drawn as a missing image. Field 3 is what AppleScript reports as the file name, and the SHA-1 isn't checked on opening. *Confirmed* by writing them ([0395](../experiments/0395-writing-a-data-file.md)).

In Keynote, a theme's own photos are such entries: field 4 (the stored name) is empty, field 5 is a path to the resource inside the app, such as `21_basicwhite/910457886_1434x1669`, Only a reduced copy, at most 256 pixels on the longer side, is stored in `Data/`, with its own entry, whose field 18 is the file's size in bytes. In every image's entry, stored or not, field 10.100.1 is the image's size in pixels: a message with the width in field 1 and the height in field 2, as floats.

Each data entry kept as an app resource, and only those, also has a colour: a type-11015 record in `Metadata.iwa` lists entries of a data ID (field 1) and a type-11014 colour (field 2), whose field 1 is RGB (1.1 = 1) with red, green, blue and alpha as floats in 1.3 to 1.6. *Confirmed* for 2,537 entries in 565 documents. The colour isn't the image's average; what it is for is *unknown*. ([0294](../experiments/0294-resource-colours.md)) *Likely* ([0292](../experiments/0292-test-theme-reruns.md)) [release: 15.4 and 14.5 differ] Which data is a resource can differ by release: Keynote 15.4 and 16.0 keep `blankMoviePosterImage.png` as a resource, with a colour ([0469](../experiments/0469-the-16-0-apps.md)), and Keynote 14.5 stores it in the package as `Data/blankMoviePosterImage-N.png`, without one ([0466](../experiments/0466-keynote-14-5.md)). That comes with 14.5's own Basic White: made from the test theme, which was saved by 15.4, a 14.5 presentation keeps it as a resource too ([0474](../experiments/0474-keynote-14-5-with-the-test-theme.md)).

## Chunks

An `.iwa` part is a sequence of chunks, with nothing before, between or after them. *Confirmed* ([0001](../experiments/0001-empty-document.md), [0002](../experiments/0002-one-word.md))

| Bytes | Holds |
| --- | --- |
| 1 | Chunk type. Always 0 so far. |
| 3 | Length of the data that follows, little-endian |
| length | A raw Snappy block (the block format, not the Snappy framing format) |

Pages accepts any valid raw Snappy block, including one made only of literal runs, so a writer need not compress: a document whose parts were re-encoded that way opens and saves normally. *Confirmed* ([0287](../experiments/0287-rewriting-a-document.md))

The apps write chunks that decode to at most 65,536 bytes: a part that decodes to more is split into chunks of exactly 65,536 decoded bytes, then a shorter last one. *Confirmed* ([0001](../experiments/0001-empty-document.md), [0141](../experiments/0141-large-text.md)). That is how Pages writes, not a limit a reader can rely on or one Pages enforces: it reads chunks of 1,000 decoded bytes, cutting records apart, and a single chunk of 338,982 (*confirmed* by writing them, [0433](../experiments/0433-writing-chunk-sizes.md)).

## Records

Decode every chunk and join the results in order. The joined bytes are a sequence of records, with nothing between them. A record can start in one chunk and end in the next, so the chunks have to be joined first. *Confirmed* ([0001](../experiments/0001-empty-document.md), [0002](../experiments/0002-one-word.md))

| Holds | Encoding |
| --- | --- |
| Header length | Varint |
| Header | Protocol Buffers message of that length |
| Payloads | One after another, one per header field 2, in the order those fields appear |

The header's fields:

| Field | Holds | Confidence |
| --- | --- | --- |
| 1 | Object ID, a varint. Unique across the whole document. | *Confirmed* that it's unique ([0001](../experiments/0001-empty-document.md), [0002](../experiments/0002-one-word.md)); that it identifies an object is *likely*, since other records refer to these numbers ([0002](../experiments/0002-one-word.md)). |
| 2 | One message per payload (repeated) | *Confirmed* |
| 2.1 | The payload's type, a varint: Pages decodes the payload by it, skips a record of a type it doesn't know, and calls the document damaged when the payload doesn't fit the type | *Confirmed* by writing it ([0396](../experiments/0396-writing-record-headers.md)) |
| 2.2 | Three packed varints, such as `1 0 5`: the same for every record of a type, so probably the version of that type's layout (`10 1 0` for placeholders, `3 2 10` for the calculation engine). Pages doesn't check it on opening: a higher, lower or missing value changes nothing | *Likely* ([0396](../experiments/0396-writing-record-headers.md), [0398](../experiments/0398-extra-payloads.md)) |
| 2.3 | The payload's length in bytes | *Confirmed* |
| 2.5 | Packed varints: IDs of objects the payload refers to. Pages doesn't need them to load a document ([0396](../experiments/0396-writing-record-headers.md)) | *Likely* ([0022](../experiments/0022-header-references.md)) |
| 2.4 | Repeated; field 4 of each entry holds more referenced IDs as packed varints, and field 1 is probably the field path that holds them | *Likely* ([0022](../experiments/0022-header-references.md)) |
| 2.6 | Packed varints: the data IDs of the files the payload uses, once per use (an image its own file, a list style its bullet image once per level). Present only on records that use data. Pages rebuilds it on saving and doesn't need it to open | *Confirmed* against 952 documents and by writing it ([0397](../experiments/0397-the-data-references-field.md)) |

Most records have one payload. In a new document, six records in `Document.iwa` have two, with the same 2.1 value and different 2.2 values. *Likely* ([0001](../experiments/0001-empty-document.md))

A payload of type 0, with 2.2 = 65535, 65535, 4294967295 and header fields 7 to 11, is an extra payload that Pages 15.4 ignores: Pages' donut and radar charts carry one, and Numbers' view state three. In a chart it holds an older chart type (5, a pie, for a donut) and its field 9 names the place it belongs (10000), so it is most likely a fallback for older versions of the apps. A reader can skip type-0 payloads. *Likely* ([0398](../experiments/0398-extra-payloads.md))

## Following references

Every ID in header fields 2.5 and 2.4.4 is a reference in the record's payload. *Confirmed* ([0022](../experiments/0022-header-references.md)). They are the references that lead down the object tree. References back up, such as a style's or a text's link to the stylesheet, or a table drawable's link to its text, aren't listed. *Likely* ([0022](../experiments/0022-header-references.md)). So the header lists are not every reference in a payload, and a reader that needs a payload's links reads them from its fields. Pages opens a document whose header lists are missing (header field 2.5 removed, [0396](../experiments/0396-writing-record-headers.md)), so a reader can meet an accepted document whose headers don't lead to every object.

In documents the apps saved, every object can be reached by starting at objects 1 (in `Document.iwa`), 2 (in `Metadata.iwa`) and 71 (in `DocumentMetadata.iwa`) and following the IDs in record headers, plus object 61 in `ObjectContainer.iwa` when a document has a chart. *Confirmed*: all 240,278 objects of the 353 samples, the 6 protected ones decrypted, were reached this way ([0022](../experiments/0022-header-references.md), [0024](../experiments/0024-keynote-and-numbers.md), [0178](../experiments/0178-regression-check.md), [0247](../experiments/0247-second-regression-check.md), [0266](../experiments/0266-decrypting-in-the-tool.md)), and in [0460](../experiments/0460-third-regression-check.md) for 1,259 of the 1,260 documents checked, 875,522 objects in all, including the files the writing experiments produced. The exception was a file written without one record's header references, which Pages opened normally while 25 of its 571 objects couldn't be reached from the headers. This is a property of the apps' output, not a rule Pages enforces: a reader that must handle other writers' files should not treat an unreachable object as an error. A document with a chart also has `Index/ObjectContainer.iwa`, whose object 61 (type 11008) is a fourth root, listing chart styles ([0067](../experiments/0067-chart.md)).

Object 1, the document root, has a different type and layout in each app (type 10000 in Pages, type 1 in Keynote and in Numbers, and those two differ). Each embeds the same block of document properties as one large message (Pages field 15, Keynote field 3, Numbers field 8), holding the locale (field 1 starts with it, field 3 is the language) and the template path (field 9, such as `Application/Blank/ISO`). *Likely* ([0027](../experiments/0027-document-roots.md))

## Password protection

A document with a password has two extra files at the top of the package, `.iwph` and `.iwpv2`, and no previews. This holds in all three apps. *Confirmed* ([0179](../experiments/0179-password.md), [0180](../experiments/0180-password-in-other-apps.md))

- `.iwph` holds the password hint as plain text.
- `.iwpv2` is 104 bytes: two 16-bit values (2 and 1, meaning *unknown*), a 32-bit iteration count (100,000), a 16-byte salt, a 16-byte IV, then 64 encrypted bytes. Decrypted, those are 32 random bytes followed by their SHA-256, which checks the password.

The key is PBKDF2-HMAC-SHA1 of the password (as UTF-8), using that salt and iteration count, 16 bytes long. Every `.iwa` part, every data file and `BuildVersionHistory.plist` is encrypted with it, using AES-128-CBC with PKCS #7 padding. `DocumentIdentifier` and `Properties.plist` are not encrypted. An encrypted part is laid out as 16 bytes of unknown meaning, the IV, the ciphertext, and 20 bytes of unknown meaning, probably an integrity check. Decrypted, a part is the same as in an unprotected document. The salt is new on every save. *Confirmed* ([0179](../experiments/0179-password.md), [0180](../experiments/0180-password-in-other-apps.md)); that the password is UTF-8 is *likely*. `iwork-probe --password` decrypts documents this way; all six protected samples then frame and are fully reachable ([0266](../experiments/0266-decrypting-in-the-tool.md)).

## View state

`ViewState.iwa` holds how the document was last shown, which a reader can ignore. Its type-10133 record has the zoom as a scale factor in field 15 (1.25 for 125%), in field 33 whether two pages are shown side by side, and in field 28 whether change tracking is paused ([0270](../experiments/0270-paused-tracking.md)). *Likely* ([0241](../experiments/0241-zoom.md), [0242](../experiments/0242-two-page-view.md), [0270](../experiments/0270-paused-tracking.md)). [release: 16.0 and 14.5] The 16.0 apps add a field to each app's view-state record in every document: field 49 to Pages' type 10133, fields 34 and 35 to Numbers' type 12026, and field 43 to Keynote's type 3 and field 13 to its type 23 ([0469](../experiments/0469-the-16-0-apps.md)). 14.5 writes them too when it saves a document it opened, but not in a new one, and no 15.4 sample has them ([0476](../experiments/0476-resaving-every-sample.md)). What they hold is *unknown*.

## IDs and save-to-save changes

Saving the same content twice can change these, and nothing else in the `.iwa` parts. *Likely* ([0001](../experiments/0001-empty-document.md), [0002](../experiments/0002-one-word.md))

- The UUIDs in `DocumentIdentifier`, `Properties.plist` and `Metadata.iwa` record 2.
- A creation time stored as text in the `Document.iwa` record of type 10012, and a time in `CalculationEngine` record type 4000.
- 128-bit-looking values in `CalculationEngine` records.
- The IDs of objects made at save time, and every reference to them. They changed between the two documents in 0001 but not between the two in 0002. Objects that come from the template keep their IDs.
- The order of entries in one list in `Metadata.iwa` record 2.

When a document is saved again, existing objects keep their IDs and newly made ones (such as the view state) get new ones. Saving under a new name gives a new document UUID. *Likely* ([0139](../experiments/0139-resave.md), [0140](../experiments/0140-edit-and-save.md))

Saving a document again also writes out what the app keeps of it, in every release tried (14.5 and 16.0, and 15.4 where its samples show it). Opened and saved again, the 1,211 samples changed in these ways and no others ([0476](../experiments/0476-resaving-every-sample.md)):

- The calculation engine's root gets the locale in fields 5 and 16 ([numbers.md](numbers.md#the-calculation-engine)), and the slide nodes of some Keynote presentations get field 20 ([keynote.md](keynote.md)).
- Fields the app doesn't keep are dropped, such as fields a writer added to cell styles (type 6001) or formula owners (type 4008).
- Data files get the app's own names, and those nothing refers to are left out ([0435](../experiments/0435-writing-an-unused-data-file.md)).
- `isMultiPage` in `Properties.plist` is set from the document: true when a Pages document has more than one page, false when a presentation or spreadsheet has one slide or sheet left.
- Records the app makes as needed, such as section records (types 3047 and 3006) and view-state records, are counted again.

A document that comes back from the app without these changes has kept nothing a writer added that the app doesn't know. *Likely*
