"""Freeze the current specification as an earlier release, before spec/ moves on to a new one.

Usage: python3 -I site/archive.py RELEASE

Copies spec/*.md to spec/versions/RELEASE/ and rewrites their relative links that leave spec/
(to experiments, recipes and the rest of the repository) so they still work two folders deeper.
Links between the spec's own pages stay inside the copy. Afterwards, set CURRENT_VERSION in
site/build.py to the new release and rebuild the site: the copy is published at spec/RELEASE/.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def deepen(md):
    return re.sub(r"(\]\()\.\./", r"\1../../../", md)


def main():
    if len(sys.argv) != 2 or not re.match(r"^\d+(\.\d+)*$", sys.argv[1]):
        sys.exit("usage: python3 -I site/archive.py RELEASE   (for example 15.4)")
    release = sys.argv[1]
    spec = os.path.join(ROOT, "spec")
    dest = os.path.join(spec, "versions", release)
    if os.path.exists(dest):
        sys.exit(f"spec/versions/{release} already exists")
    os.makedirs(dest)
    names = sorted(f for f in os.listdir(spec) if f.endswith(".md"))
    for name in names:
        with open(os.path.join(spec, name), encoding="utf-8") as f:
            md = f.read()
        with open(os.path.join(dest, name), "w", encoding="utf-8") as f:
            f.write(deepen(md))
    print(f"froze {len(names)} pages in spec/versions/{release}/; now set CURRENT_VERSION in site/build.py")


if __name__ == "__main__":
    main()
