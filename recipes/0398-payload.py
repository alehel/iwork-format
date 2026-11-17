"""Experiment 0398: drop or replace one payload of a record with several.

Usage: python3 -I recipes/0398-payload.py IN OUT RECORD_ID N (drop | HEX)

N counts the record's payloads from 1. `drop` removes the payload and its header field 2; HEX
replaces the payload's bytes (its length in 2.3 is rewritten). Everything else is re-encoded
unchanged with the writer of experiment 0287.
"""
import importlib.util
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("w", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


def main(src, dst, record, n, what):
    record, n = int(record), int(n)
    done = False
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            data = zin.read(info)
            if info.filename.endswith(".iwa"):
                recs = w.records(w.iwa_decode(data))
                for rec in recs:
                    header, payloads = rec
                    if w.record_id(header) != record or len(payloads) < n:
                        continue
                    print(f"record {record} payload {n}: {payloads[n - 1].hex()} -> {what}")
                    if what == "drop":
                        seen, new = 0, []
                        for f, t, v in header:
                            if f == 2:
                                seen += 1
                                if seen == n:
                                    continue
                            new.append((f, t, v))
                        rec[0] = new
                        del payloads[n - 1]
                    else:
                        payloads[n - 1] = bytes.fromhex(what)
                    done = True
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)
    if not done:
        raise SystemExit(f"no record {record} with {n} payloads")


if __name__ == "__main__":
    main(*sys.argv[1:6])
