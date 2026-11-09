# 0189: A web link

**Status:** run

AppleScript can't add links, so this experiment adds one through the Pages menus, to see where a link is stored.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0179/plain.pages`, the body text `one` |

## Recipe

1. Make a document with the body text `one`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "one"'
   ```
2. Double-click `one`, then choose Format → Add Link → Webpage (*Format → Legg til lenke → Nettside*).
3. Save it as `samples/0189/link.pages`, without changing the link.

Pages fills in its own default address, `http://www.apple.com/no`, and underlines the word.

## Observation

`Document.iwa` gains one record, of type 2032:

```
1: { 1: "67599FAE-72B7-417E-A752-154797023373" }
2: "http://www.apple.com/no"
```

The body text (type 2001) gains two run tables, each with one entry at position 0:

- **Field 8, character styles:** 1731540, the stylesheet's type-2021 style named `Lenke`, with the identifier `character-style-hyperlink`.
- **Field 11, smart fields:** 1732708, the type-2032 record.

## Conclusion

A link is a smart field of type 2032, held in the same run table (field 11) as the placeholder, date and merge fields of [0158](0158-essay-template.md). Its field 2 is the address and field 1 a UUID. The run covers the linked text. The link's look comes separately, from the built-in character style `character-style-hyperlink`. A reader finds links by the type-2032 entries in field 11.

## Confidence

*Likely*: a link is a type-2032 smart field with the address in field 2, run over the linked text in field 11.

*Unknown*: what the UUID in field 1 is used for.
