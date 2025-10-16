from fastapi import APIRouter, Form
from agents.pathgenerator_agent import CoachAgent
from app.state import sessions, SESSION_TTL_SECONDS
from datetime import datetime
from pydantic import BaseModel, Field
from typing import  List
import json

router = APIRouter()
agent = CoachAgent()

def check(session_id: str):
    if session_id not in sessions:
        return {"error": "Invalid session ID"}
    if (datetime.utcnow() - sessions[session_id]["created"]).total_seconds() > SESSION_TTL_SECONDS:
        del sessions[session_id]
        return {"error": "Session expired"}
    return None

@router.post("/")
async def generate_plan(session_id: str = Form(...), gaps: str = Form(...), missing_required_skills: str = Form(...), missing_preferred_skills: str = Form(...)):
    err = check(session_id)
    if err:
        return err

    gaps_list = [g.strip() for g in gaps.split(",") if g.strip()]
    missing_required_skills = [g.strip() for g in missing_required_skills.split(",") if g.strip()]
    missing_preferred_skills = [g.strip() for g in missing_preferred_skills.split(",") if g.strip()]
    memory = sessions[session_id]["memory"]

    output = agent.create_plan(gaps_list,missing_required_skills,missing_preferred_skills, memory)
    sessions[session_id]["memory"] = memory

    return {"session_id": session_id, "learning_plan": output}