import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Category Analysis Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Category Analysis Dashboard")
st.markdown("Interactive Tableau Dashboard")

tableau_url = "https://public.tableau.com/views/Capstone_proj_17806898204630/CategoryAnalysis?:showVizHome=no"

components.iframe(
    tableau_url,
    height=900,
    width=1200,
    scrolling=True
)
