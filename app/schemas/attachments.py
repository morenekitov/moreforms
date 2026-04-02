from pydantic import BaseModel

from app.models.enums import EntityType
from app.schemas.common import TimestampedModel


class AttachmentCreate(BaseModel):
    entity_type: EntityType
    entity_id: str
    file_name: str
    storage_key: str
    mime_type: str | None = None
    size_bytes: int | None = None
    uploaded_by: str | None = None


class AttachmentRead(TimestampedModel, AttachmentCreate):
    pass
