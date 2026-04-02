from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from app.schemas.common import TimestampedUpdatedModel


class CompetitorBase(BaseModel):
    name: str
    description: Optional[str] = None
    segment: Optional[str] = None
    product_type: Optional[str] = None
    pricing_model: Optional[str] = None
    website: Optional[str] = None
    strengths: Optional[str] = None
    weaknesses: Optional[str] = None
    notes: Optional[str] = None


class CompetitorCreate(CompetitorBase):
    pass


class CompetitorRead(TimestampedUpdatedModel, CompetitorBase):
    pass
