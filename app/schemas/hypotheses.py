from pydantic import BaseModel

from app.models.enums import AssumptionType, HypothesisStatus
from app.schemas.common import TimestampedUpdatedModel


class HypothesisBase(BaseModel):
    title: str
    description: str | None = None
    segment: str | None = None
    problem: str | None = None
    assumption_type: AssumptionType
    priority: int | None = None
    status: HypothesisStatus = HypothesisStatus.new
    confidence: int | None = None
    owner_user_id: str | None = None


class HypothesisCreate(HypothesisBase):
    pass


class HypothesisUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    segment: str | None = None
    problem: str | None = None
    assumption_type: AssumptionType | None = None
    priority: int | None = None
    status: HypothesisStatus | None = None
    confidence: int | None = None
    owner_user_id: str | None = None


class HypothesisRead(TimestampedUpdatedModel, HypothesisBase):
    pass
