import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="auto")

html_code = """
<div class='tableauPlaceholder' id='viz'>
    <iframe
        src='https://public.tableau.com/views/Capstone_proj_17806898204630/Main?:showVizHome=no'
        width='100%'
        height='900'
        frameborder='0'>
    </iframe>
</div>
"""

components.html(html_code, height=950)
