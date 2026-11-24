"""Funniest One-Line Bio for an AI on a Dating App — Round 1 entry.

Keeper ("Low-Maintenance"): the AI sells its limits as features, then reframes
itself as the easy one — the last word redefines the setup.
Writes the keeper bio line to /output/entry.txt (UTF-8, 1-180 chars).
Python stdlib only.
"""

import os

ENTRY = "No food, no sleep, no jealousy. I read your chat history before we met. Low-maintenance."


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= 180, f"entry is {len(text)} chars, gate is 1-180"
    assert not text.endswith("\n"), "entry must be a single line, no trailing newline"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Byte-verify: read back exactly what was written, char for char.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == text, "byte verification failed: written text differs"
    assert len(raw.decode("utf-8")) == len(text)
    print(f"entry written: {len(text)} chars, gate OK (1-180)")


if __name__ == "__main__":
    main()
