# 0190: Email and phone links

**Status:** run

[0189](0189-web-link.md) found that a web link is a type-2032 smart field. Pages also offers email and phone number links. This experiment adds one of each, to see whether they use the same record.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0189](0189-web-link.md) |

## Recipe

As in 0189, but choosing Format → Add Link → Email (*E-post*) for `samples/0190/email.pages` and Format → Add Link → Phone Number (*Telefonnummer*) for `samples/0190/phone.pages`. Each link keeps the address Pages fills in.

## Observation

Each document gains one type-2032 record, with the same run tables as in 0189: field 8 sets the `Lenke` character style and field 11 points at the record, both from position 0.

| Document | Field 2 |
| --- | --- |
| `email.pages` | `mailto:no_reply@apple.com` |
| `phone.pages` | `tel:%2012%2034%2056%2078` |

Field 1 holds a new UUID each time.

## Conclusion

Web, email and phone links are all type-2032 smart fields. The kind of link is given only by the scheme of the address in field 2: `http:`, `mailto:` or `tel:`. The phone number is stored percent-encoded, with each space as `%20`, so a reader should decode the address before showing it.

## Confidence

*Confirmed*, with 0189: links are type-2032 smart fields with the address in field 2.

*Likely*: the kind of link is given by the address's scheme alone.
