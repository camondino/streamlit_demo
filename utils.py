import streamlit as st
import numpy as np
import pandas as pd
import base64

def load_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

def load_font(font_family = 'Helvetica Now for Monks', font_weight='normal', file_name='HelveticaNowforMonks'):
    st.markdown(
        f"""
        <style>
            @font-face {{
                font-family: {font_family};
                src: url('apps/src/media/{file_name}.otf');
                src: url('apps/src/media/{file_name}.woff') format('woff');
                font-weight: {font_weight};
            }}
        </style>
        """
    , unsafe_allow_html=True)


def load_logo(file_name):
    with open(file_name, "rb") as f:
        contents = f.read()
        return base64.b64encode(contents).decode("utf-8")