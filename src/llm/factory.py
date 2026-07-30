import os
from dotenv import load_dotenv
from src.llm.gemini import GeminiClient
class LLMFactory:
    @staticmethod
    def create(provider: str):
        if provider == "gemini":
            load_dotenv()  # Load environment variables from .env file
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                raise ValueError("未找到 GEMINI_API_KEY，請確認 .env 設定！")
            return GeminiClient(api_key)

        raise ValueError(f"Unsupported provider: {provider}")