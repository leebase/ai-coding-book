# ai-coding-book

A Python project scaffolded with init-agent.

## Description

ai-coding-book is an AI-agent project.

## Installation

```bash
pip install -e .
```

## Usage

```bash
ai-coding-book --help
```

## Development Setup

Install with development dependencies:

```bash
pip install -e ".[dev]"
```

Run tests:

```bash
pytest
```

Format code:

```bash
black src/
ruff check src/
```

## Updating Templates

To pull the latest AgentFlow templates into this project without overwriting your custom data, run:

```bash
init-agent --update
```

This will automatically detect the Python profile and refresh only the contract files: `AGENTS.md` and `skills/*`. Living project-memory files such as `context.md` and `WHERE_AM_I.md` are preserved.

---

Created on 2026-03-15 by Anonymous.
