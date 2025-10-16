from fastapi import APIRouter, Form
from agents.chatbot_agent import TutorAgent
from app.state import sessions, SESSION_TTL_SECONDS
from datetime import datetime
from pydantic import BaseModel, Field

router = APIRouter()
agent = TutorAgent()

def check(session_id: str):
    if session_id not in sessions:
        return {"error": "Invalid session ID"}
    if (datetime.utcnow() - sessions[session_id]["created"]).total_seconds() > SESSION_TTL_SECONDS:
        del sessions[session_id]
        return {"error": "Session expired"}
    return None

@router.post("/")
async def chat_with_tutor(session_id: str = Form(...), msg: str = Form(...)):
    err = check(session_id)
    if err:
        return err
    memory = sessions[session_id]["memory"]
    result = agent.chat(msg, memory=memory)
    sessions[session_id]["memory"] = memory

    return {"session_id": session_id, "reply": str(result)}