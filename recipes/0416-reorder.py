"""Experiments 0416 onward: reorder or drop the entries of a repeated top-level field of one record.

Usage: python3 -I recipes/0416-reorder.py IN OUT RECORD_ID FIELD ORDER

ORDER lists the field's existing entries by position from 1, comma-separated, such as 2,1. Entries
left out are dropped. The reordered entries take the place of the first one; everything else is
re-encoded unchanged with the writer of experiment 0287.
"""
import importlib.util
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("w", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


def main(src, dst, record, field, order):
    record, field = int(record), int(field)
    order = [int(k) for k in order.split(",")]
    done = False
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            data = zin.read(info)
            if info.filename.endswith(".iwa"):
                recs = w.records(w.iwa_decode(data))
                for header, payloads in recs:
                    if w.record_id(header) != record:
                        continue
                    fs = w.parse_message(payloads[0])
                    entries = [x for x in fs if x[0] == field]
                    at = next(i for i, x in enumerate(fs) if x[0] == field)
                    rest = [x for x in fs if x[0] != field]
                    picked = [entries[k - 1] for k in order]
                    payloads[0] = w.serialize_message(rest[:at] + picked + rest[at:])
                    print(f"record {record} field {field}: {len(entries)} entries -> order {order}")
                    done = True
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)
    if not done:
        raise SystemExit(f"no record {record}")


if __name__ == "__main__":
    main(*sys.argv[1:6])
