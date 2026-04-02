import uuid
from datetime import datetime

from sqlalchemy import DateTime, Enum, ForeignKey, Integer, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.models.enums import (
    AssumptionType,
    DecisionValue,
    EntityType,
    HypothesisStatus,
    InsightType,
    InterviewStatus,
    RelationType,
    SignalType,
    SourceType,
    StrengthLevel,
)


def uuid_str() -> str:
    return str(uuid.uuid4())


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )


class Hypothesis(Base, TimestampMixin):
    __tablename__ = "hypotheses"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=uuid_str)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text())
    segment: Mapped[str | None] = mapped_column(String(255))
    problem: Mapped[str | None] = mapped_column(Text())
    assumption_type: Mapped[AssumptionType] = mapped_column(Enum(AssumptionType), nullable=False)
    priority: Mapped[int | None] = mapped_column(Integer())
    status: Mapped[HypothesisStatus] = mapped_column(Enum(HypothesisStatus), default=HypothesisStatus.new, nullable=False)
    confidence: Mapped[int | None] = mapped_column(Integer())
    owner_user_id: Mapped[str | None] = mapped_column(String(36))

    interviews = relationship("Interview", back_populates="hypothesis")
    insights = relationship("Insight", back_populates="hypothesis")
    decisions = relationship("Decision", back_populates="hypothesis")


class Company(Base, TimestampMixin):
    __tablename__ = "companies"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=uuid_str)
    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    industry: Mapped[str | None] = mapped_column(String(255))
    size: Mapped[str | None] = mapped_column(String(255))
    segment: Mapped[str | None] = mapped_column(String(255))
    website: Mapped[str | None] = mapped_column(String(500))
    notes: Mapped[str | None] = mapped_column(Text())

    contacts = relationship("Contact", back_populates="company")
    interviews = relationship("Interview", back_populates="company")
    signals = relationship("Signal", back_populates="company")


class Contact(Base, TimestampMixin):
    __tablename__ = "contacts"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=uuid_str)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    email: Mapped[str | None] = mapped_column(String(255), index=True)
    role: Mapped[str | None] = mapped_column(String(255), index=True)
    company_id: Mapped[str | None] = mapped_column(ForeignKey("companies.id"))
    segment: Mapped[str | None] = mapped_column(String(255), index=True)
    source: Mapped[str | None] = mapped_column(String(255))
    business_problem: Mapped[str | None] = mapped_column(Text())
    notes: Mapped[str | None] = mapped_column(Text())

    company = relationship("Company", back_populates="contacts")
    interviews = relationship("Interview", back_populates="contact")


class Interview(Base, TimestampMixin):
    __tablename__ = "interviews"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=uuid_str)
    contact_id: Mapped[str | None] = mapped_column(ForeignKey("contacts.id"))
    company_id: Mapped[str | None] = mapped_column(ForeignKey("companies.id"))
    hypothesis_id: Mapped[str | None] = mapped_column(ForeignKey("hypotheses.id"))
    scheduled_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    conducted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    status: Mapped[InterviewStatus] = mapped_column(Enum(InterviewStatus), default=InterviewStatus.planned, nullable=False)
    raw_notes: Mapped[str | None] = mapped_column(Text())
    summary: Mapped[str | None] = mapped_column(Text())
    transcript_url: Mapped[str | None] = mapped_column(String(500))
    recording_url: Mapped[str | None] = mapped_column(String(500))
    created_by: Mapped[str | None] = mapped_column(String(255))

    contact = relationship("Contact", back_populates="interviews")
    company = relationship("Company", back_populates="interviews")
    hypothesis = relationship("Hypothesis", back_populates="interviews")
    insights = relationship("Insight", back_populates="interview")


class Insight(Base, TimestampMixin):
    __tablename__ = "insights"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=uuid_str)
    hypothesis_id: Mapped[str | None] = mapped_column(ForeignKey("hypotheses.id"))
    interview_id: Mapped[str | None] = mapped_column(ForeignKey("interviews.id"))
    type: Mapped[InsightType] = mapped_column(Enum(InsightType), nullable=False)
    quote: Mapped[str | None] = mapped_column(Text())
    summary: Mapped[str] = mapped_column(Text(), nullable=False)
    strength: Mapped[StrengthLevel] = mapped_column(Enum(StrengthLevel), default=StrengthLevel.medium, nullable=False)
    tags: Mapped[str | None] = mapped_column(Text())
    created_by: Mapped[str | None] = mapped_column(String(255))

    hypothesis = relationship("Hypothesis", back_populates="insights")
    interview = relationship("Interview", back_populates="insights")


class Decision(Base):
    __tablename__ = "decisions"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=uuid_str)
    hypothesis_id: Mapped[str] = mapped_column(ForeignKey("hypotheses.id"), nullable=False)
    decision: Mapped[DecisionValue] = mapped_column(Enum(DecisionValue), nullable=False)
    reason: Mapped[str] = mapped_column(Text(), nullable=False)
    evidence_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    created_by: Mapped[str | None] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    hypothesis = relationship("Hypothesis", back_populates="decisions")


class Page(Base, TimestampMixin):
    __tablename__ = "pages"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=uuid_str)
    title: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    content_md: Mapped[str] = mapped_column(Text(), nullable=False)
    entity_type: Mapped[EntityType | None] = mapped_column(Enum(EntityType))
    entity_id: Mapped[str | None] = mapped_column(String(36), index=True)
    tags: Mapped[str | None] = mapped_column(Text())
    created_by: Mapped[str | None] = mapped_column(String(255))


class Attachment(Base):
    __tablename__ = "attachments"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=uuid_str)
    entity_type: Mapped[EntityType] = mapped_column(Enum(EntityType), nullable=False)
    entity_id: Mapped[str] = mapped_column(String(36), nullable=False, index=True)
    file_name: Mapped[str] = mapped_column(String(255), nullable=False)
    storage_key: Mapped[str] = mapped_column(String(500), nullable=False)
    mime_type: Mapped[str | None] = mapped_column(String(255))
    size_bytes: Mapped[int | None] = mapped_column(Integer())
    uploaded_by: Mapped[str | None] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)


class Competitor(Base, TimestampMixin):
    __tablename__ = "competitors"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=uuid_str)
    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(Text())
    segment: Mapped[str | None] = mapped_column(String(255), index=True)
    product_type: Mapped[str | None] = mapped_column(String(255))
    pricing_model: Mapped[str | None] = mapped_column(String(255))
    website: Mapped[str | None] = mapped_column(String(500))
    strengths: Mapped[str | None] = mapped_column(Text())
    weaknesses: Mapped[str | None] = mapped_column(Text())
    notes: Mapped[str | None] = mapped_column(Text())

    signals = relationship("Signal", back_populates="competitor")


class Signal(Base):
    __tablename__ = "signals"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=uuid_str)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text())
    source_type: Mapped[SourceType] = mapped_column(Enum(SourceType), nullable=False)
    source_url: Mapped[str | None] = mapped_column(String(500))
    company_id: Mapped[str | None] = mapped_column(ForeignKey("companies.id"))
    competitor_id: Mapped[str | None] = mapped_column(ForeignKey("competitors.id"))
    segment: Mapped[str | None] = mapped_column(String(255), index=True)
    signal_type: Mapped[SignalType] = mapped_column(Enum(SignalType), nullable=False)
    strength: Mapped[StrengthLevel] = mapped_column(Enum(StrengthLevel), default=StrengthLevel.medium, nullable=False)
    notes: Mapped[str | None] = mapped_column(Text())
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    company = relationship("Company", back_populates="signals")
    competitor = relationship("Competitor", back_populates="signals")


class HypothesisCompetitor(Base):
    __tablename__ = "hypothesis_competitors"

    hypothesis_id: Mapped[str] = mapped_column(ForeignKey("hypotheses.id"), primary_key=True)
    competitor_id: Mapped[str] = mapped_column(ForeignKey("competitors.id"), primary_key=True)
    relation_type: Mapped[RelationType] = mapped_column(Enum(RelationType), nullable=False)


class HypothesisSignal(Base):
    __tablename__ = "hypothesis_signals"

    hypothesis_id: Mapped[str] = mapped_column(ForeignKey("hypotheses.id"), primary_key=True)
    signal_id: Mapped[str] = mapped_column(ForeignKey("signals.id"), primary_key=True)
    relevance_score: Mapped[float | None] = mapped_column(Numeric(4, 2))


class AllowedUser(Base):
    __tablename__ = "allowed_users"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=uuid_str)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)
    role: Mapped[str] = mapped_column(String(50), default="cofounder", nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=uuid_str)
    actor_email: Mapped[str | None] = mapped_column(String(255), index=True)
    actor_role: Mapped[str | None] = mapped_column(String(50))
    action: Mapped[str] = mapped_column(String(255), nullable=False)
    entity_type: Mapped[str] = mapped_column(String(50), nullable=False)
    entity_id: Mapped[str | None] = mapped_column(String(36), index=True)
    metadata_json: Mapped[str | None] = mapped_column(Text())
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
