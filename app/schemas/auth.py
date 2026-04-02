from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, EmailStr


class UserContext(BaseModel):
    email: Optional[EmailStr] = None
    role: str = "anonymous"
    is_authenticated: bool = False
