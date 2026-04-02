from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db import get_db
from app.models.entities import Competitor
from app.schemas.auth import UserContext
from app.schemas.competitors import CompetitorCreate, CompetitorRead
from app.services.audit import write_audit_log


router = APIRouter(prefix="/competitors", tags=["competitors"])


@router.post("", response_model=CompetitorRead, status_code=status.HTTP_201_CREATED)
def create_competitor(
    payload: CompetitorCreate,
    db: Session = Depends(get_db),
    user: UserContext = Depends(get_current_user),
) -> Competitor:
    record = Competitor(**payload.model_dump())
    db.add(record)
    db.commit()
    db.refresh(record)
    write_audit_log(db, "create", "competitor", record.id, user.email, user.role)
    return record


@router.get("", response_model=list[CompetitorRead])
def list_competitors(db: Session = Depends(get_db), _: UserContext = Depends(get_current_user)) -> list[Competitor]:
    return list(db.scalars(select(Competitor).order_by(Competitor.created_at.desc())))
