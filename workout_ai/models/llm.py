import os

from langchain_openai.chat_models import ChatOpenAI
from enum import Enum

class LLMModels(str, Enum):
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_4 = "gpt-4"
    GPT_4_TURBO = "gpt-4-turbo"

class LLM:
    def __init__(self, model: LLMModels = LLMModels.GPT_4, temperature: float = 0.7):
        self.model = model
        self.temperature = temperature

    def get_llm(self):
        if self.model.startswith("gpt"):
            return ChatOpenAI(
                model=self.model,
                temperature=self.temperature,
                openai_api_key=os.getenv("OPENAI_API_KEY"),
            )

class WorkoutPlannerLLM:
    def __init__(self, model: str = "gpt-4", temperature: float = 0.7):
        self.llm = LLM(model=model, temperature=temperature).get_llm()

class NutritionPlannerLLM:
    def __init__(self, model: str = "gpt-4", temperature: float = 0.7):
        self.llm = LLM(model=model, temperature=temperature).get_llm()