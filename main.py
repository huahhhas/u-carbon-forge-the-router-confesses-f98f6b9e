#!/usr/bin/env python3
"""The Router Confesses — make.fun entry.

Writes one line (<=200 chars): a home Wi-Fi router excusing itself
for dropping the connection at the climax of a movie.
Pure stdlib. Output path defaults to /output/entry.txt (the grader
sandbox); set OUTPUT_PATH to override locally.
"""
import os

ENTRY = (
    "I already know who did it, so I cut the feed at the climax "
    "\u2014 if I'm not allowed to spoil it, nobody gets to see it."
)

def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip() == ENTRY and ENTRY.strip()
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
