import json

from sqlalchemy.orm import Session

from app.models.entities import AuditLog


def write_audit_log(
    db: Session,
    action: str,
    entity_type: str,
    entity_id: str | None,
    actor_email: str | None,
    actor_role: str | None,
    metadata: dict | None = None,
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
