"""Experiment 0292: compare Keynote samples made with Basic White and with the test theme.

Usage: python3 -I recipes/0292-compare-themes.py samples samples/theme

For every presentation under the second folder that has a namesake under the first, it checks:
  - framing: every .iwa part decodes into chunks and records (spec/container.md);
  - reachability: every object is reached from roots 1, 2, 71 and 61 through the IDs in record
    headers (fields 2.5 and 2.4.4);
  - the record types each document holds, as counts, compared between the two themes;
  - that Data/ holds only the test theme's files, the project's own media and Keynote's
    thumbnails, and none of Basic White's photos.
Only the standard library and the writer of experiment 0287 are used.
"""
import collections
import importlib.util
import os
import re
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("w", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)

ROOTS = {1, 2, 71, 61}
OURS = re.compile(r"^(photo-[a-f](-small)?|background|alpha|small|red-8x4|tone|clip|posterImage|mt-[0-9A-F-]+|st-[0-9A-F-]+)-\d+\.\w+$")


def packed(b):
    out, i = [], 0
    while i < len(b):
        v, i = w.read_varint(b, i)
        out.append(v)
    return out


def analyse(path):
    """Types counted, unreached object count, and media names that aren't ours."""
    z = zipfile.ZipFile(path)
    objects, refs, types = {}, collections.defaultdict(set), collections.Counter()
    for name in z.namelist():
        if not name.endswith(".iwa"):
            continue
        for header, _ in w.records(w.iwa_decode(z.read(name))):
            oid = w.record_id(header)
            for f, _, v in header:
                if f != 2:
                    continue
                info = w.parse_message(v)
                for ff, _, vv in info:
                    if ff == 1:
                        types[w.read_varint(vv, 0)[0]] += 1
                    elif ff == 5:
                        refs[oid].update(packed(vv))
                    elif ff == 4:
                        for f4, _, v4 in w.parse_message(vv):
                            if f4 == 4:
                                refs[oid].update(packed(v4))
            objects[oid] = name
    seen, todo = set(), [r for r in ROOTS if r in objects]
    while todo:
        o = todo.pop()
        if o in seen:
            continue
        seen.add(o)
        todo.extend(r for r in refs.get(o, ()) if r in objects and r not in seen)
    foreign = [n[5:] for n in z.namelist() if n.startswith("Data/") and not OURS.match(n[5:])]
    return types, len(objects) - len(seen), len(objects), foreign


def main(old_root, new_root):
    rows, problems = 0, 0
    for dirpath, dirs, files in sorted(os.walk(new_root)):
        packages = [d for d in dirs if d.endswith('.key')]
        dirs[:] = [d for d in dirs if not d.endswith('.key')]
        for f in sorted(files + packages):
            if not f.endswith(".key"):
                continue
            new = os.path.join(dirpath, f)
            old = os.path.join(old_root, os.path.relpath(new, new_root))
            if os.path.isdir(new) or os.path.isdir(old):
                print(f"{os.path.relpath(new, new_root)}: a folder package, not compared")
                continue
            if ".iwpv2" in zipfile.ZipFile(new).namelist():
                print(f"{os.path.relpath(new, new_root)}: password-protected, not compared")
                continue
            t_new, unreached, total, foreign = analyse(new)
            line = f"{os.path.relpath(new, new_root)}: {total} objects"
            notes = []
            if unreached:
                notes.append(f"{unreached} unreached")
            if foreign:
                notes.append("foreign media: " + ", ".join(foreign))
            if os.path.exists(old):
                t_old, _, total_old, _ = analyse(old)
                diff = {k: t_new[k] - t_old[k] for k in set(t_new) | set(t_old) if t_new[k] != t_old[k]}
                if diff:
                    notes.append("types differ: " + ", ".join(f"{k} {d:+d}" for k, d in sorted(diff.items())))
            else:
                notes.append("no original")
            rows += 1
            problems += bool(notes)
            print(line + (" — " + "; ".join(notes) if notes else " — same types, all reached, media ours"))
    print(f"{rows} presentations, {problems} with notes")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
