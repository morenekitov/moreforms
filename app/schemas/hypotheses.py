from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from app.models.enums import AssumptionType, HypothesisStatus
from app.schemas.common import TimestampedUpdatedModel


class HypothesisBase(BaseModel):
    title: str
    description: Optional[str] = None
    segment: Optional[str] = None
    problem: Optional[str] = None
    assumption_type: AssumptionType
    priority: Optional[int] = None
    status: HypothesisStatus = HypothesisStatus.new
    confidence: Optional[int] = None
    owner_user_id: Optional[str] = None


class HypothesisCreate(HypothesisBase):
    pass


class HypothesisUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    segment: Optional[str] = None
    problem: Optional[str] = None
    assumption_type: Optional[AssumptionType] = None
    priority: Optional[int] = None
    status: Optional[HypothesisStatus] = None
    confidence: Optional[int] = None
    owner_user_id: Optional[str] = None


class HypothesisRead(TimestampedUpdatedModel, HypothesisBase):
    pass
