#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="${REPO_DIR:-/srv/moreforms/deploy/repo}"
ENV_FILE="${ENV_FILE:-/srv/moreforms/runtime/.env}"
DEPLOY_DIR="${REPO_DIR}/deploy"
OPENCLAW_USER="${OPENCLAW_USER:-openclaw}"

cd "${REPO_DIR}"
git fetch origin
git checkout main
git pull --ff-only origin main

# OpenClaw edits project files directly on the server. After git pull, files updated
# by root need to be handed back to the runtime user or dashboard generation will fail.
chown "${OPENCLAW_USER}:${OPENCLAW_USER}" "${REPO_DIR}/app.py"
chown -R "${OPENCLAW_USER}:${OPENCLAW_USER}" "${REPO_DIR}/generated_dashboards"

cd "${DEPLOY_DIR}"
PROFILE_ARGS=()
if [[ -n "${COMPOSE_PROFILE:-}" ]]; then
  PROFILE_ARGS=(--profile "${COMPOSE_PROFILE}")
fi

docker compose --env-file "${ENV_FILE}" "${PROFILE_ARGS[@]}" up -d --build
