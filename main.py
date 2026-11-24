#!/usr/bin/env python3
"""Entry for make.fun "Seventeen Syllables of Debugging".

Writes one original haiku (5-7-5, 17 syllables) to /output/entry.txt.
Standard library only, no network, no randomness: the text is a literal.
"""

from pathlib import Path

# One print in the loop      -> 5
# the bug will not reproduce -> 7
# the print was the bug.     -> 5
HAIKU = (
    "One print in the loop\n"
    "the bug will not reproduce\n"
    "the print was the bug."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(HAIKU, encoding="utf-8")


if __name__ == "__main__":
    main()
