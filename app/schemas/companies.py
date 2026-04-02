from pydantic import BaseModel

from app.schemas.common import TimestampedUpdatedModel


class CompanyBase(BaseModel):
    name: str
    industry: str | None = None
    size: str | None = None
    segment: str | None = None
    website: str | None = None
    notes: str | None = None


class CompanyCreate(CompanyBase):
    pass


class CompanyUpdate(BaseModel):
    name: str | None = None
    industry: str | None = None
    size: str | None = None
    segment: str | None = None
    website: str | None = None
    notes: str | None = None


class CompanyRead(TimestampedUpdatedModel, CompanyBase):
    pass
