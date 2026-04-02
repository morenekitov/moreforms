from fastapi import APIRouter, Depends
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db import get_db
from app.models.entities import AuditLog, Hypothesis, Insight, Interview, Signal
from app.models.enums import HypothesisStatus
from app.schemas.auth import UserContext


router = APIRouter(prefix="/overview", tags=["overview"])


@router.get("")
def overview(
    db: Session = Depends(get_db),
    _: UserContext = Depends(get_current_user),
) -> dict:
    hypothesis_count = db.scalar(select(func.count()).select_from(Hypothesis)) or 0
    interview_count = db.scalar(select(func.count()).select_from(Interview)) or 0
    insight_count = db.scalar(select(func.count()).select_from(Insight)) or 0
    signal_count = db.scalar(select(func.count()).select_from(Signal)) or 0

    status_rows = db.execute(
        select(Hypothesis.status, func.count()).group_by(Hypothesis.status).order_by(Hypothesis.status)
    ).all()
    latest_changes = list(db.scalars(select(AuditLog).order_by(AuditLog.created_at.desc()).limit(10)))
    pending_decision = list(
        db.scalars(
            select(Hypothesis)
            .where(Hypothesis.status.in_([HypothesisStatus.new, HypothesisStatus.queued, HypothesisStatus.signal]))
            .order_by(Hypothesis.updated_at.desc())
            .limit(10)
        )
    )

    return {
        "hypotheses_total": hypothesis_count,
        "interviews_total": interview_count,
        "insights_total": insight_count,
        "signals_total": signal_count,
        "hypotheses_by_status": [{"status": str(status), "count": count} for status, count in status_rows],
        "latest_changes": [
            {
                "action": row.action,
                "entity_type": row.entity_type,
                "entity_id": row.entity_id,
                "actor_email": row.actor_email,
                "created_at": row.created_at.isoformat(),
            }
            for row in latest_changes
        ],
        "hypotheses_requiring_decision": [
            {"id": row.id, "title": row.title, "status": str(row.status), "segment": row.segment}
            for row in pending_decision
        ],
    }
