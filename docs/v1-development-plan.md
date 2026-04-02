# План разработки v1

## Контекст

`moreforms` развивается из internal discovery workspace в систему для:

- hypothesis tracking;
- customer development;
- market research;
- signal aggregation;
- решений по гипотезам;
- read-only аналитического слоя в Streamlit;
- controlled write-path через Codex / agents.

## Принцип работы

- `READ` -> Streamlit
- `WRITE` -> backend API через Codex / agent workflows

## Этапы

### Этап 1. Data model + API

Сделать:

- PostgreSQL schema;
- SQLAlchemy models;
- Alembic scaffolding;
- CRUD endpoints для:
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
- health / ready;
- audit log.

### Этап 2. Auth + Access

Сделать:

- server-side allowlist;
- `allowed_users` table;
- auth context extraction из reverse proxy / Google-auth слоя;
- `GET /me`;
- access checks.

### Этап 3. Streamlit dashboard

Сделать:

- `Overview`
- `Hypotheses`
- `Interviews`
- `Insights`
- `Signals`
- `Competitors`
- `Decisions`
- `Wiki`

### Этап 4. Agent-safe write paths

Сделать:

- tool-like endpoints;
- service account concept;
- ограничения на risky operations;
- audit trail по agent actions.

### Этап 5. Ops

Сделать:

- Docker Compose;
- reverse proxy;
- backup / restore;
- server runbook;
- deploy docs.

## Что делаем в этом коммите

1. Заводим backend skeleton.
2. Заводим основные модели и схемы.
3. Добавляем первые CRUD endpoints.
4. Добавляем новый Streamlit read-layer skeleton.
5. Добавляем `.env.example`, `docker-compose.yml`, Dockerfiles и scripts.

## Что пока не закрыто

- реальный Google OAuth flow;
- полноценные Alembic migrations versions;
- reverse proxy;
- attachment storage;
- production-ready audit log детализация;
- полноценный read dashboard с drill-down.
