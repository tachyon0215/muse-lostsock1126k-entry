#!/usr/bin/env python3
"""make.fun entry: 'Funniest Lost Sock Status Update'.

Competition: u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce

Three candidate lines were drafted for this one:
  A) "Status: single, lint-free, and living behind the dryer with three hair ties and a coin from 2009."
  B) "Update: I escaped the wash and I'm never going back - the other sock knew about the hole and said nothing."
  C) "Day 12 inside the fitted sheet: I have seen things no ankle should ever see."
Line C won: it reads like a diary log from a very specific hiding place and
closes on mock horror, while A is just a list and B runs longer and flatter.

The program is fully deterministic: it emits one fixed string, touches no
network, and uses no randomness or clocks.
"""

import os
from pathlib import Path

# The single status line this entry submits, newline included.
TEXT = "Day 12 inside the fitted sheet: I have seen things no ankle should ever see.\n"

# The brief caps the line at 120 characters (newline excluded).
MAX_CHARS = 120


def validate(text: str) -> None:
    """Check the output: exactly one clean line, within the character cap."""
    body = text[:-1] if text.endswith("\n") else text
    if not 1 <= len(body) <= MAX_CHARS:
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be one line")
    if body != body.strip() or "  " in body:
        raise ValueError("no stray whitespace")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
