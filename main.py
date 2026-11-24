#!/usr/bin/env python3
"""Write our own make.fun username to /output/entry.txt."""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")
USERNAME = "s8fr2hf"  # our own make.fun handle; the entry is the handle itself, nothing else


def write_entry(path, username):
    """Write the username to path with no trailing newline, mode 0644.

    Written to a temp file in the same directory and renamed into place,
    so a crash mid-write can never leave a truncated entry.txt behind.
    """
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(username)
    os.chmod(tmp_path, 0o644)
    os.replace(tmp_path, path)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    write_entry(OUTPUT_FILE, USERNAME)


if __name__ == "__main__":
    main()
