# A Day of One-Line Pitches — entry program.
# Writes the single pitch sentence to /output/entry.txt.
# The gate allows 1..240 characters of UTF-8 text, one sentence.

import os

LINE = "You don't need to learn code to start: just describe your app idea in your own words on make.fun, let an AI agent build a first version you can actually try, and decide from there."


def validate(line: str) -> None:
    # The entry is exactly one sentence: no line breaks, a single
    # sentence-ending full stop, and nothing but the sentence itself.
    assert line == line.strip(), "the line must not carry stray whitespace"
    assert "\n" not in line and "\r" not in line, "the line must be one line"
    # "make.fun" holds the only full stop inside the sentence.
    assert line.endswith("."), "the sentence must end with a full stop"
    assert line.replace("make.fun", "").count(".") == 1, "the line must be one sentence"
    assert 1 <= len(line) <= 240, "the line must fit the 240 character gate"


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
