from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db import get_db
from app.models.entities import Interview
from app.schemas.auth import UserContext
from app.schemas.interviews import InterviewCreate, InterviewRead, InterviewUpdate
from app.services.audit import write_audit_log


router = APIRouter(prefix="/interviews", tags=["interviews"])


@router.post("", response_model=InterviewRead, status_code=status.HTTP_201_CREATED)
def create_interview(
    payload: InterviewCreate,
    db: Session = Depends(get_db),
    user: UserContext = Depends(get_current_user),
) -> Interview:
    record = Interview(**payload.model_dump())
    db.add(record)
    db.commit()
    db.refresh(record)
    write_audit_log(db, "create", "interview", record.id, user.email, user.role)
    return record


@router.get("", response_model=list[InterviewRead])
def list_interviews(db: Session = Depends(get_db), _: UserContext = Depends(get_current_user)) -> list[Interview]:
    return list(db.scalars(select(Interview).order_by(Interview.created_at.desc())))


@router.get("/{interview_id}", response_model=InterviewRead)
def get_interview(
    interview_id: str,
    db: Session = Depends(get_db),
    _: UserContext = Depends(get_current_user),
) -> Interview:
    record = db.get(Interview, interview_id)
    if not record:
        raise HTTPException(status_code=404, detail="Интервью не найдено")
    return record


@router.patch("/{interview_id}", response_model=InterviewRead)
def update_interview(
    interview_id: str,
    payload: InterviewUpdate,
    db: Session = Depends(get_db),
    user: UserContext = Depends(get_current_user),
) -> Interview:
    record = db.get(Interview, interview_id)
    if not record:
        raise HTTPException(status_code=404, detail="Интервью не найдено")

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(record, field, value)

    db.add(record)
    db.commit()
    db.refresh(record)
    write_audit_log(db, "update", "interview", record.id, user.email, user.role, payload.model_dump(exclude_unset=True))
    return record
