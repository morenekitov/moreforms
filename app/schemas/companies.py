from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from app.schemas.common import TimestampedUpdatedModel


class CompanyBase(BaseModel):
    name: str
    industry: Optional[str] = None
    size: Optional[str] = None
    segment: Optional[str] = None
    website: Optional[str] = None
    notes: Optional[str] = None


class CompanyCreate(CompanyBase):
    pass


class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    industry: Optional[str] = None
    size: Optional[str] = None
    segment: Optional[str] = None
    website: Optional[str] = None
    notes: Optional[str] = None


class CompanyRead(TimestampedUpdatedModel, CompanyBase):
    pass
