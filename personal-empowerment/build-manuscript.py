#!/usr/bin/env python3
"""Build the combined markdown manuscript for the personal empowerment book."""

from __future__ import annotations

from build_common import MANUSCRIPT_PATH, assemble_markdown_book


def main() -> None:
    MANUSCRIPT_PATH.write_text(assemble_markdown_book(), encoding="utf-8")
    size = MANUSCRIPT_PATH.stat().st_size
    print(f"Written: {MANUSCRIPT_PATH} ({size // 1024}KB)")


if __name__ == "__main__":
    main()
