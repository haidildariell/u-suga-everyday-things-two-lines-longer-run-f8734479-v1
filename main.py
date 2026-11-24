"""Everyday Things, Two Lines — entry program.

Writes a two-line explanation of rain to /output/entry.txt (or the
path in ENTRY_OUTPUT). Line 1 explains rain to a 10-year-old in a
single vivid sentence built on one concrete analogy; line 2 says in
one sentence what that analogy maps and what it leaves out.
"""

import os

LINE_1 = (
    "Rain is the sky tipping over a giant watering can, "
    "pouring water down in drops that patter on the roof."
)

LINE_2 = (
    "The watering can shows that the water comes from above and "
    "falls in separate drops, but it leaves out the clouds that "
    "hold the water, the wind that pushes it, and how rain can "
    "slant sideways in a storm."
)


def build_entry() -> str:
    """Assemble the two lines into the entry text."""
    lines = [LINE_1, LINE_2]
    text = "\n".join(lines)
    return text


def validate(text: str) -> None:
    """Check the gate: 1-400 chars of UTF-8 text, exactly two lines."""
    if not (1 <= len(text) <= 400):
        raise ValueError(f"entry must be 1-400 chars, got {len(text)}")
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if text.endswith("\n"):
        raise ValueError("entry must not end with a trailing newline")
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError(f"entry must be exactly 2 lines, got {len(lines)}")
    for i, line in enumerate(lines, start=1):
        if line.strip() == "":
            raise ValueError(f"line {i} must not be empty")
        if not line.endswith("."):
            raise ValueError(f"line {i} must end as one sentence")


def main() -> None:
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    text = build_entry()
    validate(text)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
