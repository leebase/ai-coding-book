#!/usr/bin/env python3
"""Build EPUB for Teach Yourself Anything."""

from __future__ import annotations

import subprocess
from datetime import datetime
from pathlib import Path
from tempfile import TemporaryDirectory

from build_common import AUTHOR, BOOK_DIR, COVER_PATH, EPUB_PATH, PUBLISHER, SUBTITLE, TITLE, assemble_manuscript


def main() -> None:
    copyright_year = datetime.now().year
    with TemporaryDirectory() as temp_dir:
        source_path = Path(temp_dir) / "teach-yourself-anything-export.md"
        source_path.write_text(assemble_manuscript(), encoding="utf-8")
        cmd = [
            "pandoc",
            str(source_path),
            "--from",
            "markdown+hard_line_breaks+link_attributes",
            "--to",
            "epub3",
            "--standalone",
            "--toc",
            "--metadata",
            f"title={TITLE}",
            "--metadata",
            f"subtitle={SUBTITLE}",
            "--metadata",
            f"author={AUTHOR}",
            "--metadata",
            f"publisher={PUBLISHER}",
            "--metadata",
            f"rights=Copyright © {copyright_year} {AUTHOR}. All rights reserved.",
            "--resource-path",
            str(BOOK_DIR),
            f"--epub-cover-image={COVER_PATH}",
            "-o",
            str(EPUB_PATH),
        ]
        subprocess.run(cmd, cwd=BOOK_DIR, check=True)

    size = EPUB_PATH.stat().st_size
    print(f"Written: {EPUB_PATH} ({size // 1024}KB)")


if __name__ == "__main__":
    main()
