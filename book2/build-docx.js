#!/usr/bin/env node
/**
 * Build script: coding-with-agent-teams.docx
 * Converts coding-with-agent-teams.md → formatted Word document with cover image
 */

const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, ImageRun,
  Header, Footer, AlignmentType, HeadingLevel, BorderStyle, WidthType, ShadingType,
  PageNumber, PageBreak, LevelFormat, TableOfContents, SectionType
} = require('docx');
const fs = require('fs');
const path = require('path');

const BOOK2_DIR = path.dirname(__filename);
const MD_PATH   = path.join(BOOK2_DIR, 'coding-with-agent-teams.md');
const COVER_PATH = path.join(BOOK2_DIR, 'cover.jpg');
const OUT_PATH  = path.join(BOOK2_DIR, 'coding-with-agent-teams.docx');

// ─── Page dimensions (6×9 trade paperback in DXA, 1440 = 1 inch) ────────────
const PAGE_W     = 8640;   // 6 inches
const PAGE_H     = 12960;  // 9 inches
const MARGIN     = 1008;   // 0.7 inch
const CONTENT_W  = PAGE_W - MARGIN * 2; // 4.6 inches = 6624 DXA

// ─── Colours ─────────────────────────────────────────────────────────────────
const BRAND_DARK  = '1A1A2E';
const BRAND_MID   = '2E4057';
const CALLOUT_BG  = 'F0F4F8';
const CODE_BG     = 'F5F5F5';
const AMBER       = 'C8860A';

// ─── Helpers ─────────────────────────────────────────────────────────────────
function spacer(pts = 6) {
  return new Paragraph({ children: [new TextRun('')], spacing: { before: 0, after: pts * 20 } });
}

function hrule() {
  return new Paragraph({
    children: [new TextRun('')],
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: 'CCCCCC', space: 6 } },
    spacing: { before: 120, after: 120 },
  });
}

function bold(text) { return new TextRun({ text, bold: true }); }
function italic(text) { return new TextRun({ text, italics: true }); }
function code(text) {
  return new TextRun({ text, font: 'Courier New', size: 18, color: '333333' });
}

// Inline: replace **bold**, *italic*, `code`, _italic_
function parseInline(text) {
  const runs = [];
  let remaining = text;
  // strip markdown comment blocks
  remaining = remaining.replace(/<!--[\s\S]*?-->/g, '').trim();

  while (remaining.length > 0) {
    // backtick code
    const codeMatch = remaining.match(/^`([^`]+)`/);
    if (codeMatch) {
      runs.push(new TextRun({ text: codeMatch[1], font: 'Courier New', size: 18, color: '333333', shading: { fill: 'F5F5F5', type: ShadingType.CLEAR } }));
      remaining = remaining.slice(codeMatch[0].length);
      continue;
    }
    // **bold**
    const boldMatch = remaining.match(/^\*\*([^*]+)\*\*/);
    if (boldMatch) {
      runs.push(new TextRun({ text: boldMatch[1], bold: true }));
      remaining = remaining.slice(boldMatch[0].length);
      continue;
    }
    // *italic* or _italic_
    const italicMatch = remaining.match(/^\*([^*]+)\*/) || remaining.match(/^_([^_]+)_/);
    if (italicMatch) {
      runs.push(new TextRun({ text: italicMatch[1], italics: true }));
      remaining = remaining.slice(italicMatch[0].length);
      continue;
    }
    // plain char
    const next = remaining.search(/[`*_]/);
    if (next === -1) {
      runs.push(new TextRun(remaining));
      remaining = '';
    } else {
      runs.push(new TextRun(remaining.slice(0, next)));
      remaining = remaining.slice(next);
    }
  }
  return runs.length ? runs : [new TextRun(text)];
}

// ─── Callout block ────────────────────────────────────────────────────────────
function calloutParagraph(lines, labelColor) {
  const paras = [];
  lines.forEach((line, i) => {
    const stripped = line.replace(/^>\s*/, '');
    paras.push(new Paragraph({
      children: parseInline(stripped),
      indent: { left: 360, right: 360 },
      spacing: { before: i === 0 ? 120 : 60, after: 60 },
      shading: { fill: CALLOUT_BG, type: ShadingType.CLEAR },
      border: i === 0
        ? { left: { style: BorderStyle.SINGLE, size: 12, color: labelColor, space: 6 } }
        : { left: { style: BorderStyle.SINGLE, size: 12, color: labelColor, space: 6 } },
    }));
  });
  if (paras.length) {
    const last = paras[paras.length - 1];
    // add bottom spacing to last para
  }
  return paras;
}

// ─── Code block ───────────────────────────────────────────────────────────────
function codeBlock(lines) {
  return lines.map((line, i) => new Paragraph({
    children: [new TextRun({ text: line.length ? line : ' ', font: 'Courier New', size: 18, color: '333333' })],
    shading: { fill: CODE_BG, type: ShadingType.CLEAR },
    indent: { left: 360, right: 360 },
    spacing: { before: i === 0 ? 120 : 0, after: i === lines.length - 1 ? 120 : 0, line: 240 },
    border: {
      top:    i === 0              ? { style: BorderStyle.SINGLE, size: 2, color: 'DDDDDD' } : undefined,
      bottom: i === lines.length-1 ? { style: BorderStyle.SINGLE, size: 2, color: 'DDDDDD' } : undefined,
      left:   { style: BorderStyle.SINGLE, size: 2, color: 'DDDDDD' },
      right:  { style: BorderStyle.SINGLE, size: 2, color: 'DDDDDD' },
    }
  }));
}

// ─── Main parser ──────────────────────────────────────────────────────────────
function parseMarkdown(mdText) {
  const lines = mdText.split('\n');
  const paragraphs = [];
  let i = 0;
  let inCodeBlock = false;
  let codeLines = [];
  let calloutLines = [];
  let inCallout = false;

  const flushCallout = () => {
    if (calloutLines.length === 0) return;
    const label = calloutLines[0].replace(/^>\s*\*\*([^*]+)\*\*.*/, '$1');
    const color = label.includes('Antigravity') ? AMBER
                : label.includes('Key Takeaway')  ? '2E7D32'
                : label.includes('Watch')          ? BRAND_MID
                : BRAND_MID;
    paragraphs.push(...calloutParagraph(calloutLines, color));
    paragraphs.push(spacer(4));
    calloutLines = [];
    inCallout = false;
  };

  while (i < lines.length) {
    const line = lines[i];

    // Code fence
    if (line.startsWith('```')) {
      if (!inCodeBlock) {
        flushCallout();
        inCodeBlock = true;
        codeLines = [];
      } else {
        paragraphs.push(...codeBlock(codeLines));
        inCodeBlock = false;
        codeLines = [];
      }
      i++; continue;
    }
    if (inCodeBlock) { codeLines.push(line); i++; continue; }

    // Blockquote / callout
    if (line.startsWith('>')) {
      if (!inCallout && calloutLines.length > 0) flushCallout();
      inCallout = true;
      calloutLines.push(line);
      i++; continue;
    }
    if (inCallout && line.trim() === '') {
      // peek ahead — if next non-empty starts with '>', keep in callout
      let j = i + 1;
      while (j < lines.length && lines[j].trim() === '') j++;
      if (j < lines.length && lines[j].startsWith('>')) { calloutLines.push(''); i++; continue; }
      flushCallout();
      i++; continue;
    }
    if (inCallout) flushCallout();

    // HTML comment — skip
    if (line.startsWith('<!--')) {
      while (i < lines.length && !lines[i].includes('-->')) i++;
      i++; continue;
    }

    // HR
    if (/^---+$/.test(line.trim())) {
      paragraphs.push(hrule());
      i++; continue;
    }

    // Headings
    if (line.startsWith('# ')) {
      const text = line.slice(2).trim();
      // Part divider
      if (text.startsWith('Part ')) {
        paragraphs.push(new Paragraph({
          children: [new TextRun({ text, color: 'FFFFFF', bold: true, size: 32 })],
          heading: HeadingLevel.HEADING_1,
          pageBreakBefore: true,
          alignment: AlignmentType.CENTER,
          shading: { fill: BRAND_DARK, type: ShadingType.CLEAR },
          spacing: { before: 480, after: 480 },
        }));
      } else if (text === 'Introduction' || text === 'Conclusion') {
        paragraphs.push(new Paragraph({
          children: parseInline(text),
          heading: HeadingLevel.HEADING_1,
          pageBreakBefore: true,
          spacing: { before: 480, after: 240 },
        }));
      } else {
        paragraphs.push(new Paragraph({
          children: parseInline(text),
          heading: HeadingLevel.HEADING_1,
          pageBreakBefore: true,
          spacing: { before: 480, after: 240 },
        }));
      }
      i++; continue;
    }
    if (line.startsWith('## ')) {
      paragraphs.push(new Paragraph({
        children: parseInline(line.slice(3).trim()),
        heading: HeadingLevel.HEADING_2,
        spacing: { before: 360, after: 160 },
      }));
      i++; continue;
    }
    if (line.startsWith('### ')) {
      paragraphs.push(new Paragraph({
        children: parseInline(line.slice(4).trim()),
        heading: HeadingLevel.HEADING_3,
        spacing: { before: 240, after: 120 },
      }));
      i++; continue;
    }

    // Bullet list (- item or * item)
    if (/^[-*] /.test(line)) {
      paragraphs.push(new Paragraph({
        children: parseInline(line.slice(2).trim()),
        numbering: { reference: 'bullets', level: 0 },
        spacing: { before: 40, after: 40 },
      }));
      i++; continue;
    }

    // Numbered list
    if (/^\d+\. /.test(line)) {
      paragraphs.push(new Paragraph({
        children: parseInline(line.replace(/^\d+\. /, '').trim()),
        numbering: { reference: 'numbers', level: 0 },
        spacing: { before: 40, after: 40 },
      }));
      i++; continue;
    }

    // Italic-only lines (like the companion volume note)
    if (/^\*[^*].*[^*]\*$/.test(line.trim())) {
      paragraphs.push(new Paragraph({
        children: [new TextRun({ text: line.trim().slice(1, -1), italics: true })],
        spacing: { before: 120, after: 120 },
        alignment: AlignmentType.CENTER,
      }));
      i++; continue;
    }

    // Empty line
    if (line.trim() === '') { i++; continue; }

    // Normal paragraph
    paragraphs.push(new Paragraph({
      children: parseInline(line.trim()),
      spacing: { before: 0, after: 160, line: 276 },
    }));
    i++;
  }

  if (inCallout) flushCallout();
  if (inCodeBlock) paragraphs.push(...codeBlock(codeLines));

  return paragraphs;
}

// ─── Build document ───────────────────────────────────────────────────────────
async function main() {
  const mdText   = fs.readFileSync(MD_PATH, 'utf8');
  const coverImg = fs.readFileSync(COVER_PATH);

  const bodyParagraphs = parseMarkdown(mdText);

  const commonPageProps = {
    page: {
      size: { width: PAGE_W, height: PAGE_H },
      margin: { top: MARGIN, right: MARGIN, bottom: MARGIN, left: MARGIN },
    },
  };

  const doc = new Document({
    numbering: {
      config: [
        {
          reference: 'bullets',
          levels: [{ level: 0, format: LevelFormat.BULLET, text: '\u2022', alignment: AlignmentType.LEFT,
            style: { paragraph: { indent: { left: 720, hanging: 360 } } } }],
        },
        {
          reference: 'numbers',
          levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT,
            style: { paragraph: { indent: { left: 720, hanging: 360 } } } }],
        },
      ],
    },
    styles: {
      default: {
        document: { run: { font: 'Georgia', size: 22 } }, // 11pt
      },
      paragraphStyles: [
        {
          id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true,
          run: { font: 'Arial', size: 36, bold: true, color: BRAND_DARK },
          paragraph: { spacing: { before: 480, after: 240 }, outlineLevel: 0 },
        },
        {
          id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true,
          run: { font: 'Arial', size: 28, bold: true, color: BRAND_MID },
          paragraph: { spacing: { before: 360, after: 160 }, outlineLevel: 1 },
        },
        {
          id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true,
          run: { font: 'Arial', size: 24, bold: true, color: '444444' },
          paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 2 },
        },
      ],
    },
    sections: [
      // ── Section 1: Cover page (no header/footer) ──────────────────────────
      {
        properties: { ...commonPageProps, type: SectionType.NEXT_PAGE },
        children: [
          new Paragraph({
            children: [
              new ImageRun({
                type: 'jpg',
                data: coverImg,
                transformation: {
                  width:  Math.round((PAGE_W - 0) / 914400 * 914400 / 914400 * 609),  // fill page
                  height: Math.round(609 * (1500 / 1120)),
                },
                altText: { title: 'Cover', description: 'Book cover', name: 'cover' },
              }),
            ],
            alignment: AlignmentType.CENTER,
            spacing: { before: 0, after: 0 },
          }),
        ],
      },
      // ── Section 2: Title page ─────────────────────────────────────────────
      {
        properties: { ...commonPageProps, type: SectionType.NEXT_PAGE },
        children: [
          spacer(120),
          new Paragraph({
            children: [new TextRun({ text: 'Coding with Agent Teams', font: 'Arial', size: 56, bold: true, color: BRAND_DARK })],
            alignment: AlignmentType.CENTER,
            spacing: { before: 0, after: 240 },
          }),
          new Paragraph({
            children: [new TextRun({ text: 'A practical guide to document-driven multi-agent coordination', font: 'Arial', size: 24, italics: true, color: '555555' })],
            alignment: AlignmentType.CENTER,
            spacing: { before: 0, after: 720 },
          }),
          hrule(),
          spacer(60),
          new Paragraph({
            children: [new TextRun({ text: 'Lee Harrington', font: 'Arial', size: 32, color: BRAND_MID })],
            alignment: AlignmentType.CENTER,
            spacing: { before: 240, after: 120 },
          }),
        ],
      },
      // ── Section 3: TOC ────────────────────────────────────────────────────
      {
        properties: { ...commonPageProps, type: SectionType.NEXT_PAGE },
        children: [
          new Paragraph({
            children: [new TextRun({ text: 'Table of Contents', font: 'Arial', size: 36, bold: true, color: BRAND_DARK })],
            heading: HeadingLevel.HEADING_1,
            spacing: { before: 0, after: 360 },
          }),
          new TableOfContents('Table of Contents', {
            hyperlink: true,
            headingStyleRange: '1-2',
          }),
        ],
      },
      // ── Section 4: Book body ──────────────────────────────────────────────
      {
        properties: { ...commonPageProps, type: SectionType.NEXT_PAGE },
        footers: {
          default: new Footer({
            children: [new Paragraph({
              children: [
                new TextRun({ text: 'Coding with Agent Teams  •  ', color: '888888', size: 18 }),
                new TextRun({ children: [PageNumber.CURRENT], color: '888888', size: 18 }),
              ],
              alignment: AlignmentType.CENTER,
            })],
          }),
        },
        children: bodyParagraphs,
      },
    ],
  });

  const buffer = await Packer.toBuffer(doc);
  fs.writeFileSync(OUT_PATH, buffer);
  console.log(`Written: ${OUT_PATH} (${Math.round(buffer.length / 1024)}KB)`);
}

main().catch(err => { console.error(err); process.exit(1); });
