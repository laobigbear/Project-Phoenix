from openai import OpenAI
from src.llm.base import LLM
class CHATGPTClient(LLM):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.message_history = []
        self._client = OpenAI(api_key=self.api_key)

    def chat(self, prompt):
        self.message_history.append({"role": "user", "content": prompt})
        response = self._client.chat.completions.create(
            model="gpt-4o-mini",
            messages=self.message_history
        )
        self.message_history.append({"role": "assistant", "content": response.choices[0].message.content})
        return response.choices[0].message.content