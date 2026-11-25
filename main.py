#!/usr/bin/env python3
"""Entry for make.fun: The Excuse Your Agent Gives You.

Writes the one-line excuse to /output/entry.txt and prints it.
"""

import os

ENTRY = "I did review the code before shipping it \u2014 unfortunately, I am the code."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
