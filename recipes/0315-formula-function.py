"""Experiment 0315: change the function a formula calls, by writing its node.

Usage: python3 -I recipes/0315-formula-function.py IN OUT LIST_ID OLD_FUNCTION NEW_FUNCTION

In the formula list LIST_ID (type 6005), every function-call node (node type 16, field 1) whose
function (field 2) is OLD_FUNCTION gets NEW_FUNCTION. Nodes are entries 3.5.1.1 of the list, as
in spec/text.md. Everything else is re-encoded unchanged with the writer of experiment 0287.
"""
import importlib.util
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("w", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


def rewrite(b, path, fn):
    """Apply fn to every submessage reached by following the repeated field numbers in path."""
    out = []
    for f, t, v in w.parse_message(b):
        if f == path[0] and t == 2:
            v = fn(v) if len(path) == 1 else rewrite(v, path[1:], fn)
        out.append((f, t, v))
    return w.serialize_message(out)


def main(src, dst, lst, old, new):
    lst, old, new = int(lst), int(old), int(new)
    changed = []

    def node(v):
        fields = w.parse_message(v)
        d = {f: x for f, _, x in fields}
        if 1 in d and w.read_varint(d[1], 0)[0] == 16 and 2 in d and w.read_varint(d[2], 0)[0] == old:
            changed.append(1)
            return w.serialize_message([(f, t, w.write_varint(new) if f == 2 else x) for f, t, x in fields])
        return v

    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as zout:
        for info in zin.infolist():
            data = zin.read(info)
            if info.filename.endswith(".iwa"):
                recs = w.records(w.iwa_decode(data))
                for header, payloads in recs:
                    if w.record_id(header) == lst:
                        payloads[0] = rewrite(payloads[0], [3, 5, 1, 1], node)
                data = w.iwa_encode(w.encode_records(recs))
            zout.writestr(zipfile.ZipInfo(info.filename, date_time=info.date_time), data)
    print(f"list {lst}: {len(changed)} call(s) of function {old} -> {new}")


if __name__ == "__main__":
    main(*sys.argv[1:6])
