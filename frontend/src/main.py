import streamlit as st
import requests
from htmlTemplates import css, bot_template, user_template

API_URL = "http://localhost:8000/api/version1/v1/question"

def handle_userinput(user_question):
    try:
        response = requests.get(API_URL, params={'question': user_question})
        response_data = response.json()
        
        if 'error' in response_data:
            st.write(bot_template.replace("{{MSG}}", response_data['error']), unsafe_allow_html=True)
        else:
            response_text = response_data['response']
            st.session_state.chat_history.append({"content": user_question})
            st.session_state.chat_history.append({"content": response_text})
            
            for i, message in enumerate(st.session_state.chat_history):
                if i % 2 == 0:
                    st.write(user_template.replace("{{MSG}}", message['content']), unsafe_allow_html=True)
                else:
                    st.write(bot_template.replace("{{MSG}}", message['content']), unsafe_allow_html=True)
        
        # Append user's question and bot's response to the session state messages
        st.session_state.messages.append({"role": "user", "content": user_question})
        st.session_state.messages.append({"role": "assistant", "content": response_text})
        
    except Exception as e:
        st.write(bot_template.replace("{{MSG}}", f"An error occurred: {str(e)}"), unsafe_allow_html=True)

st.set_page_config(page_title="KYRA Chatbot")
st.write(css, unsafe_allow_html=True)

# Add buttons to the sidebar
if st.sidebar.button("Login"):
    st.sidebar.write("Login button clicked")
if st.sidebar.button("Sign Up"):
    st.sidebar.write("Sign Up button clicked")

col1, col2 = st.columns([8, 1])
with col1:
    st.title("Kyra Chatbot")
with col2:
    st.image("C://Users/dridi/Desktop/Generative chat/frontend/src/kyra.png", width=100)
st.write(css, unsafe_allow_html=True)

# Initialize chat history and messages in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "messages" not in st.session_state:
    st.session_state.messages = []

user_question = st.chat_input("Ask a question about KYRA")

if user_question:
    handle_userinput(user_question)
