import os
from dotenv import load_dotenv

load_dotenv()

class Settings():

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
    MODELS = ["gpt-5", "gpt-5-mini", "gpt-4o", "gpt-4-turbo", "llama-3.1-8b-instant",
              "llama-3.3-70b-versatile"]
    MODEL_NAME = "llama-3.1-8b-instant"
    
    TEMPERATURE = 0.9

    MAX_RETRIES = 3


settings = Settings()  