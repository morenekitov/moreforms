import streamlit as st

from streamlit_app.components.tables import show_table
from streamlit_app.services.api import safe_get


def render() -> None:
    st.subheader("Инсайты")
    ok, payload, error = safe_get("/insights")
    if not ok:
        st.error(f"Не удалось загрузить инсайты: {error}")
        return
    show_table(payload, "Инсайтов пока нет.")
