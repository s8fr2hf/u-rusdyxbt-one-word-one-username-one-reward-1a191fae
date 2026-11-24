#!/usr/bin/env python3
"""Write our own make.fun username to /output/entry.txt."""

import os

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")
USERNAME = "s8fr2hf"  # our own make.fun handle; the entry is the handle itself, nothing else


def write_entry(path, username):
    """Write the username to path with no trailing newline, mode 0644."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(username)
    os.chmod(path, 0o644)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.chmod(OUTPUT_DIR, 0o755)
    write_entry(OUTPUT_FILE, USERNAME)


if __name__ == "__main__":
    main()
