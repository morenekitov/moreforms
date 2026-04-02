import streamlit as st

from streamlit_app.components.tables import show_table
from streamlit_app.services.api import safe_get


def render() -> None:
    st.subheader("Гипотезы")
    ok, payload, error = safe_get("/hypotheses")
    if not ok:
        st.error(f"Не удалось загрузить гипотезы: {error}")
        return
    show_table(payload, "Гипотез пока нет.")
