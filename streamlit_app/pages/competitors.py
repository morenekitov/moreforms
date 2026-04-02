import streamlit as st

from streamlit_app.components.tables import to_frame
from streamlit_app.services.api import safe_get


def render() -> None:
    st.subheader("Конкуренты")
    ok, payload, error = safe_get("/competitors")
    if not ok:
        st.error(f"Не удалось загрузить конкурентов: {error}")
        return

    frame = to_frame(payload)
    if frame.empty:
        st.info("Конкурентов пока нет.")
        return

    filters = st.columns(2)
    segment = filters[0].selectbox("Сегмент", ["Все"] + sorted(frame["segment"].dropna().astype(str).unique().tolist()))
    product_type = filters[1].selectbox(
        "Тип продукта",
        ["Все"] + sorted(frame["product_type"].dropna().astype(str).unique().tolist()),
    )

    filtered = frame.copy()
    if segment != "Все":
        filtered = filtered[filtered["segment"] == segment]
    if product_type != "Все":
        filtered = filtered[filtered["product_type"] == product_type]

    st.dataframe(filtered, use_container_width=True, hide_index=True)
