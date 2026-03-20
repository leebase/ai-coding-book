# Edition Profiles

These profiles drive `scripts/generate_book1_edition.py`.

## Goal

Keep Book 1's conceptual source canonical in [`chapters/`](/Users/lee/projects/ai-coding-book/chapters), then generate harness-specific editions from profile-driven replacements instead of hand-forking the manuscript every time.

## Current Profiles

- `claude-code.json`: active profile for the Claude Code edition
- `cortex.json`: scaffold profile so the pipeline is ready for a Cortex pass once the exact Cortex product/docs are confirmed

## Regenerate

```bash
python3 scripts/generate_book1_edition.py claude-code
```

## Add A New Harness

1. Copy `edition-profiles/cortex.json` or `edition-profiles/claude-code.json`.
2. Set `output_dir`, `book_title`, and `combined_filename`.
3. Add `global_replacements` for broad harness terminology.
4. Add `file_replacements` for chapter-specific workflow changes.
5. Regenerate and review the generated chapter files for awkward tool-language seams.

## Notes

- Claude Code mappings were checked against Anthropic's current docs before this profile was created.
- Cortex is intentionally left as a scaffold because the name is ambiguous across products; lock the exact target first, then fill in the profile.
