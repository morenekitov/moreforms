import os
import sys
from pathlib import Path


os.environ.setdefault("AUTH_DISABLED", "false")
os.environ.setdefault("ALLOWED_EMAILS", "member@example.com")
os.environ.setdefault("BOOTSTRAP_OWNER_EMAIL", "owner@example.com")
os.environ.setdefault("DATABASE_URL", "sqlite:///./test_runtime.db")
os.environ.setdefault("AUTO_CREATE_SCHEMA", "true")

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
