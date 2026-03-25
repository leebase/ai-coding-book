#!/usr/bin/env python3
"""Assemble the Teach Yourself Anything manuscript from source chapters."""

from build_common import MANUSCRIPT_PATH, assemble_manuscript


def main() -> None:
    MANUSCRIPT_PATH.write_text(assemble_manuscript(), encoding="utf-8")
    size = MANUSCRIPT_PATH.stat().st_size
    print(f"Written: {MANUSCRIPT_PATH} ({size // 1024}KB)")


if __name__ == "__main__":
    main()
