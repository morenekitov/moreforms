from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db import get_db
from app.models.entities import Attachment
from app.schemas.attachments import AttachmentCreate, AttachmentRead
from app.schemas.auth import UserContext
from app.services.audit import write_audit_log


router = APIRouter(prefix="/attachments", tags=["attachments"])


@router.post("", response_model=AttachmentRead, status_code=status.HTTP_201_CREATED)
def create_attachment(
    payload: AttachmentCreate,
    db: Session = Depends(get_db),
    user: UserContext = Depends(get_current_user),
) -> Attachment:
    record = Attachment(**payload.model_dump())
    db.add(record)
    db.commit()
    db.refresh(record)
    write_audit_log(db, "create", "attachment", record.id, user.email, user.role)
    return record


@router.get("", response_model=list[AttachmentRead])
def list_attachments(db: Session = Depends(get_db), _: UserContext = Depends(get_current_user)) -> list[Attachment]:
    return list(db.scalars(select(Attachment).order_by(Attachment.created_at.desc())))


@router.get("/{attachment_id}", response_model=AttachmentRead)
def get_attachment(
    attachment_id: str,
    db: Session = Depends(get_db),
    _: UserContext = Depends(get_current_user),
) -> Attachment:
    record = db.get(Attachment, attachment_id)
    if not record:
        raise HTTPException(status_code=404, detail="Вложение не найдено")
    return record
