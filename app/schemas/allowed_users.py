from pydantic import BaseModel, EmailStr

from app.schemas.common import TimestampedModel


class AllowedUserRead(TimestampedModel):
    email: EmailStr
    role: str
    is_active: bool


class AllowedUserCreate(BaseModel):
    email: EmailStr
    role: str = "cofounder"
    is_active: bool = True
