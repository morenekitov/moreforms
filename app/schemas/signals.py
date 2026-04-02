from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from app.models.enums import SignalType, SourceType, StrengthLevel
from app.schemas.common import TimestampedModel


class SignalBase(BaseModel):
    title: str
    description: Optional[str] = None
    source_type: SourceType
    source_url: Optional[str] = None
    company_id: Optional[str] = None
    competitor_id: Optional[str] = None
    segment: Optional[str] = None
    signal_type: SignalType
    strength: StrengthLevel = StrengthLevel.medium
    notes: Optional[str] = None


class SignalCreate(SignalBase):
    pass


class SignalRead(TimestampedModel, SignalBase):
    pass
