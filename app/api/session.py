from fastapi import APIRouter
import uuid
from datetime import datetime, timedelta
from app.state import sessions, SESSION_TTL_SECONDS

router = APIRouter()

def cleanup():
    now = datetime.utcnow()
    expired = [sid for sid, data in sessions.items() if (now - data["created"]).total_seconds() > SESSION_TTL_SECONDS]
    for sid in expired:
        del sessions[sid]

@router.post("/")
def create_session():
    cleanup()
    session_id = str(uuid.uuid4())
    sessions[session_id] = {"created": datetime.utcnow(), "memory": {}}
    return {"session_id": session_id, "message": "Session created", "ttl_seconds": SESSION_TTL_SECONDS}