import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document
from utils.extract_data import DataExtractor
from utils.segment_data import DataSegmenter
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()  


embeddings_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")


urls = [
    "https://kyra-docs.data-tricks.net/docs/documentation/actors",
    "https://kyra-docs.data-tricks.net/docs/documentation/tiers",
    "https://kyra-docs.data-tricks.net/docs/documentation/login"
]


def fetch_and_segment_data():
    all_segments = []
    for url in urls:
        extractor = DataExtractor(url)
        soup = extractor.parse_data()
        segmenter = DataSegmenter(soup)
        segments = segmenter.segment_data()
        all_segments.extend(segments)
   
    document_texts = [" ".join(segment) for segment in all_segments]
    documents = [Document(page_content=text) for text in document_texts]
    return documents


documents = fetch_and_segment_data()
db = FAISS.from_documents(documents, embeddings_model)


genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def get_response(question: str) -> str:
    results = db.similarity_search(question, k=5)
    relevant_segments = [result.page_content for result in results]

    prompt = f"""
    Vous êtes un chatbot de support client pour la plateforme KYRA. Un client a posé la question suivante : "{question}".

    Voici les segments pertinents extraits des documents de la plateforme {relevant_segments}. En utilisant uniquement les informations fournies dans ces segments, reformulez-les pour créer une réponse précise, concise et facile à comprendre sous forme de paragraphe. Assurez-vous que les informations ne soient pas simplement copiées des segments fournis.

    Si la question n'est pas pertinente à la plateforme KYRA, répondez ainsi :
    "Je comprends que vous souhaitez savoir {question}. Cependant, les informations que je possède ne concernent que la plateforme KYRA."

    Si le client vous salue, répondez ainsi :
    "{question} Comment puis-je vous aider aujourd'hui ?"
    """
    response = model.generate_content(prompt)
    return response.text
