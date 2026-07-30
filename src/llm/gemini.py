from google import genai
from src.llm.base import LLM

class GeminiClient(LLM):
    def __init__(self, api_key):
        super().__init__(api_key)
        self._client = genai.Client(api_key=api_key)
        self.chatclient = self._client.chats.create(model="gemini-3.5-flash")

    def chat(self, prompt):
        # Gemini SDK maintain history internally, so we don't need to manage it ourselves.
        return self.chatclient.send_message(prompt).text