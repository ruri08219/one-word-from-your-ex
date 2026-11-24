"""One Word From Your Ex — make.fun entry.

Writes exactly one word, the word the entrant's ex would use to describe
them, to /output/entry.txt. Nothing else.
"""

from pathlib import Path

WORD = "rehearsal"
OUTPUT_PATH = Path("/output/entry.txt")

# Fail-fast guard BEFORE writing: the gate requires UTF-8 text of 1 to 24
# characters, not only white space.
if not WORD.strip():
    raise ValueError("entry word must not be only white space")
if not 1 <= len(WORD) <= 24:
    raise ValueError("entry word must be 1 to 24 characters long")
if len(WORD.split()) != 1:
    raise ValueError("entry must be exactly one word")

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
OUTPUT_PATH.write_text(WORD, encoding="utf-8")

# Round-trip assert: read the file back and confirm it is exactly the word.
if OUTPUT_PATH.read_text(encoding="utf-8") != WORD:
    raise AssertionError("round-trip check failed: entry.txt does not match the word")
