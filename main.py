#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human (round 3).

Validates the entry line (a single line, 1-200 characters, no leading or
trailing whitespace) and writes it to /output/entry.txt.
"""

import os

LINE = "You said 'take your time,' so I took all of it. Every second. It's gone now."

# Where the entry file goes; override for local runs (default /output).
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    line = LINE
    if line != line.strip():
        raise ValueError("line has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    out_path = os.path.join(OUTPUT_DIR, "entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # Round-trip check: what was written must be exactly the line.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read().rstrip("\n")
    if written != line:
        raise ValueError(f"round-trip mismatch in {out_path}")
    print(f"{line} ({len(line)} chars)")


if __name__ == "__main__":
    main()
