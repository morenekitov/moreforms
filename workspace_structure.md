# Workspace Structure

## Назначение

`moreforms` используется как shared venture discovery workspace для команды, которая исследует startup ideas для SMB.

Важно:

- `shared workspace` — это внутренний продукт команды;
- конечная цель — не продавать сам workspace, а найти product-market fit для внешнего AI-native B2B SaaS;
- текущий discovery идет вокруг трех pain areas:
  - управленческая отчетность;
  - составление и согласование КП;
  - обработка и интерпретация сложных Excel.

Это рабочая система, а не просто витрина.

В ней команда:

- фиксирует идеи;
- ведет backlog гипотез и задач;
- хранит контакты и interview pipeline;
- собирает статьи, видео, market signals и новости;
- ведет конкурентную карту;
- поддерживает discovery-артефакты;
- создает lightweight dashboards под отдельные вопросы.

Артефакты в `artifacts/*.md` описывают не сам workspace, а путь к формированию конечного внешнего продукта.

## Базовая структура совместной работы

### 1. Workspace

Файлы:

- `data/ideas.csv`
- `data/tasks.csv`
- `data/contacts.csv`
- `data/research_library.csv`

Назначение:

- идеи;
- next actions;
- люди и интервью;
- материалы и evidence.

### 2. Strategy

Файлы:

- `artifacts/one_pager.md`
- `artifacts/competitor_map.md`
- `data/competitors.csv`
- `data/adoption_mentions.csv`

Назначение:

- сформулировать venture thesis;
- понять рынок;
- увидеть landscape;
- выбрать правильный wedge.

На текущем этапе здесь нужно удерживать три competing directions:

- reporting;
- КП workflow;
- Excel intelligence.

### 3. Product

Файлы:

- `artifacts/roles_and_scenarios.md`
- `artifacts/jtbd.md`
- `artifacts/user_journey.md`
- `artifacts/prd_mvp.md`
- `artifacts/metrics_and_hypotheses.md`
- `artifacts/risk_register.md`

Назначение:

- превращать thesis в продуктовую гипотезу;
- не терять логику решений;
- иметь базу для прототипов и MVP.

### 4. App

Файлы:

- `app.py`
- `openclaw_agent.md`
- `openclaw_streamlit.md`
- `deploy/*`
- `generated_dashboards/*`

Назначение:

- показать команде все ключевые контуры в одном интерфейсе;
- дать chat dashboard для OpenClaw;
- быстро создавать новые lightweight views.

## Базовый ритм работы

### Еженедельно

- обновить `ideas.csv`
- обновить `tasks.csv`
- добавить новые материалы в `research_library.csv`
- обновить статус гипотез и next steps

### После каждого интервью или сигнала

- добавить запись в `contacts.csv` или обновить существующую
- положить заметку или материал в `research_library.csv`
- если есть сильный сдвиг, обновить `one_pager`, `JTBD` или `competitor_map`

### После каждого значимого продуктового решения

- обновить соответствующий артефакт
- зафиксировать задачу в `tasks.csv`
- если решение требует нового представления, создать generated dashboard

### На текущем этапе discovery

- не пытаться зафиксировать финальный product scope слишком рано;
- докручивать артефакты по мере интервью и брейншторминга;
- явно различать:
  - внутренний operating layer команды;
  - внешний продукт, который ищет PMF.

## Что должно быть видно в dashboard

В основной dashboard должны быть доступны:

- workspace overview;
- идеи;
- задачи;
- контакты;
- материалы;
- конкуренты;
- рыночные сигналы;
- артефакты;
- generated dashboards.

В chat dashboard должно быть удобно:

- задавать вопросы по knowledge base;
- просить обновить trackers;
- просить изменить UI;
- просить создать новый generated dashboard и вернуть ссылку.
