# OpenClaw x Streamlit

## Поверхности

В проекте есть два URL-режима:

- основной dashboard: `https://app.moreforms.ru`
- чат-дашборд: `https://app.moreforms.ru?view=chat`

## Основной dashboard

Основной dashboard показывает только рабочие сценарии команды:

- конкуренты;
- сигналы внедрений;
- контакты;
- артефакты;
- проведенные интервью;
- бэклог и требования.

## Чат-дашборд

Чат-дашборд содержит только:

- чат с OpenClaw;
- таблицу со ссылками на созданные lightweight dashboards.

## Правила изменений

### Если нужно обновить tracker

Обновляй соответствующий CSV:

- `data/competitors.csv`
- `data/adoption_mentions.csv`
- `data/contacts.csv`
- `data/interviews.csv`
- `data/backlog.csv`
- `data/artifacts.csv`

### Если нужно обновить продуктовую логику

Обновляй:

- `artifacts.md`
- `artifacts/*.md`

### Если нужно создать lightweight dashboard

- создай или обнови `generated_dashboards/<slug>.md`
- верни ссылку вида `https://app.moreforms.ru?dashboard=<slug>`

### Если нужно поменять Streamlit UI

Меняй:

- `app.py`

## Ограничения

- не добавляй лишние разделы в основной dashboard без прямого запроса;
- не превращай chat dashboard в второй основной dashboard;
- не придумывай ссылку без реально созданного slug.
