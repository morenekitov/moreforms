from pydantic import BaseModel

from app.models.enums import EntityType
from app.schemas.common import TimestampedUpdatedModel


class PageBase(BaseModel):
    title: str
    content_md: str
    entity_type: EntityType | None = None
    entity_id: str | None = None
    tags: str | None = None
    created_by: str | None = None


class PageCreate(PageBase):
    pass


class PageUpdate(BaseModel):
    title: str | None = None
    content_md: str | None = None
    entity_type: EntityType | None = None
    entity_id: str | None = None
    tags: str | None = None


class PageRead(TimestampedUpdatedModel, PageBase):
    pass
