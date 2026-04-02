#!/usr/bin/env bash
set -euo pipefail

python - <<'PY'
import time

from sqlalchemy import create_engine, text

from app.config import get_settings

settings = get_settings()
engine = create_engine(settings.database_url, future=True)

for attempt in range(60):
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("Database is ready.")
        break
    except Exception as exc:
        if attempt == 59:
            raise
        print(f"Waiting for database: {exc}")
        time.sleep(2)
PY

alembic upgrade head
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
