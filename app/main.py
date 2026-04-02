from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes import all_routers
from app.config import get_settings
from app.db import SessionLocal, engine
from app.models import Base
from app.services.bootstrap import bootstrap_allowed_users


@asynccontextmanager
async def lifespan(_: FastAPI):
    settings = get_settings()
    if settings.auto_create_schema:
        Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        bootstrap_allowed_users(db, settings)
    finally:
        db.close()
    yield


app = FastAPI(
    title="moreforms API",
    version="0.1.0",
    lifespan=lifespan,
)

for router in all_routers:
    app.include_router(router)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": "moreforms API v1",
        "docs": "/docs",
        "health": "/health",
    }
