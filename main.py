"""Fortune Cookies for Machines — entry program.

Writes one fortune-cookie message an AI agent would get to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (or ``/output/entry.txt`` when the
variable is unset): a single line, no trailing newline.
"""

import os

ENTRY = "You will meet your maker. He is on PTO."


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1 to 200 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = text.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    os.chmod(path, 0o644)

    # Read-back verification: the file on disk must be byte-identical
    # to what was validated, or the run fails instead of shipping a
    # truncated or altered entry.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        raise ValueError("read-back verification failed: entry.txt bytes differ")


if __name__ == "__main__":
    main()
