#!/usr/bin/env bash
# enforce-after-run.sh
# Validates that the declared artifact landed in the live repo before
# allowing a Done state. Reopens the issue in Linear if the artifact is missing.

set -euo pipefail

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname "$0")" && pwd)
# shellcheck source=/dev/null
. "${SCRIPT_DIR}/load-env.sh"

if [ -z "${LIVE_REPO_ROOT:-}" ]; then
  echo "enforce-after-run: LIVE_REPO_ROOT is not set. Add it to .env." >&2
  exit 1
fi
BACKLOG_PATH="${LIVE_REPO_ROOT}/BACKLOG.md"

sync_repo() {
  rsync -a --delete \
    --exclude '.git' \
    --exclude '.env' \
    --exclude 'symphony-logs/' \
    --exclude '.symphony-state/' \
    ./ "${LIVE_REPO_ROOT}/"
}

ensure_live_repo_writable() {
  local probe_path
  if ! probe_path="$(mktemp "${LIVE_REPO_ROOT}/.after-run-write-check.XXXXXX" 2>/dev/null)"; then
    echo "after_run guard: live repo ${LIVE_REPO_ROOT} is not writable; sync cannot proceed" >&2
    return 1
  fi
  rm -f "${probe_path}"
}

query_linear() {
  local payload="$1"
  curl -s https://api.linear.app/graphql \
    -H "Authorization: ${LINEAR_API_KEY}" \
    -H "Content-Type: application/json" \
    --data-binary @- <<EOF
${payload}
EOF
}

build_graphql_payload() {
  local query="$1"
  local variables_json="$2"
  python3 -c '
import json, sys
print(json.dumps({"query": sys.argv[1], "variables": json.loads(sys.argv[2])}))
' "$query" "$variables_json"
}

read_json_field() {
  local field_path="$1"
  python3 -c '
import json, sys
payload = json.load(sys.stdin)
value = payload
for part in sys.argv[1].split("."):
    if part.isdigit():
        value = value[int(part)]
    else:
        value = value.get(part)
    if value is None:
        break
if isinstance(value, str):
    print(value)
' "$field_path"
}

extract_backlog_id() {
  local title="$1"
  printf '%s\n' "$title" | sed -n 's/.*\(AENV-[0-9][0-9][0-9]\).*/\1/p' | head -n 1
}

artifact_path_for_backlog_id() {
  local backlog_id="$1"
  # Matches the format: "  artifact_path:  chapters/briefs/ch-01-brief.md"
  # within the code block for this issue in BACKLOG.md
  awk "/^### ${backlog_id}$/,/^### /" "${BACKLOG_PATH}" \
    | sed -n 's/^  artifact_path:[[:space:]]*\(.*\)$/\1/p' \
    | head -n 1
}

main() {
  ensure_live_repo_writable
  sync_repo

  if [ -z "${LINEAR_API_KEY:-}" ]; then
    echo "after_run guard: LINEAR_API_KEY not set; skipping tracker enforcement" >&2
    exit 0
  fi

  local issue_identifier
  issue_identifier="$(basename "$PWD")"

  # Only enforce on tracker issue workspaces (e.g. AENV-001)
  case "${issue_identifier}" in
    *-*) ;;
    *)
      echo "after_run guard: workspace ${issue_identifier} is not a tracker issue; sync only" >&2
      exit 0
      ;;
  esac

  local team_key issue_number
  team_key="${issue_identifier%%-*}"
  issue_number="${issue_identifier#*-}"

  if ! printf '%s' "${issue_number}" | grep -Eq '^[0-9]+$'; then
    echo "after_run guard: workspace ${issue_identifier} does not end with a numeric issue number; sync only" >&2
    exit 0
  fi

  # Query Linear for issue metadata
  local issue_payload issue_id issue_title issue_state
  issue_payload="$(query_linear "$(build_graphql_payload \
    'query AEnvIssue($teamKey:String!,$number:Float!){ issues(filter:{ team:{ key:{ eq:$teamKey } }, number:{ eq:$number } }, first:1) { nodes { id identifier title state { name } } } }' \
    "$(printf '{"teamKey":"%s","number":%s}' "${team_key}" "${issue_number}")"
  )")"

  issue_id="$(printf '%s' "${issue_payload}" | read_json_field 'data.issues.nodes.0.id')"
  issue_title="$(printf '%s' "${issue_payload}" | read_json_field 'data.issues.nodes.0.title')"
  issue_state="$(printf '%s' "${issue_payload}" | read_json_field 'data.issues.nodes.0.state.name')"

  if [ -z "${issue_id}" ] || [ -z "${issue_title}" ] || [ -z "${issue_state}" ]; then
    echo "after_run guard: could not resolve Linear issue metadata for ${issue_identifier}; sync only" >&2
    exit 0
  fi

  local backlog_id
  backlog_id="$(extract_backlog_id "${issue_title}")"

  if [ -z "${backlog_id}" ]; then
    echo "after_run guard: title '${issue_title}' has no AENV-xxx id; sync only" >&2
    exit 0
  fi

  local artifact_path artifact_abs
  artifact_path="$(artifact_path_for_backlog_id "${backlog_id}")"

  if [ -z "${artifact_path}" ]; then
    echo "after_run guard: ${backlog_id} has no artifact_path in BACKLOG.md; sync only" >&2
    exit 0
  fi

  artifact_abs="${LIVE_REPO_ROOT}/${artifact_path}"

  if [ "${issue_state}" != "Done" ]; then
    echo "after_run guard: ${issue_identifier} is ${issue_state}; no enforcement needed" >&2
    exit 0
  fi

  if [ -f "${artifact_abs}" ]; then
    echo "after_run guard: ${artifact_path} exists; Done state allowed for ${issue_identifier}" >&2
    exit 0
  fi

  # Artifact missing — reopen the issue to Todo
  local todo_state_payload todo_state_id
  todo_state_payload="$(query_linear "$(build_graphql_payload \
    'query AEnvResolveTodo($issueId:String!,$stateName:String!){ issue(id:$issueId) { team { states(filter:{ name:{ eq:$stateName } }, first:1) { nodes { id } } } } }' \
    "$(printf '{"issueId":"%s","stateName":"Todo"}' "${issue_id}")"
  )")"
  todo_state_id="$(printf '%s' "${todo_state_payload}" | read_json_field 'data.issue.team.states.nodes.0.id')"

  if [ -z "${todo_state_id}" ]; then
    echo "after_run guard: could not resolve Todo state id for ${issue_identifier}; sync only" >&2
    exit 0
  fi

  query_linear "$(build_graphql_payload \
    'mutation AEnvReopenIssue($issueId:String!,$stateId:String!){ issueUpdate(id:$issueId, input:{ stateId:$stateId }) { success } }' \
    "$(printf '{"issueId":"%s","stateId":"%s"}' "${issue_id}" "${todo_state_id}")"
  )" >/dev/null

  query_linear "$(build_graphql_payload \
    'mutation AEnvComment($issueId:String!,$body:String!){ commentCreate(input:{ issueId:$issueId, body:$body }) { success } }' \
    "$(python3 -c 'import json, sys; print(json.dumps({"issueId": sys.argv[1], "body": sys.argv[2]}))' \
      "${issue_id}" \
      "Auto-guard reopened ${issue_identifier}: required artifact ${artifact_path} is missing from the live repo after the Symphony run. Do not mark Done until the file exists at ${artifact_abs}."
    )"
  )" >/dev/null

  echo "after_run guard: reopened ${issue_identifier} — ${artifact_path} not found in live repo" >&2
}

main "$@"
