import streamlit as st

from streamlit_app.services.api import safe_get


def render() -> None:
    st.subheader("Обзор")
    ok, payload, error = safe_get("/overview")
    if not ok:
        st.warning(f"Backend пока недоступен: {error}")
        return

    metrics = st.columns(4)
    metrics[0].metric("Гипотезы", payload["hypotheses_total"])
    metrics[1].metric("Интервью", payload["interviews_total"])
    metrics[2].metric("Инсайты", payload["insights_total"])
    metrics[3].metric("Сигналы", payload["signals_total"])

    left, right = st.columns(2)

    with left:
        st.markdown("**Распределение гипотез по статусам**")
        by_status = payload.get("hypotheses_by_status", [])
        if by_status:
            st.dataframe(by_status, use_container_width=True, hide_index=True)
        else:
            st.info("Статусов пока нет.")

        st.markdown("**Гипотезы, требующие решения**")
        requiring_decision = payload.get("hypotheses_requiring_decision", [])
        if requiring_decision:
            st.dataframe(requiring_decision, use_container_width=True, hide_index=True)
        else:
            st.success("Нет гипотез, требующих немедленного решения.")

    with right:
        st.markdown("**Последние изменения**")
        latest_changes = payload.get("latest_changes", [])
        if latest_changes:
            st.dataframe(latest_changes, use_container_width=True, hide_index=True)
        else:
            st.info("История изменений пока пуста.")
