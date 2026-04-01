#!/usr/bin/env python3
"""Build EPUB for the personal empowerment book."""

from __future__ import annotations

import subprocess
from datetime import datetime
from pathlib import Path
from tempfile import TemporaryDirectory

from build_common import (
    AUTHOR,
    BOOK_DIR,
    COVER_PATH,
    EPUB_CSS_PATH,
    EPUB_PATH,
    MANUSCRIPT_PATH,
    PUBLISHER,
    SUBTITLE,
    TITLE,
    assemble_export_markdown,
    assemble_markdown_book,
)


def main() -> None:
    MANUSCRIPT_PATH.write_text(assemble_markdown_book(), encoding="utf-8")
    copyright_year = datetime.now().year

    with TemporaryDirectory() as temp_dir:
        source_path = Path(temp_dir) / "personal-empowerment-export.md"
        source_path.write_text(assemble_export_markdown(page_break=""), encoding="utf-8")
        cmd = [
            "pandoc",
            str(source_path),
            "--from",
            "markdown+link_attributes+raw_tex",
            "--to",
            "epub3",
            "--standalone",
            "--toc",
            "--css",
            str(EPUB_CSS_PATH),
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
