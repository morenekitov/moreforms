# moreforms

AI-first discovery workspace for a team exploring startup ideas for SMB.

## Что внутри

- shared workspace для идей, backlog, контактов и исследовательских материалов;
- конкурентная карта и рыночные сигналы;
- продуктовые артефакты;
- отдельный chat dashboard на OpenClaw;
- generated dashboards, которые чат может создавать и обновлять.

## Структура

- `workspace_structure.md` — базовая модель совместной работы
- `Agents.md` — правила для агента
- `artifacts.md` — обзор обязательных discovery-артефактов
- `artifacts/` — отдельные артефакты
- `data/ideas.csv` — идеи и venture thesis
- `data/tasks.csv` — backlog и next actions
- `data/contacts.csv` — контакты и interview pipeline
- `data/research_library.csv` — статьи, видео, заметки и market signals
- `data/competitors.csv` — конкурентная карта
- `data/adoption_mentions.csv` — кейсы и сигналы использования похожих продуктов
- `data/artifacts.csv` — реестр артефактов
- `app.py` — Streamlit workspace
- `deploy/` — серверный контур для Streamlit, Google login и OpenClaw
- `generated_dashboards/` — lightweight dashboards, создаваемые через чат
- `workspace_template_guide.md` — как применить AI-first workspace template к этому проекту

## URL-режимы

- основной workspace dashboard: `https://app.moreforms.ru`
- chat dashboard: `https://app.moreforms.ru?view=chat`
- generated dashboard: `https://app.moreforms.ru?dashboard=<slug>`

## Local run

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/streamlit run app.py
```

## AI-first Workspace Reference

В проект подключен reference-репозиторий:

`references/ai-first-workspace-template`

Он нужен как источник паттернов для:

- organization memory;
- structuring of discovery work;
- context separation for AI;
- operating workflows between strategy, research, product and delivery.
