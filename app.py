import os
from pathlib import Path

import pandas as pd
import requests
import streamlit as st


st.set_page_config(
    page_title="Moreforms: discovery workspace",
    page_icon="📊",
    layout="wide",
)

WORKSPACE_STRUCTURE_PATH = Path(__file__).parent / "workspace_structure.md"
DATA_PATH = Path(__file__).parent / "data" / "competitors.csv"
ADOPTION_PATH = Path(__file__).parent / "data" / "adoption_mentions.csv"
ARTIFACTS_PATH = Path(__file__).parent / "data" / "artifacts.csv"
IDEAS_PATH = Path(__file__).parent / "data" / "ideas.csv"
TASKS_PATH = Path(__file__).parent / "data" / "tasks.csv"
CONTACTS_PATH = Path(__file__).parent / "data" / "contacts.csv"
RESEARCH_LIBRARY_PATH = Path(__file__).parent / "data" / "research_library.csv"
OPENCLAW_AGENT_PROFILE_PATH = Path(__file__).parent / "openclaw_agent.md"
OPENCLAW_STREAMLIT_GUIDE_PATH = Path(__file__).parent / "openclaw_streamlit.md"
GENERATED_DASHBOARDS_DIR = Path(__file__).parent / "generated_dashboards"
OPENCLAW_RESPONSES_URL = os.getenv("OPENCLAW_RESPONSES_URL", "").strip()
OPENCLAW_GATEWAY_TOKEN = os.getenv("OPENCLAW_GATEWAY_TOKEN", "").strip()
OPENCLAW_AGENT_ID = os.getenv("OPENCLAW_AGENT_ID", "main").strip() or "main"
OPENCLAW_CHAT_USER_PREFIX = os.getenv("OPENCLAW_CHAT_USER_PREFIX", "streamlit").strip() or "streamlit"
MAIN_DASHBOARD_PUBLIC_URL = os.getenv("MAIN_DASHBOARD_PUBLIC_URL", "https://app.moreforms.ru").rstrip("/")
CHAT_DASHBOARD_PUBLIC_URL = os.getenv(
    "CHAT_DASHBOARD_PUBLIC_URL",
    f"{MAIN_DASHBOARD_PUBLIC_URL}?view=chat",
).strip()
DEFAULT_COLUMNS = {
    "company_name": "",
    "website": "",
    "country": "",
    "founded_year": "",
    "category": "",
    "startup_type": "",
    "similarity_type": "",
    "target_market": "",
    "target_segments": "",
    "primary_client": "",
    "primary_pain": "",
    "problem_solved": "",
    "key_features": "",
    "user_journey": "",
    "notable_features": "",
    "has_form_builder": "no",
    "has_survey_or_interviews": "no",
    "has_reminders_or_followups": "no",
    "has_response_cap_or_auto_close": "no",
    "has_ai_analysis": "no",
    "has_prompt_dashboards": "no",
    "has_excel_csv_analysis": "no",
    "has_exports_reporting": "no",
    "has_integrations": "no",
    "deployment_notes": "",
    "rf_pilot_relevance": "",
    "seed_round_date": "",
    "seed_amount_usd_m": "",
    "stage": "",
    "investors": "",
    "funding_source_url": "",
    "product_source_url": "",
    "all_links": "",
    "notes": "",
}
ADOPTION_DEFAULT_COLUMNS = {
    "startup_or_product": "",
    "relation_type": "",
    "sector": "",
    "usage_pattern": "",
    "geography_bucket": "",
    "country": "",
    "organization": "",
    "organization_type": "",
    "source_type": "",
    "source_name": "",
    "source_url": "",
    "published_date": "",
    "summary": "",
    "why_it_matters": "",
}
ARTIFACTS_DEFAULT_COLUMNS = {
    "artifact_name": "",
    "artifact_group": "",
    "priority": "",
    "status": "",
    "completion_pct": 0,
    "evidence_score": 0,
    "validation_status": "",
    "target_user": "",
    "current_focus": "",
    "deliverable_path": "",
    "validation_method": "",
    "next_step": "",
}
IDEAS_DEFAULT_COLUMNS = {
    "idea_name": "",
    "theme": "",
    "segment": "",
    "status": "",
    "priority": "",
    "thesis": "",
    "evidence": "",
    "next_step": "",
    "owner": "",
    "links": "",
    "notes": "",
}
TASKS_DEFAULT_COLUMNS = {
    "task_name": "",
    "workstream": "",
    "priority": "",
    "status": "",
    "owner": "",
    "due_date": "",
    "related_artifact": "",
    "outcome": "",
    "notes": "",
}
CONTACTS_DEFAULT_COLUMNS = {
    "contact_name": "",
    "organization": "",
    "role": "",
    "segment": "",
    "stage": "",
    "last_touch_date": "",
    "next_step": "",
    "source": "",
    "links": "",
    "notes": "",
}
RESEARCH_LIBRARY_DEFAULT_COLUMNS = {
    "title": "",
    "item_type": "",
    "theme": "",
    "geography": "",
    "source_name": "",
    "source_url": "",
    "summary": "",
    "why_it_matters": "",
    "related_idea": "",
    "tags": "",
}
LEGACY_VALUE_TRANSLATIONS = {
    "primary_client": {
        "insights and product research teams": "команды исследований и продуктовых исследований",
        "market research and product teams": "команды маркетинговых исследований и продуктовые команды",
        "brand and customer insights teams": "команды бренд-аналитики и клиентской аналитики",
        "analysts and operations teams": "аналитики и операционные команды",
        "founders and operations teams": "фаундеры и операционные команды",
        "knowledge workers and non-technical analysts": "офисные специалисты и нетехнические аналитики",
        "business users waiting on data teams": "бизнес-пользователи, зависящие от команд данных",
        "data teams and GTM leaders": "команды данных и GTM-руководители",
        "data and finance reporting teams": "команды отчетности по данным и финансам",
        "operations and finance teams with large datasets": "операционные и финансовые команды с большими датасетами",
        "ops and marketing teams living in spreadsheets": "операционные и маркетинговые команды, работающие в таблицах",
        "business users without ML teams": "бизнес-пользователи без собственной ML-команды",
        "marketing and revenue teams": "маркетинговые и коммерческие команды",
        "operations teams and founders": "операционные команды и фаундеры",
        "makers, educators, and small teams": "мейкеры, независимые создатели и небольшие команды",
        "operations teams building workflow forms": "операционные команды, собирающие workflow-формы",
        "product and UX research teams": "продуктовые команды и UX-исследователи",
        "enterprise data consumers outside the data team": "корпоративные пользователи данных вне команд данных",
        "data and analytics engineering teams": "команды инженерии данных и аналитической инженерии",
        "enterprise analysts and business leaders": "корпоративные аналитики и бизнес-руководители",
        "команды исследований и product research": "команды исследований и продуктовых исследований",
        "команды market research и product": "команды маркетинговых исследований и продуктовые команды",
        "команды brand insights и customer insights": "команды бренд-аналитики и клиентской аналитики",
        "knowledge workers и нетехнические аналитики": "офисные специалисты и нетехнические аналитики",
        "бизнес-пользователи, зависящие от data teams": "бизнес-пользователи, зависящие от команд данных",
        "data teams и GTM-лидеры": "команды данных и GTM-руководители",
        "команды data- и finance-отчетности": "команды отчетности по данным и финансам",
        "operations и finance-команды с большими датасетами": "операционные и финансовые команды с большими датасетами",
        "ops- и marketing-команды, работающие в таблицах": "операционные и маркетинговые команды, работающие в таблицах",
        "marketing- и revenue-команды": "маркетинговые и коммерческие команды",
        "product-команды и UX-исследователи": "продуктовые команды и UX-исследователи",
        "корпоративные пользователи данных вне data team": "корпоративные пользователи данных вне команд данных",
        "команды data engineering и analytics engineering": "команды инженерии данных и аналитической инженерии",
    }
}
CAPABILITY_LABELS = {
    "all": "Все",
    "has_form_builder": "Есть конструктор форм",
    "has_survey_or_interviews": "Есть опросы или интервью",
    "has_ai_analysis": "Есть AI-анализ",
    "has_prompt_dashboards": "Есть дашборды по промпту",
    "has_excel_csv_analysis": "Есть анализ Excel или CSV",
    "has_exports_reporting": "Есть экспорт и отчетность",
}
CHAT_MODE_CONFIG = {
    "strategy": {
        "label": "Стратегия",
        "description": "Venture thesis, wedge, ICP, JTBD и приоритеты discovery.",
        "context": (
            "Режим: стратегия. Сфокусируйся на venture thesis, выборе сегмента, wedge, "
            "JTBD, user journey и ключевых learning loops."
        ),
        "files": [
            "workspace_structure.md",
            "artifacts/one_pager.md",
            "artifacts/jtbd.md",
            "artifacts/user_journey.md",
            "artifacts/prd_mvp.md",
            "artifacts/metrics_and_hypotheses.md",
            "data/ideas.csv",
        ],
        "quick_prompts": [
            "Сформулируй 3 главных риска текущей venture thesis.",
            "Предложи приоритеты discovery на ближайшие 2 недели.",
            "Сравни активные идеи и предложи, что держать в фокусе.",
        ],
    },
    "market": {
        "label": "Рынок",
        "description": "Конкуренты, сигналы, category map, customer evidence.",
        "context": (
            "Режим: рынок. Сфокусируйся на конкурентной карте, category map, смежных "
            "решениях, customer signals и важности для текущих startup ideas."
        ),
        "files": [
            "data/competitors.csv",
            "data/adoption_mentions.csv",
            "data/research_library.csv",
            "artifacts/competitor_map.md",
        ],
        "quick_prompts": [
            "Собери shortlist из прямых и смежных игроков под текущую thesis.",
            "Покажи, какие категории рынка недооценены.",
            "Сравни 5 ближайших конкурентов и выдели gap в позиционировании.",
        ],
    },
    "workspace": {
        "label": "Workspace",
        "description": "Идеи, backlog, контакты, research materials, wiki и next steps.",
        "context": (
            "Режим: workspace. Сфокусируйся на совместной работе команды: ideas backlog, "
            "контакты, research materials, задачи, wiki и generated dashboards."
        ),
        "files": [
            "workspace_structure.md",
            "data/ideas.csv",
            "data/tasks.csv",
            "data/contacts.csv",
            "data/research_library.csv",
            "artifacts.md",
        ],
        "quick_prompts": [
            "Покажи, что в workspace сейчас не хватает для нормального discovery.",
            "Предложи, как почистить backlog идей и задач.",
            "Собери план следующего discovery sprint по текущим материалам.",
        ],
    },
    "development": {
        "label": "Разработка",
        "description": "Изменения в коде, UX табов, данные, инфраструктура и deploy.",
        "context": (
            "Режим: разработка. Сфокусируйся на коде, структуре workspace dashboard, "
            "generated dashboards, chat dashboard и deploy-контуре."
        ),
        "files": [
            "app.py",
            "deploy/docker-compose.yml",
            "deploy/README.md",
            "Agents.md",
            "openclaw_agent.md",
            "openclaw_streamlit.md",
        ],
        "quick_prompts": [
            "Предложи следующие 3 улучшения для workspace dashboard.",
            "Разложи, что осталось доделать для OpenClaw production contour.",
            "Покажи, какие файлы надо менять для следующего улучшения интерфейса.",
        ],
    },
}

WORKSPACE_DOC_OPTIONS = {
    "Операционная модель workspace": "workspace_structure.md",
    "Обзор артефактов": "artifacts.md",
    "One-pager": "artifacts/one_pager.md",
    "Роли и сценарии": "artifacts/roles_and_scenarios.md",
    "JTBD": "artifacts/jtbd.md",
    "User journey": "artifacts/user_journey.md",
    "PRD MVP": "artifacts/prd_mvp.md",
    "Метрики и гипотезы": "artifacts/metrics_and_hypotheses.md",
    "Риск-регистр": "artifacts/risk_register.md",
    "AI workspace template guide": "workspace_template_guide.md",
}


def ensure_schema(df: pd.DataFrame) -> pd.DataFrame:
    normalized = df.copy()
    for column, default_value in DEFAULT_COLUMNS.items():
        if column not in normalized.columns:
            normalized[column] = default_value
    for column, mapping in LEGACY_VALUE_TRANSLATIONS.items():
        normalized[column] = normalized[column].replace(mapping)
    return normalized[list(DEFAULT_COLUMNS.keys())]


@st.cache_data
def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH)
    df = ensure_schema(df)
    df["seed_round_date"] = pd.to_datetime(df["seed_round_date"], errors="coerce")
    df["seed_amount_usd_m"] = pd.to_numeric(df["seed_amount_usd_m"], errors="coerce")
    return df


def ensure_adoption_schema(df: pd.DataFrame) -> pd.DataFrame:
    normalized = df.copy()
    for column, default_value in ADOPTION_DEFAULT_COLUMNS.items():
        if column not in normalized.columns:
            normalized[column] = default_value
    return normalized[list(ADOPTION_DEFAULT_COLUMNS.keys())]


@st.cache_data
def load_adoption_data() -> pd.DataFrame:
    df = pd.read_csv(ADOPTION_PATH)
    df = ensure_adoption_schema(df)
    df["published_date"] = pd.to_datetime(df["published_date"], errors="coerce")
    return df


def ensure_artifacts_schema(df: pd.DataFrame) -> pd.DataFrame:
    normalized = df.copy()
    for column, default_value in ARTIFACTS_DEFAULT_COLUMNS.items():
        if column not in normalized.columns:
            normalized[column] = default_value
    return normalized[list(ARTIFACTS_DEFAULT_COLUMNS.keys())]


@st.cache_data
def load_artifacts_data() -> pd.DataFrame:
    df = pd.read_csv(ARTIFACTS_PATH)
    df = ensure_artifacts_schema(df)
    df["completion_pct"] = pd.to_numeric(df["completion_pct"], errors="coerce").fillna(0)
    df["evidence_score"] = pd.to_numeric(df["evidence_score"], errors="coerce").fillna(0)
    return df


def ensure_ideas_schema(df: pd.DataFrame) -> pd.DataFrame:
    normalized = df.copy()
    for column, default_value in IDEAS_DEFAULT_COLUMNS.items():
        if column not in normalized.columns:
            normalized[column] = default_value
    return normalized[list(IDEAS_DEFAULT_COLUMNS.keys())]


@st.cache_data
def load_ideas_data() -> pd.DataFrame:
    df = pd.read_csv(IDEAS_PATH)
    return ensure_ideas_schema(df)


def ensure_tasks_schema(df: pd.DataFrame) -> pd.DataFrame:
    normalized = df.copy()
    for column, default_value in TASKS_DEFAULT_COLUMNS.items():
        if column not in normalized.columns:
            normalized[column] = default_value
    return normalized[list(TASKS_DEFAULT_COLUMNS.keys())]


@st.cache_data
def load_tasks_data() -> pd.DataFrame:
    df = pd.read_csv(TASKS_PATH)
    df = ensure_tasks_schema(df)
    df["due_date"] = pd.to_datetime(df["due_date"], errors="coerce")
    return df


def ensure_contacts_schema(df: pd.DataFrame) -> pd.DataFrame:
    normalized = df.copy()
    for column, default_value in CONTACTS_DEFAULT_COLUMNS.items():
        if column not in normalized.columns:
            normalized[column] = default_value
    return normalized[list(CONTACTS_DEFAULT_COLUMNS.keys())]


@st.cache_data
def load_contacts_data() -> pd.DataFrame:
    df = pd.read_csv(CONTACTS_PATH)
    df = ensure_contacts_schema(df)
    df["last_touch_date"] = pd.to_datetime(df["last_touch_date"], errors="coerce")
    return df


def ensure_research_library_schema(df: pd.DataFrame) -> pd.DataFrame:
    normalized = df.copy()
    for column, default_value in RESEARCH_LIBRARY_DEFAULT_COLUMNS.items():
        if column not in normalized.columns:
            normalized[column] = default_value
    return normalized[list(RESEARCH_LIBRARY_DEFAULT_COLUMNS.keys())]


@st.cache_data
def load_research_library_data() -> pd.DataFrame:
    df = pd.read_csv(RESEARCH_LIBRARY_PATH)
    return ensure_research_library_schema(df)


@st.cache_data
def load_openclaw_agent_profile() -> str:
    if not OPENCLAW_AGENT_PROFILE_PATH.exists():
        return ""
    return OPENCLAW_AGENT_PROFILE_PATH.read_text(encoding="utf-8").strip()


@st.cache_data
def load_openclaw_streamlit_guide() -> str:
    if not OPENCLAW_STREAMLIT_GUIDE_PATH.exists():
        return ""
    return OPENCLAW_STREAMLIT_GUIDE_PATH.read_text(encoding="utf-8").strip()


def dashboard_link(slug: str) -> str:
    return f"{MAIN_DASHBOARD_PUBLIC_URL}?dashboard={slug}"


def parse_dashboard_title(markdown_text: str, fallback: str) -> str:
    for line in markdown_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped.removeprefix("# ").strip()
    return fallback.replace("_", " ").strip().title()


def list_generated_dashboards() -> list[dict[str, str]]:
    if not GENERATED_DASHBOARDS_DIR.exists():
        return []

    dashboards = []
    for path in sorted(GENERATED_DASHBOARDS_DIR.glob("*.md")):
        if path.name.lower() == "readme.md":
            continue
        content = path.read_text(encoding="utf-8")
        slug = path.stem
        dashboards.append(
            {
                "slug": slug,
                "title": parse_dashboard_title(content, slug),
                "content": content,
                "path": str(path),
                "link": dashboard_link(slug),
            }
        )
    return dashboards


def find_generated_dashboard(slug: str) -> dict[str, str] | None:
    for dashboard in list_generated_dashboards():
        if dashboard["slug"] == slug:
            return dashboard
    return None


def format_seed(seed_date, seed_amount) -> str:
    parts = []
    if pd.notna(seed_date):
        parts.append(seed_date.strftime("%Y-%m-%d"))
    if pd.notna(seed_amount):
        parts.append(f"${seed_amount:.1f}M")
    return " / ".join(parts) if parts else "нет данных"


def multiselect_filter(label: str, series: pd.Series) -> list[str]:
    options = sorted([value for value in series.dropna().unique().tolist() if value])
    return st.sidebar.multiselect(label, options, placeholder="Выберите варианты")


def apply_filters(df: pd.DataFrame) -> pd.DataFrame:
    st.sidebar.header("Фильтры")

    query = st.sidebar.text_input("Поиск по названию, сегменту, фичам")
    categories = multiselect_filter("Категория", df["category"])
    similarity = multiselect_filter("Тип похожести", df["similarity_type"])
    countries = multiselect_filter("Страна", df["country"])
    clients = multiselect_filter("Основной клиент", df["primary_client"])
    pains = multiselect_filter("Главная боль", df["primary_pain"])

    min_seed = float(df["seed_amount_usd_m"].min()) if not df["seed_amount_usd_m"].isna().all() else 0.0
    max_seed = float(df["seed_amount_usd_m"].max()) if not df["seed_amount_usd_m"].isna().all() else 10.0
    seed_range = st.sidebar.slider(
        "Раунд seed, $M",
        min_value=min_seed,
        max_value=max_seed,
        value=(min_seed, max_seed),
    )

    capability = st.sidebar.selectbox(
        "Функциональный фокус",
        list(CAPABILITY_LABELS.keys()),
        format_func=lambda value: CAPABILITY_LABELS[value],
    )

    filtered = df.copy()

    if query:
        haystack = (
            filtered["company_name"].fillna("")
            + " "
            + filtered["startup_type"].fillna("")
            + " "
            + filtered["target_segments"].fillna("")
            + " "
            + filtered["primary_client"].fillna("")
            + " "
            + filtered["primary_pain"].fillna("")
            + " "
            + filtered["problem_solved"].fillna("")
            + " "
            + filtered["key_features"].fillna("")
            + " "
            + filtered["user_journey"].fillna("")
            + " "
            + filtered["notable_features"].fillna("")
            + " "
            + filtered["notes"].fillna("")
        ).str.lower()
        filtered = filtered[haystack.str.contains(query.lower(), na=False)]

    if categories:
        filtered = filtered[filtered["category"].isin(categories)]

    if similarity:
        filtered = filtered[filtered["similarity_type"].isin(similarity)]

    if countries:
        filtered = filtered[filtered["country"].isin(countries)]

    if clients:
        filtered = filtered[filtered["primary_client"].isin(clients)]

    if pains:
        filtered = filtered[filtered["primary_pain"].isin(pains)]

    filtered = filtered[
        filtered["seed_amount_usd_m"].fillna(0).between(seed_range[0], seed_range[1])
    ]

    if capability != "all":
        filtered = filtered[filtered[capability].isin(["yes", "partial"])]

    return filtered.sort_values(
        by=["similarity_type", "seed_amount_usd_m", "company_name"],
        ascending=[True, False, True],
    )


def show_metrics(df: pd.DataFrame) -> None:
    direct_count = int((df["similarity_type"] == "прямой").sum())
    avg_seed = df["seed_amount_usd_m"].mean()
    countries = df["country"].nunique()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Компаний", len(df))
    col2.metric("Прямых", direct_count)
    col3.metric("Средний seed, $M", f"{avg_seed:.1f}" if pd.notna(avg_seed) else "нет данных")
    col4.metric("Стран", countries)


def show_table(df: pd.DataFrame) -> None:
    visible = df[
        [
            "company_name",
            "startup_type",
            "category",
            "similarity_type",
            "country",
            "primary_client",
            "primary_pain",
            "target_segments",
            "key_features",
            "user_journey",
            "seed_round_date",
            "seed_amount_usd_m",
            "website",
            "funding_source_url",
            "notes",
        ]
    ].copy()
    visible["seed_round_date"] = visible["seed_round_date"].dt.strftime("%Y-%m-%d")

    st.dataframe(
        visible,
        use_container_width=True,
        hide_index=True,
        column_config={
            "company_name": st.column_config.TextColumn("Компания", width="medium"),
            "startup_type": st.column_config.TextColumn("Тип стартапа", width="large"),
            "category": st.column_config.TextColumn("Категория"),
            "similarity_type": st.column_config.TextColumn("Тип"),
            "country": st.column_config.TextColumn("Страна"),
            "primary_client": st.column_config.TextColumn("Основной клиент", width="medium"),
            "primary_pain": st.column_config.TextColumn("Главная боль", width="large"),
            "target_segments": st.column_config.TextColumn("Сегменты", width="large"),
            "key_features": st.column_config.TextColumn("Ключевые фичи", width="large"),
            "user_journey": st.column_config.TextColumn("Путь пользователя", width="large"),
            "seed_round_date": st.column_config.TextColumn("Дата seed"),
            "seed_amount_usd_m": st.column_config.NumberColumn("Seed $M", format="%.1f"),
            "website": st.column_config.LinkColumn("Сайт"),
            "funding_source_url": st.column_config.LinkColumn("Источник funding"),
            "notes": st.column_config.TextColumn("Заметка", width="large"),
        },
    )


def show_company_cards(df: pd.DataFrame) -> None:
    st.subheader("Карточки")
    for row in df.to_dict(orient="records"):
        seed_text = format_seed(row["seed_round_date"], row["seed_amount_usd_m"])
        with st.expander(f'{row["company_name"]} • {row["startup_type"]} • {seed_text}'):
            st.markdown(f'**Сайт:** [ссылка]({row["website"]})')
            st.markdown(f'**Источник funding:** [ссылка]({row["funding_source_url"]})')
            st.markdown(f'**Источник по продукту:** [ссылка]({row["product_source_url"]})')
            st.markdown(f'**Тип стартапа:** `{row["startup_type"]}`')
            st.markdown(f'**Тип похожести:** `{row["similarity_type"]}`')
            st.markdown(f'**Раунд seed:** `{seed_text}`')
            st.markdown(f'**Основной клиент:** {row["primary_client"]}')
            st.markdown(f'**Главная боль:** {row["primary_pain"]}')
            st.markdown(f'**Сегменты:** {row["target_segments"]}')
            st.markdown(f'**Проблема:** {row["problem_solved"]}')
            st.markdown(f'**Ключевые фичи:** {row["key_features"]}')
            st.markdown(f'**Путь пользователя:** {row["user_journey"]}')
            st.markdown(f'**Фичи подробно:** {row["notable_features"]}')
            st.markdown(f'**Релевантность для текущей thesis:** {row["rf_pilot_relevance"]}')
            st.markdown(f'**Заметки:** {row["notes"]}')


def show_tabbed_views(df: pd.DataFrame) -> None:
    startup_types = [value for value in df["startup_type"].dropna().unique().tolist() if value]
    tab_names = ["Все"] + startup_types
    tabs = st.tabs(tab_names)

    with tabs[0]:
        show_table(df)
        st.divider()
        show_company_cards(df)

    for tab, startup_type in zip(tabs[1:], startup_types):
        subset = df[df["startup_type"] == startup_type].copy()
        with tab:
            st.caption(f"{len(subset)} компаний")
            show_table(subset)
            st.divider()
            show_company_cards(subset)


def show_workspace_overview() -> None:
    ideas = load_ideas_data()
    tasks = load_tasks_data()
    contacts = load_contacts_data()
    materials = load_research_library_data()

    active_ideas = int(ideas["status"].fillna("").isin(["в фокусе", "на исследовании"]).sum())
    open_tasks = int(tasks["status"].fillna("").isin(["в работе", "запланировано", "backlog"]).sum())
    active_contacts = int(contacts["stage"].fillna("").isin(["нужно связаться", "в переписке", "активен"]).sum())

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Идей", len(ideas))
    col2.metric("В активном фокусе", active_ideas)
    col3.metric("Открытых задач", open_tasks)
    col4.metric("Контактов и сигналов", active_contacts + len(materials))


def show_workspace_docs() -> None:
    st.markdown("### Вики и документация")
    selected_doc = st.selectbox(
        "Документ",
        list(WORKSPACE_DOC_OPTIONS.keys()),
        key="workspace_doc_select",
    )
    path_value = WORKSPACE_DOC_OPTIONS[selected_doc]
    ok, content = read_artifact_content(path_value)
    st.caption(f"Файл: `{path_value}`")
    if ok:
        st.markdown(content)
    else:
        st.warning(content)


def show_ideas_section() -> None:
    df = load_ideas_data()
    col1, col2 = st.columns(2)
    with col1:
        statuses = multiselect_main_filter("Статус идеи", df["status"], "ideas_status")
    with col2:
        themes = multiselect_main_filter("Тема", df["theme"], "ideas_theme")

    filtered = df.copy()
    if statuses:
        filtered = filtered[filtered["status"].isin(statuses)]
    if themes:
        filtered = filtered[filtered["theme"].isin(themes)]

    st.dataframe(
        filtered,
        use_container_width=True,
        hide_index=True,
        column_config={
            "idea_name": st.column_config.TextColumn("Идея", width="medium"),
            "theme": st.column_config.TextColumn("Тема"),
            "segment": st.column_config.TextColumn("Сегмент", width="medium"),
            "status": st.column_config.TextColumn("Статус"),
            "priority": st.column_config.TextColumn("Приоритет"),
            "thesis": st.column_config.TextColumn("Thesis", width="large"),
            "evidence": st.column_config.TextColumn("Evidence", width="large"),
            "next_step": st.column_config.TextColumn("Следующий шаг", width="large"),
            "owner": st.column_config.TextColumn("Owner"),
            "links": st.column_config.TextColumn("Ссылки", width="large"),
            "notes": st.column_config.TextColumn("Заметки", width="large"),
        },
    )

    for row in filtered.to_dict(orient="records"):
        with st.expander(f'{row["idea_name"]} • {row["status"]} • {row["priority"]}'):
            st.markdown(f'**Сегмент:** {row["segment"]}')
            st.markdown(f'**Thesis:** {row["thesis"]}')
            st.markdown(f'**Evidence:** {row["evidence"]}')
            st.markdown(f'**Следующий шаг:** {row["next_step"]}')
            st.markdown(f'**Owner:** {row["owner"]}')
            st.markdown(f'**Ссылки:** {row["links"] or "нет"}')
            st.markdown(f'**Заметки:** {row["notes"] or "нет"}')


def show_tasks_section() -> None:
    df = load_tasks_data()
    col1, col2 = st.columns(2)
    with col1:
        statuses = multiselect_main_filter("Статус задачи", df["status"], "tasks_status")
    with col2:
        owners = multiselect_main_filter("Owner", df["owner"], "tasks_owner")

    filtered = df.copy()
    if statuses:
        filtered = filtered[filtered["status"].isin(statuses)]
    if owners:
        filtered = filtered[filtered["owner"].isin(owners)]

    visible = filtered.copy()
    visible["due_date"] = visible["due_date"].dt.strftime("%Y-%m-%d")
    st.dataframe(
        visible,
        use_container_width=True,
        hide_index=True,
        column_config={
            "task_name": st.column_config.TextColumn("Задача", width="large"),
            "workstream": st.column_config.TextColumn("Поток"),
            "priority": st.column_config.TextColumn("Приоритет"),
            "status": st.column_config.TextColumn("Статус"),
            "owner": st.column_config.TextColumn("Owner"),
            "due_date": st.column_config.TextColumn("Срок"),
            "related_artifact": st.column_config.TextColumn("Связанный файл", width="medium"),
            "outcome": st.column_config.TextColumn("Ожидаемый результат", width="large"),
            "notes": st.column_config.TextColumn("Заметки", width="large"),
        },
    )


def show_contacts_section() -> None:
    df = load_contacts_data()
    col1, col2 = st.columns(2)
    with col1:
        stages = multiselect_main_filter("Стадия контакта", df["stage"], "contacts_stage")
    with col2:
        segments = multiselect_main_filter("Сегмент", df["segment"], "contacts_segment")

    filtered = df.copy()
    if stages:
        filtered = filtered[filtered["stage"].isin(stages)]
    if segments:
        filtered = filtered[filtered["segment"].isin(segments)]

    visible = filtered.copy()
    visible["last_touch_date"] = visible["last_touch_date"].dt.strftime("%Y-%m-%d")
    st.dataframe(
        visible,
        use_container_width=True,
        hide_index=True,
        column_config={
            "contact_name": st.column_config.TextColumn("Контакт", width="medium"),
            "organization": st.column_config.TextColumn("Организация", width="medium"),
            "role": st.column_config.TextColumn("Роль"),
            "segment": st.column_config.TextColumn("Сегмент"),
            "stage": st.column_config.TextColumn("Стадия"),
            "last_touch_date": st.column_config.TextColumn("Последний контакт"),
            "next_step": st.column_config.TextColumn("Следующий шаг", width="large"),
            "source": st.column_config.TextColumn("Источник"),
            "links": st.column_config.TextColumn("Ссылки", width="large"),
            "notes": st.column_config.TextColumn("Заметки", width="large"),
        },
    )


def show_research_library_section() -> None:
    df = load_research_library_data()
    col1, col2 = st.columns(2)
    with col1:
        item_types = multiselect_main_filter("Тип материала", df["item_type"], "research_item_type")
    with col2:
        themes = multiselect_main_filter("Тема", df["theme"], "research_theme")
    query = st.text_input("Поиск по материалам", key="research_query")

    filtered = df.copy()
    if item_types:
        filtered = filtered[filtered["item_type"].isin(item_types)]
    if themes:
        filtered = filtered[filtered["theme"].isin(themes)]
    if query:
        haystack = (
            filtered["title"].fillna("")
            + " "
            + filtered["summary"].fillna("")
            + " "
            + filtered["why_it_matters"].fillna("")
            + " "
            + filtered["tags"].fillna("")
        ).str.lower()
        filtered = filtered[haystack.str.contains(query.lower(), na=False)]

    st.dataframe(
        filtered,
        use_container_width=True,
        hide_index=True,
        column_config={
            "title": st.column_config.TextColumn("Материал", width="large"),
            "item_type": st.column_config.TextColumn("Тип"),
            "theme": st.column_config.TextColumn("Тема"),
            "geography": st.column_config.TextColumn("География"),
            "source_name": st.column_config.TextColumn("Источник"),
            "source_url": st.column_config.LinkColumn("Ссылка"),
            "summary": st.column_config.TextColumn("Summary", width="large"),
            "why_it_matters": st.column_config.TextColumn("Почему важно", width="large"),
            "related_idea": st.column_config.TextColumn("Связанная идея", width="medium"),
            "tags": st.column_config.TextColumn("Теги", width="medium"),
        },
    )

    for row in filtered.to_dict(orient="records"):
        with st.expander(f'{row["title"]} • {row["item_type"]} • {row["theme"]}'):
            st.markdown(f'**География:** {row["geography"]}')
            st.markdown(f'**Источник:** {row["source_name"] or "нет"}')
            if row["source_url"]:
                st.markdown(f'**Ссылка:** [открыть]({row["source_url"]})')
            st.markdown(f'**Summary:** {row["summary"]}')
            st.markdown(f'**Почему важно:** {row["why_it_matters"]}')
            st.markdown(f'**Связанная идея:** {row["related_idea"] or "нет"}')
            st.markdown(f'**Теги:** {row["tags"] or "нет"}')


def show_workspace_tab() -> None:
    st.subheader("Рабочее пространство")
    st.caption(
        "Совместный контур для venture discovery: идеи, backlog, контакты, материалы, "
        "артефакты и generated dashboards."
    )

    show_workspace_overview()
    st.divider()

    tab_docs, tab_ideas, tab_tasks, tab_contacts, tab_research = st.tabs(
        ["Вики", "Идеи", "Задачи", "Контакты", "Материалы"]
    )

    with tab_docs:
        show_workspace_docs()

    with tab_ideas:
        show_ideas_section()

    with tab_tasks:
        show_tasks_section()

    with tab_contacts:
        show_contacts_section()

    with tab_research:
        show_research_library_section()


def multiselect_main_filter(label: str, series: pd.Series, key: str) -> list[str]:
    options = sorted([value for value in series.dropna().unique().tolist() if value])
    return st.multiselect(label, options, key=key, placeholder="Выберите варианты")


def apply_adoption_filters(df: pd.DataFrame) -> pd.DataFrame:
    st.subheader("Фильтры по сигналам")

    col1, col2, col3 = st.columns(3)
    with col1:
        geography = multiselect_main_filter("География", df["geography_bucket"], "adoption_geography")
    with col2:
        sectors = multiselect_main_filter("Контур", df["sector"], "adoption_sector")
    with col3:
        relation_types = multiselect_main_filter("Тип сигнала", df["relation_type"], "adoption_relation")

    col4, col5, col6 = st.columns(3)
    with col4:
        usage_patterns = multiselect_main_filter("Паттерн", df["usage_pattern"], "adoption_pattern")
    with col5:
        countries = multiselect_main_filter("Страна", df["country"], "adoption_country")
    with col6:
        source_types = multiselect_main_filter("Тип источника", df["source_type"], "adoption_source_type")

    query = st.text_input(
        "Поиск по продукту, организации, описанию",
        key="adoption_query",
    )

    filtered = df.copy()

    if geography:
        filtered = filtered[filtered["geography_bucket"].isin(geography)]

    if sectors:
        filtered = filtered[filtered["sector"].isin(sectors)]

    if relation_types:
        filtered = filtered[filtered["relation_type"].isin(relation_types)]

    if usage_patterns:
        filtered = filtered[filtered["usage_pattern"].isin(usage_patterns)]

    if countries:
        filtered = filtered[filtered["country"].isin(countries)]

    if source_types:
        filtered = filtered[filtered["source_type"].isin(source_types)]

    if query:
        haystack = (
            filtered["startup_or_product"].fillna("")
            + " "
            + filtered["organization"].fillna("")
            + " "
            + filtered["organization_type"].fillna("")
            + " "
            + filtered["summary"].fillna("")
            + " "
            + filtered["why_it_matters"].fillna("")
        ).str.lower()
        filtered = filtered[haystack.str.contains(query.lower(), na=False)]

    return filtered.sort_values(
        by=["geography_bucket", "sector", "published_date", "startup_or_product", "organization"],
        ascending=[True, True, False, True, True],
    )


def show_adoption_metrics(df: pd.DataFrame) -> None:
    russia_count = int((df["geography_bucket"] == "Россия").sum())
    org_count = df["organization"].nunique()
    product_count = df["startup_or_product"].nunique()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Упоминаний", len(df))
    col2.metric("Организаций", org_count)
    col3.metric("Россия", russia_count)
    col4.metric("Продуктов / платформ", product_count)


def show_adoption_table(df: pd.DataFrame) -> None:
    visible = df[
        [
            "startup_or_product",
            "relation_type",
            "sector",
            "usage_pattern",
            "geography_bucket",
            "country",
            "organization",
            "organization_type",
            "source_type",
            "published_date",
            "source_name",
            "source_url",
            "summary",
            "why_it_matters",
        ]
    ].copy()
    visible["published_date"] = visible["published_date"].dt.strftime("%Y-%m-%d")

    st.dataframe(
        visible,
        use_container_width=True,
        hide_index=True,
        column_config={
            "startup_or_product": st.column_config.TextColumn("Продукт / платформа", width="medium"),
            "relation_type": st.column_config.TextColumn("Тип сигнала"),
            "sector": st.column_config.TextColumn("Контур"),
            "usage_pattern": st.column_config.TextColumn("Паттерн", width="medium"),
            "geography_bucket": st.column_config.TextColumn("География"),
            "country": st.column_config.TextColumn("Страна"),
            "organization": st.column_config.TextColumn("Организация", width="medium"),
            "organization_type": st.column_config.TextColumn("Тип организации"),
            "source_type": st.column_config.TextColumn("Тип источника"),
            "published_date": st.column_config.TextColumn("Дата"),
            "source_name": st.column_config.TextColumn("Источник"),
            "source_url": st.column_config.LinkColumn("Ссылка"),
            "summary": st.column_config.TextColumn("Что используется", width="large"),
            "why_it_matters": st.column_config.TextColumn("Почему важно", width="large"),
        },
    )


def show_adoption_cards(df: pd.DataFrame) -> None:
    st.subheader("Карточки сигналов")
    for row in df.to_dict(orient="records"):
        published_date = "нет данных"
        if pd.notna(row["published_date"]):
            published_date = row["published_date"].strftime("%Y-%m-%d")
        title = (
            f'{row["startup_or_product"]} • {row["organization"]} '
            f'• {row["sector"]} • {row["geography_bucket"]}'
        )
        with st.expander(title):
            st.markdown(f'**Организация:** {row["organization"]}')
            st.markdown(f'**Тип организации:** {row["organization_type"]}')
            st.markdown(f'**Продукт / платформа:** {row["startup_or_product"]}')
            st.markdown(f'**Тип сигнала:** `{row["relation_type"]}`')
            st.markdown(f'**Контур:** `{row["sector"]}`')
            st.markdown(f'**География:** `{row["geography_bucket"]}`')
            st.markdown(f'**Паттерн:** `{row["usage_pattern"]}`')
            st.markdown(f'**Страна:** {row["country"]}')
            st.markdown(f'**Тип источника:** {row["source_type"]}')
            st.markdown(f'**Дата:** {published_date}')
            st.markdown(f'**Источник:** [{row["source_name"]}]({row["source_url"]})')
            st.markdown(f'**Что используется:** {row["summary"]}')
            st.markdown(f'**Почему важно для текущей thesis:** {row["why_it_matters"]}')


def show_adoption_tab() -> None:
    st.subheader("Рынок и сигналы")
    st.caption(
        "Customer stories, deployment signals, новости и наблюдения о том, как "
        "похожие продукты используются на рынке."
    )

    df = load_adoption_data()
    filtered = apply_adoption_filters(df)

    show_adoption_metrics(filtered)
    st.download_button(
        "Скачать CSV по внедрениям",
        data=ADOPTION_PATH.read_bytes(),
        file_name="adoption_mentions.csv",
        mime="text/csv",
    )
    st.divider()
    show_adoption_table(filtered)
    st.divider()
    show_adoption_cards(filtered)


def apply_artifact_filters(df: pd.DataFrame) -> pd.DataFrame:
    selected_artifacts = multiselect_main_filter(
        "Артефакты",
        df["artifact_name"],
        "artifact_name_filter",
    )

    filtered = df.copy()
    if selected_artifacts:
        filtered = filtered[filtered["artifact_name"].isin(selected_artifacts)]

    return filtered.sort_values(by=["artifact_group", "artifact_name"], ascending=[True, True])


def show_artifacts_context() -> None:
    st.subheader("Текущий продуктовый фокус")
    st.markdown(
        """
**Текущий режим:** shared venture discovery workspace.  
**Базовый контур:** `idea -> evidence -> competitor map -> contacts -> prototype -> decision`.  
**Задача первой версии:** дать один рабочий cockpit для команды и AI, а не разрозненный набор чатов и заметок.
"""
    )


def read_artifact_content(path_value: str) -> tuple[bool, str]:
    if not path_value:
        return False, "Путь к артефакту не указан."

    path = resolve_artifact_path(path_value)
    if not path.exists():
        return False, f"Файл не найден: {path_value}"

    try:
        return True, path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return False, f"Не удалось прочитать файл как текст: {path_value}"


def resolve_artifact_path(path_value: str) -> Path:
    path = Path(path_value)
    project_root = Path(__file__).parent

    if path.exists():
        return path

    if not path.is_absolute():
        candidate = project_root / path
        if candidate.exists():
            return candidate

    parts = path.parts
    if "artifacts" in parts:
        idx = parts.index("artifacts")
        candidate = project_root / Path(*parts[idx:])
        if candidate.exists():
            return candidate

    if path.name == "artifacts.md":
        candidate = project_root / "artifacts.md"
        if candidate.exists():
            return candidate

    candidate = project_root / path.name
    if candidate.exists():
        return candidate

    return path


def show_artifact_table(df: pd.DataFrame) -> None:
    st.subheader("Таблица артефактов")
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "artifact_name": st.column_config.TextColumn("Артефакт", width="medium"),
            "artifact_group": st.column_config.TextColumn("Группа"),
            "priority": st.column_config.TextColumn("Приоритет"),
            "status": st.column_config.TextColumn("Статус"),
            "completion_pct": st.column_config.ProgressColumn("Готовность", min_value=0, max_value=100),
            "evidence_score": st.column_config.NumberColumn("Доказательства", format="%.0f"),
            "validation_status": st.column_config.TextColumn("Валидация"),
            "target_user": st.column_config.TextColumn("Целевой пользователь", width="large"),
            "current_focus": st.column_config.TextColumn("Текущий фокус", width="large"),
            "deliverable_path": st.column_config.TextColumn("Путь к артефакту", width="medium"),
            "validation_method": st.column_config.TextColumn("Как валидировать", width="large"),
            "next_step": st.column_config.TextColumn("Следующий шаг", width="large"),
        },
    )


def show_artifact_cards(df: pd.DataFrame) -> None:
    st.subheader("Карточки артефактов")
    for row in df.to_dict(orient="records"):
        with st.expander(f'{row["artifact_name"]} • {row["status"]} • {int(row["completion_pct"])}%'):
            st.markdown(f'**Группа:** `{row["artifact_group"]}`')
            st.markdown(f'**Приоритет:** `{row["priority"]}`')
            st.markdown(f'**Статус валидации:** `{row["validation_status"]}`')
            st.markdown(f'**Целевой пользователь:** {row["target_user"]}')
            st.markdown(f'**Текущий фокус:** {row["current_focus"]}')
            st.markdown(f'**Готовность:** {int(row["completion_pct"])}%')
            st.markdown(f'**Уровень доказательств:** {int(row["evidence_score"])}/5')
            st.markdown(f'**Путь к артефакту:** `{row["deliverable_path"]}`')
            st.markdown(f'**Как валидировать:** {row["validation_method"]}')
            st.markdown(f'**Следующий шаг:** {row["next_step"]}')
            st.divider()
            st.markdown("**Содержимое артефакта**")
            ok, content = read_artifact_content(row["deliverable_path"])
            if ok:
                st.markdown(content)
            else:
                st.warning(content)


def show_artifacts_tab() -> None:
    st.subheader("Продуктовые артефакты")
    st.caption(
        "Discovery-артефакты, в которых фиксируются thesis, roles, JTBD, MVP, "
        "гипотезы и риски."
    )

    df = load_artifacts_data()
    filtered = apply_artifact_filters(df)

    show_artifacts_context()
    st.download_button(
        "Скачать CSV по артефактам",
        data=ARTIFACTS_PATH.read_bytes(),
        file_name="artifacts.csv",
        mime="text/csv",
    )
    st.download_button(
        "Скачать artifacts.md",
        data=(Path(__file__).parent / "artifacts.md").read_bytes(),
        file_name="artifacts.md",
        mime="text/markdown",
    )
    st.divider()
    show_artifact_table(filtered)
    st.divider()
    show_artifact_cards(filtered)


def get_authenticated_user_key() -> str:
    headers = getattr(st.context, "headers", {}) or {}
    for header in (
        "x-auth-request-email",
        "x-forwarded-email",
        "x-auth-request-user",
        "x-forwarded-user",
    ):
        value = headers.get(header)
        if value:
            return str(value)
    return "anonymous"


def openclaw_is_configured() -> bool:
    return bool(OPENCLAW_RESPONSES_URL)


def extract_openclaw_text(response_json: dict) -> str:
    output_text = response_json.get("output_text")
    if isinstance(output_text, str) and output_text.strip():
        return output_text.strip()

    chunks: list[str] = []
    for item in response_json.get("output", []):
        if isinstance(item, dict) and item.get("type") == "message":
            for content in item.get("content", []):
                if not isinstance(content, dict):
                    continue
                if content.get("type") == "output_text" and content.get("text"):
                    chunks.append(str(content["text"]))
                elif content.get("type") == "text" and content.get("text"):
                    chunks.append(str(content["text"]))

    text = "\n\n".join(chunk.strip() for chunk in chunks if chunk and chunk.strip())
    if text:
        return text

    return "OpenClaw вернул ответ без текстового блока."


def ask_openclaw(prompt: str, user_key: str) -> str:
    agent_profile = load_openclaw_agent_profile()
    headers = {
        "Content-Type": "application/json",
        "x-openclaw-agent-id": OPENCLAW_AGENT_ID,
    }
    if OPENCLAW_GATEWAY_TOKEN:
        headers["Authorization"] = f"Bearer {OPENCLAW_GATEWAY_TOKEN}"

    payload = {
        "model": "openclaw",
        "input": build_openclaw_prompt(prompt, agent_profile),
        "user": f"{OPENCLAW_CHAT_USER_PREFIX}:{user_key}",
    }

    response = requests.post(
        OPENCLAW_RESPONSES_URL,
        headers=headers,
        json=payload,
        timeout=600,
    )
    response.raise_for_status()
    return extract_openclaw_text(response.json())


def run_chat_turn(raw_prompt: str, mode_key: str) -> str:
    prompt = build_mode_prompt(raw_prompt, mode_key)
    user_key = get_authenticated_user_key()
    return ask_openclaw(prompt, user_key)


def build_openclaw_prompt(user_prompt: str, agent_profile: str) -> str:
    if not agent_profile:
        return user_prompt

    return (
        "Ниже дан твой постоянный профиль агента и затем новый запрос пользователя.\n\n"
        "=== ПРОФИЛЬ АГЕНТА ===\n"
        f"{agent_profile}\n\n"
        "=== ЗАПРОС ПОЛЬЗОВАТЕЛЯ ===\n"
        f"{user_prompt}"
    )


def build_mode_prompt(user_prompt: str, mode_key: str) -> str:
    mode_config = CHAT_MODE_CONFIG.get(mode_key)
    if not mode_config:
        return user_prompt

    files = "\n".join(f"- {path}" for path in mode_config["files"])
    dashboard_rules = (
        "Если пользователь просит создать новый дашборд или доработать существующий Streamlit-дашборд, "
        "используй такие правила:\n"
        f"- для lightweight dashboard создай или обнови markdown-файл в `{GENERATED_DASHBOARDS_DIR.name}/<slug>.md`\n"
        f"- после создания или обновления верни ссылку формата `{MAIN_DASHBOARD_PUBLIC_URL}?dashboard=<slug>`\n"
        "- если нужно менять основной Streamlit-интерфейс или чат-дашборд, редактируй `app.py` и связанные deploy-файлы\n"
        "- не обещай ссылку, пока не определил slug дашборда явно\n"
    )
    return (
        f"{mode_config['context']}\n\n"
        "При ответе опирайся в первую очередь на эти файлы проекта:\n"
        f"{files}\n\n"
        f"{dashboard_rules}\n"
        "Новый запрос:\n"
        f"{user_prompt}"
    )


def get_chat_messages(mode_key: str) -> list[dict[str, str]]:
    history_key = f"chat_messages_{mode_key}"
    mode_label = CHAT_MODE_CONFIG[mode_key]["label"]
    mode_description = CHAT_MODE_CONFIG[mode_key]["description"]
    default_message = {
        "role": "assistant",
        "content": (
            f"Режим `{mode_label}`.\n\n"
            f"{mode_description}\n\n"
            "Спроси меня про проект, и я отвечу как рабочий агент OpenClaw."
        ),
    }
    if history_key not in st.session_state:
        st.session_state[history_key] = [default_message]
    return st.session_state[history_key]


def set_chat_messages(mode_key: str, messages: list[dict[str, str]]) -> None:
    st.session_state[f"chat_messages_{mode_key}"] = messages


def render_quick_chat_actions(mode_key: str) -> str | None:
    quick_prompts = CHAT_MODE_CONFIG[mode_key]["quick_prompts"]
    columns = st.columns(len(quick_prompts))
    for index, quick_prompt in enumerate(quick_prompts):
        if columns[index].button(
            quick_prompt,
            key=f"quick_prompt_{mode_key}_{index}",
            use_container_width=True,
        ):
            return quick_prompt
    return None


def render_top_navigation(view: str) -> None:
    main_link = MAIN_DASHBOARD_PUBLIC_URL
    chat_link = CHAT_DASHBOARD_PUBLIC_URL
    if view == "chat":
        st.markdown(f"[Открыть основной workspace]({main_link})")
    else:
        st.markdown(f"[Открыть чат-дашборд]({chat_link})")


def show_generated_dashboards_tab() -> None:
    st.subheader("Созданные дашборды")
    st.caption(
        "Здесь отображаются lightweight views, созданные или обновленные через чатбота OpenClaw."
    )

    dashboards = list_generated_dashboards()
    if not dashboards:
        st.info(
            "Пока нет созданных generated dashboards. Попроси чатбота создать dashboard и вернуть ссылку."
        )
        return

    for dashboard in dashboards:
        with st.container(border=True):
            st.markdown(f"### {dashboard['title']}")
            st.markdown(f"**Slug:** `{dashboard['slug']}`")
            st.markdown(f"**Ссылка:** [{dashboard['link']}]({dashboard['link']})")
            st.markdown(f"**Файл:** `{dashboard['path']}`")
            preview = dashboard["content"][:600].strip()
            if preview:
                st.markdown(preview)


def show_generated_dashboard_page(slug: str) -> None:
    dashboard = find_generated_dashboard(slug)
    if dashboard is None:
        st.title("Дашборд не найден")
        st.error(f"Не удалось найти generated dashboard со slug `{slug}`.")
        render_top_navigation("generated")
        return

    st.title(dashboard["title"])
    st.caption(f"Generated dashboard: `{dashboard['slug']}`")
    render_top_navigation("generated")
    st.markdown(
        f"[Назад к основному workspace]({MAIN_DASHBOARD_PUBLIC_URL}) | "
        f"[Открыть чат-дашборд]({CHAT_DASHBOARD_PUBLIC_URL})"
    )
    st.divider()
    st.markdown(dashboard["content"])


def show_chat_tab() -> None:
    st.subheader("Чат-бот")
    st.caption(
        "Интерфейс для работы с OpenClaw по venture discovery, knowledge base и changes в workspace. "
        "Контракт рассчитан на OpenResponses API `POST /v1/responses`."
    )
    render_top_navigation("chat")
    mode_key = st.selectbox(
        "Режим работы",
        list(CHAT_MODE_CONFIG.keys()),
        format_func=lambda value: CHAT_MODE_CONFIG[value]["label"],
    )
    mode_config = CHAT_MODE_CONFIG[mode_key]
    messages = get_chat_messages(mode_key)

    st.caption(
        f"Сейчас активен режим: **{mode_config['label']}**. "
        f"{mode_config['description']}"
    )

    with st.expander("Статус backend", expanded=not openclaw_is_configured()):
        st.markdown(f"**OpenClaw endpoint:** `{OPENCLAW_RESPONSES_URL or 'не задан'}`")
        st.markdown(f"**Agent ID:** `{OPENCLAW_AGENT_ID}`")
        st.markdown(f"**Пользователь:** `{get_authenticated_user_key()}`")
        if openclaw_is_configured():
            st.success("Контракт OpenClaw задан. После деплоя серверный tab сможет ходить в gateway.")
        else:
            st.warning(
                "Переменная `OPENCLAW_RESPONSES_URL` пока не задана. "
                "После серверного деплоя tab начнет отправлять запросы в OpenClaw."
            )

    with st.expander("Профиль агента", expanded=False):
        agent_profile = load_openclaw_agent_profile()
        if agent_profile:
            st.markdown(agent_profile)
        else:
            st.warning("Файл `openclaw_agent.md` не найден.")

    with st.expander("Инструкции OpenClaw x Streamlit", expanded=False):
        streamlit_guide = load_openclaw_streamlit_guide()
        if streamlit_guide:
            st.markdown(streamlit_guide)
        else:
            st.warning("Файл `openclaw_streamlit.md` не найден.")

    with st.expander("Фокус режима", expanded=False):
        st.markdown(f"**Что делает режим:** {mode_config['description']}")
        st.markdown("**Ключевые файлы:**")
        for path in mode_config["files"]:
            st.markdown(f"- `{path}`")

    st.markdown("**Быстрые действия**")
    selected_quick_prompt = render_quick_chat_actions(mode_key)

    if st.button("Очистить диалог", key=f"clear_chat_history_{mode_key}"):
        set_chat_messages(mode_key, messages[:1])
        st.rerun()

    for message in messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = selected_quick_prompt or st.chat_input(
        "Напиши вопрос по workspace, идеям, материалам, конкурентам или разработке"
    )
    if not prompt:
        return

    messages.append({"role": "user", "content": prompt})
    set_chat_messages(mode_key, messages)
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        if not openclaw_is_configured():
            reply = (
                "Чат-контур уже добавлен, но OpenClaw backend еще не подключен к этому окружению. "
                "После деплоя на сервере запросы пойдут в `OPENCLAW_RESPONSES_URL`."
            )
            st.markdown(reply)
        else:
            try:
                reply = run_chat_turn(prompt, mode_key)
                st.markdown(reply)
            except requests.HTTPError as exc:
                response_text = exc.response.text[:500] if exc.response is not None else ""
                reply = f"OpenClaw вернул HTTP-ошибку: `{exc}`\n\n{response_text}"
                st.error(reply)
            except requests.RequestException as exc:
                reply = f"Не удалось связаться с OpenClaw: `{exc}`"
                st.error(reply)

    messages.append({"role": "assistant", "content": reply})
    set_chat_messages(mode_key, messages)


def main() -> None:
    query_params = st.query_params
    dashboard_slug = str(query_params.get("dashboard", "")).strip()
    view = str(query_params.get("view", "")).strip().lower()

    if dashboard_slug:
        show_generated_dashboard_page(dashboard_slug)
        return

    if view == "chat":
        st.title("Moreforms: чат-дашборд")
        st.caption(
            "Отдельный chat workspace для работы с OpenClaw по стратегии, research, knowledge base и изменениям дашбордов."
        )
        show_chat_tab()
        return

    st.title("Moreforms: discovery workspace")
    st.caption(
        "Shared cockpit для venture discovery: идеи, задачи, контакты, research materials, "
        "конкуренты, артефакты и generated dashboards."
    )
    render_top_navigation("main")

    tab_workspace, tab_competitors, tab_adoption, tab_artifacts, tab_generated = st.tabs(
        ["Рабочее пространство", "Конкуренты", "Рынок и сигналы", "Артефакты", "Созданные дашборды"]
    )

    with tab_workspace:
        show_workspace_tab()

    with tab_competitors:
        df = load_data()
        filtered = apply_filters(df)

        show_metrics(filtered)
        st.download_button(
            "Скачать CSV",
            data=DATA_PATH.read_bytes(),
            file_name="competitors.csv",
            mime="text/csv",
        )
        st.divider()
        show_tabbed_views(filtered)

    with tab_adoption:
        show_adoption_tab()

    with tab_artifacts:
        show_artifacts_tab()

    with tab_generated:
        show_generated_dashboards_tab()


if __name__ == "__main__":
    main()
