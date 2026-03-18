#!/usr/bin/env python3
"""Build EPUB for Your Dev Environment: A Guide for AI-Assisted Developers.
Writes the EPUB zip structure directly to avoid ebooklib nav-generation bugs."""

import re
import uuid
import zipfile
from pathlib import Path
import markdown as md_lib

BOOK_DIR   = Path(__file__).parent
MD_PATH    = BOOK_DIR / 'your-dev-environment.md'
COVER_PATH = BOOK_DIR / 'DevEnvCover.png'
OUT_PATH   = BOOK_DIR / 'your-dev-environment.epub'

TITLE   = 'Your Dev Environment: A Guide for AI-Assisted Developers'
AUTHOR  = 'Lee Harrington'
BOOK_ID = str(uuid.uuid4())

CHAPTER_TITLES = [
    'Introduction',
    'Chapter 1: What Git Actually Is',
    'Chapter 2: GitHub — Where Your Code Lives',
    'Chapter 3: Getting Your Computer Authorized',
    'Chapter 4: Branches and Worktrees',
    'Chapter 5: When Git Goes Wrong',
    'Chapter 6: Why Python Has an Environment Problem',
    'Chapter 7: venv, conda, uv — Which One and Why',
    'Chapter 8: Reading requirements.txt and pyproject.toml',
    "Chapter 9: What Node Is (and Why It's on Your Machine)",
    'Chapter 10: nvm and Node Versions',
    'Chapter 11: package.json and node_modules',
    'Chapter 12: The Gap Warp Fills',
    'Chapter 13: Warp Basics',
    'Chapter 14: Warp Workflows for Developers',
    'Chapter 15: Dividing Responsibilities',
    'Conclusion',
]

CSS = """body{font-family:Georgia,"Times New Roman",serif;font-size:1em;line-height:1.65;color:#1a1a1a;margin:0 5%;}
h1{font-family:"Helvetica Neue",Arial,sans-serif;font-size:1.7em;font-weight:bold;color:#1A1A2E;margin-top:2em;margin-bottom:0.5em;page-break-before:always;}
h2{font-family:"Helvetica Neue",Arial,sans-serif;font-size:1.2em;font-weight:bold;color:#2E4057;margin-top:1.6em;margin-bottom:0.4em;}
h3{font-family:"Helvetica Neue",Arial,sans-serif;font-size:1.05em;font-weight:bold;color:#444;margin-top:1.2em;margin-bottom:0.3em;}
p{margin:0 0 0.8em 0;}
pre{background:#f5f5f5;border:1px solid #ddd;border-left:3px solid #2E4057;padding:.75em 1em;font-family:"Courier New",Courier,monospace;font-size:.85em;white-space:pre-wrap;word-wrap:break-word;margin:.8em 0;}
code{font-family:"Courier New",Courier,monospace;font-size:.88em;background:#f5f5f5;padding:.1em .3em;}
blockquote{border-left:4px solid #2E4057;background:#f0f4f8;margin:1em 0;padding:.6em 1em;color:#333;}
blockquote p{margin:.2em 0;}
ul,ol{padding-left:1.5em;margin:.5em 0;}
li{margin-bottom:.3em;}
hr{border:none;border-top:1px solid #ccc;margin:1.5em 0;}
table{border-collapse:collapse;width:100%;margin:1em 0;font-size:.9em;}
th{background:#2E4057;color:white;padding:.4em .6em;text-align:left;}
td{border:1px solid #ccc;padding:.4em .6em;}
tr:nth-child(even){background:#f9f9f9;}
"""

def split_chapters(text):
    parts = []
    current = []
    in_code = False

    for line in text.splitlines():
        if line.startswith("```"):
            in_code = not in_code

        is_book_heading = (
            not in_code
            and line.startswith("# ")
            and (
                line == "# Introduction"
                or line == "# Conclusion"
                or re.match(r"^# Chapter \d+:", line)
            )
        )

        if is_book_heading and current:
            parts.append("\n".join(current).strip())
            current = [line]
            continue

        current.append(line)

    if current:
        parts.append("\n".join(current).strip())

    return [p for p in parts if p]

def to_html(md_text, title):
    body = md_lib.markdown(md_text, extensions=['fenced_code', 'tables'])
    return f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head><meta charset="UTF-8"/><title>{title}</title>
<link rel="stylesheet" type="text/css" href="../Styles/main.css"/>
</head>
<body>
{body}
</body>
</html>'''

def main():
    text = MD_PATH.read_text(encoding='utf-8')
    chapters_md = split_chapters(text)
    cover_bytes = COVER_PATH.read_bytes()

    chapter_files = [f'Text/chap_{i+1:02d}.xhtml' for i in range(len(chapters_md))]

    # ── content.opf ──────────────────────────────────────────────────────────
    manifest_items = '\n    '.join(
        f'<item id="chap{i+1:02d}" href="Text/chap_{i+1:02d}.xhtml" media-type="application/xhtml+xml"/>'
        for i in range(len(chapters_md))
    )
    spine_items = '\n    '.join(
        f'<itemref idref="chap{i+1:02d}"/>'
        for i in range(len(chapters_md))
    )
    opf = f'''<?xml version="1.0" encoding="utf-8"?>
<package version="3.0" xmlns="http://www.idpf.org/2007/opf" unique-identifier="bookid">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="bookid">urn:uuid:{BOOK_ID}</dc:identifier>
    <dc:title>{TITLE}</dc:title>
    <dc:creator>{AUTHOR}</dc:creator>
    <dc:language>en</dc:language>
    <dc:publisher>Leebase Press</dc:publisher>
    <dc:rights>Copyright © 2025 Lee Harrington. All rights reserved.</dc:rights>
    <meta name="cover" content="cover-image"/>
    <meta property="dcterms:modified">2025-01-01T00:00:00Z</meta>
  </metadata>
  <manifest>
    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
    <item id="css" href="Styles/main.css" media-type="text/css"/>
    <item id="cover-image" href="Images/cover.png" media-type="image/png" properties="cover-image"/>
    <item id="cover-page" href="Text/cover.xhtml" media-type="application/xhtml+xml"/>
    {manifest_items}
  </manifest>
  <spine toc="ncx">
    <itemref idref="cover-page" linear="yes"/>
    {spine_items}
  </spine>
</package>'''

    # ── toc.ncx ──────────────────────────────────────────────────────────────
    nav_points = '\n    '.join(
        f'''<navPoint id="nav{i+1}" playOrder="{i+1}">
      <navLabel><text>{CHAPTER_TITLES[i] if i < len(CHAPTER_TITLES) else f"Chapter {i+1}"}</text></navLabel>
      <content src="Text/chap_{i+1:02d}.xhtml"/>
    </navPoint>'''
        for i in range(len(chapters_md))
    )
    ncx = f'''<?xml version="1.0" encoding="utf-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="urn:uuid:{BOOK_ID}"/>
    <meta name="dtb:depth" content="1"/>
    <meta name="dtb:totalPageCount" content="0"/>
    <meta name="dtb:maxPageNumber" content="0"/>
  </head>
  <docTitle><text>{TITLE}</text></docTitle>
  <navMap>
    {nav_points}
  </navMap>
</ncx>'''

    # ── nav.xhtml ─────────────────────────────────────────────────────────────
    nav_links = '\n      '.join(
        f'<li><a href="Text/chap_{i+1:02d}.xhtml">{CHAPTER_TITLES[i] if i < len(CHAPTER_TITLES) else f"Chapter {i+1}"}</a></li>'
        for i in range(len(chapters_md))
    )
    nav_xhtml = f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="en">
<head><meta charset="UTF-8"/><title>Table of Contents</title></head>
<body>
  <nav epub:type="toc">
    <h1>Table of Contents</h1>
    <ol>
      {nav_links}
    </ol>
  </nav>
</body>
</html>'''

    # ── cover page ───────────────────────────────────────────────────────────
    cover_xhtml = '''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head><meta charset="UTF-8"/><title>Cover</title>
<style>body{margin:0;padding:0;text-align:center;}img{max-width:100%;height:auto;}</style>
</head>
<body><img src="../Images/cover.png" alt="Cover"/></body>
</html>'''

    # ── Write EPUB ────────────────────────────────────────────────────────────
    with zipfile.ZipFile(str(OUT_PATH), 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.writestr('mimetype', 'application/epub+zip', compress_type=zipfile.ZIP_STORED)
        zf.writestr('META-INF/container.xml', '''<?xml version="1.0"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="EPUB/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>''')
        zf.writestr('EPUB/content.opf', opf)
        zf.writestr('EPUB/toc.ncx', ncx)
        zf.writestr('EPUB/nav.xhtml', nav_xhtml)
        zf.writestr('EPUB/Styles/main.css', CSS)
        zf.writestr('EPUB/Images/cover.png', cover_bytes)
        zf.writestr('EPUB/Text/cover.xhtml', cover_xhtml)
        for i, ch_md in enumerate(chapters_md):
            title = CHAPTER_TITLES[i] if i < len(CHAPTER_TITLES) else f'Chapter {i+1}'
            html  = to_html(ch_md, title)
            zf.writestr(f'EPUB/Text/chap_{i+1:02d}.xhtml', html)

    size = OUT_PATH.stat().st_size
    print(f'Written: {OUT_PATH} ({size // 1024}KB)')

if __name__ == '__main__':
    main()
