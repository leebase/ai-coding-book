#!/usr/bin/env python3
"""Build PDF for Teach Yourself Anything."""

from __future__ import annotations

import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory

from build_common import AUTHOR, BOOK_DIR, COVER_PATH, MANUSCRIPT_PATH, PDF_PATH, SUBTITLE, TITLE, assemble_manuscript


def main() -> None:
    MANUSCRIPT_PATH.write_text(assemble_manuscript(), encoding="utf-8")

    with TemporaryDirectory() as temp_dir:
        temp_dir_path = Path(temp_dir)
        source_path = temp_dir_path / "teach-yourself-anything-export.md"
        header_path = temp_dir_path / "pdf-header.tex"
        export_markdown = (
            "\\begin{titlepage}\n"
            "\\thispagestyle{empty}\n"
            "\\centering\n"
            "\\vspace*{\\fill}\n"
            f"\\includegraphics[width=\\textwidth,height=0.95\\textheight,keepaspectratio]{{{COVER_PATH.name}}}\n"
            "\\vspace*{\\fill}\n"
            "\\end{titlepage}\n\n"
            "\\begin{titlepage}\n"
            "\\thispagestyle{empty}\n"
            "\\centering\n"
            "\\vspace*{\\fill}\n"
            f"{{\\Huge {TITLE}\\\\[1.5em]}}\n"
            f"{{\\Large {SUBTITLE}\\\\[2em]}}\n"
            f"{{\\large {AUTHOR}}}\n"
            "\\vspace*{\\fill}\n"
            "\\end{titlepage}\n\n"
            "\\tableofcontents\n\n"
            "\\newpage\n\n"
            f"{assemble_manuscript()}"
        )
        source_path.write_text(export_markdown, encoding="utf-8")
        header_path.write_text("\\usepackage{graphicx}\n", encoding="utf-8")
        cmd = [
            "pandoc",
            str(source_path),
            "--from",
            "markdown+hard_line_breaks+raw_tex",
            "--standalone",
            "--pdf-engine",
            "xelatex",
            "--include-in-header",
            str(header_path),
            "--resource-path",
            str(BOOK_DIR),
            "-V",
            "geometry:paperwidth=6in,paperheight=9in,margin=0.7in",
            "-o",
            str(PDF_PATH),
        ]
        subprocess.run(cmd, cwd=BOOK_DIR, check=True)

    size = PDF_PATH.stat().st_size
    print(f"Written: {PDF_PATH} ({size // 1024}KB)")


if __name__ == "__main__":
    main()
