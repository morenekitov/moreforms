# AI-First Workspace Template Guide

## Что это дает проекту

Reference-репозиторий в `references/ai-first-workspace-template` нужен не как кодовая зависимость, а как operating model для совместной AI-first работы.

Для текущего `moreforms` его лучше применять так:

- не копировать структуру целиком;
- взять из него принцип разделения контекстов;
- собрать в одном репозитории легкий аналог multi-team workspace.

## Как смержить шаблон с текущим проектом

### 1. Разделить работу на контуры

Текущий проект уже можно мыслить как 5 рабочих слоев:

- `Workspace` -> идеи, backlog, контакты, research library, generated dashboards
- `Strategy` -> one-pager, competitors, market signals, positioning
- `Research` -> интервью, заметки, новости, видео, customer evidence
- `Product` -> roles, JTBD, journey, PRD, hypotheses, risks
- `App` -> Streamlit, OpenClaw, deploy

### 2. Держать context в файлах, а не в памяти

Вместо разрозненных чатов:

- идеи живут в `data/ideas.csv`
- задачи живут в `data/tasks.csv`
- контакты живут в `data/contacts.csv`
- материалы живут в `data/research_library.csv`
- стратегические выводы живут в `artifacts/*.md`

### 3. Использовать generated dashboards как lightweight views

В шаблоне важна идея быстрых AI-generated представлений для конкретной задачи.

В этом проекте это соответствует:

- `generated_dashboards/<slug>.md`
- ссылке `https://app.moreforms.ru?dashboard=<slug>`

### 4. Оставить один repo, но работать как с mini-workspace

На текущем этапе отдельные repos не нужны. Достаточно:

- одного git repo;
- понятных trackers;
- стабильных артефактов;
- chat dashboard для AI-операций;
- основного dashboard для просмотра и совместной работы.

## Практическое соответствие

| Паттерн из AI workspace template | Что использовать в `moreforms` |
| --- | --- |
| Strategy docs | `artifacts/one_pager.md`, `artifacts/competitor_map.md`, `data/competitors.csv` |
| Research docs | `data/research_library.csv`, `data/contacts.csv`, `data/adoption_mentions.csv` |
| Product docs | `artifacts/jtbd.md`, `artifacts/user_journey.md`, `artifacts/prd_mvp.md`, `artifacts/metrics_and_hypotheses.md`, `artifacts/risk_register.md` |
| Ops / execution | `data/tasks.csv`, `data/ideas.csv` |
| AI-assisted workbench | `app.py`, `openclaw_agent.md`, `openclaw_streamlit.md`, `generated_dashboards/` |

## Что не нужно делать сейчас

- не копируй весь reference repo в корень проекта;
- не делай искусственный multi-repo setup;
- не размножай папки без реального owner и процесса;
- не подменяй decision making красивой структурой.

## Что нужно делать сейчас

- вести идеи и evidence централизованно;
- работать через артефакты и trackers;
- использовать chat dashboard для генерации новых views и обновления knowledge base;
- удерживать основной dashboard как shared cockpit для всей команды.
