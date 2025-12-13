from langchain_groq import ChatGroq
from src.config.settings import settings
from langchain_openai import ChatOpenAI


def get_open_ai_client(model_name: str) -> ChatOpenAI:
    return ChatOpenAI(
        api_key=settings.OPENAI_API_KEY,
        model=model_name,
    )
