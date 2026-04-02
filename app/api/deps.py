from fastapi import Depends, Request
from sqlalchemy.orm import Session

from app.auth.access import resolve_user_context
from app.db import get_db
from app.schemas.auth import UserContext


def get_current_user(
    request: Request,
    db: Session = Depends(get_db),
) -> UserContext:
    return resolve_user_context(request, db)
