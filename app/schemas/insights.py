from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from app.models.enums import InsightType, StrengthLevel
from app.schemas.common import TimestampedUpdatedModel


class InsightBase(BaseModel):
    hypothesis_id: Optional[str] = None
    interview_id: Optional[str] = None
    type: InsightType
    quote: Optional[str] = None
    summary: str
    strength: StrengthLevel = StrengthLevel.medium
    tags: Optional[str] = None
    created_by: Optional[str] = None


class InsightCreate(InsightBase):
    pass


class InsightRead(TimestampedUpdatedModel, InsightBase):
    pass
