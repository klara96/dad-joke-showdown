#!/usr/bin/env python3
"""
Write the dad-joke-showdown entry text to a file.

The entry is a single dad joke told out loud, written exactly as specified.
The output file path can be overridden via the MAKEFUN_OUTPUT_DIR environment variable.
"""

import os
import sys
from pathlib import Path

# The exact entry text as provided
ENTRY_TEXT = (
    "<<<My boss asked why I kept staring at the kettle. "
    "I said I was waiting for it to boil down to the main point.>>>"
)

def main() -> None:
    # Resolve output directory: MAKEFUN_OUTPUT_DIR env var or default /output
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "entry.txt"
    output_file.write_text(ENTRY_TEXT, encoding="utf-8")

    print(f"Wrote entry to {output_file}")

if __name__ == "__main__":
    main()
