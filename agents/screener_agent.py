import json
from agents.base import BaseAgent
from prompts import prompts

class ScreenerAgent(BaseAgent):
    def __init__(self):
        super().__init__("ScreenerAgent", prompts.SCREENING_PROMPT)

    def analyze(self, job_description: str, resume_text: str, memory: dict) -> dict:
        user_input = f"Job Description:\n{job_description}\n\nCandidate Resume:\n{resume_text}\n\nEvaluate now."
        result = self.agent.run(user_input, memory=memory)
        raw_output = str(result.content)

        if raw_output.startswith('```json'):
            raw_output = raw_output[7:]
        if raw_output.startswith('```'):
            raw_output = raw_output[3:]
        if raw_output.endswith('```'):
            raw_output = raw_output[:-3]
        raw_output = raw_output.strip()
        try:
            return json.loads(raw_output)
        except Exception:
            return {"error": "Invalid JSON output", "raw_output": raw_output}