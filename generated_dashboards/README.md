# Generated Dashboards

Здесь лежат lightweight dashboard-страницы, которые создает или обновляет OpenClaw по запросу пользователя.

Правила:

- один dashboard = один markdown-файл;
- имя файла = `slug`, например `university-enrollment-summary.md`;
- основная ссылка формируется как:
  - `https://app.moreforms.ru?dashboard=<slug>`

Если нужна сложная логика Streamlit, фильтры, графики или отдельный runtime, надо менять основной код приложения, а не только этот каталог.
