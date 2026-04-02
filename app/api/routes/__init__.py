from app.api.routes.attachments import router as attachments_router
from app.api.routes.auth import router as auth_router
from app.api.routes.companies import router as companies_router
from app.api.routes.competitors import router as competitors_router
from app.api.routes.contacts import router as contacts_router
from app.api.routes.decisions import router as decisions_router
from app.api.routes.health import router as health_router
from app.api.routes.hypotheses import router as hypotheses_router
from app.api.routes.insights import router as insights_router
from app.api.routes.interviews import router as interviews_router
from app.api.routes.pages import router as pages_router
from app.api.routes.search import router as search_router
from app.api.routes.signals import router as signals_router

all_routers = [
    health_router,
    auth_router,
    hypotheses_router,
    companies_router,
    contacts_router,
    interviews_router,
    insights_router,
    decisions_router,
    pages_router,
    attachments_router,
    competitors_router,
    signals_router,
    search_router,
]
