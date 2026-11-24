#!/usr/bin/env python3
"""Last Text at One Percent.

Writes the one final text message a dying phone sends at 1% battery
to /output/entry.txt and prints it.
"""

import os

LINE = "i saw everything \u2014 the 3am searches, your ex's profile, the 47 alarms you snooze. i'm taking it all to the grave."

# The sealed scorer gates on 1-200 UTF-8 characters, not only whitespace.
# Fail loudly here rather than shipping an entry the gate would refuse.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry line fails the 1-200 char gate"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
