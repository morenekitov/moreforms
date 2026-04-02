from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db import get_db
from app.models.entities import Signal
from app.schemas.auth import UserContext
from app.schemas.signals import SignalCreate, SignalRead
from app.services.audit import write_audit_log


router = APIRouter(prefix="/signals", tags=["signals"])


@router.post("", response_model=SignalRead, status_code=status.HTTP_201_CREATED)
def create_signal(
    payload: SignalCreate,
    db: Session = Depends(get_db),
    user: UserContext = Depends(get_current_user),
) -> Signal:
    record = Signal(**payload.model_dump())
    db.add(record)
    db.commit()
    db.refresh(record)
    write_audit_log(db, "create", "signal", record.id, user.email, user.role)
    return record


@router.get("", response_model=list[SignalRead])
def list_signals(db: Session = Depends(get_db), _: UserContext = Depends(get_current_user)) -> list[Signal]:
    return list(db.scalars(select(Signal).order_by(Signal.created_at.desc())))
