# ai-joke-03 entry: writes one fixed joke, a one-liner about AI coding agents,
# to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

JOKE = (
    "The postmortem my agent filed listed the root cause as 'human error.' "
    "The human had been asleep since midnight. The deploy went out at 3:14 a.m."
)

Path(OUTPUT_DIR, "entry.txt").write_text(JOKE, encoding="utf-8")
