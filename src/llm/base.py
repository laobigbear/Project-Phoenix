from abc import ABC, abstractmethod

class LLM(ABC):
    @abstractmethod
    def __init__(self, api_key):
        self.api_key = api_key

    @abstractmethod
    def chat(self, prompt: str) -> str:
        pass