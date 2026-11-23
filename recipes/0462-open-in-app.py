"""Experiment 0462: open sample documents in the installed apps and check what they read.

Usage: python3 -I recipes/0462-open-in-app.py SAMPLES_DIR FIRST LAST [PROBE]

Opens every .pages and .numbers file directly under SAMPLES_DIR/NNNN for NNNN from FIRST to LAST,
one at a time, with recipes/0372-in-app.sh. For Pages it asks for the body text and compares it
with the body text record (field 1 = 0) as `iwork-probe text` prints it, leaving out spaces, control
characters such as breaks and footnote marks, and U+FFFC on both sides (a document without a body
counts as empty); for Numbers it asks for
the number of sheets and the first table's name. Prints one line per document: OK, DIFFERS or
FAILED with the reason. Stops after three failures in a row, in case the app has stopped opening
documents. Only the standard library is used.
"""
import glob
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
HELPER = os.path.join(HERE, "0372-in-app.sh")


def probe_body(probe, path):
    out = subprocess.run([probe, "text", path], capture_output=True, text=True).stdout
    body, keep = [], False
    for line in out.splitlines():
        if line.startswith("== "):
            keep = "(field 1 = 0)" in line
            continue
        if keep:
            body.append(line)
    text = "\n".join(body)
    for marker in ("[object]", "[page break]", "[section break]", "[column break]", "[line break]", "[footnote]"):
        text = text.replace(marker, "")
    return "".join(text.split())


def main(samples, first, last, probe="target/release/iwork-probe"):
    docs = []
    for n in range(int(first), int(last) + 1):
        for ext in ("pages", "numbers"):
            docs += sorted(glob.glob(os.path.join(samples, f"{n:04d}", f"*.{ext}")))
    failures_in_a_row = 0
    counts = {"OK": 0, "DIFFERS": 0, "FAILED": 0}
    for d in docs:
        rel = os.path.relpath(d, samples)
        if d.endswith(".pages"):
            script = 'return "<<" & (body text of d) & ">>"'
            app = "Pages"
        else:
            script = "return {count of sheets of d, name of table 1 of sheet 1 of d}"
            app = "Numbers"
        try:
            r = subprocess.run(["sh", HELPER, app, d, script], capture_output=True, text=True, timeout=90)
            out, err = r.stdout.strip(), r.stderr.strip()
        except subprocess.TimeoutExpired:
            out, err = "", "timed out"
        if not out or out.startswith("error:") or r.returncode != 0:
            failures_in_a_row += 1
            counts["FAILED"] += 1
            print(f"FAILED {rel}: {(out or err)[:150]}", flush=True)
            if failures_in_a_row >= 3:
                print("stopping: three failures in a row", flush=True)
                break
            continue
        failures_in_a_row = 0
        if app == "Pages":
            want = probe_body(probe, d)
            got = out.removeprefix("<<").removesuffix(">>")
            got = "" if got == "missing value" else "".join(c for c in got if c >= " " and c != chr(0xFFFC))
            got = "".join(got.split())
            status = "OK" if got == want else "DIFFERS"
            counts[status] += 1
            print(f"{status} {rel}" + ("" if status == "OK" else f": app {got[:60]!r}, file {want[:60]!r}"), flush=True)
        else:
            counts["OK"] += 1
            print(f"OK {rel}: {out}", flush=True)
    print(counts, flush=True)


if __name__ == "__main__":
    main(*sys.argv[1:5])
