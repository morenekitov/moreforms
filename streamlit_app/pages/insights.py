import streamlit as st

from streamlit_app.components.tables import to_frame
from streamlit_app.services.api import safe_get


def render() -> None:
    st.subheader("Инсайты")
    ok, payload, error = safe_get("/insights")
    if not ok:
        st.error(f"Не удалось загрузить инсайты: {error}")
        return

    frame = to_frame(payload)
    if frame.empty:
        st.info("Инсайтов пока нет.")
        return

    filters = st.columns(3)
    insight_type = filters[0].selectbox("Тип", ["Все"] + sorted(frame["type"].dropna().astype(str).unique().tolist()))
    strength = filters[1].selectbox(
        "Сила сигнала",
        ["Все"] + sorted(frame["strength"].dropna().astype(str).unique().tolist()),
    )
    hypothesis_id = filters[2].selectbox(
        "Гипотеза",
        ["Все"] + sorted(frame["hypothesis_id"].dropna().astype(str).unique().tolist()),
    )

    filtered = frame.copy()
    if insight_type != "Все":
        filtered = filtered[filtered["type"] == insight_type]
    if strength != "Все":
        filtered = filtered[filtered["strength"] == strength]
    if hypothesis_id != "Все":
        filtered = filtered[filtered["hypothesis_id"] == hypothesis_id]

    st.dataframe(filtered, use_container_width=True, hide_index=True)
