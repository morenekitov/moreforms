from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db import get_db
from app.models.entities import Page
from app.schemas.auth import UserContext
from app.schemas.pages import PageCreate, PageRead, PageUpdate
from app.services.audit import write_audit_log


router = APIRouter(prefix="/pages", tags=["pages"])


@router.post("", response_model=PageRead, status_code=status.HTTP_201_CREATED)
def create_page(
    payload: PageCreate,
    db: Session = Depends(get_db),
    user: UserContext = Depends(get_current_user),
) -> Page:
    record = Page(**payload.model_dump())
    db.add(record)
    db.commit()
    db.refresh(record)
    write_audit_log(db, "create", "page", record.id, user.email, user.role)
    return record


@router.get("", response_model=list[PageRead])
def list_pages(db: Session = Depends(get_db), _: UserContext = Depends(get_current_user)) -> list[Page]:
    return list(db.scalars(select(Page).order_by(Page.updated_at.desc())))


@router.get("/{page_id}", response_model=PageRead)
def get_page(page_id: str, db: Session = Depends(get_db), _: UserContext = Depends(get_current_user)) -> Page:
    record = db.get(Page, page_id)
    if not record:
        raise HTTPException(status_code=404, detail="Страница не найдена")
    return record


@router.patch("/{page_id}", response_model=PageRead)
def update_page(
    page_id: str,
    payload: PageUpdate,
    db: Session = Depends(get_db),
    user: UserContext = Depends(get_current_user),
) -> Page:
    record = db.get(Page, page_id)
    if not record:
        raise HTTPException(status_code=404, detail="Страница не найдена")

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(record, field, value)

    db.add(record)
    db.commit()
    db.refresh(record)
    write_audit_log(db, "update", "page", record.id, user.email, user.role, payload.model_dump(exclude_unset=True))
    return record
