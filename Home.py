# Import Custom Module
import pathlib
from pathlib import Path
import sys
sys.path.append(str(pathlib.Path().absolute()).split("/src")[0] + "/src")
import streamlit as st
import base64
from utils import load_css, load_logo

###### Page Format ######
st.set_page_config(
    page_title="Jobs in Libano",
    page_icon="\U0001f9d1\u200D\U0001f393",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
load_css("style.css")


###### Sidebar information ######
with st.sidebar:
    st.markdown(
        f"""
        <div class="center">
            Made in &#x1F1E6;&#x1F1F7; with &#x1F60D; by Carolina
        """,
        unsafe_allow_html=True
    )
    st.title("About")
    st.info(
            "🎈 **BETA:** This app is pushed through Github, please contact us for more details"
        )


###### Home Page ######

st.write("# Welcome to the Job App!👋")

st.markdown("""
## Home
This app has four pages. Use the Navigation menu on the left side bar to switch page.
- **Home:** App information and overview
- **Visualizations** Exploration of the raw dataset

## Development
- **Framework:** [Streamlit](https://streamlit.io/) an open-source python framework for building web apps for Machine Learning and Data Science
- **Source Code:** [Github]()
""", 
unsafe_allow_html=True)

