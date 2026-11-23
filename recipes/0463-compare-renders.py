"""Experiment 0463: export documents again with the installed apps and compare with PDFs exported before.

Usage: python3 -I recipes/0463-compare-renders.py SAMPLES_DIR OUT_DIR [SKIP,SKIP,...]

For every SAMPLES_DIR/NNNN/NAME.pdf that sits next to NAME.pages or NAME.numbers, exports that
document again with recipes/0372-in-app.sh into OUT_DIR/NNNN-NAME.pdf, then compares the two
first pages with recipes/0399-pdf-diff.swift. Experiments named in SKIP are left out. Documents of
experiments 0375, 0376, 0377 and 0443 are exported with comments, as they were then. Prints one
line per document and a total.
"""
import glob
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WITH_COMMENTS = {"0375", "0376", "0377", "0443"}


def main(samples, out, skip=""):
    skip = set(filter(None, skip.split(",")))
    os.makedirs(out, exist_ok=True)
    out = os.path.realpath(out)
    pairs = []
    for pdf in sorted(glob.glob(os.path.join(samples, "[0-9][0-9][0-9][0-9]", "*.pdf"))):
        exp = os.path.basename(os.path.dirname(pdf))
        if exp in skip:
            continue
        for ext, app in ((".pages", "Pages"), (".numbers", "Numbers")):
            doc = pdf[:-4] + ext
            if os.path.exists(doc):
                pairs.append((exp, doc, app, pdf))
    totals = {"same": 0, "differ": 0, "failed": 0}
    for exp, doc, app, old in pairs:
        new = os.path.join(out, f"{exp}-{os.path.basename(old)}")
        props = " with properties {include comments:true}" if exp in WITH_COMMENTS else ""
        script = f'export d to POSIX file "{new}" as PDF{props}'
        try:
            subprocess.run(["sh", os.path.join(HERE, "0372-in-app.sh"), app, doc, script],
                           capture_output=True, text=True, timeout=120)
        except subprocess.TimeoutExpired:
            pass
        name = f"{exp}/{os.path.basename(doc)}"
        if not os.path.exists(new):
            totals["failed"] += 1
            print(f"FAILED {name}", flush=True)
            continue
        r = subprocess.run(["swift", os.path.join(HERE, "0399-pdf-diff.swift"), old, new],
                           capture_output=True, text=True)
        line = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr.strip()[:100]
        if "same as" in line:
            totals["same"] += 1
            print(f"SAME {name}", flush=True)
        else:
            totals["differ"] += 1
            print(f"DIFFER {name}: {line.split(': ', 1)[-1]}", flush=True)
    print(totals, flush=True)


if __name__ == "__main__":
    main(*sys.argv[1:4])
