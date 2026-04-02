from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db import get_db
from app.models.entities import Hypothesis
from app.models.enums import HypothesisStatus
from app.schemas.auth import UserContext
from app.schemas.common import MessageResponse
from app.schemas.hypotheses import HypothesisCreate, HypothesisRead, HypothesisUpdate
from app.services.audit import write_audit_log


router = APIRouter(prefix="/hypotheses", tags=["hypotheses"])


@router.post("", response_model=HypothesisRead, status_code=status.HTTP_201_CREATED)
def create_hypothesis(
    payload: HypothesisCreate,
    db: Session = Depends(get_db),
    user: UserContext = Depends(get_current_user),
) -> Hypothesis:
    record = Hypothesis(**payload.model_dump())
    db.add(record)
    db.commit()
    db.refresh(record)
    write_audit_log(db, "create", "hypothesis", record.id, user.email, user.role, {"title": record.title})
    return record


@router.get("", response_model=list[HypothesisRead])
def list_hypotheses(db: Session = Depends(get_db), _: UserContext = Depends(get_current_user)) -> list[Hypothesis]:
    return list(db.scalars(select(Hypothesis).order_by(Hypothesis.created_at.desc())))


@router.get("/{hypothesis_id}", response_model=HypothesisRead)
def get_hypothesis(
    hypothesis_id: str,
    db: Session = Depends(get_db),
    _: UserContext = Depends(get_current_user),
) -> Hypothesis:
    record = db.get(Hypothesis, hypothesis_id)
    if not record:
        raise HTTPException(status_code=404, detail="Гипотеза не найдена")
    return record


@router.patch("/{hypothesis_id}", response_model=HypothesisRead)
def update_hypothesis(
    hypothesis_id: str,
    payload: HypothesisUpdate,
    db: Session = Depends(get_db),
    user: UserContext = Depends(get_current_user),
) -> Hypothesis:
    record = db.get(Hypothesis, hypothesis_id)
    if not record:
        raise HTTPException(status_code=404, detail="Гипотеза не найдена")

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(record, field, value)

    db.add(record)
    db.commit()
    db.refresh(record)
    write_audit_log(db, "update", "hypothesis", record.id, user.email, user.role, payload.model_dump(exclude_unset=True))
    return record


@router.post("/{hypothesis_id}/archive", response_model=MessageResponse)
def archive_hypothesis(
    hypothesis_id: str,
    db: Session = Depends(get_db),
    user: UserContext = Depends(get_current_user),
) -> MessageResponse:
    record = db.get(Hypothesis, hypothesis_id)
    if not record:
        raise HTTPException(status_code=404, detail="Гипотеза не найдена")

    record.status = HypothesisStatus.archived
    db.add(record)
    db.commit()
    write_audit_log(db, "archive", "hypothesis", record.id, user.email, user.role)
    return MessageResponse(message="Гипотеза архивирована")
