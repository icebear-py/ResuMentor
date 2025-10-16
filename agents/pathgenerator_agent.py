import json
from agents.base import BaseAgent
from prompts import prompts
from utils.youtube_resource_finder import search_youtube_resources

class CoachAgent(BaseAgent):
    def __init__(self):
        super().__init__("CoachAgent", prompts.LEARNING_PATH_PROMPT)

    def create_plan(self, gaps: list[str],missing_required_skills: list[str],missing_preferred_skills: list[str], memory: dict) -> dict:
        user_input = f"Gaps: {', '.join(gaps)}. Missing required skills: {', '.join(missing_required_skills)}. Missing preferred skills:{', '.join(missing_preferred_skills)}  Create a 7-day learning plan."
        result = self.agent.run(user_input, memory=memory)
        raw_output = str(result.content)
        
        if raw_output.startswith('```json'):
            raw_output = raw_output[7:]
        if raw_output.startswith('```'):
            raw_output = raw_output[3:]
        if raw_output.endswith('```'):
            raw_output = raw_output[:-3]
        plan = json.loads(raw_output.strip())

        for day in plan.get("days", []):
            search_list = day.get("resources_to_find", [])
            if "resources" not in day:
                day["resources"] = []
            
            try:
                for query in search_list:
                    yt_data = search_youtube_resources(query)
                    day["resources"].append(yt_data)
            except Exception as e:
                day["resources"].append(f"[Error fetching resources: {e}]")

        try:
            return plan
        except Exception:
            return {"error": "Invalid JSON output", "raw_output": raw_output}