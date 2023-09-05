############################################################ SETUP ############################################################

############################################################ Imports

import os
import sys
import io
import streamlit as st
import streamlit.components.v1 as components
from annotated_text import annotated_text
from streamlit_extras.switch_page_button import switch_page
import webbrowser
import requests

import math
import pandas as pd
import numpy as np
import json
import random
import re
from collections import Counter

############################################################ Settings

# optional celebratory balloons
balloons = True

st.set_page_config(layout="centered")
c_green = "#AD9"
c_red = "#FA9"

# hides page nav in sidebar
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {pointer-events: none; cursor: default;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)

# hides button to close sidebar, open settings
no_button_style = """
    <style>
        button[kind="header"] {display:none;}
    </style>
"""
st.markdown(no_button_style, unsafe_allow_html=True)

# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

############################################################ Public variables

############################################################ Public functions

def redirect(_url):
	link = ''
	st.markdown(link, unsafe_allow_html=True)


############################################################ MAIN ############################################################

try:
	df = st.session_state.data
	df_full = st.session_state.data_full
	data_path = os.path.join(st.session_state.project_path, "sample.csv")
	group = st.session_state.group
	filename = st.session_state.filename
	state_num = st.session_state.state_num
	student_num = st.session_state.student_num
	indexes = st.session_state.indexes
except:
    switch_page("Home")


st.markdown("Thank you for participating in our study!")

st.write("---")

st.write('You should be redirected back to Prolific in a new tab. If this has not happened, please click <a href="https://app.prolific.co/submissions/complete?cc=C13E0WG5">HERE</a>')

webbrowser.open('https://app.prolific.co/submissions/complete?cc=C13E0WG5')

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}
</style>
<p><a href="https://hai.uni-bremen.de/Imprint" target="_blank">Imprint</a> | <a href="https://www.uni-bremen.de/en/data-privacy" target="_blank">Privacy Policy</a></p>
"""
st.write(footer,unsafe_allow_html=True)


