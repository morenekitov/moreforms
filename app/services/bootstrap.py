from sqlalchemy import select
from sqlalchemy.orm import Session

from app.config import Settings
from app.models.entities import AllowedUser


def bootstrap_allowed_users(db: Session, settings: Settings) -> None:
    emails = set(settings.allowed_email_set)
    if settings.bootstrap_owner_email.strip():
        emails.add(settings.bootstrap_owner_email.strip().lower())

    if not emails:
        return

    existing = {
        row.email.lower(): row
        for row in db.scalars(select(AllowedUser).where(AllowedUser.email.in_(emails)))
    }

    changed = False
    for email in emails:
        if email in existing:
            if not existing[email].is_active:
                existing[email].is_active = True
                changed = True
            continue

        role = "owner" if email == settings.bootstrap_owner_email.strip().lower() else "cofounder"
        db.add(AllowedUser(email=email, role=role, is_active=True))
        changed = True

    if changed:
        db.commit()
