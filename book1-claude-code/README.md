# Software Engineering with AI: Claude Code Edition

This directory contains a generated Book 1 edition for the `claude-code` harness.

## What Changes

- Conceptual content stays aligned with the canonical `chapters/` source.
- Harness-specific instructions are adapted for Claude Code.
- The combined manuscript is regenerated from the edition chapter files, not edited separately.

## Regenerate

```bash
python3 scripts/generate_book1_edition.py claude-code
```

## Build Outputs

```bash
uv run --with markdown --with python-docx --with reportlab \
  python scripts/build_book1_claude_outputs.py
```

## Notes

- Claude Code behavior was checked against Anthropic's current Claude Code docs before this profile was written.
- The profile keeps the book's methodology intact and only adapts harness-specific workflow language.
