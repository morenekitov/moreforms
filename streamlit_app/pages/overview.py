import streamlit as st

from streamlit_app.services.api import safe_get


def render() -> None:
    st.subheader("Обзор")
    endpoints = {
        "Гипотезы": "/hypotheses",
        "Интервью": "/interviews",
        "Инсайты": "/insights",
        "Сигналы": "/signals",
        "Конкуренты": "/competitors",
    }

    columns = st.columns(len(endpoints))
    for idx, (label, path) in enumerate(endpoints.items()):
        ok, payload, _ = safe_get(path)
        value = len(payload) if ok and isinstance(payload, list) else "—"
        columns[idx].metric(label, value)

    ok, payload, error = safe_get("/hypotheses")
    if not ok:
        st.warning(f"Backend пока недоступен: {error}")
        return

    needs_attention = [item for item in payload if item.get("status") in {"new", "queued", "signal"}]
    st.caption("Гипотезы, которым требуется решение или следующий шаг")
    if needs_attention:
        for row in needs_attention[:10]:
            st.write(f"- **{row['title']}** — статус `{row['status']}`")
    else:
        st.success("Нет гипотез, требующих немедленного решения.")
