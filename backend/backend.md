# KYRA Chatbot Backend

## Description

The backend of the KYRA Chatbot application handles data extraction, segmentation, and response generation. It utilizes various libraries and services to ensure accurate and relevant answers to user queries about the KYRA platform. 


## `fetch_and_segment_data` Functionality

The `fetch_and_segment_data` function is designed to extract and segment information from specified URLs. Here is a detailed description of its operation:

- **Functionality**:
  - **Fetch Data**: It retrieves data from a predefined list of URLs containing documentation related to the KYRA platform.
  - **Parse Data**: For each URL, the function uses a `DataExtractor` to parse the HTML content.
  - **Segment Data**: The parsed data is then segmented into manageable pieces using a `DataSegmenter`.
  - **Create Documents**: The segmented data is combined into text documents and converted into `Document` objects.
  - **Return Documents**: The function returns a list of `Document` objects that represent the segmented content from all the URLs.

## `get_response` Functionality

The `get_response` function generates responses based on user questions by leveraging the indexed document database and a Generative AI model. Here is a detailed description of its operation:

- **Parameters**:
  - **question** (type: `str`) - The question asked by the user, which will be processed to generate a relevant response.

- **Functionality**:
  - **Similarity Search**: The function performs a similarity search on the question to find the most relevant segments from the indexed documents.
  - **Language Detection**: It detects the language of the question to generate a response in the same language.
  - **Greeting Responses**: For common greetings (e.g., "bonjour", "hi"), it provides a predefined greeting response.
  - **Generate Response**:
    - **French Questions**: Constructs a prompt in French to be used with the Generative AI model to generate a response.
    - **English Questions**: Constructs a prompt in English for response generation.
    - **Non-KYRA Questions**: If the question is not related to the KYRA platform, it responds with a standard message indicating the information is limited to KYRA.
  - **Return Response**: The function returns the generated response based on the processed information.

## Technologies Used

- **FastAPI**: The web framework used for building the API.
- **FAISS**: A vector database for efficient similarity search and retrieval.
- **Hugging Face Embeddings**: `sentence-transformers/all-mpnet-base-v2` model for generating embeddings.
- **Generative AI Model**: `gemini-1.5-flash` for generating responses based on the provided prompts.