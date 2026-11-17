"""Experiment 0378: rewrite a Keynote presentation's show order (field 3.2 of its type-2 record).

Usage: python3 -I recipes/0378-slide-order.py IN OUT RECORD_ID ORDER

ORDER lists the existing 3.2 entries by position from 1, comma-separated, such as 3,1,2. Entries
left out are dropped from the list; nothing else is removed. Everything else is re-encoded unchanged
by the writer of experiment 0287.
"""
import importlib.util
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("w", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


def main(src, dst, record, order):
    record = int(record)
    order = [int(k) for k in order.split(",")]

    def reorder(field3):
        fs = w.parse_message(field3)
        entries = [x for x in fs if x[0] == 2]
        rest = [x for x in fs if x[0] != 2]
        print("was:", [w.read_varint(w.parse_message(v)[0][2], 0)[0] for _, _, v in entries])
        picked = [entries[k - 1] for k in order]
        print("now:", [w.read_varint(w.parse_message(v)[0][2], 0)[0] for _, _, v in picked])
        return w.serialize_message(rest + picked)

    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            data = zin.read(info)
            if info.filename.endswith(".iwa"):
                recs = w.records(w.iwa_decode(data))
                for header, payloads in recs:
                    if w.record_id(header) == record:
                        payloads[0] = w.serialize_message(
                            [(f, t, reorder(v) if f == 3 else v) for f, t, v in w.parse_message(payloads[0])])
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)


if __name__ == "__main__":
    main(*sys.argv[1:5])
