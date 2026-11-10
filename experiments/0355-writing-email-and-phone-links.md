# 0355: Writing email and phone links

**Status:** run

[0190](0190-email-and-phone-links.md) found that email and phone links are type-2032 links like web links, with `mailto:` and `tel:` addresses in field 2. [0354](0354-writing-a-link.md) confirmed a web link's address by writing it and reading the exported PDF's link annotations. This experiment does the same for the other two kinds.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0190/email.pages` (link 1732708, `mailto:no_reply@apple.com`) and `samples/0190/phone.pages` (link 1732700, `tel:%2012%2034%2056%2078`) |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0355
R=recipes/0302-set-path.py
python3 -I $R samples/0190/email.pages samples/0355/email.pages 1732708 2 string "mailto:someone@example.org"
python3 -I $R samples/0190/phone.pages samples/0355/phone.pages 1732700 2 string "tel:+4712345678"
```

Pages opened each file on its own and exported it as PDF; PDFKit listed the links.

## Observation

| File | Link annotation in the PDF |
| --- | --- |
| `email.pages` | `mailto:someone@example.org` |
| `phone.pages` | `tel:+4712345678` |

## Conclusion

Email and phone links are written like web links: the URL in field 2, with the `mailto:` or `tel:` scheme deciding the kind. A phone number can be written without the percent-encoded spaces Pages uses.

## Confidence

*Confirmed*: email and phone link addresses, by writing them.
