#!/usr/bin/env bash
set -euo pipefail

BACKUP_DIR="${BACKUP_DIR:-./backups}"
TIMESTAMP="$(date +%Y%m%d-%H%M%S)"
mkdir -p "$BACKUP_DIR"

if [[ -z "${DATABASE_URL:-}" ]]; then
  echo "DATABASE_URL is required"
  exit 1
fi

pg_dump "$DATABASE_URL" > "${BACKUP_DIR}/postgres-${TIMESTAMP}.sql"
echo "Backup saved to ${BACKUP_DIR}/postgres-${TIMESTAMP}.sql"
