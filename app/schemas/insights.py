from pydantic import BaseModel

from app.models.enums import InsightType, StrengthLevel
from app.schemas.common import TimestampedUpdatedModel


class InsightBase(BaseModel):
    hypothesis_id: str | None = None
    interview_id: str | None = None
    type: InsightType
    quote: str | None = None
    summary: str
    strength: StrengthLevel = StrengthLevel.medium
    tags: str | None = None
    created_by: str | None = None


class InsightCreate(InsightBase):
    pass


class InsightRead(TimestampedUpdatedModel, InsightBase):
    pass
