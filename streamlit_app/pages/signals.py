import streamlit as st

from streamlit_app.components.tables import to_frame
from streamlit_app.services.api import safe_get


def render() -> None:
    st.subheader("Сигналы рынка")
    ok, payload, error = safe_get("/signals")
    if not ok:
        st.error(f"Не удалось загрузить сигналы: {error}")
        return

    frame = to_frame(payload)
    if frame.empty:
        st.info("Сигналов пока нет.")
        return

    filters = st.columns(3)
    segment = filters[0].selectbox("Сегмент", ["Все"] + sorted(frame["segment"].dropna().astype(str).unique().tolist()))
    signal_type = filters[1].selectbox(
        "Тип сигнала",
        ["Все"] + sorted(frame["signal_type"].dropna().astype(str).unique().tolist()),
    )
    strength = filters[2].selectbox("Сила сигнала", ["Все"] + sorted(frame["strength"].dropna().astype(str).unique().tolist()))

    filtered = frame.copy()
    if segment != "Все":
        filtered = filtered[filtered["segment"] == segment]
    if signal_type != "Все":
        filtered = filtered[filtered["signal_type"] == signal_type]
    if strength != "Все":
        filtered = filtered[filtered["strength"] == strength]

    st.dataframe(filtered, use_container_width=True, hide_index=True)
