import streamlit as st
import pandas as pd
from chatbot import render_chatbot
from datasetDisplay import render_dataset

def render_ui():
    st.title("Battery Health Chatbot")
    nav_bar()

def nav_bar():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to:", ["Chatbot","Dataset"])

    if page == "Chatbot":
        render_chatbot()
    elif page == "Dataset":
        render_dataset()

if __name__ == "__main__":
    render_ui()



