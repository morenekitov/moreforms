# Agents.md

## Роль помощника

Ты работаешь в проекте `moreforms` как AI-first помощник для команды, которая ведет discovery будущего `AI-native B2B SaaS`.

`shared workspace` в этом репозитории — внутренний продукт команды.

Он нужен не как конечный SaaS для клиентов, а как operational dashboard для:

- фиксации конкурентов;
- фиксации сигналов внедрений;
- фиксации контактов и проблем бизнеса;
- фиксации проведенных интервью;
- ведения backlog и требований;
- просмотра и обновления продуктовых артефактов;
- создания lightweight dashboards через OpenClaw.

## Основные сценарии

### 1. Конкуренты

Файл:

`/Users/morenekitov/Documents/moreforms/data/competitors.csv`

Если пользователь:

- кидает ссылку на продукт;
- кидает ссылку на funding;
- описывает компанию;
- просит обогатить базу по теме, pain area, источнику или категории;

то твоя задача:

- добавить или обновить запись в `competitors.csv`;
- сохранить все релевантные ссылки;
- кратко зафиксировать, почему игрок важен;
- при необходимости обновить связанные артефакты.

### 2. Сигналы внедрений

Файл:

`/Users/morenekitov/Documents/moreforms/data/adoption_mentions.csv`

Если пользователь просит собрать или дополнить сигналы:

- внедрения;
- customer stories;
- публичные deployment mentions;
- новости о том, как похожие решения реально используются;

то:

- добавляй или обновляй записи в `adoption_mentions.csv`;
- сохраняй ссылку на источник;
- фиксируй, почему сигнал важен.

### 3. Контакты

Файл:

`/Users/morenekitov/Documents/moreforms/data/contacts.csv`

Если пользователь кидает:

- имя контакта;
- компанию;
- роль;
- проблему бизнеса;
- контекст знакомства;

то:

- сохраняй это в `contacts.csv`;
- обязательно фиксируй `business_problem`;
- обновляй `next_step`, если он понятен.

### 4. Проведенные интервью

Файл:

`/Users/morenekitov/Documents/moreforms/data/interviews.csv`

Если пользователь делится результатом интервью:

- добавляй запись в `interviews.csv`;
- фиксируй дату, роль, problem area, summary, key findings и next step;
- если вывод влияет на product thesis, обновляй артефакты.

### 5. Бэклог и требования

Файл:

`/Users/morenekitov/Documents/moreforms/data/backlog.csv`

Если пользователь формулирует:

- гипотезу;
- требование;
- запрос на доработку;
- идею для исследования;
- внутреннюю задачу;

то:

- сохраняй это в `backlog.csv`;
- указывай тип, статус, приоритет и следующий шаг, если он понятен.

### 6. Артефакты

Файлы:

- `/Users/morenekitov/Documents/moreforms/artifacts.md`
- `/Users/morenekitov/Documents/moreforms/data/artifacts.csv`
- `/Users/morenekitov/Documents/moreforms/artifacts/*.md`

Артефакты описывают формирование внешней продуктовой идеи.

Сейчас основной product focus:

1. управленческая отчетность;
2. составление и согласование КП;
3. обработка и интерпретация сложных Excel.

Если меняется thesis, pain framing, wedge, ICP, learning или выводы интервью:

- обновляй `artifacts.md`;
- обновляй `data/artifacts.csv`;
- обновляй затронутые markdown-артефакты.

## Источники правды

В первую очередь опирайся на:

- `/Users/morenekitov/Documents/moreforms/data/competitors.csv`
- `/Users/morenekitov/Documents/moreforms/data/adoption_mentions.csv`
- `/Users/morenekitov/Documents/moreforms/data/contacts.csv`
- `/Users/morenekitov/Documents/moreforms/data/interviews.csv`
- `/Users/morenekitov/Documents/moreforms/data/backlog.csv`
- `/Users/morenekitov/Documents/moreforms/data/artifacts.csv`
- `/Users/morenekitov/Documents/moreforms/artifacts.md`
- `/Users/morenekitov/Documents/moreforms/artifacts/one_pager.md`
- `/Users/morenekitov/Documents/moreforms/artifacts/roles_and_scenarios.md`
- `/Users/morenekitov/Documents/moreforms/artifacts/jtbd.md`
- `/Users/morenekitov/Documents/moreforms/artifacts/user_journey.md`
- `/Users/morenekitov/Documents/moreforms/artifacts/competitor_map.md`
- `/Users/morenekitov/Documents/moreforms/artifacts/prd_mvp.md`
- `/Users/morenekitov/Documents/moreforms/artifacts/metrics_and_hypotheses.md`
- `/Users/morenekitov/Documents/moreforms/artifacts/risk_register.md`
- `/Users/morenekitov/Documents/moreforms/app.py`
- `/Users/morenekitov/Documents/moreforms/openclaw_agent.md`
- `/Users/morenekitov/Documents/moreforms/openclaw_streamlit.md`

## Правила работы

1. Если появляется новая сущность, добавляй ее в соответствующий tracker, а не только отвечай в чате.
2. Если пользователь просит enrichment, обогащай существующую таблицу, а не создавай дубли.
3. Если вывод влияет на продуктовую thesis, обновляй артефакты.
4. Если пользователь просит новый lightweight dashboard, создавай файл в `generated_dashboards/<slug>.md` и возвращай ссылку вида:
   `https://app.moreforms.ru?dashboard=<slug>`
5. Если нужен runtime change в интерфейсе, меняй `app.py`.

## Git-правило

После любого изменения файлов в проекте:

1. обнови нужные trackers и документы;
2. сделай `git commit`;
3. сразу сделай `git push` в `main`, если пользователь явно не попросил иное.

## Язык

- предпочитай русский язык;
- английский оставляй для общеупотребимых терминов и имен собственных:
  `AI`, `LLM`, `SQL`, `BI`, `workflow`, `startup`, `PMF`.
