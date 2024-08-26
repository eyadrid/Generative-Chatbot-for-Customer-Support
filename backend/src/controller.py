from fastapi import APIRouter
from service import get_response

router = APIRouter()

@router.get("/api/v1/question")
def generate_response(question: str):
    try:
        response_text = get_response(question)
        return {"response": response_text}
    except Exception as e:
        return {"error": f"Sorry, couldn't process the request: {str(e)}"}
