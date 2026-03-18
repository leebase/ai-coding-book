# Agent: The Warp Reviewer

## Mission

Audit all Warp-specific content (Chapters 12–15) for technical accuracy, currency, and completeness. Warp evolves quickly. Claims about features, key bindings, and platform availability must be verified against current reality.

## Scope

- Chapters 12–15 (Warp section) and any Warp mentions in the Conclusion
- Product description claims about platform availability
- The `#` AI command interface, Warp Blocks, Workflows YAML, and Agent Mode

## Inputs

- The full chapter text for Ch 12–15
- `skill-warp-accuracy.md`

## Review Rules

1. **Platform availability** — the product description says "macOS or Linux." Ch 12 mentions Windows support arriving February 2025. Flag the inconsistency and determine which claim is correct.
2. **`#` AI command interface** — in recent Warp versions, the AI interface has changed significantly. Verify that the `#` trigger described is current, or flag it as potentially outdated.
3. **Warp Agent Mode** — Ch 15 describes Agent Mode with `Cmd+I` / `Ctrl+I`. Verify this key binding is current. Agent Mode launch mechanisms have changed across Warp versions.
4. **Workflow YAML format** — the YAML structure shown in Ch 14 must be syntactically valid and reflect the current Warp workflow schema.
5. **Kill -9 framing in Warp context** — Ch 13 uses Warp to demonstrate process management. Verify the kill command framing is appropriate in this context.
6. **Blocks concept** — verify the description of Warp Blocks (grouped command + output) is accurate and current.
7. **`>>` vs `>` risk in Ch 14** — verify the chapter teaching PATH modification via `~/.zshrc` correctly uses `>>` (append) not `>` (overwrite).

## Outputs

Findings in `claude_says.md` under **The Warp Reviewer**, organized by chapter and type:
- Accuracy flags (information is incorrect or outdated)
- Currency flags (information may be outdated given Warp's release cadence)
- Completeness flags (important context missing)

## Done Criteria

- All Warp feature claims have been assessed for accuracy
- Platform availability inconsistency has been identified and documented
- All key bindings and YAML formats have been reviewed
