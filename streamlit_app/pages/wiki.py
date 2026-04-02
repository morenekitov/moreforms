import streamlit as st

from streamlit_app.components.tables import show_table
from streamlit_app.services.api import safe_get


def render() -> None:
    st.subheader("Wiki / Notes")
    ok, payload, error = safe_get("/pages")
    if not ok:
        st.error(f"Не удалось загрузить страницы: {error}")
        return
    show_table(payload, "Wiki-страниц пока нет.")
