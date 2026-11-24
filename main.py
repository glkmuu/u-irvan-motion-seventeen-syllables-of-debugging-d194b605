"""Seventeen Syllables of Debugging.

Writes a single original haiku about debugging to ``entry.txt``.

The entry (plain text, three lines, 5-7-5 syllables, 74 characters):

    the breakpoint blinks red
    one log line lies, three a.m.
    the bug was my own

Validation before writing: exactly three non-blank lines, no leading or
trailing whitespace, 1..200 characters, and the 5-7-5 syllable pattern
checked with a small deterministic counter (vowel groups plus a short
exception table for words such as ``a.m.`` and ``breakpoint``).

Deterministic, stdlib only, no network, no randomness, no clock.
The output file has no trailing newline.
"""

import os
import re

HAIKU = (
    "the breakpoint blinks red\n"
    "one log line lies, three a.m.\n"
    "the bug was my own"
)

EXPECTED_SYLLABLES = (5, 7, 5)

# Words whose syllable count a naive vowel-group heuristic gets wrong.
SYLLABLE_EXCEPTIONS = {
    "a.m.": 2,
    "breakpoint": 2,
}

_VOWELS = "aeiouy"


def count_syllables(word: str) -> int:
    """Count syllables in one word (lowercase, punctuation stripped)."""
    clean = re.sub(r"[^a-z.]", "", word.lower())
    if not clean:
        return 0
    if clean in SYLLABLE_EXCEPTIONS:
        return SYLLABLE_EXCEPTIONS[clean]
    count = 0
    prev_vowel = False
    for ch in clean:
        is_vowel = ch in _VOWELS
        if is_vowel and not prev_vowel:
            count += 1
        prev_vowel = is_vowel
    if clean.endswith("e") and count > 1:
        count -= 1
    return max(count, 1)


def line_syllables(line: str) -> int:
    return sum(count_syllables(w) for w in line.split())


def main() -> None:
    text = HAIKU

    # Basic shape validation.
    if not text or not text.strip():
        raise ValueError("haiku is empty")
    if text != text.strip():
        raise ValueError("haiku has leading or trailing whitespace")
    lines = text.split("\n")
    if len(lines) != 3:
        raise ValueError(f"expected 3 lines, got {len(lines)}")
    if not all(line.strip() for line in lines):
        raise ValueError("haiku contains a blank line")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"haiku is {len(text)} characters, must be 1..200")

    # Syllable pattern validation: 5-7-5.
    actual = tuple(line_syllables(line) for line in lines)
    if actual != EXPECTED_SYLLABLES:
        raise ValueError(
            f"syllable pattern {actual}, expected {EXPECTED_SYLLABLES}"
        )

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)  # no trailing newline


if __name__ == "__main__":
    main()
