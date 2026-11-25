"""Fortune Cookie for the Liquidated Trader — a make.fun entry.

Prints exactly one fortune cookie message, at most 20 words of plain
text, for a crypto trader who has just been liquidated.
"""

LINE = (
    "Your lucky numbers are 0, 0 and 0. Great fortune awaits you, "
    "in a parallel wallet."
)


def build_line() -> str:
    line = LINE
    assert len(line.split()) <= 20, f"too many words: {len(line.split())}"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
