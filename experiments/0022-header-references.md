# 0022: References in record headers

**Status:** run

[0020](0020-a-table.md) noticed that the header of a table record repeats field 2.4, and that a field inside each entry reads as object IDs. [Container](../spec/container.md) also lists header fields 2.4, 2.5 and 2.6 as unknown. This experiment checks, across every record of several documents, whether those fields list the objects a record's payload refers to. It saves no new documents; it reads the samples of earlier experiments.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Documents | `samples/0001/empty-a.pages`, `samples/0004/large.pages`, `samples/0019/left-right.pages`, `samples/0021/cells.pages` |

## Recipe

`iwork-probe` gained a `refs` command for this. It prints, for each record, the IDs packed in header field 2.5 and in field 4 of each header field 2.4 entry:

```bash
cargo run --release -- refs samples/0004/large.pages Index/Document.iwa
```

Two checks were then made with throwaway scripts over the `iwork-probe` output:

1. **Header against payload.** For every record, collect the payload's references, meaning every message whose only field is `1: varint N`, where N is the ID of a record in the document and at least 1000. The lower bound avoids small numbers that are values, not IDs. Then compare them with the IDs the header lists, grouped by the type of the record and the field path that holds the reference.
2. **Reachability.** Start at object 1 and follow only header-listed IDs. Count which objects are reached.

## Observation

The body record from 0004, as `refs` shows it:

```
   1732539    2001  1731511 1731481 1732647 1732607 1732296
```

These are the paragraph style, list style, character style, the type-2024 object and the section: the targets of its run tables (fields 5, 7, 8, 12 and 17). The stylesheet, which field 2 names, isn't listed.

### Header against payload

| Document | Header IDs that the payload doesn't refer to | Field paths whose references are always listed | Never listed | Mixed |
| --- | --- | --- | --- | --- |
| `0004/large` | 0 | 112 | 19 | 1 |
| `0019/left-right` | 0 | 110 | 20 | 1 |
| `0021/cells` | 0 | 194 | 25 | 1 |

The field paths never listed include:

- field 1.5 of every style type (2021, 2022, 2023, 2024, 3016, 5022–5030, 6003, 6004 …), which points at the stylesheet
- field 2 of the text record (2001), which also points at the stylesheet
- field 1.2 of the table's drawable (6000), which points at the text it sits in

The one mixed path is field 1 of the stylesheet (type 401).

### Reachability

| Document | Objects | Reached from 1 | Not reached | Reached from 1, 2 and 71 |
| --- | --- | --- | --- | --- |
| `0001/empty-a` | 571 | 564 | 7 | 571 |
| `0004/large` | 572 | 565 | 7 | — |
| `0019/left-right` | 573 | 566 | 7 | — |
| `0021/cells` | 634 | 627 | 7 | 634 |

The 7 not reached from 1 are always:

- objects 2 (type 11006) and 1732655 (type 11015), plus four objects of type 11014, in `Metadata.iwa`
- object 71 (type 11011), in `DocumentMetadata.iwa`

No header-listed ID was missing from any document.

## Conclusion

A record's header lists the objects its payload refers to, in field 2.5 and in field 4 of the entries of field 2.4, as packed varints. It lists references that lead down the object tree. It doesn't list references that lead back up to an owner or to the shared stylesheet. Whether a reference is listed depends on the field that holds it, not on the value. The entries of field 2.4 group references by the field that holds them. Their field 1 is probably a field path.

So a reader can find every object in a document without understanding any payload. It starts at the three roots, object 1 (`Document.iwa`), object 2 (`Metadata.iwa`) and object 71 (`DocumentMetadata.iwa`), and follows the IDs in the headers. The header lists alone also say which objects a record depends on, which helps when deciding what to decode first.

## Confidence

*Confirmed*: header IDs are always references found in the payload. This holds in four documents from different experiments, with no exception.

*Likely*:

- Upward references aren't listed.
- Every object is reachable from 1, 2 and 71.

*Unknown*:

- What fields 2.4.1, 2.4.2 and 2.4.3 mean. Field 2.4.1 is probably a field path.
- Header field 2.6.
