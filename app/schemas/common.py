from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ORMModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class TimestampedModel(ORMModel):
    id: str
    created_at: datetime


class TimestampedUpdatedModel(TimestampedModel):
    updated_at: datetime


class MessageResponse(BaseModel):
    message: str
