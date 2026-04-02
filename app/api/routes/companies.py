from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db import get_db
from app.models.entities import Company
from app.schemas.auth import UserContext
from app.schemas.companies import CompanyCreate, CompanyRead, CompanyUpdate
from app.services.audit import write_audit_log


router = APIRouter(prefix="/companies", tags=["companies"])


@router.post("", response_model=CompanyRead, status_code=status.HTTP_201_CREATED)
def create_company(
    payload: CompanyCreate,
    db: Session = Depends(get_db),
    user: UserContext = Depends(get_current_user),
) -> Company:
    record = Company(**payload.model_dump())
    db.add(record)
    db.commit()
    db.refresh(record)
    write_audit_log(db, "create", "company", record.id, user.email, user.role, {"name": record.name})
    return record


@router.get("", response_model=list[CompanyRead])
def list_companies(db: Session = Depends(get_db), _: UserContext = Depends(get_current_user)) -> list[Company]:
    return list(db.scalars(select(Company).order_by(Company.created_at.desc())))


@router.patch("/{company_id}", response_model=CompanyRead)
def update_company(
    company_id: str,
    payload: CompanyUpdate,
    db: Session = Depends(get_db),
    user: UserContext = Depends(get_current_user),
) -> Company:
    record = db.get(Company, company_id)
    if not record:
        raise HTTPException(status_code=404, detail="Компания не найдена")

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(record, field, value)

    db.add(record)
    db.commit()
    db.refresh(record)
    write_audit_log(db, "update", "company", record.id, user.email, user.role, payload.model_dump(exclude_unset=True))
    return record
