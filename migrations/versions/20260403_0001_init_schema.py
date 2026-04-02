from __future__ import annotations

"""init schema"""

from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision: str = "20260403_0001"
down_revision: str | None = None
branch_labels: Sequence[str] | None = None
depends_on: Sequence[str] | None = None


assumption_type = postgresql.ENUM(
    "problem",
    "solution",
    "pricing",
    "channel",
    "market",
    name="assumptiontype",
    create_type=False,
)
hypothesis_status = postgresql.ENUM(
    "new",
    "queued",
    "testing",
    "signal",
    "validated",
    "invalidated",
    "parked",
    "archived",
    name="hypothesisstatus",
    create_type=False,
)
interview_status = postgresql.ENUM(
    "planned", "completed", "canceled", "no_show", name="interviewstatus", create_type=False
)
insight_type = postgresql.ENUM(
    "pain",
    "job",
    "workaround",
    "willingness_to_pay",
    "objection",
    "buying_process",
    "competitor",
    "other",
    name="insighttype",
    create_type=False,
)
strength_level = postgresql.ENUM("weak", "medium", "strong", name="strengthlevel", create_type=False)
decision_value = postgresql.ENUM(
    "go",
    "iterate",
    "pivot",
    "drop",
    "need_more_evidence",
    name="decisionvalue",
    create_type=False,
)
entity_type = postgresql.ENUM(
    "hypothesis",
    "interview",
    "page",
    "company",
    "contact",
    "competitor",
    "signal",
    name="entitytype",
    create_type=False,
)
relation_type = postgresql.ENUM(
    "direct", "indirect", "alternative", "substitute", name="relationtype", create_type=False
)
source_type = postgresql.ENUM(
    "article", "interview", "report", "news", "internal", name="sourcetype", create_type=False
)
signal_type = postgresql.ENUM(
    "problem_signal",
    "solution_signal",
    "budget_signal",
    "urgency_signal",
    "adoption_signal",
    name="signaltype",
    create_type=False,
)


def upgrade() -> None:
    bind = op.get_bind()
    assumption_type.create(bind, checkfirst=True)
    hypothesis_status.create(bind, checkfirst=True)
    interview_status.create(bind, checkfirst=True)
    insight_type.create(bind, checkfirst=True)
    strength_level.create(bind, checkfirst=True)
    decision_value.create(bind, checkfirst=True)
    entity_type.create(bind, checkfirst=True)
    relation_type.create(bind, checkfirst=True)
    source_type.create(bind, checkfirst=True)
    signal_type.create(bind, checkfirst=True)

    op.create_table(
        "hypotheses",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("segment", sa.String(length=255), nullable=True),
        sa.Column("problem", sa.Text(), nullable=True),
        sa.Column("assumption_type", assumption_type, nullable=False),
        sa.Column("priority", sa.Integer(), nullable=True),
        sa.Column("status", hypothesis_status, nullable=False),
        sa.Column("confidence", sa.Integer(), nullable=True),
        sa.Column("owner_user_id", sa.String(length=36), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
    )

    op.create_table(
        "companies",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("industry", sa.String(length=255), nullable=True),
        sa.Column("size", sa.String(length=255), nullable=True),
        sa.Column("segment", sa.String(length=255), nullable=True),
        sa.Column("website", sa.String(length=500), nullable=True),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
    )
    op.create_index("ix_companies_name", "companies", ["name"])

    op.create_table(
        "contacts",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("full_name", sa.String(length=255), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=True),
        sa.Column("role", sa.String(length=255), nullable=True),
        sa.Column("company_id", sa.String(length=36), sa.ForeignKey("companies.id"), nullable=True),
        sa.Column("segment", sa.String(length=255), nullable=True),
        sa.Column("source", sa.String(length=255), nullable=True),
        sa.Column("business_problem", sa.Text(), nullable=True),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
    )
    op.create_index("ix_contacts_full_name", "contacts", ["full_name"])
    op.create_index("ix_contacts_email", "contacts", ["email"])
    op.create_index("ix_contacts_role", "contacts", ["role"])
    op.create_index("ix_contacts_segment", "contacts", ["segment"])

    op.create_table(
        "competitors",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("segment", sa.String(length=255), nullable=True),
        sa.Column("product_type", sa.String(length=255), nullable=True),
        sa.Column("pricing_model", sa.String(length=255), nullable=True),
        sa.Column("website", sa.String(length=500), nullable=True),
        sa.Column("strengths", sa.Text(), nullable=True),
        sa.Column("weaknesses", sa.Text(), nullable=True),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
    )
    op.create_index("ix_competitors_name", "competitors", ["name"])
    op.create_index("ix_competitors_segment", "competitors", ["segment"])

    op.create_table(
        "interviews",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("contact_id", sa.String(length=36), sa.ForeignKey("contacts.id"), nullable=True),
        sa.Column("company_id", sa.String(length=36), sa.ForeignKey("companies.id"), nullable=True),
        sa.Column("hypothesis_id", sa.String(length=36), sa.ForeignKey("hypotheses.id"), nullable=True),
        sa.Column("scheduled_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("conducted_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("status", interview_status, nullable=False),
        sa.Column("raw_notes", sa.Text(), nullable=True),
        sa.Column("summary", sa.Text(), nullable=True),
        sa.Column("transcript_url", sa.String(length=500), nullable=True),
        sa.Column("recording_url", sa.String(length=500), nullable=True),
        sa.Column("created_by", sa.String(length=255), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
    )

    op.create_table(
        "insights",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("hypothesis_id", sa.String(length=36), sa.ForeignKey("hypotheses.id"), nullable=True),
        sa.Column("interview_id", sa.String(length=36), sa.ForeignKey("interviews.id"), nullable=True),
        sa.Column("type", insight_type, nullable=False),
        sa.Column("quote", sa.Text(), nullable=True),
        sa.Column("summary", sa.Text(), nullable=False),
        sa.Column("strength", strength_level, nullable=False),
        sa.Column("tags", sa.Text(), nullable=True),
        sa.Column("created_by", sa.String(length=255), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
    )

    op.create_table(
        "decisions",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("hypothesis_id", sa.String(length=36), sa.ForeignKey("hypotheses.id"), nullable=False),
        sa.Column("decision", decision_value, nullable=False),
        sa.Column("reason", sa.Text(), nullable=False),
        sa.Column("evidence_count", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("created_by", sa.String(length=255), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
    )

    op.create_table(
        "pages",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("content_md", sa.Text(), nullable=False),
        sa.Column("entity_type", entity_type, nullable=True),
        sa.Column("entity_id", sa.String(length=36), nullable=True),
        sa.Column("tags", sa.Text(), nullable=True),
        sa.Column("created_by", sa.String(length=255), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
    )
    op.create_index("ix_pages_title", "pages", ["title"])
    op.create_index("ix_pages_entity_id", "pages", ["entity_id"])

    op.create_table(
        "attachments",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("entity_type", entity_type, nullable=False),
        sa.Column("entity_id", sa.String(length=36), nullable=False),
        sa.Column("file_name", sa.String(length=255), nullable=False),
        sa.Column("storage_key", sa.String(length=500), nullable=False),
        sa.Column("mime_type", sa.String(length=255), nullable=True),
        sa.Column("size_bytes", sa.Integer(), nullable=True),
        sa.Column("uploaded_by", sa.String(length=255), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
    )
    op.create_index("ix_attachments_entity_id", "attachments", ["entity_id"])

    op.create_table(
        "signals",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("source_type", source_type, nullable=False),
        sa.Column("source_url", sa.String(length=500), nullable=True),
        sa.Column("company_id", sa.String(length=36), sa.ForeignKey("companies.id"), nullable=True),
        sa.Column("competitor_id", sa.String(length=36), sa.ForeignKey("competitors.id"), nullable=True),
        sa.Column("segment", sa.String(length=255), nullable=True),
        sa.Column("signal_type", signal_type, nullable=False),
        sa.Column("strength", strength_level, nullable=False),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
    )
    op.create_index("ix_signals_segment", "signals", ["segment"])

    op.create_table(
        "hypothesis_competitors",
        sa.Column("hypothesis_id", sa.String(length=36), sa.ForeignKey("hypotheses.id"), primary_key=True),
        sa.Column("competitor_id", sa.String(length=36), sa.ForeignKey("competitors.id"), primary_key=True),
        sa.Column("relation_type", relation_type, nullable=False),
    )

    op.create_table(
        "hypothesis_signals",
        sa.Column("hypothesis_id", sa.String(length=36), sa.ForeignKey("hypotheses.id"), primary_key=True),
        sa.Column("signal_id", sa.String(length=36), sa.ForeignKey("signals.id"), primary_key=True),
        sa.Column("relevance_score", sa.Numeric(4, 2), nullable=True),
    )

    op.create_table(
        "allowed_users",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("role", sa.String(length=50), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.text("true")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
    )
    op.create_index("ix_allowed_users_email", "allowed_users", ["email"], unique=True)

    op.create_table(
        "audit_logs",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("actor_email", sa.String(length=255), nullable=True),
        sa.Column("actor_role", sa.String(length=50), nullable=True),
        sa.Column("action", sa.String(length=255), nullable=False),
        sa.Column("entity_type", sa.String(length=50), nullable=False),
        sa.Column("entity_id", sa.String(length=36), nullable=True),
        sa.Column("metadata_json", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
    )
    op.create_index("ix_audit_logs_actor_email", "audit_logs", ["actor_email"])
    op.create_index("ix_audit_logs_entity_id", "audit_logs", ["entity_id"])


def downgrade() -> None:
    op.drop_index("ix_audit_logs_entity_id", table_name="audit_logs")
    op.drop_index("ix_audit_logs_actor_email", table_name="audit_logs")
    op.drop_table("audit_logs")

    op.drop_index("ix_allowed_users_email", table_name="allowed_users")
    op.drop_table("allowed_users")

    op.drop_table("hypothesis_signals")
    op.drop_table("hypothesis_competitors")

    op.drop_index("ix_signals_segment", table_name="signals")
    op.drop_table("signals")

    op.drop_index("ix_attachments_entity_id", table_name="attachments")
    op.drop_table("attachments")

    op.drop_index("ix_pages_entity_id", table_name="pages")
    op.drop_index("ix_pages_title", table_name="pages")
    op.drop_table("pages")

    op.drop_table("decisions")
    op.drop_table("insights")
    op.drop_table("interviews")

    op.drop_index("ix_competitors_segment", table_name="competitors")
    op.drop_index("ix_competitors_name", table_name="competitors")
    op.drop_table("competitors")

    op.drop_index("ix_contacts_segment", table_name="contacts")
    op.drop_index("ix_contacts_role", table_name="contacts")
    op.drop_index("ix_contacts_email", table_name="contacts")
    op.drop_index("ix_contacts_full_name", table_name="contacts")
    op.drop_table("contacts")

    op.drop_index("ix_companies_name", table_name="companies")
    op.drop_table("companies")

    op.drop_table("hypotheses")

    bind = op.get_bind()
    signal_type.drop(bind, checkfirst=True)
    source_type.drop(bind, checkfirst=True)
    relation_type.drop(bind, checkfirst=True)
    entity_type.drop(bind, checkfirst=True)
    decision_value.drop(bind, checkfirst=True)
    strength_level.drop(bind, checkfirst=True)
    insight_type.drop(bind, checkfirst=True)
    interview_status.drop(bind, checkfirst=True)
    hypothesis_status.drop(bind, checkfirst=True)
    assumption_type.drop(bind, checkfirst=True)
