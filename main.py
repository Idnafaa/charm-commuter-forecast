#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

A one-line weather forecast for the invented city of Wobbleford,
written to /output/entry.txt for the make.fun judge.
"""

import os

FORECAST = (
    "Good morning, Wobbleford: rain falls upwards till nine, then sunshine "
    "\u2014 hold your umbrella upside down and your coffee the right way up."
)


def check_line(line):
    """A valid entry is one line of UTF-8 text, 1 to 140 characters."""
    if not line or line != line.strip():
        raise ValueError("entry must be non-empty with no surrounding space")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > 140:
        raise ValueError(f"entry is {len(line)} chars, over the 140 limit")
    line.encode("utf-8")
    return line


def main():
    line = check_line(FORECAST)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line)
    print(f"wrote {len(line)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
