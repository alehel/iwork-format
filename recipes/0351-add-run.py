"""Experiment 0351: add a run to a text's run table by writing it.

Usage: python3 -I recipes/0351-add-run.py IN OUT TEXT_ID FIELD POSITION STYLE_ID [POSITION STYLE_ID ...]

Replaces run table FIELD (such as 8, character styles) of text storage TEXT_ID with entries of
{1: POSITION, 2: {1: STYLE_ID}}, in the order given; STYLE_ID 0 writes an entry without a style,
which ends the previous one. Everything else is re-encoded unchanged with the writer of
experiment 0287.
"""
import importlib.util
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("w", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


def main(src, dst, text, field, pairs):
    text, field = int(text), int(field)
    entries = []
    for i in range(0, len(pairs), 2):
        pos, style = int(pairs[i]), int(pairs[i + 1])
        e = [(1, 0, w.write_varint(pos))]
        if style:
            e.append((2, 2, w.serialize_message([(1, 0, w.write_varint(style))])))
        entries.append((1, 2, w.serialize_message(e)))
    table = w.serialize_message(entries)
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            data = zin.read(info)
            if info.filename.endswith(".iwa"):
                recs = w.records(w.iwa_decode(data))
                for header, payloads in recs:
                    if w.record_id(header) == text:
                        fields = [(f, t, v) for f, t, v in w.parse_message(payloads[0]) if f != field]
                        fields.append((field, 2, table))
                        payloads[0] = w.serialize_message(sorted(fields, key=lambda x: x[0]))
                        print(f"text {text}: run table {field} = {pairs}")
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5:])
