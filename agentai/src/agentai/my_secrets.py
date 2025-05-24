import os
from dotenv import load_dotenv

load_dotenv()  # Loads .env

class Secrets:
    def __init__(self):
        self.gemini_api_key = os.getenv("GEMINI_API_KEY")
        self.gemini_api_url = os.getenv("GEMINI_API_URL")
        self.gemini_api_model = os.getenv("GEMINI_API_MODEL")

        # Sanity check
        if not self.gemini_api_key:
            raise Exception("Missing GEMINI_API_KEY")
        if not self.gemini_api_url:
            raise Exception("Missing GEMINI_API_URL")
        if not self.gemini_api_model:
            raise Exception("Missing GEMINI_API_MODEL")
