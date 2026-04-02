from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from app.models.enums import EntityType
from app.schemas.common import TimestampedModel


class AttachmentCreate(BaseModel):
    entity_type: EntityType
    entity_id: str
    file_name: str
    storage_key: str
    mime_type: Optional[str] = None
    size_bytes: Optional[int] = None
    uploaded_by: Optional[str] = None


class AttachmentRead(TimestampedModel, AttachmentCreate):
    pass
