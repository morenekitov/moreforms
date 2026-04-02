import streamlit as st

from streamlit_app.components.tables import to_frame
from streamlit_app.services.api import safe_get


def render() -> None:
    st.subheader("Решения")
    ok, payload, error = safe_get("/decisions")
    if not ok:
        st.error(f"Не удалось загрузить решения: {error}")
        return

    frame = to_frame(payload)
    if frame.empty:
        st.info("Решений пока нет.")
        return

    st.dataframe(frame, use_container_width=True, hide_index=True)
