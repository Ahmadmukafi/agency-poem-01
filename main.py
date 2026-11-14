#!/usr/bin/env python3
"""Write one poem about agency to /output/entry.txt.

The poem: a seed in a cracked pot. Agency as the small, concrete act of
planting — choosing to act even without belief, even in a broken vessel —
and the growth that follows whether or not anyone is watching.

Deterministic: the same poem, byte for byte, on every run.
Standard library only. No network.
"""

import os
import sys

POEM = """The pot was cracked. The soil was dust.
I planted a seed anyway.
Not because I believed. Because
my hands were tired of waiting.

I pressed one seed into the dark,
one small brown promise, and tucked it in.
Then I went on with my day — dishes, work,
the ordinary hours — and forgot it.

But the seed did not forget.
It split. It reached. It pushed a green
thumb through the soil and toward the light,
as if the light had been its idea all along.

That is agency: not the grand gesture,
not the speech, not the hero's leap.
Just this — a seed, a cracked pot, a hand
that pressed the future into the dark
and let it grow.
"""


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if len(sys.argv) > 1:
        out_dir = sys.argv[1]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
