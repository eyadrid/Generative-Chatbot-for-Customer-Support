import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")
LOGO_PATH = os.getenv("LOGO_PATH")

PAGE_TITLE = "KYRA Chatbot"
CAPTION = "🤖 Your KYRA Assistant: Quick Answers, Anytime, Anywhere!"
ERROR_MESSAGE = "An error occurred: {error}"

st.set_page_config(page_title=PAGE_TITLE, layout='wide')
st.title(PAGE_TITLE)
st.caption(CAPTION)
st.logo(LOGO_PATH) 

def handle_userinput(user_question):
    try:
        response = requests.get(API_URL, params={'question': user_question})
        response_data = response.json()

        if 'error' in response_data:
            response_text = f"Error: {response_data['error']}"
        else:
            response_text = response_data['response']

        st.session_state.messages.append({"role": "user", "content": user_question})
        st.session_state.messages.append({"role": "assistant", "content": response_text})

        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])
    except Exception:
        error_message = "Un problème est survenu. Veuillez essayer de poser à nouveau votre question."
        st.session_state.messages.append({"role": "assistant", "content": error_message})

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "messages" not in st.session_state:
    st.session_state.messages = []

user_question = st.chat_input("Ask a question about KYRA")

if user_question:
    handle_userinput(user_question)
