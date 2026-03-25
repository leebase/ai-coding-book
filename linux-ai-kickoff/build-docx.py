#!/usr/bin/env python3
"""Build DOCX for Teach Yourself Anything."""

from __future__ import annotations

import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory

from build_common import AUTHOR, BOOK_DIR, DOCX_PATH, MANUSCRIPT_PATH, SUBTITLE, TITLE, assemble_export_markdown, assemble_manuscript


def main() -> None:
    MANUSCRIPT_PATH.write_text(assemble_manuscript(), encoding="utf-8")

    with TemporaryDirectory() as temp_dir:
        source_path = Path(temp_dir) / "teach-yourself-anything-export.md"
        source_path.write_text(assemble_export_markdown(), encoding="utf-8")
        cmd = [
            "pandoc",
            str(source_path),
            "--from",
            "markdown+hard_line_breaks+link_attributes",
            "--to",
            "docx",
            "--resource-path",
            str(BOOK_DIR),
            "-o",
            str(DOCX_PATH),
        ]
        subprocess.run(cmd, cwd=BOOK_DIR, check=True)

    size = DOCX_PATH.stat().st_size
    print(f"Written: {DOCX_PATH} ({size // 1024}KB)")


if __name__ == "__main__":
    main()
