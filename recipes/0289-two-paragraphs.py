"""Experiment 0289: write a two-paragraph body text with the writer of experiment 0287.

Usage: python3 -I recipes/0289-two-paragraphs.py IN OUT_WITH_RUN OUT_WITHOUT_RUN
IN is a new Pages document whose body (record 1732539) is one paragraph. Both outputs get the text
"One\nTwo". OUT_WITH_RUN also gets a second paragraph-run entry (field 5) at position 4, as Pages
writes it; OUT_WITHOUT_RUN keeps the single entry at 0.
"""
import importlib.util
import os
import sys
import zipfile

spec = importlib.util.spec_from_file_location("writer", os.path.join(os.path.dirname(__file__), "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)

BODY = 1732539


def edit(recs, add_run):
    for header, payloads in recs:
        if w.record_id(header) != BODY:
            continue
        fields = []
        for f, wire, v in w.parse_message(payloads[0]):
            if f == 3:
                v = "One\nTwo".encode("utf-8")
            if f == 5 and add_run:
                # One more entry: { 1: 4 }, with no style, as Pages writes a second paragraph.
                v = v + w.serialize_message([(1, 2, w.serialize_message([(1, 0, w.write_varint(4))]))])
            fields.append((f, wire, v))
        payloads[0] = w.serialize_message(fields)


def write(src, dst, add_run):
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            if info.filename.startswith("preview"):
                continue
            data = zin.read(info)
            if info.filename == "Index/Document.iwa":
                recs = w.records(w.iwa_decode(data))
                edit(recs, add_run)
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)


write(sys.argv[1], sys.argv[2], True)
write(sys.argv[1], sys.argv[3], False)
