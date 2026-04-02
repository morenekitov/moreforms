import pandas as pd
import streamlit as st


def show_table(rows: list[dict], empty_message: str) -> None:
    if not rows:
        st.info(empty_message)
        return
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)


def to_frame(rows: list[dict]) -> pd.DataFrame:
    if not rows:
        return pd.DataFrame()
    return pd.DataFrame(rows)
