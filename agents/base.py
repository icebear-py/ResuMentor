import os
from agno.agent import Agent
from agno.models.deepinfra import DeepInfra
from dotenv import load_dotenv
load_dotenv()

DEEPINFRA_API_KEY = os.getenv("DEEPINFRA_API_KEY")
DEFAULT_MODEL = os.getenv("DEEPINFRA_MODEL", "deepseek-ai/DeepSeek-V3.2-Exp")

def make_agent(name: str, instructions: str, model_name: str = DEFAULT_MODEL):
    model = DeepInfra(
        id=model_name,
        api_key=DEEPINFRA_API_KEY
    )
    return Agent(
        name=name,
        model=model,
        markdown=False,
        instructions=instructions,
        add_history_to_context=False
    )

class BaseAgent:
    def __init__(self, name: str, system_prompt: str, model_name: str = DEFAULT_MODEL):
        self.agent = make_agent(name=name, instructions=system_prompt, model_name=model_name)

    def run(self, user_input: str, **kwargs) -> str:
        try:
            result = self.agent.run(user_input, **kwargs)
            return str(result)
        except Exception as e:
            return f"[Error in {self.agent.name}]: {e}"