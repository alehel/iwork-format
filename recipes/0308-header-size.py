"""Experiment 0308: change one row height or column width in a header storage bucket by writing.

Usage: python3 -I recipes/0308-header-size.py IN OUT BUCKET_ID INDEX SIZE

In the type-6006 record BUCKET_ID, the field-2 entry whose index (2.1) is INDEX gets SIZE, in
points, as its size (2.2, a float). Everything else is re-encoded unchanged with the writer of
experiment 0287.
"""
import importlib.util
import os
import struct
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("w", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


def main(src, dst, bucket, index, size):
    bucket, index, size = int(bucket), int(index), float(size)
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            data = zin.read(info)
            if info.filename.endswith(".iwa"):
                recs = w.records(w.iwa_decode(data))
                for header, payloads in recs:
                    if w.record_id(header) != bucket:
                        continue
                    out = []
                    for f, t, v in w.parse_message(payloads[0]):
                        if f == 2:
                            entry = w.parse_message(v)
                            if any(k == 1 and w.read_varint(x, 0)[0] == index for k, _, x in entry):
                                old = next(struct.unpack("<f", x)[0] for k, _, x in entry if k == 2)
                                v = w.serialize_message([(k, tt, struct.pack("<f", size) if k == 2 else x) for k, tt, x in entry])
                                print(f"bucket {bucket} index {index}: {old} -> {size}")
                        out.append((f, t, v))
                    payloads[0] = w.serialize_message(out)
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)


if __name__ == "__main__":
    main(*sys.argv[1:6])
