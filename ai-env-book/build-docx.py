#!/usr/bin/env python3
"""Build DOCX for Your Dev Environment: A Guide for AI-Assisted Developers"""

import re
from pathlib import Path
from docx import Document
from docx.shared import Pt, Inches, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import docx.opc.constants

BOOK_DIR   = Path(__file__).parent
MD_PATH    = BOOK_DIR / 'your-dev-environment.md'
COVER_PATH = BOOK_DIR / 'DevEnvCover.png'
OUT_PATH   = BOOK_DIR / 'your-dev-environment.docx'

TITLE    = 'Your Dev Environment'
SUBTITLE = 'A Guide for AI-Assisted Developers'
AUTHOR   = 'Lee Harrington'

# Colours
DARK  = RGBColor(0x1A, 0x1A, 0x2E)
MID   = RGBColor(0x2E, 0x40, 0x57)
GREY  = RGBColor(0x55, 0x55, 0x55)
GREEN = RGBColor(0x2E, 0x7D, 0x32)
RED   = RGBColor(0xB7, 0x1C, 0x1C)

def set_cell_bg(cell, hex_color):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex_color)
    tcPr.append(shd)

def add_page_break(doc):
    p = doc.add_paragraph()
    run = p.add_run()
    run.add_break(docx.oxml.ns.qn and __import__('docx').enum.text.WD_BREAK.PAGE)

def setup_styles(doc):
    # Normal
    normal = doc.styles['Normal']
    normal.font.name = 'Georgia'
    normal.font.size = Pt(11)

    # Heading 1
    h1 = doc.styles['Heading 1']
    h1.font.name = 'Arial'
    h1.font.size = Pt(18)
    h1.font.bold = True
    h1.font.color.rgb = DARK
    h1.paragraph_format.space_before = Pt(24)
    h1.paragraph_format.space_after  = Pt(12)
    h1.paragraph_format.page_break_before = True

    # Heading 2
    h2 = doc.styles['Heading 2']
    h2.font.name = 'Arial'
    h2.font.size = Pt(14)
    h2.font.bold = True
    h2.font.color.rgb = MID
    h2.paragraph_format.space_before = Pt(18)
    h2.paragraph_format.space_after  = Pt(8)

    # Heading 3
    h3 = doc.styles['Heading 3']
    h3.font.name = 'Arial'
    h3.font.size = Pt(12)
    h3.font.bold = True
    h3.font.color.rgb = RGBColor(0x44, 0x44, 0x44)
    h3.paragraph_format.space_before = Pt(12)
    h3.paragraph_format.space_after  = Pt(6)

    # Code style
    if 'Code' not in [s.name for s in doc.styles]:
        code_style = doc.styles.add_style('Code', WD_STYLE_TYPE.PARAGRAPH)
    else:
        code_style = doc.styles['Code']
    code_style.font.name = 'Courier New'
    code_style.font.size = Pt(9)
    code_style.paragraph_format.space_before = Pt(6)
    code_style.paragraph_format.space_after  = Pt(6)
    code_style.paragraph_format.left_indent  = Inches(0.4)

def parse_inline(para, text):
    """Add runs to paragraph with **bold**, *italic*, `code` support."""
    remaining = text.replace('<!--', '').replace('-->', '').strip()
    while remaining:
        cm = re.match(r'^`([^`]+)`', remaining)
        if cm:
            r = para.add_run(cm.group(1))
            r.font.name = 'Courier New'
            r.font.size = Pt(9.5)
            remaining = remaining[len(cm.group(0)):]; continue
        bm = re.match(r'^\*\*([^*]+)\*\*', remaining)
        if bm:
            r = para.add_run(bm.group(1)); r.bold = True
            remaining = remaining[len(bm.group(0)):]; continue
        im = re.match(r'^\*([^*]+)\*', remaining) or re.match(r'^_([^_]+)_', remaining)
        if im:
            r = para.add_run(im.group(1)); r.italic = True
            remaining = remaining[len(im.group(0)):]; continue
        nxt = min((remaining.find(c) for c in ['`','*','_'] if remaining.find(c) >= 0), default=-1)
        if nxt == -1: para.add_run(remaining); break
        para.add_run(remaining[:nxt])
        remaining = remaining[nxt:]

def add_code_block(doc, lines):
    for i, line in enumerate(lines):
        p = doc.add_paragraph(style='Code')
        p.add_run(line if line else ' ')
        # border top/bottom on first/last
        pPr = p._p.get_or_add_pPr()
        pBdr = OxmlElement('w:pBdr')
        for side in ['top', 'bottom', 'left', 'right']:
            if (side == 'top' and i > 0) or (side == 'bottom' and i < len(lines)-1):
                continue
            bdr = OxmlElement(f'w:{side}')
            bdr.set(qn('w:val'), 'single')
            bdr.set(qn('w:sz'), '4')
            bdr.set(qn('w:space'), '4')
            bdr.set(qn('w:color'), 'DDDDDD')
            pBdr.append(bdr)
        pPr.append(pBdr)
        # shading
        shd = OxmlElement('w:shd')
        shd.set(qn('w:val'), 'clear')
        shd.set(qn('w:color'), 'auto')
        shd.set(qn('w:fill'), 'F5F5F5')
        pPr.append(shd)

def add_callout(doc, lines):
    label = re.sub(r'^>\s*\*\*([^*]+)\*\*.*', r'\1', lines[0])
    color = 'F0F4F8'
    border_color = '2E4057'
    if "Don't" in label or 'Warning' in label:
        border_color = 'B71C1C'
    elif 'Key Takeaway' in label:
        border_color = '2E7D32'

    for line in lines:
        text = re.sub(r'^>\s*', '', line)
        p = doc.add_paragraph()
        p.paragraph_format.left_indent  = Inches(0.4)
        p.paragraph_format.right_indent = Inches(0.4)
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after  = Pt(3)
        parse_inline(p, text)
        pPr = p._p.get_or_add_pPr()
        pBdr = OxmlElement('w:pBdr')
        left = OxmlElement('w:left')
        left.set(qn('w:val'), 'single'); left.set(qn('w:sz'), '12')
        left.set(qn('w:space'), '6');    left.set(qn('w:color'), border_color)
        pBdr.append(left); pPr.append(pBdr)
        shd = OxmlElement('w:shd')
        shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto')
        shd.set(qn('w:fill'), color);  pPr.append(shd)

def add_hr(doc):
    p = doc.add_paragraph()
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bot = OxmlElement('w:bottom')
    bot.set(qn('w:val'), 'single'); bot.set(qn('w:sz'), '4')
    bot.set(qn('w:space'), '4');    bot.set(qn('w:color'), 'CCCCCC')
    pBdr.append(bot); pPr.append(pBdr)
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after  = Pt(6)

def parse_markdown(doc, md_text):
    lines = md_text.split('\n')
    i, in_code, in_callout = 0, False, False
    code_lines, callout_lines = [], []

    def flush_callout():
        nonlocal in_callout, callout_lines
        if callout_lines:
            add_callout(doc, callout_lines)
        callout_lines = []; in_callout = False

    while i < lines.length() if False else i < len(lines):
        line = lines[i]

        if line.startswith('```'):
            if not in_code:
                flush_callout(); in_code = True; code_lines = []
            else:
                add_code_block(doc, code_lines); in_code = False; code_lines = []
            i += 1; continue
        if in_code:
            code_lines.append(line); i += 1; continue

        if line.startswith('>'):
            in_callout = True; callout_lines.append(line); i += 1; continue
        if in_callout and not line.strip():
            j = i + 1
            while j < len(lines) and not lines[j].strip(): j += 1
            if j < len(lines) and lines[j].startswith('>'):
                callout_lines.append(''); i += 1; continue
            flush_callout(); i += 1; continue
        if in_callout:
            flush_callout()

        if line.strip().startswith('<!--'):
            while i < len(lines) and '-->' not in lines[i]: i += 1
            i += 1; continue

        if re.match(r'^---+$', line.strip()):
            add_hr(doc); i += 1; continue

        if line.startswith('# '):
            p = doc.add_paragraph(style='Heading 1')
            parse_inline(p, line[2:].strip()); i += 1; continue
        if line.startswith('## '):
            p = doc.add_paragraph(style='Heading 2')
            parse_inline(p, line[3:].strip()); i += 1; continue
        if line.startswith('### '):
            p = doc.add_paragraph(style='Heading 3')
            parse_inline(p, line[4:].strip()); i += 1; continue

        if re.match(r'^[-*] ', line):
            p = doc.add_paragraph(style='List Bullet')
            parse_inline(p, line[2:].strip()); i += 1; continue
        if re.match(r'^\d+\. ', line):
            p = doc.add_paragraph(style='List Number')
            parse_inline(p, re.sub(r'^\d+\. ', '', line).strip()); i += 1; continue

        # Simple table row
        if line.startswith('|'):
            if re.match(r'^\|[-| ]+\|$', line.strip()):
                i += 1; continue
            cells = [c.strip() for c in line.split('|') if c.strip()]
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after  = Pt(2)
            for ci, cell in enumerate(cells):
                if ci > 0: p.add_run('    ')
                parse_inline(p, cell)
            i += 1; continue

        if not line.strip():
            i += 1; continue

        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(8)
        p.paragraph_format.line_spacing = Pt(13.8)
        parse_inline(p, line.strip())
        i += 1

    if in_callout: flush_callout()
    if in_code: add_code_block(doc, code_lines)

def main():
    doc = Document()

    # Page size 6x9
    for section in doc.sections:
        section.page_width  = Inches(6)
        section.page_height = Inches(9)
        section.left_margin   = Inches(0.7)
        section.right_margin  = Inches(0.7)
        section.top_margin    = Inches(0.7)
        section.bottom_margin = Inches(0.7)

    setup_styles(doc)

    # Cover page
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    run.add_picture(str(COVER_PATH), width=Inches(5.6))
    doc.add_page_break()

    # Title page
    doc.add_paragraph()
    doc.add_paragraph()
    tp = doc.add_paragraph()
    tp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = tp.add_run(TITLE); r.font.name = 'Arial'; r.font.size = Pt(26); r.font.bold = True; r.font.color.rgb = DARK

    sp = doc.add_paragraph()
    sp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r2 = sp.add_run(SUBTITLE); r2.font.name = 'Arial'; r2.font.size = Pt(13); r2.italic = True; r2.font.color.rgb = GREY
    sp.paragraph_format.space_after = Pt(36)

    add_hr(doc)

    ap = doc.add_paragraph()
    ap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r3 = ap.add_run(AUTHOR); r3.font.name = 'Arial'; r3.font.size = Pt(16); r3.font.color.rgb = MID
    doc.add_page_break()

    # Body
    md_text = MD_PATH.read_text(encoding='utf-8')
    parse_markdown(doc, md_text)

    # Footer on all sections
    for section in doc.sections:
        footer = section.footer
        fp = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        fp.clear()
        r = fp.add_run(f'{TITLE}  •  ')
        r.font.size = Pt(9); r.font.color.rgb = RGBColor(0x88, 0x88, 0x88)
        fldChar1 = OxmlElement('w:fldChar'); fldChar1.set(qn('w:fldCharType'), 'begin')
        instrText = OxmlElement('w:instrText'); instrText.text = 'PAGE'
        fldChar2 = OxmlElement('w:fldChar'); fldChar2.set(qn('w:fldCharType'), 'end')
        pr = fp.add_run()
        pr.font.size = Pt(9); pr.font.color.rgb = RGBColor(0x88, 0x88, 0x88)
        pr._r.append(fldChar1); pr._r.append(instrText); pr._r.append(fldChar2)

    doc.save(str(OUT_PATH))
    size = OUT_PATH.stat().st_size
    print(f'Written: {OUT_PATH} ({size // 1024}KB)')

if __name__ == '__main__':
    main()
