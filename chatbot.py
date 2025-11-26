import streamlit as st
from gemini_api import ask_gemini

def render_chatbot():
    memory()
    display_message()
    message_input()

def chatbot_frame():
    st.set_page_config(page_title="Chatbot", layout ="wide")

def memory():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def display_message():
    for message in st.session_state.messages:
        st.chat_message(message["role"]).write(message["content"])

def message_input():
    input_message = st.chat_input("Ask about the battery health...")

    if input_message :
        #save message to message state
        st.session_state.messages.append({"role": "user", "content": input_message})
        #display the message
        st.chat_message("user").write(input_message)

        #loading
        with st.spinner("Predicting SOH...")
            gemini_response = ask_gemini(input_message)
            #pass message to backend
            response = gemini_response

        #display the bot message
        st.session_state.messages.append({"role": "bot", "content" :response})
        st.chat_message("bot").write(response)