#!/usr/bin/env python3
"""Write one museum placard line to /output/entry.txt.

The placard is a single fixed line of at most 180 characters, a label
for an ordinary office object catalogued as if it were an ancient
artifact: a drinking vessel of glazed ceramic, dated c. 2016, inscribed
WORLD'S BEST BOSS, donated by the staff, unanimously, in a secret ballot
whose result no one has explained.

The output never changes: every run writes the same bytes. The file is
left world-readable (mode 0644) so the grader can collect it. No network
access, no dependencies beyond the standard library.
"""

import os
import sys

PLACARD = (
    "Drinking vessel, c. 2016, glazed ceramic. "
    "Inscribed WORLD'S BEST BOSS. "
    "Donated by the staff, unanimously, "
    "in a secret ballot whose result no one has explained."
)


def main() -> int:
    line = PLACARD.strip()
    if not 1 <= len(line) <= 180:
        print(f"placard is {len(line)} characters, must be 1-180", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("placard must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    os.umask(0o022)
    raise SystemExit(main())
