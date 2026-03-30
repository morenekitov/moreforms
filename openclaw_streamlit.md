# OpenClaw x Streamlit

## Схема интерфейсов

В проекте есть два URL-режима:

- основной workspace dashboard: `https://app.moreforms.ru`
- chat dashboard: `https://app.moreforms.ru?view=chat`

Основной dashboard нужен для:

- shared workspace;
- идей;
- задач;
- контактов;
- research library;
- конкурентов;
- рыночных сигналов;
- discovery-артефактов;
- просмотра generated dashboards.

Chat dashboard нужен только для работы с OpenClaw.

Важное правило для content и generated outputs:

- workspace dashboard описывает внутреннюю систему команды;
- продуктовые артефакты описывают будущую внешнюю SaaS-идею;
- не смешивай эти два слоя в одном ответе без явной пометки.

## Как OpenClaw используется в Streamlit

Streamlit ходит не в сложный внешний gateway, а во внутренний HTTP-adapter, который:

- принимает `POST /v1/responses`;
- вызывает `openclaw agent --json`;
- возвращает `output_text` для chat UI.

Это упрощает эксплуатацию VPS и позволяет держать авторизацию на уровне приложения.

## Как работать с dashboard changes

### 1. Lightweight dashboards

Если задача решается markdown-страницей без отдельной сложной логики:

- создай или обнови `generated_dashboards/<slug>.md`
- slug должен быть коротким, lowercase, через дефисы или `_`

После этого верни ссылку:

- `https://app.moreforms.ru?dashboard=<slug>`

### 2. Основной workspace dashboard

Если нужно менять:

- структуру главного dashboard;
- новые разделы workspace;
- таблицы и карточки;
- роутинг по query params;
- общий UX для совместной работы;

то редактируй:

- `app.py`

### 3. Chat dashboard

Если нужно менять:

- режимы чата;
- quick actions;
- prompt building;
- formatting ответа;
- инструкции для OpenClaw;

то редактируй:

- `app.py`
- `openclaw_agent.md`
- `openclaw_streamlit.md`
- `deploy/openclaw_responses_adapter.py` при необходимости

## Что должен делать агент после создания дашборда

Если generated dashboard создан или обновлен, ответ должен содержать:

- короткий вывод;
- какие файлы изменены;
- slug;
- прямую ссылку;
- при возможности короткий preview содержимого.

## Ограничения

- не создавай новый Python entrypoint без необходимости;
- не ломай основной workspace ради одного эксперимента;
- не придумывай slug и ссылку без реально созданного файла;
- если задача относится к shared knowledge base, сначала обновляй trackers и docs, а потом уже строй dashboard.
