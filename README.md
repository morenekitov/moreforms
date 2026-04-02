# moreforms

V1 разработки `moreforms` как internal startup discovery system.

Система строится вокруг цикла:

`hypothesis -> interview -> insight -> decision`

Дополнительно в контур входят:

- конкуренты;
- сигналы рынка и внедрений;
- wiki / notes;
- controlled agent workflows через backend API;
- Streamlit dashboard как read-layer.

## Текущее состояние

Репозиторий находится в переходе от старого CSV-based workspace к новой архитектуре v1:

- `app/` — новый backend API слой;
- `streamlit_app/` — новый Streamlit read-layer;
- `docs/` — план реализации и документация по v1;
- старый root-level [app.py](/Users/morenekitov/Documents/moreforms/app.py) пока сохранен как legacy workspace и будет убран после переноса.

## Целевая модель работы

- `READ` -> Streamlit dashboard
- `WRITE` -> Codex / agent interface

Пользователь не должен вручную заносить большую часть данных через UI.  
Сырой ввод поступает в agent layer, затем структурируется и записывается через backend API.

## Основные сущности v1

- `hypotheses`
- `companies`
- `contacts`
- `interviews`
- `insights`
- `decisions`
- `pages`
- `attachments`
- `competitors`
- `signals`
- `allowed_users`
- `audit_logs`

## Структура

- `app/` — FastAPI backend
- `streamlit_app/` — Streamlit dashboard
- `migrations/` — Alembic migrations
- `scripts/` — backup / restore / seed
- `docs/` — roadmap и архитектурные заметки
- `tests/` — тесты
- `docker/` — Dockerfiles
- `docker-compose.yml` — локальный и серверный контур v1
- `.env.example` — шаблон окружения

## Этапы реализации

Подробный план: [docs/v1-development-plan.md](/Users/morenekitov/Documents/moreforms/docs/v1-development-plan.md)

Коротко:

1. Data model + API
2. Auth + access
3. Streamlit dashboard
4. Agent-safe endpoints
5. Ops + backup / restore

## Локальный запуск backend

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
cp .env.example .env
.venv/bin/uvicorn app.main:app --reload
```

## Локальный запуск Streamlit v1

```bash
.venv/bin/streamlit run streamlit_app/app.py
```

## Docker Compose

```bash
docker compose up --build
```

## Legacy

Старые файлы workspace пока сохранены для постепенной миграции:

- [app.py](/Users/morenekitov/Documents/moreforms/app.py)
- `data/*.csv`
- `deploy/`
- `generated_dashboards/`

Они не являются целевой архитектурой v1.
