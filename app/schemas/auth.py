from pydantic import BaseModel, EmailStr


class UserContext(BaseModel):
    email: EmailStr | None = None
    role: str = "anonymous"
    is_authenticated: bool = False
