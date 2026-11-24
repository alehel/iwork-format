"""Experiment 0467: open Keynote presentations in the installed Keynote and check what it reads.

Usage: python3 -I recipes/0467-open-keynote.py SAMPLES_DIR [SKIP,SKIP,...] [PROBE]

Opens every .key file under SAMPLES_DIR/NNNN (and SAMPLES_DIR/theme), leaving out the experiments
named in SKIP, one at a time, with recipes/0372-in-app.sh. Keynote is asked for the number of
slides and, for each slide, its title (when the title is showing) and its presenter notes. Each
title and note that isn't empty must equal the text of one text record in the file's slide parts
(Index/Slide*.iwa, not TemplateSlide), as `iwork-probe text` prints it. Both sides leave out white
space, control and format characters (such as soft hyphens) and U+FFFC. The number of slides is
compared with the number of slide nodes the presentation lists in its field 3.2, read with the IWA
reader of experiment 0287. Prints one line per document, OK, DIFFERS or FAILED, and a total. Stops
after three failures in a row. Only the standard library is used.
"""
import glob
import importlib.util
import os
import subprocess
import sys
import unicodedata
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
HELPER = os.path.join(HERE, "0372-in-app.sh")
spec = importlib.util.spec_from_file_location("w", os.path.join(HERE, "0287-iwa-writer.py"))
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)

SEP = "\x1e"
SCRIPT = f"""set sep to (ASCII character 30)
set out to (count of slides of d) as text
repeat with s in slides of d
  set t to ""
  try
    if title showing of s then set t to object text of default title item of s
  end try
  set n to ""
  try
    set n to presenter notes of s
  end try
  set out to out & sep & t & sep & n
end repeat
return out"""


def norm(text):
    for marker in ("[object]", "[page break]", "[section break]", "[column break]", "[line break]", "[footnote]"):
        text = text.replace(marker, "")
    return "".join(c for c in text if not c.isspace() and c != "￼"
                   and unicodedata.category(c) not in ("Cc", "Cf"))


def file_texts(probe, path):
    out = subprocess.run([probe, "text", path], capture_output=True, text=True).stdout
    texts, cur, keep = set(), [], False
    for line in out.splitlines() + ["== end"]:
        if line.startswith("== "):
            if keep:
                texts.add(norm("\n".join(cur)))
            keep, cur = line.startswith("== Index/Slide"), []
        else:
            cur.append(line)
    return texts


def slide_nodes(path):
    """The number of slide nodes listed in field 3.2 of the presentation (type 2)."""
    z = zipfile.ZipFile(path) if os.path.isfile(path) else None
    if z is None:
        z = zipfile.ZipFile(os.path.join(path, "Index.zip"))
    for name in z.namelist():
        if name.rsplit("/", 1)[-1].startswith("Document") and name.endswith(".iwa"):
            for header, payloads in w.records(w.iwa_decode(z.read(name))):
                info = next(v for f, _, v in header if f == 2)
                kind = w.read_varint(next(v for f, _, v in w.parse_message(info) if f == 1), 0)[0]
                if kind == 2:
                    for f, _, v in w.parse_message(payloads[0]):
                        if f == 3:
                            return sum(1 for f2, _, _ in w.parse_message(v) if f2 == 2)
    return None


def main(samples, skip="", probe="target/release/iwork-probe"):
    skip = set(filter(None, skip.split(",")))
    docs = []
    for d in sorted(glob.glob(os.path.join(samples, "*"))):
        if os.path.basename(d) not in skip:
            docs += sorted(glob.glob(os.path.join(d, "*.key")))
    counts = {"OK": 0, "DIFFERS": 0, "FAILED": 0}
    in_a_row = 0
    for d in docs:
        rel = os.path.relpath(d, samples)
        try:
            r = subprocess.run(["sh", HELPER, "Keynote", d, SCRIPT], capture_output=True, text=True, timeout=120)
            out, err, code = r.stdout.rstrip("\n"), r.stderr.strip(), r.returncode
        except subprocess.TimeoutExpired:
            out, err, code = "", "timed out", 1
        if code != 0 or not out or out.startswith("error:"):
            counts["FAILED"] += 1
            in_a_row += 1
            print(f"FAILED {rel}: {(out or err.splitlines()[-1] if (out or err) else '')[:150]}", flush=True)
            if in_a_row >= 3:
                print("stopping: three failures in a row", flush=True)
                break
            continue
        in_a_row = 0
        parts = out.split(SEP)
        n = int(parts[0])
        want_n = slide_nodes(d)
        texts = file_texts(probe, d)
        problems = []
        if n != want_n:
            problems.append(f"{n} slides, file lists {want_n}")
        for i in range(n):
            for kind, got in (("title", parts[1 + 2 * i]), ("notes", parts[2 + 2 * i])):
                g = norm(got)
                if g and g != "missingvalue" and g not in texts:
                    problems.append(f"slide {i + 1} {kind} {got[:40]!r} not in file")
        status = "DIFFERS" if problems else "OK"
        counts[status] += 1
        print(f"{status} {rel}: {n} slides" + ("" if not problems else "; " + "; ".join(problems[:3])), flush=True)
    print(counts, flush=True)


if __name__ == "__main__":
    main(*sys.argv[1:4])
