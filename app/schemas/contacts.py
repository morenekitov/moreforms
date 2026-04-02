from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, EmailStr

from app.schemas.common import TimestampedUpdatedModel


class ContactBase(BaseModel):
    full_name: str
    email: Optional[EmailStr] = None
    role: Optional[str] = None
    company_id: Optional[str] = None
    segment: Optional[str] = None
    source: Optional[str] = None
    business_problem: Optional[str] = None
    notes: Optional[str] = None


class ContactCreate(ContactBase):
    pass


class ContactUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[str] = None
    company_id: Optional[str] = None
    segment: Optional[str] = None
    source: Optional[str] = None
    business_problem: Optional[str] = None
    notes: Optional[str] = None


class ContactRead(TimestampedUpdatedModel, ContactBase):
    pass
