# 0199: Merge fields in a letter

**Status:** run

[0158](0158-essay-template.md) found one merge field (type 2036) in the Essay template, for the author's name. The Classic Letter template has many, for both sender and recipient. This experiment reads them, together with the tags AppleScript reports for each placeholder.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0158](0158-essay-template.md) |

## Recipe

```bash
mkdir -p samples/0199
osascript recipes/0199-pages-placeholder-tag.applescript "$PWD/samples/0199"
```

The recipe makes a document from `Application/23_Classic_Letter/ISO` (*Klassisk brev*), lists the `tag` of each of its `placeholder texts`, and saves it as `letter.pages`. Setting a tag fails with error −10000, so the recipe only reads them.

Pages fills the sender fields from the macOS user's contact card, so the sample holds personal details and shouldn't be shared.

## Observation

AppleScript reports 12 placeholders. Eight tags are contact properties: `TPMailMerge_FullNamePseudoProperty` (four times), `postalAddresses` (twice), `phoneNumbers` and `emailAddresses`. The other four tags are the placeholder's own prompt text, such as the greeting `Kjære`.

`Document.iwa` holds eight type-2036 records and four type-2031 records, matching those 12. A type-2036 record:

| Field | Holds | Values seen |
| --- | --- | --- |
| 1 | `{ 1: UUID, 2: 1 }` | |
| 2 | The contact property | `TPMailMerge_FullNamePseudoProperty`, `postalAddresses`, `phoneNumbers`, `emailAddresses` |
| 3 | How to format it, for addresses | `TPMailMerge_PostalAddressMultiLinePseudoKey` |
| 4 | Which of the contact's values, by label | `_$!<Home>!$_`, `_$!<Work>!$_`, `_$!<Mobile>!$_` |
| 5 | Whose contact | 0 for the four fields in the sender block and the signature, 1 for the recipient's name and address and the name after the greeting |
| 6 | | 0 |
| 8 | A second UUID | |
| 11 | | 1 |

A type-2031 placeholder holds only `{ 1: { 1: UUID }, 2: 1 }`. Its prompt is the text its run covers in the body.

## Conclusion

A merge field names a property of a contact, as in the macOS Contacts framework: the property key in field 2, the label of the value in field 4 (in Contacts' `_$!<…>!$_` form), and a formatting key in field 3 where needed. Field 5 says whose contact it draws from: 0 the sender (the document's author) and 1 the recipient. The text the field shows now is in the body, so a reader can show the letter as it stands without resolving any contact.

A placeholder (type 2031) carries no text of its own. AppleScript's `tag` reports a merge field's property key, or a plain placeholder's prompt text.

## Confidence

*Likely*: merge field fields 2, 3, 4 and 5 as described.

*Unknown*: fields 6, 8 and 11 of type 2036, and field 2 of type 2031.
