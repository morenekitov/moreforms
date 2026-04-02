from fastapi import APIRouter, Depends

from app.api.deps import get_current_user
from app.schemas.auth import UserContext


router = APIRouter(tags=["auth"])


@router.get("/me", response_model=UserContext)
def me(user: UserContext = Depends(get_current_user)) -> UserContext:
    return user
