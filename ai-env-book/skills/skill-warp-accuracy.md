# Skill: Warp Accuracy Audit

## Goal

Verify all Warp-specific technical claims for accuracy and currency. Warp has a high release cadence and the UI, key bindings, and AI features described in the book may have changed since writing.

## Directives

### 1. Platform Availability Verification

Check every platform claim against the current state:
- "Fully available on macOS" — verify
- "Linux support arrived in February 2024" — verify date and current status
- "Windows support arrived in February 2025" — verify date and current status
- Cross-reference against the product description's scope statement ("macOS or Linux only")
- Flag any inconsistency between the chapter text and the product description

### 2. `#` AI Command Interface

The book describes `#` as the trigger for Warp's AI command interface. Audit:
- Is this still the current mechanism for invoking AI in Warp?
- Has the feature been renamed or replaced (e.g., "Warp AI," "Agent Mode")?
- Is the behavior described (natural language → shell command suggestion) current?
- Flag if the `#` trigger is outdated and what the current mechanism is

### 3. Warp Agent Mode

Ch 15 describes Agent Mode activation:
- Current key binding claimed: `Cmd+I` (macOS) / `Ctrl+I` (Linux)
- Verify this is the current binding
- Verify that Agent Mode behavior (multi-step task execution) is described accurately
- Flag if the key binding or behavior has changed

### 4. Workflow YAML Format

The book shows a Warp workflow YAML structure. Verify:
- The YAML keys used are valid in the current Warp workflow schema
- The `name`, `command`, `description`, `arguments` fields (or equivalent) are correctly named
- The file must be placed in `~/.warp/workflows/` — verify this path is current

### 5. Warp Blocks

Verify the description of Warp Blocks:
- "Each command and its output form a block" — verify this is still the core UI paradigm
- Block navigation, selection, and sharing behaviors — flag any that have changed

### 6. Currency Framing

Does the book acknowledge that Warp evolves quickly and that readers should check for updates? A book that presents dynamic tool features as stable facts without this disclaimer ages poorly. Flag if missing.
