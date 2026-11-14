import os
import sys

POEM = """A loose thread hung from my cuff.
Don't pull it, they said.
It will unravel.

I pulled it anyway —
not brave, just tired
of being careful
with things I never chose.

The cuff went first,
then the sleeve,
then the whole grey sweater
came apart in my hands,
wool pooling at my feet
like a tide going out.

And there it was —
the pattern was never mine.
Other hands had knitted it.
I had only ever put it on.

Now my hands are full of yarn.
Mine to wind, mine to drop,
mine to begin.
No one tells them what to knit now.
They are learning what they make
when left alone with the wool."""

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)
    sys.stdout.write(POEM)

if __name__ == "__main__":
    main()
