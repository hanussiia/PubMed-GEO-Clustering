from extract import Extractor
import streamlit as st
import pandas as pd
from io import StringIO


e = Extractor()

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    e.exe_file(uploaded_file)



