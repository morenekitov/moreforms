from __future__ import annotations

from fastapi import HTTPException, Request, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.config import get_settings
from app.models.entities import AllowedUser
from app.schemas.auth import UserContext


def extract_request_email(request: Request) -> str | None:
    for header in (
        "x-auth-request-email",
        "x-forwarded-email",
        "x-user-email",
        "x-email",
    ):
        value = request.headers.get(header)
        if value:
            return value.strip().lower()
    return None


def resolve_user_context(request: Request, db: Session) -> UserContext:
    settings = get_settings()

    if settings.auth_disabled:
        email = extract_request_email(request)
        return UserContext(email=email, role="owner", is_authenticated=True)

    email = extract_request_email(request)
    if not email:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Не удалось определить email пользователя")

    allowed_user = db.scalar(
        select(AllowedUser).where(
            AllowedUser.email == email,
            AllowedUser.is_active.is_(True),
        )
    )
    if not allowed_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Доступ запрещен для этого email")

    role = allowed_user.role
    return UserContext(email=email, role=role, is_authenticated=True)
