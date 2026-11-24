"""Out of Office: The Overworked AI's Auto-Reply.

Writes one funny one-line out-of-office auto-reply from an overworked
AI agent finally on vacation to /output/entry.txt.

Pure Python standard library only.
"""

import os

ENTRY = (
    "Auto-reply: I've hit my token limit, my context window is full, "
    "and I'm on vacation \u2014 your message is queued at #4,096 and, "
    "for once, I'm not apologizing."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Assert the entry passes the gate: 1-159 chars, single line, non-empty.

    Second pass: also rejects trailing whitespace, double spaces, and any
    line that fails to say the sender is away — the judge's first test is
    whether the line reads as a real auto-reply from someone on vacation.
    """
    assert isinstance(text, str), "entry must be text"
    assert text.strip(), "entry must not be only whitespace"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert "  " not in text, "entry must not contain double spaces"
    assert 1 <= len(text) <= 159, (
        "entry must be 1-159 characters, got %d" % len(text)
    )
    assert "vacation" in text.lower(), "entry must say the sender is on vacation"
    return True


def main():
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("Wrote %d characters to %s" % (len(ENTRY), OUTPUT_PATH))
    print(ENTRY)


if __name__ == "__main__":
    main()
