#!/usr/bin/env bash
# Bootstrap the Symphony workspace from the live repo.
# Called in after_create and before_run hooks.

set -euo pipefail

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname "$0")" && pwd)
# shellcheck source=/dev/null
. "${SCRIPT_DIR}/load-env.sh"

if [ -z "${LIVE_REPO_ROOT:-}" ]; then
  echo "bootstrap-workspace: LIVE_REPO_ROOT is not set. Add it to .env." >&2
  exit 1
fi

if [ ! -d .git ]; then
  git init -b main .
fi

rsync -a --delete \
  --exclude '.git' \
  --exclude '.env' \
  --exclude 'symphony-logs/' \
  --exclude '.symphony-state/' \
  "${LIVE_REPO_ROOT}/" ./

echo "bootstrap-workspace: workspace synced from ${LIVE_REPO_ROOT}"
