import streamlit as st

from streamlit_app.pages import competitors, contacts, decisions, hypotheses, insights, interviews, overview, signals, wiki
from streamlit_app.services.api import API_BASE_URL, safe_get


st.set_page_config(page_title="moreforms v1", page_icon="📘", layout="wide")


def main() -> None:
    st.title("moreforms v1")
    st.caption("Read-layer для startup discovery system. Запись данных предполагается через Codex / agent workflows.")

    ok, _, error = safe_get("/health")
    with st.expander("Статус backend", expanded=not ok):
        st.write(f"API base URL: `{API_BASE_URL}`")
        if ok:
            st.success("Backend отвечает.")
        else:
            st.error(f"Backend недоступен: {error}")

    tabs = st.tabs(["Обзор", "Гипотезы", "Контакты", "Интервью", "Инсайты", "Сигналы", "Конкуренты", "Решения", "Wiki"])
    with tabs[0]:
        overview.render()
    with tabs[1]:
        hypotheses.render()
    with tabs[2]:
        contacts.render()
    with tabs[3]:
        interviews.render()
    with tabs[4]:
        insights.render()
    with tabs[5]:
        signals.render()
    with tabs[6]:
        competitors.render()
    with tabs[7]:
        decisions.render()
    with tabs[8]:
        wiki.render()


if __name__ == "__main__":
    main()
