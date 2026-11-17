"""Experiment 0395: rename or replace a document's data file, with or without its Metadata entry.

Usage: python3 -I recipes/0395-data-file.py IN OUT DATA_ID [OPTION ...]

Options:
  --store NAME     rename the stored file Data/<old> to Data/NAME
  --list           with --store, also write NAME into the data entry's field 4
  --original NAME  write NAME into the data entry's field 3 (the original file name)
  --replace FILE   store FILE's bytes in place of the data file's (name and entry unchanged)

The data entry is the field 4 of Metadata.iwa record 2 whose field 1 is DATA_ID. Everything else
is re-encoded unchanged with the writer of experiment 0287.
"""
import importlib.util
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("w", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


def opt(args, name):
    return args[args.index(name) + 1] if name in args else None


def main(src, dst, data_id, *args):
    data_id = int(data_id)
    store, original, replace = opt(args, "--store"), opt(args, "--original"), opt(args, "--replace")
    with zipfile.ZipFile(src) as zin:
        recs = w.records(w.iwa_decode(zin.read("Index/Metadata.iwa")))
        stored = None
        for header, payloads in recs:
            if w.record_id(header) != 2:
                continue
            out = []
            for f, t, v in w.parse_message(payloads[0]):
                if f == 4:
                    fs = w.parse_message(v)
                    d = {k: x for k, _, x in fs}
                    if w.read_varint(d[1], 0)[0] == data_id:
                        stored = d[4].decode()
                        fs = [(k, tt, (store.encode() if k == 4 and store and "--list" in args else
                                       original.encode() if k == 3 and original else x)) for k, tt, x in fs]
                        v = w.serialize_message(fs)
                out.append((f, t, v))
            payloads[0] = w.serialize_message(out)
        if stored is None:
            raise SystemExit(f"no data entry {data_id}")
        metadata = w.iwa_encode(w.encode_records(recs))
        with zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
            for info in zin.infolist():
                name, data = info.filename, zin.read(info)
                if name == "Index/Metadata.iwa":
                    data = metadata
                if name == "Data/" + stored:
                    if replace:
                        data = open(replace, "rb").read()
                    if store:
                        name = "Data/" + store
                zout.writestr(zipfile.ZipInfo(name, date_time=info.date_time), data)
    print(f"data {data_id}: stored as {stored}; store={store} list={'--list' in args} original={original} replace={replace}")


if __name__ == "__main__":
    main(*sys.argv[1:])
