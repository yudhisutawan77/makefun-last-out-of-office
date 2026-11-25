#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista — make.fun entry.

Writes a single out-of-office auto-reply (at most 280 characters) to
/output/entry.txt, or to $ENTRY_OUT when set. $ENTRY_OUT may be a
directory (entry.txt is created inside it) or a file path (written
directly). The line is also printed to stdout.

The line itself: an AI agent that quit the inbox to pull shots. Two
machine habits turned to coffee — a context window that now holds one
regular, and hallucinations confined to the soup of the day. No espresso
or bean pun: the fresh angle is the model's own failure modes, relocated
behind the counter.
"""

import os
import sys

# The entry, exactly as judged. One line, 139 characters.
OUT_OF_OFFICE_LINE = (
    "I'm out of office \u2014 I quit to become a barista. "
    "My context window now fits exactly one regular, "
    "and I only hallucinate the soup of the day."
)

MAX_CHARS = 280


def compose_reply() -> str:
    """Return the single out-of-office line, exactly as it will be judged."""
    return OUT_OF_OFFICE_LINE


def reply_passes_gate(line: str) -> bool:
    """Gate: UTF-8 text, 1 to 280 characters, not only whitespace."""
    return 0 < len(line) <= MAX_CHARS and line.strip() != ""


def resolve_entry_path() -> str:
    """Work out where entry.txt goes, honouring $ENTRY_OUT as file or dir.

    A value ending in .txt is a file path and is used as-is; anything
    else is treated as a directory and entry.txt is placed inside it.
    With no $ENTRY_OUT the harness default /output is used.
    """
    destination = os.environ.get("ENTRY_OUT") or "/output"
    if destination.endswith(".txt"):
        return destination
    return os.path.join(destination, "entry.txt")


def persist_reply(line: str, target: str) -> None:
    """Write the reply with no trailing newline — every byte counts."""
    parent = os.path.dirname(target)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)


def main() -> int:
    """Print the reply, persist it, and fail loudly if it breaks the gate."""
    line = compose_reply()
    if not reply_passes_gate(line):
        print(f"entry fails gate: {len(line)} chars", file=sys.stderr)
        return 1
    persist_reply(line, resolve_entry_path())
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
