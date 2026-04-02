from datetime import datetime

from pydantic import BaseModel

from app.models.enums import InterviewStatus
from app.schemas.common import TimestampedUpdatedModel


class InterviewBase(BaseModel):
    contact_id: str | None = None
    company_id: str | None = None
    hypothesis_id: str | None = None
    scheduled_at: datetime | None = None
    conducted_at: datetime | None = None
    status: InterviewStatus = InterviewStatus.planned
    raw_notes: str | None = None
    summary: str | None = None
    transcript_url: str | None = None
    recording_url: str | None = None
    created_by: str | None = None


class InterviewCreate(InterviewBase):
    pass


class InterviewUpdate(BaseModel):
    contact_id: str | None = None
    company_id: str | None = None
    hypothesis_id: str | None = None
    scheduled_at: datetime | None = None
    conducted_at: datetime | None = None
    status: InterviewStatus | None = None
    raw_notes: str | None = None
    summary: str | None = None
    transcript_url: str | None = None
    recording_url: str | None = None


class InterviewRead(TimestampedUpdatedModel, InterviewBase):
    pass
