import pandas as pd
import streamlit as st

def render_dataset():
    if "latest_dataset" not in st.session_state:
        st.session_state.latest_dataset = pd.read_excel("PulseBat Dataset.xlsx")
    uploader = st.file_uploader("Upload a new excel file of battery data", type=["xlsx"])
    if uploader is not None:
        st.session_state.latest_dataset = pd.read_excel(uploader)
    display_dataset(st.session_state.latest_dataset)

def display_dataset(dataset):
    if dataset is not None:
        st.dataframe(dataset)



