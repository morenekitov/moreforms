import streamlit as st

from streamlit_app.components.tables import show_table
from streamlit_app.services.api import safe_get


def render() -> None:
    st.subheader("Интервью")
    ok, payload, error = safe_get("/interviews")
    if not ok:
        st.error(f"Не удалось загрузить интервью: {error}")
        return
    show_table(payload, "Интервью пока нет.")
