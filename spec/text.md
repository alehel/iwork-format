# 2. Text

Where a Pages document keeps its body text, and how the text is encoded. Every finding links to the experiments that support it, with a confidence level as defined in [CONTRIBUTING.md](../CONTRIBUTING.md#confidence). Records, object IDs and types are as described in [1. Container](container.md).

Observed with Pages 15.4 on macOS 26.5.2.

## The body text

The body text is in `Index/Document.iwa`, in field 3 of a record of type 2001. *Confirmed* ([0002](../experiments/0002-one-word.md), [0003](../experiments/0003-non-ascii-word.md))

- It is UTF-8, including characters outside the Basic Multilingual Plane, which take four bytes.
- It has no terminator or extra length prefix: the field's own length is the text's length in bytes.
- An empty body has no field 3 at all.

`Document.iwa` holds more than one type-2001 record: 19 in a new document. The body's record has field 1 set to 0, and none of the others has had a field 3 so far. *Likely* ([0003](../experiments/0003-non-ascii-word.md)). What the others are for is *unknown*.

The body's type-2001 record also refers to other objects by ID, as described in [0002](../experiments/0002-one-word.md): field 2 names an object of type 401 in `DocumentStylesheet.iwa`, and fields 5, 7, 12 and 17 each hold a list whose single entry pairs 0 with an object ID. Their meaning is *unknown*.

## Positions in the text

Positions and lengths in the text count UTF-16 code units, not UTF-8 bytes or code points. So a character outside the Basic Multilingual Plane counts as 2. *Likely* ([0003](../experiments/0003-non-ascii-word.md); seen only in `ViewState.iwa` so far.)
