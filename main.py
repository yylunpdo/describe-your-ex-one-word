#!/usr/bin/env python3
"""Describe Your Ex in One Word.

Writes exactly one word to /output/entry.txt: the funniest,
sharpest one-word verdict on an ex.

Chosen word: "unsubscribed" -- the ex as a subscription you
finally cancelled. No renewal, no refund, no "we miss you"
email. Short, modern, instantly recognisable, and not one of
the flooded cliches (toxic, ghost, mistake). One word, no
spaces, 12 characters -- well inside the 1-111 gate.
"""

import os

WORD = "unsubscribed"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
