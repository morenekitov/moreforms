from enum import StrEnum


class AssumptionType(StrEnum):
    problem = "problem"
    solution = "solution"
    pricing = "pricing"
    channel = "channel"
    market = "market"


class HypothesisStatus(StrEnum):
    new = "new"
    queued = "queued"
    testing = "testing"
    signal = "signal"
    validated = "validated"
    invalidated = "invalidated"
    parked = "parked"
    archived = "archived"


class InterviewStatus(StrEnum):
    planned = "planned"
    completed = "completed"
    canceled = "canceled"
    no_show = "no_show"


class InsightType(StrEnum):
    pain = "pain"
    job = "job"
    workaround = "workaround"
    willingness_to_pay = "willingness_to_pay"
    objection = "objection"
    buying_process = "buying_process"
    competitor = "competitor"
    other = "other"


class StrengthLevel(StrEnum):
    weak = "weak"
    medium = "medium"
    strong = "strong"


class DecisionValue(StrEnum):
    go = "go"
    iterate = "iterate"
    pivot = "pivot"
    drop = "drop"
    need_more_evidence = "need_more_evidence"


class EntityType(StrEnum):
    hypothesis = "hypothesis"
    interview = "interview"
    page = "page"
    company = "company"
    contact = "contact"
    competitor = "competitor"
    signal = "signal"


class RelationType(StrEnum):
    direct = "direct"
    indirect = "indirect"
    alternative = "alternative"
    substitute = "substitute"


class SourceType(StrEnum):
    article = "article"
    interview = "interview"
    report = "report"
    news = "news"
    internal = "internal"


class SignalType(StrEnum):
    problem_signal = "problem_signal"
    solution_signal = "solution_signal"
    budget_signal = "budget_signal"
    urgency_signal = "urgency_signal"
    adoption_signal = "adoption_signal"
