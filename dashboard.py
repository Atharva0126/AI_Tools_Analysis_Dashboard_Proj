import streamlit as st

st.set_page_config(layout="wide")

# Inject a full-page iframe that breaks out of Streamlit's container
st.markdown("""
    <style>
        /* Hide all Streamlit UI */
        #root > div:first-child { visibility: hidden; }
        .stApp { background: transparent; }

        /* Full screen overlay iframe */
        .fullscreen-frame {
            position: fixed;
            top: 0; left: 0;
            width: 100vw;
            height: 100vh;
            z-index: 9999;
            border: none;
        }
    </style>

    <iframe
        class="fullscreen-frame"
        src="https://public.tableau.com/views/Capstone_proj_17806898204630/Main?:showVizHome=no&:embed=true&:toolbar=yes&:fullscreen=true"
        allowfullscreen>
    </iframe>
""", unsafe_allow_html=True)
