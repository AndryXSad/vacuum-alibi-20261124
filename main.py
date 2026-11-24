"""The Vacuum's Alibi — one-line excuse writer.

A robot vacuum explains, in one deadpan line, why it missed a spot.
The program writes exactly one line of text to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR when set, else /output).

Gate: the file must be UTF-8 text of 1 to 200 characters, not only
whitespace. This line is 98 characters.
"""

import os

LINE = "I left that spot as a control sample, so future cleans have something to compare against. Science."


def validate(line):
    """Enforce the competition gate before writing anything."""
    text = line.strip()
    if not text:
        raise ValueError("entry must not be only whitespace")
    if len(text) > 200:
        raise ValueError("entry is %d characters, over the 200 limit" % len(text))
    if "\n" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
