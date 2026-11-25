#!/usr/bin/env python3
"""Midnight Fridge Roast — make.fun bounty entry.

Writes one line of text to /output/entry.txt: a roast of a smart fridge
that refuses to open after midnight. Standard library only, deterministic.
"""

import os

ENTRY = (
    "My smart fridge locks at midnight like a bouncer "
    "\u2014 I'm not sneaking into a club, "
    "I'm sneaking into my own leftovers."
)


def check_gate(text: str) -> None:
    """Fail loudly if the entry would break the bounty gate."""
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry is {len(text)} chars, gate needs 1-200")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")


def main() -> None:
    check_gate(ENTRY)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)
    # Confirm what landed on disk matches the entry byte for byte.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != ENTRY.encode("utf-8"):
        raise ValueError("written bytes differ from ENTRY")


if __name__ == "__main__":
    main()
