#!/usr/bin/env bash
set -euo pipefail

BACKUP_DIR="${BACKUP_DIR:-./backups}"
TIMESTAMP="$(date +%Y%m%d-%H%M%S)"
mkdir -p "$BACKUP_DIR"

pg_dump "$DATABASE_URL" > "${BACKUP_DIR}/postgres-${TIMESTAMP}.sql"
echo "Backup saved to ${BACKUP_DIR}/postgres-${TIMESTAMP}.sql"
