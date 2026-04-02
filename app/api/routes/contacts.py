from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db import get_db
from app.models.entities import Contact
from app.schemas.auth import UserContext
from app.schemas.contacts import ContactCreate, ContactRead, ContactUpdate
from app.services.audit import write_audit_log


router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.post("", response_model=ContactRead, status_code=status.HTTP_201_CREATED)
def create_contact(
    payload: ContactCreate,
    db: Session = Depends(get_db),
    user: UserContext = Depends(get_current_user),
) -> Contact:
    record = Contact(**payload.model_dump())
    db.add(record)
    db.commit()
    db.refresh(record)
    write_audit_log(db, "create", "contact", record.id, user.email, user.role, {"full_name": record.full_name})
    return record


@router.get("", response_model=list[ContactRead])
def list_contacts(db: Session = Depends(get_db), _: UserContext = Depends(get_current_user)) -> list[Contact]:
    return list(db.scalars(select(Contact).order_by(Contact.created_at.desc())))


@router.get("/{contact_id}", response_model=ContactRead)
def get_contact(contact_id: str, db: Session = Depends(get_db), _: UserContext = Depends(get_current_user)) -> Contact:
    record = db.get(Contact, contact_id)
    if not record:
        raise HTTPException(status_code=404, detail="Контакт не найден")
    return record


@router.patch("/{contact_id}", response_model=ContactRead)
def update_contact(
    contact_id: str,
    payload: ContactUpdate,
    db: Session = Depends(get_db),
    user: UserContext = Depends(get_current_user),
) -> Contact:
    record = db.get(Contact, contact_id)
    if not record:
        raise HTTPException(status_code=404, detail="Контакт не найден")

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(record, field, value)

    db.add(record)
    db.commit()
    db.refresh(record)
    write_audit_log(db, "update", "contact", record.id, user.email, user.role, payload.model_dump(exclude_unset=True))
    return record
