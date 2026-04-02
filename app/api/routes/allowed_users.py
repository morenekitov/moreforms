from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db import get_db
from app.models.entities import AllowedUser
from app.schemas.allowed_users import AllowedUserCreate, AllowedUserRead
from app.schemas.auth import UserContext
from app.services.audit import write_audit_log


router = APIRouter(prefix="/allowed-users", tags=["allowed-users"])


def _require_owner(user: UserContext) -> None:
    if user.role != "owner":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Требуется роль owner")


@router.get("", response_model=list[AllowedUserRead])
def list_allowed_users(
    db: Session = Depends(get_db),
    user: UserContext = Depends(get_current_user),
) -> list[AllowedUser]:
    _require_owner(user)
    return list(db.scalars(select(AllowedUser).order_by(AllowedUser.created_at.desc())))


@router.post("", response_model=AllowedUserRead, status_code=status.HTTP_201_CREATED)
def create_allowed_user(
    payload: AllowedUserCreate,
    db: Session = Depends(get_db),
    user: UserContext = Depends(get_current_user),
) -> AllowedUser:
    _require_owner(user)
    record = AllowedUser(email=str(payload.email).lower(), role=payload.role, is_active=payload.is_active)
    db.add(record)
    db.commit()
    db.refresh(record)
    write_audit_log(db, "create", "allowed_user", record.id, user.email, user.role, {"email": record.email})
    return record
