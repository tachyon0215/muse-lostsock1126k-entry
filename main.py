#!/usr/bin/env python3
"""Field notes from a sock that never came back from the laundry.

This module is the entry for the make.fun contest 'Funniest Lost Sock
Status Update' (slug
u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce).

Rather than inventing a whole saga, the entry keeps things to a single
dispatch: a diary-style status line written by a sock that has spent
twelve days wedged inside a fitted sheet and has come out the other
side slightly traumatised. Running the module drops that line, exactly
as written, into a file called entry.txt inside whichever directory
the MAKEFUN_OUTPUT_DIR environment variable points at (falling back
to /output). Nothing here is random, timed, or fetched from anywhere;
every run produces the identical file.
"""

import os
from pathlib import Path

# The dispatch itself, kept with its trailing newline already attached
# so the bytes written to disk need no further massaging.
DISPATCH = (
    "Day 12 inside the fitted sheet: "
    "I have seen things no ankle should ever see.\n"
)

# Contest rules allow at most 120 characters for the line, not
# counting the final newline.
LINE_LIMIT = 120


def check_dispatch(line: str) -> None:
    """Raise ValueError unless *line* is one tidy line within the cap.

    The checks, in order: the visible part of the line must be neither
    empty nor longer than LINE_LIMIT; it cannot be blank space alone;
    it may not smuggle in extra line breaks; and it must be free of
    padding or doubled spaces.
    """
    visible = line[:-1] if line.endswith("\n") else line
    if not 1 <= len(visible) <= LINE_LIMIT:
        raise ValueError("dispatch length falls outside the allowed range")
    if not visible.strip():
        raise ValueError("dispatch cannot be whitespace only")
    if "\n" in visible or "\r" in visible:
        raise ValueError("dispatch has to stay on a single line")
    if visible != visible.strip() or "  " in visible:
        raise ValueError("dispatch carries stray whitespace")


def emit() -> None:
    """Validate the dispatch, then write it to entry.txt."""
    check_dispatch(DISPATCH)
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    target_dir.mkdir(parents=True, exist_ok=True)
    payload = DISPATCH.encode("utf-8")
    (target_dir / "entry.txt").write_bytes(payload)


if __name__ == "__main__":
    emit()
