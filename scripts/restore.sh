#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 path/to/backup.sql"
  exit 1
fi

psql "$DATABASE_URL" < "$1"
echo "Restore completed from $1"
