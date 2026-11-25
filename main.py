#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

Writes a single one-line tombstone epitaph, the funniest possible famous
last words, to /output/entry.txt. At most 150 characters, one line.
"""

import os

# The epitaph: a dying instruction with a twist — the plants did it.
# Revised: the em-dash joins the two refusals so the accusation lands in
# one breath instead of trailing as a third sentence.
ENTRY = (
    "Do not resuscitate. Don't water the plants either — "
    "they know what they did."
)


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 150:
        raise ValueError(f"entry must be 1-150 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
