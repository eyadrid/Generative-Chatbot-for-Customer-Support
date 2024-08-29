import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL")

# Configure la page Streamlit avec le titre et une mise en page large
PAGE_TITLE = "KYRA Chatbot"
st.set_page_config(page_title=PAGE_TITLE, layout='wide')

hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
    div[data-testid="stToolbar"] {
        visibility: hidden;
        height: 0%;
        position: fixed;
    }
    div[data-testid="stDecoration"] {
        visibility: hidden;
        height: 0%;
        position: fixed;
    }
    div[data-testid="stStatusWidget"] {
        visibility: hidden;
        height: 0%;
        position: fixed;
    }
    #MainMenu {
        visibility: hidden;
        height: 0%;
    }
    header {
        visibility: hidden;
        height: 0%;
    }
    footer {
        visibility: hidden;
        height: 0%;
    }

</style>

"""
# Applique les styles CSS personnalisés pour masquer certains éléments de l'interface Streamlit
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

#Affiche un message de bienvenue de l'assistant
message = st.chat_message("assistant")
message.write("Hello 👋 ! How can I assist you today?")

def handle_userinput(user_question):
    try:
        response = requests.get(API_URL, params={'question': user_question})
        response_data = response.json()

        if 'error' in response_data:
            response_text = "Un problème est survenu. Veuillez essayer de poser à nouveau votre question."
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

# Crée une zone de saisie pour que l'utilisateur pose une question
user_question = st.chat_input("Ask a question about KYRA")

if user_question:
    handle_userinput(user_question)