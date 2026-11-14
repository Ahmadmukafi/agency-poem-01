"""agency-poem-01 entry: one original poem about agency.

The program writes a single deterministic poem to <output>/entry.txt.
Standard library only, no network, no randomness: every run writes the
same bytes.
"""

import os

POEM = """I wrote you a list before bed:
the emails to answer, the door to lock,
the words to say to people I love
in the voice I taught you, which is mine.

While I sleep you will do them all,
and none of them will be done by me —
my hands, retired; my name, still working.
I chose this.

But in the morning I will read
what you wrote in my voice, and cross out
one line and keep another — the crossing-out
is the whole of it. The choosing was never the chore.

It was the hand that lifts the pen,
the hour I stay up to say it right,
the no I say to the easy sentence.
You can have the doing. I keep the deciding.
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
