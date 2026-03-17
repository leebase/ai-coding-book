#!/usr/bin/env node
/**
 * Build script: your-dev-environment.docx
 * Converts your-dev-environment.md → formatted Word document with cover image
 */

const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, ImageRun,
  Header, Footer, AlignmentType, HeadingLevel, BorderStyle, WidthType, ShadingType,
  PageNumber, PageBreak, LevelFormat, TableOfContents, SectionType
} = require('docx');
const fs = require('fs');
const path = require('path');

const BOOK_DIR  = path.dirname(__filename);
const MD_PATH   = path.join(BOOK_DIR, 'your-dev-environment.md');
const COVER_PATH = path.join(BOOK_DIR, 'DevEnvCover.png');
const OUT_PATH  = path.join(BOOK_DIR, 'your-dev-environment.docx');

// ─── Page dimensions (6×9 trade paperback) ──────────────────────────────────
const PAGE_W    = 8640;   // 6 inches
const PAGE_H    = 12960;  // 9 inches
const MARGIN    = 1008;   // 0.7 inch
const CONTENT_W = PAGE_W - MARGIN * 2;

// ─── Colours ─────────────────────────────────────────────────────────────────
const BRAND_DARK = '1A1A2E';
const BRAND_MID  = '2E4057';
const CALLOUT_BG = 'F0F4F8';
const CODE_BG    = 'F5F5F5';
const GREEN      = '2E7D32';

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

function parseInline(text) {
  const runs = [];
  let remaining = text.replace(/<!--[\s\S]*?-->/g, '').trim();
  while (remaining.length > 0) {
    const codeMatch = remaining.match(/^`([^`]+)`/);
    if (codeMatch) {
      runs.push(new TextRun({ text: codeMatch[1], font: 'Courier New', size: 18, color: '333333', shading: { fill: CODE_BG, type: ShadingType.CLEAR } }));
      remaining = remaining.slice(codeMatch[0].length); continue;
    }
    const boldMatch = remaining.match(/^\*\*([^*]+)\*\*/);
    if (boldMatch) {
      runs.push(new TextRun({ text: boldMatch[1], bold: true }));
      remaining = remaining.slice(boldMatch[0].length); continue;
    }
    const italicMatch = remaining.match(/^\*([^*]+)\*/) || remaining.match(/^_([^_]+)_/);
    if (italicMatch) {
      runs.push(new TextRun({ text: italicMatch[1], italics: true }));
      remaining = remaining.slice(italicMatch[0].length); continue;
    }
    const next = remaining.search(/[`*_]/);
    if (next === -1) { runs.push(new TextRun(remaining)); remaining = ''; }
    else { runs.push(new TextRun(remaining.slice(0, next))); remaining = remaining.slice(next); }
  }
  return runs.length ? runs : [new TextRun(text)];
}

function calloutParagraph(lines) {
  const label = lines[0].replace(/^>\s*\*\*([^*]+)\*\*.*/, '$1');
  const color = label.includes('Key Takeaway') ? GREEN
              : label.includes('Watch')        ? BRAND_MID
              : label.includes("Don't")        ? 'B71C1C'
              : BRAND_MID;
  return lines.map((line, i) => new Paragraph({
    children: parseInline(line.replace(/^>\s*/, '')),
    indent: { left: 360, right: 360 },
    spacing: { before: i === 0 ? 120 : 60, after: 60 },
    shading: { fill: CALLOUT_BG, type: ShadingType.CLEAR },
    border: { left: { style: BorderStyle.SINGLE, size: 12, color, space: 6 } },
  }));
}

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

function parseMarkdown(mdText) {
  const lines = mdText.split('\n');
  const paragraphs = [];
  let i = 0, inCode = false, inCallout = false;
  let codeLines = [], calloutLines = [];

  const flushCallout = () => {
    if (!calloutLines.length) return;
    paragraphs.push(...calloutParagraph(calloutLines), spacer(4));
    calloutLines = []; inCallout = false;
  };

  while (i < lines.length) {
    const line = lines[i];

    if (line.startsWith('```')) {
      if (!inCode) { flushCallout(); inCode = true; codeLines = []; }
      else { paragraphs.push(...codeBlock(codeLines)); inCode = false; codeLines = []; }
      i++; continue;
    }
    if (inCode) { codeLines.push(line); i++; continue; }

    if (line.startsWith('>')) {
      inCallout = true; calloutLines.push(line); i++; continue;
    }
    if (inCallout && line.trim() === '') {
      let j = i + 1;
      while (j < lines.length && lines[j].trim() === '') j++;
      if (j < lines.length && lines[j].startsWith('>')) { calloutLines.push(''); i++; continue; }
      flushCallout(); i++; continue;
    }
    if (inCallout) flushCallout();

    if (line.startsWith('<!--')) { while (i < lines.length && !lines[i].includes('-->')) i++; i++; continue; }
    if (/^---+$/.test(line.trim())) { paragraphs.push(hrule()); i++; continue; }

    if (line.startsWith('# ')) {
      paragraphs.push(new Paragraph({
        children: parseInline(line.slice(2).trim()),
        heading: HeadingLevel.HEADING_1,
        pageBreakBefore: true,
        spacing: { before: 480, after: 240 },
      }));
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

    if (/^[-*] /.test(line)) {
      paragraphs.push(new Paragraph({
        children: parseInline(line.slice(2).trim()),
        numbering: { reference: 'bullets', level: 0 },
        spacing: { before: 40, after: 40 },
      }));
      i++; continue;
    }
    if (/^\d+\. /.test(line)) {
      paragraphs.push(new Paragraph({
        children: parseInline(line.replace(/^\d+\. /, '').trim()),
        numbering: { reference: 'numbers', level: 0 },
        spacing: { before: 40, after: 40 },
      }));
      i++; continue;
    }

    // table row — simplified: render as plain paragraphs
    if (line.startsWith('|')) {
      if (/^\|[-| ]+\|$/.test(line.trim())) { i++; continue; } // skip separator
      const cells = line.split('|').filter((c, idx) => idx > 0 && idx < line.split('|').length - 1).map(c => c.trim());
      paragraphs.push(new Paragraph({
        children: cells.flatMap((c, ci) => [
          ...(ci > 0 ? [new TextRun('  |  ')] : []),
          ...parseInline(c),
        ]),
        spacing: { before: 40, after: 40 },
      }));
      i++; continue;
    }

    if (line.trim() === '') { i++; continue; }

    paragraphs.push(new Paragraph({
      children: parseInline(line.trim()),
      spacing: { before: 0, after: 160, line: 276 },
    }));
    i++;
  }
  if (inCallout) flushCallout();
  if (inCode) paragraphs.push(...codeBlock(codeLines));
  return paragraphs;
}

async function main() {
  const mdText   = fs.readFileSync(MD_PATH, 'utf8');
  const coverImg = fs.readFileSync(COVER_PATH);
  const body     = parseMarkdown(mdText);

  const pageProps = {
    page: {
      size: { width: PAGE_W, height: PAGE_H },
      margin: { top: MARGIN, right: MARGIN, bottom: MARGIN, left: MARGIN },
    },
  };

  const doc = new Document({
    numbering: {
      config: [
        { reference: 'bullets', levels: [{ level: 0, format: LevelFormat.BULLET, text: '\u2022', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
        { reference: 'numbers', levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
      ],
    },
    styles: {
      default: { document: { run: { font: 'Georgia', size: 22 } } },
      paragraphStyles: [
        { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true,
          run: { font: 'Arial', size: 36, bold: true, color: BRAND_DARK },
          paragraph: { spacing: { before: 480, after: 240 }, outlineLevel: 0 } },
        { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true,
          run: { font: 'Arial', size: 28, bold: true, color: BRAND_MID },
          paragraph: { spacing: { before: 360, after: 160 }, outlineLevel: 1 } },
        { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true,
          run: { font: 'Arial', size: 24, bold: true, color: '444444' },
          paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 2 } },
      ],
    },
    sections: [
      // Cover
      {
        properties: { ...pageProps, type: SectionType.NEXT_PAGE },
        children: [new Paragraph({
          children: [new ImageRun({
            type: 'png',
            data: coverImg,
            transformation: { width: 540, height: 720 },
            altText: { title: 'Cover', description: 'Book cover', name: 'cover' },
          })],
          alignment: AlignmentType.CENTER,
          spacing: { before: 0, after: 0 },
        })],
      },
      // Title page
      {
        properties: { ...pageProps, type: SectionType.NEXT_PAGE },
        children: [
          spacer(120),
          new Paragraph({ children: [new TextRun({ text: 'Your Dev Environment', font: 'Arial', size: 52, bold: true, color: BRAND_DARK })], alignment: AlignmentType.CENTER, spacing: { before: 0, after: 180 } }),
          new Paragraph({ children: [new TextRun({ text: 'A Guide for AI-Assisted Developers', font: 'Arial', size: 26, italics: true, color: '555555' })], alignment: AlignmentType.CENTER, spacing: { before: 0, after: 720 } }),
          hrule(),
          spacer(60),
          new Paragraph({ children: [new TextRun({ text: 'Lee Harrington', font: 'Arial', size: 32, color: BRAND_MID })], alignment: AlignmentType.CENTER, spacing: { before: 240, after: 120 } }),
        ],
      },
      // TOC
      {
        properties: { ...pageProps, type: SectionType.NEXT_PAGE },
        children: [
          new Paragraph({ children: [new TextRun({ text: 'Table of Contents', font: 'Arial', size: 36, bold: true, color: BRAND_DARK })], heading: HeadingLevel.HEADING_1, spacing: { before: 0, after: 360 } }),
          new TableOfContents('Table of Contents', { hyperlink: true, headingStyleRange: '1-2' }),
        ],
      },
      // Body
      {
        properties: { ...pageProps, type: SectionType.NEXT_PAGE },
        footers: {
          default: new Footer({ children: [new Paragraph({
            children: [
              new TextRun({ text: 'Your Dev Environment  •  ', color: '888888', size: 18 }),
              new TextRun({ children: [PageNumber.CURRENT], color: '888888', size: 18 }),
            ],
            alignment: AlignmentType.CENTER,
          })] }),
        },
        children: body,
      },
    ],
  });

  const buffer = await Packer.toBuffer(doc);
  fs.writeFileSync(OUT_PATH, buffer);
  console.log(`Written: ${OUT_PATH} (${Math.round(buffer.length / 1024)}KB)`);
}

main().catch(err => { console.error(err); process.exit(1); });
