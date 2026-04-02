from __future__ import annotations

import json
from typing import Optional

from sqlalchemy.orm import Session

from app.models.entities import AuditLog


def write_audit_log(
    db: Session,
    action: str,
    entity_type: str,
    entity_id: Optional[str],
    actor_email: Optional[str],
    actor_role: Optional[str],
    metadata: Optional[dict] = None,
) -> None:
    entry = AuditLog(
        action=action,
        entity_type=entity_type,
        entity_id=entity_id,
        actor_email=actor_email,
        actor_role=actor_role,
        metadata_json=json.dumps(metadata or {}, ensure_ascii=False),
    )
    db.add(entry)
    db.commit()
