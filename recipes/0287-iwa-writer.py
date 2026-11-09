"""Experiments 0287 onward: rewrite an iWork document from what the spec says, to test the spec by writing.

Usage:
  python3 -I recipes/0287-iwa-writer.py IN OUT                      re-encode every .iwa part unchanged
  python3 -I recipes/0287-iwa-writer.py IN OUT --text ID NEW        also set the text (field 3) of record ID
  python3 -I recipes/0287-iwa-writer.py IN OUT --plain              same, and leave out the previews

Everything here follows spec/container.md: a part is chunks of [type 0][3-byte little-endian
length][raw Snappy block], each decoding to at most 65,536 bytes; the joined bytes are records of
[varint header length][header message][payloads], with each payload's length in header field 2.3.
The Snappy encoder writes literals only, which the public Snappy format allows. Only the standard
library is used.
"""
import sys
import zipfile


# --- Protocol Buffers wire format (public specification) ---------------------------------------

def read_varint(b, i):
    result = shift = 0
    while True:
        c = b[i]
        i += 1
        result |= (c & 0x7F) << shift
        shift += 7
        if c < 0x80:
            return result, i


def write_varint(n):
    out = bytearray()
    while True:
        byte = n & 0x7F
        n >>= 7
        if n:
            out.append(byte | 0x80)
        else:
            out.append(byte)
            return bytes(out)


def parse_message(b):
    """A message as a list of (field, wire type, raw value bytes), kept in order."""
    fields = []
    i = 0
    while i < len(b):
        key, j = read_varint(b, i)
        field, wire = key >> 3, key & 7
        if wire == 0:
            _, k = read_varint(b, j)
            value = b[j:k]
        elif wire == 1:
            k = j + 8
            value = b[j:k]
        elif wire == 2:
            length, j = read_varint(b, j)
            k = j + length
            value = b[j:k]
        elif wire == 5:
            k = j + 4
            value = b[j:k]
        else:
            raise ValueError(f"wire type {wire}")
        fields.append((field, wire, value))
        i = k
    return fields


def serialize_message(fields):
    out = bytearray()
    for field, wire, value in fields:
        out += write_varint(field << 3 | wire)
        if wire == 2:
            out += write_varint(len(value))
        out += value
    return bytes(out)


# --- Snappy (public format) ---------------------------------------------------------------------

def snappy_decode(b):
    n, i = read_varint(b, 0)
    out = bytearray()
    while i < len(b):
        tag = b[i]
        i += 1
        kind = tag & 3
        if kind == 0:
            length = tag >> 2
            if length >= 60:
                nbytes = length - 59
                length = int.from_bytes(b[i:i + nbytes], "little")
                i += nbytes
            length += 1
            out += b[i:i + length]
            i += length
        else:
            if kind == 1:
                length = ((tag >> 2) & 7) + 4
                offset = ((tag >> 5) << 8) | b[i]
                i += 1
            elif kind == 2:
                length = (tag >> 2) + 1
                offset = int.from_bytes(b[i:i + 2], "little")
                i += 2
            else:
                length = (tag >> 2) + 1
                offset = int.from_bytes(b[i:i + 4], "little")
                i += 4
            for _ in range(length):
                out.append(out[-offset])
    if len(out) != n:
        raise ValueError("snappy length mismatch")
    return bytes(out)


def snappy_encode_literals(data):
    """A raw Snappy block holding `data` as literal runs only."""
    out = bytearray(write_varint(len(data)))
    i = 0
    while i < len(data):
        piece = data[i:i + 65536]
        n = len(piece) - 1
        if n < 60:
            out.append(n << 2)
        elif n < 1 << 8:
            out += bytes([60 << 2]) + n.to_bytes(1, "little")
        elif n < 1 << 16:
            out += bytes([61 << 2]) + n.to_bytes(2, "little")
        else:
            out += bytes([62 << 2]) + n.to_bytes(3, "little")
        out += piece
        i += len(piece)
    return bytes(out)


# --- .iwa parts (spec/container.md) -------------------------------------------------------------

CHUNK = 65536


def iwa_decode(stored):
    out = bytearray()
    i = 0
    while i < len(stored):
        if stored[i] != 0:
            raise ValueError("unknown chunk type")
        length = int.from_bytes(stored[i + 1:i + 4], "little")
        out += snappy_decode(stored[i + 4:i + 4 + length])
        i += 4 + length
    return bytes(out)


def iwa_encode(raw):
    out = bytearray()
    for start in range(0, len(raw), CHUNK):
        block = snappy_encode_literals(raw[start:start + CHUNK])
        out += b"\x00" + len(block).to_bytes(3, "little") + block
    return bytes(out)


def records(raw):
    """Each record as [header fields, [payload bytes, ...]]."""
    out = []
    i = 0
    while i < len(raw):
        hlen, i = read_varint(raw, i)
        header = parse_message(raw[i:i + hlen])
        i += hlen
        payloads = []
        for field, _, value in header:
            if field == 2:
                info = parse_message(value)
                length = next(read_varint(v, 0)[0] for f, _, v in info if f == 3)
                payloads.append(raw[i:i + length])
                i += length
        out.append([header, payloads])
    return out


def record_id(header):
    return next(read_varint(v, 0)[0] for f, _, v in header if f == 1)


def encode_records(recs):
    out = bytearray()
    for header, payloads in recs:
        new_header = []
        p = 0
        for field, wire, value in header:
            if field == 2:
                info = [(f, w, write_varint(len(payloads[p])) if f == 3 else v) for f, w, v in parse_message(value)]
                value = serialize_message(info)
                p += 1
            new_header.append((field, wire, value))
        h = serialize_message(new_header)
        out += write_varint(len(h)) + h
        for payload in payloads:
            out += payload
    return bytes(out)


def set_text(recs, object_id, text):
    for header, payloads in recs:
        if record_id(header) == object_id:
            fields = parse_message(payloads[0])
            fields = [(f, w, text.encode("utf-8") if f == 3 else v) for f, w, v in fields]
            payloads[0] = serialize_message(fields)
            return True
    return False


def main(argv):
    src, dst = argv[0], argv[1]
    text_edit = None
    plain = "--plain" in argv
    if "--text" in argv:
        k = argv.index("--text")
        text_edit = (int(argv[k + 1]), argv[k + 2])
    edited = False
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            name = info.filename
            if plain and name.startswith("preview"):
                continue
            data = zin.read(info)
            if name.endswith(".iwa"):
                recs = records(iwa_decode(data))
                if text_edit and set_text(recs, *text_edit):
                    edited = True
                data = iwa_encode(encode_records(recs))
            zout.writestr(zipfile.ZipInfo(name, date_time=info.date_time), data)
    if text_edit and not edited:
        raise SystemExit(f"no record {text_edit[0]}")


if __name__ == "__main__":
    main(sys.argv[1:])
