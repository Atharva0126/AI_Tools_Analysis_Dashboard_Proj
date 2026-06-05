import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Global Semiconductor Industry Dashboard",
    layout="wide"
)

st.title("📊 Global Semiconductor Industry Analysis Dashboard")

tableau_url = (
    "https://public.tableau.com/views/"
    "Capstone_proj_17806898204630/Main?:showVizHome=no"
)

components.iframe(
    src=tableau_url,
    width=1400,
    height=900,
    scrolling=True
)
