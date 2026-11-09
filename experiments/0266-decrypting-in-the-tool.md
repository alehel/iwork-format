# 0266: Decrypting in the tool

**Status:** run

[0179](0179-password.md) and [0180](0180-password-in-other-apps.md) worked out how password-protected documents are encrypted, using throwaway scripts. [0247](0247-second-regression-check.md) had to leave the six protected samples out of its checks, because `iwork-probe` couldn't read them. This experiment builds that reading into `iwork-probe` and runs the 0247 checks on those six documents.

## Setup

| | |
| --- | --- |
| Tool | `iwork-probe` with a new `crypt` module and a `--password` option |
| Date | 2026-11-09 |
| Baseline | Experiment [0247](0247-second-regression-check.md) |

## Recipe

The tool now:

- Recognises a protected document by its `.iwpv2` file.
- Derives the key from `--password` as described in [container.md](../spec/container.md#password-protection), and checks it against `.iwpv2`'s encrypted SHA-256.
- Decrypts every part except `.iwph`, `.iwpv2`, `Properties.plist` and `DocumentIdentifier` as it reads them.

The cryptography comes from the RustCrypto crates `aes`, `cbc`, `pbkdf2`, `sha1` and `sha2`. Unit tests encrypt a part and a header the way 0179 found Pages does, then decrypt them.

The three checks of 0178 (framing, reachability from roots 1, 2, 71 and 61, and text extraction) were then run on the six protected samples, each with its password:

```bash
iwork-probe records samples/0179/locked.pages Index/Document.iwa --password pw1234
iwork-probe text samples/0180/accent.pages --password påss
```

## Observation

| Document | Parts | Framing errors | Objects reached | Text |
| --- | --- | --- | --- | --- |
| `0179/locked.pages` | 7 | 0 | 571 of 571 | ok |
| `0179/locked2.pages` | 7 | 0 | 571 of 571 | ok |
| `0180/accent.pages` | 7 | 0 | 571 of 571 | ok |
| `0180/image.pages` | 7 | 0 | 574 of 574 | ok |
| `0180/locked.key` | 25 | 0 | 962 of 962 | ok |
| `0180/locked.numbers` | 37 | 0 | 626 of 626 | ok |

The only missing reference is root 61, which documents without a chart don't have. Without `--password`, the tool reports that the document is password-protected and shows its hint (`test`). With a wrong password, it reports "wrong password" and reads nothing.

## Conclusion

The reading of 0179 and 0180 is complete enough to rely on. Every part of every protected sample decrypts with valid padding and then frames, and all 3,875 objects are reachable, as in unprotected documents. With 0247, all 353 samples now pass the three checks. The password check in `.iwpv2` works as a reader needs it to: a wrong password is caught before any part is decrypted.

## Confidence

*Confirmed*, with 0179 and 0180: the encryption scheme, now applied by `iwork-probe` to all six protected samples.
