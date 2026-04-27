import streamlit as st

st.set_page_config(
    page_title="Lepidoptera · Identifier",
    layout="wide",
    initial_sidebar_state="collapsed",
)

from theme import inject_styles
from views import about, analysis, predict

inject_styles()

tab_predict, tab_analysis, tab_about = st.tabs(
    ["Identifier", "Analysis", "Dataset"]
)

with tab_predict:
    predict.render()

with tab_analysis:
    analysis.render()

with tab_about:
    about.render()
