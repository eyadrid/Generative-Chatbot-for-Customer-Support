import streamlit as st
import requests

API_URL = "http://localhost:8000/api/version1/v1/question"

# Configuration de la page
st.set_page_config(page_title="KYRA Chatbot", layout='wide')
st.title(" KYRA Chatbot")
st.caption("🤖 Your KYRA Assistant: Quick Answers, Anytime, Anywhere!")
st.logo("kyra.png", icon_image="kyra.png")


def handle_userinput(user_question):
    try:
        response = requests.get(API_URL, params={'question': user_question})
        response_data = response.json()

        if 'error' in response_data:
            response_text = f"Error: {response_data['error']}"
        else:
            response_text = response_data['response']

        # Mise à jour du session_state avec les messages de l'utilisateur et du chatbot
        st.session_state.messages.append({"role": "user", "content": user_question})
        st.session_state.messages.append({"role": "assistant", "content": response_text})

        # Affichage des messages mis à jour
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        st.session_state.messages.append({"role": "assistant", "content": error_message})


# Initialize chat history and messages in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "messages" not in st.session_state:
    st.session_state.messages = []

# Saisie de l'utilisateur
user_question = st.chat_input("Ask a question about KYRA")

if user_question:
    handle_userinput(user_question)
