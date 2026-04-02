from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db import get_db
from app.models.entities import AllowedUser
from app.schemas.auth import UserContext


router = APIRouter(tags=["auth"])


@router.get("/me", response_model=UserContext)
def me(user: UserContext = Depends(get_current_user)) -> UserContext:
    return user


@router.get("/auth/allowed-emails")
def allowed_emails(
    db: Session = Depends(get_db),
    user: UserContext = Depends(get_current_user),
) -> dict[str, list[str]]:
    if user.role != "owner":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Требуется роль owner")
    emails = [row.email for row in db.query(AllowedUser).filter(AllowedUser.is_active.is_(True)).all()]
    return {"emails": emails}
