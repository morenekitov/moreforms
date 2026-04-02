import streamlit as st

from streamlit_app.components.tables import to_frame
from streamlit_app.services.api import safe_get


def render() -> None:
    st.subheader("Гипотезы")
    ok, payload, error = safe_get("/hypotheses")
    if not ok:
        st.error(f"Не удалось загрузить гипотезы: {error}")
        return

    frame = to_frame(payload)
    if frame.empty:
        st.info("Гипотез пока нет.")
        return

    filters = st.columns(4)
    segment = filters[0].selectbox("Сегмент", ["Все"] + sorted(frame["segment"].dropna().astype(str).unique().tolist()))
    assumption_type = filters[1].selectbox(
        "Тип гипотезы",
        ["Все"] + sorted(frame["assumption_type"].dropna().astype(str).unique().tolist()),
    )
    status = filters[2].selectbox("Статус", ["Все"] + sorted(frame["status"].dropna().astype(str).unique().tolist()))
    owner = filters[3].selectbox(
        "Owner",
        ["Все"] + sorted(frame["owner_user_id"].dropna().astype(str).unique().tolist()),
    )

    filtered = frame.copy()
    if segment != "Все":
        filtered = filtered[filtered["segment"] == segment]
    if assumption_type != "Все":
        filtered = filtered[filtered["assumption_type"] == assumption_type]
    if status != "Все":
        filtered = filtered[filtered["status"] == status]
    if owner != "Все":
        filtered = filtered[filtered["owner_user_id"] == owner]

    st.dataframe(filtered, use_container_width=True, hide_index=True)
