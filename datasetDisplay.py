import pandas as pd
import streamlit as st
from soh_model import train

original_df = pd.read_excel("PulseBat Dataset.xlsx")

def render_dataset():
    if "latest_dataset" not in st.session_state:
        st.session_state.latest_dataset = pd.read_excel("PulseBat Dataset.xlsx")
    uploader = st.file_uploader("Upload a new excel file of battery data(Must have the same columns as the original dataset)", type=["xlsx"])
    if uploader is not None:
        xlxs_file = pd.read_excel(uploader)
        if list(original_df.columns) == list(xlxs_file.columns):            #ensure the column order is the same as the original
            xlxs_file = xlxs_file[list(original_df.columns)]
            st.session_state.latest_dataset = xlxs_file
            train(xlxs_file)
    display_dataset(st.session_state.latest_dataset)

def display_dataset(dataset):
    st.write("Applied Dataset:")
    if dataset is not None:
        st.dataframe(dataset)



