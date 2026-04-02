import streamlit as st

from streamlit_app.pages import decisions, hypotheses, insights, interviews, overview, wiki
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

    tabs = st.tabs(["Обзор", "Гипотезы", "Интервью", "Инсайты", "Решения", "Wiki"])
    with tabs[0]:
        overview.render()
    with tabs[1]:
        hypotheses.render()
    with tabs[2]:
        interviews.render()
    with tabs[3]:
        insights.render()
    with tabs[4]:
        decisions.render()
    with tabs[5]:
        wiki.render()


if __name__ == "__main__":
    main()
