from fastapi import APIRouter, UploadFile, Form
from agents.screener_agent import ScreenerAgent
from utils.resume_parser import parse_resume
from app.state import sessions, SESSION_TTL_SECONDS
from datetime import datetime
from pydantic import BaseModel, Field
import tempfile
import shutil
import json
import os

router = APIRouter()
agent = ScreenerAgent()

def check(session_id: str):
    if session_id not in sessions:
        return {"error": "Invalid session ID"}
    if (datetime.utcnow() - sessions[session_id]["created"]).total_seconds() > SESSION_TTL_SECONDS:
        del sessions[session_id]
        return {"error": "Session expired"}
    return None

@router.post("/")
async def screen_resume(session_id: str = Form(...), job_description: str = Form(...), resume_file: UploadFile = None):
    err = check(session_id)
    if err:
        return err
    if not resume_file:
        return {"error": "No resume file provided"}

    temp_path = tempfile.mktemp(suffix=resume_file.filename)
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(resume_file.file, buffer)

    try:
        parsed_resume = parse_resume(temp_path)
        memory = sessions[session_id]["memory"]

        output = agent.analyze(job_description, parsed_resume, memory)

        sessions[session_id]["memory"] = memory

        return {"session_id": session_id, "screen_result": output}
    finally:
        if os.path.exists(temp_path):
            os.unlink(temp_path)