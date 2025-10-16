from agents.base import BaseAgent
from prompts import prompts

class TutorAgent(BaseAgent):
    def __init__(self):
        super().__init__("TutorAgent", prompts.CHATBOT_PROMPT)

    def chat(self, msg: str, memory: dict) -> str:
        result = self.agent.run(msg, memory=memory)
        raw_output = str(result.content)
        
        return raw_output.strip()