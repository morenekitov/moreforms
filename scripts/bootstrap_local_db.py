from app.config import get_settings
from app.db import SessionLocal, engine
from app.models import Base
from app.services.bootstrap import bootstrap_allowed_users


def main() -> None:
    settings = get_settings()
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        bootstrap_allowed_users(db, settings)
    finally:
        db.close()
    print("Local database bootstrap completed.")


if __name__ == "__main__":
    main()
