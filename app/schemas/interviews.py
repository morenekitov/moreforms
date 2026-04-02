from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.models.enums import InterviewStatus
from app.schemas.common import TimestampedUpdatedModel


class InterviewBase(BaseModel):
    contact_id: Optional[str] = None
    company_id: Optional[str] = None
    hypothesis_id: Optional[str] = None
    scheduled_at: Optional[datetime] = None
    conducted_at: Optional[datetime] = None
    status: InterviewStatus = InterviewStatus.planned
    raw_notes: Optional[str] = None
    summary: Optional[str] = None
    transcript_url: Optional[str] = None
    recording_url: Optional[str] = None
    created_by: Optional[str] = None


class InterviewCreate(InterviewBase):
    pass


class InterviewUpdate(BaseModel):
    contact_id: Optional[str] = None
    company_id: Optional[str] = None
    hypothesis_id: Optional[str] = None
    scheduled_at: Optional[datetime] = None
    conducted_at: Optional[datetime] = None
    status: Optional[InterviewStatus] = None
    raw_notes: Optional[str] = None
    summary: Optional[str] = None
    transcript_url: Optional[str] = None
    recording_url: Optional[str] = None


class InterviewRead(TimestampedUpdatedModel, InterviewBase):
    pass
