#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="${REPO_DIR:-/srv/moreforms/deploy/repo}"
ENV_FILE="${ENV_FILE:-/srv/moreforms/runtime/.env}"
DEPLOY_DIR="${REPO_DIR}/deploy"

cd "${REPO_DIR}"
git fetch origin
git checkout main
git pull --ff-only origin main

cd "${DEPLOY_DIR}"
PROFILE_ARGS=()
if [[ -n "${COMPOSE_PROFILE:-}" ]]; then
  PROFILE_ARGS=(--profile "${COMPOSE_PROFILE}")
fi

docker compose --env-file "${ENV_FILE}" "${PROFILE_ARGS[@]}" up -d --build
