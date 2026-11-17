"""Experiments 0412 onward: remove top-level fields from one record's payload.

Usage: python3 -I recipes/0412-drop-field.py IN OUT RECORD_ID FIELD [FIELD ...]

Every occurrence of each FIELD is removed from the record's first payload. Everything else is
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


def main(src, dst, record, *fields):
    record, fields = int(record), {int(f) for f in fields}
    done = False
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            data = zin.read(info)
            if info.filename.endswith(".iwa"):
                recs = w.records(w.iwa_decode(data))
                for header, payloads in recs:
                    if w.record_id(header) == record:
                        kept = [x for x in w.parse_message(payloads[0]) if x[0] not in fields]
                        payloads[0] = w.serialize_message(kept)
                        print(f"record {record}: removed fields {sorted(fields)}")
                        done = True
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)
    if not done:
        raise SystemExit(f"no record {record}")


if __name__ == "__main__":
    main(*sys.argv[1:])
