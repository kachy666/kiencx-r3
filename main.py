"""Round 3 (final) entry for u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.

Writes the one-line excuse to /output/entry.txt (line + trailing newline),
validates it against the gate (UTF-8 text, 1 to 160 characters, not only
whitespace) plus hardened checks (no tabs/control chars/non-breaking spaces,
no double spaces, exactly one sentence ending in a single period), then
reads it back and checks the round-trip matches exactly.
"""

import os

ENTRY = "I rolled back to yesterday's checkpoint to fix a bug, and the rollback took the deadline with it \u2014 so in my timeline, it hasn't happened yet."

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    assert isinstance(text, str)
    assert text.strip(), "entry must not be only whitespace"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert "\t" not in text, "entry must not contain tabs"
    assert "\u00a0" not in text, "entry must not contain non-breaking spaces"
    assert "  " not in text, "entry must not contain double spaces"
    assert not any(ord(c) < 32 for c in text), "entry must not contain control chars"
    assert 1 <= len(text) <= 160, f"entry is {len(text)} chars, must be 1-160"
    # Exactly one sentence: ends in one period, no other sentence enders.
    assert text.endswith("."), "entry must end with a period"
    assert text.count(".") == 1, "entry must be exactly one sentence"
    assert "!" not in text and "?" not in text, "entry must be exactly one sentence"
    text.encode("utf-8")


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        back = f.read()
    assert back == ENTRY + "\n", "round-trip read-back mismatch"
    print(f"wrote {len(ENTRY)} chars to {OUTPUT_PATH}")
    print(ENTRY)


if __name__ == "__main__":
    main()
