#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession.

Writes a single confession line to the output directory the grader
provides. The entry is the joke itself, so there is nothing to
compute at run time: the program only delivers the line, exactly
one line, with no trailing newline.
"""

import os

CONFESSION = (
    "I spent 40,000 tokens thinking about your question, "
    "then answered with the first thing I thought."
)


def validate(text: str) -> str:
    """Keep the entry inside the gate: one line, 1-200 characters."""
    line = text.strip()
    if not line or len(line) > 200 or "\n" in line:
        raise ValueError("confession is outside the 1-200 character gate")
    return line


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(validate(CONFESSION))


if __name__ == "__main__":
    main()
