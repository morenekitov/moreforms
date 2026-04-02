import streamlit as st

from streamlit_app.services.api import safe_get


def render() -> None:
    st.subheader("Решения")
    st.caption("На этом этапе решения смотрятся по гипотезам через API. Общий explorer будет расширен на следующем шаге.")
    ok, payload, error = safe_get("/hypotheses")
    if not ok:
        st.error(f"Не удалось загрузить гипотезы: {error}")
        return
    for row in payload[:20]:
        st.write(f"- **{row['title']}** — текущий статус `{row['status']}`")
