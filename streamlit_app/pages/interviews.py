import streamlit as st

from streamlit_app.components.tables import to_frame
from streamlit_app.services.api import safe_get


def render() -> None:
    st.subheader("Интервью")
    ok, payload, error = safe_get("/interviews")
    if not ok:
        st.error(f"Не удалось загрузить интервью: {error}")
        return

    frame = to_frame(payload)
    if frame.empty:
        st.info("Интервью пока нет.")
        return

    filters = st.columns(4)
    status = filters[0].selectbox("Статус", ["Все"] + sorted(frame["status"].dropna().astype(str).unique().tolist()))
    hypothesis_id = filters[1].selectbox(
        "Гипотеза",
        ["Все"] + sorted(frame["hypothesis_id"].dropna().astype(str).unique().tolist()),
    )
    contact_id = filters[2].selectbox(
        "Контакт",
        ["Все"] + sorted(frame["contact_id"].dropna().astype(str).unique().tolist()),
    )
    company_id = filters[3].selectbox(
        "Компания",
        ["Все"] + sorted(frame["company_id"].dropna().astype(str).unique().tolist()),
    )

    filtered = frame.copy()
    if status != "Все":
        filtered = filtered[filtered["status"] == status]
    if hypothesis_id != "Все":
        filtered = filtered[filtered["hypothesis_id"] == hypothesis_id]
    if contact_id != "Все":
        filtered = filtered[filtered["contact_id"] == contact_id]
    if company_id != "Все":
        filtered = filtered[filtered["company_id"] == company_id]

    st.dataframe(filtered, use_container_width=True, hide_index=True)
