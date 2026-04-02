# AGENTS.md

## Project purpose

This project is an internal startup discovery system for:

- hypotheses tracking
- customer development interviews
- insights extraction
- decisions by hypothesis
- competitor and market signal tracking
- research notes / wiki
- Streamlit-based dashboard for founders

The system is not a generic CRM.  
Its main workflow is:

`hypothesis -> interview -> insight -> decision`

Additional validation loop:

`hypothesis <-> competitors <-> signals`

## Interaction model

The system is designed with a strict separation:

- `READ` -> Streamlit dashboard
- `WRITE` -> Codex / agent interface

Users should not manually input most structured data via UI.

Instead:

- users provide raw inputs such as links, transcripts, notes and source materials;
- agent processes inputs;
- agent structures and writes data via backend APIs.

## Preferred stack

- Python
- FastAPI
- PostgreSQL
- Streamlit
- Docker Compose

## Core entities

- hypotheses
- companies
- contacts
- interviews
- insights
- decisions
- pages
- attachments
- competitors
- signals
- allowed_users
- audit_logs

## Current development stage

Repository is moving from a legacy CSV-based workspace to v1 backend-first architecture.

Primary implementation targets now:

1. data model
2. backend API
3. auth and access control
4. Streamlit read-layer
5. agent-safe write paths

## Business rules

### Hypotheses

Allowed statuses:

- `new`
- `queued`
- `testing`
- `signal`
- `validated`
- `invalidated`
- `parked`
- `archived`

Allowed assumption types:

- `problem`
- `solution`
- `pricing`
- `channel`
- `market`

### Interviews

Each interview should ideally be linked to:

- one contact
- optionally one company
- one primary hypothesis

### Insights

Each insight must be linked to:

- one hypothesis
- optionally one interview

Allowed types:

- `pain`
- `job`
- `workaround`
- `willingness_to_pay`
- `objection`
- `buying_process`
- `competitor`
- `other`

### Decisions

Decisions are tied to a hypothesis and represent explicit conclusion:

- `go`
- `iterate`
- `pivot`
- `drop`
- `need_more_evidence`

### Signals

Signals represent evidence that a problem, solution, budget or adoption pattern exists on the market.

Allowed signal types:

- `problem_signal`
- `solution_signal`
- `budget_signal`
- `urgency_signal`
- `adoption_signal`

## Streamlit requirements

Streamlit is a read-oriented dashboard.  
It should visualize:

- overview
- hypotheses
- interviews
- insights
- signals
- competitors
- decisions
- wiki / notes

The UI should be in Russian where possible.

Do not turn Streamlit into the main write interface.

## Agent safety rules

Agents must not have unrestricted direct write access to production DB.

Preferred write path:

- validated backend APIs
- tool-like endpoints
- service account with limited scope

Agents may:

- read structured data
- create draft hypotheses
- add interview summaries
- add insights
- create draft wiki pages
- create competitors and signals
- run search and synthesis tasks

Agents must not without explicit approval:

- delete records
- bulk edit records
- mark hypotheses as `validated` or `invalidated`
- alter allowed users / auth configuration
- modify production secrets

## Coding rules

- Keep code modular.
- Use migrations.
- Use typed schemas and explicit validation.
- No secrets in repository.
- Maintain `.env.example`.
- Add tests for core business logic.
- Keep deployment simple.
- Prefer readability over premature abstraction.

## Deployment target

Single-server deployment is acceptable for v1:

- reverse proxy
- backend
- postgres
- streamlit
- backup job

Use Docker Compose.

## Git rule

After file changes:

1. make the smallest coherent implementation slice;
2. run available checks;
3. commit;
4. push to `main`, unless user explicitly asks otherwise.
