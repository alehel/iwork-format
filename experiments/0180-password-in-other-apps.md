# 0180: A password in Keynote and Numbers

**Status:** run

[0179](0179-password.md) found how Pages encrypts a document that has a password. This experiment tests the same reading on Keynote and Numbers documents, a password with a non-ASCII letter, and a document with an image.

## Setup

| | |
| --- | --- |
| Pages, Keynote, Numbers | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0179](0179-password.md) |

## Recipe

```bash
mkdir -p samples/0180
osascript recipes/0180-password-apps.applescript "$PWD/samples/0180" "$PWD/samples/0023/red-8x4.png"
```

The recipe saves:

- `locked.key` and `locked.numbers`: new documents with the password `pw1234`.
- `accent.pages`: the body text `one`, with the password `påss`.
- `image.pages`: the body text `one` and the 75-byte PNG from [0023](0023-an-image.md), with the password `pw1234`.

## Observation

All four documents have `.iwph` and `.iwpv2`, and no previews. Each `.iwpv2` starts with the same 8 bytes as in 0179.

Every file except `.iwph`, `.iwpv2`, `Properties.plist` and `DocumentIdentifier` decrypts with the reading from 0179: valid padding everywhere.

| Document | Files decrypted |
| --- | --- |
| `locked.key` | 49, including the theme's 23 images under `Data/` |
| `locked.numbers` | 38, including 31 parts under `Index/Tables/` |
| `image.pages` | 9, including `Data/data-24.png` |
| `accent.pages` | 8, with the password as UTF-8 |

The decrypted `Data/data-24.png` is byte for byte the original image: 132 bytes stored, 75 decrypted. Repacked, the decrypted documents read as normal:

- The Pages documents give the text `one`.
- Every decrypted Keynote and Numbers part frames as records: 962 in 25 parts and 626 in 37 parts. Walking references from object 1 leaves no dangling references. The only objects it doesn't reach are the `Metadata.iwa` and `DocumentMetadata.iwa` records known to hang from the other roots.

## Conclusion

The same encryption holds across all three apps. It covers embedded data files as well as `.iwa` parts. Passwords are encoded as UTF-8 before key derivation. A reader can decrypt every file other than the four left in the clear, then read the document as normal.

## Confidence

*Confirmed*, together with 0179: the key derivation, the cipher, the layout of `.iwpv2` and of an encrypted file, and which files are encrypted.

*Likely*: passwords are UTF-8. Only one non-ASCII password was tried, and it was typed in its composed (NFC) form.

*Unknown*: the first 16 and last 20 bytes of each encrypted file.
