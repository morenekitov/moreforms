from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db import get_db
from app.models.entities import Decision
from app.schemas.auth import UserContext
from app.schemas.decisions import DecisionCreate, DecisionRead
from app.services.audit import write_audit_log


router = APIRouter(tags=["decisions"])


@router.post("/decisions", response_model=DecisionRead, status_code=status.HTTP_201_CREATED)
def create_decision(
    payload: DecisionCreate,
    db: Session = Depends(get_db),
    user: UserContext = Depends(get_current_user),
) -> Decision:
    record = Decision(**payload.model_dump())
    db.add(record)
    db.commit()
    db.refresh(record)
    write_audit_log(db, "create", "decision", record.id, user.email, user.role)
    return record


@router.get("/decisions", response_model=list[DecisionRead])
def list_decisions(db: Session = Depends(get_db), _: UserContext = Depends(get_current_user)) -> list[Decision]:
    return list(db.scalars(select(Decision).order_by(Decision.created_at.desc())))


@router.get("/hypotheses/{hypothesis_id}/decisions", response_model=list[DecisionRead])
def list_hypothesis_decisions(
    hypothesis_id: str,
    db: Session = Depends(get_db),
    _: UserContext = Depends(get_current_user),
) -> list[Decision]:
    return list(
        db.scalars(
            select(Decision).where(Decision.hypothesis_id == hypothesis_id).order_by(Decision.created_at.desc())
        )
    )
