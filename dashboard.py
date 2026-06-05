import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# Remove Streamlit's default padding
st.markdown("""
    <style>
        .block-container {
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
        .stApp {
            margin: 0;
        }
        iframe {
            display: block;
        }
    </style>
""", unsafe_allow_html=True)

html_code = """
<style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { overflow: hidden; }
    .tableau-container {
        width: 100vw;
        height: 100vh;
    }
    iframe {
        width: 100%;
        height: 100%;
        border: none;
        display: block;
    }
</style>
<div class='tableau-container'>
    <iframe
        src='https://public.tableau.com/views/Capstone_proj_17806898204630/Main?:showVizHome=no&:embed=true&:toolbar=no'
        allowfullscreen>
    </iframe>
</div>
"""

components.html(html_code, height=950, scrolling=False)
