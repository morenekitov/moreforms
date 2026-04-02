import streamlit as st

from streamlit_app.components.tables import to_frame
from streamlit_app.services.api import safe_get


def render() -> None:
    st.subheader("Wiki / Notes")
    ok, payload, error = safe_get("/pages")
    if not ok:
        st.error(f"Не удалось загрузить страницы: {error}")
        return

    frame = to_frame(payload)
    if frame.empty:
        st.info("Wiki-страниц пока нет.")
        return

    query = st.text_input("Поиск по заголовку и контенту")
    if query:
        lowered = query.lower()
        frame = frame[
            frame.apply(
                lambda row: lowered in str(row.get("title", "")).lower()
                or lowered in str(row.get("content_md", "")).lower(),
                axis=1,
            )
        ]

    st.dataframe(frame, use_container_width=True, hide_index=True)
