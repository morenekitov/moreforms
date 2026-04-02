from __future__ import annotations

from typing import Dict, List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db import get_db
from app.models.entities import AuditLog
from app.schemas.auth import UserContext


router = APIRouter(prefix="/audit-logs", tags=["audit-logs"])


@router.get("")
def list_audit_logs(
    limit: int = 20,
    db: Session = Depends(get_db),
    _: UserContext = Depends(get_current_user),
) -> List[Dict[str, Optional[str]]]:
    rows = list(db.scalars(select(AuditLog).order_by(AuditLog.created_at.desc()).limit(limit)))
    return [
        {
            "id": row.id,
            "action": row.action,
            "entity_type": row.entity_type,
            "entity_id": row.entity_id,
            "actor_email": row.actor_email,
            "created_at": row.created_at.isoformat(),
        }
        for row in rows
    ]
