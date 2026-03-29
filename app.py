from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(
    page_title="Moreforms: продуктовая карта",
    page_icon="📊",
    layout="wide",
)

DATA_PATH = Path(__file__).parent / "data" / "competitors.csv"
ADOPTION_PATH = Path(__file__).parent / "data" / "adoption_mentions.csv"
ARTIFACTS_PATH = Path(__file__).parent / "data" / "artifacts.csv"
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
        "makers, educators, and small teams": "мейкеры, преподаватели и небольшие команды",
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
    direct_count = int((df["similarity_type"] == "direct").sum())
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
            st.markdown(f'**Релевантность для РФ:** {row["rf_pilot_relevance"]}')
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


def multiselect_main_filter(label: str, series: pd.Series, key: str) -> list[str]:
    options = sorted([value for value in series.dropna().unique().tolist() if value])
    return st.multiselect(label, options, key=key, placeholder="Выберите варианты")


def apply_adoption_filters(df: pd.DataFrame) -> pd.DataFrame:
    st.subheader("Фильтры по внедрениям")

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
    st.subheader("Карточки внедрений")
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
            st.markdown(f'**Почему важно для moreforms:** {row["why_it_matters"]}')


def show_adoption_tab() -> None:
    st.subheader("Внедрения и рыночные сигналы")
    st.caption(
        "Точечные кейсы и официальные сигналы по использованию похожих продуктов "
        "в вузах, образовании, ФОИВ, ведомствах и администрациях."
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
    st.subheader("Фильтры по артефактам")

    col1, col2, col3 = st.columns(3)
    with col1:
        groups = multiselect_main_filter("Группа артефакта", df["artifact_group"], "artifact_group")
    with col2:
        priorities = multiselect_main_filter("Приоритет", df["priority"], "artifact_priority")
    with col3:
        statuses = multiselect_main_filter("Статус", df["status"], "artifact_status")

    col4, col5 = st.columns(2)
    with col4:
        validation_statuses = multiselect_main_filter(
            "Статус валидации",
            df["validation_status"],
            "artifact_validation_status",
        )
    with col5:
        query = st.text_input(
            "Поиск по артефакту, фокусу, следующему шагу",
            key="artifact_query",
        )

    filtered = df.copy()

    if groups:
        filtered = filtered[filtered["artifact_group"].isin(groups)]

    if priorities:
        filtered = filtered[filtered["priority"].isin(priorities)]

    if statuses:
        filtered = filtered[filtered["status"].isin(statuses)]

    if validation_statuses:
        filtered = filtered[filtered["validation_status"].isin(validation_statuses)]

    if query:
        haystack = (
            filtered["artifact_name"].fillna("")
            + " "
            + filtered["target_user"].fillna("")
            + " "
            + filtered["current_focus"].fillna("")
            + " "
            + filtered["validation_method"].fillna("")
            + " "
            + filtered["next_step"].fillna("")
        ).str.lower()
        filtered = filtered[haystack.str.contains(query.lower(), na=False)]

    return filtered.sort_values(
        by=["priority", "completion_pct", "artifact_group", "artifact_name"],
        ascending=[True, False, True, True],
    )


def show_artifacts_context() -> None:
    st.subheader("Текущий продуктовый фокус")
    st.markdown(
        """
**Сегмент первой итерации:** вузы, административный персонал, руководители курсов и преподаватели.  
**Базовый сценарий:** `текст или видео -> автосоздание Яндекс.Формы -> загрузка результатов -> дашборд по промпту`.  
**Продуктовая цель первой версии:** сократить ручную сборку форм, ускорить анализ Excel и опросных данных и дать понятные шаблоны визуализации без отдельного аналитика.
"""
    )


def show_artifact_metrics(df: pd.DataFrame) -> None:
    avg_completion = df["completion_pct"].mean()
    avg_evidence = df["evidence_score"].mean()
    critical_count = int((df["priority"] == "Критично").sum())
    validated_count = int((df["validation_status"] != "Не валидировано").sum())

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Артефактов", len(df))
    col2.metric("Средняя готовность", f"{avg_completion:.0f}%")
    col3.metric("Средний уровень доказательств", f"{avg_evidence:.1f}/5")
    col4.metric("С валидацией", validated_count if validated_count else critical_count)


def show_artifact_charts(df: pd.DataFrame) -> None:
    col1, col2 = st.columns(2)

    status_counts = (
        df.groupby("status", as_index=False)
        .size()
        .rename(columns={"size": "count"})
        .sort_values("count", ascending=False)
    )
    fig_status = px.bar(
        status_counts,
        x="status",
        y="count",
        color="status",
        text="count",
        title="Статус продуктовых артефактов",
    )
    fig_status.update_layout(showlegend=False, margin=dict(l=20, r=20, t=60, b=20))

    priority_validation = (
        df.groupby(["priority", "validation_status"], as_index=False)
        .size()
        .rename(columns={"size": "count"})
    )
    fig_validation = px.bar(
        priority_validation,
        x="priority",
        y="count",
        color="validation_status",
        barmode="stack",
        text="count",
        title="Приоритет и уровень валидации",
    )
    fig_validation.update_layout(margin=dict(l=20, r=20, t=60, b=20))

    with col1:
        st.plotly_chart(fig_status, use_container_width=True)
    with col2:
        st.plotly_chart(fig_validation, use_container_width=True)

    scatter = px.scatter(
        df,
        x="completion_pct",
        y="evidence_score",
        color="priority",
        size="completion_pct",
        hover_name="artifact_name",
        hover_data={
            "artifact_group": True,
            "status": True,
            "validation_status": True,
            "completion_pct": True,
            "evidence_score": True,
        },
        title="Готовность артефактов и сила подтверждения",
        labels={
            "completion_pct": "Готовность, %",
            "evidence_score": "Уровень доказательств, 1-5",
        },
    )
    scatter.update_layout(margin=dict(l=20, r=20, t=60, b=20))
    st.plotly_chart(scatter, use_container_width=True)


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
            st.markdown(f'**Путь к артефакту:** [{row["deliverable_path"]}]({row["deliverable_path"]})')
            st.markdown(f'**Как валидировать:** {row["validation_method"]}')
            st.markdown(f'**Следующий шаг:** {row["next_step"]}')


def show_artifacts_tab() -> None:
    st.subheader("Продуктовые артефакты")
    st.caption(
        "Контур продуктовой проработки для текущей гипотезы: "
        "генерация Яндекс.Форм из текста или видео и анализ результатов в вузах."
    )

    df = load_artifacts_data()
    filtered = apply_artifact_filters(df)

    show_artifacts_context()
    show_artifact_metrics(filtered)
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
    show_artifact_charts(filtered)
    st.divider()
    show_artifact_table(filtered)
    st.divider()
    show_artifact_cards(filtered)


def main() -> None:
    st.title("Moreforms: продуктовая карта")
    st.caption(
        "Конкуренты, внедренческие сигналы и продуктовые артефакты "
        "для гипотезы форм и аналитики данных в вузах."
    )

    tab_competitors, tab_adoption, tab_artifacts = st.tabs(
        ["Конкуренты", "Внедрения и сигналы", "Продуктовые артефакты"]
    )

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


if __name__ == "__main__":
    main()
