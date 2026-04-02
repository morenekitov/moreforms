from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db import get_db
from app.models.entities import Insight
from app.schemas.auth import UserContext
from app.schemas.insights import InsightCreate, InsightRead
from app.services.audit import write_audit_log


router = APIRouter(tags=["insights"])


@router.post("/insights", response_model=InsightRead, status_code=status.HTTP_201_CREATED)
def create_insight(
    payload: InsightCreate,
    db: Session = Depends(get_db),
    user: UserContext = Depends(get_current_user),
) -> Insight:
    record = Insight(**payload.model_dump())
    db.add(record)
    db.commit()
    db.refresh(record)
    write_audit_log(db, "create", "insight", record.id, user.email, user.role)
    return record


@router.get("/insights", response_model=list[InsightRead])
def list_insights(db: Session = Depends(get_db), _: UserContext = Depends(get_current_user)) -> list[Insight]:
    return list(db.scalars(select(Insight).order_by(Insight.created_at.desc())))


@router.get("/hypotheses/{hypothesis_id}/insights", response_model=list[InsightRead])
def list_hypothesis_insights(
    hypothesis_id: str,
    db: Session = Depends(get_db),
    _: UserContext = Depends(get_current_user),
) -> list[Insight]:
    return list(
        db.scalars(
            select(Insight).where(Insight.hypothesis_id == hypothesis_id).order_by(Insight.created_at.desc())
        )
    )
