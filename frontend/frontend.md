# KYRA Chatbot Frontend

## Description

The frontend of the application is developed using Streamlit, a library that facilitates the creation of interactive and user-friendly web interfaces.

## `handle_userinput` Functionality

The `handle_userinput` function is responsible for managing the questions asked by the user. Here is a detailed description of its operation:

- **Parameter** : `user_question` (type : `str`) - The question posed by the user through the user interface.
- **Functionality** :
  - The function sends a GET request to the backend API, passing the user's question as a parameter.
  - It retrieves the response from the API and checks if the response contains an error.
  - If an error is detected, an error message is displayed to the user. Otherwise, the API's response is shown.
  - The message history, including the user's question and the assistant's response, is updated.
 