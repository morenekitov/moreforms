# Workspace Structure

## Назначение

`moreforms` — это внутренний shared workspace команды.

Он нужен для поиска `PMF` будущего `AI-native B2B SaaS`, а не как конечный внешний продукт.

## Что видно на основном dashboard

В основном dashboard есть два top-level таба:

1. `Чат`
2. `Пространство`

### Чат

В табе `Чат` есть только:

- выбор режима;
- статус backend;
- сам чат.

### Пространство

В табе `Пространство` есть подтабы:

1. `Конкуренты`
2. `Сигналы внедрений`
3. `Контакты`
4. `Артефакты`
5. `Интервью`
6. `Бэклог и требования`
7. `Созданные дашборды`

## Что видно в chat dashboard

В chat dashboard есть только:

- выбор режима;
- статус backend;
- сам чат.

## Основные tracker-файлы

- `data/competitors.csv`
- `data/adoption_mentions.csv`
- `data/contacts.csv`
- `data/interviews.csv`
- `data/backlog.csv`
- `data/artifacts.csv`

## Основные документы

- `artifacts.md`
- `artifacts/*.md`
- `Agents.md`
- `openclaw_agent.md`
- `openclaw_streamlit.md`

## Текущий product discovery focus

Сейчас команда исследует три pain areas:

1. управленческая отчетность;
2. составление и согласование КП;
3. обработка и интерпретация сложных Excel.

## Generated dashboards

Lightweight dashboards живут в:

- `generated_dashboards/<slug>.md`

Публичный формат ссылки:

- `https://app.moreforms.ru?dashboard=<slug>`
