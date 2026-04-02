from pydantic import BaseModel, EmailStr

from app.schemas.common import TimestampedUpdatedModel


class ContactBase(BaseModel):
    full_name: str
    email: EmailStr | None = None
    role: str | None = None
    company_id: str | None = None
    segment: str | None = None
    source: str | None = None
    business_problem: str | None = None
    notes: str | None = None


class ContactCreate(ContactBase):
    pass


class ContactUpdate(BaseModel):
    full_name: str | None = None
    email: EmailStr | None = None
    role: str | None = None
    company_id: str | None = None
    segment: str | None = None
    source: str | None = None
    business_problem: str | None = None
    notes: str | None = None


class ContactRead(TimestampedUpdatedModel, ContactBase):
    pass
