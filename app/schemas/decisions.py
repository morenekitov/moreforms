from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from app.models.enums import DecisionValue
from app.schemas.common import TimestampedModel


class DecisionBase(BaseModel):
    hypothesis_id: str
    decision: DecisionValue
    reason: str
    evidence_count: int = 0
    created_by: Optional[str] = None


class DecisionCreate(DecisionBase):
    pass


class DecisionRead(TimestampedModel, DecisionBase):
    pass
