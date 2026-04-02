import streamlit as st

from streamlit_app.components.tables import to_frame
from streamlit_app.services.api import safe_get


def render() -> None:
    st.subheader("Контакты")
    ok, payload, error = safe_get("/contacts")
    if not ok:
        st.error(f"Не удалось загрузить контакты: {error}")
        return

    frame = to_frame(payload)
    if frame.empty:
        st.info("Контактов пока нет.")
        return

    filters = st.columns(4)
    role = filters[0].selectbox("Роль", ["Все"] + sorted(frame["role"].dropna().astype(str).unique().tolist()))
    company_id = filters[1].selectbox(
        "Компания",
        ["Все"] + sorted(frame["company_id"].dropna().astype(str).unique().tolist()),
    )
    segment = filters[2].selectbox(
        "Сегмент",
        ["Все"] + sorted(frame["segment"].dropna().astype(str).unique().tolist()),
    )
    source = filters[3].selectbox(
        "Источник",
        ["Все"] + sorted(frame["source"].dropna().astype(str).unique().tolist()),
    )

    filtered = frame.copy()
    if role != "Все":
        filtered = filtered[filtered["role"] == role]
    if company_id != "Все":
        filtered = filtered[filtered["company_id"] == company_id]
    if segment != "Все":
        filtered = filtered[filtered["segment"] == segment]
    if source != "Все":
        filtered = filtered[filtered["source"] == source]

    st.dataframe(filtered, use_container_width=True, hide_index=True)
