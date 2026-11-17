# 0408: Writing a merge field's property

**Status:** run

A merge field is a type-2036 smart field whose field 2 names a property of a contact, such as `emailAddresses`; AppleScript lists merge fields among the `placeholder texts` and reports that key as their `tag` ([0199](0199-letter-merge-fields.md)). This experiment writes another key.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0199/letter.pages`, a letter from a template, with eight merge fields; record 2489890 is the sender's `emailAddresses` |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); read back with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) |

## Recipe

```bash
mkdir -p samples/0408
R=recipes/0302-set-path.py
F=samples/0199/letter.pages
O=samples/0408
cp $F $O/original.pages
python3 -I $R $F $O/email-to-phone.pages 2489890 2 string phoneNumbers
python3 -I $R $F $O/email-to-custom.pages 2489890 2 string someMadeUpKey
for f in original email-to-phone email-to-custom; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages 'set out to {}
repeat with p in placeholder texts of d
  set end of out to tag of p
end repeat
return out'
done
```

## Observation

The first four tags, which belong to the sender block, in order:

| File | Field 2 of 2489890 | Tags |
| --- | --- | --- |
| `original.pages` | `emailAddresses` | full name, `postalAddresses`, `phoneNumbers`, `emailAddresses` |
| `email-to-phone.pages` | `phoneNumbers` | full name, `postalAddresses`, `phoneNumbers`, `phoneNumbers` |
| `email-to-custom.pages` | `someMadeUpKey` | full name, `postalAddresses`, `phoneNumbers`, `someMadeUpKey` |

(The full name's tag is `TPMailMerge_FullNamePseudoProperty`.) The other tags, and the text of the letter, were the same in all three.

## Conclusion

Field 2 of a merge field is the property key Pages reports and merges by, and Pages keeps a key it doesn't know rather than rejecting the field. Which values a key can take is up to the Contacts framework; a reader only needs to show the field's current text, which is in the body.

## Confidence

*Confirmed*: field 2 of type 2036 as the merge field's property key, by writing it.
