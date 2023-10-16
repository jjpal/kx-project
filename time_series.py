import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

st.title('Time Series Analysis')

DATE_COLUMN = 'date/time'
DATA_URL = (' ')

def load_data(nrows):
    data = pd.read_csv(DATA_URL)
