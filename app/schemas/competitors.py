from pydantic import BaseModel

from app.schemas.common import TimestampedUpdatedModel


class CompetitorBase(BaseModel):
    name: str
    description: str | None = None
    segment: str | None = None
    product_type: str | None = None
    pricing_model: str | None = None
    website: str | None = None
    strengths: str | None = None
    weaknesses: str | None = None
    notes: str | None = None


class CompetitorCreate(CompetitorBase):
    pass


class CompetitorRead(TimestampedUpdatedModel, CompetitorBase):
    pass
