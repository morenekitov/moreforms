from pydantic import BaseModel

from app.models.enums import SignalType, SourceType, StrengthLevel
from app.schemas.common import TimestampedModel


class SignalBase(BaseModel):
    title: str
    description: str | None = None
    source_type: SourceType
    source_url: str | None = None
    company_id: str | None = None
    competitor_id: str | None = None
    segment: str | None = None
    signal_type: SignalType
    strength: StrengthLevel = StrengthLevel.medium
    notes: str | None = None


class SignalCreate(SignalBase):
    pass


class SignalRead(TimestampedModel, SignalBase):
    pass
