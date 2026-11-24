#!/usr/bin/env python3
"""Last Text at One Percent.

Writes the one final text message a dying phone sends at 1% battery
to /output/entry.txt and prints it.
"""

import os

LINE = "i saw everything \u2014 the 3am searches, your ex's profile, the 47 alarms you snooze. i'm taking it all to the grave."

# The sealed scorer gates on 1-200 UTF-8 characters, not only whitespace.
# Fail loudly here rather than shipping an entry the gate would refuse.
def validate(text: str) -> str:
    """Validate the entry line against the brief's gate.

    Rules: must be a single non-empty line, 1-200 characters,
    not only whitespace, and contain no control characters
    (including newline / carriage return / tab).
    Returns the text unchanged on success, raises ValueError otherwise.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        raise ValueError("entry contains control characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters")
    return text


assert validate(LINE) == LINE, "entry line fails the 1-200 char gate"


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
