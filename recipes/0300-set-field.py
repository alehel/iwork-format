"""Experiment 0300: set top-level varint fields in every record of one type.

Usage: python3 -I recipes/0300-set-field.py IN OUT TYPE FIELD=VALUE [FIELD=VALUE ...]

Replaces (or adds) each FIELD as a varint VALUE in the payload of every record of TYPE, keeping
the fields in number order, and re-encodes everything else unchanged with the writer of
experiment 0287. Prints each changed record's ID and the fields' old values.
"""
import importlib.util
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("w", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


def record_type(header):
    info = {f: v for f, _, v in w.parse_message({f: v for f, _, v in header}[2])}
    return w.read_varint(info[1], 0)[0]


def main(src, dst, kind, settings):
    kind = int(kind)
    values = {int(k): int(v) for k, v in (s.split("=") for s in settings)}
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            data = zin.read(info)
            if info.filename.endswith(".iwa"):
                recs = w.records(w.iwa_decode(data))
                for header, payloads in recs:
                    if record_type(header) != kind:
                        continue
                    fields = w.parse_message(payloads[0])
                    old = {f: w.read_varint(v, 0)[0] for f, t, v in fields if f in values and t == 0}
                    kept = [(f, t, v) for f, t, v in fields if f not in values]
                    kept += [(f, 0, w.write_varint(v)) for f, v in values.items()]
                    payloads[0] = w.serialize_message(sorted(kept, key=lambda x: x[0]))
                    print(f"{info.filename} record {w.record_id(header)}: was {old or 'absent'}, now {values}")
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:])
