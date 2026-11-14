"""Agency: a poem about the capacity to act.

Writes one poem to /output/entry.txt. Deterministic: no randomness,
no time, no network, no model calls. Python 3.13, standard library only.
"""

import os

POEM = """The door was never locked.
Only shut.
One morning I put my hand to it
and it gave — a sigh of hinges,
light lying across the floorboards
in one long, unbroken blade.

No one handed me the key.
There was no key.
There was a hand, and the hand was mine,
and the morning was mine to open.

I have planted seeds in frozen ground
and waited beside them.
I have written letters I never sent
and sent the ones that scared me.
Each time, the same small thunder:
I chose. It happened. I was there.

The world does not ask permission
to turn. Neither do I.
I am the hand that turns it.
"""


def main() -> None:
    out = "/output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
