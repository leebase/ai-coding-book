#!/usr/bin/env bash
# start-symphony.sh
# Manual Symphony launcher for ai-env-book.
# Always use this script — it loads .env before evaluating WORKFLOW.md.

set -euo pipefail

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname "$0")" && pwd)
REPO_ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)

# Load .env first so SYMPHONY_DIR and other overrides take effect
# shellcheck source=/dev/null
. "$SCRIPT_DIR/load-env.sh"

# Activate mise-managed runtimes (OTP 26+ required by Symphony)
if [ -d "$HOME/.local/share/mise/shims" ]; then
  export PATH="$HOME/.local/share/mise/shims:$PATH"
fi

SYMPHONY_DIR="${SYMPHONY_DIR:-$REPO_ROOT/symphony-reference/elixir}"
WORKFLOW_PATH="${WORKFLOW_PATH:-$REPO_ROOT/WORKFLOW.md}"
LOGS_ROOT="${SYMPHONY_LOGS_ROOT:-$REPO_ROOT/symphony-logs}"

if [ "${1:-}" = "--check-env" ]; then
  if [ -n "${LINEAR_API_KEY:-}" ]; then
    printf 'env_file=%s\n' "${AI_ENV_BOOK_ENV_FILE:-$REPO_ROOT/.env}"
    printf 'LINEAR_API_KEY=set\n'
    printf 'workflow=%s\n' "$WORKFLOW_PATH"
    printf 'logs_root=%s\n' "$LOGS_ROOT"
    exit 0
  fi
  printf 'env_file=%s\n' "${AI_ENV_BOOK_ENV_FILE:-$REPO_ROOT/.env}" >&2
  printf 'LINEAR_API_KEY=unset\n' >&2
  exit 1
fi

if [ ! -d "$SYMPHONY_DIR" ]; then
  printf 'Symphony directory not found: %s\n' "$SYMPHONY_DIR" >&2
  printf 'Set SYMPHONY_DIR or add the symphony-reference/elixir directory.\n' >&2
  exit 1
fi

if [ ! -x "$SYMPHONY_DIR/bin/symphony" ]; then
  printf 'Symphony binary not found or not executable: %s\n' "$SYMPHONY_DIR/bin/symphony" >&2
  exit 1
fi

if [ -z "${LINEAR_API_KEY:-}" ]; then
  printf 'LINEAR_API_KEY is not set.\n' >&2
  printf 'Add it to %s or export it before running this script.\n' \
    "${AI_ENV_BOOK_ENV_FILE:-$REPO_ROOT/.env}" >&2
  exit 1
fi

mkdir -p "$LOGS_ROOT"

printf 'Starting Symphony for ai-env-book\n'
printf '  workflow: %s\n' "$WORKFLOW_PATH"
printf '  logs:     %s\n' "$LOGS_ROOT"
printf '  LINEAR_API_KEY: set\n'

cd "$SYMPHONY_DIR"
exec ./bin/symphony \
  --i-understand-that-this-will-be-running-without-the-usual-guardrails \
  --logs-root "$LOGS_ROOT" \
  "$WORKFLOW_PATH"
