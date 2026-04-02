from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from app.models.enums import EntityType
from app.schemas.common import TimestampedUpdatedModel


class PageBase(BaseModel):
    title: str
    content_md: str
    entity_type: Optional[EntityType] = None
    entity_id: Optional[str] = None
    tags: Optional[str] = None
    created_by: Optional[str] = None


class PageCreate(PageBase):
    pass


class PageUpdate(BaseModel):
    title: Optional[str] = None
    content_md: Optional[str] = None
    entity_type: Optional[EntityType] = None
    entity_id: Optional[str] = None
    tags: Optional[str] = None


class PageRead(TimestampedUpdatedModel, PageBase):
    pass
