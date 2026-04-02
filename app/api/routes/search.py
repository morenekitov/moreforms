from fastapi import APIRouter, Depends, Query
from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db import get_db
from app.models.entities import Company, Contact, Hypothesis, Page
from app.schemas.auth import UserContext


router = APIRouter(tags=["search"])


@router.get("/search")
def search(
    q: str = Query(min_length=2),
    db: Session = Depends(get_db),
    _: UserContext = Depends(get_current_user),
) -> dict[str, list[dict[str, str | None]]]:
    pattern = f"%{q}%"
    hypotheses = list(
        db.scalars(
            select(Hypothesis).where(or_(Hypothesis.title.ilike(pattern), Hypothesis.problem.ilike(pattern))).limit(10)
        )
    )
    companies = list(db.scalars(select(Company).where(Company.name.ilike(pattern)).limit(10)))
    contacts = list(
        db.scalars(
            select(Contact).where(or_(Contact.full_name.ilike(pattern), Contact.role.ilike(pattern))).limit(10)
        )
    )
    pages = list(db.scalars(select(Page).where(or_(Page.title.ilike(pattern), Page.content_md.ilike(pattern))).limit(10)))

    return {
        "hypotheses": [{"id": row.id, "title": row.title, "segment": row.segment} for row in hypotheses],
        "companies": [{"id": row.id, "name": row.name, "segment": row.segment} for row in companies],
        "contacts": [{"id": row.id, "full_name": row.full_name, "role": row.role} for row in contacts],
        "pages": [{"id": row.id, "title": row.title, "tags": row.tags} for row in pages],
    }
